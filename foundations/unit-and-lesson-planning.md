# Lesson and Unit Planning — Maya's Playbook

*Owner: Maya Delgado, Founding Curriculum Designer. Updated
2026-04-18.*

This is the pedagogical counterpart to `content-platform.md`. That doc
says *what* the layers are (atoms, crosswalks, templates, overlays).
This doc says *how* a curriculum designer turns a stub into a full
unit — lesson shape, activity taxonomy, generator mapping, and the
rules for picking the right activity for a given skill.

If you're a designer sitting down with an atom stub on Monday morning,
start here.

## What "done" looks like for a lesson

Every lesson ships as a slide deck rendered in the **Presentator**.
Real CTE teachers shift between three lesson shapes depending on what
kind of atom they're teaching. Pick one of the three below *before*
running the generator.

### Selection table (pick Shape first)

| atom `skill_type` | Default Shape |
|---|---|
| `knowledge` | A — Gradual Release |
| `skill` | B — Workshop Model |
| `both` | C — 5E / Inquiry (if discoverable) else A |

### Shape A — Gradual Release (default for knowledge atoms)

Hook (1 slide) → Objective (1) → Direct instruction (4–8) → Guided
application (2–4) → Check for understanding (1–2) → Close (1).

The Madeline Hunter / I-Do-We-Do-You-Do arc. Use for conceptual,
vocabulary, or framework lessons where students need the content
*before* they can apply it.

CTE examples I've taught: medical-terminology word parts, AI history,
networking fundamentals, the Troubleshooting Methodology lesson in
any IT pathway.

### Shape B — Workshop Model (default for skill atoms)

Hook (1) → Objective + quick demo (2–3) → **Work time / lab
(20–25 min)** → Share out (2–3) → Close (1).

Thinner instruction, much bigger practice block. Use for hands-on
skill-building where the best teaching is watching the teacher do it
once, then doing it yourself while the teacher coaches. Simulation
atoms almost always live in Shape B.

CTE examples: Teachable Machine training, router-config lab, PC
assembly, Pandas debugging session, a knife-technique lesson in
Culinary I.

### Shape C — 5E / Inquiry (for `both` atoms when content is discoverable)

Engage (1–2 slides: phenomenon or question) → Explore (hands-on or
dataset exploration, 10–15 min, *before* vocabulary is introduced) →
Explain (3–5: teacher names what students just observed) →
Elaborate (1–2: extension) → Evaluate (1–2).

Use when students can *see the pattern before hearing the rule*.
The Explore phase front-loads the hands-on; the Explain phase pays
the conceptual debt afterward. Strong for ethics lessons, bias
discovery, data patterns, any content where the phenomenon is
accessible without vocabulary.

CTE examples: an "explore a dataset and notice what's weird about
it" lesson, a bias-discovery lab with Teachable Machine, an ethics
case study that opens with the facts before naming the framework.

Fall back to Shape A if the `both` atom is too dense to discover
from scratch — e.g., a lesson on Python OOP with methods vs.
functions isn't a Shape C lesson, it's Shape A.

### Budget and cuts

All three shapes fit in a 45-minute period with room to breathe. If
a deck can't run in 45 minutes, it's too long — generators
over-produce, the editor is where you cut. Block-schedule teachers
combine two 45-minute decks per day.

## Delivery mode — voice-over slides or video-first

Two modes, used interchangeably per lesson based on content fit.
Designer records `delivery_mode: voice-over | video-first` in the
lesson frontmatter, and adds a one-line `delivery_rationale` only
when the choice is non-obvious.

The **"slides + live teacher voice"** option is intentionally NOT a
named mode. Both modes below ship with a deck that has narration or
video; teachers can always mute the audio and present live over the
visuals if they want. That's an inherent capability of the decks,
not a third mode.

### Mode 1 — Voice-over slides (the default for most lessons)

Every slide ships with AI-generated narration. Teacher runs class:
plays the deck, pauses to add context, asks the class questions
between slides, mutes a slide and presents live where their own
expertise adds value.

**Pick this when:**
- Content is mostly conceptual, vocabulary, or framework-driven
  (Shape A lessons).
