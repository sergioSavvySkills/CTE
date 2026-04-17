---
atom_id: troubleshoot-motherboards-ram-cpus
title: Troubleshooting Motherboards, RAM, CPUs, and Power
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::5.1
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - internal-components
  - ram-fundamentals
  - power-supplies
  - troubleshooting-methodology
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to diagnose and resolve hardware failures in motherboards, RAM, CPUs, and power supplies using systematic techniques and diagnostic tools.

## Content stub

- **POST beep codes and LED indicators:** interpreting BIOS beep codes (1 beep = OK, patterns = specific failures); diagnostic LEDs on modern boards
- **No POST troubleshooting:** no power vs. powers on but no display; breadboarding technique; minimum hardware boot
- **RAM failures:** blue screens with MEMORY_MANAGEMENT, random reboots; MemTest86; reseating, slot testing
- **CPU issues:** overheating (thermal throttle → shutdown), bent pins (AMD), improper seating, cooler failure
- **Power supply testing:** PSU tester, multimeter voltages (+12V, +5V, +3.3V rails); paperclip test; swapping with known-good
- **Motherboard failures:** capacitor bulge, CMOS battery dead (time resets), POST checkpoint cards

## Assessment stub

- Symptom-to-cause matching: given 8 hardware failure symptoms, identify the most likely component
- Lab: deliberately unseat a RAM stick, power on, observe the failure, then reseat and verify
- Short answer: a PC powers on (fans spin, lights on) but shows no display — list three components to check in order
