---
sme-review:
  personas:
    - role: "Quality / CAPA systems lead (ISO 45001 10.2 nonconformity & corrective action)"
      expertise: "CAPA-system management, corrective-vs-preventive discipline, effectiveness-verification design, audit-finding closure, and recognising a 'closed-on-paper, recurs-in-practice' CAPA."
      lens: "Will this CAPA actually STOP RECURRENCE — every action traces to a real cause, preventive ≠ corrective, and each has a scheduled effectiveness check before it can be called 'verified-effective'?"
---

# SME Review & Sign-off — capa-manager

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a CAPA-lifecycle manager that shares one schema/engine with
its sibling producers (the B6→B7 seam: safety-audit emits, capa-manager ingests the verbatim
B5 register schema). The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only,
owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Root-cause → action linkage is genuine, not cosmetic — a corrective action bolted to a vague/symptom-level cause is a FLAG; an ingested cause id is reused, never re-keyed to a weaker statement.
- [ ] Corrective vs preventive genuinely differ — ≥1 preventive per cause, distinct from the corrective; a "preventive" that just restates the corrective is a FLAG.
- [ ] Effectiveness verification is real, scheduled, and gated — a CAPA cannot reach `verified-effective` without a recorded check.
- [ ] The verification method actually tests effectiveness — "re-train and remind" is an action, not a verification; a method that only confirms the action was *done* (not that it *worked*) is a FLAG.
- [ ] An ingested register is re-checked, not assumed clean — silent trust of an upstream audit/incident artifact is a FLAG; the De-identifier re-checks ingested facts.
- [ ] No "general non-compliance" anchor — the finding the CAPA addresses must be specific.
- [ ] Due dates are risk-proportionate — a high-severity NC with a distant due date, or one boilerplate date everywhere, is a FLAG; anonymous owners and "ASAP" dates are refused.

## Sign-off note
SME review: ran (persona: Quality / CAPA systems lead); this is **decision-support only**.
It **precedes — and never replaces, never emits — the human competent-person sign-off**, and
it never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
