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
6. `## References`

Preserve this order when editing.

## Transversal standards

`127.403-c1B`, `127.403-c1C`, and `127.403-c4C` are transversal — behavior standards reinforced across every lesson, not taught in a dedicated session. Their front-matter carries a `reinforced_by:` list of host standards where the behavior gets surfaced.
