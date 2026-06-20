---
sme-review:
  personas:
    - role: "Aviation SMS Safety Risk Manager / hazard-register custodian"
      expertise: "Annex 19 Pillar 2 hazard identification, the ICAO 5x5 Risk Classification Scheme, evidence-traced register discipline, hierarchy-of-controls ranking"
      lens: "would two assessors score this hazard identically, and does every entry trace to evidence with a real mitigation owner?"
---

# SME Review & Sign-off — aviation-hazard-register

This skill carries **one** SME lens, narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the "hazards rated + HoC-mitigated" + 5×5 RCS clauses) to the hazard
register. The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only,
owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every entry traces hazard → consequence → existing controls → 5×5 classification → mitigation — flag any row that skips a stage (esp. a hazard with no consequence, or a rating with no existing-control baseline).
- [ ] The 5×5 rating came from `risk_matrix.score()` with the ICAO MatrixConfig, not an eyeballed band — flag any rating inconsistent with its severity×likelihood pair (`KB-DATA-AVI-RISK-MATRIX`).
- [ ] Residual risk is re-scored after mitigation and the movement reported (`risk_matrix.residual_delta()`) — a register that never scores residual is incomplete.
- [ ] Each hazard is evidence-traced to an occurrence report / audit finding / FDM-FOQA summary; an asserted hazard with no evidence is `[GAP]`-flagged, not silently accepted.
- [ ] Mitigations are HoC-ranked and any PPE/admin-only mitigation carries a justification or escalation.
- [ ] Reporter/crew confidentiality — names in source occurrence reports are scrubbed to role labels; a hazard narrative that re-identifies the reporter is flagged (a leak is a de-id hard-fail, distinct from a FLAG).

## Sign-off note
SME review: ran (persona: Aviation SMS Safety Risk Manager — Annex 19 Pillar 2); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person (aviation-SME) sign-off**, and it never outputs the affirmative claim
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation) are a separate enforcement class.
