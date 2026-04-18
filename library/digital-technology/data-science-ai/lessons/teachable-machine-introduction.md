---
lesson_id: teachable-machine-introduction
atom_id: teachable-machine-introduction
subcluster: data-science-ai
title: "Training Your First ML Model with Teachable Machine"
shape: B
delivery_mode: voice-over
delivery_rationale:
duration_minutes: 45
prerequisites:
  - ai-domains-ml-nlp-cv
credential_objectives:
  - certiport-its-artificial-intelligence::3.3
  - ms-ai-900::2.1
standards_hit:
  georgia:
    - IT-FAI-3.6
    - IT-AIC-3.3
    - IT-AIA-5.7
status: golden-reference
reviewer: maya-delgado
review_date: 2026-04-18
---

# Training Your First ML Model with Teachable Machine

*Golden-reference lesson — the shape every future atom-expansion
should target. First lesson where students build an AI instead of
hearing about one. Kids remember this one, which is why it carries a
lot of weight in the pathway.*

## Lesson at a glance

| | |
|---|---|
| Shape | B (Workshop Model) |
| Delivery mode | Voice-over slides (Mode 1 default) |
| Duration | 45 min (30 min work block) |
| Prerequisite atom | `ai-domains-ml-nlp-cv` |
| Atom skill_type | `skill` |
| Activity type | #2 Simulation (Teachable Machine itself) |
| Core artifact students produce | A trained 2-class image classifier in Teachable Machine |

## Materials

Per student:
- A Chromebook / laptop with a working **webcam** and a modern browser
  (Chrome, Edge, or Safari — Teachable Machine works in all three).
- Internet access. Teachable Machine runs entirely in-browser; no
  install.

Per room:
- Projector or shared screen for the teacher's live demo.
- (Optional) a small 3D-printable "prop kit" — a flashcard with a
  thumbs-up printed on it, a hat, a pair of glasses — for students
  who are shy about using their own face in training.

## Teacher prep (5 min before class)

1. Open a blank Teachable Machine image project on the projected
   screen. Sign out of any personal Google account; you want a clean
   session students can mirror.
2. Verify the webcam permission on the teacher browser. If it asks
   again for permissions in front of students, that's fine — model
   the "click Allow" flow.
3. Pre-load slide 5's class names ("Waving" and "Not Waving") so the
   live demo is fast.
4. Have a visible timer on the projector; students pace themselves
   better when they see time remaining.

## Common misconceptions to watch for

| Misconception | What to say |
|---|---|
| "The model is memorizing my samples" | "Partially. It's learning a pattern from your samples. Test it on a new pose and see." |
| "More is always better" | "More *varied* is better. Thirty samples of one pose still only knows one pose." |
| "The accuracy percentage is the model's IQ" | "Accuracy is about this batch. Feed it new data, accuracy changes." |
| "If it's 100% accurate, it's perfect" | "If you got 100% on your first try, your two classes might be too similar or you tested with only what you trained. Test harder." |

## Differentiation

- **Stretch for fast finishers:** add a third class and see how
  accuracy behaves. Then export the model and paste it into a p5.js
  sketch (Teachable Machine provides the snippet).
- **Scaffold for students who struggle:** pair-up, pick classes from
  the prop kit, split the labor (one collects "Class 1" samples, the
  other collects "Class 2"). Reduces the friction of on-camera
  self-consciousness.
- **ELL support:** the narration is auto-captioned; pre-teach the
  five vocab words below; pair ELL students with bilingual peers
  where possible.

## Vocabulary (pre-taught in the prior lesson)

- **Machine learning** — computers learning patterns from examples
  instead of being programmed with rules.
- **Classifier** — a model that puts inputs into categories.
- **Training sample** — one example you show the model.
- **Accuracy** — the percent of examples the model got right.
- **Generalize** — work correctly on examples it hasn't seen before.

---

## Slide-by-slide script

### Slide 1 — Hook (2 min)

**On-screen:** a 60-second looping video, split-screen. Left: a
teenager waving at a laptop. Right: the laptop's screen showing a
label update in real time: "Waving → 97% confidence." Title overlaid:
*"In 25 minutes, you're going to make this."*

