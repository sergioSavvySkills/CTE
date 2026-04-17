---
atom_id: internal-components
title: Internal Computer Components (Motherboard, CPU, RAM, BIOS)
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::2.3
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - hardware-components-overview
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to describe the purpose and key specifications of the motherboard, CPU, RAM, and BIOS/UEFI, and explain how they interact during the boot process.

## Content stub

- **Motherboard anatomy:** chipset, form factors (ATX/mATX/ITX), slots (PCIe, RAM), SATA/M.2 connectors, CMOS battery
- **CPU specs:** cores, threads, clock speed, cache levels (L1/L2/L3), TDP, socket types (Intel vs AMD)
- **RAM specs:** DDR4 vs DDR5, MHz, CAS latency, dual-channel; how capacity affects multitasking
- **BIOS/UEFI:** firmware that initializes hardware at boot; POST sequence; boot order; Secure Boot
- **Boot process:** BIOS POST → bootloader → OS kernel handoff; failure points
- **Thermal management:** heatsinks, thermal paste, case airflow; why CPU throttles when overheating

## Assessment stub

- Spec comparison: given two motherboard spec sheets, identify which supports DDR5 and PCIe 5.0
- BIOS walkthrough: enter BIOS on a lab PC, change boot order, save and exit
- Short answer: what does POST check, and what happens if it fails?
