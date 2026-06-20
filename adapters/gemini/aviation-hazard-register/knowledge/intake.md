---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-TEMPORAL: "a hazard register is a living log, not a periodic artifact; review cadence is set at SMS-manual level, not per-register"
    ELI-OBLIGATIONS: "no submission deadline attaches to the register itself"
    ELI-BASELINE: "existing controls are captured per-hazard inside ELI-SUBJECT (Q7), not as a separate baseline elicitation"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator/area is the location identity"
  branches:
    - when: Q3
      equals: India
      activates_questions: [Q3a]
      activates_kb_row: KB-REG-IN-DGCA
      mandatory: true
    - when: Q3
      equals: FAA
      activates_output_section: ask-reference-no-fabrication
    - when: Q3
      equals: EASA
      activates_output_section: ask-reference-no-fabrication
    - when: Q1
      equals: Add
      activates_questions: [Q2]           # ingest existing register first; suppress re-logging
    - when: Q1
      equals: Review
      activates_questions: [Q2]
---

# Structured intake — aviation-hazard-register

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. Severity and likelihood are user choices on the ICAO 5×5
axes; the **band is assigned by `risk_matrix.score()`, never by the model**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Build a new register or maintain/review an existing one? | MCQ | Build/a new register, Add/hazards to an existing register, Review/re-score an existing register | ELI-SCOPE | always |
| Q2 | Name the operator/airport/AMO and the operation/area the register covers. | free-text | "name *this* org and area; 'an airline' is refused." | ELI-SUBJECT | always |
| Q3 | Which certificating authority / SSP applies? | MCQ | India/DGCA, FAA, EASA, Other CAA (specify), Unknown | ELI-JURIS | always |
| Q3a | *(India only)* Which Indian operations / which State Safety Programme layer applies? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q3==India |
| Q4 | Describe each hazard and its supporting evidence. | free-text | one per hazard; each must trace to an evidence item | ELI-SUBJECT | always |
| Q5 | For each hazard, how was it surfaced? | MCQ | Reactive (occurrence/report) · Proactive (audit/inspection/survey) · Predictive (FDM/FOQA, trend) | ELI-EVIDENCE | per hazard |
| Q6 | Who/what is exposed to each hazard's consequence? | MCQ | Flight crew · Cabin crew · Ground/ramp crew · Passengers · Third party/public · Aircraft/asset · Multiple | ELI-EXPOSURE | per hazard |
| Q7 | What is the credible worst consequence, and what controls already exist? | free-text | per hazard; the existing-control baseline for residual scoring | ELI-SUBJECT | per hazard |
| Q8 | Choose ICAO severity. | MCQ | Negligible · Minor · Major · Hazardous · Catastrophic | ELI-SCORING | per hazard |
| Q9 | Choose ICAO likelihood. | MCQ | Extremely Improbable · Improbable · Remote · Occasional · Frequent | ELI-SCORING | per hazard |
| Q10 | Who will own the mitigating actions? | free-text | role label; validated by `smart_actions` | ELI-COMPETENCY | always |

**Branch map.** `Q3==India` → Q3a + `KB-REG-IN-DGCA` (the mandatory India follow-up resolves
the State Safety Programme layer). `Q3∈{FAA,EASA,Other}` → ask the reference, no fabricated
clause. `Q1∈{Add,Review}` → ask for the existing register (Q2) first, suppress re-prompting
logged hazards. `Q8 & Q9` per hazard → `risk_matrix.score(severity, likelihood,
matrix=AVIATION_5X5)`; the model never assigns the band.

## Echo-back
Echo the captured facts back and ask the user to confirm before any analysis:
*"Confirmed: register for **{named operator}** ({area}), under **{CAA}**, **{N}** hazards,
each traced to evidence. Scoring on the ICAO 5×5. Proceed?"*

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "rate our risks" with no named operator → **refuse**; never
  proceed on a vague subject.
- A hazard with no supporting evidence → ask, record `[GAP]`, do not invent.
- Never let the model pick a band to hit a desired rating — the band is the engine's.
