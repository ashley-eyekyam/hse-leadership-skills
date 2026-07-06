---
sme-review:
  personas:
    - role: "Aviation Safety Manager (SMS owner / accountable-manager advisor)"
      expertise: "ICAO Annex 19 four-pillar SMS design, SMS-acceptance submissions, State-Safety-Programme alignment (DGCA SSP / FAA / EASA), key-personnel accountabilities"
      lens: "would this manual be ACCEPTED by the certificating authority, and does it bind a real Accountable Manager to real accountabilities — not a generic template?"
modes:
  sms-manual:
    detected_by: "Q1 — What do you want this SMS work to do? == Build (a new SMS manual: the four-pillar ICAO Annex 19 manual, the primary produced artifact)"
    floor:
      - id: sms-four-pillars-populated
        description: "All four ICAO Annex 19 pillars (Safety Policy & Objectives, Safety Risk Management, Safety Assurance, Safety Promotion) are present AND populated with operator-specific content — a pillar that is a heading with no operator arrangement is the copy-paste failure (KB-SNIP-ARCHETYPES Aviation-SMS)"
        anchors: ['four pillar', 'Safety Policy', 'Safety Risk Management', 'Safety Assurance', 'Safety Promotion']
        min_matches: 3
      - id: sms-accountable-safety-manager-bound
        description: "The two defining Annex 19 appointments — Accountable Manager AND Safety Manager — appear as roles with stated accountabilities (de-identified to role labels, but the role is filled), never an unfilled accountability"
        anchors: ['Accountable Manager', 'Safety Manager']
        min_matches: 2
      - id: sms-ssp-alignment-cited
        description: "State Safety Programme alignment is cited, never invented — India → DGCA SSP (KB-REG-IN-DGCA) with the exact CAR number [GAP]-marked; FAA/EASA → the user-supplied reference"
        anchors: ['State Safety Programme', '\bSSP\b', 'DGCA']
        min_matches: 1
      - id: sms-erp-and-doc-control
        description: "Emergency-response-plan coordination AND SMS documentation/record control are addressed in Pillar 1, not dropped — the operational-continuity leg an accepted manual must carry"
        anchors: ['emergency response', '\bERP\b', 'document control', 'record.retention']
        min_matches: 1
      - id: sms-downstream-artifacts-pointed
        description: "The four downstream artifacts (hazard register, SPI/SPT, just-culture, confidential-reporting) are pointed to, not silently re-authored or contradicted — flag scope creep where a pillar restates a sibling skill's detail"
        anchors: ['hazard register', '\bSPI', 'just.culture', 'confidential.report']
        min_matches: 2
      - id: sms-mitigations-hoc-ranked
        description: "Pillar-2 Safety Risk Management ranks mitigations through the hierarchy of controls, with no lower-order (PPE/admin)-only treatment presented as a complete control"
        anchors: ['hierarchy of controls', 'higher.order', 'elimination', 'engineering control']
        min_matches: 1
      - id: sms-review-cadence-stated
        description: "A manual review/revision cadence is stated (intake Q8), not left open — an SMS manual with no stated review cycle is unmanaged"
        anchors: ['review', 'revision', 'cadence', 'annual']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The Annex-19 regime named, its element set unswept** — the manual cites ICAO Annex 19 /
  the DGCA SSP but leaves the mandated element set as fluent headings: the safety-policy
  accountability signature, the SRM hazard-identification procedure, the SPI linkage, the
  competence/training arrangements, MOC, and continuous improvement each need an
  operator-specific arrangement, not commitment prose. A manual whose sections are policy
  statements binds no one to anything a certificating authority could verify.
- **The missing emergency leg** — the SMS references safety throughout but never binds itself
  to the operator's Emergency Response Plan: activation triggers, the SMS↔ERP interface,
  crisis roles, and the post-event review that feeds Safety Risk Management. An accepted SMS
  manual is an operational document; an emergency-response-blind manual is incomplete.
- **Scope honesty / leg interaction** — a pillar silently re-authors (and risks
  contradicting) a downstream sibling artifact (the hazard register, SPI framework,
  just-culture policy, confidential-reporting scheme) instead of pointing to it, so two
  documents drift out of agreement.

## Sign-off note
SME review: ran (persona: Aviation Safety Manager — ICAO Annex 19 SMS owner); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person (aviation-SME / accountable-manager) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak, invented citation) are a separate
enforcement class.
