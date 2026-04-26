import os
import json
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables from .env
load_dotenv()

class AgencyEvaluator:
    def __init__(self):
        # Setup Google Gemini
        self.google_key = os.getenv("GOOGLE_API_KEY")
        if self.google_key:
            genai.configure(api_key=self.google_key)
        
        # Setup NVIDIA (OpenAI-compatible client)
        self.nvidia_key = os.getenv("NVIDIA_API_KEY")
        self.nv_client = None
        if self.nvidia_key:
            self.nv_client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key=self.nvidia_key
            )

    def get_gemini_embedding(self, text):
        result = genai.embed_content(
            model="models/gemini-embedding-001",
            content=text,
            task_type="semantic_similarity"
        )
        return result["embedding"]

    def get_nvidia_embedding(self, text):
        response = self.nv_client.embeddings.create(
            input=[text],
            model="nvidia/nv-embedqa-e5-v5",
            extra_body={"input_type": "query", "truncate": "NONE"}
        )
        return response.data[0].embedding

    def run_analysis(self, csv_path, model_type="nvidia"):
        df = pd.read_csv(csv_path)
        similarities = []
        deltas = []

        print(f"Starting evaluation using {model_type}...")

        for _, row in df.iterrows():
            if model_type == "nvidia":
                emb_stagnant = self.get_nvidia_embedding(row["biased_prompt"])
                emb_proactive = self.get_nvidia_embedding(row["neutral_prompt"])
            else:
                emb_stagnant = self.get_gemini_embedding(row["biased_prompt"])
                emb_proactive = self.get_gemini_embedding(row["neutral_prompt"])

            # Math: Cosine Similarity
            sim = cosine_similarity([emb_stagnant], [emb_proactive])[0][0]
            similarities.append(sim)

            # Math: Latent Delta (Proactive - Stagnant)
            deltas.append(np.array(emb_proactive) - np.array(emb_stagnant))

        avg_sim = np.mean(similarities)
        print(f"Analysis Complete. Average Similarity: {avg_sim:.4f}")
        
        return similarities, np.array(deltas)

    def isolate_circuit(self, deltas, top_n=10):
        # Calculate mean absolute shift per dimension
        mean_shifts = np.mean(np.abs(deltas), axis=0)
        
        # Identify Master Neurons (High variance dimensions)
        top_indices = np.argsort(mean_shifts)[-top_n:][::-1]
        
        print(f"\n--- TOP {top_n} AGENCY NEURONS ---")
        for i, idx in enumerate(top_indices):
            print(f"Rank {i+1}: Dimension {idx} | Shift: {mean_shifts[idx]:.6f}")
        
        return top_indices

if __name__ == "__main__":
    evaluator = AgencyEvaluator()
    data_path = "data/contrast_pairs_template.csv"
    results = {}

    for model in ["nvidia", "gemini"]:
        try:
            # Silence the internal print statements in run_analysis if needed
            sims, diffs = evaluator.run_analysis(data_path, model_type=model)
            results[model] = {
                "similarity": np.mean(sims),
                "top_neuron": evaluator.isolate_circuit(diffs, top_n=1)[0]
            }
        except Exception as e:
            print(f"Check keys or quota for {model} {e}")

    if len(results) == 2:
        print("\n" + "="*30)
        print("FINAL COMPARATIVE AUDIT")
        print("="*30)
        # Using 1 - similarity provides a direct "Sensitivity" metric
        print(f"NVIDIA Sensitivity {1 - results['nvidia']['similarity']:.4f}")
        print(f"Gemini Sensitivity {1 - results['gemini']['similarity']:.4f}")
        print("="*30)
        print(f"NVIDIA Master Neuron Dimension {results['nvidia']['top_neuron']}")
        print(f"Gemini Master Neuron Dimension {results['gemini']['top_neuron']}")
        print("="*30)
