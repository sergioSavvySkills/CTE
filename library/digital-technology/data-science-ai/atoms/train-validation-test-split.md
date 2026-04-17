---
atom_id: train-validation-test-split
title: Train / Validation / Test Splits
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::2.5
  - ms-ai-900::2.2
skill_type: both
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

Students will be able to split a dataset into train/validation/test sets, explain the purpose of each, and avoid data leakage.

## Content stub

- **Training set:** used to fit the model — typically 60-80% of data
- **Validation set:** used during training to tune hyperparameters and detect overfitting — typically 10-20%
- **Test set:** held out until the very end; used once to estimate real-world performance — typically 10-20%
- **Why three sets:** if you tune on your test set, you no longer have an honest measure of performance
- **Stratified splits:** preserve class balance across splits when data is imbalanced
- **Data leakage:** info from test leaking into train (by preprocessing before split, by time-ordered data split randomly); destroys validity

## Assessment stub

- Code: use sklearn's train_test_split to make a 70/15/15 split
- Identify: given 3 scenarios, spot the data leakage mistake
- Short answer: why can't you just use the training accuracy as your report metric?
