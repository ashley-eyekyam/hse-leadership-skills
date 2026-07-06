---
sme-review:
  personas:
    - role: "Aviation Safety-Assurance / SPI-SPT performance specialist"
      expertise: "Annex 19 Pillar 3 safety performance monitoring, leading vs lagging indicator design, alert/target threshold setting, ALoSP alignment to a State Safety Programme"
      lens: "is every indicator measurable, threshold-bearing, owned, and tied to a real hazard/objective — or is it a vanity metric?"
modes:
  spi-framework:
    detected_by: "Q1 — Design a new SPI/SPT set (the produced Safety Performance Indicator / Target framework, ICAO Annex 19 Pillar 3 / SSP ALoSP)"
    floor:
      - id: spi-alert-and-target
        description: "Every SPI carries BOTH a defined alert level AND a target level (the SPT) — an SPI with no threshold is unmeasurable"
        anchors: ['alert level', 'target', '\bSPT\b']
        min_matches: 2
      - id: spi-maps-to-hazard
        description: "Every SPI maps to an owning hazard or safety objective — an orphan indicator that tracks nothing in the hazard register is flagged"
        anchors: ['hazard', 'objective', 'maps? to', 'linked to']
        min_matches: 1
      - id: spi-leading-lagging-balanced
        description: "The leading/lagging mix is balanced — flag an all-lagging (outcome-only) set with no leading precursors"
        anchors: ['leading', 'lagging']
        min_matches: 2
      - id: spi-thresholds-data-derived
        description: "Thresholds are derived from data, not invented — alert levels reference baseline rate/occurrence data (incident_rates), quoting source+year; an absent figure is [GAP], never a fabricated number"
        anchors: ['baseline', 'occurrence data', 'incident rate', '\[GAP\]']
        min_matches: 1
      - id: spi-owner-named
        description: "Each SPI has a named role owner / accountable monitor (not just an owning hazard) — a metric nobody owns is never actioned"
        anchors: ['owner', 'accountable', 'monitor']
        min_matches: 1
      - id: spi-measurement-basis-period
        description: "Each SPI states its measurement basis, period, and data source (monthly / quarterly / rolling-12) so the indicator is reproducible"
        anchors: ['measurement', 'period', 'monthly', 'quarterly', 'rolling']
        min_matches: 1
      - id: spi-review-feeds-srb-alosp
        description: "A review cadence is stated and the SPIs feed the SRB and the SSP ALoSP — an indicator set that is never reviewed or escalated is inert"
        anchors: ['review', '\bSRB\b', 'ALoSP', '\bSSP\b']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The threshold with no inputs** — alert and target levels are stated as clean round
  numbers with no baseline, no data source, and no derivation, so they are invented rather
  than data-derived; where the baseline is genuinely absent the honest form is a [GAP], not a
  fabricated figure.
- **The breach with no response** — an SPI is defined with an alert level but the framework
  never states what happens when it is breached: the escalation to the SRB, the interim
  response, and the owner who acts. A tripwire with no wired response is decorative.
- **Record identity & basis** — an SPI is specified without its measurement period, counting
  definition, or data source, so two analysts would compute it differently and it cannot be
  reproduced quarter to quarter.

## Sign-off note
SME review: ran (persona: Aviation Safety-Assurance / SPI-SPT specialist — Annex 19
Pillar 3); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person (aviation-SME) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
