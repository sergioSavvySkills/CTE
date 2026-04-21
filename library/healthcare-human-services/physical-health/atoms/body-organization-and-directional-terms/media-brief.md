---
atom_id: body-organization-and-directional-terms
atom_serial: HHS-PH-0003
sidecar: media-brief
status: ai-draft
asset_count: 6
author: claude
reviewer:
review_date:
---

# Media brief — body-organization-and-directional-terms

A 45-minute survey of anatomical language needs a small set of
orientation-level visuals. Per-organ diagrams (heart chambers, kidney
anatomy, appendix histology) belong in each deep-dive atom, not this
one.

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | Full-body figure in anatomical position, front view, labeled with all six directional pairs (superior/inferior, anterior/posterior, medial/lateral, proximal/distal, superficial/deep, ipsilateral/contralateral) with arrows on the body. Color-safe labeling. | high | needed | create (or adapt OpenStax §1.6 figure) |
| m02 | diagram | concept | Levels-of-organization vertical stack showing chemical → cellular → tissue → organ → organ system → organism, with one worked path (e.g., water molecule → red blood cell → blood → heart → cardiovascular system → person). | high | needed | create |
| m03 | diagram | concept | Three side-by-side translucent body figures showing the three planes: sagittal (with midsagittal highlighted), frontal/coronal, and transverse. Plane orientations shown as flat translucent slabs cutting through the body. | high | needed | create (or adapt OpenStax §1.6 figure) |
| m04 | diagram | concept | Body cavities cutaway: lateral view of torso showing dorsal cavity (cranial, spinal) and ventral cavity (thoracic, abdominopelvic) with the diaphragm labeled as the dividing structure. Serous-membrane layers indicated, not detailed. | medium | needed | create |
| m05 | diagram | example | Abdomen front view with both the four-quadrant map (RUQ/LUQ/RLQ/LLQ) and the nine-region map side by side. Common organs labeled in each quadrant for the four-quadrant version. | high | needed | create |
| m06 | diagram | cfu | Unlabeled full-body figure in anatomical position with click-spots at named landmarks (elbow, knee, sternum, navel) — student must apply directional pairs to describe each spot relative to another. | medium | needed | create (interactive version of m01) |

## Accessibility requirements

- Alt text on every diagram names the planes, cavities, or directional
  pairs depicted so screen-reader users get the same semantic map as
  sighted users.
- Labels minimum 14 pt in the rendered slide; arrows use shape and
  dash pattern in addition to color so the figure reads on a
  color-blind palette.
- In m05, quadrant labels should be doubled on-screen (as both
  acronyms and full names the first time) to support students
  reading the map for the first time.
- Figures use the medical convention for left/right: label the
  patient's right side on the viewer's left (and note that
  convention in the alt text).

## Reuse notes

- **m01** (directional-pairs body figure) and **m03** (three planes)
  are high-reuse across every later anatomy atom and any medical
  imaging content. Invest in clean originals.
- **m02** (levels of organization) reuses directly in
  *body-systems-overview* and any introductory physiology atom.
- **m05** (quadrants/regions map) reuses in any atom that mentions
  abdominal pain, abdominal palpation, or GI/urinary system
  regional anatomy.
- **m06** is m01 wrapped in a click-handler; build it from the same
  source file to keep the two visuals in sync.
