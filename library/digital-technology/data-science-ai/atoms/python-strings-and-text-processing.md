---
atom_id: python-strings-and-text-processing
title: Strings and Text Processing
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
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

Students will be able to construct, format, and transform strings using Python's string methods, important for NLP and data cleaning.

## Content stub

- **Constructing strings:** single/double/triple quotes; escape sequences; raw strings for regex and paths
- **f-strings:** `f'{name} scored {score:.1f}'` — modern Python formatting; supports expressions and format specs
- **Methods:** lower, upper, strip, split, join, replace, find, startswith, endswith
- **Slicing:** s[0:5], s[-3:], s[::-1] reverses; produces new strings since strings are immutable
- **Character vs Unicode:** strings are Unicode; encoding matters when reading files (use encoding='utf-8')

## Assessment stub

- Lab: parse '2026-04-17' into year, month, day using string methods
- Write: one-liner that splits a sentence into words, lowercases, and returns unique words
- Short answer: why does 'abc'.replace('a','z') not modify the original string?
