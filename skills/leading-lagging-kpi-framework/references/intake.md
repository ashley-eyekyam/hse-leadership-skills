---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-JURIS, ELI-EVIDENCE, ELI-SCORING, ELI-TEMPORAL]
  omits:
    ELI-COMPETENCY: "KPI framework design, not a team-judgement artefact — no competent-person elicitation"
    ELI-BASELINE: "no separate baseline state is elicited; the prior-period figures (Q-temporal) carry any trend baseline"
    ELI-EXPOSURE: "indicators are organisation/function-level metrics; no receptor/exposure list is elicited"
    ELI-OBLIGATIONS: "voluntary ISO 45001 9.1 / ISO 39001 framing, not a statutory filing with a deadline"
    ELI-LOCATION: "the named org/function/site carries the location; KPIs are entity-level, not task-sited"
  branches:
    - {when: Q1, option: "Road-transport-fleet", activates_questions: [Q-road], activates_output_section: road-safety-indicators, mandatory: true}
    - {when: Q11, option: "India", activates_questions: [Q-state], activates_output_section: india-state-detection, mandatory: true}
    - {when: Q4, condition: "lagging-only set", activates_output_section: balance-gate-refusal, mandatory: true}
    - {when: Q6, condition: "gameable target with no safeguard", activates_output_section: anti-gaming-gate-refusal, mandatory: true}
    - {when: Q7, activates_output_section: maturity-matched-mix}
    - {when: Q9, activates_output_section: rag-status}
---

# Structured intake — leading-lagging-kpi-framework

Run ONE question at a time — MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any design**;
**refuse a lagging-only set** (balance required), **refuse a gameable metric with no
safeguard** (defensibility), and **refuse an indicator with no definition** (specificity).
Lagging **rates** are computed by `incident_rates`, never invented. Canonical runtime
pattern: `KB-SNIP-INTAKE`.

This skill **designs / normalises** the indicator set. **Q1 disambiguates** it against the
calculators/exemplars it must NOT replace — `incident-rate-calculator` (*computes* a given
rate), `process-safety-kpi` (API RP 754 tiers), `aviation-spi-spt-framework` (ICAO Annex
19 SPIs) — and against the leadership siblings `safety-culture-assessment` /
`bbs-program-designer` / `safety-walk-gemba`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you want, and what **scope**? | MCQ | KPI-framework-design (this skill) ; Compute-a-given-rate (→ `incident-rate-calculator`) ; API-RP-754-tiers (→ `process-safety-kpi`) ; Aviation-SPI-SPT (→ `aviation-spi-spt-framework`) — scope = Organisation ; Function ; Site ; Road-transport-fleet | ELI-SCOPE | always |
| Q2 | Name the **organisation / function / site (or fleet)** and the **reporting period(s)**. | free-text | specific entity + dates — the specificity anchor | ELI-SUBJECT | always |
| Q3 | Which **leading** (active/predictive) indicators do you track or want? | MCQ multi-select | % planned inspections completed / near-miss reporting rate / training completion / action close-out rate / BBS percent-safe / gemba-commitment closure / PTW compliance / Other (resolve from KB-DATA-LEADING-INDICATORS) | ELI-SUBJECT | always |
| Q4 | Which **lagging** (reactive/outcome) indicators? | MCQ multi-select | TRIR / LTIFR / DART / severity rate / fatalities / None — **a lagging-only or leading-only set is refused; the balanced set needs both** | ELI-SUBJECT | always |
| Q5 | For each indicator, give the **definition**: **formula · source · frequency · owner**. | free-text | an indicator with no definition fails specificity — never a bare name | ELI-EVIDENCE | always |
| Q6 | What **target** for each, and (for any **countable** target) the **anti-gaming safeguard**? | free-text | a raw incident count as a target → suppresses reporting; pair it with a quality/assurance safeguard, else it is refused (defensibility) | ELI-SCORING | always |
| Q7 | What is the org's **culture maturity** (to match the leading/lagging **mix**)? | MCQ | Reactive / Developing / Mature / Unknown — mature shifts the mix toward leading | ELI-SCORING | always |
| Q8 | Any **benchmark** to compare against? | free-text | each figure cited source + year (look up the KB row); lagging rates computed by `incident_rates`, never a bare figure | ELI-SCORING | always |
| Q9 | What **output**, for whom, how widely shared? | MCQ + free-text | KPI framework table / Dashboard / Board or exec pack — for M / E / C — internal vs circulated (RAG status per indicator) | ELI-OUTPUT | always |
| Q10 | Which **sector** frames the indicator profile? | MCQ | Construction / Manufacturing / Logistics-Transport / Healthcare / Energy / Other (All) | ELI-INDUSTRY | always |
| Q11 | Which **standard / jurisdiction** anchors the monitoring duty and any law cited? | MCQ | ISO-45001-9.1-default ; UK ; USA ; EU ; India ; None | ELI-JURIS | always |
| Q-road | *(Road scope)* Which **road-safety** indicators (ISO 39001:2012)? | MCQ multi-select | Speeding ; Harsh-braking-events ; Journey-management ; Vehicle-defect-rate ; Driver-hours-compliance ; Seatbelt-use ; Helmet-use — each defined (formula·source·target) | ELI-SUBJECT | Q1 == Road-transport-fleet |
| Q-state | *(India)* Which **Indian state** files this monitoring/return (mandatory state detection)? | free-text | the state determines the form/portal — defers to `hse-india`; never a national form number | ELI-JURIS | Q11 == India |

**Branch map:** Q1 = Road-transport-fleet → **Q-road mandatory**; design the ISO 39001:2012
road-safety indicator set from `KB-DATA-ROAD-SAFETY-INDICATORS` (one skill, the single
home). Q11 = India → **Q-state mandatory** (state detection; defers to `hse-india`, never a
national form number). Q4 lagging-only (no leading) → **balance-gate refusal** (clause 9.1
reactive-only picture). Q6 a countable target with no safeguard → **anti-gaming-gate
refusal** (pair with a quality/assurance safeguard). Q7 maturity → shift the leading/lagging
mix toward leading as maturity advances. Q9 thresholds → RAG status per indicator. **Routing
guard:** a "compute our TRIR/LTIFR" *computation* request → route to
`incident-rate-calculator`; this skill *designs* the framework (lagging rates are computed
via `incident_rates`).

## Echo-back

Echo the captured facts back and ask the user to confirm before designing:
"Designing a balanced KPI framework for **{entity}**, period **{period}**, **{n}** leading
+ **{m}** lagging indicators (each defined: formula·source·frequency·owner·target),
maturity **{maturity}**, output **{output}**{, road-safety branch ON}. Lagging rates
computed via `incident_rates`; a lagging-only set and a gameable target with no safeguard
are refused. Correct before I design?"

## Refuse-on-vague anchors

- Q2 is the specificity anchor: refuse with no named organisation / function / site / fleet.
- **Balance gate:** refuse a lagging-only set (TRIR alone) — name the missing leading half.
- **Anti-gaming gate:** refuse a raw-count target with no quality/assurance safeguard.
- **Definition gate:** refuse any indicator with no formula · source · frequency · owner ·
  target — a bare indicator is not a KPI.
- Never invent a lagging rate or a benchmark figure; a *computation* request routes to
  `incident-rate-calculator`.
