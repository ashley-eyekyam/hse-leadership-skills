---
sme-review:
  personas:
    - role: "Management-of-Change (MoC) process-safety specialist"
      expertise: "Technical-basis adequacy; change-classification/triage (replacement-in-kind vs significant change → PHA); change-risk assessment (initial vs residual); temporary-change expiry; the PSSR as a hard pre-start-up authorization gate (OSHA 1910.119(l)/(i), ISO 45001 8.1.3)."
      lens: "Is the PSSR being treated as an inviolable pre-start-up gate, and does the change-risk assessment actually capture the new hazards this specific change introduces?"
modes:
  moc-package:
    detected_by: "Q11 — What output, for whom? (MOC package / PSSR checklist / Change RA — all legs of the one MoC package artifact this skill produces)"
    floor:
      - id: change-stated-and-classified
        description: "The exact change is stated and classified — replacement-in-kind (exits MoC, justification logged) / minor / significant (links a full PHA-HAZOP) / emergency (retrospective review flagged) (intake Q1/Q3 triage)"
        anchors: ['classif', 'replacement.in.kind|significant change']
        min_matches: 2
      - id: technical-basis-stated
        description: "The engineering/operational technical basis for the change is stated — why the change is sound (intake Q5; OSHA 1910.119(l) requirement)"
        anchors: ['technical basis']
        min_matches: 1
      - id: change-ra-introduced-hazards
        description: "The change risk assessment captures the hazards the change INTRODUCES (not just pre-existing ones), scored initial vs residual with HoC-ranked controls (intake Q6)"
        anchors: ['introduce', 'initial.{0,40}residual|residual risk']
        min_matches: 2
      - id: temporary-expiry-condition
        description: "Permanent/temporary is stated and a temporary change carries an expiry condition/date — temporary-without-expiry is flagged (intake Q4/Q4a)"
        anchors: ['temporary', 'expiry']
        min_matches: 1
      - id: pssr-startup-gate
        description: "The PSSR is the hard pre-start-up gate: start-up authorization is explicitly withheld/blocked while ANY PSSR item is open — no exceptions (the B6 criteria-as-runtime-gate core)"
        anchors: ['PSSR|pre.start.?up safety review', 'withheld|blocked|not authori']
        min_matches: 2
      - id: pssr-items-evidenced
        description: "The PSSR checklist covers PSI updated · procedures updated · training done · RA controls in place · equipment as-designed, each item evidenced (intake Q9)"
        anchors: ['PSI|process safety information', 'training', 'procedure']
        min_matches: 3
      - id: gate-signatories-as-roles
        description: "The change owner and the start-up (PSSR) authoriser are named as roles — the gate signatories (intake Q8, de-identified)"
        anchors: ['change owner', 'authoris|authoriz']
        min_matches: 2
      - id: moc-statutory-grounding
        description: "The MoC duty is grounded per jurisdiction — OSHA 1910.119(l) for a US covered process (KB-STD-PSM / KB-REG-US-OSHA), ISO 45001 8.1.3 as the management-system hook"
        anchors: ['1910\.119', 'ISO 45001', '8\.1\.3']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A package that documents the change but never gates it** — technical basis, affected
  documents, even an RA — yet no explicit start-up-withheld statement; the PSSR reads as
  a form to file rather than the authorization gate, which is the whole point of MoC.
- **A change RA of pre-existing hazards** — the assessment re-scores the unit's known
  hazards and never asks what THIS change newly introduces (the impeller swap's new
  deadhead pressure, the new material's compatibility).
- **The un-classified change** — no RIK/minor/significant triage anywhere, so nothing
  justifies the review depth chosen and a significant change quietly avoids its PHA.
- **Updates promised after start-up** — procedures/training marked "to follow"
  post-start-up while the package still authorizes; sequencing is the discipline.

## Sign-off note
SME review: ran (persona: MoC process-safety specialist); this is **decision-support only**.
It **precedes — and never replaces, never emits — the human competent-person sign-off**, and
it never outputs "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score
below threshold) are a separate enforcement class owned by the automated harness.
