---
sme-review:
  personas:
    - role: "HSE Performance / Assurance Manager"
      expertise: "ISO 45001:2018 clause 9.1 monitoring, measurement, analysis & performance evaluation; balanced leading/lagging indicator design; per-indicator definition (formula·source·frequency·owner·target); anti-gaming guardrails against under-reporting; target-setting matched to culture maturity; ISO 39001:2012 road-safety performance indicators; aggregate-metric de-identification (<5 small-cell suppression)."
      lens: "Is the set BALANCED (not lagging-only) per clause 9.1, is EVERY indicator fully defined, is any countable target paired with an anti-gaming safeguard, are lagging rates computed to standard definitions (not invented), and does the framework stay distinct from incident-rate-calculator (computes) and process-safety-kpi (API RP 754)?"
---

# SME Review & Sign-off — leading-lagging-kpi-framework

This skill carries **one** specialized SME lens: an **HSE Performance / Assurance Manager**.
It narrows the family's HSE-leadership archetype (`KB-SNIP-ARCHETYPES`) to ISO 45001 clause
9.1 performance evaluation and balanced KPI design; the generic **HSE-SME-Reviewer** hook
is the inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC /
no PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**The set must be balanced, every indicator defined, and no target gameable.** The failure
modes this lens guards are a **lagging-only** scorecard (TRIR alone — a reactive-only
clause-9.1 picture), an indicator with **no definition** (a bare name with no
formula·source·frequency·owner·target is not a KPI), a **gameable** metric (a raw incident
count as a target → under-reporting) with **no quality/assurance safeguard**, a lagging
**rate invented** rather than computed by `incident_rates` to standard definitions, the
road-safety branch **citing the wrong standard** (it is ISO 39001:2012) or being spun off
into a **second build** (it stays one skill, the single home), and the framework **subsuming**
`incident-rate-calculator` / `process-safety-kpi` instead of referencing them as exemplars.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The set is **balanced** — leading *and* lagging are both represented per ISO 45001:2018 clause 9.1; a lagging-only set is flagged, not presented.
- [ ] **Every** indicator carries a full definition: formula · source · frequency · owner · target — no bare indicator name.
- [ ] Any **countable** target (e.g. an incident count) is paired with an **anti-gaming safeguard** (a reporting-quality / assurance measure); a gameable target with no safeguard is flagged (defensibility).
- [ ] Lagging **rates** are computed to standard definitions via `incident_rates` (anchors TRIR 2.07 / LTIFR 6.00) — a missing work-hours denominator is `[GAP]`, never a fabricated figure.
- [ ] The leading/lagging **mix** is matched to culture maturity (reactive → developing → mature shifts toward leading) and every benchmark figure carries source + year.
- [ ] On a road/transport/fleet scope, the **road-safety branch** is built from `KB-DATA-ROAD-SAFETY-INDICATORS` and cites **ISO 39001:2012**; it stays **one skill** (the single home — no second road-safety build, no fabricated form/rule number).
- [ ] The framework stays **distinct** — it *designs* the set; it does NOT *compute* a given rate (`incident-rate-calculator`) or own the API RP 754 / ICAO Annex 19 tiers (`process-safety-kpi` / `aviation-spi-spt-framework`), referencing them as exemplars only.
- [ ] Metrics are **aggregate**; any per-person/per-team breakdown applies the `<5` small-cell suppression with secondary suppression (no re-identification).

## Sign-off note
SME review: ran (persona: HSE Performance / Assurance Manager, ISO 45001 9.1 / ISO 39001);
this is **decision-support only**. It **precedes — and never replaces — the human
competent-person sign-off**, and it never outputs the literal sign-off phrase a human
reviewer gives. A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class owned by the automated harness.
