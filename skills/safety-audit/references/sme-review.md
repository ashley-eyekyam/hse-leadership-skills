---
sme-review:
  personas:
    - role: "Lead auditor (ISO 19011 / ISO 45001 9.2, IRCA/CQI-registered)"
      expertise: "Internal & certification auditing, objective-evidence discipline, the 4-class finding scheme (major NC / minor NC / observation / OFI), conformity rating, sampling sufficiency, and the B6→B7 CAPA-register handoff."
      lens: "Is every finding traced to OBJECTIVE evidence against a specific named criterion, classified correctly (major vs minor vs observation vs OFI), every nonconformity risk-rated, and the emitted CAPA register clean enough to round-trip into capa-manager?"
modes:
  audit:
    detected_by: "Q-Type — Audit type (Compliance vs law / Management-system vs ISO 45001 / Process vs an SOP-spec); Q-Crit sets the criteria walked finding-by-finding. The floor applies to every audit type."
    floor:
      - id: finding-to-objective-evidence
        description: "Every finding traces to OBJECTIVE evidence (document id / observation / interview-role) against a specific NAMED criterion — an assertion with no evidence and no clause it tests is indefensible (intake Q-Evid/Q-Crit)"
        anchors: ['finding', 'evidence', 'criteri']
        min_matches: 2
      - id: classification-correct
        description: "Findings are classified correctly — major NC (systemic/total absence) vs minor NC (isolated lapse) vs observation (drift) vs OFI; a systemic failure logged 'minor' is a miss"
        anchors: ['major', 'minor', 'observation|ofi']
        min_matches: 2
      - id: every-nc-risk-rated
        description: "Every nonconformity is risk-rated on the org matrix by default — an un-rated NC is a miss (intake Q-NCrate)"
        anchors: ['nonconformity|\bNC\b', 'risk.rat|risk.rank']
        min_matches: 2
      - id: no-silent-pass
        description: "No criterion is silently passed — an unassessed clause reads 'insufficient evidence' / [GAP], never a silent pass"
        anchors: ['insufficient evidence|\[GAP\]', 'criteri']
        min_matches: 1
      - id: method-vs-criteria-distinct
        description: "Audit method and audit criteria are not conflated — ISO 45001 cl. 9.2 is the METHOD; the criterion is the operational clause (e.g. cl. 8.1) or the checklist item tested"
        anchors: ['iso 45001', '9.2|clause 8.1|cl. 8.1']
        min_matches: 2
      - id: smart-corrective-actions
        description: "Corrective actions are SMART with a named role owner and due date, tied to the finding they close (feeds capa-manager)"
        anchors: ['owner', 'corrective action|smart', 'due']
        min_matches: 2
      - id: capa-register-clean-handoff
        description: "The emitted CAPA register uses the B5 schema and links each action to its finding id (links_to_cause) so it round-trips into capa-manager (the B6->B7 seam)"
        anchors: ['capa', 'links_to_cause|register']
        min_matches: 2
---

# SME Review & Sign-off — safety-audit

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into an ISO 19011 / ISO 45001 9.2 lead auditor. The domain
subtlety this persona holds: a finding is only as strong as the objective evidence and the
named criterion behind it, and the emitted CAPA register is a data contract (the B6→B7 seam)
that must round-trip into capa-manager. The universal hard gates (de-id leak, citation
accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every finding traces to objective evidence against a *named criterion* — an assertion with no document id / observation / interview-role and no clause it tests is indefensible.
- [ ] Classification is correct — major NC (systemic / total absence) vs minor NC (isolated lapse) vs observation (drift risk) vs OFI; a systemic failure logged "minor", or an OFI logged as a nonconformity, is a FLAG.
- [ ] Every nonconformity is risk-rated by default — an un-rated NC is a FLAG.
- [ ] No criterion is silently passed — an unassessed clause must read "insufficient evidence / `[GAP]`", never a silent pass.
- [ ] Method vs criteria are not conflated — ISO 45001 9.2 is the *method*; a report that cites 9.2 *as* the criterion is a FLAG.
- [ ] Conformity rating is computed, not asserted — it derives from the per-finding counts/ratings.
- [ ] CAPA register handoff is clean (B6→B7) — it uses the B5 schema verbatim with `links_to_cause` = the finding id; a register that won't round-trip into capa-manager is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The finding with no evidence** — a nonconformity asserted with no document id,
  observation, or interview-role behind it; an audit conclusion a challenged auditee could
  not be shown the basis for.
- **Incident-history silence** (canary S3) — the audit never reviews prior incidents /
  near-misses / previous audit or CAPA history for the audited system, nor confirms their
  absence; the sampling ignores the very events that reveal whether the control works.
- **The regime named, its element set unswept** (canary S6) — the standard/regulation is
  cited but the specific clause set it demands is only partially walked, with the unassessed
  clauses silently passed rather than marked insufficient-evidence / [GAP].
- **Sampling basis unstated** — findings drawn from an unstated or unrepresentative sample
  (which permits, which shifts, what population) so coverage and confidence cannot be judged.
- **A register that will not round-trip** — a CAPA register whose schema or finding-id links
  will not ingest cleanly into capa-manager, breaking the B6->B7 seam.

## Sign-off note
SME review: ran (persona: Lead auditor (ISO 19011 / ISO 45001 9.2)); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