- Lesson is a Shape B where narration sets up the activity and the
  teacher coaches during work time.
- Discovery-style Shape C where narration carries the Engage /
  Explain / Evaluate phases and students do hands-on Explore in
  between.

**Why this is the default:**

- **Teacher relief.** The deck does the heavy narration; teacher
  pauses to add their own value rather than carrying every minute on
  the mic. This is the single biggest teacher-product win I've
  heard in 9 years of teacher conversations.
- **Consistent baseline.** Every student in every cohort sees the
  same canonical explanation, regardless of teacher.
- **Asynchronous compatibility.** Same deck works for in-class,
  flipped, makeup, and remote without re-authoring.
- **ELL support.** Narration models pronunciation; captions follow
  the audio for free.

**Constraint:** every slide edit requires voice-over re-render.
Treat voice-over decks as "freeze when ready" — iterate the textual
deck first, then render narration once the content is stable.

### Mode 2 — Video-first opening (interchangeable alternative)

Lesson opens with a 3–5 minute explainer video (Video Explainer
Generator) covering the core concept, then transitions into slides
for application, check, and close.

**Pick this when:**
- Content is highly visual or dynamic and a still-image slide would
  degrade it (packets routing across a WAN, mitosis, transistor
  switching, how blood flows through the heart, how an algorithm
  sorts a list).
- Concept benefits from a single canonical animated explanation
  shared across cohorts and across teachers (math-heavy or
  diagram-heavy topics where teacher delivery varies widely).
- Story flows better as video than as slides (lab walkthroughs,
  field-tour openers, real-practitioner interviews).

**Constraint:** respect the attention cliff. No explainer over 5
minutes without a deliberate pause-and-interact checkpoint built
into the deck immediately after.

### Always-on constraints (regardless of mode)

Both modes bind to these rules:

1. **Hook videos at the start of a Mode 1 lesson are 60–90 seconds
   max.** Mode 2's opener is the longer 3–5 minute video.
2. **Embedded concept-explainer clips inside a slide are 90–180
   seconds max** in either mode. They are inline, not lesson
   replacements.
3. **Every lesson has one application activity** (from the 12-type
   taxonomy below).
4. **Every lesson has a check for understanding** built into the
   deck as a 2–3 item interactive — both modes need this in-deck so
   the lesson stands alone for absent / async students.

## The activity taxonomy — what goes in slide set #4

Every lesson gets *at least one* application activity. No exceptions.
Reading and watching aren't applying. Here are the twelve shapes I'll
sign off on. Pick one. Two if the lesson is 60 minutes.

### 1. Comparison cases (A / B / C)

Present 2–4 parallel cases side-by-side and have students predict or
analyze how outcomes differ. The cases can be **people** (two
startups with different cultures), **configurations** (three router
settings, which one performs best), **decisions** (three filing
statuses, which owes what), **policies**, **datasets** — anything
comparable.

- *DS/AI example:* Three ML models trained on the same data with
  different bias — which misclassified which group, and why?
- *IT example:* Three troubleshooting approaches to the same symptom
  — which tech reached the root cause fastest?

Slide shape: a 3-column layout with the same fact-set per column,
then a "so what?" question slide. Classwork generator can produce the
analysis worksheet as homework extension.

### 2. Simulation / virtual lab

Interactive HTML simulation embedded in the deck. Students manipulate
variables and see consequences. This is the Simulation Generator's
job, not the slide generator's.

- *DS/AI example:* A Teachable-Machine-style neural-network trainer;
  student feeds biased images, watches accuracy drift.
- *IT example:* Packet-Tracer-style router monitor; student
  misconfigures a subnet and sees packets dropped in real time.
- *Business example:* A TurboTax-shaped tax-filing simulator;
  student picks filing status and inputs, compares refund outcomes.

One sim per lesson max. They take 15–20 minutes to run well.

### 3. Sort / classify

Student drags items into buckets. Fast, visual, works for
categorical knowledge.

- *DS/AI example:* Classify 10 real AI products into ML / NLP / CV /
  Speech / GenAI.
- *IT example:* Sort 12 cables by connector type.

