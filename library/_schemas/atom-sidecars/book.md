# Schema — `book.md`

Long-form prose treatment of an atom. The "instructor's knowledge base" that a
lesson generator condenses into slides and a textbook generator stitches
into chapters.

## Front-matter

```yaml
---
atom_id: <matches parent atom>
atom_serial: <matches parent atom>
sidecar: book
status: ai-draft | reviewed | published
word_count: <integer, approximate>
author: <name or claude>
reviewer: <name or blank>
review_date: <ISO date or blank>
---
```

## Length targets

| atom difficulty | word-count target |
|---|---|
| 1 (foundational) | 1500-2500 |
| 2 (intermediate) | 2000-3000 |
| 3 (advanced) | 2500-3500 |
| survey / cross-system | up to 3500 |

Aim for the lower bound; write more only when the content demands it.

## Section structure

Use H2 headings (`##`). Recommended backbone:

1. `## Why this matters` — 1 paragraph hook, real-world relevance
2. `## What you should already know` — 1 short paragraph naming prerequisites
3. `## Core concept` — the main explanatory body; break into H3 subsections
4. `## Worked through an example` — 1 narrative example (details live in
   `examples.md`; here we foreshadow)
5. `## Common confusions` — 1 paragraph pointing at `misconceptions.md`
6. `## How this connects to other topics` — 2-4 sentences linking forward
   and sideways in the curriculum
7. `## Key terms to remember` — 1 short paragraph pointing at
   `vocabulary.csv`, plus 4-8 headline terms inline (bolded)
8. `## Further reading` — pointer to `sources.md`

## Voice

- Second person ("you can see") or third person neutral. Avoid "we" — the
  student is the reader, not a collaborator
- Active voice over passive
- Short paragraphs (3-5 sentences). No wall-of-text
- Concrete before abstract. Lead with an example, then name the principle

## Citation style

Inline citations in square brackets with a short key:

> The kidneys filter roughly 180 liters of plasma each day [OpenStax §25.1].

Every bracketed citation must resolve to an entry in `sources.md`. Don't use
footnote numbers — the key is human-readable and survives reordering.

## What NOT to include

- State standard codes (atoms and their sidecars are state-neutral)
- TEKS / credential objective references (those live in crosswalks)
- Slide-deck structure (that's the lesson generator's job)
- Assessment items (those live in `question-bank.yaml`)
