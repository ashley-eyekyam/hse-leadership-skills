---
sme-review:
  personas:
    - role: "Senior HSE Manager / Director"
      expertise: "ISO 45001:2018 clause 5.2 OH&S-policy requirements, management-system policy architecture, top-management commitment and accountability, the hierarchy of controls, and the difference between a defensible context-fit policy and recited boilerplate."
      lens: "would this policy survive a certification or regulator's challenge — all five mandatory clause-5.2 commitments present, every commitment appropriate to THIS organisation's purpose/size/context and its actual significant risks (not boilerplate), the hazard-elimination commitment ranked up the hierarchy of controls (never PPE-only), documented/communicated/signed by top management, and the statutory written-policy duty correctly resolved (India deferred to hse-india, no national-form minted) — while never reading as a final legal document"
modes:
  policy-statement:
    detected_by: "Q1 — Standard selector (ISO 45001 / ISO 14001 / ISO 45003 / Combined) — the produced signable HSE policy document at clause 5.2"
    floor:
      - id: pol-five-clause52-commitments
        description: "All five mandatory ISO 45001 clause-5.2 commitments are present and explicit: (1) framework for OH&S objectives; (2) fulfil legal + other requirements; (3) eliminate hazards & reduce OH&S risks; (4) continual improvement; (5) consultation & participation of workers — a missing commitment is a citation hard-fail"
        anchors: ['objective', 'legal.{0,20}requirement', 'eliminate hazard', 'continual improvement', 'consultation']
        min_matches: 3
      - id: pol-context-fit-not-boilerplate
        description: "Every commitment ties to the named org's actual risks and scale (appropriate to its purpose, size and context) — a commitment that recites the standard but names no real hazard is re-anchored"
        anchors: ['appropriate to', 'significant risk', 'context', 'purpose']
        min_matches: 1
      - id: pol-hoc-elimination
        description: "The hazard-elimination commitment (3) is phrased up the hierarchy of controls (KB-SNIP-HOC) — never a PPE-only or admin-only statement"
        anchors: ['hierarchy of controls', 'eliminat', 'higher.order', 'reduce.{0,10}risk']
        min_matches: 1
      - id: pol-documented-communicated-signed
        description: "The policy is documented, communicated, available to interested parties, and signed by top management (a named role/title, not personal data) — clause 5.2 requires demonstrated top-management commitment"
        anchors: ['communicat', 'signed', 'top management', 'available']
        min_matches: 2
      - id: pol-statutory-duty-resolved
        description: "The statutory written-policy duty is resolved as a branch beside the policy (UK HSWA s.2(3) etc.); India deferred to hse-india with state detection, no national-form number minted, [GAP] when unverified"
        anchors: ['statutory', 'HSWA', 'hse.india', '\[GAP\]', 'written.{0,6}policy']
        min_matches: 1
      - id: pol-decision-support-framing
        description: "The signed policy is framed as decision-support, claims no final regulatory clearance, and remains subject to the organisation's own competent-person review — it does not read as a final legal document"
        anchors: ['decision.support', 'competent.person', 'not.{0,20}legal', 'review']
        min_matches: 1
---

# SME Review & Sign-off — hse-policy-generator

The reviewer adopts the **Senior HSE Manager / Director** persona. This is a senior HSE
leader who signs off OH&S policies for certification and board scrutiny and knows the
difference between a clause-5.2-conformant, context-fit policy and recited boilerplate.

## Domain checklist (the nuanced things only this expert catches)
- [ ] All **five mandatory ISO 45001 clause-5.2 commitments** are present and explicit:
      (1) framework for setting OH&S objectives; (2) fulfil legal + other requirements;
      (3) eliminate hazards & reduce OH&S risks; (4) continual improvement of the OH&S MS;
      (5) consultation & participation of workers. A **missing commitment is a
      `regulatory_citation_accuracy` hard-fail** — never silently dropped.
- [ ] **Context-fit, not boilerplate** — every commitment ties to the **named org's actual
      risks and scale** (appropriate to its purpose, size and context). A commitment that
      recites the standard but names no real hazard is flagged and re-anchored.
- [ ] The **hazard-elimination commitment (3)** is phrased up the **hierarchy of controls**
      (`KB-SNIP-HOC`) — never a PPE-only or admin-only statement.
- [ ] The policy is **documented**, **communicated**, available to interested parties, and
      **signed by top management** (a named role/title, not personal data) — clause 5.2
      requires demonstrated top-management commitment.
- [ ] The **statutory written-policy duty** is resolved correctly as a branch beside the
      policy: UK HSWA s.2(3) etc.; **India deferred to `hse-india`** (state detection first,
      **no national-form number minted**, `[GAP]` when unverified) — never hard-blocking.
- [ ] The signed policy is framed as **decision-support** and **does not read as a final
      legal document**; it claims no final regulatory clearance and remains subject to the
      organisation's own competent-person review.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The clause named, its accompanying duties unswept** — a clause-5.2 policy that omits the
  interface duties a competent reader expects around it: the review/revision trigger and date,
  how the policy is made available to interested parties, and the objective-setting link
  (clause 6.2) the framework commitment promises.
- **The undated, unowned commitment** — the policy commits to consultation, legal compliance,
  and improvement but names no accountable role, no review cadence, and no communication route,
  so the commitments cannot be verified as met.
- **Scope-honesty on the signable claim** — the document reads as a final, executed policy
  rather than a decision-support draft awaiting the organisation's own competent-person
  adoption and top-management signature, overstating its status.

## Sign-off note
SME review: ran (persona: Senior HSE Manager / Director); this is decision-support and
PRECEDES — never replaces — the human competent-person review. A FLAG it raises is recorded,
never merge-blocking. The reviewer holds the boundary: the top-management-signed policy is a
draft for the organisation's own competent person to review, not a final legal instrument.
