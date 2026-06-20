---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "SOP-writer uses `controls` only and ingests already-rated controls from B1/B2 (Q4); it never re-scores risk."
    ELI-EXPOSURE: "At-risk population is defined in the upstream RA/JSA; the SOP names executing roles (Q9), not bystanders."
  branches:
    - {when: Q4, option: have JSA, activates_output_section: ingested-hazards, mandatory: false}
    - {when: Q4, option: have RA, activates_output_section: ingested-hazards, mandatory: false}
    - {when: Q4, option: Neither, activates_questions: [Q6, Q7], activates_output_section: inline-hazard-flag, mandatory: false}
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
    - {when: Q11, activates_output_section: assumption-review-on-change, mandatory: false}
---

# Structured intake — sop-writer

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, branch
on the answers; **echo the captured facts back before authoring**. The two **specificity
anchors** are the **task/operation (Q3)** and the **procedure steps (Q8)**: **refuse to
proceed on a vague task or generic/missing steps** — ask again, or record `[GAP]` /
`[ASSUMPTION]`; never invent. Q4 is the **ingest gate** (ingest a B1 RA / B2 JSA vs elicit
hazards inline).

Branches: the **ingest branches** (Q4 = have JSA / have RA → the ingested-hazards section,
do NOT re-score; Q4 = Neither → elicit Q6/Q7 inline + flag a formal RA/JSA is more
rigorous); the **mandatory India→state branch** (Q1 = India → Q1a +
`KB-REG-IN-STATEFORMS`; confirm the state before citing any duty); and the **no-review
branch** (Q11 blank → record "review on change or at minimum annually" as `[ASSUMPTION]`).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown (India → Q1a) | ELI-JURIS | always |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any duty** | ELI-JURIS | Q1 == India |
| Q2 | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q3 | **The task/operation this SOP covers, and its boundaries** | free-text | "Describe the exact task or operation, and what is explicitly in/out of scope." — **specificity anchor (a); refuse a vague answer** | ELI-SUBJECT | always |
| Q4 | **Hazard/control source** — the **ingest gate** (JSA/RA → ingest its hazards + rated controls, do NOT re-score; Neither → elicit inline via Q6/Q7 + flag a formal RA/JSA is more rigorous) | MCQ | have JSA / have RA / Neither | ELI-SCOPE | always |
| Q5 | Location / asset | free-text | "Which specific site/area/equipment/asset does this procedure apply to?" | ELI-LOCATION | always |
| Q6 | Hazards present in this task | free-text | "What hazards arise during this task? (energy sources, substances, environment, human factors)" — asked when Q4 = Neither; pre-filled from the ingested RA/JSA otherwise | ELI-BASELINE | Q4 == Neither |
| Q7 | Existing / required controls & PPE/permits | free-text | "What controls, PPE, and permits already apply or are required?" — seeds the control set + names the higher-order controls the procedure sits within | ELI-OBLIGATIONS | always |
| Q7b | **Standards / limits this procedure must satisfy** | free-text | "Any exposure limits, codes, or org standards this procedure must meet beyond the ingested controls? (optional)" | ELI-OBLIGATIONS | always (optional) |
| Q8 | **The procedure steps, in order** | free-text | "List the actual steps to perform the task, in order." — **specificity anchor (b); refuse generic/missing steps** | ELI-SUBJECT | always |
| Q9 | Roles & competencies | MCQ multi-select + free-text | Operator-technician / Supervisor / Authorised person (PTW) / Competent person (named role) / Other (+ free-text) — who executes/authorises/verifies (role labels); the competencies/training each role needs | ELI-COMPETENCY | always |
| Q10 | Target literacy level / language register | MCQ | Frontline operator (plain, short imperatives) / Technician / Supervisor-technical / Bilingual note (India) — **literacy calibration (KB-SNIP-AUDIENCE)** | ELI-OUTPUT | always |
| Q11 | Review cycle / revision control | MCQ + free-text | Annual / 2-yearly / On change (MoC-triggered) / Other (+ free-text) — feeds the revision/approval block | ELI-TEMPORAL | always |
| Q12 | Output document type | MCQ | Full SOP / Short work instruction (single task) / Procedure within a larger manual — scopes breadth + triage | ELI-OUTPUT | always |

**Branch map:** `ingest-jsa`/`ingest-ra` (Q4 = have JSA / have RA → ingested-hazards
section; non-mandatory); `elicit-inline` (Q4 = Neither → Q6, Q7 + inline-hazard-flag);
`india-state` (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`; **mandatory**); `no-review`
(Q11 blank → `[ASSUMPTION]` review-on-change).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
authoring: "Authoring: SOP for manual print-head changeover on Press 4, Plant 2,
Maharashtra; hazards/controls ingested from JSA-2026-A14; 9 ordered steps; roles =
operator + authorised PTW person; frontline literacy; annual + on-change review —
correct?" If Q4 = Neither, the echo-back flags that a formal RA/JSA is the more rigorous
hazard source and that hazards were elicited inline. If the user gives no review cycle
(Q11), record "review on change (MoC-triggered) or at minimum annually" and flag it
`[ASSUMPTION]`.

## Refuse-on-vague anchors

- Q3 (task/boundaries) and Q8 (steps) — refuse generic steps ("work safely", "follow all
  rules"); never invent.

## Domain evidence types (ELI-EVIDENCE)

Ingested B1 RA or B2 JSA (Q4, by id) · existing manual the procedure slots into (Q12) ·
competency/training matrix for Q9 roles · SDS where the procedure handles substances.

*This skill has the cleanest omit-reasons in the family (ELI-SCORING, ELI-EXPOSURE both
genuinely upstream) — the model for a defensible omit.*
