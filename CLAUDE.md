# CTE repo — Claude working preferences

## Lesson length

Standard lesson length is **45 minutes to 1 hour**. Default to this range when drafting or sequencing lessons unless the user specifies otherwise. Dense or high-stakes standards (clinical math, safety culture, malpractice elements) may warrant 60–90 min — call it out explicitly when proposing longer blocks.

## Standards files

Each §127.403 standard file under `library/healthcare-human-services/physical-health/texas/standards/` follows this section order:

1. Front-matter (YAML)
2. `## Learning objective`
3. `## Content stub`
4. `## Vocabulary` — 6–12 terms; `**Term** — one-line definition.` with optional trailing `*(also in cXY)*` cross-ref, capped at 2 refs per annotation.
5. `## Assessment stub`
6. `## Activities` — 2+ classroom sims; each a bold name + one-paragraph evocative description + italic goal tags (application, pattern recognition, decision under constraint, systems thinking, etc.). Sims are delivered as plain HTML + CDN libraries; prefer vanilla, only reach for a library if its output is visually polished out of the box.
7. `## References`
8. `## Activity specs` — detailed YAML spec per activity, appended at end of file. Each spec covers name, format, supports, duration/mode/equipment, learning_goal, vocab_exercised, content_model, content, initial_state, controls, feedback, scoring, win_condition, reset, student_view, teacher_view, accessibility, success_criteria, tech_stack, ai_required, visual_notes — followed by **Instructions to student** and **Teacher notes** paragraphs. The `ai_required` field is a list (possibly empty) of `{category, reason, fallback}` objects; supported categories are `text_rubric_scoring` and `tts`. **Out of scope:** `stt` (speech-to-text) and `pose` (webcam pose detection) are not supported — design activities around typed text and pre-generated audio / animation instead of voice capture or body tracking. An empty list means the sim runs on regex, keyword match, and numeric logic alone.

Preserve this order when editing.

## AI-required field schema

Every `ai_required` entry carries the three base fields (`category`, `reason`, `fallback`) plus category-specific execution fields so a downstream generator has everything it needs to build the sim.

**For `text_rubric_scoring`** — add these fields:
- `dimensions` — list of rubric dimensions that need AI scoring (the rest of the rubric is deterministic and runs client-side).
- `deterministic_dimensions` — rubric dimensions scored by regex, keyword match, or numeric heuristics (word count, reading grade, banned-phrase check).
- `prompt_template` — reference to a shared prompt template in `activities/ai-prompts/` (e.g., `text-rubric-v1`).
- `output_schema` — structured description of the JSON the AI must return (`scores: map<dimension, int 0-5>`, `diagnostics: map<dimension, string>`).
- `model` — target model (default `claude-haiku-4-5`).
- `max_tokens` — output token budget for cost control.
- `content_file` — path under `activities/content/` pointing to the YAML file containing the actual source material (source notes, gold answers, banned phrases, required facts).

**For `tts`** — add these fields:
- `scripts_file` — path under `activities/content/` pointing to the YAML file containing every script line to synthesize.
- `voice_profile` — object: `{persona, gender, age_band, accent}`. Persona values include `clinician`, `patient`, `family_member`, `narrator`, `unit_clerk`. Accent uses a locale tag (`en-US general`, `es-MX`, etc.).
- `pacing` — one of `natural`, `measured`, `urgent`.
- `output_format` — `mp3` by default.
- `sample_rate` — integer, default `24000`.
- `filename_pattern` — format string the generator uses to name output files (e.g., `c2d-incident-{index:02d}.mp3`).

All extended fields are optional at the YAML-parser level — a spec without them parses fine and signals "AI instructions still owed." A generator sees the missing fields and either warns or refuses to build; that explicit unknown state is safer than silent guessing.

## Activity content and AI-prompt layout

Source material and prompt templates live under `library/healthcare-human-services/physical-health/texas/activities/`:

- `activities/content/<sim-slug>.yaml` — per-activity source material (source notes, gold answers, scenario scripts, banned phrases). One file per activity; use a subdirectory when an activity needs both rubric content and TTS scripts (e.g., `c2D-incident-report-generator/`).
- `activities/ai-prompts/` — shared prompt templates (`text-rubric-v1.md` etc.) plus a `README.md` describing the template authoring contract. Templates are versioned by name so prompt changes don't silently break specs pinned to an older version.

## Transversal standards

`127.403-c1B`, `127.403-c1C`, and `127.403-c4C` are transversal — behavior standards reinforced across every lesson, not taught in a dedicated session. Their front-matter carries a `reinforced_by:` list of host standards where the behavior gets surfaced.
