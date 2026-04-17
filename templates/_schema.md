# Templates — Layer 3 Schema

Course templates define a specific course in a specific state as an
ordered sequence of atoms. Templates are configuration — they contain
no instructional content.

## Folder convention

```
templates/
  <state>/
    <subcluster>/
      <course-code>-<course-slug>.md    # one file per course template
```

## Course template file format

```yaml
# YAML front-matter
template_id: string          # e.g. tx-it-principles-2025
state: TX
course_name: string          # official state course name
course_code: string          # state-assigned code
subcluster: string
grade_band: HS | PS | Both
credit_hours: number
credential_targets:          # credentials this course prepares for
  - comptia-itf-plus
  - comptia-a-plus
framework_version: string    # state TEKS version
status: draft | reviewed | active
reviewer: string
review_date: ISO date
```

### Slots section (markdown table)

| slot | atom_id | notes |
|---|---|---|
| 01 | atom-id-here | optional pacing/transition note |

## Rules (from content-platform.md)

- Templates reference atoms — never copy atom content inline.
- State standards coverage is derived (atom → crosswalk), never
  hand-authored in the template.
- A new state is primarily a new set of templates reusing existing atoms.
- Credential targets drive which atoms are slotted, not the reverse.
