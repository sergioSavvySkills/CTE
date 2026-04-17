---
atom_id: end-to-end-ai-project
title: End-to-End AI Project: Problem to Deployment
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::4.5
  - ms-ai-900::2.2
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 4
prerequisites:
  - training-evaluating-ml-models
  - agile-and-github-for-ai-projects
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to walk through the full lifecycle of an AI software project from problem definition to deployment.

## Content stub

- **1. Define the problem:** who is the user, what decision does AI inform, what success metric, what's the business/social case
- **2. Collect and prepare data:** source datasets, clean, split into train/val/test, document lineage
- **3. Model development:** baseline first (simple model), iterate to more complex if baseline is insufficient
- **4. Evaluation:** hold-out test set, compare to baseline, per-group analysis, failure case review
- **5. Deployment:** API endpoint, containerize with Docker, monitor latency and accuracy in production
- **6. Monitoring and iteration:** drift detection, periodic retraining, A/B testing new versions

## Assessment stub

- Design: walk through this 6-step lifecycle for an AI that predicts your school's cafeteria waste
- Identify: given a scenario where 'accuracy dropped after deployment,' what likely went wrong?
- Short answer: why must you have a baseline model before celebrating a fancy one?
