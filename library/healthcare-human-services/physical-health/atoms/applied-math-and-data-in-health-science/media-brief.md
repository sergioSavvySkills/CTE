---
atom_id: applied-math-and-data-in-health-science
atom_serial: HHS-PH-0001
sidecar: media-brief
status: ai-draft
asset_count: 5
author: claude
reviewer:
review_date:
---

# Media brief — applied-math-and-data-in-health-science

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | Side-by-side conversion reference: pounds↔kilograms, °F↔°C, fl oz↔mL, in↔cm. Clean pocket-card layout with formula and one example each. | high | needed | create |
| m02 | chart | example | Sample CDC growth chart for a 2-year-old showing percentile curves; overlay the trajectory from Example 4 (75th → 50th → 25th) with annotations. | high | needed | adapt (CDC-GrowthCharts is public domain) |
| m03 | chart | example | Glucose trend graph for Example 3: four daily fingerstick readings plotted against a reference-range band (70–99 mg/dL shaded green, > 126 shaded red). | medium | needed | create |
| m04 | diagram | cfu | Decimal-discipline do / don't card: side-by-side good vs. bad forms (0.5 vs .5; 1 vs 1.0) with one-sentence error story for each. | high | needed | create |
| m05 | diagram | example | Weight-based dosing workflow: 4 boxes (patient weight in lb → convert to kg → multiply by mg/kg → sanity-check against reference range), with Example 1 numbers filled in. | medium | needed | create |

## Accessibility requirements

- Alt text on each asset states the specific conversion, trend, or workflow depicted
- Color coding in m03 (reference-range band) must pair with pattern/label so it does not rely on color alone
- Labels minimum 14 pt
- Do not use red-green as the sole distinguishing pair in m04

## Reuse notes

- **m01** (conversion reference card) reuses in any atom that involves
  patient measurements — vital-signs overview, pharmacology atoms.
- **m04** (decimal-discipline card) reuses in *common-medical-
  abbreviations* and any medication-safety content.
- **m05** (weight-based dosing workflow) reuses in pharmacology atoms.
