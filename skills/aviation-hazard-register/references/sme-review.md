---
sme-review:
  personas:
    - role: "Aviation SMS Safety Risk Manager / hazard-register custodian"
      expertise: "Annex 19 Pillar 2 hazard identification, the ICAO 5x5 Risk Classification Scheme, evidence-traced register discipline, hierarchy-of-controls ranking"
      lens: "would two assessors score this hazard identically, and does every entry trace to evidence with a real mitigation owner?"
modes:
  register-entry:
    detected_by: "Q1 — Build a new register or add hazards (the produced hazard register entry + structure, ICAO Annex 19 Pillar 2 with the 5×5 RCS)"
    floor:
      - id: haz-hazard-consequence-control-chain
        description: "Each entry traces hazard → consequence → existing controls → 5×5 classification → mitigation; flag any row that skips a stage (esp. a hazard with no consequence or a rating with no existing-control baseline)"
        anchors: ['consequence', 'existing control', 'mitigation']
        min_matches: 2
      - id: haz-icao-5x5-classified
        description: "The 5×5 rating comes from the ICAO MatrixConfig (KB-DATA-AVI-RISK-MATRIX), consistent with its severity×likelihood pair — not an eyeballed band"
        anchors: ['\b5.?5\b', 'severity', 'likelihood']
        min_matches: 2
      - id: haz-residual-rescored
        description: "Residual risk is re-scored after mitigation and the movement reported — a register that never scores residual is incomplete"
        anchors: ['residual', 're.?scor', 'after mitigation', 'target risk']
        min_matches: 1
      - id: haz-evidence-traced
        description: "Each hazard is evidence-traced to an occurrence report / audit finding / FDM-FOQA summary; an asserted hazard with no evidence is [GAP]-flagged, not silently accepted"
        anchors: ['evidence', 'occurrence', 'audit', 'FDM']
        min_matches: 1
      - id: haz-mitigations-hoc-ranked
        description: "Mitigations are HoC-ranked and any PPE/admin-only mitigation carries a justification or escalation — a briefing card is never accepted alone for a Hazardous consequence"
        anchors: ['hierarchy of controls', '\bPPE\b', 'higher.order', 'briefing card']
        min_matches: 1
      - id: haz-mitigation-owner-dated
        description: "Each mitigating action has a named role owner and a due date (validated via smart_actions)"
        anchors: ['owner', 'due', 'action']
        min_matches: 2
      - id: haz-reporter-confidentiality
        description: "Names in source occurrence reports are scrubbed to role labels — a hazard narrative that re-identifies the reporter is a de-id hard-fail, distinct from a FLAG"
        anchors: ['role label', 'de.identif', 'scrub', 'confidential']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The high-severity hazard with no bridge** — a Hazardous/Occasional (or worse) entry is
  left on an acknowledged-inadequate control (a briefing card) with the real upgrade dated
  far out and no interim measure and no acceptable-for-now statement for the gap period.
- **The band with no components** — a risk band is asserted ("Medium", "High") without the
  severity and likelihood values that produced it shown, so a reviewer cannot check the score
  or re-derive the residual.
- **Occurrence-history silence** — the register entry never confirms whether the hazard has
  prior-occurrence or industry history (bird-strike rates on that route/season), so the
  likelihood rests on judgement with no data trail.

## Sign-off note
SME review: ran (persona: Aviation SMS Safety Risk Manager — Annex 19 Pillar 2); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person (aviation-SME) sign-off**, and it never outputs the affirmative claim
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation) are a separate enforcement class.
