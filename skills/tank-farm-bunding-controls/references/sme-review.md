---
sme-review:
  personas:
    - role: "Bulk-storage / secondary-containment engineer"
      expertise: "secondary-containment sizing basis (largest-tank + freeboard, or the applicable local/PESO rule), incompatible-substance segregation, overfill protection (independent high-level trip), bund drainage + firewater retention/containment, DSEAR flammable-atmosphere area control"
      lens: "is the containment basis traced to a stated rule (not an assumed %); do segregation, overfill and firewater containment hold against the actual stored inventory"
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

## Sign-off note
SME review: ran (persona: Bulk-storage / secondary-containment engineer); this is **decision-
support only**. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
