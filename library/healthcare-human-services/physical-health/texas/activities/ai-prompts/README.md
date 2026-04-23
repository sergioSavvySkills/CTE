# Activity AI prompt templates

This directory holds the prompt templates that sims call into when their spec declares an `ai_required` category that needs text scoring (currently only `text_rubric_scoring` — TTS is handled by the voice service, not a prompt template). One template file per prompt version; specs reference a template by name (`prompt_template: text-rubric-v1`).

## File naming

Templates are named `<category>-v<version>.md`:

- `text-rubric-v1.md` — generic text_rubric_scoring prompt body
- `text-rubric-v1.examples.md` — canonical few-shot examples paired with the template

Version the name when you change the prompt. Specs pin to a specific version so prompt drift doesn't silently change scoring behavior across the course.

## Template contract

Every template must:

1. **Accept these substitution variables** (a generator fills them in from the spec + content file at call time):
   - `{dimensions}` — list of rubric dimensions to score (from the spec's `ai_required.dimensions`)
   - `{dimension_rubric}` — per-dimension scoring definitions and 5-/3-/1-point examples (from the activity's content file)
   - `{gold_answer}` — the canonical correct answer (from the content file)
   - `{student_response}` — what the student typed
   - `{required_facts}` / `{banned_phrases}` — passed through so the AI stays on-rubric even on dimensions it isn't scoring
   - `{scoring_scale}` — the integer range for each dimension (e.g., 0-5 or 0-1, from the spec's `output_schema`)

2. **Return JSON matching the spec's `output_schema`**:
   - `scores` — `{<dimension>: int}` within the declared range
   - `diagnostics` — `{<dimension>: "<one-line feedback for the student>"}`
   - The wrapper does strict JSON-schema validation; a malformed response triggers the spec's fallback, not a retry.

3. **Include few-shot examples** (at least one response at high/mid/low per dimension), either inline or in a paired `.examples.md` file.

4. **Declare the model and token budget** in a frontmatter block so a generator can fail early on mismatch with the spec's `model` / `max_tokens`.

## Writing a new template

- Copy an existing template, bump the version suffix, edit the prompt body.
- Add corresponding examples in `<name>.examples.md`.
- Calibrate against at least 10 real student responses before any spec pins to the new template; document the calibration in the PR that introduces it.
- Never edit a published template in place — always version. Specs must be able to pin to an immutable artifact.

## Status

**PLACEHOLDER — no templates authored yet.**

`text-rubric-v1.md` is the first template to write. It's blocked on the first content file being populated (likely `c1A-rewrite-this-chart-note.yaml`) so that calibration has real student-response examples to work against. Writing the template before the content is counterproductive — you end up tuning to imagined student behavior.

### Specs currently pointing at templates that don't yet exist

All six AI-tagged specs pin to `text-rubric-v1`:

- `127.403-c1A.md` — Rewrite This Chart Note, Active-vs-Passive Spotter
- `127.403-c2C.md` — Jargon Decoder
- `127.403-c2D.md` — Incident-Report Generator, Shift-Summary Card
- `127.403-c2F.md` — Precision Rewriter

Until `text-rubric-v1.md` exists, these specs' AI paths fall back to the deterministic partial scoring declared in each `ai_required.fallback`.
