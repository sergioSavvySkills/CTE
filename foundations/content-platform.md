# Content Platform Architecture (Strategic Shape)

## Purpose of This Document

This is the strategic shape of our content platform — the layers, their
responsibilities, and the rules that must not be broken. It is the
source of truth a future Founding Engineer builds against and the
reference Sergio and Maya use when deciding whether a proposed feature
respects the architecture.

No technology choices are made here. What is locked in is the *shape*
of the system.

## Core Principles

1. **Content is data, not documents.** A lesson is a structured object,
   not a PDF. Everything else follows from this.
2. **Standards are the spine.** Texas TEKS standards are the primary
   organizing principle. Every piece of content is keyed to one or more
   TEKS expectations.
3. **Course-first organization.** Content is organized by course code
   (e.g. 127.403 Principles of Health Science), not by national taxonomy.
4. **Separation of content from delivery.** What is taught (a lesson)
   is separate from how it is sequenced in a course (a template) and
   how a teacher runs it (customization overlay).
5. **Crosswalks are generated, not authored.** The mapping from lessons
   to TEKS standards is AI-produced with human review. It is never
   hand-maintained as a primary artifact.

## Architecture Layers

### Layer 1 — Course Content

**Responsibility:** hold every piece of instructional content, organized
by course and TEKS standard.

**A lesson is:**

- Keyed to one TEKS expectation (e.g. §127.403-c1A).
- A textbook chapter providing the instructional content.
- A workbook page providing student practice and assessment.
- Activities (AI prompts, simulations, projects) tied to that standard.

**What lessons do NOT contain:**

- Course sequencing information. (That lives in Layer 2.)
- Teacher-specific customizations. (Those live in the overlay.)

**Structure:**
```
courses/
  <course-slug>/
    _about.md              # course overview, TEKS code, credit hours
    teks-<code>.md         # verbatim TEKS text
    course-skeleton.md     # module/lesson sequencing map
    standards/             # one .md per TEKS expectation
    textbook/              # one chapter per standard
    workbook/              # one student page per standard
    activities/            # prompts, simulations, projects
```

### Layer 2 — State Standards Crosswalk

**Responsibility:** map each lesson to Texas TEKS standards.

**Shape:** a relation:
`(lesson_id, state, standard_code) → alignment_strength + rationale`.

**Key properties:**

- One lesson can align to multiple standards.
- One standard can be covered by multiple lessons.
- Alignment has strength (primary / supporting / tangential) and a
  human-readable rationale.
- Each entry has provenance: AI-generated draft + human reviewer +
  date + framework version.

**How it gets built:** an AI pipeline ingests the state's published
framework, produces a draft crosswalk, Maya (or a curriculum designer)
reviews and approves.

### Layer 3 — Course Templates

**Responsibility:** define the ordered sequence of lessons in a course,
with pacing and generation directives.

**A course template is:**

- A state + course name (e.g., "Texas — Principles of Health Science").
- The official course code and metadata (credit hours, prerequisites, grade band).
- An ordered list of units and lessons.
- The credentials this course prepares students for.
- Standards coverage derived from the lesson → crosswalk chain.

### Teacher Customization Layer (the overlay)

**Responsibility:** let a teacher adapt a course for her class without
mutating shared content or breaking alignment reporting.

**Supported operations:**

- Reorder lessons.
- Skip a lesson (with an optional reason for reporting).
- Add supplementary activities.
- Add teacher-authored notes pinned to a lesson.

**Invariant:** customization can never edit shared lesson content.

## Content Discovery — How We Know What to Build

Content creation is driven by TEKS standards gap detection:

1. Ingest the Texas TEKS for a course code.
2. The AI crosswalk pipeline produces a coverage report: every standard
   that has no lesson covering it becomes a content request.
3. The curriculum designer authors a textbook chapter + workbook page
   for each uncovered standard.

## Key Invariants

1. **Standards are the spine.** Every lesson is keyed to a TEKS expectation.
2. **Alignment is derived.** A course's state alignment report is computed
   from its lessons + the crosswalk. Never a standalone document.
3. **Crosswalks are reviewable.** Every AI-generated alignment has
   provenance and a human reviewer.

## Decisions (Locked)

1. **Pathway: Texas Health Science.** First pathway is Texas Health
   Science Technology (Chapter 127). Entry course: Principles of Health
   Science (§127.403).
2. **First state: Texas.** Texas has the largest CTE footprint and the
   clearest TEKS to build against.
3. **Standards-first authoring.** Each textbook chapter and workbook
   page is authored to cover a specific TEKS expectation.

## Out of Scope for This Document

- Technology choices (database, language, service architecture).
- Authoring UI for curriculum designers.
- Teacher and learner product surfaces (classroom UI, gradebook, analytics).
- Platform concerns (auth, SSO, rostering, FERPA, multi-tenancy).
