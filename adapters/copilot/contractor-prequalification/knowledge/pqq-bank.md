<!-- KB-SNIP-PQQ-BANK -->
# Contractor PQQ bank — evidence-anchored questions by risk tier

**Fragment ID:** `KB-SNIP-PQQ-BANK`
**This is prompt text, applied by the model — not a generator.** It is the evidence-anchored
prequalification-question bank the `contractor-prequalification` (#16) skill draws from,
keyed to the risk tier in `KB-DATA-CONTRACTOR-TIERS`. Every question is tied to the
**verifiable evidence** that answers it — claims alone never score.

> Source: ISO 45001:2018 cl. 8.1.4 (procurement/contractors) · UK CDM 2015 reg. 8 · UK SSIP question-set convention · US OSHA multi-employer policy · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — select the tier's questions; each question names its required evidence

### Core (all tiers — T1+)
- HSE policy signed by top management — *evidence: the signed policy.*
- Employers'/public-liability insurance — *evidence: current certificate.*
- Accident & enforcement history (last 3–5 yrs) — *evidence: rates + any notices (de-identify named injured persons before scoring).*
- Competence of the workforce for the work — *evidence: training/competence records.*

### Task-specific (T2+)
- Method statements / RAMS for the scope — *evidence: the RAMS, hazard-specific.*
- Recognised accreditation (SSIP / ISO 45001) — *evidence: valid certificate, not a claim.*
- Sub-contractor management arrangements — *evidence: the process + an example.*

### High-hazard module (T3 — hot work / confined space / height / lifting / energised electrical)
- Activity-specific competence/certification — *evidence: the certification, in date.*
- Safe-system-of-work / permit integration — *evidence: the SSoW/permit procedure.*
- Verified accident-rate data for the high-hazard activity — *evidence: the data, verifiable.*

## Scoring discipline

- **Never score a self-asserted claim as met** without the named evidence (#16 eval case 1)
  — missing evidence becomes a `[GAP]` and blocks an unconditional pass.
- **High-hazard work cannot pass on PPE/competence claims alone** — higher-order controls
  must be evidenced (`KB-SNIP-HOC`).
- Output an approve / conditional / reject recommendation with **named conditions + a review
  date** (`smart_actions`).

## Output expectation

A risk-tiered PQQ, an evidence register with verification status, a scorecard, and a
recommendation. Feeds `specificity`, `defensibility`, `hierarchy_of_controls`.