**Voice-over:**
> "Look at this. A camera sees a face. A program decides whether that
> person is waving or not. That program is artificial intelligence,
> and the thing making it work is called machine learning. In the
> next 25 minutes, you're going to build one of these yourself. No
> coding required. By the end of class, you will have trained your
> first AI model. Ready? Let's go."

**Teacher note:** Pause narration here. Ask the room: *"What else
does your phone do this way?"* Take 3–4 answers. Don't correct
anyone. This is warm-up, not evaluation.

---

### Slide 2 — Objective (1 min)

**On-screen:**

> **Today you'll:**
> 1. Use Google **Teachable Machine** to train an image classifier.
> 2. Hit at least **80% accuracy** on new images.
> 3. Explain **why your model got some examples wrong.**

**Voice-over:**
> "Three things by the end of class. First, you'll train an image
> classifier with Google's Teachable Machine. Second, you'll get
> 80% accuracy on images you didn't train on. Third — and this is
> the one that matters — you'll be able to explain why it got the
> wrong ones wrong. Goal three is the real skill. Let's go."

---

### Slide 3 — Getting in (1 min)

**On-screen:** screenshot of `teachablemachine.withgoogle.com` with
the "Get Started" button circled. Then a second screenshot with
"Image Project" → "Standard Image Model" circled.

**Voice-over:**
> "Open a browser. Go to t-e-a-c-h-a-b-l-e-m-a-c-h-i-n-e dot
> w-i-t-h-g-o-o-g-l-e dot com. Click Get Started, then Image Project,
> then Standard Image Model. Your screen should look like this."

**Teacher note:** Pause playback. Wait 60 seconds. Walk the room.
Two common fails:
- Student picked "Embedded Image Model" (for microcontrollers). Have
  them back up and pick Standard.
- Student clicked Block on the camera permission. Go to browser
  settings → site permissions → camera → Allow. Then reload.

---

### Slide 4 — The whole tool on one screen (2 min)

**On-screen:** screenshot of the Teachable Machine training interface
with three numbered callouts:
1. **Class names** (left column — "Class 1", "Class 2")
2. **Webcam / Upload** button per class (middle)
3. **Train Model** button (right column)

**Voice-over:**
> "Three parts. On the left, you name your classes. In the middle,
> you give each class training samples from your webcam. On the
> right, you click Train Model. That's the whole tool. I'm going to
> do one round with you watching, then you'll do your own."

---

### Slide 5 — Teacher live demo (5 min)

**On-screen:** the teacher's live Teachable Machine browser, projected.
Pre-loaded with "Waving" and "Not Waving" as class names. Slide
background is a subtle border marking this as a live demo moment.

**Voice-over OFF for this slide.** Teacher narrates live.

**Teacher script (approximately):**
> "Watch. I click the webcam button for 'Waving.' Hold to record. I
> wave for about 30 seconds — see the counter going up, I have 87
> samples now. Good enough. Now Class 2, 'Not Waving.' I hold still.
> 30 seconds. About 80 samples. Now the big button — Train Model.
> Don't close the tab. Training bar. Done. Preview is on. Watch —
> when I wave, the bar jumps to 'Waving' 98%. Stop, 'Not Waving'
> 99%. That's it. Total time: about 90 seconds. That was machine
> learning."

**Teacher note:** Do this live even though narration exists for it in
draft. The magic-feeling is real and it sells the lesson. If you
must use the voice-over, at least let the class see your webcam
during the demo.

---

### Slide 6 — Your turn (instructions) (1 min)

**On-screen:**

