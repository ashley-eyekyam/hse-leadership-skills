---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "the analysis structures supplied exceedance summaries; any 5x5 hazard scoring is handled downstream in aviation-hazard-register, not here"
    ELI-EXPOSURE: "exposure is per-hazard in the register; this skill structures FDM event summaries, not hazard exposure"
    ELI-BASELINE: "the trend baseline is the prior-period supplied summary data captured at ELI-EVIDENCE (Q5), not a separate baseline elicitation"
    ELI-OBLIGATIONS: "no submission deadline attaches to an internal FDM analysis"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator/fleet is the location identity"
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
    - when: Q6
      equals: Trend
      activates_output_section: require-two-or-more-periods   # a single exceedance is never a trend
---

# Structured intake — aviation-fdm-foqa-analysis

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. This is an **assistive** skill: it structures the
exceedance summaries the user supplies, **never raw flight data**, and **never invents an
exceedance count or value** — an absent datum is `[GAP]`, routed to the competent FDM team.
Crew detail is intrinsically identifying, so de-identification to **role labels** runs first
and a crew-identity leak is a de-id hard-fail.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you want produced from the FDM/FOQA data? | MCQ | Structure a period's exceedance summary · Trend a metric across periods · Summarise for an SRB/SPI pack | ELI-SCOPE | always |
| Q2 | Name the operator/fleet and the operation the data covers. | free-text | "name *this* operator/fleet; 'an airline' is refused." | ELI-SUBJECT | always |
| Q3 | Which certificating authority / SSP applies? | MCQ | India/DGCA, FAA, EASA, Other CAA (specify), Unknown | ELI-JURIS | always |
| Q3a | *(India only)* Which Indian operations / which State Safety Programme layer applies? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q3==India |
| Q4 | What is the audience and how will it circulate? | MCQ | Internal FDM team · SRB/safety pack · SPI baseline input · Other | ELI-OUTPUT | always |
| Q5 | Paste the FDM/FOQA exceedance summary(ies) to structure. | free-text | **de-identify crew detail (name, route/base/flight, exact dates) FIRST**; the skill structures *supplied* summaries, never raw flight data | ELI-EVIDENCE | always |
| Q6 | Is each finding a one-off or a trend? | MCQ | OneOff/a single event, Trend/across ≥2 periods of supplied data | ELI-EVIDENCE | per finding |
| Q7 | What period(s) does the data cover? | MCQ+free-text | Single month · Quarter · Rolling-12 · Other — plus the dates | ELI-TEMPORAL | always |
| Q8 | Who owns the resulting SMS actions? | free-text | role label; validated by `smart_actions`; never a crew-blame owner | ELI-COMPETENCY | always |

**Branch map.** `Q3==India` → Q3a + `KB-REG-IN-DGCA` (the mandatory India follow-up resolves
the State Safety Programme layer). `Q3∈{FAA,EASA,Other}` → ask the reference, no fabricated
clause. `Q6==Trend` → require ≥2 periods of supplied data; a single exceedance is never
reported as a trend. **No exceedance count or value is ever invented** — an absent datum is
`[GAP]` routed to the competent FDM team.

## Echo-back
Echo the captured facts back (crew detail de-identified to role labels) and ask the user to
confirm before any analysis:
*"Confirmed: FDM/FOQA **{structure/trend}** for **{named operator/fleet}**, under **{CAA}**,
**{N}** findings from supplied summaries, period **{…}**, audience **{…}**. Crew detail
de-identified; nothing computed from raw data. Proceed?"*

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "analyse our flight data" with no supplied summary →
  **refuse** (the skill cannot and must not analyse raw data).
- Any crew detail entering the output → **blocked** (acute de-id).
- An exceedance count/value not present in the supplied summary → `[GAP]`, never fabricated.
