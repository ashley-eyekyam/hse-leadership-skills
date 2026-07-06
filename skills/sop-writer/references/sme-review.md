---
sme-review:
  personas:
    - role: "Operations / technical-procedure author (safe-work-procedure specialist)"
      expertise: "SOP/SWP authoring, ISO 45001 8.1 operational control, embedding controls into procedure steps, literacy-level calibration, revision/approval control, and RA/JSA ingestion."
      lens: "Are controls embedded INTO each risk-bearing step (not a generic PPE list at the end), the higher-order controls the procedure sits within surfaced, and is it written to the stated reader's literacy level — never re-scoring the ingested risk?"
modes:
  sop:
    detected_by: "Q12 — Output document type (Full SOP / Short work instruction / Procedure within a manual); Q4 sets the hazard/control source (ingest JSA/RA or elicit). The floor applies to every procedure."
    floor:
      - id: controls-embedded-per-step
        description: "Controls are embedded INTO each risk-bearing step, not appended as a flat 'wear your PPE' list at the end (the signature SOP failure)"
        anchors: ['step', 'control', 'hazard']
        min_matches: 2
      - id: higher-order-controls-surfaced
        description: "The higher-order controls the procedure operates within are surfaced — the SOP is never presented as the sole defence (e.g. line de-energised & locked out before the steps begin)"
        anchors: ['isolat|lockout|loto|de.energ|permit']
        min_matches: 1
      - id: steps-real-ordered
        description: "Steps are real, ordered, one action each — 'work safely at all times' boilerplate is refused, not authored (intake Q8 specificity anchor)"
        anchors: ['step', 'procedure']
        min_matches: 2
      - id: literacy-calibrated
        description: "The register matches the stated reader's literacy level (frontline operator = plain short imperatives) — a mismatch to the captured level is a miss (intake Q10; KB-SNIP-AUDIENCE)"
        anchors: ['operator', 'plain|imperative|frontline|short']
        min_matches: 1
      - id: no-rescore-ingested-risk
        description: "An ingested RA/JSA is used for its controls and NOT re-scored — sop-writer consumes the risk rating, it does not recompute it (intake Q4 ingest gate)"
        anchors: ['jsa|risk assessment', 'control']
        min_matches: 2
      - id: roles-emergency-provisions
        description: "Roles and competencies are named (role labels), and emergency / abnormal-stop provisions are present (intake Q9)"
        anchors: ['role|competen', 'emergency|abnormal|stop']
        min_matches: 2
      - id: revision-approval-control
        description: "The revision/approval block is complete — SOP id, version, effective date, author/reviewer/approver roles, review cycle (intake Q11)"
        anchors: ['revision|version', 'review', 'approv']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **PPE list at the end, not controls in the steps** — the signature SOP failure: a tidy
  procedure with a generic PPE block appended, so the risk-bearing step carries no embedded
  control at the point of the action.
- **The missing abnormal/emergency leg** (canary S1) — the SOP covers the normal task but
  has no stop conditions, no abnormal-situation response, no emergency shutdown or spill/exposure
  step; the operator has no instruction for when it goes wrong.
- **The procedure as sole defence** — the higher-order controls the SOP sits within
  (isolation/LOTO, permit, engineering guard) are not surfaced, so the reader believes the
  written steps are the whole safety case.
- **Register mismatch** — written above the stated reader's literacy level (dense technical
  prose for a frontline operator), so the people who must follow it cannot.
- **Silent re-scoring** — the ingested RA/JSA risk quietly recomputed instead of consumed;
  sop-writer must not re-rate the risk.

## Sign-off note
SME review: ran (persona: Operations / technical-procedure author); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
