---
atom_id: applied-math-and-data-in-health-science
atom_serial: HHS-PH-0001
sidecar: examples
status: ai-draft
example_count: 4
author: claude
reviewer:
review_date:
---

# Worked examples — applied-math-and-data-in-health-science

## Example 1 — A pediatric weight-based dose

**Scenario:** A 3-year-old weighs 44 pounds. The physician orders
amoxicillin at 25 mg/kg per dose. What dose do you draw?

**Step-by-step:**

1. Convert pounds to kilograms: 44 ÷ 2.2 = **20 kg**.
2. Multiply kg by the mg/kg: 20 × 25 = **500 mg**.
3. Sanity-check against a reference range: amoxicillin for children is
   commonly 25–50 mg/kg/dose; 500 mg is within range for a 20 kg child
   [OpenStax-PharmMath].

**Answer:** 500 mg per dose.

**Why it matters:** Skipping step 1 and treating 44 as the weight in
kg would produce 44 × 25 = 1100 mg — a 2.2× overdose. The conversion
is where safety lives [AAP-PediDose].

## Example 2 — Spotting a decimal error

**Scenario:** A handwritten order reads "digoxin .25 mg PO daily." The
pharmacy clarifies to you that it should be "digoxin 0.25 mg." What's
the rule, and why does it matter?

**Step-by-step:**

1. A value less than 1 must always be written with a leading zero:
   **0.25**, not .25.
2. Without the leading zero, a reader under time pressure can miss the
   decimal and interpret ".25" as "25" — a 100× overdose.
3. The matching rule: a whole number is written without a trailing
   zero. **1 mg**, not 1.0 mg, because 1.0 can be misread as 10
   [ISMP-Decimal, TJC-DoNotUse].

**Answer:** The order should be transcribed as 0.25 mg (leading zero
added). No trailing zero was present, which is already correct.

**Why it matters:** Both rules come from real-world medication errors
that killed patients. The Joint Commission and ISMP maintain the
do-not-use list specifically because handwriting and decimal habits
cause deaths.

## Example 3 — Reading a glucose trend

**Scenario:** A patient's fingerstick glucose readings over four days:
day 1 = 110 mg/dL, day 2 = 135, day 3 = 160, day 4 = 185. Their
fasting reference range is 70–99 mg/dL. What does the trend tell you?

**Step-by-step:**

1. Day 1 value alone is slightly above **reference range** but
   unremarkable.
2. Each subsequent day rises by ~25 mg/dL. The direction — the **trend**
   — is monotonic upward.
3. Day 4 is approaching the range that requires intervention (≥ 200
   mg/dL fasting is diabetic territory) [AHA-Vital-Signs].

**Answer:** Even though no single reading is yet in the "danger" range,
the trend is the signal. This patient needs provider notification
before day 5 confirms the pattern.

**Why it matters:** A clinician reading only the day-4 number might
not escalate; a clinician reading the trend will. Always read a
series, not a single data point.

## Example 4 — Interpreting a growth-chart percentile

**Scenario:** A 2-year-old girl weighs 22 pounds. The growth chart
shows her at the 25th **percentile** today, down from the 75th
percentile at her 12-month visit and the 50th percentile at her
18-month visit. Should the clinic be concerned?

**Step-by-step:**

1. Percentile tells you where a child sits in the reference population —
   25th percentile means she is heavier than 25 percent of 2-year-old
   girls and lighter than 75 percent [CDC-GrowthCharts].
2. What matters is not the absolute percentile but whether the child
   is staying on a consistent curve.
3. This child has fallen from 75th to 50th to 25th across three
   visits. That is a crossing of two percentile curves — a flag for
   faltering growth.

**Answer:** Yes, the clinic should be concerned. The absolute weight
looks fine; the trajectory does not.

**Why it matters:** Reading one number off a growth chart tells you
very little. Reading the pattern across visits is the whole point of
the chart. The same logic applies to blood pressure, weight, and lab
values across the lifespan.