### 4. Sequencing

Student orders steps. Great for procedures, troubleshooting methods,
anything with a defined sequence.

- *IT example:* Six troubleshooting steps out of order — sequence
  them correctly.
- *DS/AI example:* Seven stages of an ML project — put in order.

### 5. Prediction before reveal

"What do you think will happen if…?" Student writes or clicks a
prediction, then the deck reveals the answer. Primes attention and
exposes misconceptions.

- *DS/AI example:* Before running a biased classifier, students
  predict which demographic it will misclassify most.
- *IT example:* Predict which of four config changes breaks the
  connection; then run it and see.

### 6. Diagnosis / troubleshooting

Student is given a symptom and must propose cause + fix. Core to
every service-oriented CTE pathway.

- *IT:* "User reports no network. Here's the ipconfig output. What's
  wrong?"
- *Health Science:* "Patient presents with X. Which vitals would you
  check first?"

### 7. Decision tree / branching scenario

Click-through "choose your own adventure." Student makes a decision,
sees the next scene based on that decision. Works beautifully for
ethics, customer service, management.

- *DS/AI example:* Your AI model shows bias. Do you (a) retrain, (b)
  ship anyway, (c) escalate? Each choice branches.
- *Business example:* Customer complaint scenarios.

### 8. Error-spotting / debug

Show something broken; student finds the mistakes.

- *Programming:* Here's a 15-line function that's supposed to sum
  odd numbers. It's wrong. Find the bug.
- *IT:* Here's a router config that doesn't route. What's missing?

### 9. Design challenge

Given constraints, sketch a solution. Time-boxed, not a multi-day
project.

- *Networking:* "Design the smallest network that connects 3
  departments of 5 people each with one shared printer."
- *DS/AI:* "Sketch how you'd collect training data for a school-
  specific lunch-recommender."

### 10. Data / log / chart interpretation

Present a dataset, chart, or log excerpt; student answers 3–4
structured questions about it.

- *IT:* "Here's the last hour of the firewall log. What attack is
  happening?"
- *DS/AI:* "Here are the per-class accuracy numbers. Which class is
  underperforming and what would you change?"

### 11. Role-play / scripted scenario

Student is given a role and a situation. Short — a 5-minute
interaction, not a skit. Great for soft skills **embedded in
subject matter** (which is why soft-skill atoms thread across units
rather than living alone).

- *IT help desk:* "You're the level-1 tech. The caller says their
  email won't send. What do you ask first?"

### 12. Live poll / voting

Class-wide snap poll. Use the Presentator's live-poll slide.
Lightweight activation, not sole application activity — pair with one
of #1–#11.

## Activity choice by atom skill_type (inside the Shape)

Once you've picked the Shape from the atom's `skill_type` (see the
Selection table above), pick the activity type that fits the slot
the Shape defines for it:

- **Shape A (knowledge atom):** the "Guided application" slot takes
  comparison, sort/classify, sequencing, data interpretation,
  decision tree, or prediction.
- **Shape B (skill atom):** the "Work time / lab" block takes
  simulation, diagnosis, design challenge, error-spotting, or
  role-play. This is the big block; the activity *is* most of the
  lesson.
- **Shape C (both atom, discoverable):** the "Explore" phase takes
  data interpretation, diagnosis, or design challenge; the
  "Elaborate" phase takes comparison or decision tree.

Do not pair a knowledge atom with a simulation. Do not teach a
skill atom with only comparison cases. If the atom says "apply,"
the activity must require applying.

## Unit-level activity mix

Across a 6-to-10-lesson unit:

- Target **at least one simulation** per unit if any atom in the unit
  has `skill_type: skill` or `both`. Teachers won't buy a "hands-on"
  unit that's actually a lecture unit.
- **Do not repeat the same activity type back-to-back.** If lesson 3
  is a comparison case, lesson 4 should be a different shape.
- **Performance task** anchors every unit. The Performance Task
  Generator isn't live yet (see `product/capabilities.md`), so for
  now we define performance tasks manually at the unit level and
  treat them as multi-lesson activities with a rubric.
