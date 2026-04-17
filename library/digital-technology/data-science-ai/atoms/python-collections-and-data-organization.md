---
atom_id: python-collections-and-data-organization
title: Organizing Data with Lists, Dicts, and Files
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
  - certiport-its-data-analytics::2.1
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - python-data-types
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to write programs that collect different kinds of data and store them in appropriate Python structures.

## Content stub

- **Lists for ordered data:** list of temperature readings, list of student names; append, index, iterate
- **Dictionaries for labeled data:** `{'name': 'Ada', 'score': 92}` — key-value pairs when order matters less than labels
- **Lists of dicts:** the most common shape for 'rows of records'; foundational for CSV/dataset work
- **Reading a CSV:** `import csv; csv.DictReader(open(path))` → iterate rows as dicts
- **Writing output:** print, write to a .txt or .csv file; f-strings for formatting

## Assessment stub

- Lab: build a list of 5 dicts representing students {name, score} and compute the average score
- Lab: read a CSV file and print the 3rd column of each row
- Short answer: when would you choose a list of dicts over a flat list?
