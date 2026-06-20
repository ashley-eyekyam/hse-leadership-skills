---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-EVIDENCE, ELI-SCORING, ELI-TEMPORAL]
  omits:
    ELI-COMPETENCY: "KPI computation, not a team-judgement artefact — no competent-person elicitation"
    ELI-BASELINE: "the PSE events carry their own consequence; no separate baseline state"
    ELI-EXPOSURE: "events carry consequence; no receptor list is elicited"
    ELI-OBLIGATIONS: "voluntary API RP 754 framing, not a statutory filing with a deadline"
    ELI-LOCATION: "the facility name carries the location; KPIs are facility-level, not task-sited"
  branches:
    - {when: Q4, activates_output_section: rate-gap-marker, mandatory: true}
    - {when: Q1, option: Trend (multi-period), activates_questions: [Q8], activates_output_section: trend-line}
    - {when: Q6, activates_output_section: rag-status}
---

# Structured intake — process-safety-kpi

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any computation**;
**never report a rate without its work-hours denominator** (missing/zero hours → the rate
is `[GAP]`, fail-loud, but the count is still reported) and **never invent a PSE count or a
benchmark figure**. Canonical runtime pattern: `KB-SNIP-INTAKE`.

This skill is the **API RP 754 PSE pyramid** (process-safety events), **not** occupational
TRIR/LTIFR/DART — an occupational-rate request routes to `incident-rate-calculator`. A
count is only a managed KPI once it carries a **target / threshold** (the RAG line).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Single reporting period**, or a **trend across periods**? | MCQ | Single period / Trend (multi-period) | ELI-SCOPE | always |
| Q2 | Name the **facility** and the **reporting period(s)**. | free-text | specific site + dates — the specificity anchor | ELI-SUBJECT | always |
| Q3 | List the **PSE events** with enough fact for the **Tier-1/Tier-2 threshold test** (material, quantity, consequence). | free-text | counts from facts, never invented | ELI-SUBJECT | always |
| Q4 | What is the **total work-hours denominator** for the rate? | free-text | missing/zero → rate `[GAP]` (fail-loud); the count is still reported | ELI-EVIDENCE | always |
| Q5 | Which **leading indicators** do you track? | MCQ multi-select | Tier-3 (challenges to safety systems: SIS demands, relief activations, excursions) / Tier-4 (operating discipline: procedure compliance, training currency, overdue inspections) / None | ELI-SUBJECT | always |
| Q6 | What is your **target / threshold per indicator** (red/amber/green)? | free-text | turns a count into a managed KPI | ELI-SCORING | always |
| Q7 | Any **benchmark** to compare against? | free-text | each figure cited source + year (look up the KB row); never a bare figure | ELI-SCORING | always |
| Q8 | *(Trend)* Do you have **prior-period counts/rates**? | free-text | required for the trend line | ELI-EVIDENCE | Q1 == Trend (multi-period) |
| Q9 | What **output**, for whom, how widely shared? | MCQ + free-text | KPI table / Dashboard / Board or exec pack — for M or C — internal vs circulated | ELI-OUTPUT | always |
| Q10 | Which **sector** frames the facility's PSE profile? | MCQ | Chemicals / Oil & Gas / Refining / Petrochemicals / Other | ELI-INDUSTRY | always |
| Q11 | Which **framing standard / jurisdiction** for the tier definitions and any duty hook? | MCQ | API RP 754 (voluntary) / UK / USA / EU / None | ELI-JURIS | always |

**Branch map:** Q4 missing/zero hours → rate `[GAP]` (fail-loud); the count is still reported (mandatory). Q1 = Trend → Q8 mandatory; trend-line section. Q6 thresholds supplied → rag-status (red/amber/green per indicator). Q7 benchmark → look up the benchmark KB row; cite source + year; never a bare figure. **Routing guard:** an occupational TRIR/LTIFR/DART request → route to `incident-rate-calculator` (this skill is the PSE pyramid only).

## Echo-back

Echo the captured facts back and ask the user to confirm before computing:
"Facility **{facility}**, period **{period}**, **{n}** PSE events for the Tier-1/2 test,
work-hours **{hours}**, leading indicators **{indicators}**, thresholds **{thresholds}**.
Missing-hours → rate `[GAP]`, count still reported. Correct before I compute?"

## Refuse-on-vague anchors

- Q2 is the specificity anchor: refuse with no named facility / period.
- "Compute our rate" with no work-hours → the rate is `[GAP]`, never guessed; the count is
  still reported.
- Never invent a PSE count or a benchmark figure; an occupational-rate request routes to
  `incident-rate-calculator`.
