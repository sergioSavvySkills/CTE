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
   Schoology) via roster import and grade sync.

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
objective. *(Format, length, and generation pipeline: to confirm.)*

### Simulation Generator
Produces interactive simulations students can run inside the
Presentator. *(Scope of supported simulation types: to confirm —
useful to document whether this is generic interactive content or
CTE-specific sims like network labs, OS install flows, etc.)*

### Game Generator
Produces educational games students can play inside the Presentator.
*(Format, genre, and generation pipeline: to confirm.)*

### Textbook Generator
Produces textbook chapters. **Current scope: chapter-level only** —
does not yet assemble a full textbook.

### Printable Material Generator
Open-ended generator. The teacher describes what they need for the
classroom in natural language; the generator produces a printable
artifact. Used for anything that doesn't fit a narrower generator
above.

## LMS Layer

### Source LMS Integration — Roster & Class Import
Teachers can import classes and rosters from their existing LMS.

- **Supported source LMSs:** Canvas, Schoology.
- **Imported data:** classes, student rosters.
- **Direction:** one-way *in* (source LMS → our platform) for roster
  and class setup.
- **Protocol / mechanism:** to confirm (OneRoster, LTI, direct API —
  document whichever is in use).

### Presentator (Content Delivery Surface)
The classroom delivery component where students see generated
content: slides, explainer videos, simulations, games, classwork,
quizzes. This is the "run the class on our side" surface that
replaces the teacher presenting from the source LMS's native
delivery tools.

### Assignments & Submissions
Teachers assign generated artifacts (classwork, quizzes, projects)
to classes. Students complete and submit inside the LMS Layer.
Submissions are captured and stored on our side.

### Gradebook
Student work is graded inside our LMS Layer — auto-graded where
possible (quizzes) and teacher-graded for open-ended submissions.

### Grade Sync — Back to Source LMS
Grades computed on our side are synced back to the teacher's source
LMS (Canvas, Schoology) so the district-of-record gradebook stays
the single source of truth for district reporting.

- **Direction:** one-way *out* (our platform → source LMS) for grades.
- **Protocol / mechanism:** to confirm (LTI Assignment and Grade
  Services / OneRoster Gradebook / direct API — document whichever is
  in use).

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
- **Deep source-LMS parity** — only roster import (in) and grade
  sync (out). Assignment round-tripping, announcements, and calendar
  integration are not in scope yet.
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
- **Additional source LMSs** — Google Classroom, PowerSchool, and
  others are not yet integrated.

## Open Questions / To Confirm

These are items in the inventory above where the description is
accurate at a capability level but the underlying detail is unspecified
in this doc. Fill in as we have answers.

1. Video Explainer Generator — generation pipeline (AI-generated
   footage vs. AI voice-over on stock/scripted visuals vs. other),
   typical output length, delivery format.
2. Simulation Generator — supported simulation types, whether output
   is CTE-domain-specific or general-purpose interactive content.
3. Game Generator — supported game formats / genres, generation
   pipeline.
4. Roster import protocol (Canvas and Schoology specifically).
5. Grade sync protocol (Canvas and Schoology specifically).
6. Underlying tech stack — languages, frameworks, model providers,
   hosting. Not captured here yet; document as the Founding Engineer
   lands and we formalize the stack.

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
