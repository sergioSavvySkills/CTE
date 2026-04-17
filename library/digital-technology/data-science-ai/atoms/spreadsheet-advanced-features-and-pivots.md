---
atom_id: spreadsheet-advanced-features-and-pivots
title: Advanced Spreadsheet Features: Pivots, Formulas, Cell References
subcluster: data-science-ai
credential_objectives:
  - certiport-its-data-analytics::3.1
  - comptia-data-plus::3.2
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - spreadsheet-fundamentals-for-data
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to use pivot tables, structured references, and advanced formulas to analyze data in a spreadsheet.

## Content stub

- **Pivot tables:** drag-and-drop summarization: rows, columns, values, filters; instant group-bys
- **Pivot measures:** count, sum, average, % of total, running total — switch via 'Summarize Values By'
- **Absolute vs relative references:** $A$1 locks both, $A1 locks column, A$1 locks row — critical for dragging formulas
- **Conditional formulas:** SUMIF, COUNTIF, AVERAGEIF — aggregate with a condition
- **Lookups:** XLOOKUP (modern), VLOOKUP (legacy); how to match across two sheets
- **When to leave the spreadsheet:** rule of thumb: >100k rows or multi-step transforms → move to Python/Pandas

## Assessment stub

- Lab: build a pivot table from a sales dataset showing sum-of-revenue by region and year
- Write a SUMIF formula that totals sales only for one product category
- Short answer: why would you use XLOOKUP instead of VLOOKUP?
