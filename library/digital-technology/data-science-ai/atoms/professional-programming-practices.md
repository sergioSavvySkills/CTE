---
atom_id: professional-programming-practices
title: Professional Programming Practices
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::4.3
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - comments-documentation-and-ux
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply professional practices: commenting, file organization, naming conventions, and version control basics.

## Content stub

- **Commenting discipline:** comment the WHY, not the WHAT; no redundant comments; document tricky parts
- **File and project structure:** src/ for code, tests/ for tests, data/ for data, one .py per class; __init__.py for packages
- **Naming conventions:** snake_case for functions/variables, PascalCase for classes, UPPER for constants
- **Code style:** run a linter (ruff/black); follow PEP 8; 4-space indent; 79-100 char lines
- **Version control basics:** git commit often, meaningful messages, .gitignore the secrets and venv; push to GitHub regularly

## Assessment stub

- Audit: review a given messy script and list 5 professional-practice violations
- Lab: reorganize a single-file project into src/ + tests/ structure
- Short answer: why is 'commit often' better than 'commit only when perfect'?
