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
6. `## Activities` — 2+ classroom sims, listed as a bold name + italic goal tags only (application, pattern recognition, decision under constraint, systems thinking, etc.). The evocative description moves down to sit above each activity's User journey in `## Activity specs`. Sims are delivered as plain HTML + CDN libraries; prefer vanilla, only reach for a library if its output is visually polished out of the box.
7. `## References`
8. `## Activity specs` — per activity, in order: (a) short evocative description paragraph, (b) `**User journey**` numbered step list showing what the student sees end-to-end (AI review points marked inline as `→ AI review: <dimension>, ~<seconds>s, <fallback>`), (c) YAML spec, (d) `**Instructions:**` paragraph written for the student. The YAML spec covers name, format, supports, duration/mode/equipment, learning_goal, vocab_exercised, content_model, content, initial_state, controls, feedback, result, student_view, accessibility, success_criteria, tech_stack, ai_required, visual_notes. Sims are student-facing only — no `teacher_view` field, no teacher-notes paragraph. The `ai_required` field is a list (possibly empty) of `{category, reason, fallback}` objects; supported categories are `text_rubric_scoring` and `tts`. **Out of scope:** `stt` (speech-to-text) and `pose` (webcam pose detection) are not supported — design activities around typed text and pre-generated audio / animation instead of voice capture or body tracking. An empty list means the sim runs on regex, keyword match, and numeric logic alone.

Preserve this order when editing.

## Activity scoring

Activities are **pass/fail**, not rubric-scored. Every spec's `result:` block has two fields:

- `pass_rule` — one or two sentences, plain English, describing the pass condition.
- `instructions_for_scorer` — the deterministic (or near-deterministic) steps a grader or sim follows to decide pass/fail. Default to regex, keyword match, sentence count, numeric thresholds.

Keep thresholds **forgiving**. The point is pattern practice, not ranking — a student who mostly got it should pass. Retries on a fresh case or passage are always fine. Nuance (audience fit, clarity, judgment calls) belongs in the teacher debrief, not the score. Do not add point totals, 0–5 rubrics, `mastery_threshold`, `win_condition`, or `reset` blocks — they bureaucratize what should feel like a game.

## AI-required field schema

Most activities score deterministically and keep `ai_required: []`. Only add an AI block when the pass rule genuinely requires semantic judgment (e.g., meaning preservation across freeform paraphrase) and no regex, keyword match, or numeric heuristic can decide the case. When you do add one, every `ai_required` entry carries the three base fields (`category`, `reason`, `fallback`) plus category-specific execution fields so a downstream generator has everything it needs to build the sim.

**For `text_rubric_scoring`** — add these fields:
- `dimensions` — list of dimensions the AI is asked to judge. Keep it tight; one dimension per call is usually enough. Deterministic pass rules live in the `result:` block, not here.
- `prompt_template` — reference to a shared prompt template in `activities/ai-prompts/` (e.g., `text-rubric-v1`).
- `output_schema` — structured description of the JSON the AI must return (default: `scores: map<dimension, pass|fail>`, `diagnostics: map<dimension, string one-line>`).
- `model` — target model (default `claude-haiku-4-5`).
- `max_tokens` — output token budget for cost control.
- `invoked_at` — when in the flow the AI call fires (e.g., `on_submit_after_deterministic_checks`). The same moment must appear as a labeled step in the User journey so the AI role is a visible part of the flow, not buried metadata.

**For `tts`** — add these fields:
- `voice_profile` — object: `{persona, gender, age_band, accent}`. Persona values include `clinician`, `patient`, `family_member`, `narrator`, `unit_clerk`. Accent uses a locale tag (`en-US general`, `es-MX`, etc.).
- `pacing` — one of `natural`, `measured`, `urgent`.
- `output_format` — `mp3` by default.
- `sample_rate` — integer, default `24000`.
- `filename_pattern` — format string the generator uses to name output files (e.g., `c2d-incident-{index:02d}.mp3`).

All extended fields are optional at the YAML-parser level — a spec without them parses fine and signals "AI instructions still owed." A generator sees the missing fields and either warns or refuses to build; that explicit unknown state is safer than silent guessing.

## Activity content

Per-activity source material (source notes, gold answers, scenario scripts, TTS script lines, required facts, banned phrases) lives **inline** in the spec's `content:` block in the standards file. No separate content files. Keep scannable blocks at the top of `content:` describing what each entry provides; append populated lists (`notes: []`, `passages: []`, `scripts: []`, etc.) when authoring.

## AI prompt templates

Shared AI prompt templates live under `library/healthcare-human-services/physical-health/texas/activities/ai-prompts/`. Template files (`text-rubric-v1.md` etc.) plus a `README.md` describing the template authoring contract. Templates are versioned by name so prompt changes don't silently break specs pinned to an older version. Prompts are shared across activities (all `text_rubric_scoring` specs currently pin to `text-rubric-v1`), so they live in a shared directory rather than inline.

## Transversal standards

`127.403-c1B`, `127.403-c1C`, and `127.403-c4C` are transversal — behavior standards reinforced across every lesson, not taught in a dedicated session. Their front-matter carries a `reinforced_by:` list of host standards where the behavior gets surfaced.
