---
atom_id: body-systems-overview
atom_serial: HHS-PH-0004
sidecar: media-brief
status: ai-draft
asset_count: 5
author: claude
reviewer:
review_date:
---

# Media brief — body-systems-overview

A 45-minute survey of eleven systems needs a small set of system-level
visuals. Per-system diagrams (nephron, alveolus, skin cross-section,
heartbeat cycle) belong in each system's deep-dive atom, not this one.

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | Labeled human-body silhouette with all 11 organ systems shown as color-coded overlays. Legible at 10-foot distance. Color-coding paired with shape/label differences for accessibility. | high | needed | create (or adapt OpenStax Fig 1.3) |
| m02 | diagram | concept | Levels of organization: cell → tissue → organ → organ system → organism, shown as a vertical stack of five tiles. | medium | needed | create |
| m03 | diagram | concept | System-interaction diagram: blood-pressure regulation. Cardiovascular, nervous, endocrine, and urinary systems shown as four nodes with labeled arrows between them. | high | needed | create |
| m04 | chart | example | Vital-signs display for the infected-cut example (temp, HR, RR, BP) with normal values shown alongside the patient's values. | medium | needed | create |
| m05 | diagram | cfu | Interactive version of m01 — student clicks an organ and the diagram identifies which system(s) it belongs to. | medium | needed | create (interactive version of m01) |

## Accessibility requirements

- Alt text on every diagram names the system(s) shown and the key
  structures labeled
- Color-coding pairs with shape or label differences (color-blind safe);
  do not rely on color alone in m01
- Labels minimum 14 pt in the rendered slide
- Do not use red-green as the only distinguishing color pair

## Reuse notes

- **m01** (11-system body silhouette) is the anchor image for the whole
  HHS-PH sub-cluster and will appear in almost every downstream atom.
  Worth investing in a clean original rather than licensing.
- **m02** (levels of organization) reuses in *body-organization-and-
  directional-terms* and any early anatomy course.
- **m03** (BP interaction diagram) is a template that other system-
  interaction atoms can reuse with different node sets.
- **m05** is m01 wrapped in a click-handler. Build it from the same
  source file.
