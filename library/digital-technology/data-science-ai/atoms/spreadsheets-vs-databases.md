---
atom_id: spreadsheets-vs-databases
title: Spreadsheets vs. Databases
subcluster: data-science-ai
credential_objectives:
  - comptia-data-plus::2.1
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - spreadsheet-fundamentals-for-data
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to compare spreadsheets and databases and recommend the right tool for a given data task.

## Content stub

- **Spreadsheet strengths:** quick exploration, ad-hoc analysis, small datasets (<100k rows), non-technical users
- **Spreadsheet limits:** row limits, one editor at a time, formulas break silently, no enforced schema
- **Database strengths:** concurrent access, enforced schema, relational integrity, scales to billions of rows, query language (SQL)
- **Database limits:** setup overhead, requires knowledge of SQL, less interactive than a sheet
- **When to pick which:** if the data grows, is shared by multiple users, or needs consistency guarantees → database

## Assessment stub

- Recommend: for each of 5 scenarios (classroom roster, e-commerce orders, household budget, city census, Twitter feed), pick sheet or database
- Design: sketch a table schema for a library's book-loan records
- Short answer: what breaks in a spreadsheet when 10 people edit at once?
