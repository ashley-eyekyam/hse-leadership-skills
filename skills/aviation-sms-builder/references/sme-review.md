---
sme-review:
  personas:
    - role: "Aviation Safety Manager (SMS owner / accountable-manager advisor)"
      expertise: "ICAO Annex 19 four-pillar SMS design, SMS-acceptance submissions, State-Safety-Programme alignment (DGCA SSP / FAA / EASA), key-personnel accountabilities"
      lens: "would this manual be ACCEPTED by the certificating authority, and does it bind a real Accountable Manager to real accountabilities — not a generic template?"
---

# SME Review & Sign-off — aviation-sms-builder

This skill carries **one** SME lens, narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`) — this skill is the archetype's home artifact, so a 2nd lens is not
justified (the Accountable-Manager view is a lens *within* the same reviewer). The universal
hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Four pillars (Safety Policy & Objectives, Safety Risk Management, Safety Assurance, Safety Promotion) are genuinely present and populated with operator-specific content — flag any pillar that is a heading with no content.
- [ ] Accountable Manager AND Safety Manager are named roles with stated accountabilities (de-identified to role labels, but the *role* is filled) — an unfilled accountability is the indefensible copy-paste output.
- [ ] The four downstream artifacts (hazard register, SPI/SPT, just-culture, confidential-reporting) are *pointed to*, not silently re-authored or contradicted — flag scope creep where a pillar restates a sibling skill's detail.
- [ ] ERP / emergency-response coordination and SMS documentation control are addressed in Pillar 1, not dropped.
- [ ] State-programme alignment is cited, never invented — India → DGCA SSP (`KB-REG-IN-DGCA`), exact CAR number `[GAP]`-marked; FAA/EASA → the user-supplied reference, never a fabricated clause.
- [ ] Operator/operation specificity — names *this* operator type and operation; a generic "an airline" SMS is flagged.

## Sign-off note
SME review: ran (persona: Aviation Safety Manager — ICAO Annex 19 SMS owner); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person (aviation-SME / accountable-manager) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
