# it-support-services (texas) — SME Review

Automated first-pass review of course templates. Surfaces items a human
SME (Maya) should confirm before promoting any template to `status: active`.
Not every finding is a defect — some are intentional design choices that
just need a sign-off.

## How to read the findings

**`prereq appears later`** — Real ordering bug within a course. Fix by
reordering slots.

**`prereq not in course`** — Usually expected cross-course coupling
(prereq supplied by an earlier course in the pathway). Review only when
the listed prereq wouldn't be covered elsewhere in the pathway.

**`skill_type` / `simulation` mismatch** — Confirm intent. Deliberate
overrides are fine; sloppy ones can degrade the lesson.

## 130.303 — Computer Maintenance

- Units: **11** — Slots: **50** — Weeks declared: **20**
- **Pacing:** 50 slots, 2535 atom-minutes total, 20 declared weeks (4500 min @ 5×45 min/week). Slack for assessments/reviews: 1965 min (44%).

### Findings to review

- U04 slot 1 `internal-components` requires `hardware-components-overview` — **prereq not in course**
- U04 slot 4 `troubleshoot-motherboards-ram-cpus` requires `power-supplies` — **prereq appears later** at position 20
- U05 slot 2 `troubleshoot-storage` requires `filesystems-and-partitioning` — **prereq not in course**
- U05 slot 3 `display-components` requires `hardware-components-overview` — **prereq not in course**
- U05 slot 4 `troubleshoot-display` requires `cables-and-connectors` — **prereq appears later** at position 22
- U05 slot 5 `power-supplies` requires `hardware-components-overview` — **prereq not in course**
- U06 slot 1 `peripheral-devices` requires `hardware-components-overview` — **prereq not in course**
- U06 slot 2 `cables-and-connectors` requires `hardware-components-overview` — **prereq not in course**
- U07 slot 1 `mobile-device-hardware` requires `hardware-components-overview` — **prereq not in course**
- U08 slot 6 `linux-features` requires `file-management` — **prereq not in course**
- U08 slot 8 `troubleshoot-windows` requires `windows-cli` — **prereq not in course**
- U09 slot 1 `application-installation` requires `os-installation` — **prereq not in course**
- U09 slot 2 `software-licensing` requires `data-value-and-intellectual-property` — **prereq not in course**
- U09 slot 3 `virtualization-concepts` requires `hardware-components-overview` — **prereq not in course**
- U09 slot 4 `cloud-computing` requires `networking-fundamentals` — **prereq appears later** at position 41
- U10 slot 6 `networking-tools` requires `network-configuration` — **prereq not in course**
- U11 slot 2 `it-environmental-impacts` requires `data-destruction-and-disposal` — **prereq not in course**
- U02 slot 1 `troubleshooting-methodology` (skill_type=both) has `simulation: false` — skill atom losing hands-on component
- U04 slot 3 `motherboard-and-cpu-installation` (skill_type=skill) has `simulation: false` — skill atom losing hands-on component

## 130.304 — Computer Maintenance Lab

- Units: **10** — Slots: **51** — Weeks declared: **20**
- **Pacing:** 51 slots, 2670 atom-minutes total, 20 declared weeks (4500 min @ 5×45 min/week). Slack for assessments/reviews: 1830 min (41%).

### Findings to review

- U01 slot 3 `change-management` requires `documentation-and-ticketing-systems` — **prereq appears later** at position 6
- U03 slot 1 `hardware-components-overview` requires `input-processing-output-storage` — **prereq not in course**
- U04 slot 1 `storage-technologies` requires `computing-units-of-measure` — **prereq not in course**
- U04 slot 2 `filesystems-and-partitioning` requires `file-management` — **prereq appears later** at position 31
- U05 slot 3 `troubleshoot-mobile-os` requires `operating-systems-overview` — **prereq appears later** at position 28
- U06 slot 1 `operating-systems-overview` requires `input-processing-output-storage` — **prereq not in course**
- U06 slot 2 `os-installation` requires `windows-editions` — **prereq not in course**
- U06 slot 3 `windows-features-and-tools` requires `windows-editions` — **prereq not in course**
- U08 slot 1 `networking-fundamentals` requires `input-processing-output-storage` — **prereq not in course**
- U08 slot 2 `ip-addressing-and-subnetting` requires `binary-number-systems` — **prereq not in course**
- U08 slot 3 `network-configuration` requires `dns-and-dhcp-services` — **prereq not in course**
- U08 slot 5 `networking-tools` requires `tcp-udp-protocols` — **prereq not in course**
- U09 slot 1 `windows-security-settings` requires `authentication-authorization-accounting` — **prereq not in course**
- U09 slot 2 `malware-detection-and-removal` requires `behavioral-security` — **prereq not in course**
- U09 slot 3 `workstation-security-hardening` requires `device-security-practices` — **prereq not in course**
- U10 slot 1 `business-continuity-and-disaster-recovery` requires `cia-triad` — **prereq not in course**
- U10 slot 2 `data-destruction-and-disposal` requires `encryption-fundamentals` — **prereq not in course**
- U01 slot 1 `it-safety-procedures` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U03 slot 1 `hardware-components-overview` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U03 slot 2 `internal-components` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U03 slot 3 `ram-fundamentals` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U03 slot 5 `power-supplies` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U04 slot 1 `storage-technologies` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U07 slot 3 `virtualization-concepts` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U08 slot 2 `ip-addressing-and-subnetting` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U10 slot 2 `data-destruction-and-disposal` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional
- U10 slot 3 `remote-access-and-virtual-machines` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional

