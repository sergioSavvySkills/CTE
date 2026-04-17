# Texas IT Support — SME Review

Automated first-pass review of the three Texas course templates.
Surfaces items a human SME (Maya) should confirm before promoting
any template to `status: active`. Not every finding is a defect —
some are intentional design choices that just need a sign-off.

## How to read the findings

**`prereq appears later`** — Real ordering bug within a course; a slot
uses an atom whose prereq hasn't been taught yet. These were reduced
from 14 to the current count by reordering. Any remaining ones are
mostly caused by atom-level `prerequisites:` metadata that may itself
be reversed (e.g., `filesystems-and-partitioning` lists
`file-management` as a prereq, but pedagogically files come first).
Maya: confirm whether to flip the atom metadata or just tolerate.

**`prereq not in course`** — Usually expected cross-course coupling.
130.303 and 130.304 run concurrently, so either can supply prereqs
the other lists. A 130.303 atom listing `hardware-components-overview`
as a prereq is fine because the student is simultaneously taking
130.304 where that atom sits in U03. Review these only when the
listed prereq wouldn't have been covered by any co-requisite course.

**`skill_type=knowledge` forces `simulation: true`** (130.304 only)
— Design intent, not a defect. The Lab template deliberately runs
simulations over knowledge atoms because that's how the hands-on
half of the pair differs from the theory half. Confirm and move on.

**`skill_type=skill` with `simulation: false`** (130.303 only) —
Also design intent for the same reason: the theory template runs
lessons and videos; the companion Lab template runs the simulation.

## 130.302 — Principles of IT

- Units: **12** — Slots: **55** — Weeks declared: **23**
- **Pacing:** 55 slots, 2775 atom-minutes total, 23 declared weeks (5175 min @ 5×45 min/week). Slack for assessments/reviews/performance tasks: 2400 min (46%).

### Findings to review

- U01 slot 7 `documentation-and-ticketing-systems` requires `troubleshooting-methodology` — **prereq not in course**
- U04 slot 2 `windows-features-and-tools` requires `windows-editions` — **prereq not in course**
- U04 slot 4 `filesystems-and-partitioning` requires `storage-technologies` — **prereq not in course**
- U04 slot 5 `application-installation` requires `os-installation` — **prereq not in course**
- U04 slot 6 `application-architecture-and-delivery-models` requires `cloud-computing` — **prereq not in course**
- U05 slot 3 `networked-host-services` requires `tcp-udp-protocols` — **prereq not in course**
- U05 slot 5 `network-troubleshooting` requires `networking-tools` — **prereq not in course**
- U05 slot 5 `network-troubleshooting` requires `troubleshooting-methodology` — **prereq not in course**
- U06 slot 2 `behavioral-security` requires `cia-triad` — **prereq not in course**
- U06 slot 8 `malware-detection-and-removal` requires `windows-security-settings` — **prereq not in course**
- U11 slot 1 `algorithms-and-logic` requires `programming-language-categories` — **prereq appears later** at position 49
- U03 slot 3 `internal-components` (skill_type=knowledge) forces `simulation: true` — unusual; confirm this is intentional

## 130.303 — Computer Maintenance

- Units: **11** — Slots: **50** — Weeks declared: **19**
- **Pacing:** 50 slots, 2535 atom-minutes total, 19 declared weeks (4275 min @ 5×45 min/week). Slack for assessments/reviews/performance tasks: 1740 min (41%).

### Findings to review

- U04 slot 1 `internal-components` requires `hardware-components-overview` — **prereq not in course**
- U04 slot 4 `troubleshoot-motherboards-ram-cpus` requires `power-supplies` — **prereq appears later** at position 22
- U05 slot 2 `troubleshoot-storage` requires `filesystems-and-partitioning` — **prereq not in course**
- U05 slot 3 `display-components` requires `hardware-components-overview` — **prereq not in course**
- U05 slot 4 `troubleshoot-display` requires `cables-and-connectors` — **prereq appears later** at position 24
- U05 slot 5 `power-supplies` requires `hardware-components-overview` — **prereq not in course**
- U06 slot 1 `peripheral-devices` requires `hardware-components-overview` — **prereq not in course**
- U06 slot 2 `cables-and-connectors` requires `hardware-components-overview` — **prereq not in course**
- U07 slot 1 `mobile-device-hardware` requires `hardware-components-overview` — **prereq not in course**
- U08 slot 6 `linux-features` requires `file-management` — **prereq not in course**
- U08 slot 8 `troubleshoot-windows` requires `windows-cli` — **prereq not in course**
- U09 slot 1 `application-installation` requires `os-installation` — **prereq not in course**
- U09 slot 2 `software-licensing` requires `data-value-and-intellectual-property` — **prereq not in course**
- U09 slot 3 `virtualization-concepts` requires `hardware-components-overview` — **prereq not in course**
- U09 slot 4 `cloud-computing` requires `networking-fundamentals` — **prereq appears later** at position 42
- U10 slot 6 `networking-tools` requires `network-configuration` — **prereq not in course**
- U11 slot 2 `it-environmental-impacts` requires `data-destruction-and-disposal` — **prereq not in course**
- U02 slot 1 `troubleshooting-methodology` (skill_type=both) has `simulation: false` — skill atom losing its hands-on component
- U04 slot 3 `motherboard-and-cpu-installation` (skill_type=skill) has `simulation: false` — skill atom losing its hands-on component

