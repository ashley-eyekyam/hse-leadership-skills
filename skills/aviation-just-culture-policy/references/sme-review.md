---
sme-review:
  personas:
    - role: "Just-culture / human-factors specialist"
      expertise: "Annex 19 Pillar 4 safety promotion, the substitution test, the culpability ladder (honest error → at-risk → reckless → negligent), Reason/Hudson just-culture models"
      lens: "can a reviewer APPLY this decision tree to a real case and get a defensible, consistent verdict — or is it a slogan?"
    - role: "Aviation HR / employment-law-aware reviewer"
      expertise: "the disciplinary-vs-safety boundary, protection of reporters from punitive action for honest error, alignment of the policy's consequences with employment process"
      lens: "does the policy protect honest error and at-risk behaviour from punitive action while leaving a defensible route for genuinely reckless/negligent conduct — without creating an employment-law trap?"
modes:
  policy-document:
    detected_by: "Q1/Q5 — draft or revise a just-culture policy + the decision-tree basis (substitution test / culpability ladder) — the produced just-culture policy document"
    floor:
      - id: jc-applicable-decision-line
        description: "An explicit, applicable decision line exists — substitution test and/or culpability ladder — that a reviewer can APPLY to a real case, not a 'we have a just culture' statement"
        anchors: ['substitution test', 'culpability', 'decision tree', 'decision line']
        min_matches: 1
      - id: jc-four-culpability-bands
        description: "The four culpability bands (honest error, at-risk, reckless, negligent) are distinguished with criteria a reviewer can apply, not just labels"
        anchors: ['honest error', 'at.risk', 'reckless', 'negligent']
        min_matches: 3
      - id: jc-protected-vs-actionable
        description: "The reporting/disciplinary boundary is stated — what is protected (honest error, most at-risk behaviour) vs what may attract action (reckless/negligent), and WHO decides"
        anchors: ['protect', 'disciplinar', 'boundary', 'may attract']
        min_matches: 1
      - id: jc-substitution-test-correct
        description: "The substitution test is correctly framed — 'would a peer in the same situation with the same information have done the same?' — flag a mis-stated or inverted test"
        anchors: ['substitution test', 'peer', 'same (situation|information)']
        min_matches: 1
      - id: jc-interlocks-confidential-reporting
        description: "The policy interlocks with, but does not duplicate, the confidential-reporting scheme — it points to aviation-confidential-reporting for the mechanics and makes only a promise the scheme can mechanically keep"
        anchors: ['confidential.report', 'interlock', 'reporting (scheme|system)']
        min_matches: 1
      - id: jc-protection-basis-cited
        description: "The legal protection basis is cited, never invented — India → DGCA CAR (KB-REG-IN-DGCA); EU → Reg 376/2014; FAA → ASAP; unknown → ICAO Annex 19 Appendix 3 principles + [GAP] legal-review flag"
        anchors: ['376', 'ASAP', 'Annex 19', 'DGCA', 'protection']
        min_matches: 1
      - id: jc-worked-example-deidentified
        description: "Any worked example uses role labels only — no individual named, no real case re-identified (de-id runs first)"
        anchors: ['role label', 'de.identif', 'example', 'scenario']
        min_matches: 1
---

# SME Review & Sign-off — aviation-just-culture-policy

This skill carries **two** SME lenses, both narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the "just culture has a line" clause) to the just-culture
artifact. A 2nd lens is justified because the culpability line is simultaneously a
**human-factors judgement** AND has **employment/disciplinary-law consequences** — two
distinct professions own two distinct failure modes (a slogan with no applicable line vs
an employment-law trap). The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] An explicit, applicable decision line exists — substitution test and/or culpability ladder — not a "we have a just culture" statement.
- [ ] The four culpability bands (honest error, at-risk, reckless, negligent) are distinguished with criteria a reviewer can apply, not just labels.
- [ ] The reporting/disciplinary boundary is stated — what is protected (honest error, most at-risk behaviour) vs what may attract action (reckless/negligent), and *who* decides.
- [ ] Any worked example uses role labels only — no individual named, no real case re-identified (de-id runs first; the recurring confidentiality check).
- [ ] The policy interlocks with, but does not duplicate, the confidential-reporting scheme — it points to `aviation-confidential-reporting` for the mechanics, and the promise it makes is one the scheme can mechanically keep.
- [ ] The substitution test is correctly framed — "would a *peer* in the same situation with the same information have done the same?" — flag a mis-stated or inverted substitution test.
- [ ] The legal protection basis is cited, never invented — India → DGCA CAR (`KB-REG-IN-DGCA`); EU → Reg 376/2014; FAA → ASAP; unknown → drafted to ICAO Annex 19 Appendix 3 principles only and flagged `[GAP]` for legal review. The policy never asserts a reporter protection the jurisdiction's law does not grant.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The regime named, its governance element set unswept** — the policy states a decision tree
  but never names who convenes and owns the just-culture panel, the appeal/review route, the
  interface with the drug-and-alcohol and disciplinary procedures, or how a verdict is
  recorded and audited. The line exists; the machinery to apply it defensibly does not.
- **The promise the scheme cannot keep** — the policy asserts a protection (anonymity,
  non-disclosure) that the confidential-reporting scheme or the jurisdiction's law cannot
  mechanically deliver, creating an undeliverable commitment and an employment-law trap.
- **Scope-honesty on the disciplinary boundary** — the policy protects reporting but leaves
  the reckless/negligent boundary and the burden of proof vague, so in practice either
  everything is punished or nothing is — the two failure modes a real panel meets.

## Sign-off note
SME review: ran (persona: Just-culture / human-factors specialist, with an aviation
HR / employment-law lens — Annex 19 Pillar 4); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person (aviation-SME /
accountable-manager) sign-off**, and it never outputs the affirmative claim "approved by a
competent person". The employment-law lens is advisory framing only; the universal "not
legal advice" disclaimer still governs. A FLAG it raises is recorded, never merge-blocking;
the deterministic hard blocks (de-id leak, invented citation) are a separate enforcement class.
