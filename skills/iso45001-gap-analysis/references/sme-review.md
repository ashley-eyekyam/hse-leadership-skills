---
sme-review:
  personas:
    - role: "Lead Auditor / Management-Systems Consultant (ISO 45001 / ISO 17021-1)"
      expertise: "ISO 45001:2018 clause-by-clause conformance auditing (and ISO 14001 / ISO 45003 by selector), the staged conformance/maturity scale, certification-body readiness under ISO/IEC 17021-1, distinguishing a major nonconformity (certification-blocker) from a minor finding, and building a defensible, prioritised remediation roadmap."
      lens: "Would a certification body accept this gap analysis — is EVERY clause (4–10) scored or N/A-with-reason (none silently dropped), is every mandatory clause at level ≤ 2 flagged as a certification-blocker and not downgraded to a minor gap, is every gap traced to its clause + evidence + a named owner, and is the roadmap ordered blockers-first with real owners and dates?"
modes:
  gap-analysis:
    detected_by: "Q = the requested deliverable (an ISO 45001/14001/45003 gap analysis for the named site) — single-output skill; this mode is always active"
    floor:
      - id: every-clause-scored-or-na
        description: "Every clause across 4 (context) → 10 (improvement) is either scored on the maturity scale or explicitly N/A-with-reason — none silently dropped"
        anchors: ['clause', 'n/a|not applicable|every clause|none omitted|scored']
        min_matches: 2
      - id: blockers-classified-not-downgraded
        description: "A mandatory clause at maturity level <=2 (5.2 policy, 6.1.2 hazard-id, 9.2 internal audit, 10.2 incident/nonconformity) is flagged a certification-blocker, never downgraded to a minor gap"
        anchors: ['blocker|major nonconform', 'mandatory|5.2|6.1.2|9.2|10.2|certification']
        min_matches: 2
      - id: conformance-matches-evidence
        description: "The conformance level matches the evidence — a clause scored Implemented on a procedure alone (no records of it being followed) is a FLAG"
        anchors: ['evidence|record', 'level|maturity|conformant']
        min_matches: 2
      - id: gap-traces-clause-evidence-owner
        description: "Every gap traces to its clause reference + evidence basis + a named owner — a gap missing any of these is a FLAG"
        anchors: ['owner', 'clause|evidence']
        min_matches: 2
      - id: roadmap-blockers-first-owned-dated
        description: "The remediation roadmap leads with certification-blockers (by severity), each costed/owned/dated — a roadmap not ordered blockers-first is a FLAG"
        anchors: ['roadmap|prioriti', 'blocker|owner|date']
        min_matches: 2
      - id: hierarchy-on-planning-clause
        description: "Where clause 6.1 controls are assessed, elimination/substitution is tested before a jump to admin/PPE (no PPE-only planning control)"
        anchors: ['hierarchy|elimination|6.1', 'control|ppe']
        min_matches: 2
      - id: standard-fidelity
        description: "The cited clause numbers and titles match the selected standard (ISO 45001 vs 14001 vs 45003) — an invented or mis-numbered clause is a FLAG"
        anchors: ['45001|45003|14001', 'clause']
        min_matches: 2
---

# SME Review & Sign-off — iso45001-gap-analysis

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a **Lead Auditor / Management-Systems Consultant**. The
ISO 14001 / ISO 45003 selector variants are the SAME clause-walk against a different clause
set — a checklist item, not a second lens. The universal hard gates (de-id leak, citation
accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **No clause silently omitted** — every clause across 4 (context) → 10 (improvement) is either scored on the maturity scale or explicitly marked **N/A with a stated reason**. A missing clause (e.g. 6.1.2 hazard-id absent from the matrix) is a FLAG — it makes the analysis vacuously "conformant".
- [ ] **Certification-blockers correctly classified, not downgraded** — a mandatory clause (5.2 policy, 6.1.2 hazard-id, 9.2 internal audit, 10.2 incident/nonconformity) sitting at level ≤ 2 is flagged as a **certification-blocker**, not buried as a minor gap. A blocker shown as a low-priority improvement is a FLAG.
- [ ] **Conformance level matches the evidence** — a clause scored level 3 (Implemented/conformant) on a procedure alone (no records of it being followed), or scored "ready" on self-assertion with no evidence, is a FLAG. The level must satisfy that level's **evidence test** in `KB-DATA-ISO45001-MATURITY`.
- [ ] **Every gap traces to clause + evidence + owner** — a gap with no clause reference, no evidence basis, or no named owner is a FLAG.
- [ ] **Roadmap ordered blockers-first, costed, owned, dated** — the remediation roadmap leads with certification-blockers (by severity), then high-severity non-blockers; an action with no owner, no due date, or "ASAP" is a FLAG.
- [ ] **Planning-clause controls beat the hazard, not just name PPE** — where clause 6.1 controls are assessed, a jump to PPE/admin without testing elimination/substitution/engineering, unjustified, is a FLAG.
- [ ] **Standard fidelity** — the cited clause numbers and titles match the selected standard (ISO 45001 vs 14001 vs 45003); an invented or mis-numbered clause is a FLAG (and a `regulatory_citation_accuracy` hard block when wrong).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The silently-dropped clause** — a gap analysis that scores the clauses the site is strong on
  and quietly omits the ones it is weak on reads well and certifies nothing. Every clause 4→10 is
  scored or N/A-with-reason; a missing clause is the signature failure of a hollow gap analysis.
- **The blocker downgraded to a minor gap (S2)** — a mandatory clause at low maturity relabelled a
  "minor observation" with a comfortable due date hides a certification-blocker. Classify by the
  clause's mandatory status, not by how convenient the finding is.
- **Conformance asserted from a document, not evidence (S5)** — a clause scored "implemented"
  because a procedure EXISTS, with no records that it is followed, is an evidence-free score. Tie
  every conformance level to sighted records, or mark it a gap.
- **The un-owned, undated roadmap** — remediation actions with no named owner, no date, and no
  blockers-first ordering are a wish-list, not a certification plan.

## Sign-off note
SME review: ran (persona: Lead Auditor / Management-Systems Consultant); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "certified" or
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented/mis-cited clause, weighted score below
threshold) are a separate enforcement class.
