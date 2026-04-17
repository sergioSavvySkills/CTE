---
atom_id: data-cleansing-and-transformation
title: Data Cleansing, Collection, and Transformation
subcluster: data-science-ai
credential_objectives:
  - certiport-its-data-analytics::2.2
  - comptia-data-plus::2.3
  - certiport-its-artificial-intelligence::2.1
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

Students will be able to identify common data-quality problems and apply Pandas operations to clean and transform a dataset.

## Content stub

- **Missing values:** detect (.isna().sum()); fix by drop, fill with mean/median, forward-fill, model-based imputation
- **Duplicates:** .duplicated() and .drop_duplicates(); decide on subset of columns that define a duplicate
- **Inconsistent categories:** 'NYC' vs 'New York' vs 'ny' — normalize with .str.lower(), .str.strip(), mapping dicts
- **Outliers:** detect with boxplots or z-score; investigate before removing — they might be real
- **Type fixes:** numbers stored as strings, dates not parsed — cast with pd.to_numeric, pd.to_datetime
- **Transformation:** scaling/normalizing, one-hot encoding of categoricals, log transforms for skewed data

## Assessment stub

- Lab: given a messy CSV, apply cleaning steps and produce a report of before/after counts
- Design: propose a cleaning plan for a survey dataset with 15% missing responses
- Short answer: when should you drop rows with missing data vs. impute?
