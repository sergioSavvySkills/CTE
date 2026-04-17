---
atom_id: storage-technologies
title: Storage Technologies (HDD, SSD, NVMe, Cloud)
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::2.5
  - comptia-a-plus::core1::3.4
skill_type: knowledge
grade_band: HS
estimated_minutes: 60
difficulty: 2
prerequisites:
  - computing-units-of-measure
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to compare HDD, SSD, and NVMe storage technologies by speed, durability, and use case, and describe how cloud storage fits into the storage hierarchy.

## Content stub

- **HDD internals:** spinning platters, read/write heads, seek time, RPM (5400/7200); good for large cold storage
- **SSD technology:** NAND flash cells (SLC/MLC/TLC/QLC), no moving parts, shock-resistant, faster than HDD
- **NVMe vs SATA:** NVMe uses PCIe bus for much higher bandwidth; M.2 form factor; when the upgrade is worth it
- **RAID concepts:** RAID 0/1/5/10 — striping, mirroring, parity; RAID is not a backup
- **Cloud storage:** how services like OneDrive/Google Drive work; sync vs. backup; latency trade-off
- **Choosing storage:** workload-based selection: OS drive (NVMe), media library (HDD), backup (cloud)

## Assessment stub

- Comparison table: complete a 4-column table (HDD/SSD/NVMe/Cloud) comparing speed, cost per GB, durability, and best use
- Lab: use CrystalDiskInfo or similar to read SMART data from a drive and interpret health
- Short answer: why is RAID not a substitute for backup?
