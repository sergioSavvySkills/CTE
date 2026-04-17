#!/usr/bin/env python3
"""Generate Batch 1: Foundation atoms (6 files)"""
import os

BASE = "/home/user/CTE/library/atoms/it-support-services"
os.makedirs(BASE, exist_ok=True)

atoms = {
"binary-number-systems": {
    "title": "Binary and Hexadecimal Number Systems",
    "creds": ["comptia-itf-plus::1.1", "google-it-support::c1m1"],
    "skill_type": "knowledge", "mins": 60, "diff": 2,
    "prereqs": [],
    "obj": "Students will be able to convert numbers between binary, decimal, and hexadecimal, and explain why computers use binary at the hardware level.",
    "content": [
        ("Why binary?", "transistors as on/off switches; bits, nibbles, bytes; voltage levels representing 0 and 1"),
        ("Binary counting", "place values (2⁰ through 2⁷), counting sequences, reading an 8-bit byte"),
        ("Binary ↔ decimal conversion", "positional method for binary-to-decimal; repeated division for decimal-to-binary"),
        ("Hexadecimal", "base-16 digits 0–9 and A–F; hex as a shorthand for four bits; converting hex ↔ binary ↔ decimal"),
        ("Practical uses", "MAC addresses, IPv6, color codes (#RRGGBB), memory addresses, error codes"),
        ("Unsigned vs. signed integers", "two's complement overview; range of 8-bit unsigned (0–255) vs. signed (−128 to +127)"),
    ],
    "assess": [
        "Conversion worksheet: convert 10 values across binary, decimal, and hex (timed)",
        "Error-code decode: given a hex error code from a real OS event log, identify what each byte represents",
        "Exit ticket: explain in one sentence why a technician needs to read hex",
    ],
},
"fundamental-data-types": {
    "title": "Fundamental Data Types in Computing",
    "creds": ["comptia-itf-plus::1.2"],
    "skill_type": "knowledge", "mins": 45, "diff": 1,
    "prereqs": ["binary-number-systems"],
    "obj": "Students will be able to identify and describe the fundamental data types used in computing and explain how each is stored and sized.",
    "content": [
        ("Integer types", "whole numbers; 8/16/32/64-bit widths; signed vs. unsigned; overflow"),
        ("Floating-point", "representing decimals; single vs. double precision; why floating-point arithmetic is approximate"),
        ("Characters and strings", "ASCII (7-bit, 128 characters), extended ASCII, Unicode (UTF-8/UTF-16); how text is encoded as bytes"),
        ("Boolean", "true/false values; 1-bit logical data; use in conditions and flags"),
        ("Binary large objects (BLOBs)", "images, audio, video stored as raw byte sequences; file formats as structured binary"),
        ("Data type size implications", "storage cost, memory alignment, network bandwidth; choosing the right type for the job"),
    ],
    "assess": [
        "Matching exercise: pair each data type with a real-world example (e.g., pixel color → integer, employee name → string)",
        "Short answer: why does a programmer choose float over int for a temperature sensor reading?",
        "Mini-lab: use a hex editor or Python to inspect the raw bytes of a small text file and identify the ASCII values",
    ],
},
"input-processing-output-storage": {
    "title": "Input-Processing-Output-Storage Computing Model",
    "creds": ["comptia-itf-plus::1.3"],
    "skill_type": "knowledge", "mins": 45, "diff": 1,
    "prereqs": [],
    "obj": "Students will be able to describe the IPO+S model, classify computer components by function, and trace how data flows through a system from input to stored output.",
    "content": [
        ("The IPO+S model", "Input → Process → Output + Storage; origin in systems thinking; applies to any information system"),
        ("Input devices", "keyboard, mouse, touchscreen, microphone, scanner, camera, sensors; digitizing analog signals"),
        ("Processing", "CPU as the processor; ALU, control unit, registers; clock speed and cores; RAM as working memory"),
        ("Output devices", "monitor, printer, speaker, projector; rendering processed data for human use"),
        ("Storage", "primary (RAM — volatile) vs. secondary (HDD/SSD — non-volatile); hierarchy: registers → cache → RAM → disk → cloud"),
        ("Data flow example", "tracing a keystroke: keyboard → CPU decodes scancode → rendered on display → saved to file on disk"),
    ],
    "assess": [
        "Component sort: given a list of 20 hardware items, classify each as Input / Processing / Output / Storage",
        "Data-flow diagram: draw the path a voice command takes from microphone to smart-speaker audio output",
        "Short answer: why does the storage tier need to be non-volatile?",
    ],
},
"data-value-and-intellectual-property": {
    "title": "Value of Data and Intellectual Property",
    "creds": ["comptia-itf-plus::1.4"],
    "skill_type": "knowledge", "mins": 45, "diff": 1,
    "prereqs": [],
    "obj": "Students will be able to explain why data has economic and personal value, identify categories of intellectual property, and describe the legal and ethical obligations IT workers have to protect both.",
    "content": [
        ("Why data has value", "business intelligence, personalization, monetization; data as an asset on a balance sheet; the data economy"),
        ("Personal data and privacy", "PII (personally identifiable information) and PHI; FERPA, HIPAA, COPPA overview; breach consequences"),
        ("Intellectual property categories", "copyright, trademark, patent, trade secret; what each protects and for how long"),
        ("Software licensing as IP", "proprietary vs. open-source; EULA terms; software piracy as IP theft"),
        ("IT worker obligations", "acceptable-use policies, NDAs, data classification (public/internal/confidential/restricted)"),
        ("Consequences of violations", "civil liability, criminal charges, reputational damage; real-world breach case studies"),
    ],
    "assess": [
        "Case study analysis: read a 1-page data-breach summary; identify what PII was exposed and what law likely applies",
        "License sort: classify five software tools by license type and explain what a user may or may not do",
        "Scenario reflection: an IT tech finds a coworker copying company source code to a personal drive — what should they do and why?",
    ],
},
"computing-units-of-measure": {
    "title": "Units of Measure in Computing",
    "creds": ["comptia-itf-plus::1.5"],
    "skill_type": "knowledge", "mins": 45, "diff": 1,
    "prereqs": ["binary-number-systems"],
    "obj": "Students will be able to correctly interpret and convert between computing units of measure for storage capacity, data-transfer speed, and processing speed.",
    "content": [
        ("Storage units", "bit → byte → KB → MB → GB → TB → PB; binary (KiB/MiB) vs. decimal (KB/MB) definitions; why drive sizes appear smaller in the OS"),
        ("Data-transfer speed", "bits per second (bps); Kbps, Mbps, Gbps; difference between storage (bytes) and transfer (bits)"),
        ("Processing speed", "Hz, MHz, GHz for CPU clock; operations per second; IOPS for storage"),
        ("Memory bandwidth", "MHz/MT/s for RAM; relationship between speed, width, and throughput"),
        ("Practical conversions", "reading a spec sheet: '500 MB/s NVMe SSD', '2.4 GHz Wi-Fi', '32 GB RAM'; calculating download times"),
        ("Common gotchas", "storage marketing math (1 TB drive = 931 GiB in OS); ISP speed caps in Mbps vs. MB/s file speeds"),
    ],
    "assess": [
        "Spec-sheet interpretation: given three hardware spec sheets, identify each unit and convert to a common unit for comparison",
        "Download-time calculation: given file size in GB and connection speed in Mbps, calculate transfer time",
        "Short answer: a drive is advertised as '1 TB'; why does the OS show ~931 GB?",
    ],
},
"troubleshooting-methodology": {
    "title": "IT Troubleshooting Methodology",
    "creds": ["comptia-itf-plus::1.6", "google-it-support::c1m6"],
    "skill_type": "both", "mins": 60, "diff": 2,
    "prereqs": [],
    "obj": "Students will be able to apply a structured six-step troubleshooting methodology to diagnose and resolve IT problems, documenting each step clearly.",
    "content": [
        ("The six-step model", "1 Identify the problem, 2 Establish a theory, 3 Test the theory, 4 Establish an action plan, 5 Implement and verify, 6 Document; CompTIA A+ alignment"),
        ("Step 1 — Identify", "gathering user information; open-ended vs. closed questions; reproducing the issue; checking for recent changes"),
        ("Steps 2–3 — Theory and test", "top-down vs. bottom-up approaches; least-disruptive test first; divide-and-conquer method"),
        ("Steps 4–5 — Plan and implement", "communicating the plan to the user; change control considerations; escalation triggers"),
        ("Step 6 — Document", "what was done, what worked, time spent; updating the knowledgebase; closing the ticket"),
        ("Real-world application", "applying the model to a 'no internet' scenario and a 'computer won't boot' scenario step by step"),
    ],
    "assess": [
        "Scenario walkthrough: given a 'printer not printing' ticket, write out all six steps you would take",
        "Role-play: one student plays the end user, one plays the technician; observer scores adherence to the methodology",
        "Documentation task: after resolving a practice scenario, write a complete ticket closure note",
    ],
},
}

