# data-science-ai (georgia) — SME Review

Automated first-pass review of course templates. Surfaces items a human
SME (Maya) should confirm before promoting any template to `status: active`.
Not every finding is a defect — some are intentional design choices that
just need a sign-off.

## How to read the findings

**`prereq appears later`** — Real ordering bug within a course. Fix by
reordering slots.

**`prereq not in course`** — Usually expected cross-course coupling
(prereq supplied by an earlier course in the pathway). Review only when
the listed prereq wouldn't be covered elsewhere in the pathway.

**`skill_type` / `simulation` mismatch** — Confirm intent. Deliberate
overrides are fine; sloppy ones can degrade the lesson.

## 11.44500 — Artificial Intelligence Applications

- Units: **9** — Slots: **39** — Weeks declared: **21**
- **Pacing:** 39 slots, 1755 atom-minutes total, 21 declared weeks (4725 min @ 5×45 min/week). Slack for assessments/reviews: 2970 min (63%).

### Findings to review

- U02 slot 1 `current-ai-research-and-events` requires `what-is-artificial-intelligence` — **prereq not in course**
- U02 slot 2 `non-ml-ai-genetic-algorithms-robotics` requires `ai-domains-ml-nlp-cv` — **prereq not in course**
- U03 slot 1 `ai-cloud-services-overview` requires `ai-domains-ml-nlp-cv` — **prereq not in course**
- U03 slot 2 `open-source-ai-tools` requires `python-external-libraries` — **prereq not in course**
- U03 slot 4 `ides-and-packages-for-ai-dev` requires `python-external-libraries` — **prereq not in course**
- U04 slot 1 `professional-programming-practices` requires `comments-documentation-and-ux` — **prereq not in course**
- U04 slot 3 `researching-an-ai-problem` requires `future-of-work-with-ai` — **prereq not in course**
- U05 slot 1 `balanced-vs-imbalanced-datasets` requires `datasets-and-dataframes` — **prereq not in course**
- U05 slot 2 `train-validation-test-split` requires `datasets-and-dataframes` — **prereq not in course**
- U05 slot 3 `data-cleansing-and-transformation` requires `datasets-and-dataframes` — **prereq not in course**
- U05 slot 4 `evaluating-data-sources` requires `big-data-and-ai` — **prereq not in course**
- U05 slot 5 `pandas-for-data-work` requires `datasets-and-dataframes` — **prereq not in course**
- U05 slot 6 `statistics-for-ai-and-ds` requires `data-analysis-for-decisions` — **prereq not in course**
- U07 slot 3 `programming-a-sensor-driven-robot` requires `python-input-and-decisions` — **prereq not in course**
- U09 slot 2 `statistics-for-ai-and-ds` requires `data-analysis-for-decisions` — **prereq not in course**
- U09 slot 1 `predicting-future-ai-developments` — **duplicate** (first appears U02 slot 3)
- U09 slot 2 `statistics-for-ai-and-ds` — **duplicate** (first appears U05 slot 6)
- U09 slot 3 `productive-collaboration-and-diversity` — **duplicate** (first appears U01 slot 7)
- U06 `Community Problem-Solving with AI` has `summative_quiz: false` — unusual for a CTE unit

## 11.44400 — Artificial Intelligence Concepts

- Units: **10** — Slots: **47** — Weeks declared: **23**
- **Pacing:** 47 slots, 2115 atom-minutes total, 23 declared weeks (5175 min @ 5×45 min/week). Slack for assessments/reviews: 3060 min (59%).

### Findings to review

- U02 slot 1 `current-ai-research-and-events` requires `what-is-artificial-intelligence` — **prereq not in course**
- U03 slot 1 `supervised-unsupervised-reinforcement-learning` requires `ai-domains-ml-nlp-cv` — **prereq not in course**
- U03 slot 2 `teachable-machine-introduction` requires `ai-domains-ml-nlp-cv` — **prereq not in course**
- U03 slot 3 `training-evaluating-ml-models` requires `train-validation-test-split` — **prereq not in course**
- U03 slot 4 `investigating-ai-in-daily-life` requires `ai-in-everyday-life` — **prereq not in course**
- U04 slot 1 `computational-thinking` requires `algorithms-for-ai` — **prereq not in course**
- U05 slot 4 `professional-programming-practices` requires `comments-documentation-and-ux` — **prereq not in course**
- U06 slot 1 `spreadsheets-vs-databases` requires `spreadsheet-fundamentals-for-data` — **prereq not in course**
- U06 slot 4 `ethical-issues-in-data-science` requires `data-cleansing-and-transformation` — **prereq not in course**
- U07 slot 3 `data-visualization-basics` requires `spreadsheet-fundamentals-for-data` — **prereq not in course**
- U07 slot 4 `statistics-for-ai-and-ds` requires `data-analysis-for-decisions` — **prereq not in course**
- U08 slot 1 `ai-bias-privacy-accuracy` requires `how-ai-uses-data-for-predictions` — **prereq not in course**
- U09 slot 1 `design-thinking-process` requires `productive-collaboration-and-diversity` — **prereq not in course**
- U09 slot 2 `researching-an-ai-problem` requires `future-of-work-with-ai` — **prereq not in course**
- U09 `Real-World AI Problem-Solving Capstone` has `summative_quiz: false` — unusual for a CTE unit
- U10 `Portfolio and CTSO` has `summative_quiz: false` — unusual for a CTE unit

