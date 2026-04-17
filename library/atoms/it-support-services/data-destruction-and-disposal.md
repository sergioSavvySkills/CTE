---
atom_id: data-destruction-and-disposal
title: Data Destruction and Disposal Methods
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core2::2.9
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 1
prerequisites:
  - storage-technologies
  - encryption-fundamentals
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to select the appropriate data destruction method for a given storage media type and regulatory context, and explain why deletion is not destruction.

## Content stub

- **Why deletion is not enough:** deleted files remain on disk until overwritten; file system only removes directory entry
- **Overwriting (wiping):** DoD 5220.22-M, Gutmann method; single-pass with random data often sufficient for HDDs; tools (DBAN, Eraser)
- **SSD and flash challenges:** wear leveling means data may persist in unreachable cells; manufacturer secure erase (ATA SE) preferred
- **Physical destruction:** degaussing (HDD only), shredding, drilling, incineration; when to use each; chain of custody
- **Regulatory requirements:** HIPAA, GDPR, PCI-DSS data disposal requirements; certificates of destruction
- **Asset disposal process:** decommission checklist: wipe, document, certificate, physical disposal or donation

## Assessment stub

- Method selection: given 5 media types and disposal scenarios, select the most appropriate destruction method
- Short answer: why is degaussing ineffective for SSDs?
- Policy draft: write a 5-step data disposal SOP for a school that replaces 50 laptops per year
