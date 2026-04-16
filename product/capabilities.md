# Product Capabilities — Current State

## Purpose

Snapshot of what exists in the product today. This file is the
answer to "what have we actually built?" — useful for onboarding new
hires, briefing advisors, pitching design partners, and sanity-checking
scope decisions. It is a *current-state inventory*, not a roadmap and
not a spec for future work.

Keep this file updated as capabilities ship, mature, or get cut.

## Architecture at a Glance

The product is three stages a teacher moves through: **generate →
edit → deliver**.

1. **Generator Suite** — AI-powered tools that produce digital
   classroom artifacts from teacher inputs. Includes a **Course
   Builder** that produces a full course scope-and-sequence and
   per-artifact generators for lessons, quizzes, classwork, videos,
   simulations, games, textbook chapters, and printable material.
2. **Editor Surface** — in-house editors tailored to each artifact
   type (slide editor for slide decks, etc.) where teachers edit
   generated output before delivery — both section-level
   regeneration and manual editing.
3. **LMS Layer** — the class-execution environment where students
   consume generated content, submit work, and get graded. The LMS
   Layer is interoperable with the teacher's existing LMS (Canvas,
   Schoology today) through Edlink; students launch into our content
   via LTI 1.1.

Generators produce first drafts. The Editor Surface turns those
drafts into teacher-owned content. The LMS Layer delivers the
finished content to students and captures the resulting work. All
three stages are digital-first; nothing ships as a static PDF by
default.

## Generator Suite

Most of the generators below are operational today and produce
shippable output; one is surfaced as "coming soon" (noted in-place).
Each generator takes teacher-provided inputs and returns a digital
artifact consumable in the LMS Layer.

### Generation Flow

Every generator follows the same front-end flow:

