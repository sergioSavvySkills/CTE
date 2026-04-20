# Atom sidecars — schemas

Atoms (Layer 1) are 30-line stubs. Sidecar artifacts expand a single atom into
richer source material that generators (lesson, quiz, flashcard, textbook,
simulation) consume at authoring time.

## Folder convention

```
library/<cluster>/<subcluster>/atoms/
├── <atom-id>.md              # the canonical stub (unchanged)
└── <atom-id>/                # sidecar folder (same slug, no .md)
    ├── book.md               # long-form prose
    ├── vocabulary.csv        # structured glossary
    ├── examples.md           # worked examples / cases
    ├── misconceptions.md     # common student errors + corrections
    ├── question-bank.yaml    # item bank
    ├── media-brief.md        # image/video/diagram specs
    └── sources.md            # citations / primary sources
```

Any subset of sidecars may be present; generators degrade gracefully when a
sidecar is missing. Extra sidecar types beyond the seven above (e.g.,
`rubric.md` for skill-type atoms, `scenarios.md`, `pronunciation.csv`) are
permitted when the atom calls for them.

## Schema files

One schema doc per sidecar type:

| sidecar | schema file | format |
|---|---|---|
| book.md | [book.md](book.md) | markdown prose |
| vocabulary.csv | [vocabulary.csv](vocabulary.csv) | CSV with header row |
| examples.md | [examples.md](examples.md) | markdown, numbered |
| misconceptions.md | [misconceptions.md](misconceptions.md) | markdown, pair format |
| question-bank.yaml | [question-bank.yaml](question-bank.yaml) | YAML list of items |
| media-brief.md | [media-brief.md](media-brief.md) | markdown table + notes |
| sources.md | [sources.md](sources.md) | markdown with citation list |

## Status field convention

Every prose sidecar (`book.md`, `examples.md`, `misconceptions.md`,
`media-brief.md`, `sources.md`) opens with a YAML front-matter block:

```yaml
---
atom_id: body-systems-overview
atom_serial: HHS-PH-0004
sidecar: book            # one of: book, examples, misconceptions, media-brief, sources
status: ai-draft         # ai-draft | reviewed | published
author: claude
reviewer:
review_date:
---
```

CSV and YAML sidecars carry the same fields in a comment header or top-level
key, as noted in their individual schema docs.
