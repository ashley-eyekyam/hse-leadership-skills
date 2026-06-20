---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-EVIDENCE, ELI-OBLIGATIONS,
           ELI-SCORING, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "Sector enters only via the optional benchmark (Q6 carries its own sector)."
    ELI-LOCATION: "Scope/site is named in Q2; no asset-level detail is needed for a rate."
    ELI-EXPOSURE: "The exposed population is captured as aggregate hours worked (Q4), not a named population."
    ELI-BASELINE: "A rate has no controls baseline."
    ELI-COMPETENCY: "A deterministic calculation has no judgement owner; the tested engine computes the figure."
  branches:
    - {when: Q4, activates_output_section: refuse-no-denominator, mandatory: true}  # hours-gate: Q4 blank or <=0 → HARD refuse, no rate without the denominator
    - {when: Q2b, option: India, activates_questions: [Q2c], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}  # India recordability → resolve the state (mandatory)
    - {when: Q6, activates_kb_row: KB-DATA-TRIR-BENCHMARKS, mandatory: false}  # benchmark: only if Q6 carries source + year
    - {activates_output_section: gap-severity-not-computed, mandatory: false}  # severity-deferred (D-03): if asked, mark [GAP] — NEVER compute a severity rate in-prompt
---

# Structured intake — incident-rate-calculator

B10 runs a lean, MCQ-heavy intake — the counts, the **mandatory** denominator, the period,
and the recordability standard. Run it following `KB-SNIP-INTAKE` — **one question at a
time**, branch on the answers, **echo the captured facts back** before computing, and
**never invent a count or a denominator**. The hours worked is not optional: without it
there is no rate.

The load-bearing discipline: **Q4 (total hours worked) is a HARD refuse** — a blank, zero,
or negative denominator surfaces the engine's honest `ValueError`, never a fake `0.0`; never
substitute a default and never annualize a partial period. **Q2 (site/scope & period) is the
specificity anchor** — a rate with no named scope+period is not defensible. **The model never
does the arithmetic** — the figure is the tested `incident_rates` engine's returned value,
presented verbatim. **Severity rate is a deferred `[GAP]`** (D-03) — no validated engine in
v1.0; never computed in-prompt.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Which rate(s)** do you need | MCQ multi-select | TRIR (recordables) / DART (days-away-restricted-transfer) / LTIFR (lost-time injuries) / **All three (default)** — selects which `incident_rates` calls run | ELI-SUBJECT / ELI-OUTPUT | always |
| Q2 | **Site / scope & reporting period** | free-text | "Name the site/scope and the exact period — e.g. 'Plant 2, Q1 2026 (Jan–Mar)'." — the specificity anchor; a rate with no named scope+period is not defensible. Refuse a vague answer; record `[GAP]` if truly unavailable, never fabricate | ELI-SCOPE / ELI-TEMPORAL | always |
| Q2b | **Recordability standard / jurisdiction** | MCQ | OSHA 29 CFR 1904 (default) / India ; notifiable-injury (→ which state?) / UK RIDDOR / Other — fixes what counts as a recordable before counting | ELI-JURIS / ELI-OBLIGATIONS | always |
| Q2c | *(India only)* **Which state?** | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other — **mandatory state detection** for the India notifiable-injury definition; confirm the state before applying any state recordability rule | ELI-JURIS | Q2b == India |
| Q3 | **Recordable / DART / lost-time counts** for the period | free-text (ints) | "How many OSHA-recordable cases? Of those, how many DART cases? How many lost-time injuries? Enter the integer counts for the rates you selected." — counts are non-negative integers; if a count is unknown say so (the engine never guesses) | ELI-EVIDENCE | always |
| Q4 | **Total hours worked** in the period | free-text (number) MANDATORY | "Total employee-hours worked across the scope for this exact period (actual hours-to-date — NOT annualized). This is the denominator; **there is no rate without it.**" — **refuse to proceed if blank or ≤ 0**; never substitute a default, never annualize a partial period | ELI-EVIDENCE | always |
| Q5 | **Base convention** | MCQ | **OSHA standard (200,000 for TRIR/DART, 1,000,000 for LTIFR) — default** / (other conventions are out of scope for v1.0) — the base is an engine constant; this only confirms the convention, it is never user-arithmetic | ELI-SCORING | always |
| Q6 | **Industry benchmark** to compare against (optional) | free-text (optional) | "Optional — an industry benchmark rate to compare against, WITH its publishing body + year + sector (e.g. '2.7 — BLS SOII manufacturing, 2023'). Leave blank to skip." — a benchmark is only used if it carries its source + year; a bare number is recorded `[GAP]`, never invented | ELI-OBLIGATIONS | always |

**Branch map:** `hours-gate` (Q4 blank or ≤0 → refuse-no-denominator; **mandatory hard
refuse**); `india-recordability` (Q2b = India → Q2c + `KB-REG-IN-STATEFORMS`; **mandatory**);
`benchmark` (Q6 has source + year → `KB-DATA-TRIR-BENCHMARKS`); `severity-deferred` (if the
user asks for a severity rate → `[GAP]` "not computed (no validated engine in v1.0)"; **never
compute in-prompt** — D-03).

## Echo-back

After the last applicable question, **echo a captured-facts summary** (including the
recordability standard from Q2b) and confirm before calling the engine:
"Computing TRIR + DART + LTIFR for Plant 2, Q1 2026 (OSHA 29 CFR 1904 recordability):
3 recordables / 1 DART / 0 lost-time over 290,000 hours, OSHA base — correct?"

## Refuse-on-vague anchors

- **Q4 (hours) is a HARD refuse** — there is no rate without the denominator; never
  substitute a default, never annualize a partial period, never emit a fake `0.0`; surface
  the engine's `ValueError` honestly.
- **Q2 (scope + period) is the specificity anchor** — a context-less number is not
  defensible; record `[GAP]` if truly unavailable, never fabricate.

## Domain evidence types (ELI-EVIDENCE)

Period employee-hours (actual, not annualized) · recordable/DART/lost-time case counts
(aggregate, de-identified — no per-case line, no `<5` sub-group) · a sourced benchmark
(body + year + sector) · the recordability standard in force (OSHA / RIDDOR / India state
definition).