## 11.44300 — Foundations of Artificial Intelligence

- Units: **10** — Slots: **51** — Weeks declared: **23**
- **Pacing:** 51 slots, 2295 atom-minutes total, 23 declared weeks (5175 min @ 5×45 min/week). Slack for assessments/reviews: 2880 min (56%).

### Findings to review

- U06 slot 6 `boolean-logic-for-ai` requires `python-operators-and-expressions` — **prereq not in course**
- U09 slot 4 `identify-real-world-ai-problem` requires `researching-an-ai-problem` — **prereq not in course**
- U09 `Design Thinking and Collaboration` has `summative_quiz: false` — unusual for a CTE unit
- U10 `Capstone and CTSO Participation` has `summative_quiz: false` — unusual for a CTE unit

## Cross-course atom sharing

Total atoms used across the templates: **86**.
Atoms shared by 2+ courses: **36**.

- `ai-industry-trends` — in 11.44500, 11.44400, 11.44300
- `career-technical-student-organizations-overview` — in 11.44500, 11.44400, 11.44300
- `creativity-and-innovation-workplace` — in 11.44500, 11.44400, 11.44300
- `critical-thinking-for-career-planning` — in 11.44500, 11.44400, 11.44300
- `ctso-participation-and-competitions` — in 11.44500, 11.44400, 11.44300
- `current-ai-research-and-events` — in 11.44500, 11.44400, 11.44300
- `design-thinking-process` — in 11.44500, 11.44400, 11.44300
- `identify-real-world-ai-problem` — in 11.44500, 11.44400, 11.44300
- `professional-communication-skills` — in 11.44500, 11.44400, 11.44300
- `professional-image-presentation` — in 11.44500, 11.44400, 11.44300
- `teamwork-in-technology-workplace` — in 11.44500, 11.44400, 11.44300
- `work-readiness-and-professional-traits` — in 11.44500, 11.44400, 11.44300
- `ai-bias-privacy-accuracy` — in 11.44400, 11.44300
- `ai-ethics-and-philosophy` — in 11.44400, 11.44300
- `ai-for-good-organizations` — in 11.44400, 11.44300
- `computational-thinking` — in 11.44400, 11.44300
- `data-visualization-basics` — in 11.44400, 11.44300
- `debugging-and-code-tracing` — in 11.44400, 11.44300
- `developer-portfolio-for-ai` — in 11.44500, 11.44400
- `end-to-end-ai-project` — in 11.44500, 11.44400
- `exploring-bias-with-teachable-machine` — in 11.44400, 11.44300
- `investigating-ai-in-daily-life` — in 11.44400, 11.44300
- `legal-and-regulatory-landscape-of-ai` — in 11.44400, 11.44300
- `pandas-for-data-work` — in 11.44500, 11.44400
- `predicting-future-ai-developments` — in 11.44500, 11.44400
- `productive-collaboration-and-diversity` — in 11.44500, 11.44300
- `professional-programming-practices` — in 11.44500, 11.44400
- `programming-paradigms-overview` — in 11.44400, 11.44300
- `python-collections-and-data-organization` — in 11.44400, 11.44300
- `python-control-flow` — in 11.44400, 11.44300
- `python-data-types` — in 11.44400, 11.44300
- `researching-an-ai-problem` — in 11.44500, 11.44400
- `spreadsheet-advanced-features-and-pivots` — in 11.44400, 11.44300
- `statistics-for-ai-and-ds` — in 11.44500, 11.44400
- `supervised-unsupervised-reinforcement-learning` — in 11.44400, 11.44300
- `teachable-machine-introduction` — in 11.44400, 11.44300