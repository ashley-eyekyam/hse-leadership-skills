---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-SCORING: "The CPP is risk-proportionate per CDM 2015 Reg 12(1)–(2): significant-activity risks are scored on the org's risk matrix at control-selection time via the A7 risk_matrix engine (default 5×5), not a separate intake question — the skill defaults the matrix and re-confirms on the activity rows, so a dedicated matrix-size question is not asked up front."
  branches:
    - {when: Q3, option: Notifiable, activates_output_section: notification-status-f10, mandatory: true}
    - {when: Q5, option: No, activates_output_section: assumptions-gap, mandatory: true}
    - {when: Q6, option: UK, activates_kb_row: KB-REG-CDM2015, activates_output_section: cdm-reg12-basis, mandatory: false}
    - {when: Q6, option: USA, activates_kb_row: KB-REG-OSHA1926, activates_output_section: osha-1926-basis, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: bocw-state-gap, mandatory: true}
---

# Structured intake — construction-phase-plan

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**.

**The GATE (refuse-on-vague):** no Construction Phase Plan is produced until all three of
**a named project (Q1)**, **≥1 significant activity (Q4)**, and **the contractor
configuration (Q2)** are captured. The skill **refuses a generic "a building site"** — ask
again, or record `[ASSUMPTION]` / `[GAP]`; never invent.

**Two jurisdiction paths:** the **UK → CDM 2015 branch** (Q6 = UK → `KB-REG-CDM2015` + the
Reg 12 basis; non-mandatory) and the **mandatory India → state branch** (Q6 = India → Q6a +
`KB-REG-IN-STATEFORMS`, **defers to `hse-india` / `bocw-compliance`, mandatory state
detection, literal `[GAP]`, never a minted national form number**). The **notifiability
branch** (Q3 = notifiable → the F10 / Reg 12 notification-status section is mandatory) and
the **PCI branch** (Q5 = no PCI → the Reg 4 gap is flagged `[GAP]` and the assumptions
section is mandatory) tune the plan.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named project (scope + programme)** | free-text | "Which project — name it, its scope, and its programme/duration (e.g. 'Tower B fit-out: demolish level-3 partitions, then erect steel frame + cladding to levels 3–5, wk 8–20')?" — **specificity anchor; refuse 'a building site'.** Also **disambiguates the CDM document**: this skill owns the **Construction Phase Plan**; a request for the Pre-Construction Information or the Health & Safety File is routed to its CDM-chain sibling. | ELI-SUBJECT / ELI-SCOPE | always |
| Q2 | **Contractor configuration** | MCQ | Principal contractor (multi-contractor) / **Sole contractor** / Sub-contractor / Not yet appointed — **a sole contractor still owns the CPP under Reg 12(2)** | ELI-SCOPE | always |
| Q3 | **Notifiability** | MCQ | Non-notifiable / Notifiable / Unsure — Notifiable = >30 working days **with** >20 workers simultaneously, **or** >500 person-days; **Notifiable → the plan must state the F10 / Reg 12 notification duty** | ELI-OBLIGATIONS | always |
| Q4 | **Significant / high-risk activities (Schedule 3)** | MCQ multi-select + free-text | Work at height / Excavation & ground works / Demolition / Lifting operations / Confined spaces / Work near water or services / Hot works / Other (+ detail) — **≥1 required for the GATE**; drives the significant-risks-&-controls-by-activity section | ELI-SUBJECT / ELI-EXPOSURE | always |
| Q5 | **Pre-Construction Information (PCI) available?** | MCQ | Yes / No — Yes = paste / reference it (pulled in to inform the plan); **No → the Reg 4 gap is flagged `[GAP]` and the plan proceeds on stated assumptions**. **PCI is an OPTIONAL input; the CPP never assumes a sibling produced it** (D-06 loose coupling) | ELI-EVIDENCE / ELI-BASELINE | always |
| Q6 | **Jurisdiction** | MCQ | UK / USA / India / EU / Unknown — UK → CDM 2015 (Reg 12 + L153); USA → 29 CFR 1926 Subpart C; India → Q6a + BOCW; Unknown → ask before citing | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india` / `bocw-compliance`; confirm the state before citing any form; emit a literal `[GAP]`, never a minted national form number** | ELI-JURIS | Q6 == India |
| Q7 | **Existing controls / arrangements already in place** | free-text | "What site-wide arrangements already exist (site induction, traffic-management plan, edge protection, welfare, an emergency plan)?" | ELI-BASELINE | always |
| Q8 | **Duty-holders & competence** | free-text | "Who are the named duty-holders for this project (principal contractor, CDM construction manager, site manager) and their competencies? **Name them for the CPP record.**" — never invent an appointment (record `[GAP]`) | ELI-COMPETENCY | always |
| Q9 | **Programme & review trigger** | free-text | "Construction-phase start/finish dates, and when this CPP must be reviewed/updated (Reg 12(3)–(4): on change of method, sequence, or significant activity)?" | ELI-TEMPORAL | always |

*ELI-INDUSTRY thin-covered (always construction; Q1/Q4 detail). ELI-LOCATION covered by the named project/site in Q1. ELI-EXPOSURE covered by the significant activities in Q4.*

**Branch map:** `notifiable` (Q3 = notifiable → the **mandatory** F10 / Reg 12
notification-status section); `no-pci` (Q5 = No → the Reg 4 gap is flagged `[GAP]` and the
**mandatory** assumptions section); `uk-cdm` (Q6 = UK → `KB-REG-CDM2015` + the Reg 12 basis;
non-mandatory); `us-osha` (Q6 = USA → `KB-REG-OSHA1926`; non-mandatory); `india-bocw`
(Q6 = India → Q6a + `KB-REG-IN-STATEFORMS`, **mandatory** state detection, defers to
`hse-india`).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
any analysis: "CPP for the Tower B fit-out (demolish level-3 partitions → erect steel frame
+ cladding levels 3–5), principal contractor, **notifiable** (F10 due), significant
activities = demolition + work at height + lifting, **PCI supplied**, UK / CDM 2015,
duty-holders named, construction phase wk 8–20 / review on method change — correct?" The
risk for each significant activity is scored on the org's matrix at control-selection time.

## Refuse-on-vague anchors

- **The GATE:** Q1 (named project), Q4 (≥1 significant activity), and Q2 (contractor
  configuration) are load-bearing — **refuse a generic "a building site"**; never invent a
  project, an activity, or a duty-holder appointment (record `[GAP]`).
- Q5 = No (no PCI) is **not** a refusal — the Reg 4 gap is flagged `[GAP]` and the plan
  proceeds on **stated assumptions** (PCI is optional; the CPP never assumes a sibling ran).

## Domain evidence types (ELI-EVIDENCE)

Pre-Construction Information (Reg 4) · existing site arrangements / traffic-management plan ·
prior RAMS for the significant activities · the project programme / phasing · the
duty-holder appointments and competencies per Q8 · the F10 notification (if filed).
