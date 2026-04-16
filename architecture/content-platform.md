# Content Platform Architecture (Strategic Shape)

## Purpose of This Document

This is the strategic shape of our content platform — the layers, their
responsibilities, and the rules that must not be broken. It is the
source of truth a future Founding Engineer builds against and the
reference Sergio and Maya use when deciding whether a proposed feature
respects the architecture.

No technology choices are made here; those belong to the eventual
engineer. What is locked in is the *shape* of the system.

The architecture must hold up against four scenarios (these are the
design tests, and they reappear as the verification section):

1. Add a new state in weeks, not years.
2. Update one industry credential (e.g., CompTIA A+ revision) once and
   have it propagate to every course that uses it.
3. A teacher customizes a course for her class without breaking her
   district's state alignment report.
4. Generate a Perkins V accountability report on demand, with no
   hand-maintained alignment document anywhere in the chain.

## Core Principles

1. **Content is data, not documents.** A lesson is a structured object,
   not a PDF. Everything else follows from this.
2. **Authoring is industry-driven, alignment is state-driven.** The
   authoring surface speaks industry credentials and competencies.
   State standards are *projections* over that content, not the source
   of truth.
3. **Composition over duplication.** Courses are composed from shared
   atoms. We never fork content into a `states/texas/` folder. When a
   state needs something new, we add an atom to the shared library.
4. **Separation of content from curriculum.** "What is taught" (an
   atom) is separate from "how it's sequenced in a specific state
   course" (a template) is separate from "how this teacher ran it this
   semester" (a customization overlay).
5. **Crosswalks are generated, not authored.** The mapping from atoms
   to state standards is AI-produced with human review. It is never
   hand-maintained as a primary artifact.

## Architecture Layers

### Layer 1 — Content Atoms (the shared library)

**Responsibility:** hold every piece of instructional content, exactly
once, in an industry-neutral vocabulary.

**An atom is:**

- One competency (a single thing a student should be able to do/know).
- The instructional content that teaches it (text, media, interactive
  elements, scaffolding).
- One or more assessments that verify mastery.
- Metadata: career cluster & pathway, industry credential objectives
  it maps to, skill/knowledge statements, prerequisite atoms,
  difficulty, estimated student time.

**What atoms do NOT contain:**

- State standard codes. (Those live in Layer 2.)
- Course sequencing information. (That lives in Layer 3.)
- Teacher-specific customizations. (Those live in the overlay.)

**Granularity rule:** an atom is the smallest unit that can stand
alone pedagogically. Roughly 15–60 minutes of student time. Small
enough to recompose; large enough that the assessment means something.

### Layer 2 — State Standards Crosswalk

**Responsibility:** map each atom to each state's published standards.

**Shape:** a many-to-many relation:
`(atom_id, state, standard_code) → alignment_strength + rationale`.

**Key properties:**

- One atom can align to multiple standards in the same state.
- One standard can be satisfied by multiple atoms (some standards
  require a sequence of atoms).
- Alignment has strength (primary / supporting / tangential) and a
  human-readable rationale.
- Each entry has provenance: AI-generated draft + human reviewer +
  date + state framework version.

**How it gets built:** an AI pipeline ingests the state's published
framework, produces a draft crosswalk, Maya (or a curriculum designer)
reviews and approves. Versioned per state, because states revise
frameworks.

**What the crosswalk does NOT do:**

- It never changes atom content. If an alignment requires atom
  changes, that's a library change that benefits every state.
- It does not dictate course ordering. (That is Layer 3.)

### Layer 3 — Course Templates

**Responsibility:** define a specific course in a specific state as an
ordered sequence of atoms wrapped in that state's required course
shell.

**A course template is:**

