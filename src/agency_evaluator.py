import os
import json
import numpy as np
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity

class AgencyEvaluator:
    def __init__(self, api_key=None):
        """Initializes the Gemini API and configuration."""
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("API Key not found. Please set GOOGLE_API_KEY environment variable.")
        
        genai.configure(api_key=self.api_key)
        self.model_name = "models/gemini-embedding-001"

    def get_embedding(self, text):
        """Extracts embeddings using the gemini-embedding-001 model."""
        result = genai.embed_content(
            model=self.model_name,
            content=text,
            task_type="SEMANTIC_SIMILARITY"
        )
        return result['embedding']

    def evaluate_dataset(self, file_path):
        """Processes a JSON dataset to compute similarities and difference vectors."""
        with open(file_path, 'r') as f:
            dataset = json.load(f)

        records = []
        print(f"Found {len(dataset)} pairs. Starting extraction...")

        for pair in dataset:
            try:
                biased_emb = self.get_embedding(pair['biased_prompt'])
                neutral_emb = self.get_embedding(pair['neutral_prompt'])

                # Compute Cosine Similarity
                sim = cosine_similarity([biased_emb], [neutral_emb])[0][0]

                records.append({
                    'id': pair.get('id'),
                    'category': pair.get('bias_category'),
                    'similarity': sim,
                    'diff_vector': np.array(biased_emb) - np.array(neutral_emb)
                })
            except Exception as e:
                print(f"Error processing pair {pair.get('id')}: {e}")

        return records

    def identify_circuits(self, records, top_n=20):
        """Identifies the most activated dimensions (the 'Agency Circuit')."""
        diff_matrix = np.array([r['diff_vector'] for r in records])
        mean_abs_diff = np.mean(np.abs(diff_matrix), axis=0)
        top_dimensions = np.argsort(mean_abs_diff)[-top_n:][::-1]
        return top_dimensions

if __name__ == "__main__":
    # Example usage
    evaluator = AgencyEvaluator()
    results = evaluator.evaluate_dataset('data/agency_bias_dataset.json')
    
    for res in results:
        print(f"ID {res['id']} [{res['category']}]: Similarity = {res['similarity']:.4f}")
    
    circuits = evaluator.identify_circuits(results)
    print(f"\nTop 20 Circuit Dimensions: {circuits}")
