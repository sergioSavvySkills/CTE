---
atom_id: training-evaluating-ml-models
title: Training and Evaluating ML Models
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
  - ms-ai-900::2.2
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - supervised-unsupervised-reinforcement-learning
  - train-validation-test-split
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to train a simple classifier, evaluate its performance with appropriate metrics, and describe what worked and what didn't.

## Content stub

- **Training loop concept:** show the model examples, compute loss, update parameters, repeat — supervised learning in one sentence
- **Accuracy:** % correct — useful when classes are balanced; misleading when imbalanced
- **Precision and recall:** precision = of predicted positives, how many were right; recall = of actual positives, how many were found
- **Confusion matrix:** true/false × positive/negative grid; the ground truth of 'what's happening with my model'
- **Overfitting vs underfitting:** overfitting: memorizes training data; underfitting: doesn't learn enough. Use val set to detect
- **Describing results:** report metric, caveats, data size, failure cases — not just 'my model got 95% accuracy'

## Assessment stub

- Lab: train a sklearn LogisticRegression on a small dataset and report accuracy + confusion matrix
- Interpret: given a confusion matrix, compute precision and recall
- Short answer: why is training-set accuracy a dangerous metric?
