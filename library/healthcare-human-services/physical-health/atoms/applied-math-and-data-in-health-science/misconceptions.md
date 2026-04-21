---
atom_id: applied-math-and-data-in-health-science
atom_serial: HHS-PH-0001
sidecar: misconceptions
status: ai-draft
misconception_count: 4
author: claude
reviewer:
review_date:
---

# Common misconceptions — applied-math-and-data-in-health-science

## Misconception 1 — A calculator prevents errors

**What students often think:**
If I use a calculator, the math will be right, so my dose will be right.

**What's actually true:**
Calculators multiply what they're given. They don't know whether the
number you typed was in pounds or kilograms, whether you meant 1.0 or
10, or whether you shifted a decimal when you copied the order. Every
well-known medication-error story involves arithmetic a calculator
computed correctly — from the wrong inputs [ISMP-Decimal].

**How to check:**
Ask: *"A student doubles a dose because they entered 10 when the label
said 1.0. Whose fault is the error?"* A student with the correct model
will say it's the human who typed the number, not the calculator, and
will name leading-zero / trailing-zero discipline as the fix.

## Misconception 2 — Pounds and kilograms are roughly the same

**What students often think:**
Pounds and kilograms both measure weight, so the number doesn't matter
much as long as it's close.

**What's actually true:**
1 kg ≈ 2.2 lb. A 44-pound child (20 kg) is less than half the weight of
a 110-pound child (50 kg). For **weight-based dosing**, dosing a
44-pound child as if they were 44 kg would be a 2.2× overdose — enough
to hospitalize them on many drugs [AAP-PediDose, OpenStax-PharmMath].
Pounds and kilograms are not interchangeable; conversion is mandatory.

**How to check:**
Ask: *"A child weighs 22 pounds. The order is 10 mg/kg. What dose do
you draw?"* A student with the correct model first converts (22 lb ÷
2.2 = 10 kg), then multiplies (100 mg). A student who skips the
conversion gets 220 mg — a 2.2× overdose.

## Misconception 3 — Read the number off the chart

**What students often think:**
The chart shows a number. I write down the number.

**What's actually true:**
Numbers on charts mean something only in context. A lab value means
normal or abnormal relative to a **reference range**. A glucose reading
means stable or deteriorating relative to its **trend**. A pediatric
weight means on-track or concerning relative to the child's previous
**percentile**. Reading the number without the context is the same as
not reading the chart [CDC-GrowthCharts, AHA-Vital-Signs].

**How to check:**
Ask: *"A patient's blood glucose is 145 mg/dL. Is that a problem?"* A
student with the correct model asks "fasting or post-meal?" and
"what's the trend across the last week?" A student without the model
tries to answer yes or no from 145 alone.

## Misconception 4 — If it's on the pharmacy label, it must be right

**What students often think:**
The pharmacy is the checkpoint. By the time a drug reaches me, someone
else has already verified the dose.

**What's actually true:**
Medication errors happen at every stage — prescribing, transcribing,
dispensing, administering. The bedside check is the last line of
defense, and national safety systems treat it that way. Every
administering clinician recalculates the dose themselves and checks
that it matches the order, the weight, and the drug reference range
[ISMP-Decimal, AAP-PediDose]. The right assumption is that any number
you didn't verify yourself is suspect.

**How to check:**
Ask: *"Under what circumstances would you skip double-checking a
weight-based dose the pharmacy computed?"* A student with the correct
model answers "never." A student without the model offers reasons like
"if the patient is stable" or "if the pharmacist is experienced."
