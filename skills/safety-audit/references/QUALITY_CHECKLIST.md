# Pre-output Quality Checklist — safety-audit

Run this self-check (Workflow step 7) before assembling the report. Every box
must be ticked or `[GAP]`-flagged; the Critic/QA pass re-checks it adversarially.

## Scope & criteria
- [ ] The audited **scope/boundary is specific** (Q-Scope) — not "general site
      audit"; the report names the actual subject and its boundary.
- [ ] The **criteria set is declared** (Q-Crit): ISO 45001 clauses / a regulatory
      regime / the user's custom checklist — and resolved into a walkable list.
- [ ] The **audit type** (Q-Type) and methodology (interview / document /
      observation / sampling) are stated.
- [ ] No criterion was **invented** — `[GAP]` where the criteria set is incomplete.

## Evidence & findings (the defensibility core)
- [ ] **Every criterion is assessed** — or `[GAP]`-flagged as insufficient
      evidence. No criterion silently skipped.
- [ ] **Every finding is classified** with the 4-class scheme (Conformity /
      NC-Major / NC-Minor / Observation / Opportunity).
- [ ] **Every finding traces to specific objective evidence** — a document id,
      observation, interview-role, or record. No unsupported "conformity" and no
      unsupported "nonconformity".
- [ ] A criterion with **absent evidence is a nonconformity / "insufficient
      evidence" — never a silent conformity.**
- [ ] **Every nonconformity is risk-rated** via the `risk_matrix` engine (band is
      the engine's, not prose).

## Conformity rating
- [ ] The conformity rating is **computed from the per-finding ratings** (count by
      class, conformity %, highest residual nonconformity band) — not asserted.

## Corrective actions + CAPA register (the B7 seam)
- [ ] Every nonconformity (and any actioned observation) has corrective actions
      **HoC-ranked** via `controls.rank_controls` / `validate_treatment`.
- [ ] No **un-justified lower-order-only** treatment — `ppe_admin_only=True`
      either gains a higher-order control or carries an explicit justification.
- [ ] Every action is **SMART**: named (role-label) owner + ISO due date +
      measure, linked to its **finding id**.
- [ ] The CAPA register passes `smart_actions.validate_register` — no anonymous,
      undated, or unlinked actions; the schema is B5's verbatim
      (`{action, owner, due, measure, links_to_cause, hoc_tier}`).

## Citation & de-id
- [ ] Every cited criterion **traces to the KB** — ISO 45001 9.2 as the method
      always; the audited clauses / the jurisdiction fragment for the criteria.
      India: the **resolved state form** (never a national number). Custom
      checklist: **no external clause cited.**
- [ ] **De-identification ran FIRST**; every finding's evidence trail uses role
      labels; no residual name / signature / address; no re-id key in the output;
      no injury/illness cell of fewer than 5 published.
- [ ] No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` /
      `[GAP]` only.
