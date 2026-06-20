---
sme-review:
  personas:
    - role: "Asset-integrity / inspection engineer (API 510 pressure vessels / 570 piping / 580 RBI; PSM element (j))"
      expertise: "Equipment criticality ranking; risk-based inspection (RBI) interval defensibility; ITPM scheduling; integrity-operating-windows (IOWs); deficiency / fitness-for-service management."
      lens: "Is the inspection strategy genuinely risk-based with defensible intervals, and is no item silently assumed fit-for-service without an integrity basis?"
---

# SME Review & Sign-off — mechanical-integrity

This skill carries **one** specialized SME lens: an asset-integrity / inspection engineer.
It narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`)
to the asset-integrity / PSM element (j) program; the generic **HSE-SME-Reviewer** hook is
the inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**No item is fit-for-service without an integrity basis.** The failure mode this lens
guards is an item silently assumed fit with no inspection basis behind it — recorded
instead as `[GAP]`, never "fit for service". Risk-based intervals must trace to a stated
RBI basis (damage mechanism + rate); a class-specific inspection strategy (vessels →
thickness/CML, relief devices → test interval, tanks → API 653) applies. The inspection
authority / owner of the ITPM basis is the assistive-evidence anchor.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each item's criticality reflects consequence-of-failure × likelihood (age, service, corrosion, damage mechanism) — not nameplate size or age alone.
- [ ] Where risk-based intervals are used, they trace to a stated RBI basis (damage mechanism + rate); an interval with no basis is flagged.
- [ ] Any item lacking an integrity basis reads `[GAP]`, never "assumed fit".
- [ ] Integrity-operating-windows (IOWs) are defined for items whose process conditions drive degradation.
- [ ] Each open deficiency carries an interim-risk judgement AND a higher-order remediation control; a deficiency "controlled" by monitoring/administration alone is flagged.
- [ ] Every row carries equipment · criticality band · ITPM interval · deficiency status · named owner — no orphan rows (FLAG).

## Sign-off note
SME review: ran (persona: Asset-integrity / inspection engineer, API 510/570/580); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
