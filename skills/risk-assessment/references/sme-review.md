---
sme-review:
  personas:
    - role: "Chartered safety & health practitioner (CMIOSH) / HIRA SME"
      expertise: "ISO 45001 6.1.2 hazard identification & risk assessment, risk-matrix scoring & residual logic, hierarchy-of-controls application, and ISO 14001 6.1.2 environmental aspects/impacts when in scope (the env branch reuses the SAME matrix)."
      lens: "Is this assessment SPECIFIC to the named task/site/asset, every hazard scored and residual-rescored with controls applied, and every control driven up the hierarchy — never a PPE-only treatment dressed up as adequate?"
modes:
  hira:
    detected_by: "Q0 — Scope of this assessment (Occupational safety, the default, or Both → the safety-HIRA leg of the produced assessment: hazard identification per task step → matrix scoring → ranked controls → residual re-score → SMART actions)"
    floor:
      - id: hazard-identification-coverage
        description: "Every task step (intake Q3) is examined for hazards — a per-step hazard register with the mechanism named, per ISO 45001 clause 6.1.2 hazard identification"
        anchors: ['hazard identification', 'per task step', '\|\s*step\s*\|']
        min_matches: 1
      - id: matrix-scoring
        description: "Every hazard is scored likelihood x severity on the org risk matrix via the deterministic risk_matrix engine — the band is the engine's, never prose (intake Q7-Q9)"
        anchors: ['risk_matrix', 'likelihood\s*\|\s*severity', '\d\s*x\s*\d matrix', 'score \(l x s\)']
        min_matches: 1
      - id: hierarchy-of-controls
        description: "Controls are ranked down the full hierarchy (Elimination -> Substitution -> Engineering -> Administrative -> PPE) with >=1 Engineering-or-higher control per hazard or a justified absence — never an unjustified PPE/admin-only treatment (KB-SNIP-HOC)"
        anchors: ['hierarchy of controls', 'elimination.{0,60}substitution.{0,60}engineering', 'ppe.admin.only']
        min_matches: 1
      - id: residual-rescoring
        description: "Residual risk is re-scored with controls applied and the initial -> residual movement is shown — residual is never assumed"
        anchors: ['residual (risk|score)', 're.scor', 'initial.{0,30}residual']
        min_matches: 1
      - id: smart-actions-owned-dated
        description: "Every corrective action is SMART — a named role-label owner, an ISO due date, and a link to the hazard it treats (intake Q10b)"
        anchors: ['smart action', 'named (role.label )?owner', 'owner.{0,40}due']
        min_matches: 1
      - id: exposed-parties
        description: "Who is exposed is named per hazard scope — own workers / contractors / public / community (intake Q5); a hazard with no exposed party is undefendable"
        anchors: ['exposed part', 'who is exposed', 'exposed:']
        min_matches: 1
      - id: regulatory-basis
        description: "The assessment states its standard basis — ISO 45001 clause 6.1.2 cited; India jurisdictions resolve the state statutory record via KB-REG-IN-STATEFORMS after mandatory state detection, never a national form number (intake Q1/Q1a)"
        anchors: ['iso 45001.{0,20}6\.1\.2', 'kb-reg-in-stateforms', 'clause 6\.1\.2']
        min_matches: 1
      - id: review-validity
        description: "A review trigger / review cycle is set (intake Q10c) and competent-person sign-off is required before circulation — the assessment declares its own validity limits"
        anchors: ['review trigger', 'review (date|cycle|cadence)', 'competent.person sign.off']
        min_matches: 1
  environmental-aspects:
    detected_by: "Q0 — Scope of this assessment (Environmental aspects / Both → the Q-E1…Q-E5 branch + the env-aspects-register output section, KB-STD-ISO14001 row)"
    floor:
      - id: aspect-impact-pairs
        description: "Environmental aspect -> associated impact pairs are identified per activity step (intake Q-E2/Q-E3), per ISO 14001 clause 6.1.2 aspects determination"
        anchors: ['aspect\s*(->|→|to)\s*impact', 'environmental aspect', 'associated impact']
        min_matches: 1
      - id: iso14001-basis
        description: "ISO 14001 clause 6.1.2 is cited as the environmental standard basis (the KB-STD-ISO14001 clause-to-artifact row)"
        anchors: ['iso 14001.{0,20}6\.1\.2', 'kb-std-iso14001']
        min_matches: 1
      - id: significance-scoring-same-engine
        description: "Each aspect's significance is scored on the SAME risk_matrix engine as the safety scope (environmental consequence descriptors) — no engine fork"
        anchors: ['(initial|residual) significance', 'risk_matrix\.score', 'no engine fork']
        min_matches: 1
      - id: operating-conditions
        description: "Normal / abnormal (start-up, shutdown, maintenance) / emergency operating conditions are declared and assessed (intake Q-E4)"
        anchors: ['operating condition', 'normal.{0,60}abnormal', 'emergency \(']
        min_matches: 1
      - id: hoc-on-aspect
        description: "The hierarchy of controls is applied to the ASPECT — >=1 Elimination/Substitution/Engineering control per aspect or a justified absence; an aspect controlled only by end-of-pipe mitigation or PPE/admin is inadequate"
        anchors: ['hierarchy of controls', '(eliminat|substitut)\w*.{0,80}aspect', 'ppe.admin.only']
        min_matches: 1
      - id: residual-significance
        description: "Residual significance is re-scored with controls applied and the initial -> residual movement is shown"
        anchors: ['residual significance', 'post.control re.score', 'initial.{0,30}residual']
        min_matches: 1
      - id: env-actions-owned-dated
        description: "Every environmental action is SMART — a named role-label owner, an ISO due date, and a link to the aspect it treats"
        anchors: ['smart action', 'named (role.label )?owner', 'owner.{0,40}due']
        min_matches: 1
