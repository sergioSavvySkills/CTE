---
atom_id: applied-math-and-data-in-health-science
atom_serial: HHS-PH-0001
sidecar: book
status: ai-draft
word_count: 1507
author: claude
reviewer:
review_date:
---

# Applied Math and Data in Health Science

## Why this matters

A nurse gives a child a dose of medication. A med-tech reads a chart with
ten rows of lab values. An EMT eyeballs a glucose trend on a monitor and
decides whether to treat. None of these are complex math problems —
they're reading numbers, converting units, and checking whether a value
makes sense. But they happen under time pressure, at two in the morning,
on a patient the worker has never met before. That is where ordinary
arithmetic becomes a safety skill [ISMP-Decimal].

This atom covers the math a healthcare worker actually does on a shift:
**unit conversion** between patient-reported numbers and the metric
values the chart demands, reading tables and charts fast enough to act
on them, and the decimal discipline that prevents a slipped key from
becoming a ten-fold overdose.

## What you should already know

Basic arithmetic — add, subtract, multiply, divide, work with decimals
and fractions. Nothing past middle-school math. What this atom adds is
the specific domain: which numbers belong in which units, which charts
you'll see on the floor, and which errors matter most.

## Core concept

### Two measurement systems, one standard

Two measurement systems show up every shift. The **metric system**
(International System of Units, or SI) uses grams, liters, meters, and
degrees Celsius [NIH-Metric]. The **US customary system** uses pounds,
ounces, inches, feet, and degrees Fahrenheit — the language patients
grew up speaking. Hospitals and pharmacies standardize on metric
because it's the dosing language of every medication label, every
laboratory reference, and every clinical guideline [AAP-PediDose].

The consequence: patients will tell you a number in US customary, and
you will write it into the chart in metric. Every time. Conversion is
a one-way ramp from patient language into clinical language. The most
common conversions are:

- **Pounds to kilograms** — divide pounds by 2.2. A 154-pound adult
  weighs 70 **kilograms**. A 44-pound child weighs 20 kg.
- **Ounces to milliliters** — 1 fluid ounce ≈ 30 mL; 1 teaspoon = 5 mL;
  1 tablespoon = 15 mL.
- **Fahrenheit to Celsius** — subtract 32, then divide by 1.8. A
  temperature of 98.6 °F is 37 °C. 100.4 °F is 38 °C.
- **Inches to centimeters** — multiply inches by 2.54.

The arithmetic is easy. What's hard is remembering to do the conversion
every single time, and to do it in the right direction.

### Weight-based dosing — why this matters in pediatrics

An adult's dose for a common antibiotic might be a fixed 500 mg. A
child's dose is often written as "20 mg/kg" — twenty milligrams of
drug per kilogram of body weight [OpenStax-PharmMath]. This is
**weight-based dosing**, and it is the standard for children because a
three-year-old is biologically different enough from an adult that a
one-size dose would either under-treat or poison them [AAP-PediDose].

The workflow is always: (1) get the patient's weight in **pounds** if
that's what's reported, (2) convert to **kilograms**, (3) multiply by
the prescribed milligrams per kilogram, (4) check that the total
**dose** is within a safe range. The conversion is where the errors
happen. Double-check it.

Weight-based dosing also appears in adult medicine — chemotherapy,
anticoagulants, critical-care drips — any situation where the drug has
a narrow margin between therapeutic and toxic. The general rule:
whenever a prescriber writes a dose as a ratio rather than a fixed
number, the conversion from whatever weight the patient reported into
kilograms is part of the order. Institutions that chart patient weight
only in kilograms (now the national standard for pediatric care) avoid
the whole class of errors that come from mixing the two systems
[AAP-PediDose].

### Tables and charts — reading what's already in the chart

Most of the "math" in healthcare is actually chart-reading. The chart
already has the numbers; the skill is spotting which number matters.

A **reference range** tells you what counts as normal for a test. A
fasting blood glucose between 70 and 99 mg/dL is normal; above 126 is
diabetic range. The value itself is meaningless until you know the
range [AHA-Vital-Signs]. When you see a lab report, look at the value
AND the flag (low / high / normal) together.

A **trend** tells you where a value is heading. Three glucose readings
of 140, 160, 180 across three days are individually fine but together
signal a problem. Never read one value in isolation if you can see its
history.

