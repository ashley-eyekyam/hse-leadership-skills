---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-BASELINE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL, ELI-OBLIGATIONS]
  omits:
    ELI-EXPOSURE: "SPIs measure organisational safety performance, not per-hazard exposure"
    ELI-EVIDENCE: "the trend evidence is the baseline/occurrence data captured at ELI-BASELINE (Q7); no separate evidence pull"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator is the location identity"
  branches:
    - when: Q3
      equals: India
      activates_questions: [Q3a]
      activates_kb_row: KB-REG-IN-DGCA
      activates_output_section: dgca-ssp-alosp-alignment
      mandatory: true
    - when: Q3
      equals: FAA
      activates_output_section: ask-reference-no-fabrication
    - when: Q3
      equals: EASA
      activates_output_section: ask-reference-no-fabrication
    - when: Q8
      equals: HistoricalBaseline
      activates_questions: [Q7]           # baseline data becomes REQUIRED; else [GAP]
    - when: Q1
      equals: Review
      activates_output_section: ingest-existing-spi-set
---

# Structured intake — aviation-spi-spt-framework

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. Alert/target thresholds are derived from supplied baseline
data via `incident_rates` (quote `KB-DATA-TRIR-BENCHMARKS` source+year); an absent figure is
`[GAP]`, **never a fabricated number**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Design a new SPI/SPT set or review an existing one? | MCQ | Design/a new set, Review/re-baseline an existing set | ELI-SCOPE | always |
| Q2 | Name the operator/airport/AMO and operation type. | free-text | refused if generic | ELI-SUBJECT | always |
| Q3 | Which CAA/SSP applies (sets the ALoSP basis)? | MCQ | India/DGCA SSP ALoSP, FAA, EASA, Other CAA (specify), Unknown | ELI-JURIS | always |
| Q3a | *(India only)* Which Indian operations / which State Safety Programme ALoSP layer applies? | free-text | aligns the DGCA State Safety Programme ALoSP layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q3==India |
| Q4 | Which hazards / safety objectives must the SPIs track? | free-text | each SPI maps to one; pull from `aviation-hazard-register` | ELI-SUBJECT | always |
| Q5 | For each candidate SPI, leading or lagging? | MCQ | Leading (precursor) · Lagging (outcome) | ELI-SCORING | per SPI |
| Q6 | What is the measurement period for each SPI? | MCQ | Monthly · Quarterly · Rolling-12-month · Annual · Other | ELI-TEMPORAL | per SPI |
| Q7 | What baseline/occurrence data exists for trend context? | free-text | feeds `incident_rates`; quote `KB-DATA-TRIR-BENCHMARKS` source+year; absent → `[GAP]` | ELI-BASELINE | always |
| Q8 | How are alert/target levels derived? | MCQ | HistoricalBaseline/statistical, ALoSP/from the regulator, Benchmark/industry, Mixed | ELI-SCORING | per SPI |
| Q9 | Who owns each SPI? | free-text | role label; an SPI with no owner is flagged | ELI-COMPETENCY | always |

**Branch map.** `Q3==India` → Q3a + `KB-REG-IN-DGCA` (DGCA SSP ALoSP), ALoSP-alignment output
line — the mandatory India follow-up resolves the State Safety Programme ALoSP layer.
`Q3∈{FAA,EASA,Other}` → ask the reference, no fabricated clause. `Q8==HistoricalBaseline` →
Q7 baseline data becomes **required** (an alert/target cannot be statistical without it; else
`[GAP]`). `Q1==Review` → ingest the existing SPI set; re-baseline rather than redesign.

## Echo-back
Echo the captured facts back and ask the user to confirm before any analysis:
*"Confirmed: SPI/SPT set for **{named operator}**, **{N}** indicators ({L} leading / {M}
lagging), ALoSP basis **{CAA}**, periods **{…}**. Proceed?"*

## Refuse-on-vague anchors
- Q2 is the specificity anchor: an SPI request with no named operator → **refuse**; never
  proceed on a vague subject.
- An SPI with no owning hazard/objective → flag; a performance figure invented to fill a
  baseline gap → never; an absent datum → `[GAP]` per `KB-DATA-TRIR-BENCHMARKS` discipline.
