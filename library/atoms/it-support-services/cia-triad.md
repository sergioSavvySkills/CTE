---
atom_id: cia-triad
title: CIA Triad (Confidentiality, Integrity, Availability)
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::6.1
  - google-it-support::c5m1
skill_type: knowledge
grade_band: HS
estimated_minutes: 45
difficulty: 1
prerequisites: []
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to define the three components of the CIA triad, provide examples of controls that support each, and classify security incidents by which component they violate.

## Content stub

- **Confidentiality:** preventing unauthorized disclosure; encryption, access controls, need-to-know principle
- **Integrity:** preventing unauthorized modification; hashing, digital signatures, version control, audit logs
- **Availability:** ensuring authorized users can access resources; redundancy, backups, DDoS protection, uptime SLAs
- **Trade-offs:** more security often reduces availability; balancing the triad for different systems
- **CIA in incidents:** ransomware violates all three; data breach = confidentiality; defacement = integrity; DDoS = availability
- **Additional security goals:** non-repudiation, authentication, authorization — how they complement the triad

## Assessment stub

- Incident classification: given 8 security event descriptions, identify which CIA component each violates
- Control matching: pair 10 security controls (e.g., disk encryption) with the CIA component they primarily support
- Short answer: a hospital must prioritize availability over confidentiality — give a real scenario where this is true
