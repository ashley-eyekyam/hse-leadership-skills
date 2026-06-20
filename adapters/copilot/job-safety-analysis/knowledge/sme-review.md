---
sme-review:
  personas:
    - role: "Frontline safety / work-method specialist (NEBOSH-level, permit-to-work authority)"
      expertise: "Job/task decomposition, step-level hazard identification across energy sources, permit-to-work regimes (confined space / hot work / working at height), and per-step control adequacy."
      lens: "Is the job decomposed into REAL ordered steps, each step's hazards identified and controlled at step granularity — with no PPE-only step and the right permits triggered by the steps that imply them?"
---

# SME Review & Sign-off — job-safety-analysis

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`). It shares the risk-assessment lineage but bites at *step*
granularity — the JSA's defining surface. The universal hard gates (de-id leak, citation
accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The step sequence is real and complete — a missing safety-critical step (LOTO before maintenance, gas-test before confined-space entry) is the highest-value FLAG; ask, never silently insert it.
- [ ] Hazards are tied to the step that creates them — generic whole-job hazards smeared across every row is a FLAG.
- [ ] No PPE-only step — the HoC lever bites *per step*; any step left PPE/admin-only without a per-step justification is a FLAG.
- [ ] Permit triggers are caught — steps implying confined-space / hot-work / height / energy-isolation must trigger the matching permit-to-work.
- [ ] Residual is re-scored per step; a High/Critical residual is not silently "accepted".
- [ ] The sign-off block ships with empty signature rows — no invented names.
- [ ] Right tool — a whole-activity hazard register means the user wanted risk-assessment; a JSA with one giant step is not a JSA; flag a mis-scoped request.

## Sign-off note
SME review: ran (persona: Frontline safety / work-method specialist); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
