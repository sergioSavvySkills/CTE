# Templates — Layer 3 Schema

Course templates are **generation recipes**, not content. A template
tells the system which atoms to sequence and which generators to invoke
for each atom and each unit. All instructional content comes from the
shared atom library and the generator suite — the template itself
contains zero lesson text.

## Folder convention

```
templates/
  <state>/
    <subcluster>/
      <template-id>.md    # one file per course
```

## Course template file format

A course template is a markdown file with a YAML front-matter block
(course metadata) and a body that declares units and slots as a YAML
code block.

---

### Front-matter fields

```yaml
template_id: string          # e.g. tx-principles-of-it-2025
state: TX                    # two-letter state code
course_name: string          # official state course name
course_code: string          # state-assigned code (e.g. 130.272)
subcluster: string           # e.g. it-support-services
grade_band: HS | PS | Both
credit_hours: number         # 0.5 | 1 | 2
credential_targets:          # IBC credentials this course prepares for
  - comptia-itf-plus
  - google-it-support
framework_version: string    # state TEKS/standards version
status: draft | reviewed | active
reviewer: string
review_date: ISO date
```

---

### Units and slots (body YAML block)

The body contains a single `units` YAML block. Units are ordered.
Slots within each unit are ordered.

```yaml
units:
  - unit_id: u01
    title: "Unit title"
    weeks: 2                  # suggested pacing in weeks

    slots:
      - slot: 1
        atom_id: atom-id-here
        generate:             # omit a key to use the default for that atom's skill_type
          lesson: true        # slide-deck instructional artifact — always true
          classwork: guided_practice   # see classwork types below
          quiz: exit_ticket   # see quiz types below
          simulation: false   # virtual lab (self-contained HTML)
          video: false        # AI explainer video

    unit_generate:
      game: true              # review game (Jeopardy/Bingo) covering all unit atoms
      summative_quiz: true    # end-of-unit assessment
      performance_task: false # project-based assessment — ⚠ generator not yet built
```

---

### Generator reference

#### Slot-level generators

| Key | Values | Notes |
|---|---|---|
| `lesson` | `true` | Always true. Slide-deck artifact covering the full instructional arc. |
| `classwork` | `warm_up` `guided_practice` `independent_practice` `discussion` `applied_task` `none` | In-class activity. Default varies by `skill_type` (see below). |
| `quiz` | `exit_ticket` `formative_check` `none` | Low-stakes slot-level quiz. |
| `simulation` | `true` `false` | Virtual lab — self-contained HTML, runs in browser. No physical equipment. Appropriate for `skill` and `both` atoms. |
| `video` | `true` `false` | AI explainer video. Good for abstract concepts or dense knowledge atoms. |

#### Unit-level generators

| Key | Values | Notes |
|---|---|---|
| `game` | `true` `false` | Review game (Jeopardy, Bingo) covering all atoms in the unit. Occasional use — not every unit. |
| `summative_quiz` | `true` `false` | End-of-unit assessment. Almost always true. |
| `performance_task` | `true` `false` | Project brief + deliverables + rubric + milestones. ⚠ Generator not yet built. Include in template so the recipe is complete. |

#### Generation defaults by `skill_type`

When a slot's `generate` block is omitted or a key is missing, these
defaults apply based on the atom's `skill_type`:

| `skill_type` | `classwork` default | `simulation` default | `video` default |
|---|---|---|---|
| `knowledge` | `guided_practice` | `false` | `false` |
| `skill` | `applied_task` | `true` | `false` |
| `both` | `applied_task` | `true` | `false` |

`lesson: true` and `quiz: exit_ticket` are always the default regardless
of skill_type. Override by setting explicitly in the slot.

---

### Complete annotated example

```yaml
units:
  - unit_id: u01
    title: "IT Foundations"
    weeks: 2

    slots:
      - slot: 1
        atom_id: binary-number-systems
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: true           # override: concept benefits from visual explainer

      - slot: 2
        atom_id: fundamental-data-types
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: false

      - slot: 3
        atom_id: input-processing-output-storage
        # generate omitted — defaults apply (skill_type: knowledge)

    unit_generate:
      game: true
      summative_quiz: true
      performance_task: false

  - unit_id: u02
    title: "Hardware"
    weeks: 3

    slots:
      - slot: 1
        atom_id: hardware-components-overview
        generate:
          lesson: true
          classwork: guided_practice
          quiz: exit_ticket
          simulation: false
          video: false

      - slot: 2
        atom_id: internal-components
        generate:
          lesson: true
          classwork: applied_task
          quiz: exit_ticket
          simulation: true      # virtual PC assembly / component identification sim
          video: false

    unit_generate:
      game: true
      summative_quiz: true
      performance_task: true    # ⚠ not yet built — e.g. "build a PC spec sheet for a given budget"
```

---

## Rules (from content-platform.md)

- Templates reference atoms — never copy atom content inline.
- State standards coverage is derived (slot → atom → crosswalk chain), never hand-authored here.
- A new state is a new set of templates reusing the same shared atoms.
- `performance_task: true` is the signal for the Performance Task Generator when it ships.
- `simulation: true` means a virtual/browser-based lab — there are no physical lab requirements.
- Textbook chapters are not a slot-level default; generate on-demand outside the template if needed.