> **Your turn: Build a 2-class classifier**
>
> 1. Pick two classes that are **visually distinct** (not "red pen vs
>    blue pen" — pick "holding a book vs holding nothing").
> 2. Collect **at least 30 samples per class**.
> 3. Click **Train Model**.
> 4. Hit **Preview** and test with poses you didn't train on.
>
> **Target:** 80% accuracy on your preview tests. **Time:** 15 min.

**Voice-over:**
> "Pick two visually distinct classes — not just color differences,
> your webcam can't always see those. At least 30 samples per class.
> Train. Preview. Target: 80 percent on new poses. You have 15
> minutes. Go."

---

### Slides 7 — Work time (15 min, embedded simulation)

**On-screen:** a single slide hosting the student's own Teachable
Machine session inline (iframe) OR a side-by-side with simple
instructions. Students spend the next 15 minutes here. **Narration
is OFF** for this block.

**Teacher behavior:** this is the Shape B Workshop block. Walk the
room. Don't lecture. Coach.

**Expected situations and what to say:**

| What you see | What to say |
|---|---|
| Student frozen picking classes | "Two things your webcam can clearly tell apart. Glasses / no glasses. Thumbs up / thumbs down. Leaning left / leaning right. Pick one." |
| Student trained on one background only | "Now try standing somewhere else." *Watch accuracy drop. Let them see it. Don't fix it for them.* |
| Student trained only 5 samples | "What did Google recommend?" *Send them back.* |
| Student hits 100% on first try | "Test with a different angle or different lighting. Does it still work?" *Usually: no.* |
| Model stuck training | Refresh the page. Has to be done, Teachable Machine occasionally hangs. |
| Student says "it's broken" | "Walk me through what you did." *They usually fix it themselves while narrating.* |

---

### Slide 8 — Mid-work check (2 min, ~17 min in)

**On-screen:**

> **Pause. Answer in the chat / on a sticky / out loud:**
> 1. What two classes did you pick?
> 2. What was your first-try accuracy before you added more samples?

**Voice-over:**
> "Pause your work for two minutes. Two questions. Your class pick
> and your first-try accuracy. Go."

**Teacher note:** Call on three students at random (not volunteers).
You're sampling for the range — you want a 50%, a 75%, and a 95%
answer to surface in share-out later. Log them mentally.

---

### Slide 9 — Share out, part 1 (3 min)

**On-screen:**

> **Who got 80%+?**
>
> *Raise hand. Then: what changed between your first try and your
> best result?*

**Voice-over:**
> "Show of hands — 80 percent or better? Good. Now: who got there
> AND can explain what changed between the first try and the best
> try? That's the skill today. Tell us."

**Teacher note:** Call on three students with different stories. Push
each of them: "What changed?" Likely answers and how to push back:

- *"I added more samples."* → "Why did that help?"
- *"I moved around more."* → "So what was the model really
  learning?"
- *"I used different lighting."* → "Why does lighting matter for an
  image model?"

Let students explain the answers to each other. You're the
conductor. This is why Shape B works — the activity IS the lesson.

---

### Slide 10 — The three rules (2 min)

**On-screen:**

> **The three things that matter:**
>
> 1. **More samples per class** — more examples → better
>    generalization.
> 2. **Varied samples** — different angles, lighting, backgrounds.
> 3. **Visually distinct classes** — the model can only learn what
>    the camera can see.

**Voice-over:**
> "Three rules from what you just saw. More samples. Varied samples.
> Distinct classes. Those three rules carry forward every time you
> train any AI model, in this class, in Concepts next year, and in
> your first job. Write them in your notes."

---

### Slide 11 — Check for understanding (5 min, in-deck interactive)

**On-screen:** three-item interactive check.

**Question 1 — multiple choice:**
> Which of these would likely cause a trained model to fail on new
> images?
> - a. Training all samples against one background color
> - b. Having 30 samples per class
> - c. Picking two visually distinct classes
> - d. Using the webcam instead of uploaded images

*Correct: **a**. Training on one background means the model learned
"this background" as part of the class. When the background changes,
it fails. This is overfitting.*

**Question 2 — short answer:**
> In one sentence: what is the difference between "training accuracy"
> and "preview accuracy" in Teachable Machine?

*Looking for answers in the spirit of: "Training accuracy is how well
it learned what you showed it; preview accuracy is how well it
generalizes to new examples. If training is high and preview is
low, that's overfitting."*

**Question 3 — drag to bucket:**
> Classify each situation as *likely to train well* or *likely to
> struggle*:
> - 50 samples of smiling, 50 of neutral, varied lighting → **train
>   well**
> - 30 samples, all in the same chair with the same background →
>   **struggle** *(one-background trap)*
> - 10 samples per class, different clothing → **struggle** *(too
>   few samples)*
> - 40 samples each of "red book" vs "blue book" with the same
>   cover design → **struggle** *(visually too similar for a webcam)*

**Voice-over:**
> "Three questions. Answer all three before the bell. This goes to
> your grade. Ninety seconds."

**Teacher note:** Data from this auto-grades into the gradebook via
the Edlink pipeline. Log which students got Q3's last item wrong —
that's the subtle one, and it's the one that surfaces whether they
internalized the "what can the camera see" principle.

---

### Slide 12 — Close and tomorrow (1 min)

**On-screen:**

> **Tomorrow:** we'll take the classifier you just trained and break
> it on purpose. We're going to talk about **bias** — what happens
> when AI works for some people and not others. Keep your Teachable
> Machine project open or saved.
>
> **Homework:** none. Show up with a working classifier.

**Voice-over:**
> "Tomorrow you'll take the model you trained today and break it on
> purpose. We'll talk about bias — when AI works for some people and
> not others. Come in with a model that still works so we can watch
> it stop working. Homework: none. Nice job today."

---

## Assessment — how the exit ticket scores

| Item | Points | Rubric |
|---|---|---|
| Q1 (MC) | 1 | Auto-graded |
| Q2 (short) | 2 | 2 pts if both concepts present (training = seen data; preview = new data). 1 pt if only one present. 0 if neither. |
| Q3 (drag) | 2 | Auto-graded; half-credit if 3 of 4 correct. |

Total 5 points, posts to gradebook via Edlink. Below-3 score flags a
student for a short re-teach conversation the next class.

## Activity specification (for the Simulation Generator)

For this lesson the "simulation" is Teachable Machine itself, not a
generated artifact. The deck embeds it either as:

- An iframe to `teachablemachine.withgoogle.com` if the classroom's
  network allows cross-origin iframes, OR
- A link-out button that opens TM in a new tab while the student's
  progress slide stays visible.

Future v2 of this lesson should replace the iframe with a locally-
hosted clone (the Simulation Generator can produce a simpler
teach-and-classify sim in 200 lines of TensorFlow.js). That removes
the network dependency.

## Pacing

| Block | Slides | Minutes |
|---|---|---|
| Hook + Objective | 1–2 | 3 |
| Tool tour + teacher demo | 3–5 | 8 |
| Your-turn setup | 6 | 1 |
| Work time | 7 | 15 |
| Mid-work check + share-out | 8–9 | 5 |
| Three rules | 10 | 2 |
| Check for understanding | 11 | 5 |
| Close | 12 | 1 |
| **Total** | **12** | **40** |

5-min buffer for transitions / tech issues / one student who gets
way ahead. If the lesson consistently runs short, move slide 11 to
the start of the next class as a warm-up; if it runs long, cut the
share-out to one student instead of three.

## Standards covered

| Framework | Standard | Coverage strength |
|---|---|---|
| Georgia CTAE | IT-FAI-3.6 | primary |
| Georgia CTAE | IT-AIC-3.3 | partial (lays the foundation; Concepts course completes it) |
| Georgia CTAE | IT-AIA-5.7 | introduces |
| Certiport ITS AI | objective 3.3 (Algorithms and Models — training) | primary |
| Microsoft AI-900 | objective 2.1 (ML principles) | primary |

## Generator composition

What each part of the product produces for this lesson:

| Part | Generator | Notes |
|---|---|---|
| Slide deck (12 slides) | Lesson / Slide Deck Generator | |
| Voice-over for all slides | Voice-over render pipeline | Render after slide content is frozen |
| Hook video on slide 1 | Video Explainer Generator | 60-sec loop, split-screen |
| Embedded simulation (slide 7) | Simulation Generator (wrapper) | v1 is iframe; v2 is local clone |
| Exit ticket (slide 11) | Quiz Generator (sub-type: exit ticket) | 3 items, auto-grade |
| Delivery to student | Presentator via LTI | Edlink handles gradebook |

## Why this lesson is the golden reference

Three reasons this lesson is the example every future atom-expansion
should match:

1. **Every part of the playbook is exercised.** Shape B workshop
   model; voice-over default mode; simulation activity type; in-deck
   check for understanding; generator composition across five
   product components.
2. **It's honest about teacher behavior.** The "Your turn" block is
   silent. The teacher walks the room and coaches. The script calls
   that out — the lesson doesn't pretend the teacher is narrating
   every minute.
3. **Students build something real.** The artifact they leave with
   is a working AI model they trained. No pathway is more
   differentiated than ours by the end of class.

Every future lesson doesn't need this exact shape, but it needs this
level of specification. If a teacher can't walk in Monday and run
this from the document, it's not done.