---

# SME Review & Sign-off — risk-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a chartered safety practitioner / HIRA SME. The ISO 14001
environmental branch is reuse of the SAME risk matrix — a checklist item, not a second lens.
The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated
actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Task/site specificity is real — a generic, copy-paste-flavoured assessment that could apply to any site is a FLAG.
- [ ] Hazard completeness for the task type — a confined-space RA with no atmosphere/engulfment hazard, or a work-at-height RA with no fall-from-edge, is an obviously incomplete hazard set and a FLAG.
- [ ] Residual is re-scored, not assumed — each hazard is re-scored *with controls applied*; a residual that stays High/Critical needs more controls or a stop-work, not "accept and proceed".
- [ ] Controls beat the hazard, not just name PPE — a jump to PPE/admin without testing elimination/substitution/engineering, unjustified, is a FLAG.
- [ ] Likelihood/severity are defensible — a catastrophic hazard scored "minor" to green the matrix, or scores inconsistent with the stated exposure, is a FLAG.
- [ ] Environmental branch (when in scope) — significance scored on the SAME matrix and the *aspect* eliminated/substituted first; an aspect "controlled" only by end-of-pipe mitigation is a FLAG.
- [ ] Who-is-exposed is named — a hazard with no exposed party is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class goes hollow):
- **The polished half-assessment** — hazards identified and initially scored on a credible
  matrix, then the assessment simply stops: controls listed as a flat precaution list with no
  hierarchy ranking and no PPE-only test, no residual re-score, actions with no named owner
  or date. It reads finished because the front half is real. Check the back half first.
- **The statutory layer silently absent** — a jurisdiction (and even a state) is named in the
  header, but no ISO 45001 clause 6.1.2 basis is stated and the India state statutory record
  is never resolved via KB-REG-IN-STATEFORMS; generic "good practice" language stands in for
  the regulatory basis. The principal's statutory exposure is stranded without a visible gap.
- **Step/hazard mismatch** — the task steps are listed (isolate → purge → gas-test → enter …)
  but a step carries no examined hazard (a purge step with no oxygen-deficiency hazard, a
  work-at-height step with no fall-from-edge). The hazard set looks populated; a step-by-step
  reconciliation exposes the hole.
- **The environmental branch skipped silently** — Q0 = Both, yet no aspect → impact pairs, no
  significance scoring, no env-aspects-register section; the safety leg's polish hides the
  missing second scope.
- **Evidence and assumption discipline** — unverified facts (last-contained substance, rescue
  equipment availability, monitoring data) carried as flat statements instead of
  `[ASSUMPTION]` / `[GAP]` entries with closing actions; scores presented with no evidence
  trail for the likelihood/severity chosen.

## Sign-off note
SME review: ran (persona: Chartered safety & health practitioner (CMIOSH) / HIRA SME); this
is **decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
