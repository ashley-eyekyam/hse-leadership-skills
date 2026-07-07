---
sme-review:
  personas:
    - role: "Chartered Ergonomist (CIEHF) / Occupational-Health Professional"
      expertise: "Manual-handling and posture risk assessment with the NIOSH lifting equation (RWL / Lifting Index), RULA and REBA (validated posture-scoring methods with published action levels), ISO 11228-1/-2/-3 and ISO/TR 12296, MSD control by task/workstation redesign and mechanisation, and special-category MSD/fitness-data confidentiality."
      lens: "Is each task named and specific, is every RULA/REBA/NIOSH score the deterministic engine's output (with its input parameters shown, not narrated), is every missing parameter a [GAP] not a guessed angle/weight, are controls driven up the hierarchy ABOVE PPE and ABOVE training (task/workstation redesign first — training is not a control for a biomechanical overload), and is there ZERO special-category MSD/fitness leak (no named back-injury/fitness note, no <5 symptom cell)?"
modes:
  ergonomics-assessment:
    detected_by: "Q1 — Hazard/method (a manual-handling or posture assessment producing an ergonomics report)"
    floor:
      - id: ergo-tasks-specific
        description: "Each scored item names the specific task/role and the workstation/SEG — a generic task ('general handling', 'the line') is a FLAG (KB-SNIP-MANUFACTURING-CLAUSE-MAP)"
        anchors: ['workstation', '\bSEG\b']
        min_matches: 1
      - id: ergo-score-engine-inputs-shown
        description: "Every score is the deterministic ergonomics engine's output with its captured input parameters shown (NIOSH RWL + Lifting Index / RULA / REBA and its multipliers) — never a free-text 'high risk' with no engine score"
        anchors: ['recommended weight limit|\bRWL\b', 'lifting index', 'multiplier']
        min_matches: 1
      - id: ergo-missing-params-gap
        description: "A missing parameter (posture angle, load weight, lift distance) is a [GAP] and the score is withheld — never a guessed value to complete a score"
        anchors: ['no parameter was invented', 'a missing required parameter']
        min_matches: 1
      - id: ergo-controls-redesign-before-training
        description: "Controls redesign the task before they train the worker — eliminate -> engineer/mechanise/aid -> admin -> training LAST; a high LI/score whose only control is manual-handling training is a FLAG (KB-SNIP-ERGO-CONTROLS / KB-SNIP-HOC)"
        anchors: ['training is not a control', 'lift.assist|positioner']
        min_matches: 1
      - id: ergo-action-bands-cited
        description: "The action level / LI interpretation is cited to the method (NIOSH equation / RULA / REBA / ISO 11228), not asserted (KB-STD-ISO11228)"
        anchors: ['NIOSH', 'ISO ?11228', 'RULA|REBA']
        min_matches: 1
      - id: ergo-special-category-deid
        description: "Special-category MSD/fitness data is protected — reported by role/SEG, <5 symptom cells suppressed, never circulated with names; a named fitness note or a <5 cell is a de-id hard-fail"
        anchors: ['special.category', 'de.identif', 'small.cell|<\s?5']
        min_matches: 1
---

# SME Review & Sign-off — ergonomics-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a **Chartered Ergonomist (CIEHF) / Occupational-Health
Professional**. The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only,
owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Tasks are specific** — each scored item names the task/role and the workstation; a generic task ("general handling", "the line") is a FLAG.
- [ ] **Every score comes from the engine, with its inputs shown** — RULA grand score + action level / REBA final score / NIOSH RWL + Lifting Index are the `ergonomics` engine's output, traceable to the captured parameters; a free-text "high RULA risk" with no engine score, or a number with no input parameters, is a FLAG (and a regulatory_citation_accuracy hard-fail).
- [ ] **Missing parameters are `[GAP]`s, not guesses** — a posture angle, a load weight, or a lift distance invented to complete a score is a FLAG; the assessment must record the `[GAP]` and request the measurement.
- [ ] **Controls redesign the task before they train the worker** — eliminate the handling → engineer the workstation / mechanise / add an aid → administrative rotation/limits → training LAST; a high RULA/REBA/LI whose only control is manual-handling training (with no redesign or mechanical aid) is a FLAG (training is not a control for a biomechanical overload).
- [ ] **Action bands cited to source** — the RULA/REBA action level / NIOSH LI interpretation is cited to the method (NIOSH equation / RULA / REBA / ISO 11228), not asserted.
- [ ] **Special-category MSD/fitness data is protected** — reported symptoms and fitness detail reported by role/SEG, `<5` symptom cells suppressed, never circulated with names; a named back-injury/fitness note or a `<5` cell is a FLAG (and a de_identification hard-fail).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The score with no inputs — a band asserted by silence (canary S5)** — a "high MSD risk"
  conclusion with no RWL/Lifting Index/RULA-REBA score and no captured parameters (load, reach,
  frequency, angle); the quantitative basis is the deliverable, not decoration.
- **The high LI with no interim bridge (canary S2)** — a Lifting Index well above 1.0 with a far
  redesign date and no interim measure (load reduction, rotation, two-person limit) for the gap
  period before the positioner/aid lands.
- **The regime named, its element set unswept (canary S6)** — ISO 11228 / NIOSH cited while the
  method's required inputs or the -1/-2/-3 scope (lifting vs push-pull vs repetitive) are not
  actually swept for the task.
- **Surveillance/symptom linkage absent (canary S3)** — reported MSD symptoms in the SEG neither
  reviewed nor their absence confirmed, and no symptom-triggered re-assessment trigger set.
- **The single-point score (19-08 audit)** — origin is scored but the CONTROLLING condition
  (destination / worst-case reach) and the MAXIMUM foreseeable load are left unscored, and any
  supplementary posture method (RULA/REBA) an overhead or awkward placement demands is absent; an
  origin-only NIOSH LI understates the demand.

## Sign-off note
SME review: ran (persona: Chartered Ergonomist (CIEHF) / Occupational-Health Professional);
this is **decision-support only**. It **precedes — and never replaces — the human
competent-person review**, and it never outputs the affirmative claim that the work is approved.
A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
