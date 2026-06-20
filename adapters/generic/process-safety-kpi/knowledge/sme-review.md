---
sme-review:
  personas:
    - role: "Process-safety-metrics SME (API RP 754 / CCPS process-safety KPIs)"
      expertise: "Tier-1/Tier-2 PSE threshold classification; normalized-rate denominator discipline; Tier-3/Tier-4 leading indicators; benchmarking with source+year; the PSE-vs-occupational-injury distinction."
      lens: "Is every event tiered correctly under API 754, is the rate denominator fail-loud rather than fabricated, and are leading and lagging indicators both represented?"
---

# SME Review & Sign-off — process-safety-kpi

This skill carries **one** specialized SME lens: a process-safety-metrics SME. It narrows
the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) to API RP
754 process-safety metrics; the generic **HSE-SME-Reviewer** hook is the inherited
fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**The denominator is fail-loud and the metric must not be conflated.** The failure modes
this lens guards are a fabricated rate when the work-hours denominator is missing/zero (the
count is still reported, but the rate reads `[GAP]`), a mis-tiered PSE count, an occupational
TRIR/LTIFR/DART metric conflated into the PSE counts (those route to
`incident-rate-calculator`), and a lagging-only dashboard with no Tier-3/Tier-4 leading
indicators. Every benchmark figure carries source + year; a PSE count or benchmark is never
invented.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each counted event is classified against the actual Tier-1 vs Tier-2 PSE threshold criteria (consequence / quantity), not lumped or mis-tiered.
- [ ] A missing/zero work-hours denominator yields `[GAP]`, never a fabricated rate; the count is still reported when the denominator is absent.
- [ ] rate = count × base hours ÷ total work hours — the base hours are stated and the arithmetic is consistent.
- [ ] Tier-3 (challenges to safety systems) and Tier-4 (operating discipline) leading indicators are framed alongside the lagging Tier-1/2 counts — not a lagging-only dashboard.
- [ ] No TRIR/LTIFR/DART occupational metric is conflated into the PSE counts — those route to `incident-rate-calculator`.
- [ ] Any benchmark figure carries source + year from KB-DATA; no invented industry comparison appears (FLAG).

## Sign-off note
SME review: ran (persona: Process-safety-metrics SME, API RP 754 / CCPS); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
