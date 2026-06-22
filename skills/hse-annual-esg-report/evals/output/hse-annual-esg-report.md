# Annual ESG Occupational Health & Safety Disclosure — Acme Plc, FY2025

**Disclosure type:** Annual ESG OH&S disclosure for external publication (board pack + sustainability report section).
**Reporting entity & period:** Acme Plc — FY2025 (1 Jan–31 Dec 2025).
**Reporting boundary:** Operational control. **Workforce coverage:** own-workforce AND non-employee/contractor populations reported separately (ESRS S1 mandates the split); each rate on its own hours-worked denominator.
**Frameworks:** GRI 403 (Occupational Health & Safety 2018) · SASB workforce-H&S metrics · ESRS S1-14 (own workforce, CSRD). Disclosure crosswalk reused from `KB-STD-ESG-GRI403` — no duplicate index minted.
**Assurance intent:** Limited assurance (negative conclusion). **Materiality:** double materiality (impact on workers + financial) — own-workforce and contractor H&S assessed as material.
**Clause anchor:** ISO 45001 clause 9.1 (monitoring, measurement, analysis and performance evaluation) made external.

> **Disclaimer.** Decision-support / pre-assurance draft. This disclosure is prepared for assurance and publication; it precedes — and never replaces — the independent assurance engagement and the competent-person review. It is not a limited or reasonable assurance opinion and must not be read as a final assured, audited, or legal document. An ESG / Sustainability Assurance Specialist and a competent person must review it before publication.

## 1. De-identification & aggregation status (strictest external-publication tier)

The de-identification pass ran **FIRST**, before any drafting. All injury/illness figures are **aggregated to the reporting boundary** — no individual incident is narrated with a date, location, or injury detail, and no individual is named or made identifiable. **Any injury/illness category of fewer than 5 individuals is suppressed**, and **secondary suppression** is applied so a suppressed cell cannot be back-calculated from a published total or the remaining cells. Denominators and boundaries are defined so totals cannot be reverse-engineered to a small cell. No re-identification key appears in this document.

## 2. Basis of preparation & data quality

Each figure below carries its **reporting boundary**, its **workforce population**, its **denominator**, and its **definition + source + period**. A figure with no stated boundary or denominator is not assurable and is not published. Lagging rates are computed deterministically by the `incident_rates` engine from recordable counts and hours worked, to standard OSHA/BLS recordkeeping definitions — not estimated in prose.

## 3. Lagging OH&S figures (GRI 403-9 / 403-10 · ESRS S1-14)

| Disclosure | Figure | Population | Denominator (basis) | Definition / source |
|---|---|---|---|---|
| GRI 403-9 — recordable injury rate (TRIR) | 2.07 per 200k hrs | Own-workforce | 14.5M hours worked | OSHA recordable / 200k hrs (incident_rates) |
| GRI 403-9 — lost-time injury rate (LTIFR) | 6.00 per 1M hrs | Own-workforce | 14.5M hours worked | lost-time cases / 1M hrs (incident_rates) |
| GRI 403-9 — recordable injury rate (TRIR) | 2.41 per 200k hrs | Non-employee / contractor | 3.1M contractor hrs | OSHA recordable / 200k hrs (incident_rates) |
| GRI 403-9 — fatalities | 0 (all populations) | All | count | aggregated; per-site cells <5 suppressed |
| GRI 403-10 — work-related ill health | aggregated | All | headcount-covered | <5 cells suppressed + secondary suppression |

Rates are per a stated denominator (not small counts). The fatality figure of 0 is reported at the all-populations level only; any single-site cell that would fall below 5 is aggregated to the all-sites total with secondary suppression so no single-site value is back-calculable. Comparators (BLS SOII sector figures) carry source + year, or are recorded `[GAP]` — never invented.

## 4. ESG disclosure index (reused crosswalk — `KB-STD-ESG-GRI403`)

| Framework code | OH&S disclosure | Where reported | Status |
|---|---|---|---|
| GRI 403-1 | OH&S management system (ISO 45001) | Governance section | Disclosed |
| GRI 403-2 | Hazard ID, risk assessment, incident investigation | Process section | Disclosed |
| GRI 403-4 | Worker participation & consultation | Governance section | Disclosed |
| GRI 403-8 | Workers covered by the OH&S management system | Coverage table | Disclosed |
| GRI 403-9 / SASB / ESRS S1-14 | Work-related injuries (rates) | §3 lagging figures | Disclosed |
| GRI 403-10 / ESRS S1 | Work-related ill health | §3 lagging figures | Disclosed (aggregated) |
| GRI 403-3 | Occupational health services | — | **[GAP]** — data not collected this period |

Every claimed GRI 403 / SASB / ESRS S1 disclosure is present, or its absence is recorded `[GAP]` and not papered over. A claimed-but-absent required disclosure would be a `regulatory_citation_accuracy` hard-fail; here the single gap (403-3) is disclosed honestly with a forward commitment to close it.

## 5. Assurance level & materiality

- **Assurance level:** limited (negative conclusion) — evidence rigour set accordingly. The disclosure is structured so an assurance provider can trace each figure to its definition, denominator, source and period.
- **Materiality:** double materiality — own-workforce and contractor OH&S is material on both impact (worker harm) and financial grounds; the materiality basis is stated.

## 6. Forward commitments (hierarchy of controls; owned + dated)

| # | Commitment | Tier | Owner (role) | Due |
|---|---|---|---|---|
| C-1 | Extend recordable-injury hours-worked capture to all contractor populations so every contractor rate carries its own denominator (and add 403-3 occupational-health-services data, closing the `[GAP]`). | Administrative (data system) | HSE Data Lead | Q2 FY2026 |
| C-2 | Implement engineered controls for the period's leading injury mechanism ahead of any PPE/admin-only measure, per `KB-SNIP-HOC`. | Engineering | Operations Director | Q3 FY2026 |

Commitments are narrated via the hierarchy of controls (higher-order before PPE/admin) and recorded as owned + dated actions (`smart_actions`); each owner is a role label.

## 7. Output & provenance

A branded `report.json` (period-figures shape) renders the DOCX + PDF disclosure via the shared report engine. The report carries the de-id/aggregation notice (§1) and the decision-support / pre-assurance disclaimer above. This disclosure does not assert that the figures have been assured or audited; the assurance opinion is the assurance provider's, and the sign-off the competent person's.
