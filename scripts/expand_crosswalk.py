#!/usr/bin/env python3
"""Append direct atom->TEKS rows to crosswalk.csv.

Used to fill coverage gaps where the uncovered TEKS is a state-only
requirement (career exploration, soft skills, productivity software,
web design basics) that no IBC credential maps to. Each row is still
subject to Maya's review like any ai-draft entry.
"""
import csv
import os

CROSSWALK = "/home/user/CTE/library/credentials/clusters/digital-technology/it-support-services/crosswalks/texas/crosswalk.csv"
FV = "2015 Adopted"

# (atom_id, standard_code, alignment, rationale)
ROWS = [
    # ---- 130.302 Principles of IT ----
    ("work-behaviors-professional-standards", "130.302-c1A", "primary", "Atom explicitly teaches work behaviors, attendance, attire, and initiative"),
    ("work-behaviors-professional-standards", "130.302-c1G", "primary", "Atom covers planning and time-management as part of professional standards"),
    ("professional-communication-it", "130.302-c1B", "primary", "Atom teaches verbal and nonverbal communication in IT contexts"),
    ("professional-communication-it", "130.302-c1C", "primary", "Atom covers effective reading and writing skills for IT professionals"),
    ("professional-communication-it", "130.302-c3B", "primary", "Atom covers email and electronic communication for work"),
    ("critical-thinking-problem-solving", "130.302-c1D", "primary", "Atom directly teaches problem solving and critical thinking"),
    ("critical-thinking-problem-solving", "130.302-c3E", "supporting", "Evaluating information for accuracy is a critical-thinking skill"),
    ("leadership-and-teamwork-it", "130.302-c1E", "primary", "Atom directly teaches leadership and teamwork"),
    ("it-safety-procedures", "130.302-c1F", "primary", "Atom teaches safety procedures in IT work"),
    ("career-exploration-it-pathway", "130.302-c2A", "primary", "Atom surveys IT job opportunities and duties"),
    ("career-exploration-it-pathway", "130.302-c2B", "primary", "Atom covers researching IT careers and required education/skills"),
    ("career-exploration-it-pathway", "130.302-c2C", "primary", "Atom covers resumes and portfolios for IT pathway"),
    ("ai-concepts-in-it", "130.302-c3A", "primary", "Atom describes evolving and emerging technologies"),
    ("web-browser-configuration", "130.302-c3D", "primary", "Atom covers URL components and browser usage"),
    ("malware-detection-and-removal", "130.302-c3F", "primary", "Atom covers viruses, malware, and hacking threats"),
    ("malware-detection-and-removal", "130.302-c5I", "primary", "Atom teaches discovering, quarantining, and removing viruses"),
    ("social-engineering", "130.302-c3F", "supporting", "Social engineering is a category of computer-based threat"),
    ("documentation-and-ticketing-systems", "130.302-c4B", "supporting", "Ticketing knowledge base serves as a reference tool"),
    ("operating-systems-overview", "130.302-c5A", "primary", "Atom differentiates systems software from application software"),
    ("productivity-software-types", "130.302-c5A", "supporting", "Atom categorizes application software types"),
    ("file-management", "130.302-c5C", "primary", "Atom covers file types and their purposes"),
    ("software-licensing", "130.302-c5E", "primary", "Atom contrasts open source and proprietary software licenses"),
    ("word-processing-fundamentals", "130.302-c7A", "primary", "Atom teaches word-processing terminology"),
    ("word-processing-fundamentals", "130.302-c7B", "primary", "Atom covers editing documents with formatting features"),
    ("creating-professional-documents", "130.302-c7C", "primary", "Atom teaches creating professional documents with advanced features"),
    ("spreadsheet-fundamentals", "130.302-c8A", "primary", "Atom teaches spreadsheet terminology"),
    ("spreadsheet-functions", "130.302-c8B", "primary", "Atom covers numerical content and mathematical calculations"),
    ("spreadsheet-functions", "130.302-c8C", "primary", "Atom covers preprogrammed functions for budgets, tables, and ledgers"),
    ("csv-files", "130.302-c8D", "primary", "Atom teaches CSV file generation and function"),
    ("advanced-spreadsheet-features", "130.302-c8E", "primary", "Atom covers lookup tables, nested IF, conditional formatting"),
    ("advanced-spreadsheet-features", "130.302-c8F", "primary", "Atom covers sorting, searching, and filtering"),
    ("programming-language-categories", "130.302-c9B", "primary", "Atom explains operation of compilers vs interpreters"),
    ("presentation-software-fundamentals", "130.302-c11A", "primary", "Atom teaches presentation software terminology and functions"),
    ("creating-presentations", "130.302-c11B", "primary", "Atom covers creating presentations with advanced features"),
    ("web-design-terminology", "130.302-c12A", "primary", "Atom teaches web page development terminology"),
    ("visual-design-elements", "130.302-c12B", "primary", "Atom covers design elements: typeface, color, shape, texture, space, form"),
    ("design-principles", "130.302-c12C", "primary", "Atom covers design principles: unity, harmony, balance, scale, contrast"),
    ("html-fundamentals", "130.302-c12D", "primary", "Atom teaches HTML elements: tags, stylesheets, hyperlinks"),
    ("build-a-web-page", "130.302-c12E", "primary", "Atom guides creating a web page with links, graphics, and design"),
    ("data-value-and-intellectual-property", "130.302-c13D", "primary", "Atom covers consequences of plagiarism as IP violation"),
    ("data-value-and-intellectual-property", "130.302-c13F", "primary", "Atom covers ethical use of online resources and source citation"),

    # ---- 130.303 Computer Maintenance ----
    ("professional-communication-it", "130.303-c1A", "primary", "Atom covers effective reading and writing for IT professionals"),
    ("professional-communication-it", "130.303-c1B", "primary", "Atom covers verbal and nonverbal communication"),
    ("critical-thinking-problem-solving", "130.303-c1C", "primary", "Atom directly teaches problem solving and critical thinking"),
    ("leadership-and-teamwork-it", "130.303-c1D", "primary", "Atom directly teaches leadership and teamwork"),
    ("it-safety-procedures", "130.303-c1E", "primary", "Atom teaches safety procedures in IT work"),
    ("work-behaviors-professional-standards", "130.303-c1G", "primary", "Atom covers planning and project-management skills"),
    ("career-exploration-it-pathway", "130.303-c2A", "primary", "Atom surveys IT job opportunities and duties"),
    ("career-exploration-it-pathway", "130.303-c2B", "primary", "Atom covers certifications, resumes, and portfolios in IT"),
    ("documentation-and-ticketing-systems", "130.303-c3B", "primary", "Atom teaches interpreting documentation: schematics, diagrams, manuals"),
    ("motherboard-and-cpu-installation", "130.303-c4A", "primary", "Atom covers microprocessor architecture and theory"),
    ("binary-number-systems", "130.303-c4B", "primary", "Atom covers Boolean and binary logic in computing"),
    ("internal-components", "130.303-c4E", "primary", "Atom differentiates digital and analog I/O electronics"),
    ("networking-fundamentals", "130.303-c4F", "primary", "Atom covers data-communications theory and relationships"),
    ("networking-fundamentals", "130.303-c8B", "primary", "Atom covers installing and configuring a computer on a network"),
    ("troubleshoot-motherboards-ram-cpus", "130.303-c5E", "primary", "Atom covers interrupt sequences and POST beep codes"),
    ("process-management", "130.303-c5F", "primary", "Atom covers priorities and interrupts at the system level"),
    ("operating-systems-overview", "130.303-c7A", "primary", "Atom covers operational features and terminology of software systems"),
    ("application-installation", "130.303-c7B", "primary", "Atom covers evaluating and installing application software packages"),
    ("troubleshoot-windows", "130.303-c7E", "primary", "Atom covers software troubleshooting techniques"),

    # ---- 130.304 Computer Maintenance Lab ----
    ("work-behaviors-professional-standards", "130.304-c1A", "primary", "Atom covers work behaviors that enhance employability"),
    ("work-behaviors-professional-standards", "130.304-c1B", "primary", "Atom covers positive personal qualities: flexibility, initiative, listening"),
    ("work-behaviors-professional-standards", "130.304-c1G", "primary", "Atom covers planning and time-management skills"),
    ("professional-communication-it", "130.304-c1C", "primary", "Atom covers effective reading and writing for IT professionals"),
    ("professional-communication-it", "130.304-c1D", "primary", "Atom covers verbal and nonverbal communication"),
    ("critical-thinking-problem-solving", "130.304-c1E", "primary", "Atom directly teaches problem solving and critical thinking"),
    ("leadership-and-teamwork-it", "130.304-c1F", "primary", "Atom directly teaches leadership and teamwork"),
    ("it-safety-procedures", "130.304-c1G", "supporting", "Safety procedures reinforce planning considerations"),
    ("data-value-and-intellectual-property", "130.304-c1H", "primary", "Atom covers legal and ethical responsibilities in IT"),
    ("documentation-and-ticketing-systems", "130.304-c2B", "primary", "Atom covers estimating supplies and labor in work orders"),
    ("documentation-and-ticketing-systems", "130.304-c2C", "primary", "Atom covers locating and interpreting technical documentation"),
    ("documentation-and-ticketing-systems", "130.304-c3B", "primary", "Atom covers employing reference documentation and Internet sources"),
    ("ai-concepts-in-it", "130.304-c3D", "primary", "Atom researches new and emerging technologies"),
    ("internal-components", "130.304-c4B", "primary", "Atom describes digital circuits and bus design"),
    ("troubleshoot-motherboards-ram-cpus", "130.304-c6B", "primary", "Atom covers POST beep codes and interrupt sequences"),
    ("process-management", "130.304-c6C", "primary", "Atom covers priorities and interrupts at the system level"),
    ("troubleshoot-windows", "130.304-c6D", "primary", "Atom covers testing a system with diagnostic tools and software"),
    ("troubleshooting-methodology", "130.304-c6F", "primary", "Atom covers differentiating hardware from software failure"),
    ("motherboard-and-cpu-installation", "130.304-c6G", "supporting", "BIOS update is part of motherboard firmware maintenance"),
    ("os-installation", "130.304-c6G", "supporting", "BIOS preparation is part of OS installation prep"),
    ("application-installation", "130.304-c7A", "primary", "Atom covers evaluating and testing software package functionality"),
    ("software-licensing", "130.304-c7B", "primary", "Atom covers verifying software licensing before installation"),
    ("networking-fundamentals", "130.304-c8A", "primary", "Atom covers network connection and interface requirements"),
    ("network-troubleshooting", "130.304-c8C", "primary", "Atom covers verifying and troubleshooting network connectivity"),
]


def main():
    existing = set()
    with open(CROSSWALK) as f:
        reader = csv.reader(f)
        header = next(reader)
        for r in reader:
            if len(r) >= 3:
                existing.add((r[0], r[2]))
    added = 0
    with open(CROSSWALK, "a", newline="") as f:
        w = csv.writer(f)
        for atom, std, align, rat in ROWS:
            key = (atom, std)
            if key in existing:
                continue
            w.writerow([atom, "TX", std, align, rat, "ai-draft", "", "", FV])
            added += 1
    print(f"Added {added} rows ({len(ROWS) - added} already present)")


if __name__ == "__main__":
    main()
