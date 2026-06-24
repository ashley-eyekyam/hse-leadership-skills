# Balanced leading/lagging KPI design — `leading-lagging-kpi-framework`

Grounds in `KB-SNIP-KPI-DESIGN` (method) + `KB-DATA-LEADING-INDICATORS` (the single-source
catalogue) + `KB-SNIP-LEADERSHIP-CLAUSE-MAP` (clause 9.1 ownership), and — on a
road/transport/fleet scope — `KB-DATA-ROAD-SAFETY-INDICATORS` (ISO 39001:2012). Lagging
**rates** are computed by `scripts/hse_components/incident_rates` to standard definitions
(anchors TRIR 2.07 / LTIFR 6.00), never invented. Cited as **method, not law**.

> The single load-bearing lever: a **balanced** set (leading + lagging) against **ISO
> 45001:2018 clause 9.1**, with **every indicator fully defined** and **no gameable target
> without a safeguard**.

## Steps

1. **Bound** the scope/level (organisation · function · site · fleet) and the reporting
   period. The named subject is the specificity anchor — refuse a generic "build KPIs".
2. **Design the balanced set** — pair **lagging** outcomes (TRIR, LTIFR, DART, severity
   rate, fatalities — *computed* by `incident_rates`) with **leading** predictors (%
   planned inspections completed, near-miss reporting rate, training completion, action
   close-out rate, BBS percent-safe, gemba-commitment closure, PTW compliance) resolved
   from `KB-DATA-LEADING-INDICATORS`. **A lagging-only set fails the balance gate** (ISO
   45001 clause 9.1 demands monitoring *and* measurement *and* analysis, not a
   reactive-only picture) — name the missing leading half and refuse to present a
   TRIR-only scorecard.
3. **Define every indicator** — each carries **formula · source · frequency · owner ·
   target**. An indicator with no definition fails specificity; a named target with no
   formula or owner is not a KPI.
4. **Apply the anti-gaming guardrails** — avoid metrics that incentivise **under-reporting**
   (a raw **incident count** as a target suppresses reporting). Pair any countable target
   with a **quality/assurance safeguard** (e.g. an audited reporting-quality measure
   alongside the count). **A gameable metric with no safeguard fails the defensibility
   gate.**
5. **Set targets by maturity** — match the leading/lagging **mix** to culture maturity:
   reactive → developing → mature shifts the balance **toward leading**. Targets are
   risk-matched and stretch-but-credible.
6. **Road-safety branch** (D-01) — when the scope is **road / transport / fleet**, add the
   ISO 39001:2012 road-safety indicator set from `KB-DATA-ROAD-SAFETY-INDICATORS`
   (speeding · harsh-braking / harsh events · journey management · vehicle-defect rate ·
   driver-hours compliance; + seatbelt / helmet use where occupants / two-wheelers are in
   scope), each with its `leading|lagging` tag · formula · source · target. This is **one
   skill** (an in-skill branch), the single home of road-safety KPIs — LEAD-06 owns the
   *indicator*; the LOG-01 engine / SUB-03 fatigue-index own the *computation* of
   driver-hours, which is cross-referenced, not computed here. No fabricated form/rule
   number is minted.
7. **Validate the rates** — any lagging rate is computed by `incident_rates` to standard
   definitions; a missing work-hours denominator is `[GAP]`, never a fabricated figure.
8. **Cite** — clause 9.1 (ISO 45001:2018) + the indicator definitions; ISO 39001:2012 on
   the road-safety branch; every benchmark figure carries source + year from KB-DATA.

## Discipline (load-bearing)

- **Balance:** a lagging-only set (e.g. TRIR alone) is refused — pair lagging outcomes with
  leading predictors (clause 9.1 fidelity / specificity).
- **Anti-gaming:** a gameable metric (raw incident count as a target) with **no safeguard**
  is refused (defensibility). Pair any countable target with a quality/assurance safeguard.
- **Per-indicator definition:** formula · source · frequency · owner · target — mandatory
  on each; a bare indicator fails specificity.
- **Distinctness (SC-2):** this skill **designs / normalises** the set. It does NOT
  *compute* a given rate — that is **`incident-rate-calculator`**. It does NOT own the API
  RP 754 process-safety tiers — that is **`process-safety-kpi`** — nor the ICAO Annex 19
  aviation SPIs — that is `aviation-spi-spt-framework`. Reference these as exemplars; never
  subsume them.
- **No fabrication:** lagging rates via `incident_rates`; benchmarks cited source + year;
  no minted form/rule numbers on the road-safety branch.
