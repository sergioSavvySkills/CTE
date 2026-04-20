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
atom_serial: string        # CCC-SSS-NNNN hierarchy-encoded serial; assigned by scripts/assign_atom_serials.py
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

## Sidecar artifacts

An atom may have a **sidecar folder** next to its `.md` file containing
expanded source material that generators (lesson, quiz, flashcard,
textbook) consume at authoring time. Sidecars are optional and additive —
the stub remains the canonical entry point, and every generator degrades
gracefully when a sidecar is absent.

```
library/<cluster>/<subcluster>/atoms/
├── <atom-id>.md        # the stub (unchanged)
└── <atom-id>/          # sidecar folder (same slug, no .md)
    ├── book.md
    ├── vocabulary.csv
    ├── examples.md
    ├── misconceptions.md
    ├── question-bank.yaml
    ├── media-brief.md
    └── sources.md
```

Supported sidecar types and their schemas live at
[`_schemas/atom-sidecars/`](atom-sidecars/README.md). Each sidecar type has
its own conventions doc (length targets, section structure, front-matter).

## Atom serials

`atom_serial` is a hierarchy-encoded identifier in the format
`<CLUSTER>-<SUBCLUSTER>-<NNNN>` (e.g., `HHS-PH-0042`). It sits alongside the
kebab-case `atom_id`, which remains the primary reference used by templates,
crosswalks, scripts, and data files.

- **Cluster and sub-cluster codes** come from `library/_schemas/atom-serial-codes.csv` (2-3 letter mnemonics)
- **NNNN** is a zero-padded 4-digit integer assigned sequentially within the sub-cluster; gaps are allowed (retired atoms keep their serial)
- **Immutability:** serials are permanent once assigned. Renaming an atom does not change its serial. Moving an atom between sub-clusters retires the old serial and assigns a new one in the destination
- **Assignment:** run `scripts/assign_atom_serials.py --assign --subcluster <slug>` to populate serials; run `--next <slug>` to get the next available serial for a new atom; run `--verify` to confirm uniqueness and format
- Per-sub-cluster manifests at `library/<cluster>/<subcluster>/atoms/_serials.csv` record all assigned serials and their status (active / retired)
