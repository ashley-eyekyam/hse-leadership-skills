---
sme-review:
  personas:
    - role: "ESG / Sustainability Assurance Specialist"
      expertise: "GRI 403 / SASB / ESRS S1 OH&S disclosure requirements; ISAE 3000 (Revised) and AA1000AS assurance engagements; reporting-boundary and consolidation concepts (operational / financial control, own-workforce vs non-employee split); per-metric data quality (definition, denominator, source, period, completeness); double materiality; and statistical-disclosure-control de-identification (small-cell <5 suppression + secondary suppression so totals cannot back-calculate a cell)."
      lens: "would a limited/reasonable-assurance provider sign this — is every figure boundary-stated and denominator-defined, is every claimed GRI 403 disclosure actually present, do the lagging rates match incident_rates standard definitions, can any suppressed small cell be reverse-engineered from a published total, and does the document avoid reading as a final assured or legal disclosure"
---

# SME Review & Sign-off — hse-annual-esg-report

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Every published figure carries its reporting boundary** (operational / financial / equity-share) AND its workforce split (own-workforce vs non-employee/contractors, per ESRS S1) — a figure with no stated boundary is not assurable and is rejected.
- [ ] **Every published rate carries its denominator + definition** (hours worked, the recordable basis), is sourced + period-bound, and the lagging rates (TRIR / DART / LTIFR / fatality rate) match the `incident_rates` standard definitions — a rate with no denominator/definition is rejected, never estimated.
- [ ] **Framework fidelity** — every claimed "GRI 403" / SASB / ESRS S1 disclosure is actually present (selected from the reused `KB-STD-ESG-GRI403` crosswalk); a claimed-but-absent required 403 disclosure is a citation hard-fail, recorded `[GAP]`, never papered over.
- [ ] **Strictest-tier de-id holds** — all injury/illness figures aggregated; no `<5` small cell published (especially fatalities/ill-health by site or demographic); **secondary suppression applied so no suppressed cell is back-calculable** from a published total or the remaining cells; no re-identification mapping in the document.
- [ ] **Assurance level + materiality stated** — the intended assurance level (limited / reasonable) is recorded so the evidence rigour matches it, and the double-materiality basis for reporting own-workforce H&S is stated.
- [ ] **Boundary held** — the disclosure carries a decision-support / pre-assurance disclaimer and a de-id/aggregation notice, and never reads as a final assured, audited, or legal document.

## Sign-off note
SME review: ran (persona: ESG / Sustainability Assurance Specialist); this is
decision-support that **precedes and never replaces** the assurance engagement or the
human competent-person review, and it never asserts that the disclosure has been assured,
audited, or finally approved. A FLAG it raises is recorded, never merge-blocking.
