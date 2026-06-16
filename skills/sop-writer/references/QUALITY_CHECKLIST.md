# Pre-output Quality Checklist — sop-writer

The self-check loop the Workflow runs at step 7, before assembling the branded SOP.
The Critic/QA subagent re-runs this adversarially. A `[ ]` that cannot be ticked is a
`[GAP]` to resolve or an `[ASSUMPTION]` to flag — never silently ship.

## Specificity (the core value — both task AND steps)

- [ ] Names the **actual task/operation/asset** (not "machine maintenance", "general work").
- [ ] Scope **and boundaries** stated — what the SOP does NOT cover (and who owns that).
- [ ] The procedure is a **real, ordered, task-derived** step list — **no generic
      "work safely" / "follow all rules" boilerplate** (refuse it; record `[GAP]` if the
      user cannot supply real steps).

## Hierarchy of controls, embedded INTO the steps

- [ ] Every control ran through `KB-SNIP-HOC` + `controls.rank_controls` /
      `controls.validate_treatment` (the only A7 engine) — ranks are the engine's.
- [ ] Each **risk-bearing step** names its controls / PPE / checks / hold-points
      **inline** (embedded into the step, not appended as a flat end-list).
- [ ] The **higher-order controls the procedure operates within** (isolation, lock-out,
      guard, ventilation) are surfaced up front and in the `hoc_table`.
- [ ] **No un-justified PPE/admin-only treatment** — if `ppe_admin_only` is True, a
      higher-order control was added OR an explicit justification recorded.

## Ingest-don't-overlap (compose with B1/B2)

- [ ] If a B1 RA / B2 JSA was supplied, it is **ingested and cross-referenced by id** —
      its hazards/rated controls carried forward, **not re-scored** (no `risk_matrix`
      call, no risk register produced).
- [ ] If none was supplied, hazards were elicited inline **and** the flag that a formal
      RA/JSA is the more rigorous source was recorded.

## Defensibility (would it survive an audit)

- [ ] **Responsibilities** named by **role** (authorise / execute / verify) — no real names.
- [ ] **Required competencies/training** named per role (the "tied to training" bar).
- [ ] **Equipment / materials / permits** listed; any PTW / isolation regime linked.
- [ ] **Emergency / abnormal-condition provisions** present (stop conditions,
      hold-point-failure actions, rescue/spill/first-aid).
- [ ] **Revision/approval block** complete — id, version, effective date, author/
      reviewer/approver **roles**, review cycle. **If no review cycle given, "review on
      change (MoC-triggered) or at minimum annually" recorded + flagged `[ASSUMPTION]`.**

## Citations

- [ ] **ISO 45001 8.1** (operational control) cited — always; 8.1.2/8.1.4 as relevant.
- [ ] The ingested RA/JSA cited **by id**.
- [ ] India: state resolved (Q1a) before any state duty cited; **no SOP form number**
      fabricated (an SOP is an internal MS document).

## Document quality & de-identification

- [ ] Written to the **stated literacy level** (Q10, `KB-SNIP-AUDIENCE`) — register and
      sentence length match the reader.
- [ ] De-id pass complete **before** drafting; role labels only; **no name/phone/address
      in the approval or responsibilities blocks**; no re-identification key in the output.
- [ ] No conclusion rests on an unstated assumption (`[ASSUMPTION]` / `[GAP]` only).
