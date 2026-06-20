---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL, ELI-EVIDENCE]
  omits:
    ELI-OBLIGATIONS: "a routine MoC carries no statutory submission deadline unless the change itself triggers a CAA approval — handled by asking the approval authority (Q10)"
    ELI-BASELINE: "the standing SMS/register is referenced via sibling skills, not rebuilt here"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator is the location identity"
  branches:
    - when: Q5
      equals: India
      activates_questions: [Q5a]
      activates_kb_row: KB-REG-IN-DGCA
      mandatory: true
    - when: Q5
      equals: FAA
      activates_output_section: ask-reference-no-fabrication
    - when: Q5
      equals: EASA
      activates_output_section: ask-reference-no-fabrication
    - when: Q2
      equals: Organisational
      activates_output_section: competency-staffing-fatigue-handover-hazards
    - when: Q2
      equals: Fleet
      activates_output_section: technical-training-mel-maintenance-hazards
    - when: Q4
      equals: Trial
      activates_output_section: review-after-trial-action
---

# Structured intake — aviation-change-safety-assessment

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. A change that identifies **zero new or changed hazards is
hard-flagged** — that is the skill's signature failure mode.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Name the operator/airport/AMO. | free-text | "name *this* org; refused if generic." | ELI-SUBJECT | always |
| Q2 | What type of change is this? | MCQ | New route/destination, Fleet/aircraft-type change, Equipment/avionics change, Procedure/SOP change, Organisational/personnel change, Infrastructure change, Other | ELI-SUBJECT | always |
| Q3 | Describe the specific change. | free-text | concrete; "we're changing things" is refused | ELI-SUBJECT | always |
| Q4 | When does the change take effect, and is it trialled/reversible? | MCQ+free-text | Permanent, Trial/period, Phased, Reversible — plus the effective date | ELI-TEMPORAL | always |
| Q5 | Which CAA/SSP applies? | MCQ | India/DGCA, FAA, EASA, Other CAA (specify), Unknown | ELI-JURIS | always |
| Q5a | *(India only)* Which Indian operations / which State Safety Programme layer applies? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q5==India |
| Q6 | What new or changed hazards does this introduce? | free-text | per hazard; **a change with no new hazards is flagged** | ELI-SUBJECT | always |
| Q7 | Who/what does the change newly expose? | MCQ | Flight crew · Cabin crew · Ground crew · Passengers · Public · Asset · Multiple | ELI-EXPOSURE | per hazard |
| Q8 | ICAO severity for each new hazard. | MCQ | Negligible · Minor · Major · Hazardous · Catastrophic | ELI-SCORING | per hazard |
| Q9 | ICAO likelihood for each new hazard. | MCQ | Extremely Improbable · Improbable · Remote · Occasional · Frequent | ELI-SCORING | per hazard |
| Q10 | Who approves or declines this change? | free-text | the named approval authority + their role | ELI-COMPETENCY | always |

**Branch map.** `Q2==Organisational` → prompt competency/staffing/fatigue/handover hazards in
Q6. `Q2∈{Fleet,Equipment}` → prompt technical/training/MEL/maintenance hazards. `Q5==India` →
Q5a + `KB-REG-IN-DGCA` (the mandatory India follow-up resolves the State Safety Programme
layer). `Q5∈{FAA,EASA,Other}` → ask the reference, no fabricated clause. `Q4==Trial` → output
records a review-after-trial trigger as an action.

## Echo-back
Echo the captured facts back and ask the user to confirm before any analysis:
*"Confirmed: **{change type}** at **{named operator}**, effective **{date/mode}**, **{N}**
new/changed hazards, approval authority **{role}**. Proceed to 5×5 scoring + approve/decline?"*

## Refuse-on-vague anchors
- Q3 is the specificity anchor: a change described as "we're changing things" → **refuse**;
  never proceed on a vague subject.
- Zero new hazards identified → **hard flag** (the skill's signature failure mode).
- An FAA/EASA/Other clause not supplied → `[GAP]`; never fabricate a CAR / AC number.
