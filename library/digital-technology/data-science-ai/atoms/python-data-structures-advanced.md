---
atom_id: python-data-structures-advanced
title: Choosing Python Data Structures: List, Set, Dict, Tuple
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - python-collections-and-data-organization
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to select the appropriate Python data structure for a given task and reason about trade-offs.

## Content stub

- **List:** ordered, mutable, allows duplicates — the default when order matters
- **Set:** unordered, unique elements, fast membership test — use to dedupe or test 'is X in this group'
- **Dict:** key-value, unordered (insertion-order preserved in modern Python), fast lookup by key
- **Tuple:** ordered, immutable — use for fixed-size records or when you need a hashable collection
- **Performance notes:** O(1) dict and set lookup; O(n) list `in`; choose based on the operation you do most
- **Nested structures:** list of dicts, dict of lists — the patterns behind most real-world AI/DS data

## Assessment stub

- Given 4 scenarios (unique visitors, ordered events, lookup by id, fixed coordinate), pick the right structure
- Lab: refactor a program that uses `if x in lst:` on a large list to use a set instead
- Short answer: why is a dict's lookup faster than searching a list?
