# Pre-output Quality Checklist — Leading/Lagging KPI Framework

> The pre-output validation gate the Workflow runs before producing any output. The SME
> Review & Sign-off (HSE Performance / Assurance Manager) runs alongside it; a
> de-identification leak is a non-waivable hard-fail.

Before producing any output, validate the draft against this gate:

- [ ] **Balance** — the set has **both** leading and lagging indicators per ISO 45001:2018
  clause 9.1; a lagging-only set (e.g. TRIR alone) is flagged and rebalanced, not presented.
- [ ] **Definition** — **every** indicator carries formula · source · frequency · owner ·
  target; no bare indicator name survives.
- [ ] **Anti-gaming** — any countable target (e.g. an incident count) is paired with a
  quality/assurance safeguard; a gameable target with no safeguard is flagged (defensibility).
- [ ] **Rates** — lagging rates are computed by `incident_rates` to standard definitions
  (anchors TRIR 2.07 / LTIFR 6.00); a missing work-hours denominator is `[GAP]`, never a
  fabricated figure.
- [ ] **Maturity** — the leading/lagging mix is matched to culture maturity; targets are
  risk-matched and stretch-but-credible.
- [ ] **Road-safety branch** (road/transport/fleet scope) — built from
  `KB-DATA-ROAD-SAFETY-INDICATORS`, cites ISO 39001:2012, each indicator defined; stays
  one skill (no second build, no fabricated form/rule number).
- [ ] **Distinctness** — the framework *designs* the set; it does not *compute* a given
  rate (`incident-rate-calculator`) or own the API RP 754 / ICAO Annex 19 tiers
  (`process-safety-kpi` / `aviation-spi-spt-framework`) — referenced as exemplars only.
- [ ] **Citation** — clause 9.1 (ISO 45001:2018) + each indicator definition cited; ISO
  39001:2012 on the road-safety branch; every benchmark figure carries source + year.
- [ ] **Owner + date** — every action / target has a named owner (role label) and a
  target/review date.
- [ ] **De-identification** — pass complete BEFORE designing; metrics are aggregate; any
  per-person/per-team breakdown applies `<5` small-cell suppression; no identifier leak and
  no embedded re-identification key.
