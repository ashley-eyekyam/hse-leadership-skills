---
sme-review:
  personas:
    - role: "Aviation Safety-Assurance / SPI-SPT performance specialist"
      expertise: "Annex 19 Pillar 3 safety performance monitoring, leading vs lagging indicator design, alert/target threshold setting, ALoSP alignment to a State Safety Programme"
      lens: "is every indicator measurable, threshold-bearing, owned, and tied to a real hazard/objective — or is it a vanity metric?"
---

# SME Review & Sign-off — aviation-spi-spt-framework

This skill carries **one** SME lens, narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the "SPIs are real — every SPI has a defined alert/target level and an
owning hazard/objective" clause) to the SPI/SPT framework. The universal hard gates (de-id
leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and
are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every SPI carries BOTH a defined alert level AND a target level (the SPT) — an SPI with no threshold is unmeasurable; flag it.
- [ ] Every SPI maps to an owning hazard or safety objective — an orphan indicator that tracks nothing in the hazard register is flagged.
- [ ] Targets are realistic and the leading/lagging mix is balanced — flag an aspirational target with no baseline, or an all-lagging (outcome-only) set with no leading precursors.
- [ ] Thresholds are derived from data, not invented — alert levels reference baseline rate/occurrence data via `incident_rates`, quoting `KB-DATA-TRIR-BENCHMARKS` source+year; an absent figure is `[GAP]`, never a fabricated number.
- [ ] Each SPI has a named owner / accountable monitor (not just an owning hazard) — a metric nobody owns is never actioned.
- [ ] India ALoSP alignment — where India is in scope, SPIs align to the DGCA SSP's ALoSP expectations (`KB-REG-IN-DGCA`), cited not invented.

## Sign-off note
SME review: ran (persona: Aviation Safety-Assurance / SPI-SPT specialist — Annex 19
Pillar 3); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person (aviation-SME) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
