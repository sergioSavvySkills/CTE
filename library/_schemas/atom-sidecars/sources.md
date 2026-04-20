# Schema — `sources.md`

Citations and primary sources that ground the atom's content. Every
bracketed citation in `book.md`, `examples.md`, or `misconceptions.md` must
resolve to a key in this file. Provides an accuracy audit trail for
regulated content (healthcare, law, finance).

## Front-matter

```yaml
---
atom_id: <matches parent atom>
atom_serial: <matches parent atom>
sidecar: sources
status: ai-draft | reviewed | published
source_count: <integer>
---
```

## Structure

One H2 section per source-type, then an H3 entry per source.

### Source types (H2)

- `## Textbooks`
- `## Standards and guidelines` — CDC, WHO, OSHA, professional bodies
- `## Peer-reviewed articles`
- `## Government / regulatory pages` — HHS.gov, NIH, FDA, state agencies
- `## Open educational resources` — OpenStax, Khan Academy, CK-12
- `## Other authoritative pages` — professional associations, hospital systems

### Per-source entry (H3)

```markdown
### OpenStax §25.1

- **Citation:** OpenStax, *Anatomy and Physiology 2e*, Chapter 25
  "The Urinary System", §25.1 "Internal and External Anatomy of the Kidney"
  (2023, CC BY 4.0).
- **URL:** https://openstax.org/books/anatomy-and-physiology-2e/pages/25-1
- **Used for:** kidney anatomy, filtration rate figures, nephron structure
- **Confidence:** high — tier-1 open text, peer-reviewed
- **Access date:** 2026-04-20
```

Keys should be compact and meaningful — `OpenStax §25.1` over
`source-12`. Inline citations in book.md write `[OpenStax §25.1]`.

## Confidence levels

- **high** — peer-reviewed, government regulator, authoritative professional body
- **medium** — reputable textbook, mainstream educational resource
- **low** — secondary explainer (e.g., Wikipedia) used for framing only;
  should not be the sole source for a factual claim

Citations at `low` confidence must be corroborated by at least one `medium`
or `high` source in the same claim.

## Not in scope

- Instructor materials or lesson-plan repositories (those are Layer 3, not
  Layer 1)
- State standards or credential objectives (those live in the state-framework
  and credentials files, not here)
- Trademarked clinical pathways unless cited as a reference, not a source
  of copied content
