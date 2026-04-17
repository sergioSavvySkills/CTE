---
atom_id: boolean-logic-for-ai
title: Boolean Logic in Programming and AI
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - python-operators-and-expressions
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to evaluate boolean expressions, build truth tables, and recognize how boolean logic appears in AI decision rules.

## Content stub

- **True / False:** the two boolean values; every comparison reduces to one or the other
- **AND, OR, NOT:** truth tables; precedence (NOT > AND > OR); parens to be safe
- **XOR:** exactly-one-is-true; used in cryptography and some neural-network training
- **De Morgan's laws:** NOT (A AND B) == (NOT A) OR (NOT B); a useful refactoring tool
- **In AI decision rules:** expert systems chain boolean conditions; a leaf in a decision tree is a boolean test

## Assessment stub

- Build the truth table for `(A AND B) OR (NOT C)`
- Simplify: use De Morgan's law to rewrite `NOT (x > 0 AND x < 10)`
- Short answer: how does a decision tree use boolean logic?