1. Teacher enters a free-form prompt and picks a state.
2. The system surfaces relevant state / national standards for the
   prompt (e.g., for a Maryland Health Science prompt about medical
   terminology, NCHSE Standard 2.2.1 *"Use common roots, prefixes,
   and suffixes"* appears).
3. Each standard item is pre-unpacked into 3–5 concrete learning
   objectives the teacher can opt into or out of individually.
4. Teacher selects the standards + LOs to target.
5. The generator produces the artifact against that selection.
6. If the generator is invoked with a lesson as context (e.g., the
   quiz is being generated for a specific lesson), the LOs already
   attached to the lesson carry through without re-selection —
   coherence-by-reference across generators.

This is the shared front-end the Course Builder and per-artifact
generators below all use.

### Course Builder

Produces a full course scope-and-sequence from a high-level input —
the course topic and the state / pathway context. The Course Builder
emits a unit-structured course: units, lessons within each unit, and
the general semester arc. Per-artifact generators (below) then
produce the actual content inside each slot.

This is the planner tier — it gives a teacher a ready-to-teach
semester outline rather than a single artifact. *(Exact scope — eager
vs. lazy generation, editability of unit structure and sequencing,
whether assessments are built per unit — to confirm.)*

### Lesson / Slide Deck Generator
Produces a lesson as a slide deck rendered in the Presentator. Covers
the instructional arc (intro, content, checks for understanding,
close) rather than a bare set of bullet slides.

### Classwork Generator
Produces in-class activities — **assessment FOR learning** (practice,
not measurement). Output spans structured exercises, worksheets,
discussion prompts, and applied tasks tied to a lesson's objectives.

Supported sub-types (specified via prompt today, eventually surfaced
as presets in *More settings...*):

- **Warm-up / bell-ringer** — 5-minute opening activity.
- **Guided practice** — worksheet-style, teacher-supported.
- **Independent practice** — student-alone work.
- **Discussion prompt** — teacher-facilitated conversation.
- **Applied task** — short real-world-shaped exercise.
- **Homework** *(open: placement)* — classwork-shaped but done
  outside class; often becomes gradable. May warrant its own
  "gradable" flag here or a distinct generator — flagged but not
  yet decided.

### Quiz Generator
Produces quizzes — **assessment OF learning**. Output is delivered
as an auto-gradable assignment inside the LMS Layer.

Supported sub-types (specified via prompt today, eventually surfaced
as presets in *More settings...*):

- **Formative quick-check** — short, in-lesson, immediate feedback,
  low stakes.
- **Summative unit assessment** — longer, end of unit, gradebook-
  bound.
- **Credential-prep practice set** — mirrors the psychometric shape
  of the target credential exam (meaningful once credential-objective
  targeting lands — see gaps below).
- **Exit ticket** — 3-item micro-quiz at end of class.

Assessment type is a prompt parameter today. Surfacing the sub-types
as presets is the discoverability fix for teachers who don't already
use formative/summative vocabulary; validating that prompted types
produce meaningfully different item shapes is the output-consistency
check.

### Design note: Quiz vs. Classwork kept separate

The two generators map to a real pedagogical distinction —
**assessment OF learning** (Quiz) vs. **assessment FOR learning**
(Classwork). Keeping them separate preserves conceptual clarity for
teachers and keeps LMS-sync behavior clean (Quiz flows to the
gradebook; Classwork does not by default). Merging them into a
single "question generator" would optimize UI simplicity at the cost
of a distinction teachers actively use.

### Video Explainer Generator
Produces explainer videos tied to a lesson topic or learning
objective. Pipeline: AI-generated images + AI-generated voice-over
bundled together into a video artifact.

### Simulation Generator
Produces CTE-domain-specific virtual labs tied to a lesson's topic.
Examples: a Packet-Tracer-style network-routing sim for a lesson on
how packets are delivered across the internet; a TensorFlow.js-based
neural-network sim for a lesson on how artificial neural networks
work. Each generated simulation is a single self-contained HTML file
that runs entirely client-side — no server-side runtime dependency,
ships anywhere a browser does. The underlying pipeline is fully
operational: any generated HTML artifact runs in the Presentator.

*Open orchestration question (not a generator gap): whether the
upstream lesson / course generation logic reliably decides **when** a
lesson actually warrants a simulation. The sim generator works; the
"should I invoke it?" decision is the fuzzy part.*

### Game Generator
Produces classroom engagement games in formats teachers already run
in class — Jeopardy, Bingo, and similar. Distinct from simulations:
these are lightweight, teacher-facilitated activities used to break
up a lesson or review content, not hands-on labs.

### Textbook Generator
Produces textbook chapters. **Current scope: chapter-level only** —
does not yet assemble a full textbook.

### Printable Material Generator
Open-ended generator. The teacher describes what they need for the
classroom in natural language; the generator produces a printable
artifact. Used for anything that doesn't fit a narrower generator
above.

### Cross-Cutting Generator Capabilities

These apply to every generator above:

- **Multilingual output.** Default generation language is English,
  but any generator can produce content in a different language at
  the teacher's request — designed for multilingual classrooms and
  English-language-learner support.
- **Accessibility-aware generation.** Generators can adapt output
  for specific accessibility needs (e.g., dyslexia-friendly
  formatting). The goal is to make accommodations a generation
  parameter, not a manual retrofit after the fact.

## Editor Surface (Post-Generation)

Every generated artifact opens in a custom-built editor tailored to
the artifact type — e.g., slide decks open in a slide editor built
in-house for our slide format (similar in spirit to PowerPoint, but
specific to our content model). Other artifacts open in their own
type-appropriate editors.

Inside an editor the teacher can:

- **Regenerate** specific sections — regenerate this slide, regenerate
  the last three quiz questions, re-voice a segment of an explainer.
- **Manually edit** any content — text, ordering, structure — the way
  a teacher would in a conventional editor.

This is the stage that turns an AI-generated draft into teacher-owned
content. Without it, the generators would be a demo; with it, they're
a workflow.

## LMS Layer

All integration with external LMSs flows through **Edlink**, a
consolidated LMS-integration API that abstracts over Canvas,
Schoology, Google Classroom, ClassLink, Blackboard, D2L Brightspace,
PowerSchool, and others. We integrate with Edlink once; Edlink
handles the per-LMS specifics.

- **Currently live:** Canvas, Schoology.
- **Student content access:** students launch into our content from
  the source LMS via **LTI 1.1**.
- **Everything else** — roster import, assignment posting, submission
  posting, grade passback — goes through the Edlink API.

### Roster & Class Import
Classes and student rosters are pulled from the source LMS.

- **Direction:** one-way *in* (source LMS → our platform).
- **Imported data:** classes, student rosters.

### Presentator (Content Delivery Surface)
The classroom delivery component where students see generated
content: slides, explainer videos, simulations, games, classwork,
quizzes. This is the "run the class on our side" surface that
replaces the teacher presenting from the source LMS's native
delivery tools.

### Assignments & Submissions
Teachers assign generated artifacts (classwork, quizzes, projects)
to classes. The assignment is posted to the source LMS via Edlink so
it appears in the teacher's native gradebook. Students launch into
the assignment via LTI 1.1, complete the work inside our Presentator,
and submit inside our LMS Layer. Submissions are captured on our
side and posted back to the source LMS via Edlink.

### Gradebook
Student work is graded inside our LMS Layer — auto-graded where
possible (quizzes) and teacher-graded for open-ended submissions.

### Grade Sync — Back to Source LMS
Grades computed on our side are posted back to the source LMS via
Edlink so the district-of-record gradebook in Canvas or Schoology
stays the single source of truth for district reporting.

- **Direction:** one-way *out* (our platform → source LMS).

## What This Enables (End-to-End Teacher Flow)

1. Teacher imports their class + roster from Canvas or Schoology.
2. *(Optional)* Teacher uses the **Course Builder** to produce a
   full course scope-and-sequence at the start of a semester.
3. Teacher uses per-artifact generators to produce individual
   classroom artifacts — lessons, classwork, quizzes, videos,
   simulations, games, printables, textbook chapters — either inside
   a Course-Builder-produced course or standalone.
4. Teacher opens each generated artifact in its **Editor Surface**
   to regenerate sections, tweak wording, reorder content — making
   the draft classroom-ready.
5. Teacher runs class through the **Presentator**; students consume
   content on our platform.
6. Students complete assignments and submit inside our LMS Layer.
7. Grades flow back into the teacher's source LMS via Edlink.

The teacher never has to leave this loop to plan, build, customize,
deliver, assess, or report on a unit.

## What's Not Built Yet (Explicit Gaps)

- **Performance Task Generator.** The single biggest gap in the
  generator suite. 60–70% of CTE assessment is hands-on performance:
  students build a network, diagnose a patient scenario, cook a meal,
  frame a wall, present a business plan. Today's generators all
  produce question-based or content-based artifacts — nothing
  produces a full performance task. A Performance Task Generator
  should emit:
    - A **project brief** — the real-world scenario the student must
      respond to (e.g., *"Design a small-business network for a
      15-person office with three departments and specific security
      needs."*).
    - **Deliverables** — what the student produces (network diagram,
      IP plan, hardware list, written justification).
    - **A rubric** — criteria + performance levels for grading
      (e.g., 4 levels across 5 criteria).
    - **Milestones / checkpoints** — a sequenced work plan that
      breaks the project into class-sized chunks with due dates.
    - Optional **supporting materials** — reference docs, templates,
      scaffolds, exemplars.
  Aligned to the same LOs / standards / (future) credential objectives
  the other generators target. Once built, this is a real
  differentiator vs. academic-subject LMSs — legacy CTE publishers
  barely do this.
- **Full textbook assembly** — the textbook generator produces
  chapters, not full books.
- **Deeper source-LMS parity** — rostering, assignments, submissions,
  and grades round-trip via Edlink today; announcements and calendar
  integration are not yet in scope.
- **Adaptive delivery / personalization** — content is generated, not
  yet adaptively re-sequenced per learner.
- **Analytics & reporting beyond the gradebook** — e.g., Perkins V
  accountability reports, credential-readiness dashboards, district-
  level standards coverage.
- **State-standards crosswalk and atom library** as described in
  `../foundations/content-platform.md`. The Course Builder and the
  standards-surfacing + LO-unpacking flow are the v0 shapes of the
  architecture's Course Template and atom tiers, but the durable
  shared atom library, cross-state crosswalk layer, and full
  atom-based template model are the next architectural build-out.
- **Additional source LMSs beyond Canvas and Schoology.** Edlink
  supports many more (Google Classroom, ClassLink, Blackboard, D2L
  Brightspace, PowerSchool, etc.) — these are reachable via our
  existing Edlink integration but are not yet surfaced in product
  UI or onboarding.

## Open Questions / To Confirm

These are items in the inventory above where the description is
accurate at a capability level but the underlying detail is unspecified
in this doc. Fill in as we have answers.

1. **Underlying tech stack** — languages, frameworks, model providers
   (image generation, voice generation, text generation — which
   vendors?), database, hosting, CDN / media pipeline, auth system.
   Not captured here yet; document as we formalize the stack and the
   Founding Engineer lands.

## Relationship to the Content Platform Architecture

This inventory describes what exists today. The architecture in
`../foundations/content-platform.md` describes the durable shape
the product should take as it scales across states and pathways.

The two are compatible but not yet aligned: today's generators
produce artifacts directly; the architecture calls for artifacts to
be composed from *atoms* that live in a shared, state-neutral
library and are tagged to industry credentials and state standards.
Bridging the two — i.e., making the generators produce (or wrap)
atoms rather than one-off artifacts — is future work and is the most
important architectural decision the Founding Engineer will face.

Two existing capabilities map cleanly to architecture concepts and
will be the natural anchor points for that migration:

- The **Course Builder** is the v0 precursor to the architecture's
  **Course Templates**. Today it emits units + lessons directly;
  architecturally it should emit a template that composes atoms per
  slot and tags them to the target state's standards via the
  crosswalk.
- The **standards-surfacing + LO-unpacking** step in the Generation
  Flow already treats learning objectives as the atomic unit of
  instruction. An LO in the current product is the same competency
  statement that would anchor an atom in the architecture.