- **Game as review, not instruction.** Jeopardy-style review games
  belong at unit close, not in the middle.

## Generator mapping

Which product generator produces which part of a lesson:

| Lesson part | Generator | Notes |
|---|---|---|
| Slide deck (hook → close) | **Lesson / Slide Deck Generator** | Produces the deck; activity slides inline |
| Voice-over narration on the deck | **Voice-over render pipeline** (Mode 1 finishing step) | AI narration per slide; freeze when content stable |
| Simulation embedded in deck | **Simulation Generator** | Self-contained HTML; stays inside deck |
| Video on a slide | **Video Explainer Generator** | Three uses per delivery rules: 60–90s hook opener (Mode 1), 90–180s embedded concept-explainer (either mode), 3–5 min video-first opener (Mode 2). Never longer than 5 min without an interact checkpoint. |
| Exit ticket | **Quiz Generator** (sub-type: exit ticket) | 3 items, end of class |
| Take-home practice | **Classwork Generator** (sub-type: independent practice) | Homework placement |
| Unit-end review | **Game Generator** (Jeopardy / Bingo) | Unit-close only |
| Printable worksheet | **Printable Material Generator** | Equity fallback for non-1:1 classrooms |
| Chapter reference | **Textbook Generator** | Chapter-level only today — treat as optional supplementary |
| Multi-lesson project | **Performance Task Generator** *(not yet built)* | Manually scaffold until the generator ships |

## Planning a unit from atom stubs

The concrete workflow for a designer sitting with a unit's worth of
atoms:

1. **Pick the unit's through-line.** One sentence: what students will
   be able to do at the end of this unit that they couldn't at the
   start. Write it on the whiteboard before touching the atom files.
2. **Pick the performance task.** What is the unit-capstone artifact
   or demonstration? Work backward from this.
3. **Order the atoms.** Knowledge → skill → both. Don't pair a
   dependent atom before its prerequisite. (If the SME-review script
   yells, fix the order.)
4. **For each atom, pick the activity type.** Use the skill_type
   rules above. Write the activity one-liner in the lesson's content
   stub under a "Activity" subsection before running the generator.
5. **Vary the mix across the unit.** Avoid three comparison-cases
   lessons in a row; alternate shapes.
6. **Run the Course Builder** to produce the deck scaffolds; edit in
   the Editor Surface. The builder will propose activities; your job
   is to swap in the right activity type where the default is weak.
7. **Pilot with one teacher** before shipping the unit to the TAP
   cohort.

## Things I will reject in review

- A lesson with no application activity.
- A lesson whose "activity" is "discuss with your neighbor for 2
  minutes" with no prompt, structure, or artifact.
- A unit where 4+ lessons use the same activity type.
- A skill-type atom paired with a knowledge-type activity (comparison
  when the atom requires doing).
- A Shape that doesn't match the atom's `skill_type` — e.g., a Shape
  A lesson on a skill atom, or a Shape C on a dense atom that can't
  be discovered from scratch.
- `delivery_mode` missing from the lesson frontmatter, or set to
  `video-first` without a `delivery_rationale` that cites a Mode 2
  condition (dynamic/visual content, canonical-explanation need, or
  video-native storytelling).
- An activity so long it eats the direct-instruction time; activities
  serve content, they don't replace it.
- Employability/soft-skill content presented as a standalone lesson
  instead of threaded through a content lesson. Standard 1 of every
  CTAE course says *"integrated throughout;"* I'll hold us to that.

---

## What I still need from Sergio and engineering

1. **Performance Task Generator.** This is the single biggest missing
   piece. 60-70% of CTE assessment is hands-on performance. Until
   this ships, every unit's capstone is hand-authored, which does not
   scale across states.
2. **Activity-type presets surfaced in the generators.** The Classwork
   and Quiz generators already support sub-types via prompt; the
   twelve activity types above should become selectable presets in
   the Lesson Generator specifically.
3. **Slide-native interactive primitives.** Drag-and-drop, live poll,
   click-to-reveal, branching click-throughs. If these aren't first-
   class in the slide format, activities 3, 4, 5, 7, and 12 get
   degraded to static versions.

File updates as these ship.
