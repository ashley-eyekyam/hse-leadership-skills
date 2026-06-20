---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL, ELI-OBLIGATIONS]
  omits:
    ELI-EXPOSURE: "program-level, not task-level; receptors not elicited"
    ELI-LOCATION: "program-level; the facility name carries the location"
  branches:
    - {when: Q2, option: No (not a PSM-covered process), activates_output_section: framework-not-statutory-note}
    - {when: Q5, activates_output_section: overdue-elements}
    - {when: Q8, option: USA (29 CFR 1910.119 statutory), activates_kb_row: us-osha}
    - {when: Q8, option: India, activates_questions: [Q8a], mandatory: true, activates_kb_row: in-factories-act}
---

# Structured intake — psm-program-manager

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse to mark an element compliant with no evidence** (record `[GAP]`, never assert).
Canonical runtime pattern: `KB-SNIP-INTAKE`.

This is the **program backbone**: a 14-element PSM (29 CFR 1910.119) status assessment.
Status must be **evidence-based**, never asserted — an element with no supporting evidence
is `[GAP]`, never "compliant"; "overdue" status needs a **cycle-date** basis (triennial
compliance audit, 5-yearly PHA revalidation).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What's the **task**? | MCQ | Build the 14-element status matrix · Gap assessment (where are our gaps) · Audit-readiness prep · Track a specific element | ELI-SCOPE | always |
| Q2 | Name the **facility** and **covered process(es)** — is it a **PSM-covered process** (threshold quantity of a highly hazardous chemical)? | MCQ + free-text | Yes (PSM-covered) / No (not a PSM-covered process) / Help-determine — name the facility + process; the specificity anchor; refuse a vague "our plant" | ELI-SUBJECT | always |
| Q3 | Which **elements** are in scope? | MCQ multi-select | All 14 · Employee participation · PSI · PHA · Operating procedures · Training · Contractors · PSSR · Mechanical integrity · Hot work · MOC · Incident investigation · Emergency planning · Compliance audits · Trade secrets | ELI-OBLIGATIONS | always |
| Q4 | For each in-scope element, what **evidence exists** (documents, audit findings, dates)? | free-text | status must be evidence-based, not asserted; no evidence → `[GAP]` | ELI-EVIDENCE | always |
| Q5 | What **cycle dates** drive "overdue" — last compliance audit, last PHA / revalidation? | free-text | PSM triennial audit, 5-yr PHA revalidation → overdue status | ELI-TEMPORAL | always |
| Q6 | Who **owns** each element? | free-text | the matrix carries owners up front (de-identified to roles) | ELI-COMPETENCY | always |
| Q7 | What is the **current programme baseline** — which elements already have a documented, maintained system? | free-text | seeds the compliant-vs-gap starting state | ELI-BASELINE | always |
| Q8 | **Jurisdiction** (statutory hook)? | MCQ | USA (29 CFR 1910.119 statutory) / UK / EU / India / PSM-as-framework | ELI-JURIS | always |
| Q8a | *(India only)* Which **state** is the facility in (for the Factories-Act statutory hook)? | MCQ + free-text | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — confirm the state before citing any state-specific obligation; never silently assume | ELI-JURIS | Q8 == India |
| Q9 | Which **risk matrix** bands the gap-risk? | MCQ | Our matrix · Default 5×5 | ELI-SCORING | always |
| Q10 | What **output**, for whom, how widely shared, and which **sector**? | MCQ + free-text | Status matrix · Gap report · Audit-prep pack // M / C // internal vs circulated // sector (chemicals · O&G · refining · other) | ELI-OUTPUT | always |
| Q11 | Which **sector** frames the covered process? | MCQ | Chemicals · Oil & Gas · Refining · Petrochemicals · Other | ELI-INDUSTRY | always |

**Branch map:** Q2 = No (not PSM-covered) → framework-not-statutory-note (PSM-as-best-practice, not statutory). Q5 cycle date overdue → element status auto-flags **overdue**; overdue-elements section. Element with no evidence (Q4) → status `[GAP]`, never asserted "compliant". Q8 = USA → `us-osha` (1910.119) + the PSM standard; Q8 = India → **mandatory state branch** (Q8a) + `in-factories-act` (+ MSIHC framework note) — confirm the state before citing any state-specific obligation.

## Echo-back

Echo the captured facts back and ask the user to confirm before building the matrix:
"Facility **{facility}**, covered process **{process}** (PSM-covered: **{Y/N}**), elements
**{scope}**, cycle dates **{audit/PHA}**, owners **{owners}**, matrix **{matrix}**. An
element with no evidence is `[GAP]`, never 'compliant'. Correct before I build the matrix?"

## Refuse-on-vague anchors

- Q2 is the specificity anchor: refuse a vague "our plant" with no named facility/covered
  process; never proceed without it.
- Refuse to mark an element compliant with no evidence → record `[GAP]`; "are we
  compliant?" with no element scope or evidence is refused until both are supplied.
