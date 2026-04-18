---
atom_id: exploring-bias-with-teachable-machine
title: Exploring Bias Hands-On with Teachable Machine
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::5.2
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - teachable-machine-introduction
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to deliberately create and then detect bias in a no-code ML model, and propose remediation.

## Content stub

- **Design the experiment:** build a 2-class classifier; deliberately under-sample one class, or use unrepresentative photos
- **Test on held-out examples:** use photos not seen during training, including examples the model should classify but was underexposed to
- **Observe bias:** confidence scores drop or flip for underrepresented group — the model learned 'what's common'
- **Remediation options:** add more training samples for the minority class; remove the confounding variable; augment with varied poses/lighting
- **Document findings:** record accuracy per class, not just overall; write up what you saw and why

## Assessment stub

- Lab: build a biased 2-class classifier intentionally; test and record per-class accuracy
- Remediate: rebalance training data and re-test; compare before/after accuracy
- Short answer: how does this small experiment connect to the real-world facial-recognition audits?
