---
atom_id: common-medical-abbreviations
atom_serial: HHS-PH-0005
sidecar: media-brief
status: ai-draft
asset_count: 6
author: claude
reviewer:
review_date:
---

# Media brief — common-medical-abbreviations

A 45-minute documentation atom needs visuals that show shorthand in
context and make the do-not-use patterns visually distinct. Exhaustive
abbreviation glossaries and drug-pharmacology visuals belong to other
atoms, not this one.

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | Side-by-side reproduction of two handwritten order lines — *Insulin 4U stat* and *Insulin 4 units stat* — annotated to show how the letter U can be misread as a zero. High-contrast, legible at classroom projection. | high | needed | create |
| m02 | chart | concept | One-page reference card of the Joint Commission do-not-use list: each banned form in the left column, the reason it was banned in the middle, the safe rewrite in the right column. | high | needed | create (adapt from TJC-DoNotUse fact sheet, CC-compatible redraw) |
| m03 | diagram | concept | A 2x2 decimal-discipline grid contrasting *1.0 mg vs 1 mg* (trailing zero) and *.5 mg vs 0.5 mg* (leading zero), each cell showing the misread risk in red and the safe form in green. | high | needed | create |
| m04 | chart | vocab | Categorized shorthand table organized by slot — frequency, route, status, orders/procedures — with 4-6 representative abbreviations per slot and a plain-English gloss for each. | medium | needed | create |
| m05 | diagram | example | Before/after sample order sheet illustrating Example 2 from examples.md: the original sheet with 4 do-not-use violations circled, and the rewritten safe version shown alongside. | medium | needed | create |
| m06 | diagram | cfu | Three-step habit flowchart — *Recognize → Look up → Avoid the banned forms* — presented as a decision diagram a student can trace with their finger while reading an order. | medium | needed | create |

## Accessibility requirements

- Alt text on every image names the abbreviations shown and the
  intended safe rewrite.
- Red/green color-coding in m03 and m05 must be paired with a shape or
  label cue (e.g., an X for banned, a check for safe) so color-blind
  readers can distinguish the cells without color.
- Handwriting in m01 must be legible at 10-foot distance; labels on
  m02 and m04 must be at least 14 pt.
- Any facsimile of a real-looking order must show a fictitious patient
  name and medical-record number to avoid privacy associations.

## Reuse notes

- **m02** (do-not-use reference card) will also be referenced by the
  *Medication administration and the rights of drug administration*
  atom — worth designing for print-at-workstation use.
- **m06** (recognize-look up-avoid flowchart) is a generic safe-charting
  habit diagram; downstream documentation atoms (vital-signs charting,
  handoff communication) can reuse it verbatim.
- **m04** (categorized shorthand table) is a candidate for a printable
  pocket card students can carry through clinical rotations.
