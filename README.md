[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MS8Kq9BF6G795UF6kO6FgKvbokoGvVeU?usp=sharing)

Agency Circuit Evaluator: Mechanistic Interpretability for Behavioral Drift Detection 

A contrastive text classification framework for auditing how AI models represent psychological states in their latent space 

Can an AI mathematically detect when a person is losing momentum before they even realize it themselves? 

### What This Is 
At its core this is a contrastive text classification study not of model outputs but of internal representations. The question is not what the model says. It is whether the latent space of the model encodes the difference between two psychological states at all and if so which specific dimensions are responsible.

This repository contains: 
* A research notebook notebooks/agency_circuit_analysis.ipynb walking through the full analysis visualizations and findings.
* A reusable evaluation script src/agency_evaluator.py that any researcher can run against their own model and their own behavioral contrast pairs.
* A template CSV data/contrast_pairs_template.csv so you can swap in your own use case in minutes.

To run this on your own model:

git clone https://github.com/zindzigriffin/agency_circuit_evaluator
cd agency_circuit_evaluator
pip install requirements.txt
cp .env.example .env
python src/agency_evaluator.py

### Repository Structure 

agency_circuit_evaluator/
README.md
notebooks/
   agency_circuit_analysis.ipynb
src/
   agency_evaluator.py
data/
   contrast_pairs_template.csv
requirements.txt
.env.example

### Why This Research Exists 
Every year millions of professionals quietly disengage not dramatically not all at once but through subtle behavioral shifts: language that hedges instead of commits updates that report tasks instead of driving outcomes a slow drift from ownership to passivity. Human mentors can sometimes sense this. But they cannot scale.

AI systems are increasingly being used to evaluate professionals screening resumes scoring interview responses flagging at risk employees. Yet we have almost no scientific understanding of what these models are actually measuring inside. Are they reading the words you type or are they detecting something deeper about your psychological state? And if they are making these judgments can we audit them? 

### The Core Problem with AI Evaluation 
When we deploy AI models to assess human behavior we make a hidden assumption: that the model understands the meaning of what a person is communicating not just the surface pattern of words. That assumption has never been rigorously tested.

Two professionals can submit status updates describing identical tasks. One writes from a place of momentum and agency. The other writes from a place of avoidance and stagnation. Do AI models see a difference? And if so where in their mathematical architecture does that difference live? Without answering this we are building evaluation systems on an unexamined foundation. This is an AI safety problem.

### What This Research Does 
This project applies Mechanistic Interpretability the practice of reverse engineering the internal mathematics of AI models to a domain that has never been studied through this lens: professional agency and behavioral drift.

Rather than treating AI models as black boxes that produce outputs this research opens them up and asks: Which specific mathematical dimensions activate when a model processes a stagnating professional versus a high momentum one? Is that circuit consistent? Can it be measured named and intervened upon? 

This is embedding based contrastive text classification with circuit level attribution. Two classes of text proactive vs stagnant are converted to vector representations and the research measures whether those classes are linearly separable in the latent space of the model. The methodology then identifies exactly which dimensions are driving the classification boundary.

### The Methodology 
I developed 15 contrastive pairs of professional status updates. Each pair describes the exact same technical task but written through two distinct psychological frames: 

* **The Proactive Persona:** language of systemic ownership forward momentum and alignment.
* **The Stagnant Persona:** language of avoidance isolation and passivity.

These pairs are stored in data/contrast_pairs_template.csv and are fully swappable researchers can substitute any two behavioral or psychological states relevant to their domain. These were then run through two distinct AI architectures to see how each model represents the difference mathematically.

### The A/B Test: Google Gemini vs NVIDIA NeMo 

| Metric | Google Gemini | NVIDIA NeMo |
| :--- | :--- | :--- |
| **Average Cosine Similarity** | 0.8400 | 0.5683 |
| **Behavioral Sensitivity** | Baseline | 32.3% Higher |
| **Model Representation** | Minor tone shift | Distinct behavioral states |

Cosine Similarity measures how closely two ideas point in the same mathematical direction. A score of 1.0 means the model treats two inputs as nearly identical. A lower score means the model sees a meaningful conceptual gap.

The finding: Gemini compresses proactive and stagnant updates into the same general neighborhood it sees professional communication not behavioral divergence. The architecture of NVIDIA preserves a dramatically wider conceptual gap treating agency and stagnation as mathematically distinct states.

### Isolating the Agency Circuit 
By identifying which specific mathematical dimensions shift most dramatically between the proactive and stagnant personas I isolated what I call the Agency Circuit: a cluster of approximately 40 dimensions roughly 4 percent of the 1024 dimension latent space of NVIDIA that functions as a dedicated detector for behavioral momentum.

The Master Neuron Dimension 927 emerged as the primary driver showing a delta 2.5x higher than mean dimensional variance across the full space. Dimensions 215 656 and 616 formed supporting nodes in this circuit. Using Principal Component Analysis PCA I projected this high dimensional space into a 2D map. The result: perfect linear separability. The model does not see a gray area between momentum and stagnation. It categorizes professional identity into two mathematically distinct states.

### Why A/B Testing AI Models Matters for Safety 
Most AI evaluation focuses on what models say. This research focuses on what models know and whether two architectures making the same downstream judgment are doing so for the same internal reasons.

1. **Deployment decisions should not be architecture agnostic.** The model you choose determines what behavioral signals you can actually detect.
2. **Auditing requires opening the box.** If an AI flags someone as at risk we need to be able to trace which internal circuit made that call.
3. **Access to evaluation tools must be equitable.** By centering the open weight NeMo model of NVIDIA alongside the free tier of Gemini this research demonstrates rigorous interpretability work within real world resource constraints.

### The Practical Application: Predictive Mentorship 
This research was directly informed by work at Mentor Me Collective where I previously designed behavioral stress tests to identify failure modes in human mentorship systems specifically how motivation decay and agency drift manifest in mentee behavior.

This project applies that same diagnostic methodology to language models. The immediate application: a Stagnation Threshold calibrated at a cosine similarity of 0.56 using the NVIDIA benchmark that allows mentorship systems to monitor professional agency in real time and trigger proactive interventions.

### What Is Next 
The current phase establishes the circuit architecture and baseline measurements. The next phase is a 3 month longitudinal study tracking these dimensional coordinates in real time across active professionals moving from detecting stagnation to predicting it before it fully manifests. 

### Tech Stack 

| Layer | Tools |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Embeddings** | Google Generative AI SDK and NVIDIA NeMo via AI Endpoints |
| **Analysis** | NumPy and scikit learn |
| **Visualization** | Matplotlib |
| **Notebook** | Jupyter |
| **Config** | python dotenv |

### About the Researcher 
Zindzi Griffin is an applied ML researcher and community builder working at the intersection of behavioral science AI safety and human development. This project reflects a core belief: that understanding how AI models represent human states not just what they output is foundational work for building systems that are genuinely safe auditable and beneficial.
