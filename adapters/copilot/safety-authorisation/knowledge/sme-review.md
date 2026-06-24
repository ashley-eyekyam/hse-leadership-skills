---
sme-review:
  personas:
    - role: "Rail ORR-submission lead / safety-authorisation application author"
      expertise: "ROGS 2006 application practice — the safety-authorisation / safety-certificate / Part-3-verification route, what a complete ORR application pack must contain, how an application REFERENCES the SMS without duplicating it, CSM-RA change evidence (significance test + risk-acceptance + independent AsBo), and ORR decision practice"
      lens: "would ORR accept this application for the CORRECT route (authorisation for an infrastructure manager, certificate for a transport operator, Part-3 for non-mainline), does it REFERENCE the SMS as an input rather than rebuild it, does it bind a real accountable duty-holder — not a generic template — and does it stay framed FOR submission rather than claiming it is already authorised?"
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

## Sign-off note
SME review: ran (persona: Rail ORR-submission lead / safety-authorisation application
author — ROGS 2006 + CSM-RA); this is **decision-support only**. It **precedes — and never
replaces, never emits — the human competent-person (rail-SME / accountable-duty-holder)
sign-off**, and it never outputs the affirmative claim "approved by a competent person". A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation) are a separate enforcement class.