## 130.302 — Principles of Information Technology

- Units: **12** — Slots: **55** — Weeks declared: **22**
- **Pacing:** 55 slots, 2775 atom-minutes total, 22 declared weeks (4950 min @ 5×45 min/week). Slack for assessments/reviews: 2175 min (44%).

### Findings to review

- U01 slot 3 `documentation-and-ticketing-systems` requires `troubleshooting-methodology` — **prereq not in course**
- U04 slot 2 `windows-features-and-tools` requires `windows-editions` — **prereq not in course**
- U04 slot 4 `filesystems-and-partitioning` requires `storage-technologies` — **prereq not in course**
- U04 slot 5 `application-installation` requires `os-installation` — **prereq not in course**
- U04 slot 6 `application-architecture-and-delivery-models` requires `cloud-computing` — **prereq not in course**
- U05 slot 3 `networked-host-services` requires `tcp-udp-protocols` — **prereq not in course**
- U05 slot 5 `network-troubleshooting` requires `networking-tools` — **prereq not in course**
- U05 slot 5 `network-troubleshooting` requires `troubleshooting-methodology` — **prereq not in course**
- U06 slot 2 `behavioral-security` requires `cia-triad` — **prereq not in course**
- U06 slot 8 `malware-detection-and-removal` requires `windows-security-settings` — **prereq not in course**
- U11 slot 1 `algorithms-and-logic` requires `programming-language-categories` — **prereq appears later** at position 48
- U03 slot 3 `internal-components` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional

## Cross-course atom sharing

Total atoms used across the templates: **91**.
Atoms shared by 2+ courses: **49**.

- `ai-concepts-in-it` — in 130.303, 130.304, 130.302
- `application-installation` — in 130.303, 130.304, 130.302
- `cables-and-connectors` — in 130.303, 130.304, 130.302
- `critical-thinking-problem-solving` — in 130.303, 130.304, 130.302
- `documentation-and-ticketing-systems` — in 130.303, 130.304, 130.302
- `internal-components` — in 130.303, 130.304, 130.302
- `it-safety-procedures` — in 130.303, 130.304, 130.302
- `leadership-and-teamwork-it` — in 130.303, 130.304, 130.302
- `network-troubleshooting` — in 130.303, 130.304, 130.302
- `networking-fundamentals` — in 130.303, 130.304, 130.302
- `operating-systems-overview` — in 130.303, 130.304, 130.302
- `peripheral-devices` — in 130.303, 130.304, 130.302
- `professional-communication-it` — in 130.303, 130.304, 130.302
- `software-licensing` — in 130.303, 130.304, 130.302
- `windows-features-and-tools` — in 130.303, 130.304, 130.302
- `work-behaviors-professional-standards` — in 130.303, 130.304, 130.302
- `application-architecture-and-delivery-models` — in 130.303, 130.302
- `binary-number-systems` — in 130.303, 130.302
- `career-exploration-it-pathway` — in 130.303, 130.302
- `change-management` — in 130.303, 130.304
- `computing-units-of-measure` — in 130.303, 130.302
- `data-value-and-intellectual-property` — in 130.304, 130.302
- `display-components` — in 130.303, 130.304
- `file-management` — in 130.304, 130.302
- `filesystems-and-partitioning` — in 130.304, 130.302
- `fundamental-data-types` — in 130.303, 130.302
- `hardware-components-overview` — in 130.304, 130.302
- `input-processing-output-storage` — in 130.303, 130.302
- `internet-service-types` — in 130.303, 130.302
- `ip-addressing-and-subnetting` — in 130.303, 130.304
- `it-environmental-impacts` — in 130.303, 130.304
- `malware-detection-and-removal` — in 130.304, 130.302
- `mobile-device-hardware` — in 130.303, 130.304
- `motherboard-and-cpu-installation` — in 130.303, 130.304
- `networking-tools` — in 130.303, 130.304
- `power-supplies` — in 130.303, 130.304
- `printers-and-maintenance` — in 130.303, 130.304
- `process-management` — in 130.303, 130.304
- `ram-fundamentals` — in 130.303, 130.304
- `storage-technologies` — in 130.303, 130.304
- `troubleshoot-display` — in 130.303, 130.304
- `troubleshoot-mobile-hardware` — in 130.303, 130.304
- `troubleshoot-motherboards-ram-cpus` — in 130.303, 130.304
- `troubleshoot-printers` — in 130.303, 130.304
- `troubleshoot-storage` — in 130.303, 130.304
- `troubleshoot-windows` — in 130.303, 130.304
- `troubleshooting-methodology` — in 130.303, 130.304
- `virtualization-concepts` — in 130.303, 130.304
- `wireless-technologies` — in 130.303, 130.302