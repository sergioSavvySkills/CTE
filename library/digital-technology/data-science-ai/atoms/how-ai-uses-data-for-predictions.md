---
atom_id: how-ai-uses-data-for-predictions
title: How AI Uses Data to Make Predictions
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::2.2
  - ms-ai-900::2.1
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - data-vs-information
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to explain at a high level how data flows through an ML model to produce predictions or decisions.

## Content stub

- **Training data → model:** show the algorithm many labeled examples so it learns statistical patterns
- **Model as pattern-finder:** a function that takes new input and returns a prediction; the 'parameters' encode what it learned
- **Inference:** running a trained model on new data; much cheaper than training
- **Predictions ≠ truth:** a model outputs probabilities or best guesses; always evaluate accuracy against ground truth
- **Feedback loops:** real-world data collected after deployment can retrain the model — careful with bias amplification

## Assessment stub

- Diagram: sketch how training data flows into a model and how new predictions come out
- Short answer: why is a model's prediction never '100% certain' even on training data?
- Scenario: a spam filter starts flagging legitimate mail — describe what might have caused this drift
