---
sme-review:
  personas:
    - role: "Rail Safety Management System owner / ORR-aware safety assurance lead"
      expertise: "ROGS 2006 SMS design + the safety-certificate / safety-authorisation / Part-3-verification route, CSM-RA significance test + risk-acceptance principles + independent AsBo, competence/Sentinel + ECM maintenance, ORR acceptance practice"
      lens: "would this SMS be ACCEPTED by ORR for the CORRECT route (certificate vs authorisation vs Part-3 verification), does it bind a real accountable duty-holder to real accountabilities — not a generic template — and does it stay framed FOR acceptance rather than claiming it is already accepted?"
modes:
  sms-manual:
    detected_by: "Q1 — What do you want this SMS work to do? (Build / Review / Submission — all emit the ROGS element-set SMS manual; Q2 dutyholder type sets the certificate/authorisation/Part-3 route the manual is framed against)"
    floor:
      - id: dutyholder-route-resolved
        description: "The route is resolved from the dutyholder type and stated — mainline transport operator → safety certificate; infrastructure manager → safety authorisation; non-mainline (tram/metro/heritage) → ROGS Part 3 verification (intake Q2, the route-determining question)"
        anchors: ['safety certificate', 'safety authorisation', 'Part.?3']
        min_matches: 1
      - id: rogs-elements-populated
        description: "The ROGS/ORR element set is present AND populated with operator-specific content — policy · accountabilities · risk-control arrangements · CSM-RA change interface · competence/Sentinel · asset/ECM maintenance · emergency · monitoring/audit · continuous improvement; a heading with no content fails (KB-REG-ROGS element map)"
        anchors: ['ROGS', 'continuous improvement', 'monitoring']
        min_matches: 2
      - id: accountable-dutyholder-bound
        description: "The accountable duty-holder (the defining ROGS appointment) and the safety-critical roles are bound to stated accountabilities as role labels — no unfilled accountability (intake Q5)"
        anchors: ['accountable duty.?holder', 'accountabilit']
        min_matches: 2
      - id: csm-ra-change-interface
        description: "The change element names the CSM-RA significance test, the three risk-acceptance principles, and the independent AsBo — not a vague 'we manage change' (intake Q6; KB-REG-CSM-RA)"
        anchors: ['CSM.?RA', 'AsBo', 'risk.acceptance']
        min_matches: 2
      - id: competence-sentinel-ecm-present
        description: "Competence management (Sentinel where applicable) and asset/ECM maintenance arrangements are populated with the operator's facts (intake Q7)"
        anchors: ['Sentinel|competence management', 'ECM|entity in charge of maintenance']
        min_matches: 2
      - id: risk-controls-sfairp-hoc
        description: "The risk-control arrangements rank every mitigation through the hierarchy of controls (SFAIRP); any PPE/admin-only treatment carries the 'higher order not reasonably practicable' justification"
        anchors: ['SFAIRP|so far as is reasonably practicable|reasonably practicable', 'hierarchy of controls']
        min_matches: 2
      - id: framed-for-acceptance
        description: "The SMS is framed FOR acceptance by the Safety Authority — it never states it is 'accepted by ORR'; acceptance status is reported as a fact only (intake Q10 discipline)"
        anchors: ['for acceptance|for.acceptance', 'ORR']
        min_matches: 2
      - id: review-cadence-stated
        description: "The SMS states its review/revision cadence (annual / biennial / on-change) per intake Q8 — the continuous-improvement clock"
        anchors: ['review (cadence|cycle)|annual review|biennial']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **Element headings standing in for arrangements** — all nine ROGS elements present as
  sections, several populated only with policy prose; the manual demonstrates awareness
  of the element set while containing no operator-specific arrangement a regulator could
  verify.
- **Accountabilities that name structures, not duties** — an organogram and role list with
  no stated accountability per role; the defining ROGS appointment (the accountable
  duty-holder) is described but bound to nothing.
- **A change section without the CSM-RA machinery** — 'changes are risk assessed' with no
  significance test, no risk-acceptance principle, no AsBo; the one legally-prescribed
  change mechanism is the part most often paraphrased away.
- **The monitoring loop without teeth** — audit/monitoring described with no cadence, no
  nonconformity route, and no link back into continuous improvement; the SMS cannot
  learn.

## Sign-off note
SME review: ran (persona: Rail SMS owner / ORR-aware assurance lead — ROGS 2006 + CSM-RA);
this is **decision-support only**. It **precedes — and never replaces, never emits — the
human competent-person (rail-SME / accountable-duty-holder) sign-off**, and it never outputs
the affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
