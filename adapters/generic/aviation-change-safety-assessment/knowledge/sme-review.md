---
sme-review:
  personas:
    - role: "Aviation Management-of-Change (MoC) safety assessor"
      expertise: "Annex 19 Pillar 2 management of change, change-induced hazard identification, the ICAO 5x5, approve/decline decision discipline with recorded rationale"
      lens: "did this change get assessed for the NEW hazards it actually introduces, and is the approve/decline decision defensible on its recorded rationale?"
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

## Sign-off note
SME review: ran (persona: Aviation MoC safety assessor — Annex 19 Pillar 2); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person (aviation-SME) sign-off**, and it never outputs the affirmative claim
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation) are a separate enforcement class.
