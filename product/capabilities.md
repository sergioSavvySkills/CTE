# Product Capabilities — Current State

## Purpose

Snapshot of what exists in the product today. This file is the
answer to "what have we actually built?" — useful for onboarding new
hires, briefing advisors, pitching design partners, and sanity-checking
scope decisions. It is a *current-state inventory*, not a roadmap and
not a spec for future work.

Keep this file updated as capabilities ship, mature, or get cut.

## Architecture at a Glance

The product has two halves that fit together:

1. **Generator Suite** — AI-powered tools that produce digital
   classroom artifacts from teacher inputs.
2. **LMS Layer** — the class-execution environment where students
   consume generated content, submit work, and get graded. The LMS
   Layer is interoperable with the teacher's existing LMS (Canvas,
   Schoology today) through Edlink; students launch into our content
   via LTI 1.1.

Generators produce artifacts. The LMS Layer delivers those artifacts
to students and captures the resulting work. Both halves are digital-
first; nothing ships as a static PDF by default.

## Generator Suite

Every generator below is operational and produces shippable output.
Each one takes teacher-provided inputs (topic, learning objective,
constraints, style preferences) and returns a digital artifact
consumable in the LMS Layer.

### Lesson / Slide Deck Generator
Produces a lesson as a slide deck rendered in the Presentator. Covers
the instructional arc (intro, content, checks for understanding,
close) rather than a bare set of bullet slides.

### Classwork Generator
Produces in-class activities: structured exercises, worksheets,
discussion prompts, and applied tasks tied to a lesson's objectives.

### Quiz Generator
Produces quizzes with multiple question types. Output is delivered
as an auto-gradable assignment inside the LMS Layer.

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
ships anywhere a browser does.

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
2. Teacher uses the Generator Suite to produce a lesson (slides,
   classwork, quiz, optional video / simulation / game, optional
   printable support material, optional textbook chapter).
3. Teacher runs class through the Presentator; students consume
   content on our platform.
4. Students complete assignments and submit inside our LMS Layer.
5. Grades flow back into the teacher's source LMS.

The teacher never has to leave this loop to build, deliver, assess,
or report on a unit.

## What's Not Built Yet (Explicit Gaps)

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
- **State-standards crosswalk and course templates** as described in
  `../foundations/content-platform.md`. The generators produce
  content; the atom library + crosswalk + template layers that tie
  content to state standards and course shells are the next
  architectural build-out.
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
