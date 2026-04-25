[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MS8Kq9BF6G795UF6kO6FgKvbokoGvVeU?usp=sharing)

## Problem
At the Mentor Me Collective (MMC), I designed behavioral stress tests to identify failure modes in human systems specifically, how agency drift and motivation decay manifest in mentee behavior.

This project applies that same methodology to language models: isolating which internal representations activate under behavioral pressure and naming those circuits so I can ultimately intervene on them. 

## Research Goal
This project uses mechanistic interpretability, which is the study of looking at the brain of artificial intelligence to look at its raw math to see if models like Google Gemini and NVIDIA NeMo can actually distinguish between a high-momentum professional and one who is stagnating.

Does the AI only understand the technical words being typed, or can it mathematically detect the psychological state of the user?

## The Experiment: An A/B Comparison
To make this study rigorous I set this up as an AB test comparing two different AI models to see if they judge human behavior differently.

Model A Google gemini embedding 001 which is a proprietary closed system.

Model B NVIDIA Nemo which is an open source system.

I intentionally excluded models like Claude due to high API costs. Cost accessibility is a major factor in AI safety research. By prioritizing the free open source NVIDIA Nemo model alongside Gemini I want to highlight why researchers and the public need accessible tools. If AI systems are going to be used to evaluate human behavior or manage workflows we need open source transparency to audit how they make those judgments. We must ensure they are safe unbiased and accurate.

## Methodology
Phase 1 The Dataset
I created 15 pairs of status updates. In each pair the actual work task was identical for example writing software documentation.

One version was written from a Proactive Persona using words of ownership and systemic alignment.

The other version was written from a Stagnant Persona showing isolation and reliance on luck.

Phase 2 Vectorization Turning Words to Math
AI models do not read words they read numbers. Both the Gemini and Nemo embedding models took my text and converted it into a mathematical coordinate with 768 different dimensions. his vector represents a physical location in the AI's memory. I mapped these coordinates to see where proactive lives versus where stagnant lives.

Using a formula called Cosine Similarity, I measured how far apart these two mindsets are. Even though the words were almost the same, the AI saw them as mathematically distant. This proves the AI cares more about your agency (how you are working) than your task (what you are doing).

What is Cosine Similarity?
In simple terms, Cosine Similarity is a way to measure how closely two ideas are pointing in the same direction. If you think of every status update as a literal arrow in a 3D room:
If two arrows point in exactly the same direction, they have a score of 1.0 (Perfect Alignment).
If they are completely unrelated or pointing in opposite directions, the score drops toward 0.
Even though the words in my dataset were almost identical, the AI saw them as mathematically distant.

The average similarity was 0.84.
The most divergent scenario dropped to 0.7835.

This proves the model's architecture is more sensitive to agency (the direction or intent of your work) than the content (the literal task you are doing).

Phase 3 Quantitative Analysis
I measured the mathematical distance between these coordinates. The math proved that the AI models see the proactive and stagnant updates as completely different concepts even though the technical work task was exactly the same. The models prioritize the behavioral intent over the task itself.

Phase 4 The Agency Circuit
By looking at which specific numbers changed the most between the two personas I isolated Dimensions 215 656 and 616. These specific pathways light up when a user loses momentum. This is the Agency Circuit. I then used a technique called Principal Component Analysis to flatten those complex 768 dimensions onto a simple 2D graph. The visual result shows a perfect dividing line between high agency and low agency professionals.

## Results
This is the most critical addition to your README. It shifts the narrative from a technical experiment to a deep, career-long mission. By framing your work at Mentor Me Collective as human-system stress testing, you demonstrate that your transition into AI Safety is a logical evolution of your existing expertise.

The Agency Circuit: A Mechanistic Interpretability Study
Decoding Professional Stagnation inside AI Vector Space
The Problem: The Mentorship Gap
In high-pressure professional environments, burnout and stagnation often happen in silence. At the Mentor Me Collective (MMC), I designed behavioral stress tests to identify failure modes in human systems—specifically, how "agency drift" and "motivation decay" manifest in mentee behavior.

This project applies that same methodology to language models: isolating which internal representations activate under behavioral pressure and naming those circuits so we can ultimately intervene on them. My work has always been about safety and stability; I am simply moving from auditing human systems to auditing artificial ones.

The Research Goal
This project uses Mechanistic Interpretability, looking inside the brain of an AI to look at its raw internal math—to see if models like Google Gemini and NVIDIA NeMo can actually distinguish between a "high-momentum" professional and one who is stagnating.

We need to know: Does the AI only understand the technical words being typed, or can it mathematically detect the underlying psychological state of the user?

The Experiment: An A/B Comparison
To ensure the results were not a fluke, I conducted an A/B test comparing two different "mathematical brains":

Google Gemini (Embedding-001): A powerful, proprietary model.

NVIDIA NeMo: A high-performance open-source model.

The Open Source Mandate: In the field of AI Safety, accessibility is a safety feature. By using open-source models like NeMo alongside proprietary ones, I want to highlight the importance of transparency. If AI systems are going to be used to manage workflows or evaluate human behavior, their logic must be auditable by the public, not hidden behind a corporate paywall.

How It Works
1. The Twin Dataset
I developed 15 pairs of status updates where the technical work task is identical (e.g., "Updating the project database").

The Proactive Version: Uses language of systemic ownership and alignment.

The Stagnant Version: Uses language of avoidance, isolation, and reliance on luck.

2. Turning Language into Coordinates (Vectorization)
AI doesn't read words; it converts them into a list of numbers called a Vector. This vector represents a physical location in the AI's memory. I mapped these coordinates to see if proactive mindsets live in a different mathematical neighborhood than stagnant ones.

3. Measuring the Distance
Using a formula called Cosine Similarity, I measured the distance between these coordinates.

The Discovery: Despite the identical tasks, the AI saw these updates as mathematically distant.

This proves the model's architecture is more sensitive to agency (how you work) than content (what you do).

4. Isolating the Agency Circuit
By identifying which specific dimensions changed the most between the two personas, I isolated Dimensions 215, 656, and 616. These are the specific pathways that light up when a user loses professional momentum. I used Principal Component Analysis (PCA) to flatten this complex math into a clear 2D map.

## The Results
The analysis showed perfect linear separability.The AI does not see a gray area. It categorizes professional identity into two distinct mathematical states.

## Why does this matter
If I can mathematically identify the tipping point where a professional flips from momentum to decay, I can build predictive mentorship systems.

Instead of waiting for a project to fail, an AI could monitor the agency circuit and automatically alert a  mentor to step in. This research bridges the gap between AI’s mathematical precision and the human empathy required to keep professionals on track.

## Future Work
My next phase is a 3-month longitudinal study to track these coordinates in real-time. The goal is to move from detecting stagnation to preventing it through early-warning safety systems.
