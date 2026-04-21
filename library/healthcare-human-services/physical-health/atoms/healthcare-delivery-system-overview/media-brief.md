---
atom_id: healthcare-delivery-system-overview
atom_serial: HHS-PH-0014
sidecar: media-brief
status: ai-draft
asset_count: 5
author: claude
reviewer:
review_date:
---

# Media brief — healthcare-delivery-system-overview

The atom teaches how care settings, payers, and the continuum of care
fit together. Visuals are integrator diagrams — maps of how the pieces
connect — rather than per-setting deep dives.

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | Patient-journey map across one episode of care: a single patient silhouette traces through primary care → ED → inpatient → post-acute → home, with the payer mix annotated at each step. | high | needed | create |
| m02 | diagram | concept | Three-circle diagram: providers, payers, regulators. Examples listed in each circle. Overlapping regions show where one organization can play two roles (e.g., VA as provider + payer). | high | needed | create |
| m03 | diagram | concept | Continuum-of-care ribbon: preventive → primary → acute → specialty → post-acute → end-of-life, with care-transition arrows highlighted between each stage as the fragile seams. | high | needed | create |
| m04 | chart | concept | Grid of care settings vs. acuity: rows for ED, urgent care, primary care, home health, telehealth; columns for typical acuity, typical wait, relative cost. | medium | needed | create |
| m05 | diagram | example | Access-barriers map: one central patient icon surrounded by six labeled barriers (cost, geography, language, insurance, transportation, digital access), each annotated with a one-line outcome consequence. | medium | needed | create |

## Accessibility requirements

- Alt text on each diagram describes the relationship depicted, not just
  the labels — the point of an integrator diagram is the connections
- Color coding paired with shape or label differences (e.g., circles for
  providers, squares for payers, diamonds for regulators in m02) so it
  does not rely on color alone
- Labels minimum 14 pt at rendering size
- Do not rely on red-green as the only distinguishing pair

## Reuse notes

- **m02** (provider-payer-regulator circles) reuses in
  *healthcare-regulatory-agencies* and *health-economics-and-government-
  impact* with different emphasis on which circle is featured.
- **m03** (continuum ribbon) is the anchor image for this atom and
  reuses in any atom about specific transitions (discharge planning,
  post-acute handoffs).
- **m05** (access-barrier map) reuses in *cultural-competence-in-
  healthcare* and in any public-health atom.

Per-setting diagrams (a detailed ED layout, a telehealth UI, etc.)
belong in setting-specific atoms, not this integrator.
