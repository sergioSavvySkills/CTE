# Schema — `media-brief.md`

Specification for images, videos, diagrams, and animations that a lesson
generator needs for this atom's slides. The brief tells a media librarian
(human or AI) what visuals to source, which ones exist, and which need
creation.

## Front-matter

```yaml
---
atom_id: <matches parent atom>
atom_serial: <matches parent atom>
sidecar: media-brief
status: ai-draft | reviewed | published
asset_count: <integer>
---
```

## Sections

### `## Visuals needed`

A markdown table. One row per asset:

| id | type | purpose | description | priority | status | source |
|---|---|---|---|---|---|---|
| m01 | diagram | hook | A labeled silhouette of the human body showing the 11 organ systems as colored overlays | high | needed | create |
| m02 | photo | concept | A healthy dermal cross-section showing the three skin layers | medium | needed | license |
| m03 | video | example | 30-second animation of a heartbeat cycle, labeled | high | exists | openstax-ap-fig-19-11 |

Column spec:

- `id` — atom-local, m01 m02 m03...
- `type` — diagram | photo | video | animation | audio | chart
- `purpose` — hook | concept | example | cfu | vocab | media-only-slide
- `description` — enough detail to search for or brief a designer
- `priority` — high (lesson fails without it) | medium | low (nice-to-have)
- `status` — needed | exists | in-progress
- `source` — create | license | <catalog-id> | <URL>

### `## Accessibility requirements`

Per-asset alt text guidance, captioning requirements, color-blind-safe
palette notes, audio-description needs.

### `## Reuse notes`

Which of these assets will other atoms likely reuse? (Helps avoid
re-licensing / re-creating the same diagram across 3 atoms.)

## Count

Roughly 1 asset per 2-3 slides of lesson. For a 45-minute atom, expect
4-8 visual assets briefed. Per-system or per-concept diagrams belong in
the deep-dive atom for that system or concept, not in a survey atom.
