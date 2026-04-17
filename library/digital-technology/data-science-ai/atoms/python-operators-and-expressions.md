---
atom_id: python-operators-and-expressions
title: Python Operators: Logical, Relational, Boolean, Math
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
skill_type: knowledge
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

Students will be able to apply the full operator set (arithmetic, comparison, logical, bitwise) and predict the result of compound expressions.

## Content stub

- **Arithmetic:** + - * / // % **; precedence; integer vs float division; PEMDAS applies
- **Comparison:** == != < > <= >= — return True/False; can chain like `0 < x < 10`
- **Logical:** and, or, not; short-circuit evaluation — `a and b` skips b if a is False
- **Bitwise:** &, |, ^, <<, >> — operate on binary representations; used in flags and low-level code
- **Assignment operators:** =, +=, -=, *=, /= — shortcut for update-in-place
- **Operator precedence traps:** `not a == b` parses as `not (a == b)`; parenthesize when in doubt

## Assessment stub

- Predict the output of 5 expressions mixing arithmetic, comparison, and logical operators
- Lab: rewrite a multi-line if chain using compound boolean expressions
- Short answer: what does short-circuit evaluation mean, and why is it useful?
