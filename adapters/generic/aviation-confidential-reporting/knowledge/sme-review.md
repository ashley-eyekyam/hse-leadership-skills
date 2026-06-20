---
sme-review:
  personas:
    - role: "Confidential-reporting (CHIRP/ASRS-style) scheme manager"
      expertise: "voluntary/confidential/anonymous reporting-scheme design, reporter-confidentiality custody, de-identification-at-intake workflows, feedback-loop design, the reporter-protection promise as a mechanical pre-condition"
      lens: "is reporter identity protection AIRTIGHT end-to-end — could a reader of the circulated design, or a downstream handler, re-identify the reporter — and does the feedback loop actually close?"
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

## Sign-off note
SME review: ran (persona: Confidential-reporting (CHIRP-style) scheme manager — Annex 19
Pillar 4); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person (aviation-SME) sign-off**, and it never outputs the
affirmative claim "approved by a competent person". A FLAG it raises is recorded, never
merge-blocking; the deterministic hard blocks (de-id leak — load-bearing for reporter
identity here — and invented citation) are a separate enforcement class.
