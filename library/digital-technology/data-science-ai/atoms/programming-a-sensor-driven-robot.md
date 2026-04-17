---
atom_id: programming-a-sensor-driven-robot
title: Programming a Sensor-Driven Robot
subcluster: data-science-ai
credential_objectives: []
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 4
prerequisites:
  - building-an-embedded-robot
  - python-input-and-decisions
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to write a program for an embedded robot that reads sensor input, makes decisions, and controls actuators.

## Content stub

- **Read sensor values:** GPIO on Raspberry Pi or analog/digital pin on Arduino; poll in a loop or on interrupt
- **Decision logic:** thresholding (if distance < 20 then stop); state machines for multi-step behaviors
- **Control actuators:** digitalWrite for on/off; PWM for motor speed; servo libraries for angle control
- **The sense-plan-act loop:** read sensors → update state → decide action → actuate → repeat (classic robotics architecture)
- **Integrate a small ML model:** on Raspberry Pi: use TFLite to classify camera frames; on Arduino: use TinyML for keyword/gesture
- **Fail safely:** what does the robot do if a sensor reading is invalid? default to stop, don't default to 'full speed'

## Assessment stub

- Lab: program a robot to stop when an object is closer than 20cm (ultrasonic sensor)
- Extend: add a second behavior (e.g., turn away after stopping)
- Short answer: why is 'fail to stop' safer than 'fail to continue' for a moving robot?
