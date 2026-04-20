# Schema — `misconceptions.md`

Common student errors or intuitive-but-wrong beliefs about the atom's content,
paired with corrections. Feeds check-for-understanding slides and remediation
prompts. The foldable "gotcha" knowledge that separates a lesson from a
textbook chapter.

## Front-matter

```yaml
---
atom_id: <matches parent atom>
atom_serial: <matches parent atom>
sidecar: misconceptions
status: ai-draft | reviewed | published
misconception_count: <integer>
---
```

## Count

**3-5 misconceptions per atom.** Fewer than 3 means you probably haven't
thought hard enough; more than 5 means you're mixing in minor quibbles.

## Per-misconception structure

Each misconception is an H2 section:

```markdown
## Misconception N — <one-line summary>

**What students often think:**
A 1-2 sentence statement of the mistaken belief, in plausible student voice.

**What's actually true:**
The correct understanding, 2-4 sentences. Cite `book.md` section or
`sources.md` key where appropriate.

**Why the confusion is natural:**
1-2 sentences acknowledging what makes the wrong answer feel right. This is
what makes misconceptions.md more than a list of errors.

**How to check whether a student has the correct model:**
One diagnostic question or behavioral indicator. This is what the CFU slide
will probe.
```

## What counts as a misconception (vs. just "a mistake")

A misconception is a **stable, structured, intuitive** wrong model — one that
a student keeps returning to even after being corrected, because it fits their
prior experience or common-sense intuition. It's not a slip-up, a factual gap,
or a vocabulary confusion.

Good examples:
- "The heart beats faster to push blood; it doesn't have anything to do with
  the lungs" (ignores cardiorespiratory coupling)
- "Bones are dead because they don't move on their own" (ignores bone as
  living tissue with metabolism)

Weaker examples to avoid:
- "Students forget the name of the pancreas" (vocabulary gap, not a model)
- "Students don't know the normal respiratory rate" (factual gap)
