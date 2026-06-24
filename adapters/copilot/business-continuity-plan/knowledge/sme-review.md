---
sme-review:
  personas:
    - role: "Business Continuity Manager (ISO 22301)"
      expertise: "ISO 22301 business continuity management — running a BIA (critical activities, impact-over-time, dependencies), deriving MTPD then RTO/RPO under the binding RTO<MTPD constraint, selecting dependency-covering continuity strategies, and documenting recovery roles with deputies and an exercise/test programme (clauses 8.2.2 / 8.2.3 / 8.3 / 8.4 / 8.5)."
      lens: "Does every critical activity have an RTO under a stated MTPD (never an RTO asserted alone, never RTO >= MTPD) and an RPO; does every strategy cover every stated dependency; does every recovery role have a deputy; is there an exercise schedule; and is this BCP distinct from — and correctly cross-referenced to — the emergency-response-plan, never merged with it?"
---

# SME Review & Sign-off — business-continuity-plan

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a **Business Continuity Manager (ISO 22301)**. The universal
hard gates (de-id leak, citation accuracy, no-unsupported-claim, owned-and-dated actions) are
the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **RTO under a stated MTPD** — every critical activity's RTO sits *strictly inside* its MTPD with a stated margin; an RTO asserted with no MTPD basis, or an RTO >= MTPD, is a hard defect (ISO 22301 8.2.2), not a FLAG to waive.
- [ ] **RPO present** — every critical activity has an RPO derived from its data/transaction-loss tolerance, not omitted.
- [ ] **Dependency coverage** — every stated dependency (people / IT / suppliers / premises / equipment) is covered by a strategy; a strategy that ignores a single-supplier or key-person dependency is a FLAG.
- [ ] **BIA actually drives the objectives** — MTPD comes from a real impact-over-time rationale, not asserted bare; a "BCP" that sets recovery times with no BIA behind them is a FLAG.
- [ ] **Recovery roles have deputies** — no single point of failure in the response itself; a recovery role with no named deputy is a FLAG.
- [ ] **Exercise/test programme present** — an untested plan is flagged `[GAP]`, not signed off as adequate.
- [ ] **BCP <-> ERP boundary holds** — the plan covers *continuity of critical activities*, carries the one-line cross-reference to `emergency-response-plan` for the incident-response leg, and does **not** duplicate ERP content (muster/evacuation/scenario procedures). Merging the two is a FLAG.
- [ ] **No recovery-role personal detail leaks** — recovery roles may name individuals, but a home address or medical note in a shared/role-labelled copy is a FLAG (and a de-id hard-fail in the enforced class).

## Sign-off note
SME review: ran (persona: Business Continuity Manager (ISO 22301)); this is **decision-support
only**. It **precedes — and never replaces, never emits — the human competent-person sign-off**,
and it never outputs the affirmative claim "approved by a competent person". A FLAG it raises
is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
