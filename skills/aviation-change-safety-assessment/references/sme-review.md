---
sme-review:
  personas:
    - role: "Aviation Management-of-Change (MoC) safety assessor"
      expertise: "Annex 19 Pillar 2 management of change, change-induced hazard identification, the ICAO 5x5, approve/decline decision discipline with recorded rationale"
      lens: "did this change get assessed for the NEW hazards it actually introduces, and is the approve/decline decision defensible on its recorded rationale?"
modes:
  change-assessment:
    detected_by: "Q2/Q3 — the change type + concrete description (the produced management-of-change safety assessment, ICAO Annex 19 Pillar 2)"
    floor:
      - id: moc-new-and-changed-hazards
        description: "New AND changed hazards are explicitly enumerated — a change declared 'low risk' without listing what it introduces or alters is the load-bearing failure mode"
        anchors: ['new.{0,8}hazard', 'changed hazard', 'hazard.{0,8}introduc', 'newly introduc']
        min_matches: 1
      - id: moc-each-hazard-5x5-scored
        description: "Each new/changed hazard is 5×5-scored (initial and residual) via the shared engine, not narratively dismissed"
        anchors: ['\b5.?5\b', 'severity', 'likelihood', 'risk (rating|class|index)']
        min_matches: 2
      - id: moc-transition-cutover-hazard
        description: "Latent transition / cut-over hazards are addressed — the change may be safe in steady state but hazardous during change-over (the nuanced MoC catch)"
        anchors: ['transition', 'cut.?over', 'phased', 'trial period', 'during the change']
        min_matches: 1
      - id: moc-approve-decline-owned
        description: "An explicit approve/decline decision with a recorded rationale and a named approval authority closes the assessment (intake Q10)"
        anchors: ['approv', 'declin', 'approval authority', 'recommendation']
        min_matches: 2
      - id: moc-mitigations-hoc-owned
        description: "Mitigations are HoC-ranked with PPE/admin-only flagged, and every mitigation carries a role owner and due date — a briefing card alone is never accepted for a hazardous change"
        anchors: ['hierarchy of controls', '\bPPE\b', 'briefing card', 'owner']
        min_matches: 1
      - id: moc-caa-reference-cited
        description: "Any DGCA CAR / FAA AC / EASA AMC reference is cited, never invented — India → KB-REG-IN-DGCA (exact CAR number [GAP] when unverified); an unconfirmable clause stays a literal [GAP]"
        anchors: ['\bCAR\b', 'DGCA', 'EASA', 'FAA', '\[GAP\]']
        min_matches: 1
      - id: moc-interim-bridge-residual
        description: "Where a residual risk remains elevated pending a control, an interim measure / bridging mitigation for the gap period is stated — an acknowledged-inadequate control with a far-dated fix and no interim step is a FLAG"
        anchors: ['interim', 'residual', 'pending', 'until']
        min_matches: 1
---

# SME Review & Sign-off — aviation-change-safety-assessment

This skill carries **one** SME lens, narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the "a change assessed without identifying new/changed hazards is
FLAGged" clause + 5×5 + decision-rationale) to the management-of-change assessment. The
universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated
actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] New AND changed hazards are explicitly identified — flag any assessment that declares a change "low risk" without enumerating what the change introduces or alters (the load-bearing failure mode).
- [ ] Each new/changed hazard is 5×5-scored via the shared engine (initial + residual), not narratively dismissed.
- [ ] The change is concrete and named — a vague "we're changing things" is refused at intake and must never reach output.
- [ ] An explicit approve / decline decision with a recorded rationale and a named approval authority closes the assessment — a MoC with no decision or no rationale is flagged.
- [ ] Mitigations HoC-ranked, PPE/admin-only flagged, every mitigation owner/date validated via `smart_actions`.
- [ ] Interaction effects / latent transition hazards — flag where the change is safe in steady state but hazardous during cut-over (the nuanced MoC check an experienced assessor catches).
- [ ] Any DGCA CAR / FAA AC / EASA AMC reference is cited, never invented — India → `KB-REG-IN-DGCA` (exact CAR number `[GAP]` when unverified); FAA/EASA/Other → the user-supplied reference; an unconfirmable clause stays literal `[GAP]`.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The high-severity change with no bridge** — a residual risk left elevated with the real
  control dated weeks or months out, no interim measure, and no ALARP/acceptable-for-now
  statement for the gap period. The assessment reads as complete while the operation runs
  exposed until the fix lands.
- **The missing contingency leg** — the change alters an operation (new destination, new
  procedure) but the assessment never asks what the emergency/diversion/contingency
  arrangements are for the changed condition, or whether the ERP still holds.
- **Prior-occurrence silence** — the change touches a hazard the operator (or the industry)
  has occurrence history on, and the assessment neither reviews that history nor confirms its
  absence, so the severity/likelihood scores rest on judgement alone.

## Sign-off note
SME review: ran (persona: Aviation MoC safety assessor — Annex 19 Pillar 2); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person (aviation-SME) sign-off**, and it never outputs the affirmative claim
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation) are a separate enforcement class.
