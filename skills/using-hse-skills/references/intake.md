---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE]
  omits:
    ELI-LOCATION:    "Deferred to the chosen skill — physical-environment hazards are artifact-specific."
    ELI-BASELINE:    "Deferred to the chosen skill — existing-controls baseline is per-assessment."
    ELI-EVIDENCE:    "Deferred to the chosen skill — source data depends on the artifact."
    ELI-OBLIGATIONS: "Deferred to the chosen skill — statutory obligations are artifact/jurisdiction-specific."
    ELI-SCORING:     "Deferred to the chosen skill — matrix config is per-risk-assessment."
    ELI-COMPETENCY:  "Deferred to the chosen skill — named reviewer roles are per-deliverable."
    ELI-TEMPORAL:    "Deferred to the chosen skill — review cadence is per-artifact."
  branches:
    - {when: Q-JUR, option: India, activates_questions: [Q-JUR-STATE], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — using-hse-skills (catalog router)

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**,
MCQ where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any recommendation**.
This router elicits only the **shared, carry-over facts** every downstream skill reuses
(the 3 universal facets + jurisdiction/industry/exposed-population) so the user enters
them **once**; each deep, per-artifact facet (scoring, baseline, evidence, obligations,
competency, temporal, location) is **deferred to the chosen skill's own intake** — no
double-intake. **Refuse to proceed on a vague task (Q-SUBJECT is the specificity anchor)**
— ask again, or record `[ASSUMPTION]` / `[GAP]`; never invent.

One load-bearing branch: the **mandatory India→state branch** (Q-JUR = India → Q-JUR-STATE
+ `KB-REG-IN-STATEFORMS`; confirm the state before routing to any India form-bearing skill —
never a national form number).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q-INTENT | **The HSE outcome / artifact you need** | free-text | "What HSE outcome or artifact do you need? (e.g. 'make a re-roofing job safe', 'I'm onboarding a new contractor', 'an overview of what HSE I need for this site')." — captures intent + scope so the router can match the catalog | ELI-SCOPE | always |
| Q-SUBJECT | **The named task / site / asset (the specificity anchor)** | free-text | "Name the specific task, activity, site, or asset — broken into steps where it helps (e.g. 'strip-and-re-roof Block C at [SITE], working at height from the eaves')." — **the specificity anchor; refuse a vague subject** | ELI-SUBJECT | always |
| Q-OUTPUT | **Deliverable, reader, and what 'done' looks like** | free-text | "What deliverable(s) do you need, who reads them, and what does 'done' look like? (e.g. 'a permit + a toolbox talk the night-shift crew can sign today')." — the success-criteria overlay | ELI-OUTPUT | always |
| Q-JUR | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown (India → Q-JUR-STATE) | ELI-JURIS | always |
| Q-JUR-STATE | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm the state before routing to any India form-bearing skill** | ELI-JURIS | Q-JUR == India |
| Q-IND | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / Healthcare / Utilities-Power / Logistics / Marine-Offshore / Rail / Renewables / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q-EXP | Who is exposed? | MCQ multi-select | Own workers / Contractors / Public-visitors / Nearby community | ELI-EXPOSURE | always |

**Branch map:** `india-state` (Q-JUR = India → Q-JUR-STATE + `KB-REG-IN-STATEFORMS`;
**mandatory** — confirm the state before routing to any India form-bearing skill).

## Echo-back

After Q-EXP (and Q-JUR-STATE if the branch ran), **echo the captured facts back** and
confirm before recommending any skill or emitting any run sheet:
"Routing for: re-roofing fall-from-height at [SITE-1], own workers + [CONTRACTOR],
UK, construction, deliverables = RA + JSA + permit + toolbox talk — correct?"
Only on confirmation do you read the index and assemble the recommended chain.

## Refuse-on-vague anchors

- Q-SUBJECT is the specificity anchor — refuse a vague subject ("help me with safety
  stuff", "I need some HSE docs"); ask again or record `[ASSUMPTION]` / `[GAP]`, never
  invent a task, a hazard, or a deliverable. Never recommend a skill until intent + the
  six shared facets are concrete.
- The shared facts captured here **ride the handoff** (the de-identified run sheet), so
  the chosen skill's own §2.7 intake confirms them and asks only the deep facets this
  router deferred — it does not re-ask jurisdiction, industry, or exposure.
