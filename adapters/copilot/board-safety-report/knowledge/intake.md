---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-EXPOSURE, ELI-EVIDENCE,
           ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "B9 reports computed rates via `incident_rates`; it does not score risk on a matrix."
    ELI-INDUSTRY: "Sector enters only to pick the benchmark; Q8 carries its own source + sector."
    ELI-LOCATION: "A board paper is org/period-level; naming a single site can re-identify (de-id/aggregation rule — ELI-LOCATION is omitted BY DESIGN)."
    ELI-COMPETENCY: "The deliverable is governance asks, not an action register; Q6b is an optional accountability sharpener, not a required owner field."
    ELI-BASELINE: "A board narrative reports period performance against prior period + benchmark, not a controls baseline."
  branches:
    - {when: Q9, option: "Yes", activates_kb_row: KB-STD-ISO14001, activates_output_section: env-performance-line, mandatory: false}  # single ISO 14001 9.1.2 line, NOT full ESG (D-02)
    - {when: Q5, activates_output_section: hipo-sif-lens-interpreted, mandatory: false}  # D-01 lens, interpreted not listed; fires when Q5 non-empty
    - {when: Q3, activates_output_section: computed-rates, mandatory: false}  # rates-guard: only if Q3 has hours AND counts, else pre-computed rate or [GAP]
    - {when: Q8, activates_kb_row: KB-DATA-TRIR-BENCHMARKS, mandatory: false}  # benchmark: only if Q8 carries source + year
    - {when: Q10, option: India, activates_questions: [Q10a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}  # mandatory only if a statutory figure is cited
---

# Structured intake — board-safety-report

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. Never
proceed on a vague period or audience — ask, or record `[ASSUMPTION]` / `[GAP]`. **Never
invent a figure or a benchmark.**

**De-id + aggregation is stronger here than anywhere else.** Q4 (key events) and Q5
(HiPo/SIF) are **flagged for IMMEDIATE de-identification AND aggregation** in Workflow
step 1 — *before* any analysis — because the board-report leak vector is re-identification
through a vivid **single-incident anecdote** (a name is not required to re-identify). The
echo-back therefore shows **aggregated, de-identified facts only**: no individual incident
narrated, no named site (ELI-LOCATION is omitted by design), no `<5` cell. The scrub runs
*before* the echo-back.

Load-bearing branches: the **hours+counts rates-guard** (Q3 → `incident_rates` only when
hours AND counts are present, else a pre-computed rate or `[GAP]` — never a fabricated
denominator); the **HiPo/SIF lens** (Q5 non-empty → interpreted, not merely listed — D-01);
the optional **ISO 14001 9.1.2 env-performance line** (Q9 = Yes → a single line, NOT a full
ESG branch — D-02); and the **mandatory India→state branch** (Q10 = India → Q10a +
`KB-REG-IN-STATEFORMS`, only when a statutory figure is cited).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Reporting period** | free-text + MCQ | "Which period does this report cover?" — Monthly / Quarterly / Half-year / Annual / Other (+ the exact dates, e.g. 'FY2025' or 'Q2 2026'). Sets the subtitle + the `period` label passed to `incident_rates`; the comparison baseline. | ELI-TEMPORAL | always |
| Q2 | **Audience body** | MCQ | Board of directors / Executive committee / Senior leadership team. Tunes register/depth (board = most strategic, least operational) — the narrative altitude. *(The audience facet stays `[E]`; this only tunes the register.)* | ELI-OUTPUT | always |
| Q3 | **Safety data / metrics available** | free-text (structured) | "Provide the period's safety metrics — recordable / lost-time / DART counts **and hours worked** (for rates), plus any leading indicators: training %, audit/inspection closure, near-miss reporting rate, action closure." The **hours + counts gate the `incident_rates` call**; leading indicators are synthesized. | ELI-EVIDENCE | always |
| Q4 | **Key events of the period** | free-text | "Summarize the significant HSE events of the period (serious incidents, notable near-misses, regulatory contacts, audits). **These will be de-identified AND aggregated — do not name individuals; a single event will be rolled up, never narrated as an anecdote.**" Flagged for **immediate** de-id + aggregation (step 1). | ELI-SUBJECT | always |
| Q5 | **HiPo / SIF events** | free-text | "List any **high-potential (HiPo) incidents** and **serious-injury-or-fatality (SIF) precursors** in the period — events that *could* have been life-altering regardless of actual outcome." Drives the **D-01 HiPo/SIF lens** (step 4); de-identified + aggregated like Q4. | ELI-SUBJECT | always |
| Q6 | **Strategic priorities** | free-text | "What are the organisation's current HSE strategic priorities or objectives?" Frames the narrative against objectives (ISO 45001 9.3) + the strategic-actions section. | ELI-SUBJECT | always |
| Q6b | **Accountability for strategic asks** | free-text | "For each strategic priority/ask, which executive is accountable? (role-level — sharpens the governance asks; optional)" — accountability sharpens the *output* ask (ELI-COMPETENCY is omitted by design: a board paper names asks, not an action register). | ELI-OUTPUT | always |
| Q7 | **Prior-period comparison data** | free-text | "Provide the prior period's figures for trend comparison (or say if unavailable)." Absent → trends flagged `[GAP]`, never invented. | ELI-EVIDENCE | always |
| Q8 | **Benchmark target** | free-text | "Which benchmark should performance be compared against (industry/sector average, an internal target)? If you have a figure, state it **with its source**; otherwise the skill reads the KB benchmark with its source + year." Resolves `KB-DATA-TRIR-BENCHMARKS`; absent → `[GAP]`. | ELI-OBLIGATIONS | always |
| Q9 | **Environmental metrics?** (optional) | MCQ + free-text | No / Yes ; (if Yes, list them) — "Are environmental events/metrics in scope for this board paper?" then a **single** optional ISO 14001 9.1.2 env-performance line (D-02); **not** a full ESG branch. | ELI-EXPOSURE | always |
| Q10 | **Jurisdiction** | MCQ | India / UK / USA / EU / Other-or-Unknown. Mostly context (B9 is narrative); **India → resolve the state (Q10a)** only if a statutory figure is cited. | ELI-JURIS | always |
| Q10a | *(India only, if a statutory figure is cited)* **Which state?** | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other — **mandatory state detection; confirm the state before citing any statutory figure or form** (never a national form number). | ELI-JURIS | Q10 == India |

**Branch map:** `env-line` (Q9 = Yes → `KB-STD-ISO14001` + single env line, D-02; non-mandatory);
`hipo-sif` (Q5 non-empty → interpreted-not-listed lens, D-01); `rates-guard` (Q3 has hours
AND counts → computed-rates, else pre-computed / `[GAP]`); `benchmark` (Q8 has source + year
→ `KB-DATA-TRIR-BENCHMARKS`); `india-state` (Q10 = India AND a statutory figure cited → Q10a +
`KB-REG-IN-STATEFORMS`; **mandatory**).

## Echo-back

After the last applicable question — and **after** the de-id/aggregation scrub (step 1) —
**echo a captured-facts summary** showing **aggregated, de-identified facts only** (no
named individual, no single-incident anecdote, no named site) and confirm before any
analysis:
"Board safety report for FY2025, for the Board of directors; lagging metrics +
training/audit leading indicators provided; key events + HiPo/SIF to be aggregated;
priorities = contractor safety + psychosocial; comparison vs FY2024; benchmark = sector
TRIR [source, year] — correct?"

## Refuse-on-vague anchors

- Never proceed on a vague period or audience; never invent a figure or benchmark; an
  absent prior period or benchmark → `[GAP]`, never a fabricated comparator.
- **The hours + counts guard on Q3 is load-bearing** — it prevents fabricating a rate
  denominator; if hours are absent, take a pre-computed rate as input or flag `[GAP]`.
- **De-id + aggregation is the load-bearing anchor** — the Q4/Q5 scrub runs *before*
  echo-back, so no individual incident, person, or `<5` cell is identifiable in the echo
  or the report.

## Domain evidence types (ELI-EVIDENCE)

Period recordable/LTI/DART counts + hours worked · leading indicators (training %,
audit/inspection closure, near-miss reporting rate, CAPA on-time closure %,
leadership-tour count) · HiPo/SIF event list · prior-period figures · a sourced benchmark
(body + year + sector) · optional environmental metrics for the ISO 14001 9.1.2 line.
