---
atom_id: process-management
title: Process Management and System Resources
subcluster: it-support-services
credential_objectives:
  - google-it-support::c3m5
skill_type: skill
grade_band: HS
estimated_minutes: 45
difficulty: 2
prerequisites:
  - operating-systems-overview
  - windows-features-and-tools
status: draft
reviewer:
review_date:
---

## Learning objective

Students will be able to view and manage running processes, identify resource-hungry tasks, and take corrective action when a system is unresponsive.

## Content stub

- **Processes vs. threads:** a process is an isolated program instance; threads share a process's memory; context switching
- **Windows tools:** Task Manager (Processes/Details tabs), Resource Monitor, tasklist/taskkill commands
- **Linux tools:** ps aux, top, htop, kill/killall, nice/renice; process states (R/S/Z)
- **Memory management:** RAM usage, virtual memory/page file, commit charge; what happens when RAM is exhausted
- **CPU and disk bottlenecks:** identifying high CPU vs. high I/O wait; which resource is the actual bottleneck
- **Startup and scheduled tasks:** msconfig startup, Task Scheduler, cron jobs; disabling unnecessary startup items

## Assessment stub

- Lab: use Task Manager and Resource Monitor to identify the process causing high CPU during a simulated load
- Kill task: find and terminate a hung process using both GUI and CLI methods
- Short answer: what is a zombie process and why does it indicate a programming bug?
