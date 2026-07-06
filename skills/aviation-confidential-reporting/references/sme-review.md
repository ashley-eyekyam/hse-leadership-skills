---
sme-review:
  personas:
    - role: "Confidential-reporting (CHIRP/ASRS-style) scheme manager"
      expertise: "voluntary/confidential/anonymous reporting-scheme design, reporter-confidentiality custody, de-identification-at-intake workflows, feedback-loop design, the reporter-protection promise as a mechanical pre-condition"
      lens: "is reporter identity protection AIRTIGHT end-to-end — could a reader of the circulated design, or a downstream handler, re-identify the reporter — and does the feedback loop actually close?"
modes:
  reporting-scheme:
    detected_by: "Q2 — What scheme type? (Confidential / Voluntary / Anonymous) — the produced confidential-safety-reporting scheme design, ICAO Annex 19 Pillar 4"
    floor:
      - id: csr-reporter-protection-endtoend
        description: "Reporter-identity protection is airtight end-to-end — name, role/route/base/flight, exact dates AND narrative re-identifiers tokenised to role labels before the content is reasoned about; residual quasi-identifiers flagged"
        anchors: ['reporter.{0,12}identit', 'de.identif', 'role label', 'quasi.identif']
        min_matches: 2
      - id: csr-reid-key-custodian-separate
        description: "The re-identification key is held by a named custodian role, separate from the circulated design, and is NEVER embedded in the shared artifact (no name↔label mapping inside it)"
        anchors: ['re.identif', 'custodian', '\bkey\b']
        min_matches: 2
      - id: csr-scheme-type-consistent
        description: "The scheme type (confidential / voluntary / anonymous) is modelled and the handling workflow matches it, not a blend of the three"
        anchors: ['confidential', 'voluntary', 'anonymous']
        min_matches: 1
      - id: csr-feedback-loop-closes
        description: "The feedback loop is real and closes — reporters learn the outcome (de-identified bulletin / via-custodian / both); a scheme with intake but no feedback is flagged"
        anchors: ['feedback', 'outcome', 'bulletin', 'closed the loop']
        min_matches: 1
      - id: csr-no-disciplinary-routing
        description: "The design guarantees a report cannot be routed into a disciplinary/punitive process against the reporter, with de-id at the earliest point"
        anchors: ['disciplinar', 'punitive', 'not be used against', 'protection from']
        min_matches: 1
      - id: csr-protection-basis-cited
        description: "The legal protection basis is cited (India → DGCA CAR KB-REG-IN-DGCA / EU Reg 376-2014 / FAA ASAP / Annex 19 Appendix 3 principles + [GAP] legal-review flag), never asserting a protection the law does not grant"
        anchors: ['376', 'ASAP', 'Annex 19', 'DGCA', 'protection basis']
        min_matches: 1
      - id: csr-mor-interface
        description: "The interface with mandatory occurrence reporting (MOR) is stated — which events go to the voluntary scheme vs the mandatory channel, reconciled not blurred"
        anchors: ['mandatory occurrence', '\bMOR\b', 'occurrence report']
        min_matches: 1
---

# SME Review & Sign-off — aviation-confidential-reporting

This skill carries **one** SME lens, narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the "reporter identity protected … re-identification key held
separately" clause) to the confidential-reporting design; it is the family's confidentiality
keystone. One primary persona suffices — a CHIRP-style scheme manager already embodies the
dual confidentiality + scheme-design expertise; a 2nd lens would dilute it. Reporter
confidentiality is **load-bearing and de-id runs first**: a reporter-identity leak is the
hard de-id auto-fail, not a soft FLAG. The universal hard gates (de-id leak, citation
accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Reporter-identity protection is airtight end-to-end — name, role/route/base/flight, exact dates, AND narrative re-identifiers tokenised to role labels *before* the content is reasoned about; flag any residual quasi-identifier a determined reader could triangulate. Role labels only; no re-identification.
- [ ] The re-identification key is held by a *named custodian*, separate from the circulated design, and is NEVER embedded — flag any design that puts the key, or a name↔label mapping, inside the shared artifact.
- [ ] The scheme type is correctly modelled and consistent — confidential vs voluntary vs anonymous; the handling workflow must match the chosen type, not blend them incoherently.
- [ ] No disciplinary leakage — the design ensures a report cannot be routed into a disciplinary process against the reporter, and de-id happens at the earliest point.
- [ ] The feedback loop is real and closes — reporters learn the outcome (bulletin / via-custodian / both); a scheme with intake but no feedback is flagged.
- [ ] The reporter-protection promise is mechanical, not aspirational — backed by actual workflow steps, not a statement of intent; the legal protection basis is cited (India → DGCA CAR `KB-REG-IN-DGCA` / EU Reg 376/2014 / FAA ASAP / unknown → Annex 19 Appendix 3 principles + `[GAP]` legal-review flag), never asserting a protection the law does not grant. A de-id leak here is a hard-fail, distinct from a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The two channels that never meet** — the voluntary/confidential scheme and the mandatory
  occurrence-reporting channel are both described but never reconciled: which event types go
  where, what happens when a confidential report reveals a mandatorily-reportable occurrence,
  and how double-reporting is avoided.
- **The protection promise the scheme cannot mechanically keep** — the design asserts reporter
  protection as intent ("we value openness") without the workflow steps, access controls, and
  legal basis that make the promise enforceable; a promise the just-culture policy and the law
  cannot back is worse than none.
- **Record identity & basis** — the retention period, the feedback SLA, and the review cadence
  are stated without tying them to a dated basis or the custodian's access-control record, so
  the scheme cannot be audited against its own commitments.

## Sign-off note
SME review: ran (persona: Confidential-reporting (CHIRP-style) scheme manager — Annex 19
Pillar 4); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person (aviation-SME) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak — load-bearing for reporter
identity here — and invented citation) are a separate enforcement class.
