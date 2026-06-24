<!-- KB-SNIP-KPI-DESIGN -->
# Leading/lagging KPI design — balanced architecture + anti-gaming

**Fragment ID:** `KB-SNIP-KPI-DESIGN`
**This is prompt text, applied by the model — not a generator.** It is the method the
`leading-lagging-kpi-framework` skill applies to design a **balanced** cross-domain KPI architecture
against ISO 45001 clause 9.1. The curated indicator catalogue (each cited) is single-sourced in
`KB-DATA-LEADING-INDICATORS`; the LEAD-06 road-safety branch uses `KB-DATA-ROAD-SAFETY-INDICATORS`.
Lagging rates are **computed** by `incident_rates` (anchors TRIR 2.07 / LTIFR 6.00), not invented.
Cited as **method, not law**.

> Source: ISO 45001:2018 clause 9.1 (monitoring, measurement, analysis, performance evaluation) · HSE HSG65 active vs reactive monitoring · OECD / CCPS leading-indicator guidance (recognised method) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — balance leading and lagging, define every indicator

| Class | Examples | Discipline |
|---|---|---|
| **Lagging** (reactive/outcome) | TRIR, LTIFR, DART, severity rate, fatalities | computed by `incident_rates` to standard definitions (anchors TRIR 2.07 / LTIFR 6.00). **A lagging-only set fails the balance gate.** |
| **Leading** (active/predictive) | % planned inspections completed, near-miss reporting rate, training completion, action close-out rate, BBS percent-safe, gemba-commitment closure, PTW compliance | the predictive half of the balance; resolve from `KB-DATA-LEADING-INDICATORS`. |

### Per-indicator definition (mandatory each)

Every indicator carries **formula · source · frequency · owner · target**. An indicator with no
definition fails specificity — a named target with no formula or owner is not a KPI.

### Anti-gaming guardrails

- Avoid metrics that incentivise **under-reporting** — e.g. raw incident count as a target suppresses
  reporting. Pair any countable target with a **quality/assurance safeguard**.
- A gameable metric with no safeguard fails the defensibility gate.

### Target-setting by maturity

Match the leading/lagging **mix** to culture maturity: reactive → developing → mature shifts the
balance **toward leading**. Targets are risk-matched and stretch-but-credible.

## LEAD-06 distinctness (SC-2)

LEAD-06 **designs/normalises** the indicator set. It is distinct from:

- `incident-rate-calculator` — **computes** given rates (the calculator, not the designer);
- `process-safety-kpi` — API RP 754 tiered process-safety indicators (a domain **exemplar**);
- `aviation-spi-spt-framework` — ICAO Annex 19 SPI/SPT (a domain **exemplar**).

Reference these; **do not subsume** them.

## Road-safety EXTEND branch (D-01)

When the intake selects a road-transport scope, LEAD-06 adds the road-safety indicator set from
`KB-DATA-ROAD-SAFETY-INDICATORS` (ISO 39001:2012) — **the only home of road-safety KPIs**; LEAD-06
owns the *indicator*, LOG-01 owns the *engine*. This stays one skill (an in-skill branch).

## How the skill uses this fragment

`leading-lagging-kpi-framework` builds the balanced set from `KB-DATA-LEADING-INDICATORS` (+ the
road-safety branch where selected), defines every indicator (formula·source·frequency·owner·target),
applies the anti-gaming safeguards, and matches the mix to maturity — computing lagging rates via
`incident_rates`, never inventing a figure.
