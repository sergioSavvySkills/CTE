---
atom_id: fundamental-data-types
title: Fundamental Data Types in Computing
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::1.2
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 1
prerequisites:
  - binary-number-systems
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to identify and describe the fundamental data types used in computing and explain how each is stored and sized.

## Content stub

- **Integer types:** whole numbers; 8/16/32/64-bit widths; signed vs. unsigned; overflow
- **Floating-point:** representing decimals; single vs. double precision; why floating-point arithmetic is approximate
- **Characters and strings:** ASCII (7-bit, 128 characters), extended ASCII, Unicode (UTF-8/UTF-16); how text is encoded as bytes
- **Boolean:** true/false values; 1-bit logical data; use in conditions and flags
- **Binary large objects (BLOBs):** images, audio, video stored as raw byte sequences; file formats as structured binary
- **Data type size implications:** storage cost, memory alignment, network bandwidth; choosing the right type for the job

## Assessment stub

- Matching exercise: pair each data type with a real-world example (e.g., pixel color → integer, employee name → string)
- Short answer: why does a programmer choose float over int for a temperature sensor reading?
- Mini-lab: use a hex editor or Python to inspect the raw bytes of a small text file and identify the ASCII values
