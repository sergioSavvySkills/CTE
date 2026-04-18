---
template_id: ga-ai-applications-2025
state: GA
course_name: Artificial Intelligence Applications
course_code: "11.44500"
subcluster: data-science-ai
grade_band: HS
credit_hours: 1
credential_targets:
  - certiport-its-artificial-intelligence
  - ms-ai-900
framework_version: 2021-03-04
status: draft
reviewer:
review_date:
---

# Artificial Intelligence Applications (GA 11.44500)

Third and capstone course in Georgia's AI CTAE pathway. Applies
previously learned skills to build functional, real-world AI
solutions. Covers AI tools ecosystem, Agile/GitHub workflows,
dataset engineering, community-problem-solving projects, and
embedded AI / robotics. Prereqs: Foundations of AI (11.44300) and
AI Concepts (11.44400). Concludes with end-of-pathway assessment.
Each atom is 45 minutes.

Standard 1 (employability) and Standard 8 (CTSO) are threaded across
units per Georgia's guidance that these elements be *integrated
throughout the content of this course.* Because this is the capstone
course, employability atoms cluster toward teamwork (u06) and
professional-image/communication (u08 portfolio pitch), reflecting
how students actually use these skills at the end of the pathway.

```yaml
units:
  - unit_id: u01
    title: "Course Launch and AI Industry Landscape"
    weeks: 1
    slots:
      - slot: 1
        atom_id: current-ai-research-and-events
      - slot: 2
        atom_id: non-ml-ai-genetic-algorithms-robotics
      - slot: 3
        atom_id: career-technical-student-organizations-overview
      - slot: 4
        atom_id: critical-thinking-for-career-planning
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u02
    title: "AI Trends and Future Predictions"
    weeks: 2
    slots:
      - slot: 1
        atom_id: predicting-future-ai-developments
      - slot: 2
        atom_id: ai-industry-trends
      - slot: 3
        atom_id: creativity-and-innovation-workplace
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u03
    title: "AI Tools Ecosystem"
    weeks: 2
    slots:
      - slot: 1
        atom_id: ai-cloud-services-overview
      - slot: 2
        atom_id: open-source-ai-tools
      - slot: 3
        atom_id: proprietary-ai-tools-and-platforms
      - slot: 4
        atom_id: ides-and-packages-for-ai-dev
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: false

  - unit_id: u04
    title: "Agile and GitHub for AI Projects"
    weeks: 2
    slots:
      - slot: 1
        atom_id: professional-programming-practices
      - slot: 2
        atom_id: agile-and-github-for-ai-projects
      - slot: 3
        atom_id: researching-an-ai-problem
      - slot: 4
        atom_id: end-to-end-ai-project
      - slot: 5
        atom_id: work-readiness-and-professional-traits
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u05
    title: "Dataset Engineering for AI"
    weeks: 3
    slots:
      - slot: 1
        atom_id: balanced-vs-imbalanced-datasets
      - slot: 2
        atom_id: train-validation-test-split
      - slot: 3
        atom_id: data-cleansing-and-transformation
      - slot: 4
        atom_id: evaluating-data-sources
      - slot: 5
        atom_id: pandas-for-data-work
      - slot: 6
        atom_id: statistics-for-ai-and-ds
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u06
    title: "Community Problem-Solving with AI"
    weeks: 3
    slots:
      - slot: 1
        atom_id: productive-collaboration-and-diversity
      - slot: 2
        atom_id: design-thinking-process
      - slot: 3
        atom_id: identify-real-world-ai-problem
      - slot: 4
        atom_id: collaborative-ai-solution-design
      - slot: 5
        atom_id: prototyping-ai-solutions
      - slot: 6
        atom_id: teamwork-in-technology-workplace
    unit_generate:
      game: false
      summative_quiz: false
      performance_task: true

  - unit_id: u07
    title: "Embedded AI and Robotics"
    weeks: 3
    slots:
      - slot: 1
        atom_id: embedded-systems-and-sensors
      - slot: 2
        atom_id: building-an-embedded-robot
      - slot: 3
        atom_id: programming-a-sensor-driven-robot
      - slot: 4
        atom_id: debugging-hardware-issues
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u08
    title: "Portfolio and CTSO"
    weeks: 2
    slots:
      - slot: 1
        atom_id: developer-portfolio-for-ai
      - slot: 2
        atom_id: ctso-participation-and-competitions
      - slot: 3
        atom_id: professional-image-presentation
      - slot: 4
        atom_id: professional-communication-skills
    unit_generate:
      game: false
      summative_quiz: true
      performance_task: true

  - unit_id: u09
    title: "End-of-Pathway Assessment Review"
    weeks: 2
    slots:
      - slot: 1
        atom_id: ai-bias-privacy-accuracy
      - slot: 2
        atom_id: ai-ethics-and-philosophy
      - slot: 3
        atom_id: legal-and-regulatory-landscape-of-ai
    unit_generate:
      game: true
      summative_quiz: true
      performance_task: true
```
