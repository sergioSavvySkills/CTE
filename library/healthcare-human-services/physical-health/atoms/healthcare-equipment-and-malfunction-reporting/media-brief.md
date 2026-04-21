---
atom_id: healthcare-equipment-and-malfunction-reporting
atom_serial: HHS-PH-0015
sidecar: media-brief
status: ai-draft
asset_count: 6
author: claude
reviewer:
review_date:
---

# Media brief — healthcare-equipment-and-malfunction-reporting

A 45-minute foundational atom about equipment categories and the
reporting workflow. Visuals should help students (a) recognize that
equipment falls into five predictable categories, (b) spot the
visible signs of malfunction, and (c) follow the layered reporting
path from bedside to FDA. Vendor-specific UI screenshots,
imaging-physics diagrams, analyzer-chemistry schematics, and
circuit-board teardowns belong to other atoms, not this one.

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | A five-panel "equipment across the five health science systems" poster: diagnostic (imaging + lab analyzer + EKG + glucose meter), therapeutic (IV pump + ventilator + AED + hospital bed), informatics (EHR workstation + barcode scanner + telemetry monitor), support services (sterilizer + HVAC/HEPA + call-light panel), biotech R&D (centrifuge + PCR thermocycler + biosafety cabinet). Each panel has 3-5 line-drawn, labeled devices on a color-coded background. | high | needed | create |
| m02 | chart | concept | "Signs of malfunction" reference card with five rows: alarms, error codes, abnormal readings, physical damage, unexpected behavior. Each row shows a one-line example and a simple icon (speaker for alarm, code text for error code, question-mark reading for abnormal value, cracked-case silhouette for physical damage, shuffled arrows for unexpected behavior). | high | needed | create |
| m03 | diagram | concept | Reporting-workflow flowchart from bedside to FDA: discovery at bedside -> switch to backup / stop use -> attach 'Do Not Use' lockout tag -> submit work order (to biomed) -> if patient involved, file incident report (to risk management) -> if serious injury or death, facility files MDR (to FDA) -> if pattern confirmed across facilities, FDA + manufacturer issue recall. Three swim lanes: clinician, facility (biomed + risk management), FDA. | high | needed | create |
| m04 | photo | example | Reference photos (or detailed illustrations) of three real "Do Not Use" lockout tags in context — one on an IV pump, one on a sterilizer door, one on a hallway AED. Tag text legible; device clearly out of use location. | medium | needed | license |
| m05 | diagram | example | Annotated "AED shift check" infographic illustrating Example 4: an AED on a wall bracket with a red status light and error code circled, the swap to a backup unit, and the broken unit in a biomed drop-off bin with a work-order card attached. | medium | needed | create |
| m06 | chart | cfu | Four-quadrant "common mistakes" card mapping to the atom's four misconceptions: silence alarm = fix (wrong), cosmetic damage is okay (wrong), reporting is one step (wrong), FDA is only pre-market (wrong) — each quadrant with the one-sentence correction and the verb the student should internalize (READ, TAG, ROUTE, ESCALATE). | medium | needed | create |

## Accessibility requirements

- Alt text on every image names the category panel or error pattern
  shown and the intended safe-practice takeaway (not just "photo of
  an IV pump").
- Color-coding in m01 (five system categories) and m03 (three swim
  lanes) must be paired with a label or shape cue so color-blind
  readers can distinguish categories without relying on color alone.
- The flowchart arrows in m03 must be thick enough to read at
  classroom projection distance; every box needs a text label, not
  just an icon.
- Any lockout-tag photograph in m04 must show the full "Do Not Use"
  wording clearly; a blurry tag defeats the visual's teaching point.
- The AED status-light illustration in m05 must show both the red
  and the green state so the malfunction signal is visible, not
  implied.
- Captions under each quadrant of m06 must state the correction in
  a full sentence (not just "wrong!") so screen-reader output still
  teaches the correct model.

## Reuse notes

- **m01** (five-system equipment poster) is the canonical category
  map for this atom and is a strong candidate for reuse in the
  intro-to-healthcare-careers survey atom and the five-system
  overview atom; design it so individual category panels can be
  extracted and cropped.
- **m02** (signs-of-malfunction card) is usable as a printable pocket
  card for clinical rotations; any later atom on safe-equipment
  habits (e.g., PPE inspection) can reuse the five-signal structure.
- **m03** (reporting-workflow flowchart) will be referenced by the
  future medical-device-regulation atom and the patient-safety-and-
  reporting atom; build it with modular blocks so the FDA-facing
  end can be swapped if a more regulation-specific version is
  needed later.
- **m06** (common-mistakes poster) encodes this atom's
  misconceptions; a later quality-and-safety survey atom can reuse
  the four-quadrant format with different content.
