---
atom_id: embedded-systems-and-sensors
title: Embedded Systems and Sensors for AI
subcluster: data-science-ai
credential_objectives: []
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites: []
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to identify components of an embedded system and describe how sensors enable AI at the edge.

## Content stub

Conceptual overview only — circuit wiring and breadboard work belong in `building-an-embedded-robot`.

- **Microcontroller vs. microcomputer:** microcontroller (Arduino, micro:bit) runs one loop, ultra-low power; microcomputer (Raspberry Pi) runs a full OS and can run Python ML models
- **Sensors:** input devices that read the physical world — temperature, motion, camera, microphone, accelerometer; the data source for edge AI
- **Actuators:** output devices that act on the world — motors, servos, LEDs; what the system *does* with its decisions
- **Edge AI:** running a trained ML model on the device itself rather than sending data to the cloud; faster response, better privacy, works offline

## Assessment stub

- Match: given 4 real products (smart thermostat, fitness tracker, doorbell camera, robotic vacuum), identify the key sensors and whether it runs edge AI or cloud AI
- Short answer: name one reason a designer would choose edge AI over a cloud API
