---
atom_id: balanced-vs-imbalanced-datasets
title: Balanced vs. Imbalanced Datasets
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::2.4
  - ms-ai-900::2.2
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - datasets-and-dataframes
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to define balance in a dataset, identify when it's imbalanced, and describe the problems imbalance causes for AI.

## Content stub

- **Balanced dataset:** roughly equal examples per class — makes training stable
- **Imbalanced dataset:** one class dominates (e.g., fraud detection: 99% normal, 1% fraud)
- **Why imbalance hurts:** the model can achieve 99% accuracy by always predicting 'normal' — and be useless
- **Detecting imbalance:** count examples per class; visualize with a bar chart; ratios > 10:1 warrant concern
- **Fixes:** oversample the minority, undersample the majority, SMOTE synthetic samples, weighted loss
- **Different metrics needed:** when imbalanced, use precision/recall/F1, not accuracy

## Assessment stub

- Lab: use Pandas to check class balance of a sample dataset; plot counts
- Describe: for a rare-disease classifier, which fix (over/under/SMOTE) would you try first and why?
- Short answer: why does 99% accuracy mean nothing for fraud detection?
