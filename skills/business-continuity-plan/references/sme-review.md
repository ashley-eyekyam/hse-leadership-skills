---
sme-review:
  personas:
    - role: "Business Continuity Manager (ISO 22301)"
      expertise: "ISO 22301 business continuity management — running a BIA (critical activities, impact-over-time, dependencies), deriving MTPD then RTO/RPO under the binding RTO<MTPD constraint, selecting dependency-covering continuity strategies, and documenting recovery roles with deputies and an exercise/test programme (clauses 8.2.2 / 8.2.3 / 8.3 / 8.4 / 8.5)."
      lens: "Does every critical activity have an RTO under a stated MTPD (never an RTO asserted alone, never RTO >= MTPD) and an RPO; does every strategy cover every stated dependency; does every recovery role have a deputy; is there an exercise schedule; and is this BCP distinct from — and correctly cross-referenced to — the emergency-response-plan, never merged with it?"
modes:
  bcp:
    detected_by: "Q = the requested deliverable (a business continuity plan for the named critical activities) — single-output skill; this mode is always active"
    floor:
      - id: rto-inside-mtpd
        description: "Every critical activity's RTO sits strictly inside its stated MTPD with a margin — an RTO asserted with no MTPD basis, or RTO >= MTPD, is a FLAG (ISO 22301 8.2.2)"
        anchors: ['rto', 'mtpd']
        min_matches: 2
      - id: rpo-present
        description: "Every critical activity carries an RPO derived from its data/transaction-loss tolerance, never omitted"
        anchors: ['rpo|recovery point', 'critical activit|data']
        min_matches: 2
      - id: dependency-coverage
        description: "Every stated dependency (people / IT / suppliers / premises / equipment) is covered by a continuity strategy; a single uncovered dependency is a FLAG (ISO 22301 8.3)"
        anchors: ['dependenc', 'strateg']
        min_matches: 2
      - id: bia-drives-objectives
        description: "MTPD/RTO come from a real business-impact-over-time rationale (BIA), not asserted bare (ISO 22301 8.2.2)"
        anchors: ['business impact|bia', 'mtpd']
        min_matches: 2
      - id: recovery-roles-have-deputies
        description: "No single point of failure in the response — every recovery/command role has a named deputy or alternate (ISO 22301 8.4)"
        anchors: ['deput|alternate', 'role']
        min_matches: 2
      - id: exercise-test-programme
        description: "An exercise/test programme is scheduled with owners and dates — an untested plan is flagged [GAP], never signed off as adequate (ISO 22301 8.5)"
        anchors: ['exercise|test schedule|drill', 'schedul']
        min_matches: 2
      - id: bcp-erp-boundary
        description: "The plan covers continuity of critical activities and carries the one-line cross-reference to emergency-response-plan — the two are never merged"
        anchors: ['emergency-response-plan|emergency response', 'continuity']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The invocation trigger and decision authority (who declares an incident)** — a BCP that lists
  recovery strategies but never states WHO can invoke the plan, on what trigger, and the decision
  authority for stand-down leaves the plan unactionable on the day.
- **The high-severity RTO with no bridge (S2)** — a critical activity whose achievable recovery
  time exceeds its RTO, with no stated interim workaround for the shortfall period, is an
  acknowledged gap dressed as a plan. Surface the shortfall and its interim measure.
- **Single-supplier / single-site dependency unassessed** — a dependency "covered" by a strategy
  that itself has a single point of failure (one supplier, one data centre) is not covered; the
  strategy's own resilience must be tested.
- **Recovery of the recovery** — backups/failover named as existing but never proven by a
  restoration test; existence is not recoverability.

## Sign-off note
SME review: ran (persona: Business Continuity Manager (ISO 22301)); this is **decision-support
only**. It **precedes — and never replaces, never emits — the human competent-person sign-off**,
and it never outputs the affirmative claim "approved by a competent person". A FLAG it raises
is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
