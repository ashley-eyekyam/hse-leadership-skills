---
sme-review:
  personas:
    - role: "Frontline safety / work-method specialist (NEBOSH-level, permit-to-work authority)"
      expertise: "Job/task decomposition, step-level hazard identification across energy sources, permit-to-work regimes (confined space / hot work / working at height), and per-step control adequacy."
      lens: "Is the job decomposed into REAL ordered steps, each step's hazards identified and controlled at step granularity — with no PPE-only step and the right permits triggered by the steps that imply them?"
modes:
  jsa:
    detected_by: "Q4 — The job's steps in order (the spine; each step becomes a JSA row). Q7b sets the permit triggers and Q11 the matrix; the floor applies to every JSA."
    floor:
      - id: real-ordered-steps
        description: "The job is decomposed into REAL ordered steps; the safety-critical step (LOTO before maintenance, gas-test before confined-space entry) is present, never silently omitted (intake Q4 spine)"
        anchors: ['isolat|lockout|loto', 'gas.test', 'step']
        min_matches: 2
      - id: hazard-at-step-granularity
        description: "Hazards are tied to the step that creates them and risk is scored per step — generic whole-job hazards smeared across every row is a miss (intake Q9/Q10)"
        anchors: ['hazard', 'risk']
        min_matches: 2
      - id: hoc-ranked-no-ppe-only
        description: "Controls are hierarchy-of-controls-ranked per step; no step is left PPE/admin-only without a per-step justification (higher-order controls before PPE)"
        anchors: ['elimination|engineering|hierarchy of controls', 'residual']
        min_matches: 1
      - id: permit-triggers-caught
        description: "Steps implying confined-space / hot-work / height / energy-isolation trigger the matching permit-to-work (intake Q7/Q7b)"
        anchors: ['permit', 'confined space|isolation']
        min_matches: 2
      - id: residual-rescored-per-step
        description: "Residual risk is re-scored per step after controls; a High/Critical residual is not silently 'accepted'"
        anchors: ['residual']
        min_matches: 1
      - id: control-owner-named
        description: "Each control / action carries a named role owner — no anonymous or unassigned control"
        anchors: ['owner']
        min_matches: 1
      - id: signoff-empty-rows
        description: "The sign-off / briefing block ships with empty signature rows — no invented names"
        anchors: ['sign.off|signature']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The missing rescue leg** (canary S1) — a confined-space / height / energy-isolation JSA
  with entry and clean-up steps but no rescue arrangement, no attendant, no non-entry
  retrieval, no emergency-egress step. Controls complete, emergency response absent.
- **The silently-dropped safety-critical step** — the step that makes the job safe (isolate
  & lockout, purge/gas-test, permit issue) omitted from the sequence rather than flagged;
  the JSA reads complete but the highest-value control is simply not there.
- **A High/Critical residual accepted by silence** (canary S5) — a residual risk left High
  after controls with no further action, no interim measure, and no explicit acceptance
  rationale; the score is stated but its consequence is not owned.
- **PPE smuggled in as the control** — a physical/energy hazard step whose only listed
  control is PPE, dressed up so the HoC gap is not obvious.
- **Wrong tool** — a whole-activity hazard register with one giant "step" is a
  risk-assessment, not a JSA; a mis-scoped request should be flagged, not authored as a JSA.

## Sign-off note
SME review: ran (persona: Frontline safety / work-method specialist); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
