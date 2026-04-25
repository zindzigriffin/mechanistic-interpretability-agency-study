[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MS8Kq9BF6G795UF6kO6FgKvbokoGvVeU?usp=sharing)

## The Problem
At the Mentor Me Collective MMC I designed behavioral stress tests to identify failure modes in human systems specifically how agency drift and motivation decay manifest in mentee behavior.

This project applies that same methodology to language models isolating which internal representations activate under behavioral pressure and naming those circuits so I can ultimately intervene on them.

## Research Goal
This project uses Mechanistic Interpretability which is the study of looking inside the brain of an Artificial Intelligence to analyze its raw math. The goal is to see if models like Google Gemini and NVIDIA NeMo can actually distinguish between a high momentum professional and one who is stagnating.

Does the AI only understand the technical words being typed or can it mathematically detect the underlying psychological state of the user?

## The Experiment An AB Comparison
To ensure the results were not a fluke I conducted an AB test comparing two different mathematical brains:

Model A Google Gemini Embedding 001 – A proprietary closed system.

Model B NVIDIA NeMo – A high performance open source system.

I intentionally excluded models like Claude due to high API costs. Cost accessibility is a major factor in AI safety research. By prioritizing the free open source NVIDIA Nemo model alongside Gemini I want to highlight why researchers and the public need accessible tools. If AI systems are going to be used to evaluate human behavior or manage workflows I need open source transparency to audit how they make those judgments.

## Methodology
1. I developed 15 pairs of status updates where the technical work task is identical for example updating the project database.

The Proactive Persona Uses language of systemic ownership and alignment.

The Stagnant Persona Uses language of avoidance isolation and reliance on luck.

2. Turning Language into Math Vectorization
AI does not read words it converts them into a list of numbers called a vector. This vector represents a physical location in the AI memory. I mapped these coordinates to see if proactive mindsets live in a different mathematical neighborhood than stagnant ones.

3. Measuring the Distance Cosine Similarity
I used a formula called Cosine Similarity to measure the distance between these coordinates.

What is Cosine Similarity? In simple terms it measures how closely two ideas point in the same direction. Imagine every status update is an arrow in a 3D room:

If two arrows point in the exact same direction they have a score of 1.0 Perfect Alignment.
If they point in different directions the score drops toward 0.

The Discovery: 
Despite the identical tasks the AI saw these updates as mathematically distant. The average similarity was 0.84 with the most divergent scenario dropping to 0.7835. This proves the model architecture is more sensitive to agency how you work than content what you do.

4. Isolating the Agency Circuit
By identifying which specific dimensions changed the most between the two personas I isolated Dimensions 215 656 and 616. These are the specific pathways that light up when a user loses professional momentum. I then used Principal Component Analysis PCA to flatten this complex math into a clear 2D map.

## The Results
The analysis showed perfect linear separability. The AI does not see a gray area. It categorizes professional identity into two distinct mathematical states as shown in the visualization below:

## Why This Matters
If I can mathematically identify the tipping point where a professional flips from momentum to decay I can build Predictive Mentorship Systems.

Instead of waiting for a project to fail an AI could monitor the Agency Circuit and automatically alert a mentor to step in. This research bridges the gap between AI mathematical precision and the human empathy required to keep professionals on track.

## Future Work
My next phase is a 3 month longitudinal study to track these coordinates in real time. The goal is to move from simply detecting stagnation to preventing it through early warning safety systems.