A **growth chart** plots pediatric measurements — weight, height, head
circumference — against age, with curves drawn at the 5th, 10th, 25th,
50th, 75th, 90th, and 95th **percentile** of the reference population
[CDC-GrowthCharts]. A child at the 90th percentile is heavier than
90 percent of peers the same age. What matters is not which curve a
child is on, but whether they are staying on the same curve visit
after visit. Falling off a curve is a flag; climbing a curve may also
be one.

One last chart type worth a mention: the body-mass-index (BMI) chart,
which relates weight to height-squared. A BMI value on its own is
meaningless — it has to be read against the adult BMI categories
(under 18.5, 18.5–24.9, 25–29.9, 30+) or, for children and teens,
against a BMI-for-age percentile curve [CDC-GrowthCharts]. Same
pattern as every other chart in this section: the number alone is
not the story; the number plus its context is.

### The common error sources

Four errors account for most of the mistakes trainees make:

1. **Mixing units.** Doing the math in pounds when the formula wants
   kilograms, or using milligrams when the order was milliliters. Always
   write the unit next to every number on your scratch work.
2. **Decimal misplacement.** "1.0" misread as "10" is a ten-fold
   overdose. "0.5" written as ".5" gets misread as "5." This is why
   **decimal discipline** is a national patient-safety rule: always
   write a leading zero (0.5, not .5), never write a trailing zero
   (1, not 1.0) [ISMP-Decimal].
3. **Misreading chart axes.** A graph of blood pressure looks dramatic
   or benign depending on the scale. Always read the Y-axis labels
   before reacting to a curve's shape.
4. **Trusting a chart's scale without checking.** Percentile lines on
   a growth chart are non-linear; lab reference ranges differ by
   patient age and sex. The chart tells you a story only if you
   understand its conventions.

Each of these errors is preventable by one habit: slow down for one
extra breath before you act on a number [ISMP-Decimal].

### Why a "medication error" is the shape that matters

"**Medication error**" is the term national safety organizations use
for any preventable mistake in prescribing, transcribing, dispensing,
or administering a drug [ISMP-Decimal]. The four error sources named
above are the arithmetic side of that definition. There are also
non-arithmetic medication errors — wrong drug, wrong patient, wrong
time, wrong route — but a healthcare worker who never touches the drug
cabinet still owns the arithmetic errors. Decimal discipline, unit
discipline, and the habit of verifying every number one more time are
the arithmetic line of defense.

The reason to learn the *name* "medication error" is that you will see
it in policy documents, incident reports, in-service training, and the
reports the hospital files with state regulators after a harm event.
Recognizing the phrase tells you that a document or a conversation is
about preventable harm specifically, not clinical outcomes in general
[ISMP-Decimal, TJC-DoNotUse].

## Worked through an example

A two-year-old weighs 22 pounds. The physician orders an antibiotic at
15 mg/kg per dose. What dose do you draw up?

1. Convert: 22 lb ÷ 2.2 = 10 kg.
2. Multiply: 10 kg × 15 mg/kg = 150 mg.
3. Sanity-check: the reference for this drug says 5–20 mg/kg/dose; 150
   mg is within range for a 10 kg child.

Three lines of arithmetic, but each line has an opportunity to go
wrong. See `examples.md` for this case plus three others (a decimal
error spot-check, a glucose trend reading, and a growth-chart
interpretation).

## Common confusions

A calculator does not prevent a **unit conversion** error. Charts lie
when axes are read carelessly. Pounds and kilograms are not
interchangeable, even for one patient. Full corrections and diagnostic
probes live in `misconceptions.md`.

## How this connects to other topics

Every other atom in the sub-cluster uses the math from this one. *Vital
signs overview* turns numbers into clinical decisions using the
reference-range habit taught here. *Common medical abbreviations*
shares the decimal-discipline rule from the do-not-use list. Any
pharmacology content deepens weight-based dosing into mechanism, but
the arithmetic here is the floor everyone builds on [ISMP-Decimal].

## Key terms to remember

Five anchor terms: **unit conversion**, **weight-based dosing**,
**reference range**, **percentile**, and **decimal discipline**. The
remaining eight terms in `vocabulary.csv` fill in the between-the-
systems vocabulary and the specific chart types you'll meet.

## Further reading

Citations resolve to `sources.md`. The ISMP and Joint Commission pages
on error-prone dose designations are worth bookmarking — they're the
authoritative sources for which abbreviations and decimal forms to
avoid on real orders [ISMP-Decimal, TJC-DoNotUse].