- A state + course name (e.g., "Texas — Principles of Information
  Technology").
- The state's official course code and required course metadata
  (hours, prerequisite courses, grade band).
- An ordered list of "slots." Each slot references an atom — or a
  small set of interchangeable atoms — plus optional slot-level notes
  (pacing, transitions).
- The set of credentials this course is designed to prepare students
  for.
- The state standards this course is designed to cover — **derived**
  from the slot → atom → crosswalk chain, not hand-authored.

**Key property:** a course template is a *configuration*, not content.
A new state is primarily a new set of templates reusing the same
atoms.

### Teacher Customization Layer (the overlay)

**Responsibility:** let a teacher adapt a course for her class without
mutating shared content or breaking alignment reporting.

**Shape:** a per-class overlay on a course template. Supported
operations:

- Reorder slots.
- Skip a slot (with an optional reason, used for admin reporting).
- Swap an atom for another from the shared library, subject to a
  competency-compatibility check.
- Add an atom from the library (enrichment, remediation).
- Add teacher-authored supplementary notes pinned to a slot.

**Invariant:** customization can never edit a shared atom. A typo fix
is a pull request against the shared library, not a per-class edit.
This is how we stay a single-content-source company.

**Alignment impact:** the class-level state alignment report is
recomputed live. If the teacher skips an atom that was the primary
carrier for a state standard, the report flags that standard as
at-risk and surfaces alternative atoms that could cover it.

## What Crosses Layer Boundaries (and What Doesn't)

- A course template **references** atoms — never copies them.
- A crosswalk entry **references** atoms — never embeds them.
- A customization **references** a template and atoms — never forks
  them.
- No atom ever contains a state standard code.
- No course template ever contains inline instructional content.
- No state-specific folder inside the atom library.
- No teacher-specific copy of a shared atom.

If a proposed feature requires violating one of these rules, that's a
signal the feature is wrong or the architecture needs a deliberate
amendment — not a quiet workaround.

## Key Invariants (Must Always Be True)

1. **Single source of truth per atom.** One atom, one canonical
   version, referenced everywhere.
2. **Alignment is derived, not authored.** A course's state alignment
   report is computed from its atoms + the crosswalk. It is never a
   standalone document.
3. **Updates propagate.** Change an atom → every course using it
   reflects the change on next load. Revise an industry credential →
   every atom tagged to that credential is flagged for review.
4. **Customization is additive.** Teacher customization never mutates
   shared content.
5. **Crosswalks are reviewable.** Every AI-generated alignment has
   provenance and a human reviewer.

## Out of Scope for This Document

- **Technology choices.** Database, language, service architecture —
  belong to the future engineer.
- **Authoring UI.** How a curriculum designer sits down and creates an
  atom is a product-design problem downstream of this.
- **Teacher / learner product surfaces.** Classroom UI, gradebook,
  analytics — live above this architecture.
- **Platform concerns.** Auth, SSO, rostering (Clever / ClassLink /
  OneRoster), FERPA, multi-tenancy.
- **Content governance.** Review workflow, versioning policy,
  deprecation — important but downstream of having atoms at all.

## Verification — How We Know the Architecture Is Right

These are the four scenarios any implementation must satisfy. They are
the acceptance tests for the architecture itself, independent of
technology.

1. **Add a new state in under one month.** Ingest the state's
   framework, run the AI crosswalk, Maya reviews, spin up one course
   template. Zero atom changes required.
2. **Propagate a credential update.** When CompTIA revises A+, every
   atom tagged to affected objectives is flagged, revised once, and
   every state's affected course templates reflect the change
   automatically.
3. **Customize mid-semester without breaking reporting.** A teacher
   skips an atom and adds an enrichment atom. The class-level state
   alignment report updates live and flags any at-risk standards.
4. **Generate a Perkins V report on demand** from a district's courses
   + students + atom completion data, with no hand-maintained
   alignment document anywhere in the chain.

## Open Questions (for Sergio + Maya)

1. **Wedge pathway.** The architecture is pathway-neutral, but the
   first atom library must be built for exactly one pathway (IT vs.
   Business vs. Health Science). Decision needed before atoms start
   being authored.
2. **First state.** Texas has the largest CTE footprint and the
   clearest IBC list, which argues for TX first. Maya's call.
3. **Credential-first vs. standard-first authoring UX.** Industry
   credentials are the atom-tagging spine in this document, so the
   recommended authoring UX presents credentials first and lets state
   alignment fall out. Maya to confirm this matches how curriculum
   designers actually think.
