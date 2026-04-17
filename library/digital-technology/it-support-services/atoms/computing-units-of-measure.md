---
atom_id: computing-units-of-measure
title: Units of Measure in Computing
subcluster: it-support-services
credential_objectives:
  - comptia-itf-plus::1.5
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

Students will be able to correctly interpret and convert between computing units of measure for storage capacity, data-transfer speed, and processing speed.

## Content stub

- **Storage units:** bit → byte → KB → MB → GB → TB → PB; binary (KiB/MiB) vs. decimal (KB/MB) definitions; why drive sizes appear smaller in the OS
- **Data-transfer speed:** bits per second (bps); Kbps, Mbps, Gbps; difference between storage (bytes) and transfer (bits)
- **Processing speed:** Hz, MHz, GHz for CPU clock; operations per second; IOPS for storage
- **Memory bandwidth:** MHz/MT/s for RAM; relationship between speed, width, and throughput
- **Practical conversions:** reading a spec sheet: '500 MB/s NVMe SSD', '2.4 GHz Wi-Fi', '32 GB RAM'; calculating download times
- **Common gotchas:** storage marketing math (1 TB drive = 931 GiB in OS); ISP speed caps in Mbps vs. MB/s file speeds

## Assessment stub

- Spec-sheet interpretation: given three hardware spec sheets, identify each unit and convert to a common unit for comparison
- Download-time calculation: given file size in GB and connection speed in Mbps, calculate transfer time
- Short answer: a drive is advertised as '1 TB'; why does the OS show ~931 GB?
