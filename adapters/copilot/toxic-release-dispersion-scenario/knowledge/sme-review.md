---
sme-review:
  personas:
    - role: "Consequence-modelling / dispersion specialist (process-safety engineer)"
      expertise: "source-term derivation, release modes (catastrophic/continuous/instantaneous), neutral vs dense-gas dispersion, weather/stability (Pasquill class), toxic endpoints (ERPG/AEGL/IDLH), the bowtie/LOPA/QRA consequence interface"
      lens: "is this honest SCENARIO FRAMING for the modelling team — or has a quantitative result been smuggled in"
---

# SME Review & Sign-off — toxic-release-dispersion-scenario

This is the family's deliberately most omit-heavy skill — assistive-only, it captures the
source term and hands off; it never models. One lens suffices: a consequence-modelling /
dispersion specialist whose single job is to confirm the output is honest scenario framing for
the modelling team and that no quantitative result has been smuggled in. The persona **narrows**
the Chemical-Process-Safety sector slot that extends the generic **HSE-SME-Reviewer** hook
(`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-
only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Source term captured, **not computed** — substance, inventory-at-risk, release mode, hole size/duration recorded from the user; a release **rate** derived from first principles without user input is a FLAG.
- [ ] No invented dispersion distance or concentration — any un-modelled distance/concentration is `[GAP]`, routed to PHAST/ALOHA + a competent person. An invented quantitative result presented as if modelled is **hard-gate-adjacent** (escalate).
- [ ] Weather / atmospheric stability held as an explicit assumption — an implied stability class or wind speed is flagged `[ASSUMPTION]`, never asserted as fact.
- [ ] Receptors and the toxic endpoint named, not optimistic — on-site/public/environment receptors listed and the endpoint basis (ERPG/AEGL/IDLH) named for the modeller; silently assuming "no public receptor" is a FLAG.
- [ ] Consequence band qualitative only — the `risk_matrix` output is the consequence-axis band, explicitly *not* a modelled severity; a band dressed up as a modelled outcome is a FLAG.
- [ ] Downstream owners named — the consequence side handed to `bowtie-builder` and `lopa-worksheet` by name (SCOPE-OUT); a scenario that closes out the study itself is a FLAG.

## Sign-off note
SME review: ran (persona: Consequence-modelling / dispersion specialist); this is **decision-
support only** — scenario framing for a competent-person study, NOT a modelled result. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
