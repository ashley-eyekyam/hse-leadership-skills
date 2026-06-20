---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}
  branches:
    - {when: Q1, option: UK, activates_kb_row: KB-REG-UK-HSWA, activates_output_section: cdm-duty-basis, mandatory: false}
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: bocw-form-xxv, mandatory: true}
    - {when: Q6, activates_output_section: reg13-or-reg15-citation, mandatory: false}
---

# Structured intake — rams-builder

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
**two specificity anchors** are **Q2 (the construction activity)** and **Q-S (the
sequence of works)** — the Workflow **refuses to proceed** on a vague activity or an
unsequenced method; ask again, or record `[ASSUMPTION]` / `[GAP]`; never invent.

Two jurisdiction paths: the **UK→CDM branch** (Q1 = UK → `KB-REG-UK-HSWA` +
cdm-duty-basis; non-mandatory) and the **mandatory India→state/BOCW branch** (Q1 = India
→ Q1a + `KB-REG-IN-STATEFORMS` + bocw-form-xxv; confirm the state before citing any
form — BOCW legacy-first, never a national form number). The **role-duty branch**
(Q6 selected → the Reg 13 / Reg 15 citation) tunes the CDM duty cited.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Jurisdiction | MCQ | UK / India / USA / EU / Other / Unknown — UK → CDM 2015 (Reg 13) duty path; India → Q1a + BOCW | ELI-JURIS | always |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any form** | ELI-JURIS | Q1 == India |
| Q2 | **The construction activity / works being assessed** | free-text | "Describe the exact works and the structure/element (e.g. 'erect a mobile tower to replace cladding panels on the south elevation, levels 2–4')." — **specificity anchor #1; refuse a vague answer** | ELI-SUBJECT | always |
| Q3 | Site & environment | free-text | "Which specific site/area? What's around it — occupied building, public footpath, live traffic, other trades, overhead/buried services, ground conditions, weather exposure?" | ELI-LOCATION / ELI-EXPOSURE | always |
| Q-S | **Sequence of works (the ordered steps, start to finish)** | free-text | "List the work steps in order, set-up to clear-down (e.g. 'mobilise & set exclusion zone → inspect & erect tower → transfer materials → remove old panels → fit new panels → inspect → dismantle → clear site')." — **specificity anchor #2; refuse an unsequenced answer** | ELI-SUBJECT | always |
| Q-P | Plant & equipment | MCQ multi-select + free-text | Access (scaffold/tower/MEWP/ladder) / Lifting (crane/telehandler/hoist) / Excavation (excavator/breaker) / Power tools / Welding-hot-work kit / Other (+ detail) | ELI-BASELINE | always |
| Q-C | Personnel & competencies / cards | free-text | "Who does each step, and what competency/cards do they hold (CSCS, CPCS, IPAF, PASMA, appointed-person for lifts)? **Name the competent persons for the sign-off record.**" — **never invent a card the user did not state** (record `[GAP]`) | ELI-COMPETENCY | always |
| Q-W | Permits-to-work required | MCQ multi-select | None / Hot work / Excavation-ground disturbance / Confined space / Working at height-suspended access / Lifting operations / Electrical isolation / Other | ELI-OBLIGATIONS | always |
| Q4 | Existing controls already in place | free-text | "What site-wide or activity controls already exist (site induction, traffic-management plan, edge protection, the Construction Phase Plan)?" | ELI-BASELINE | always |
| Q4b | **CPP / prior RAMS / SDS to ingest** | free-text | "Do you have a Construction Phase Plan, prior RAMS, or SDS for substances in the works to reference (by id)? (or 'none')" | ELI-EVIDENCE | always |
| Q5 | Org risk-matrix size | MCQ | 3×3 / 4×4 / **5×5 (default)** / Supply our matrix | ELI-SCORING | always |
| Q6 | **CDM / contractor role** *(asked for UK; offered elsewhere)* | MCQ | Principal contractor / Contractor-sub / Principal designer / Client / Not applicable — tunes the CDM 2015 duty cited (Reg 13 PC / Reg 15 contractor) + the CPP linkage; for India maps to the BOCW principal-employer/contractor duty | ELI-OBLIGATIONS / ELI-SCOPE | always |
| Q7 | **Works window / RAMS validity** | free-text | "Programme dates for these works, and when this RAMS must be re-briefed/revised (on change of method/sequence)?" | ELI-TEMPORAL | always |

*ELI-INDUSTRY thin-covered (always construction; Q2 detail).*

**Branch map:** `uk-cdm` (Q1 = UK → `KB-REG-UK-HSWA` + cdm-duty-basis; non-mandatory);
`india-bocw` (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS` + bocw-form-xxv; **mandatory**);
`role-duty` (Q6 selected → Reg 13 / Reg 15 citation).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
any analysis: "RAMS for erecting a mobile tower to replace south-elevation cladding
(levels 2–4), occupied building + public footpath, 8-step sequence, tower + MEWP, PASMA +
IPAF operatives, working-at-height permit, UK / principal contractor, 5×5 matrix, works
window wk 12–14 / re-brief on method change — correct?" Likelihood/severity bands are
applied **per-hazard** at scoring time on the org's matrix.

## Refuse-on-vague anchors

- Q2 (activity) and Q-S (sequence) are load-bearing — refuse a vague activity or an
  unsequenced method; never invent a step or a competency card (record `[GAP]`).

## Domain evidence types (ELI-EVIDENCE)

Construction Phase Plan (Reg 12) · prior RAMS for similar works · competency cards/tickets
per Q-C · SDS for substances · lift plan / appointed-person details · ground-investigation
/ services drawings for excavation.
