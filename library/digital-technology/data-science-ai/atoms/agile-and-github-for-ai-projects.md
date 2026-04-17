---
atom_id: agile-and-github-for-ai-projects
title: Agile Development and GitHub for AI Projects
subcluster: data-science-ai
credential_objectives:
  - certiport-its-artificial-intelligence::4.1
skill_type: both
grade_band: HS
estimated_minutes: 45
difficulty: 3
prerequisites:
  - professional-programming-practices
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to describe Agile/Scrum basics, and use Git and GitHub to version-control an AI project.

## Content stub

- **Agile principles:** iterative, customer-focused, responds to change; short cycles (sprints) deliver working software
- **Scrum basics:** sprint planning, daily standup, sprint review, retrospective; roles: PO, Scrum Master, dev team
- **Git fundamentals:** commit (save snapshot), branch (parallel work), merge (combine); local history
- **GitHub:** hosts your repo; pull requests for reviews; issues for tasks; Actions for CI
- **Team workflow:** feature branch → push → open PR → review + CI → merge; never develop on main
- **AI project specifics:** .gitignore for data/ and models/; Git LFS for large files; reproducibility via requirements.txt

## Assessment stub

- Lab: create a GitHub repo, add a README, commit 3 changes, open a pull request to yourself
- Apply Agile: break a simple AI project into 3 sprints with deliverables
- Short answer: why don't you commit the trained model file to Git directly?
