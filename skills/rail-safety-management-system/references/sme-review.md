---
sme-review:
  personas:
    - role: "Rail Safety Management System owner / ORR-aware safety assurance lead"
      expertise: "ROGS 2006 SMS design + the safety-certificate / safety-authorisation / Part-3-verification route, CSM-RA significance test + risk-acceptance principles + independent AsBo, competence/Sentinel + ECM maintenance, ORR acceptance practice"
      lens: "would this SMS be ACCEPTED by ORR for the CORRECT route (certificate vs authorisation vs Part-3 verification), does it bind a real accountable duty-holder to real accountabilities — not a generic template — and does it stay framed FOR acceptance rather than claiming it is already accepted?"
---

# SME Review & Sign-off — rail-safety-management-system

This skill carries **one** SME lens, narrowing the rail-SMS archetype
(`KB-SNIP-ARCHETYPES`) — this skill is the archetype's home artifact (the hse-rail
keystone), so a 2nd lens is not justified (the accountable-duty-holder view is a lens
*within* the same reviewer). The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The **dutyholder route is correct** — a mainline transport operator carries a **safety certificate**, an infrastructure manager a **safety authorisation**, a non-mainline (tram/metro/heritage) operation a **ROGS Part 3 safety verification**. A certificate where an authorisation is required (or vice-versa) is the integrity-of-advice failure this skill must not make.
- [ ] The **SMS is framed for-acceptance** — it **never states it is "accepted by ORR"**. ORR is the Safety Authority; acceptance is its act. Flag any sentence that asserts the SMS / certificate / authorisation has been accepted/approved/granted by ORR.
- [ ] The **ROGS/ORR element set is genuinely present and populated** with operator-specific content — policy, accountabilities, risk-control arrangements, CSM-RA change interface, competence/Sentinel, asset/ECM maintenance, emergency, monitoring/audit, continuous improvement. Flag any element that is a heading with no content.
- [ ] The **accountable duty-holder AND the safety-critical role-holders** are named roles with stated accountabilities (de-identified to role labels, but the *role* is filled) — an unfilled accountability is the indefensible copy-paste output.
- [ ] The **CSM-RA change element** (where there is a significant change) names the significance test, the three risk-acceptance principles, and the **independent AsBo** — not a vague "we manage change".
- [ ] **Risk-control arrangements** rank every mitigation through the hierarchy of controls (SFAIRP); any PPE/admin-only treatment carries the "higher-order not reasonably practicable" justification.
- [ ] **Operator/operation specificity** — names *this* dutyholder and operation; a generic "a railway" SMS is flagged.
- [ ] **India** content cites the Railways Act 1989 / CRS framing and defers state-specific non-railway-depot content to `hse-india` after state detection — no national form invented.

## Sign-off note
SME review: ran (persona: Rail SMS owner / ORR-aware assurance lead — ROGS 2006 + CSM-RA);
this is **decision-support only**. It **precedes — and never replaces, never emits — the
human competent-person (rail-SME / accountable-duty-holder) sign-off**, and it never outputs
the affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
