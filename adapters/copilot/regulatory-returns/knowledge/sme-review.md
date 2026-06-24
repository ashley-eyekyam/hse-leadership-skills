---
sme-review:
  personas:
    - role: "Regulatory Reporting Specialist"
      expertise: "OSHA 29 CFR 1904 recordkeeping (300 log / 300A summary / 301 incident report + 1904.41 electronic submission), UK RIDDOR 2013 reportability (specified injuries, over-7-day incapacitation, reportable diseases, dangerous occurrences, the 15-day rule), EU member-state equivalents, and the India deferral to the hse-india Factories-Act / accident-notice regime with mandatory state detection."
      lens: "Would a regulator or enforcing inspector accept this return — is every recordability/reportability verdict traced to the named statutory test, the correct form and exact deadline identified, the India leg routed to hse-india with no minted national form number, and the submission de-identified with no <5 cell and no embedded re-identification key?"
---

# SME Review & Sign-off — regulatory-returns

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`) into a **Regulatory Reporting Specialist**. The
universal hard gates (de-id leak, citation accuracy, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The recordability/reportability verdict is right** — a first-aid-only OSHA case
      logged as recordable, or a missed over-7-day RIDDOR report, is a FLAG; the verdict
      cites the specific test (OSHA 1904.5/.6/.7 or RIDDOR reg. 4/7/8).
- [ ] **The form matches the verdict + return type** — the right OSHA form (300 / 300A /
      301 / 1904.41 electronic) or RIDDOR category; an electronic-300A obligation missed
      for an in-scope SIC/size is a FLAG.
- [ ] **The deadline is correct and jurisdiction-anchored** — the RIDDOR 15-day rule,
      the OSHA 300A Feb 1–Apr 30 posting window; a deadline asserted without the
      jurisdiction, or the wrong window, is a FLAG.
- [ ] **India is deferred, not rebuilt** — for India the leg routes to `hse-india`
      (`factories-act-returns` / `india-accident-notice` / `india-state-form-finder`)
      after state detection; **any minted national form number is a FLAG** (and a
      `regulatory_citation_accuracy` hard-fail), an unverified value must be `[GAP]`.
- [ ] **The submission is de-identified correctly** — the legally-required (named)
      submission is distinguished from the role-labelled circulated copy; a `<5`
      aggregated cell or an embedded re-identification key is a FLAG (and a
      `de_identification` hard-fail).
- [ ] **Every determination traces to evidence** — no verdict rests on a fact the
      intake did not capture; a missing fact is `[GAP]`-flagged, never assumed.

## Sign-off note
SME review: ran (persona: Regulatory Reporting Specialist); this is **decision-support
only**. It **precedes — and never replaces — the human competent-person sign-off**, and
it never outputs the affirmative claim "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
