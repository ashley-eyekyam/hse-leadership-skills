---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "N/A — this skill prequalifies a contractor before appointment; there are no existing on-site controls to baseline. The contractor's current HSE arrangements are captured as evidence under ELI-EVIDENCE (Q3), not as a site baseline."
  branches:
    - {when: Q1, option: High-hazard, activates_questions: [Q1b], activates_kb_row: KB-DATA-CONTRACTOR-TIERS, activates_output_section: high-hazard-pqq-module, mandatory: true}
    - {when: Q4, option: India, activates_questions: [Q4a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — contractor-prequalification

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the answers;
**echo the captured facts back for confirmation before any analysis**. The intake opens with
the **scope & risk tier (Q1)** — the specificity anchor that sets the PQQ depth and the pass
threshold — then captures the contractor, the evidence set, the jurisdiction, and the decision
type. **Refuse to score** until the scope+risk tier and at least the **core evidence set**
(insurance + accident/enforcement history + relevant competence) are captured; **never score
a self-asserted claim** — missing evidence becomes a `[GAP]`.

Two load-bearing branches: the **risk-tier branch** (Q1 = High-hazard → the T3 high-hazard
PQQ module from `KB-SNIP-PQQ-BANK` + the higher pass threshold from `KB-DATA-CONTRACTOR-TIERS`;
**mandatory** when high-hazard work is in scope) and the **mandatory India→state branch**
(Q4 = India → Q4a + `KB-REG-IN-STATEFORMS`; confirm the state before citing any form — never
a national form number).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Scope of work & its risk** (then free-text the actual work package) | MCQ + free-text | Low-admin / Medium / High-hazard | ELI-SCOPE | always |
| Q1b | *(High-hazard only)* Which high-hazard activities? | MCQ multi-select | Hot work / Confined space / Work at height / Lifting / Energised electrical / Demolition / Other | ELI-SCOPE | Q1 == High-hazard |
| Q2 | **The named contractor + work package** | free-text | "Name the contractor/subcontractor and the specific work package and site/asset they would perform (e.g. 'Acme Scaffolding — erect/dismantle access scaffold for the Plant 3 turnaround')." — **the subject anchor; refuse a vague 'a contractor'** | ELI-SUBJECT | always |
| Q2b | Site / location of the work | free-text | "Which specific site/area/asset will the work be performed on?" | ELI-LOCATION | always |
| Q2c | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / Utilities / General-Other (+ detail) — selects sector hazards + which statutory regime applies (e.g. CDM where construction) | ELI-INDUSTRY | always |
| Q2d | Who will be exposed to / affected by the contractor's work? | MCQ multi-select | Own workers / Other contractors on site / Public-visitors / Nearby community | ELI-EXPOSURE | always |
| Q3 | **Evidence available** | MCQ multi-select + free-text | Insurance certificates / Accreditations (SSIP / ISO 45001) / Accident & enforcement history / Method statements / RAMS / Competence records / References — **plus free-text for each: is the actual evidence supplied, or only asserted?** **Missing or asserted-only evidence becomes a `[GAP]`; never scored as met.** | ELI-EVIDENCE | always |
| Q3b | **Obligations the contractor must satisfy** | free-text | "Any standards/accreditations your procurement requires (SSIP, ISO 45001), permits the work needs (PTW / hot-work / confined-space), or client HSE rules they must sign up to?" | ELI-OBLIGATIONS | always |
| Q4 | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown (India → Q4a; UK + construction → CDM reg. 8; USA → OSHA multi-employer policy) | ELI-JURIS | always |
| Q4a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any form** | ELI-JURIS | Q4 == India |
| Q5 | **Decision type + output** | MCQ | New approval / Re-approval (existing contractor) / Project-specific — produces the risk-tiered PQQ + evidence-based scorecard + approve/conditional/reject recommendation | ELI-OUTPUT | always |
| Q5b | Pass-threshold / scoring scheme | MCQ | **Tier-default thresholds (KB-DATA-CONTRACTOR-TIERS, default)** / Supply our own contractor-approval scoring scheme | ELI-SCORING | always |
| Q5c | **Decision owner + review cadence** | free-text + MCQ | "Who owns the approval decision and the conditions (named role)?" + review cadence: On expiry of evidence / Annual / Per-project / Other (+date) — feeds the conditions' owners and the review date | ELI-COMPETENCY, ELI-TEMPORAL | always |

**Q1 band definitions:** *Low-admin* = office, cleaning, light maintenance (→ T1, Core PQQ);
*Medium* = general trades, M&E, plant on a managed site (→ T2, Core + task-specific PQQ);
*High-hazard* = hot work, confined space, work at height, lifting, energised electrical,
demolition (→ T3, full PQQ + high-hazard module + the higher pass threshold). The tier is set
by the **highest-risk activity** in the scope, not the average.

**Branch map:** `risk-tier` (Q1 = High-hazard → Q1b + the T3 high-hazard PQQ module +
`KB-DATA-CONTRACTOR-TIERS` T3 threshold; **mandatory**); `india-state` (Q4 = India → Q4a +
`KB-REG-IN-STATEFORMS`; **mandatory**).

## Echo-back

After the last applicable question (Q5c, and Q1b if the high-hazard branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Prequalifying: Acme Scaffolding for the work-at-height scaffold package, Plant 3,
Maharashtra, construction, **risk tier T3 (high-hazard)** — evidence held: insurance ✓,
SSIP certificate ✓, accident history ✓, height-competence certs *asserted only → [GAP]*;
new approval, tier-default thresholds, decision owner = Procurement Lead, review on certificate
expiry — correct?" The tier and the evidence-verification status drive the scorecard; no score
rests on an asserted-only claim.

## Refuse-on-vague anchors

- Q1 is the **specificity anchor** — refuse a vague scope ("approve this contractor"); the
  risk tier (and therefore the PQQ depth and pass threshold) cannot be set without the actual
  work package. Ask again or record `[GAP]`, never assume a low tier.
- **Never score a self-asserted claim as met** — an accreditation or competence asserted in
  Q3 without the supplied certificate/record is a `[GAP]` and blocks an unconditional pass;
  high-hazard (T3) work cannot pass on PPE/competence claims alone.
- Refuse to produce a recommendation until at least the **core evidence set** (insurance +
  accident/enforcement history + relevant competence) is captured.

## Domain evidence types (ELI-EVIDENCE)

Current employers'/public-liability insurance certificate · signed HSE policy · recognised
accreditation certificate (SSIP / ISO 45001) — the certificate, not a claim · method
statements / RAMS for the scope · accident & enforcement history (rates + any notices,
**de-identify named injured persons before scoring**) · competence/training records for the
trade · activity-specific certification for any high-hazard activity (in date) · safe-system-of-work
/ permit procedure · sub-contractor-management arrangements · references.
