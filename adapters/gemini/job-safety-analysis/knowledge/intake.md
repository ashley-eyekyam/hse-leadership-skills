---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}
  branches:
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
    - {when: Q5, activates_questions: [Q5b], mandatory: false}
---

# Structured intake — job-safety-analysis

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
**two load-bearing free-text questions are the job/task (Q3) and its ordered step
sequence (Q4) — the spine**. **Refuse to proceed on a vague job or an empty/one-line
step list** — ask the user to break the job into its actual sequence of steps, or record
`[ASSUMPTION]` / `[GAP]`; **never invent a step**. A JSA with no steps is not a JSA.

Two branches: the **mandatory India→state branch** (Q1 = India → Q1a +
`KB-REG-IN-STATEFORMS`; confirm the state before citing any form) and the **SDS-evidence
branch** (when Q5 names a hazardous substance → Q5b; non-mandatory).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown (India → Q1a) | ELI-JURIS | always |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any form** | ELI-JURIS | Q1 == India |
| Q2 | Industry / sector | MCQ + free-text | Manufacturing / Oil & Gas / Construction / Mining / Other physical-work sector (+ detail) | ELI-INDUSTRY | always |
| Q3 | **The job/task being analysed** | free-text | "Name the exact job/task — e.g. 'clean and inspect storage tank T-402, Plant 3'." — **specificity anchor (a); refuse a vague answer** | ELI-SUBJECT | always |
| Q4 | **The job's steps, in the order performed** | free-text | "List the steps in sequence — e.g. '1. isolate & lockout · 2. purge/ventilate · 3. gas-test · 4. enter · 5. clean · 6. exit & restore'. One step per line." — **specificity anchor (b), THE SPINE; each step becomes a JSA row; refuse an empty/one-line list — ask the user to decompose** | ELI-SUBJECT | always |
| Q5 | Tools / equipment / materials used | free-text | "What tools, plant, equipment, or materials does this job use (e.g. cherry-picker, angle grinder, solvent, scaffold)?" (introduces equipment/substance hazards into the relevant steps) | ELI-BASELINE | always |
| Q5b | **SDS / data you hold** | free-text | "For any hazardous substance in Q5, do you have its SDS? Any prior incident/near-miss on this job?" | ELI-EVIDENCE | Q5 names a substance |
| Q6 | Who performs the job, and their competencies | MCQ multi-select + free-text | Own workers / Contractors / Specialist-licensed trade / Mixed crew (+ required competencies/permits — confined-space entry permit, hot-work permit) | ELI-COMPETENCY | always |
| Q7 | Environment / conditions | MCQ multi-select + free-text | Working at height / Confined space / Hot-cold-outdoor / Live plant nearby / Public-traffic nearby / Restricted access / Other — flags permit-to-work triggers | ELI-EXPOSURE | always |
| Q7b | **Permits-to-work required** | MCQ multi-select | None / Hot work / Confined space / Working at height / Electrical isolation / Excavation / Other — formalises the Q7 triggers | ELI-OBLIGATIONS | always |
| Q8 | Location / site | free-text | "Which specific site/area/asset?" | ELI-LOCATION | always |
| Q9 | Likelihood band (org scale) | MCQ | 1 Rare / 2 Unlikely / 3 Possible / 4 Likely / 5 Almost certain | ELI-SCORING | always |
| Q10 | Severity band (org scale) | MCQ | 1 Negligible / 2 Minor / 3 Moderate / 4 Major / 5 Catastrophic | ELI-SCORING | always |
| Q11 | Org risk-matrix size | MCQ | 3×3 / 4×4 / **5×5 (default)** / Supply our matrix | ELI-SCORING | always |
| Q12 | **Review trigger** | MCQ + free-text | Per shift/job / On change / Periodic (+interval) — when this JSA is re-validated | ELI-TEMPORAL | always |

*ELI-SCOPE and ELI-OUTPUT are thin-cover-by-fixed-format (a JSA is always a per-step
register — no audience/format branch), recorded as covered, not omitted.*

**Branch map:** `india-state` (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`; **mandatory**);
`sds-evidence` (Q5 names a hazardous substance → Q5b; non-mandatory).

## Echo-back

After Q12, **echo a captured-facts summary** and confirm before any analysis:
"Analysing: clean & inspect tank T-402, Plant 3, Maharashtra, 6 steps (isolate → purge →
gas-test → enter → clean → exit), own workers + confined-space-permitted contractors,
cherry-picker + solvent, confined-space + hot-work permits, 5×5 matrix, re-validate per
job — correct?" Q9/Q10 establish the org scale; each step's hazard is scored
individually at the per-step scoring step.

## Refuse-on-vague anchors

- Q4 (ordered steps) is the load-bearing anchor — refuse an empty/one-line step list; a
  JSA with no steps is not a JSA. Record `[GAP]` for an unconfirmed step; never invent.
- Q3 is the job specificity anchor — refuse a vague job ("general maintenance").

## Domain evidence types (ELI-EVIDENCE)

SDS for materials in Q5 · prior JSA/RA for the job · prior incidents on this
job/equipment · competency cards/permits held (CSCS, confined-space, hot-work).
