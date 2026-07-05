---
sme-review:
  personas:
    - role: "Rail ORR-submission lead / safety-authorisation application author"
      expertise: "ROGS 2006 application practice — the safety-authorisation / safety-certificate / Part-3-verification route, what a complete ORR application pack must contain, how an application REFERENCES the SMS without duplicating it, CSM-RA change evidence (significance test + risk-acceptance + independent AsBo), and ORR decision practice"
      lens: "would ORR accept this application for the CORRECT route (authorisation for an infrastructure manager, certificate for a transport operator, Part-3 for non-mainline), does it REFERENCE the SMS as an input rather than rebuild it, does it bind a real accountable duty-holder — not a generic template — and does it stay framed FOR submission rather than claiming it is already authorised?"
modes:
  application-pack:
    detected_by: "Q1 — What do you want this application work to do? (Assemble / Gap-check / Submission-format — all emit the one ROGS application pack; Q2 dutyholder type sets the authorisation/certificate/Part-3 route)"
    floor:
      - id: applicant-route-declared
        description: "The applicant identity and the CORRECT route are declared — infrastructure manager → safety authorisation; mainline transport operator → safety certificate; non-mainline → ROGS Part 3 verification (intake Q2, the route-determining question)"
        anchors: ['safety authorisation', 'infrastructure manager']
        min_matches: 2
      - id: sms-referenced-never-rebuilt
        description: "The pack REFERENCES the SMS (built by rail-safety-management-system, RAIL-01) as an input with its scope — it never re-authors the element set; a missing SMS is a literal [GAP] routed to RAIL-01 (intake Q3, the CONV-12 anchor)"
        anchors: ['rail-safety-management-system', 'SMS']
        min_matches: 2
      - id: pack-elements-populated
        description: "The application elements are present and populated with dutyholder-specific content — applicant identity & route declaration · SMS reference + scope · risk-control summary · CSM-RA change evidence · competence/Sentinel & ECM assurance · the declaration (KB-REG-ROGS application map)"
        anchors: ['declaration', 'risk.control summary']
        min_matches: 2
      - id: csm-ra-change-evidence
        description: "Where a significant change is in scope: the CSM-RA significance test, the risk-acceptance principle applied, and the independent AsBo evidence appear (intake Q6; KB-REG-CSM-RA)"
        anchors: ['CSM.?RA', 'AsBo']
        min_matches: 2
      - id: accountable-dutyholder-roles
        description: "The accountable duty-holder and safety-critical role-holders carry stated application accountabilities as role labels — no unfilled accountability (intake Q7)"
        anchors: ['accountable duty.?holder']
        min_matches: 1
      - id: risk-control-summary-sfairp
        description: "The risk-control summary ranks mitigations through the hierarchy of controls (SFAIRP); PPE/admin-only treatments carry the justification"
        anchors: ['SFAIRP|reasonably practicable', 'hierarchy of controls']
        min_matches: 2
      - id: framed-for-submission
        description: "The pack is framed FOR submission — it never states it is 'authorised / accepted / granted by ORR'; the decision status is reported as a fact only (intake Q10 discipline)"
        anchors: ['for submission', 'ORR']
        min_matches: 2
      - id: submission-timeline-recorded
        description: "The submission status and the application clock are recorded — target/actual submission state (e.g. 'not yet submitted') plus dated actions (or a literal [GAP]) (intake Q10/Q11)"
        anchors: ['not yet submitted|submission (date|deadline)|target date', 'due']
        min_matches: 2
---

# SME Review & Sign-off — safety-authorisation

This skill carries **one** SME lens, narrowing the rail-ORR-submission archetype
(`KB-SNIP-ARCHETYPES`). The application-author view and the route-correctness view are a
lens *within* the same reviewer, so a 2nd persona is not justified. The universal hard
gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The **dutyholder route is correct** — an **infrastructure manager** files a **safety authorisation**, a mainline **transport operator** a **safety certificate**, a non-mainline (tram/metro/heritage) operation a **ROGS Part 3 safety verification**. An authorisation where a certificate is required (or vice-versa) is the integrity-of-advice failure this skill must not make.
- [ ] The application **REFERENCES the SMS — it does NOT rebuild it.** The pack cites the SMS (built by `rail-safety-management-system`, RAIL-01) as an input; it must **not** re-author or regenerate the ROGS/ORR SMS element set. Flag any section that reconstructs the full SMS element set instead of referencing it. If the SMS does not exist, the pack must route the user to RAIL-01 and record the SMS as a `[GAP]` input (CONV-12).
- [ ] The application is framed **for-submission** — it **never states it is "authorised / accepted / approved / granted by ORR"**. ORR is the Safety Authority; granting the authorisation is its act. Flag any sentence that asserts the application has been authorised/accepted/granted by ORR.
- [ ] The **application elements are genuinely present and populated** with dutyholder-specific content — applicant identity & route declaration, the SMS reference + scope, the risk-control summary, the CSM-RA change evidence (where there is a significant change), competence/Sentinel & ECM assurance, the declaration. Flag any element that is a heading with no content.
- [ ] The **accountable duty-holder AND the safety-critical role-holders** are named roles with stated accountabilities (de-identified to role labels, but the *role* is filled) — an unfilled accountability is the indefensible copy-paste output.
- [ ] The **risk-control summary** ranks every mitigation through the hierarchy of controls (SFAIRP); any PPE/admin-only treatment carries the "higher-order not reasonably practicable" justification.
- [ ] **Dutyholder/operation specificity** — names *this* dutyholder and operation; a generic "a railway" application is flagged.
- [ ] **India** content cites the Railways Act 1989 / CRS framing and defers state-specific non-railway-depot content to `hse-india` after state detection — no national form invented.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A pack that quietly rebuilds the SMS** — pages of element content duplicated from (or
  invented in place of) the SMS instead of a scoped reference; the application doubles
  its review surface and drifts from the document it claims to demonstrate.
- **The route assumed, not resolved** — an 'authorisation' assembled for what is actually
  a mainline operator (certificate route); every downstream element inherits the wrong
  statutory frame and the whole submission bounces.
- **A declaration with no declarant accountability** — the formal declaration present as
  text but bound to no accountable duty-holder role; the one signature ORR reads first
  is the least anchored thing in the pack.
- **Change evidence without the AsBo** — the significance test argued, the risk-acceptance
  principle picked, and no independent assessment body anywhere; the CSM-RA limb fails
  precisely at its independence requirement.

## Sign-off note
SME review: ran (persona: Rail ORR-submission lead / safety-authorisation application
author — ROGS 2006 + CSM-RA); this is **decision-support only**. It **precedes — and never
replaces, never emits — the human competent-person (rail-SME / accountable-duty-holder)
sign-off**, and it never outputs the affirmative claim "approved by a competent person". A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation) are a separate enforcement class.
