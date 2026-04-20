# Schema — `examples.md`

Worked examples or integrative cases. Students follow the reasoning
step-by-step; the lesson generator turns each example into a guided-practice
slide sequence.

## Front-matter

```yaml
---
atom_id: <matches parent atom>
atom_serial: <matches parent atom>
sidecar: examples
status: ai-draft | reviewed | published
example_count: <integer>
---
```

## Count

Aim for **3-5 examples per atom.** Enough variety that guided practice has
options; not so many that maintenance becomes a burden. Keep each example
at the level the atom's LO targets — a survey atom's examples name systems,
not the internal mechanisms of any one system.

## Per-example structure

Each example is an H2 section:

```markdown
## Example N — <short descriptive title>

**Scenario:** 1-2 sentences framing the situation. Concrete, named, specific.

**What to work out:** The question or decision the student should resolve.

**Step-by-step:**

1. First reasoning step. Each step is 1-2 sentences.
2. Second step.
3. ...

**Answer:** The conclusion in one sentence.

**Why it matters:** 1-2 sentences connecting back to the atom's learning
objective or to a clinical / workplace consequence.
```

## Example types by atom skill_type

| atom skill_type | example style |
|---|---|
| knowledge | Reasoning walk-throughs (symptoms → system → likely cause) |
| skill | Procedural demos (each step = one student action, with "why") |
| both | Mix — 2 reasoning + 2 procedural |

## Voice

Same rules as `book.md`. Second person. Active. Short.

Examples should stand alone — a student who skipped the book should still
learn something from reading them.
