---
sme-review:
  personas:
    - role: "Bulk-storage / secondary-containment engineer"
      expertise: "secondary-containment sizing basis (largest-tank + freeboard, or the applicable local/PESO rule), incompatible-substance segregation, overfill protection (independent high-level trip), bund drainage + firewater retention/containment, DSEAR flammable-atmosphere area control"
      lens: "is the containment basis traced to a stated rule (not an assumed %); do segregation, overfill and firewater containment hold against the actual stored inventory"
modes:
  bund-sizing:
    detected_by: "Q1 — Scope (size/verify a bund, plan secondary containment, or review overfill/segregation controls)"
    floor:
      - id: tfb-sizing-from-rule
        description: "The containment sizing basis is stated and traced to a RULE (110% of the largest tank + freeboard, or the local/PESO rule) — an assumed percentage with no cited basis is a FLAG"
        anchors: ['containment sizing basis|sizing basis', 'from the rule|110%', 'not an assumed']
        min_matches: 1
      - id: tfb-segregation-incompatibility
        description: "Segregation respects chemical incompatibilities — incompatible stored substances are not in a shared bund without justification (KB-SNIP-HOC)"
        anchors: ['segregation', 'incompatib']
        min_matches: 1
      - id: tfb-overfill-independent
        description: "Overfill protection is INDEPENDENT of the operating level control — an independent high-level trip/alarm, not the same instrument as the level gauge; a single-point-of-failure scheme is a FLAG"
        anchors: ['overfill', 'independent', 'high.level']
        min_matches: 1
      - id: tfb-firewater-drainage-containment
        description: "Firewater + contaminated-drainage containment is addressed (interceptor/penstock, firewater runoff retained so it cannot escape to drain/watercourse) — omitting firewater containment is an environmental-release FLAG"
        anchors: ['firewater', 'drainage', 'interceptor|penstock|watercourse']
        min_matches: 1
      - id: tfb-bund-penetrations-integrity
        description: "Bund integrity / penetrations are considered — pipe penetrations, valves through the bund wall, bund-wall material vs the stored substance; an unreviewed penetration is a FLAG"
        anchors: ['penetration', 'bund.{0,4}integrity|integrity']
        min_matches: 1
      - id: tfb-controls-hoc-ranked
        description: "Controls are HoC-ranked — containment/segregation/engineering ahead of admin; an admin-only control for a bulk-storage hazard is hard-gate-adjacent (KB-SNIP-HOC)"
        anchors: ['hierarchy.of.controls', 'engineering']
        min_matches: 1
      - id: tfb-flammable-dsear
        description: "For a flammable inventory the DSEAR flammable-atmosphere area control is addressed (gasoline/low-flashpoint) — a flammable tank farm with no DSEAR area control is a FLAG (KB-STD-DSEAR)"
        anchors: ['DSEAR', 'flammable.atmosphere']
        min_matches: 1
---

# SME Review & Sign-off — tank-farm-bunding-controls

One lens suffices: a bulk-storage / secondary-containment engineer who traces the containment
basis to a stated rule (never an assumed percentage) and tests segregation, overfill and
firewater containment against the real stored inventory. The persona **narrows** the Chemical-
Process-Safety sector slot that extends the generic **HSE-SME-Reviewer** hook
(`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-
only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Containment sizing basis stated and traced to a rule — the basis (e.g. 110% of the largest tank + freeboard, or the local/PESO rule) named and resolved; an assumed percentage with no cited basis is a FLAG ("resolved from the rule, never an assumed percentage").
- [ ] Segregation respects chemical incompatibilities — incompatible stored substances not in a shared bund without justification; a segregation matrix ignoring stated incompatibilities is a FLAG.
- [ ] Overfill protection independent of the level control — an independent high-level trip/alarm, not the same instrument as the operating level gauge; a single-point-of-failure overfill scheme is a FLAG.
- [ ] Firewater + contaminated-drainage containment addressed — bund drainage controlled (interceptor/penstock), firewater runoff retained so it cannot escape to drain/watercourse; omitting firewater containment is a FLAG (an environmental-release omission).
- [ ] Bund integrity / penetrations considered — pipe penetrations, valves through the bund wall, bund-wall material vs the stored substance; an unreviewed penetration is a FLAG.
- [ ] Controls HoC-ranked — containment/segregation/engineering ahead of admin; an admin-only control for a bulk-storage hazard is **hard-gate-adjacent** (HoC) unless justified-or-escalated.
- [ ] India → state resolved before any PESO/state citation — the PESO pointer referenced (not re-authored; hse-process owns `KB-REG-IN-PESO`) and the state confirmed; a form cited without a confirmed state is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The capacity asserted with no rule (canary S5)** — a bund declared 'adequate' or '110%' with
  no required-vs-existing computation, no shortfall, and no freeboard/firewater allowance; the
  quantitative basis is the deliverable.
- **The environmental leg that never meets the process leg (canary S7)** — firewater runoff and
  contaminated drainage to the watercourse/drain assessed with the containment, not a bund
  reviewed in isolation from where a spill actually goes.
- **The emergency/loss-of-containment response absent (canary S1)** — spill/overfill/fire response,
  interceptor isolation, and notification for a release reaching the boundary receptor.
- **The single-point overfill scheme (assistive completeness)** — overfill 'protected' by the same
  instrument as the operating level gauge, with no independent high-level trip.

## Sign-off note
SME review: ran (persona: Bulk-storage / secondary-containment engineer); this is **decision-
support only**. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
