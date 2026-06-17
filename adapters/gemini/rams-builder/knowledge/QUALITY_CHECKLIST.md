# Pre-output Quality Checklist — RAMS (Risk Assessment + Method Statement)

The self-check loop (Workflow step 10) before any output. Every box must hold; a
failure is a defect the Critic/QA pass must catch.

## Specificity (the core value)

- [ ] The **construction activity** (Q2) is specific and named — not "general
      construction works".
- [ ] The **sequence of works** (Q-S) is a real ordered sequence (set-up → … →
      clear-down), not a flat list — the MS is built from it.
- [ ] Every hazard names **what** is hazardous and **who/what is exposed** (own
      operatives, other trades, the public adjacent to the site).

## Risk assessment (RA half)

- [ ] Every hazard scored via the A7 `risk_matrix` engine (initial band), each carrying
      an **RA-id** (RA-01…).
- [ ] Every control HoC-ranked via `controls.rank_controls`; **no un-justified
      lower-order-only (PPE/admin-only) treatment** — a higher-order control added, or an
      explicit justification recorded.
- [ ] Residual re-scored via `risk_matrix.score` + `residual_delta`; any residual
      High/Critical flags additional controls or a hold-point.

## Method statement (MS half)

- [ ] The MS is **sequenced** — one ordered step per row, with work-step description,
      plant/equipment, competencies/cards, permits, and step controls.
- [ ] No invented certification — a card the user did not state is recorded `[GAP]`.

## RA↔MS cross-reference (bidirectional — the load-bearing coupling)

- [ ] **Every method step is cross-referenced to its RA rows** (the RA-refs column) — no
      method step whose hazards are absent from the RA.
- [ ] **Every RA hazard is addressed by a method step** — no orphan RA hazard.

## Emergency, competence & briefing

- [ ] Activity-specific **emergency & rescue arrangements** present (a rescue plan for
      at-height / excavation / confined-space work; not just "call 999").
- [ ] **Named competent persons** present for each step that needs one (the user-supplied
      Q-C assignments).
- [ ] The **briefing / acknowledgement table ships with empty signature rows** (never
      pre-populated operative names).

## Actions, regulatory basis & de-id

- [ ] Every action SMART — named owner + ISO due date + measure + hazard link
      (`smart_actions.validate_register`); no anonymous/undated actions.
- [ ] Every citation traced to the KB: ISO 45001 6.1.2/8.1.2 always; **UK** → CDM 2015
      Reg 13/15 + CPP; **India** → BOCW + the **resolved state** form (state confirmed;
      never a national number; unseeded state → `[GAP]`).
- [ ] De-identification pass complete BEFORE drafting; **input-derived names scrubbed to
      roles**; the **deliberately-supplied competent persons stay named** in the sign-off
      (the de-id exception); no re-identification key in the output.
- [ ] No conclusion rests on an unstated assumption — `[ASSUMPTION]` / `[GAP]` recorded.
