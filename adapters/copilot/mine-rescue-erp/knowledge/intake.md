---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-LOCATION, ELI-JURIS, ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL, ELI-SCORING]
  omits:
    ELI-OBLIGATIONS: "narrows to the emergency-preparedness duty citation only — no numbered-form output; this is an SOP-class plan (B8 pattern)."
  branches:
    - ask: ELI-JURIS
      when: Q3
      equals: "infer-then-confirm the DGMS region and the **state** if the jurisdiction is India"
      activates_questions: [Q3]   # India -> DGMS region/state infer-then-confirm (mandatory)
    - ask: ELI-SCOPE
      when: Q1
      option: "b) Review-gap-check existing"
      activates_output_section: gap-check   # gap-check output vs a clean draft
    - ask: ELI-COMPETENCY
      when: Q5
      # a capability stated aspirationally -> refuse + re-ask for actuals; [GAP] where unknown
---

# Structured intake — mine-rescue-erp

Run **one question at a time** (`KB-SNIP-INTAKE`). MCQ where the answer space is
enumerable, free-text where it is open; **branch on the answers**; **echo the captured
facts back before any drafting**; **refuse on a vague subject** — an aspirational
rescue-team/mutual-aid placeholder is rejected and re-asked for actuals, and an unknown
response time is `[GAP]`, **never a fabricated timing** (realism is the whole point).

**De-identification runs first** (`METHODOLOGY.md`). For India the **DGMS region/state (Q3)
is resolved infer-then-confirm**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Build a new ERP or review an existing one? | MCQ | a) Draft new / b) Review-gap-check existing | ELI-SCOPE | always |
| Q2 | Commodity + mine type + workforce? | MCQ | commodity (coal / metal / other) × opencast-UG × workforce band (<100 / 100–500 / 500–2000 / >2000) | ELI-INDUSTRY/ELI-EXPOSURE | always |
| Q3 | DGMS region / state (India)? | MCQ→confirm | infer-then-confirm the DGMS region and the **state** if the jurisdiction is India | ELI-JURIS/ELI-LOCATION | India |
| Q4 | Which emergency scenarios? | mcqmulti-select | fire-explosion · inrush-inundation · strata failure · irrespirable-flammable atmosphere · entrapment · mobile-plant event · other (`KB-DATA-MINING-HAZARDS`) | ELI-SUBJECT | always |
| Q5 | Rescue-team capability? | free-text | "Trained-rescuer count, apparatus type/sets, certification currency — **reject aspirational; realism is the point**" | ELI-COMPETENCY | always |
| Q6 | Rescue-station + mutual-aid links? | free-text | "Station name + distance/response time; mutual-aid agreements (named, actual)" | ELI-EVIDENCE/ELI-BASELINE | always |
| Q7 | Mobilisation route + comms + refuge? | free-text | "Actual mobilisation sequence, communication systems, refuge-chamber capacity" | ELI-BASELINE | always |
| Q8 | Drill cadence + last drill? | MCQ+free-text | statutory cadence (confirm against the duty) — + last-drill date per scenario | ELI-TEMPORAL | always |
| Q9 | Scenario-ranking scheme? | MCQ | a) Org's existing emergency / risk matrix / b) Default 5×5 (D-02 bands) — confirm | ELI-SCORING | always |
| Q10 | Output + distribution? | MCQ | a) Full ERP document / b) Gap-check report / c) Drill schedule only | ELI-OUTPUT | always |

## Branch map
- **Q1=b (review)** → activate a **gap-check output section** against the existing ERP rather
  than a clean draft.
- **Q2 mine type** sets scenario plausibility (UG coal → methane / inrush / irrespirable;
  opencast → highwall / mobile-plant).
- **Q3** (India) resolves the DGMS region / state, infer-then-confirm.
- **Q4 scenarios** each get a mobilisation sequence (team → station → mutual-aid →
  NDMA/DGMS) with credible timing from Q5/Q6.
- **Q5 aspirational answer** → refuse + re-ask for actuals; `[GAP]` where genuinely unknown,
  never an invented capability.
- **Q8 last-drill** seeds the `smart_actions` drill schedule with owner + date.
- Scenario ranking via `risk_matrix` (Q9); the top-ranked scenarios drive the plan detail.

## Echo-back
"Mine-rescue ERP (**{build / review}**) for **{mine, commodity / type, workforce}**;
scenarios **{list}**; rescue capability **{n rescuers / apparatus}**; station **{name @
time}**; output **{type}**. Confirm before I draft." — echo the captured facts back and
**confirm** before any drafting.

## Refuse-on-vague anchors
- **"We have a rescue team"** with no count / apparatus / certification → re-ask for actuals
  (Q5 is the realism anchor).
- A **placeholder mutual-aid link** ("to be arranged") → reject; an un-agreed link is
  `[ASSUMPTION]`.
- **Unknown response time** → `[GAP]`, never a fabricated timing.

## Domain evidence types (ELI-EVIDENCE)
Rescue-team roster + certification currency; self-contained breathing-apparatus inventory;
rescue-station location + response time; mutual-aid agreements; refuge-chamber / SCSR
provision; communication / gas-monitoring systems; last-drill records per scenario.

> **[GAP] for the human verifier:** Indian statutory mine-rescue drill cadence /
> rescue-station rules are cited generically via `KB-REG-IN-MINES-ACT`; Q8 cadence is authored
> as **confirm-against-duty**, not a hard-coded interval.
