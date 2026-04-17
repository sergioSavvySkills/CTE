---
atom_id: business-continuity-and-disaster-recovery
title: Business Continuity and Disaster Recovery
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::6.7
  - comptia-a-plus::core2::4.3
  - google-it-support::c4m5
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - storage-technologies
  - cia-triad
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to differentiate business continuity from disaster recovery, describe backup types and strategies, and explain RTO and RPO objectives.

## Content stub

- **Business continuity vs. DR:** BC = keeping operations running during a disruption; DR = restoring systems after a failure
- **Backup types:** full, incremental, differential — storage and restore time trade-offs; backup rotation (GFS)
- **Backup locations:** on-site vs. off-site vs. cloud; 3-2-1 rule (3 copies, 2 media types, 1 offsite)
- **RTO and RPO:** Recovery Time Objective = how fast; Recovery Point Objective = how much data loss is acceptable
- **Fault tolerance:** RAID, UPS, redundant power supplies, hot/cold standby; preventing single points of failure
- **Testing backups:** why untested backups are worthless; restore drills; backup verification logs

## Assessment stub

- Backup strategy design: given an organization's RTO/RPO requirements, design a backup plan
- 3-2-1 audit: evaluate a provided backup plan against the 3-2-1 rule and identify gaps
- Short answer: a backup completed at 11 PM and a failure occurs at 3 PM the next day — what is the RPO?
