---
atom_id: datasets-and-dataframes
title: Datasets and Pandas DataFrames
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::2.3
  - comptia-data-plus::2.1
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - python-external-libraries
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to define a dataset, load one into a Pandas DataFrame, and perform basic inspection and selection.

## Content stub

- **Dataset:** a collection of related records; usually a CSV/JSON/Parquet file or a DB table
- **Dataset components:** rows = records, columns = features/attributes; metadata about what columns mean
- **DataFrame:** Pandas' tabular structure; labeled rows + labeled columns; behaves like a supercharged spreadsheet
- **Loading data:** `pd.read_csv(path)`, `pd.read_json`, `pd.read_sql`; first step of every DS project
- **Inspection:** `.head()`, `.info()`, `.describe()`, `.shape` — what you do before anything else
- **Selection:** `df['col']`, `df.loc[...]`, `df.iloc[...]`, boolean masks for filtering rows

## Assessment stub

- Lab: load a sample CSV into Pandas; run .head, .info, .describe and summarize
- Write code: filter the DataFrame to rows where 'score' > 90 and sort by name
- Short answer: why do practitioners always run .info() and .describe() first?