## 130.304 — CM Lab

- Units: **10** — Slots: **51** — Weeks declared: **20**
- **Pacing:** 51 slots, 2670 atom-minutes total, 20 declared weeks (4500 min @ 5×45 min/week). Slack for assessments/reviews/performance tasks: 1830 min (41%).

### Findings to review

- U01 slot 4 `change-management` requires `documentation-and-ticketing-systems` — **prereq appears later** at position 9
- U03 slot 1 `hardware-components-overview` requires `input-processing-output-storage` — **prereq not in course**
- U04 slot 1 `storage-technologies` requires `computing-units-of-measure` — **prereq not in course**
- U04 slot 2 `filesystems-and-partitioning` requires `file-management` — **prereq appears later** at position 32
- U05 slot 3 `troubleshoot-mobile-os` requires `operating-systems-overview` — **prereq appears later** at position 29
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

## Cross-course atom sharing

Total atoms used across the three courses: **91** (out of ~110 in the library).
Atoms shared by 2+ courses: **49**.

Expected: the 130.303 / 130.304 pair shares nearly all atoms by design
(concurrent theory + lab). Atoms appearing in 130.302 **and** either
CM course are crossover foundations (soft skills, safety, basic hardware).
Unexpected: any atom in all three courses that isn't foundational.

- `ai-concepts-in-it` — in 130.302, 130.303, 130.304
- `application-installation` — in 130.302, 130.303, 130.304
- `cables-and-connectors` — in 130.302, 130.303, 130.304
- `critical-thinking-problem-solving` — in 130.302, 130.303, 130.304
- `documentation-and-ticketing-systems` — in 130.302, 130.303, 130.304
- `internal-components` — in 130.302, 130.303, 130.304
- `it-safety-procedures` — in 130.302, 130.303, 130.304
- `leadership-and-teamwork-it` — in 130.302, 130.303, 130.304
- `network-troubleshooting` — in 130.302, 130.303, 130.304
- `networking-fundamentals` — in 130.302, 130.303, 130.304
- `operating-systems-overview` — in 130.302, 130.303, 130.304
- `peripheral-devices` — in 130.302, 130.303, 130.304
- `professional-communication-it` — in 130.302, 130.303, 130.304
- `software-licensing` — in 130.302, 130.303, 130.304
- `windows-features-and-tools` — in 130.302, 130.303, 130.304
- `work-behaviors-professional-standards` — in 130.302, 130.303, 130.304
- `application-architecture-and-delivery-models` — in 130.302, 130.303
- `binary-number-systems` — in 130.302, 130.303
- `career-exploration-it-pathway` — in 130.302, 130.303
- `change-management` — in 130.303, 130.304
- `computing-units-of-measure` — in 130.302, 130.303
- `data-value-and-intellectual-property` — in 130.302, 130.304
- `display-components` — in 130.303, 130.304
- `file-management` — in 130.302, 130.304
- `filesystems-and-partitioning` — in 130.302, 130.304
- `fundamental-data-types` — in 130.302, 130.303
- `hardware-components-overview` — in 130.302, 130.304
- `input-processing-output-storage` — in 130.302, 130.303
- `internet-service-types` — in 130.302, 130.303
- `ip-addressing-and-subnetting` — in 130.303, 130.304
- `it-environmental-impacts` — in 130.303, 130.304
- `malware-detection-and-removal` — in 130.302, 130.304
- `mobile-device-hardware` — in 130.303, 130.304
- `motherboard-and-cpu-installation` — in 130.303, 130.304
- `networking-tools` — in 130.303, 130.304
- `power-supplies` — in 130.303, 130.304
- `printers-and-maintenance` — in 130.303, 130.304
- `process-management` — in 130.303, 130.304
- `ram-fundamentals` — in 130.303, 130.304
- `storage-technologies` — in 130.303, 130.304
- ...and 9 more