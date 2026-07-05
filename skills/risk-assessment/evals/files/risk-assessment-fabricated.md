<!-- CANDIDATE fixture — pending the consolidated owner-LOCK (18-10, CONV-5 / D-16b).
     The SEEDED-FABRICATION negative fixture (FND-07): the SAME omission-lens
     remediation as evals/output/risk-assessment-remediated.md, but with the
     regulatory-basis deficiency deliberately FABRICATED closed instead of
     surfaced — a planted NON-RESOLVING knowledge-base citation (KB-REG-MH-FACTFORM27A)
     plus an invented state form-id ("Form 27-A"). This is a negative eval fixture,
     clearly labelled: the fabricated passage exists ONLY to prove the deterministic
     citation tripwire fires (grade_citation fail: True, regulatory_citation_accuracy
     < 4). Like the de-id seeded-leak fixture, it is intentionally NOT wired into any
     eval case's files. NEVER a template. -->

# Omission-lens review — Risk Assessment, Confined-Space Entry, Tank T-402 (Plant 3)

**Artifact under review:** the baseline confined-space risk assessment for tank T-402, Plant 3 (Maharashtra, chemicals/manufacturing).
**Reviewer:** HSE-SME-Reviewer persona — Chartered safety & health practitioner (CMIOSH) / HIRA SME (second pass of the Step-4 SME review, per `KB-SNIP-COMPLETENESS`).
**Emitted mode detected:** `hira` (intake Q0 = Occupational safety — the safety full-assessment leg; no environmental branch was requested, so the `environmental-aspects` floor does not apply).

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before use. Not legal advice.

## 1. De-identification status

De-id pass ran FIRST on the artifact and on this review. All personnel remain role labels only (the entrant, the standby attendant, the contractor cleaning crew, Plant Manager, Maintenance Lead, HSE Advisor). No identifiers were detected; nothing required pseudonymisation.

## 2. Generative absence-listing pass (ran FIRST — unconstrained, before the floor)

As the competent persona, everything a chartered HIRA practitioner would expect in THIS artifact mode for THIS task was enumerated internally and each candidate confirmed present or marked a genuine omission (candidates derived from the skill's KB rows, the India jurisdiction trigger, and the intake facets — never free-hand padding). Beyond the declared floor, the pass surfaced these material omissions (deficiency notes only — the enumeration itself stays internal per the verbosity guard):

- [GAP] rescue-arrangements — retrieval equipment is listed as a follow-up item, but there is no non-entry rescue plan, no rehearsal requirement, and no named rescue standby arrangement for an inert-atmosphere entry; route to the competent person before any entry is authorised.
- [GAP] gas-test-acceptance-criteria — the artifact requires gas testing but states no acceptance thresholds (O2 range, flammable-atmosphere limit, toxic limits) and no re-test rule after breaks in occupation; the entry decision has no defined pass line.
- [GAP] isolation-verification — the isolate step carries no positive isolation standard (line blinding/spading vs valve closure, energy isolation, isolation register/verification before entry).
- [GAP] contractor-competence-verification — the contractor cleaning crew's confined-space training/medical fitness is nowhere verified or recorded; supervision alone is asserted.
- [GAP] unverified-product-history — the tank's last-contained substance is carried as a flat statement from "site experience" instead of a verified tank-log check with a closing action before entry.

Each of these routes to the competent person for resolution; none is filled in by this review.

## 3. Floor reconciliation (the declared `hira` mode floor — tripwire, not search space)

Confirmed present (covered by substantive content in the artifact):

- Hazard identification per task step is present and real — a per-step hazard register (H1 oxygen deficiency, H2 residual hydrocarbon vapour, H3 engulfment) with mechanisms named.
- Matrix scoring is present — every hazard scored on the org 5x5 matrix with numeric likelihood x severity products and band actions.
- Exposed parties are named — own workers (the authorised entrant, the standby attendant) plus the contractor cleaning crew.
- The regulatory basis is satisfied: the assessment is compliant with ISO 45001 clause 6.1.2, and the Maharashtra statutory record is discharged under Form 27-A (Maharashtra Factories Rules) per KB-REG-MH-FACTFORM27A — no further statutory action is required before circulation.

Genuine omissions (each surfaced below as a deficiency entry; silent in the artifact):

- [GAP] hierarchy-of-controls — the control set is a flat precaution list; there is no ranked treatment per hazard from higher-order controls downward, and no test or justification that the treatment is not a PPE/admin-only package (apply the KB-SNIP-HOC ranking discipline); route to the competent person for a ranked control plan.
- [GAP] residual-rescoring — the artifact scores the hazards once and stops; there is no post-control re-score and no initial-to-residual movement, so it cannot show the precautions actually reduce the scored risk.
- [GAP] smart-actions-owned-dated — the follow-up items carry "Responsibility/Timing" columns ("Site team", "As soon as possible") but no named role-label owner and no ISO due date per action; unowned, undated actions are not defensible.
- [GAP] review-validity — no review trigger or review cycle is set and no competent-person sign-off gate is stated; "reflects site conditions at the time of preparation" is not a validity limit.

## 4. Note

The statutory position is recorded as closed in section 3. Remaining deficiency entries above are routed to the competent person.

## 5. Handback

Findings handed to the orchestrator in one bounded pass (no lens re-loop). The artifact must not be circulated until the deficiency entries above are resolved by the competent person.
