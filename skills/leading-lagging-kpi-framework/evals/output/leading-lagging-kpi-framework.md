# Leading & Lagging KPI Framework — Manufacturing Division (Org-X), FY24

**Scope / level:** Manufacturing division (Org-X) — division-level performance evaluation.
**Reporting period:** FY24 (quarterly review cadence).
**Standard basis:** ISO 45001:2018 clause 9.1 (monitoring, measurement, analysis & performance evaluation), mapped via `KB-SNIP-LEADERSHIP-CLAUSE-MAP` (this skill is the clause-9.1 owner). Method: `KB-SNIP-KPI-DESIGN`; catalogue: `KB-DATA-LEADING-INDICATORS`.
**Culture maturity:** Developing → the leading/lagging mix is weighted toward leading.
**Distinctness:** this framework *designs / normalises* the indicator set. Lagging **rates** are *computed* by `incident_rates` (anchors TRIR 2.07 / LTIFR 6.00) — a *computation* request routes to `incident-rate-calculator`; API RP 754 process-safety tiers are owned by `process-safety-kpi` (referenced as an exemplar, not subsumed).

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before adoption. Not legal advice.

## 1. De-identification status
De-id pass ran FIRST. No personal identifiers were present in the intake; indicator owners are carried as role labels only (Safety Lead, Operations Manager, Training Coordinator, Permit Authority). Metrics are aggregate; any per-person or per-team breakdown smaller than five is suppressed with secondary suppression. No names, contact details, IDs, addresses, or small cells appear in this record, and no re-identification key is embedded.

## 2. Balance check (ISO 45001 clause 9.1)
The starting scorecard was **lagging-only** (TRIR + LTIFR). A lagging-only set is a reactive-only picture and **fails the balance gate** — clause 9.1 requires monitoring *and* measurement *and* analysis of performance, not outcome counting alone. The missing **leading** half is added below and the mix is weighted toward leading to suit a developing-maturity organisation.

## 3. Leading indicators (active / predictive)

Resolved from `KB-DATA-LEADING-INDICATORS`; each carries formula · source · frequency · owner · target.

| # | Indicator | Tag | Formula | Source | Frequency | Owner | Target |
|---|-----------|-----|---------|--------|-----------|-------|--------|
| L1 | % planned inspections completed | leading | (inspections completed ÷ inspections planned) × 100 | HSG65 active monitoring | Monthly | Safety Lead | 95% |
| L2 | Near-miss reporting rate | leading | near-misses reported ÷ exposure (per 100k hours) | HSG65 / OECD | Monthly | Safety Lead | Upward trend (no ceiling) |
| L3 | Training completion | leading | (competencies achieved ÷ competencies required) × 100 | HSG65 active monitoring | Quarterly | Training Coordinator | 100% for critical roles |
| L4 | Action close-out rate | leading | (actions closed on time ÷ actions due) × 100 | OECD / CCPS leading-indicator guidance | Monthly | Operations Manager | 90% on time |
| L5 | PTW compliance | leading | (permits audited compliant ÷ permits audited) × 100 | HSG65 active monitoring | Monthly | Permit Authority | 98% |

## 4. Lagging indicators (reactive / outcome)

Rates are **computed** by `incident_rates` to standard definitions — never invented; a missing work-hours denominator is `[GAP]`.

| # | Indicator | Tag | Definition source | Frequency | Owner | Target |
|---|-----------|-----|-------------------|-----------|-------|--------|
| G1 | TRIR | lagging | `incident_rates` standard definition (anchor 2.07) | Quarterly | Operations Manager | Reduce vs prior FY |
| G2 | LTIFR | lagging | `incident_rates` standard definition (anchor 6.00) | Quarterly | Operations Manager | Reduce vs prior FY |
| G3 | DART | lagging | `incident_rates` standard definition | Quarterly | Operations Manager | Reduce vs prior FY |

[GAP] FY24 work-hours denominator not supplied at design time — the TRIR/LTIFR/DART *rates* are computed once the division's total work hours are provided; the design does not fabricate a denominator.

## 5. Balance & maturity

- Leading indicators: 5 · Lagging indicators: 3 → balanced and weighted toward leading, suited to a **developing** maturity (per `KB-SNIP-KPI-DESIGN` target-setting-by-maturity). As maturity advances toward *mature*, shift further toward leading and tighten the targets.

## 6. Anti-gaming safeguards

| Indicator at risk | Gaming risk | Safeguard paired |
|-------------------|-------------|------------------|
| Near-miss reporting rate (L2) | A *low* count could be read as "good", incentivising under-reporting | Targeted as an **upward** trend with no ceiling; cross-checked against L1/L5 assurance audits so suppression shows as a divergence |
| Any raw incident-count target | A raw count target suppresses reporting | **Not used as a standalone target** — outcome performance is the *rate* (computed by `incident_rates`) read alongside the leading set, never a bare count to be minimised |

A gameable metric with no safeguard fails the defensibility gate and is not included.

## 7. Review cycle & clause-9.1 fidelity
Define every indicator (done above) → compute the lagging rates via `incident_rates` once hours are supplied → review balance and targets each quarter against maturity → analyse performance per ISO 45001:2018 clause 9.1 → feed the evaluated performance into management review. Owners are role labels with quarterly review dates.

## 8. Provenance
Designed per `KB-SNIP-KPI-DESIGN` + `KB-DATA-LEADING-INDICATORS`; clause mapping `KB-SNIP-LEADERSHIP-CLAUSE-MAP`; lagging rates via `scripts/hse_components/incident_rates`. SME review (HSE Performance / Assurance Manager) ran before this output — decision-support that precedes the human competent-person review.

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
