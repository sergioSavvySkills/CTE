---
atom_id: pandas-for-data-work
title: Pandas for Data Analysis
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::2.3
  - comptia-data-plus::3.2
skill_type: skill
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

Students will be able to use core Pandas operations (groupby, merge, apply) to manipulate tabular data.

## Content stub

- **groupby:** `df.groupby('category')['value'].mean()` — the SQL GROUP BY of Pandas
- **merge / join:** `pd.merge(left, right, on='key')` — combine DataFrames like SQL JOINs
- **apply and map:** run a function across rows, columns, or cells — use sparingly vs. vectorized operations
- **Vectorized operations:** `df['c'] = df['a'] + df['b']` — faster than loops; always try this first
- **Pivot and melt:** reshape long → wide and back; parallels Excel pivot but scriptable
- **Common pipeline:** read_csv → clean → groupby → merge → write_csv

## Assessment stub

- Lab: given a sales DataFrame, compute sum-of-revenue by region and product using groupby
- Lab: merge a customers DataFrame with an orders DataFrame on customer_id
- Short answer: why is a vectorized operation faster than a Python loop in Pandas?
