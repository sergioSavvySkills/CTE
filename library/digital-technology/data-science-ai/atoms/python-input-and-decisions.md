---
atom_id: python-input-and-decisions
title: User Input, Sensor Input, and Decisions
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::3.2
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - python-control-flow
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to write a program that accepts user or sensor input and uses it to make decisions.

## Content stub

- **input() from the keyboard:** reads a string; convert with int() or float() if you need a number
- **Validating input:** check range, type, emptiness; loop until valid input arrives
- **Sensor input (intro):** on a Raspberry Pi or Arduino, sensors return numbers over time; process similarly to user input
- **Making decisions:** chain if/elif on the input value; for sensors often compare to a threshold
- **Giving feedback:** print meaningful messages; never just `print(x)` — label what the user is seeing

## Assessment stub

- Lab: write a program that asks for a temperature and outputs 'freezing', 'cold', 'warm', or 'hot'
- Lab: write a program that accepts 3 test scores and outputs a letter grade
- Design: describe how the same logic would work with a temperature sensor replacing user input
