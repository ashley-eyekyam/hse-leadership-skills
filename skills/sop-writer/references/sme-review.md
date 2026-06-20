---
sme-review:
  personas:
    - role: "Operations / technical-procedure author (safe-work-procedure specialist)"
      expertise: "SOP/SWP authoring, ISO 45001 8.1 operational control, embedding controls into procedure steps, literacy-level calibration, revision/approval control, and RA/JSA ingestion."
      lens: "Are controls embedded INTO each risk-bearing step (not a generic PPE list at the end), the higher-order controls the procedure sits within surfaced, and is it written to the stated reader's literacy level — never re-scoring the ingested risk?"
---

# SME Review & Sign-off — sop-writer

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into an operations / procedure-writing SME. The load-bearing
subtlety this persona holds: the procedure is itself an administrative control, so it must
surface (not stand in for) the higher-order controls it operates within. The universal hard
gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Controls are embedded per step, not appended — a flat "wear your PPE" list at the end is the signature SOP FLAG.
- [ ] The procedure is not presented as the sole defence — surface the higher-order controls it operates within (e.g. line de-energised & locked out before steps begin).
- [ ] Steps are real, ordered, one action each — "work safely at all times" boilerplate is refused, not authored.
- [ ] Literacy calibration matches the stated reader — a register mismatch to the literacy level captured at intake is a FLAG.
- [ ] It ingests the RA/JSA and does NOT re-score — a re-scored risk is a FLAG (sop-writer uses `controls` only).
- [ ] Roles + competencies are named (roles, not names) and emergency provisions are present.
- [ ] Revision/approval control is complete — SOP id, version, effective date, author/reviewer/approver roles, review cycle; no cycle → "review on change or at minimum annually" recorded as an `[ASSUMPTION]`.

## Sign-off note
SME review: ran (persona: Operations / technical-procedure author); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
