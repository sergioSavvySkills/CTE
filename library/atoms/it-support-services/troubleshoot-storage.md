---
atom_id: troubleshoot-storage
title: Troubleshooting Storage and RAID
subcluster: it-support-services
credential_objectives:
  - comptia-a-plus::core1::5.2
skill_type: skill
grade_band: HS
estimated_minutes: 60
difficulty: 3
prerequisites:
  - storage-technologies
  - filesystems-and-partitioning
  - troubleshooting-methodology
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to diagnose storage failures using SMART data, event logs, and diagnostic tools, and recover data or rebuild a RAID array.

## Content stub

- **HDD failure signs:** clicking/grinding sounds, slow reads, SMART errors; CrystalDiskInfo health status
- **SSD failure signs:** sudden read-only mode, corruption errors, disappearing drive, high reallocated sectors
- **SMART data interpretation:** key attributes: Reallocated Sectors, Pending Sectors, Uncorrectable Errors; threshold vs. value
- **File system errors:** chkdsk /f /r; NTFS journal corruption; dirty bit; when chkdsk runs at boot
- **RAID failure and rebuild:** degraded array; replacing a failed drive; rebuild time and risk of second failure; importance of hot spare
- **Data recovery basics:** when to attempt recovery (Recuva) vs. when to escalate to professional services; acting quickly matters

## Assessment stub

- SMART analysis: given a CrystalDiskInfo screenshot, classify the drive health and recommend action
- chkdsk lab: run chkdsk on a volume with simulated errors and document the output
- Short answer: why is a RAID 5 array at higher risk of total failure while one drive is rebuilding?
