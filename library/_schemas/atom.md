# Atoms — Layer 1 Schema

The shared content library. Every instructional unit lives here exactly
once. No state-specific content. No course sequencing.

## Folder convention

```
library/
  <cluster>/
    <subcluster>/
      atoms/
        <atom-id>.md    # one file per atom
```

## Atom file format

Each atom is a markdown file with a YAML front-matter block followed
by the instructional content stub.

### Front-matter fields

```yaml
atom_id: string            # kebab-case, globally unique
title: string              # one clear competency statement
subcluster: string         # e.g. it-support-services
credential_objectives:     # list of objective_codes from objectives CSVs
  - comptia-a-plus::core1::1.1
  - comptia-itf-plus::FC0-U61::1.1
skill_type: knowledge | skill | both
grade_band: HS | PS | Both
estimated_minutes: integer  # 15–60
difficulty: 1 | 2 | 3       # 1=foundational, 2=intermediate, 3=advanced
prerequisites:              # list of atom_ids
  - atom-id-here
status: draft | reviewed | published
reviewer: string
review_date: ISO date
```

### Body sections

- **Learning objective** — one sentence: "Students will be able to…"
- **Content stub** — key concepts, terminology, examples (populated by
  curriculum designer; kept industry-neutral)
- **Assessment stub** — question types and sample items

## Rules (from content-platform.md)

- Atoms never contain state standard codes.
- One atom per competency — smallest unit that stands alone pedagogically.
- 15–60 minutes of estimated student time.
- Authored in industry-neutral vocabulary, never from state standard phrasing.
- Every anchor credential objective must have at least one covering atom.
