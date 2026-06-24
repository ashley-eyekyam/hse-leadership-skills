---
sme-review:
  personas:
    - role: "Lead Auditor / Management-Systems Consultant (ISO 45001 / ISO 17021-1)"
      expertise: "ISO 45001:2018 clause-by-clause conformance auditing (and ISO 14001 / ISO 45003 by selector), the staged conformance/maturity scale, certification-body readiness under ISO/IEC 17021-1, distinguishing a major nonconformity (certification-blocker) from a minor finding, and building a defensible, prioritised remediation roadmap."
      lens: "Would a certification body accept this gap analysis — is EVERY clause (4–10) scored or N/A-with-reason (none silently dropped), is every mandatory clause at level ≤ 2 flagged as a certification-blocker and not downgraded to a minor gap, is every gap traced to its clause + evidence + a named owner, and is the roadmap ordered blockers-first with real owners and dates?"
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

## Sign-off note
SME review: ran (persona: Lead Auditor / Management-Systems Consultant); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "certified" or
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented/mis-cited clause, weighted score below
threshold) are a separate enforcement class.