TEMPLATE = '''---
atom_id: {atom_id}
title: {title}
subcluster: it-support-services
credential_objectives:{cred_block}
skill_type: {skill_type}
grade_band: HS
estimated_minutes: {mins}
difficulty: {diff}
prerequisites:{prereq_block}
status: draft
reviewer:
review_date:
---

## Learning objective

{obj}

## Content stub

{content_block}

## Assessment stub

{assess_block}
'''

def fmt_creds(creds):
    if not creds:
        return " []"
    return "\n" + "\n".join(f"  - {c}" for c in creds)

def fmt_prereqs(prereqs):
    if not prereqs:
        return " []"
    return "\n" + "\n".join(f"  - {p}" for p in prereqs)

def fmt_content(content):
    lines = []
    for heading, body in content:
        lines.append(f"- **{heading}:** {body}")
    return "\n".join(lines)

def fmt_assess(assess):
    return "\n".join(f"- {a}" for a in assess)

count = 0
for atom_id, data in atoms.items():
    path = os.path.join(BASE, f"{atom_id}.md")
    if os.path.exists(path):
        print(f"SKIP (exists): {atom_id}")
        continue
    content = TEMPLATE.format(
        atom_id=atom_id,
        title=data["title"],
        cred_block=fmt_creds(data["creds"]),
        skill_type=data["skill_type"],
        mins=data["mins"],
        diff=data["diff"],
        prereq_block=fmt_prereqs(data["prereqs"]),
        obj=data["obj"],
        content_block=fmt_content(data["content"]),
        assess_block=fmt_assess(data["assess"]),
    )
    with open(path, "w") as f:
        f.write(content)
    print(f"WROTE: {atom_id}")
    count += 1

print(f"\nDone — {count} files written")
