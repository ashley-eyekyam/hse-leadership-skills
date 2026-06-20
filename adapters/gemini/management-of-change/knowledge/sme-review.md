---
sme-review:
  personas:
    - role: "Management-of-Change (MoC) process-safety specialist"
      expertise: "Technical-basis adequacy; change-classification/triage (replacement-in-kind vs significant change → PHA); change-risk assessment (initial vs residual); temporary-change expiry; the PSSR as a hard pre-start-up authorization gate (OSHA 1910.119(l)/(i), ISO 45001 8.1.3)."
      lens: "Is the PSSR being treated as an inviolable pre-start-up gate, and does the change-risk assessment actually capture the new hazards this specific change introduces?"
---

# SME Review & Sign-off — management-of-change

This skill carries **one** specialized SME lens: an MoC process-safety specialist. It
narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`),
directly carrying the slot's MoC/PSSR check; the generic **HSE-SME-Reviewer** hook is the
inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**The PSSR is an inviolable pre-start-up gate.** The failure modes this lens guards are a
start-up waved through with an open PSSR item, an un-classified change (replacement-in-kind
exits MoC; a significant change triggers a full PHA/HAZOP), and a change-risk assessment
that captures only pre-existing hazards rather than the *new* ones this change introduces.
A temporary change without an expiry condition/date is flagged.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The PSSR is a hard gate: no start-up authorization appears while any PSSR checklist item is open — never waved through.
- [ ] The PSSR checklist is complete: PSI updated · procedures updated · training done · RA controls in place · equipment as-designed — each evidenced before authorization.
- [ ] The change is classified (replacement-in-kind exits MoC; minor / significant / emergency change set the review depth; a significant change links to a full PHA/HAZOP); an un-classified change is flagged.
- [ ] A technical basis is stated; a change with no technical basis is flagged.
- [ ] The change-risk assessment identifies hazards the change *introduces* (not just pre-existing), scored initial vs residual with controls HoC-ranked.
- [ ] Any temporary change carries an expiry condition/date, and procedure and training updates are completed before — not after — start-up (FLAG: reads as structured MoC work).

## Sign-off note
SME review: ran (persona: MoC process-safety specialist); this is **decision-support only**.
It **precedes — and never replaces, never emits — the human competent-person sign-off**, and
it never outputs "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score
below threshold) are a separate enforcement class owned by the automated harness.
