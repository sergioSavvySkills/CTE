---
atom_id: electronic-health-records-basics
atom_serial: HHS-PH-0008
sidecar: media-brief
status: ai-draft
asset_count: 6
author: claude
reviewer:
review_date:
---

# Media brief — electronic-health-records-basics

A 45-minute EHR-basics atom needs visuals that show the chart's
section layout, the access-logging backbone, and the named error
patterns in context. Vendor-specific UI screenshots, pharmacology
visuals, FHIR-payload schematics, and coding/billing diagrams belong
to other atoms, not this one.

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | Vendor-neutral schematic of an EHR chart — a labeled "dashboard" showing the eight or nine common section panels (demographics, problem list, allergies, medications, orders, progress notes, results, flowsheet, imaging). No real patient data; fictitious name and MRN. | high | needed | create |
| m02 | diagram | concept | Side-by-side contrast of EMR vs EHR: left panel shows a single clinic's chart siloed behind its walls; right panel shows a longitudinal record flowing between primary care, hospital, specialist, and patient portal, with arrows labeled "interoperability". | high | needed | create |
| m03 | chart | concept | One-page reference card of the four safe-documentation rules (objective language, time-stamped entries, correct-not-erase, every entry signed), each with a one-line example of compliant vs non-compliant text. | high | needed | create |
| m04 | diagram | concept | Access-controls diagram: a clinician login tied to a user icon, role-based permissions shown as different-colored keys, and an audit-log tape rolling beneath the chart showing "user X opened chart at time T". | high | needed | create |
| m05 | diagram | example | Annotated before/after progress note illustrating Example 3 from examples.md: the original note with pasted prior-admission HPI highlighted in red, and the amended note reflecting today's heart-failure presentation in green alongside. | medium | needed | create |
| m06 | chart | cfu | Four-quadrant "common EHR errors" poster: copy-paste error, wrong-patient error, alert fatigue, and upcoding, each quadrant with a one-sentence description and a single-habit fix. | medium | needed | create |

## Accessibility requirements

- Alt text on every image names the chart sections or error patterns
  shown and the intended safe-practice takeaway.
- Any facsimile of a chart must use fictitious patient names and
  medical record numbers to avoid privacy associations.
- Red/green color coding in m05 must be paired with a shape or label
  cue (e.g., a strikethrough for stale text, a check for corrected
  text) so color-blind readers can distinguish the versions without
  relying on color alone.
- Labels on m01, m03, and m06 must be at least 14 pt and legible at
  classroom projection distance.
- The audit-log tape in m04 should be readable at normal slide
  distance — avoid small font for the user/time stamps.

## Reuse notes

- **m01** (chart-section schematic) will also be referenced by
  downstream atoms on vital-signs charting, medication
  administration, and handoff communication — worth designing as a
  canonical, reusable diagram.
- **m03** (safe-documentation rules card) is a candidate for a
  printable pocket card students can carry through clinical
  rotations.
- **m04** (access-controls diagram) will be cited back from the
  prerequisite HIPAA atom's sidecar when that atom is refreshed; the
  audit-log tape motif should be portable to that context.
- **m06** (common EHR errors) is a generic safe-charting-habit poster
  that lesson designers for later documentation atoms can reuse
  verbatim.
