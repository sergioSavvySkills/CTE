---
atom_id: python-external-libraries
title: Using External Python Libraries
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.4
  - ms-ai-900::2.2
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - python-functions-and-returns
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to install, import, and use external Python libraries common in data science and AI.

## Content stub

- **import statements:** `import math`, `import numpy as np`, `from pandas import DataFrame` — different access styles
- **Installing packages:** pip install name; virtual environments keep projects isolated; pip freeze > requirements.txt
- **Reading library docs:** check the official docs first; scan the quickstart; then find specific functions
- **Essential AI/DS libraries:** numpy (arrays), pandas (tabular), matplotlib (plots), scikit-learn (ML), requests (HTTP)
- **Handling ImportError:** module not installed? typo in name? Python version mismatch? case-sensitive?

## Assessment stub

- Lab: install numpy, import as np, and compute the mean of [1,2,3,4,5]
- Read: browse the Pandas DataFrame docs and summarize 3 commonly-used methods
- Troubleshoot: given an ImportError, list 3 most likely causes
