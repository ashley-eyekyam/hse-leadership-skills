---
sme-review:
  personas:
    - role: "Regulatory Reporting Specialist"
      expertise: "OSHA 29 CFR 1904 recordkeeping (300 log / 300A summary / 301 incident report + 1904.41 electronic submission), UK RIDDOR 2013 reportability (specified injuries, over-7-day incapacitation, reportable diseases, dangerous occurrences, the 15-day rule), EU member-state equivalents, and the India deferral to the hse-india Factories-Act / accident-notice regime with mandatory state detection."
      lens: "Would a regulator or enforcing inspector accept this return — is every recordability/reportability verdict traced to the named statutory test, the correct form and exact deadline identified, the India leg routed to hse-india with no minted national form number, and the submission de-identified with no <5 cell and no embedded re-identification key?"
modes:
  return:
    detected_by: "Q = the requested deliverable (a regulatory return / recordability determination for the named incident and jurisdiction) — single-output skill; this mode is always active"
    floor:
      - id: recordability-verdict-tested
        description: "Every recordability/reportability verdict traces to the named statutory test (OSHA 1904.7 / RIDDOR) — a verdict asserted without the test is a FLAG"
        anchors: ['recordab|reportab', '1904.7|riddor|statutory test|the test']
        min_matches: 2
      - id: form-matches-verdict
        description: "The form matches the verdict + return type (the right OSHA 300/300A/301 or RIDDOR form) — a form/verdict mismatch is a FLAG"
        anchors: ['form', '300|301|riddor|f2508']
        min_matches: 2
      - id: deadline-jurisdiction-anchored
        description: "The deadline is correct and jurisdiction-anchored (RIDDOR 15-day / 10-day, OSHA posting window) — a wrong or generic deadline is a FLAG"
        anchors: ['deadline|days|15-day|10-day|by ', 'riddor|osha|300a|jurisdiction']
        min_matches: 2
      - id: india-deferred-not-rebuilt
        description: "For India the leg routes to hse-india after state detection — no national form number is rebuilt/minted here"
        anchors: ['hse-india|india', 'defer|state|\[gap']
        min_matches: 2
      - id: submission-deidentified
        description: "The submission is de-identified correctly — the legally-required named fields are distinguished from de-id, no <5 cell, no embedded re-identification key"
        anchors: ['de-identif|de-id', '<5|re-identif|role label']
        min_matches: 2
      - id: determination-traces-evidence
        description: "Every determination traces to evidence — no verdict rests on a fact the record does not support"
        anchors: ['evidence', 'determination|verdict|trace']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The verdict with no statutory test (S6)** — a recordable/reportable call asserted without
  walking the actual test (OSHA 1904.7 general-recording criteria, RIDDOR's reportable-categories)
  reads confident and may be wrong; show the test applied, not just the conclusion.
- **The deadline that is generic, not anchored (S5)** — "report promptly" instead of the exact
  jurisdiction-anchored clock (RIDDOR 10-day/15-day, OSHA 8-hour fatality / posting window) leaves
  the duty-holder exposed to a missed statutory deadline.
- **The India national-form rebuild** — assembling an Indian return here instead of deferring to
  hse-india after state detection mints a form this skill must not invent; route it onward.
- **De-id over-redaction of a legally-named field** — the return has fields the law requires be
  named (the injured worker on some statutory forms); blanket de-id that strips a legally-required
  field is as wrong as leaking one. Distinguish the legally-named fields from the de-identified.

## Sign-off note
SME review: ran (persona: Regulatory Reporting Specialist); this is **decision-support
only**. It **precedes — and never replaces — the human competent-person sign-off**, and
it never outputs the affirmative claim "approved by a competent person". A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
