---
atom_id: common-medical-abbreviations
atom_serial: HHS-PH-0005
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — common-medical-abbreviations

Two reasoning examples (decode and audit) and two procedural examples
(rewrite and look up) — the skill_type for this atom is *both*, so the
mix is deliberate. Each example targets the atom's two LO parts:
reading shorthand correctly and avoiding do-not-use forms.

## Example 1 — Decoding a routine order

**Scenario:** A medication order reads
*Amoxicillin 500 mg PO tid x 7 days, stat first dose.*

**What to work out:** Translate the order into plain English, naming
every abbreviation and the category it belongs to.

**Step-by-step:**

1. *500 mg* is the dose. No decimal problems — no leading or trailing
   zeros to police.
2. *PO* is the **route**: by mouth (per os).
3. *tid* is the **frequency**: three times a day.
4. *x 7 days* is duration: for seven days.
5. *stat first dose* is a **timing** instruction: the first dose is
   given immediately, not at the next scheduled mealtime.

**Answer:** *Give 500 mg of amoxicillin by mouth three times a day for
seven days; give the first dose right now.*

**Why it matters:** Every piece of a chart order — dose, route,
frequency, duration, special timing — fits into a small number of
categories. Naming the category is the first step in reading orders
safely [ISMP-ErrorProne].

## Example 2 — Auditing an order sheet for do-not-use violations

**Scenario:** A printed order sheet from a busy floor contains the
following lines:

- *Insulin regular 4U subQ ac*
- *Furosemide 40 mg PO QD*
- *Warfarin .5 mg PO hs*
- *Morphine 2 mg IV q4h prn pain, MSO4 only*
- *Acetaminophen 650 mg PO q6h prn T > 38.0, NKDA*

**What to work out:** Identify every **do-not-use list** violation and
rewrite each line safely.

**Step-by-step:**

1. Line 1: *4U* uses a banned *U* for *unit*. Rewrite as *4 units*
   [TJC-DoNotUse].
2. Line 2: *QD* is banned (confusable with *QOD* and with *QID*).
   Rewrite as *daily*.
3. Line 3: *.5 mg* is missing its leading zero. Rewrite as *0.5 mg*.
   This is a **decimal discipline** fix [FDA-SafeDose].
4. Line 4: *MSO4* is banned (ambiguous with *MgSO4*; *MS* itself is
   banned). Rewrite the drug name as *morphine sulfate* or just
   *morphine*.
5. Line 5: no violations. *NKDA* (no known drug allergies) and the
   temperature threshold *T > 38.0* are acceptable shorthand. Note that
   *38.0* here is a temperature reading, not a dose — the trailing-
   zero rule applies to dose expressions, not to measurements on a
   thermometer.

**Answer:** Four of the five lines need rewriting. Corrected forms:
*4 units subQ ac* / *40 mg PO daily* / *0.5 mg PO hs* / *Morphine
sulfate 2 mg IV q4h prn pain*.

**Why it matters:** Four distinct harm patterns — unit-as-zero, QD/QID
confusion, missing leading zero, MS/MgSO4 swap — each have caused real
patient events [TJC-DoNotUse, AHRQ-Errors]. Catching them in the chart
before the dose is given is exactly what auditing shorthand is for.

## Example 3 — Rewriting a risky order safely

**Scenario:** A physician hands you a handwritten slip reading
*MgSO4 1.0 g IM QOD, hold if BP < 100/60.*

**What to work out:** Rewrite the order so that nothing on it appears
on the do-not-use list.

**Step-by-step:**

1. *MgSO4* is banned — it is easily misread as *MSO4* (morphine
   sulfate). Spell out *magnesium sulfate* [TJC-DoNotUse].
2. *1.0 g* has a trailing zero; the decimal can be missed and the dose
   read as *10 g*. Rewrite as *1 g*.
3. *QOD* is banned — easily confused with *QD* or *QID*. Rewrite as
   *every other day*.
4. *IM* (intramuscular), *BP* (blood pressure), and the numeric
   threshold are all acceptable shorthand and stay.
5. Re-read the whole order aloud to confirm the meaning hasn't changed.

**Answer:** *Magnesium sulfate 1 g IM every other day; hold if BP <
100/60.*

**Why it matters:** Rewriting, not just flagging, is the skill. In
real settings you will sometimes be the person who types the verbal or
handwritten order into the electronic record, and the record must not
contain banned forms. A drug-name swap between *morphine* and
*magnesium* is a high-alert error category because both can cause
serious harm at wrong doses [ISMP-HighAlert].

## Example 4 — Checking a facility's approved abbreviation list

**Scenario:** It is your first day at a new clinic. You are about to
chart *patient ambulated x 50 ft, SOB resolved, discharged home*. You
paused because you are not sure whether *SOB* is acceptable here.

**What to work out:** Decide whether to use *SOB* and carry out the
check the right way.

**Step-by-step:**

1. Recognize that *SOB* (shortness of breath) is a category-of-status
   abbreviation — no dose risk, but it is still bound by facility rules.
2. Locate the clinic's **approved abbreviation list**. It lives in the
   policy binder at the charge nurse's station, or in the electronic
   medical record's help menu [TJC-NPSG].
3. Search the list. Suppose *SOB* is not on the approved list at this
   clinic, even though it was approved at your last site.
4. Rewrite the note to say *shortness of breath resolved* instead.
5. Raise it at the next team huddle — if the list omits a term the
   clinic actually uses, the omission should be fixed, not worked
   around silently.

**Answer:** *Patient ambulated 50 ft; shortness of breath resolved;
discharged home.*

**Why it matters:** The habit this atom is teaching is not
memorization — it is *recognize, look up, avoid the banned forms*. The
look-up step is the one students most often skip, and it is the one
that transfers cleanly between sites, rotations, and jobs
[ISMP-ErrorProne].
