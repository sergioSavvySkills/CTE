---
atom_id: debugging-hardware-issues
title: Debugging Hardware Issues
subcluster: data-science-ai
credential_objectives: []
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - building-an-embedded-robot
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to apply a systematic debugging methodology to hardware problems.

## Content stub

- **Reproduce the problem:** can you make it happen on demand? intermittent issues are the hardest
- **Narrow to component:** swap one part at a time (known-good cable, fresh battery, different sensor)
- **Multimeter basics:** measure continuity (cable intact?), voltage (power supplied?), resistance (component intact?)
- **Read error messages:** serial console output is your friend; print sensor values and state to trace behavior
- **Check the obvious first:** is it powered on? is the cable plugged in? is the code uploaded? is the battery charged?
- **When stuck, explain out loud:** 'rubber ducking' on hardware works too — you'll often spot the issue yourself

## Assessment stub

- Lab: intentionally introduce 3 faults in a working setup; have a partner debug them
- Create a checklist: the 10 things you always check first when hardware misbehaves
- Short answer: why is 'check the obvious first' the hardest step to remember?
