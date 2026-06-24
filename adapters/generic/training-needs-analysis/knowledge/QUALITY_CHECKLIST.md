# Pre-output Quality Checklist — Training Needs Analysis

Validate the draft against this gate **before any output** (the Workflow step-9 self-check).
Anything unchecked is fixed or recorded as `[GAP]` / `[ASSUMPTION]` — never papered over.

## Specificity & evidence (the core value)
- [ ] **Named roles, not "everyone"** — the matrix is built on named roles + headcounts; a
      "train everyone" request was refused at intake.
- [ ] **Every gap traces to a named role + an evidence source** — no competence level is
      asserted without a named evidence source (job description / training record / appraisal /
      legal requirement / incident); unevidenced cells are flagged `[GAP]`, not guessed.
- [ ] **Required levels reflect task risk** — high-hazard tasks require level 3 (competent) +
      valid certification where the law mandates one; the required level is set by the task,
      not the person.

## Legal-required competencies (regulatory_citation_accuracy — hard)
- [ ] **No legal-required competency omitted** — every statutory competence for the roles in
      scope is a row in the matrix, cited to its named legal source (jurisdiction resolved;
      India → state via `hse-india`, never a national form number).
- [ ] **No statutory gap downgraded to "pass"** — an unmet legal-required competence is a gap
      against its legal source, ranked as mandatory regardless of headcount.

## Hierarchy of controls (the no-training-only lever)
- [ ] **Training is framed as an administrative control** (`KB-SNIP-HOC` + `controls`) — where
      the underlying hazard admits a higher-order control (eliminate/substitute/engineer), the
      plan says so; "more training" is **never** shipped as the sole treatment.
- [ ] **No admin-only treatment without justification** — `controls.validate_treatment`
      clears, or an explicit "higher-order controls not reasonably practicable because…" is
      recorded.

## SPOF & expiry
- [ ] **Single-points-of-failure flagged by role** — a critical competence held by only one
      person is flagged, by role label, with a cross-training action.
- [ ] **Certification/expiry tracker present** — time-limited certificates carry holder role,
      expiry date, and refresher due date; expired statutory certs rank high-priority.

## Plan integrity (defensibility)
- [ ] **Every action SMART, owned, dated, costed** — each prioritised gap → a SMART action via
      `smart_actions.validate_register` with a named owner role, an ISO due date, a measure, and
      an indicative cost; no "TBD", no "ASAP".
- [ ] **Prioritised by risk × legal × gap size** — statutory + high-hazard gaps and SPOFs rank
      first.

## De-identification (de_identification — hard)
- [ ] **De-id pass complete BEFORE drafting** — competence/appraisal data pseudonymised to role
      labels; no individual's competence gap published by name in a widely shared artifact.
- [ ] **Small cells suppressed** — where one named person is the sole competence holder, the
      gap is reported, the identity is not; no re-identification key embedded in the matrix.
