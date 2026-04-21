---
atom_id: hand-hygiene-technique
atom_serial: HHS-PH-0011
sidecar: media-brief
status: ai-draft
asset_count: 6
author: claude
reviewer:
review_date:
---

# Media brief — hand-hygiene-technique

## Visuals needed

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | concept | The WHO Five Moments poster: a patient-centered diagram with the patient in a silhouetted bed inside a dashed "patient zone" circle, five numbered arrows labeled Moment 1 through Moment 5 showing where each indication sits relative to the patient and surroundings. | high | exists | WHO-FiveMoments (license from WHO — free for educational use) |
| m02 | video | example | 45–60 second timed demonstration of correct ABHR technique: palm-full volume, six-step rub (palms, backs, interlaced fingers, thumbs, fingertips into opposite palm, wrists), on-screen 20-second timer, ending at fully dry. | high | needed | create |
| m03 | video | example | 45–60 second timed demonstration of correct soap-and-water handwash: wet, lather, 20-second scrub across all surfaces, rinse fingertips-down, paper-towel dry, turn off tap with towel. | high | needed | create |
| m04 | diagram | cfu | Decision flow "Which technique?": entry question "Are hands visibly soiled?" then "Is the patient on C. diff or norovirus precautions?" then "Did you just use the restroom?" — any yes routes to soap-and-water; all no routes to ABHR. | high | needed | create |
| m05 | diagram | concept | "Commonly missed surfaces" hand illustration: front and back of both hands with thumbs, fingertips/nails, and wrists highlighted in a contrast color, showing the areas that fail an ABHR fluorescent-dye test. | medium | needed | create |
| m06 | photo | vocab | Side-by-side photo set of typical clinical dispensers: wall-mounted ABHR dispenser, sink with soap dispenser and paper-towel holder, and a bedside-mounted ABHR pump. Labels name each. | medium | needed | license or create |

## Accessibility requirements

- Alt text on each asset names the specific concept (e.g., "WHO Five
  Moments diagram showing five numbered indications around a
  patient") rather than generic phrases like "hand-washing image"
- In m04 (decision flow), yes/no paths must differ in shape or line
  style as well as color so the distinction survives grayscale
  printing
- Videos (m02, m03) require closed captions naming each surface as
  it is cleaned and an on-screen 20-second countdown visible to
  low-vision viewers
- Demonstration videos should depict workers of varied skin tones
  and hand sizes; the technique applies regardless
- Text labels minimum 14 pt, high-contrast against background

## Reuse notes

- **m01** (Five Moments diagram) will reuse in any atom that covers
  infection prevention in a clinical workflow — standard precautions,
  PPE sequencing, wound care
- **m04** (technique decision flow) reuses in isolation-precautions
  and outbreak-response atoms
- **m05** (missed surfaces) reuses in any skill-check or simulation
  atom that references hand-hygiene observation
- **m02** and **m03** (technique demos) are canonical assets; any
  downstream clinical-skills atom that references hand hygiene
  should link to these rather than re-shooting
