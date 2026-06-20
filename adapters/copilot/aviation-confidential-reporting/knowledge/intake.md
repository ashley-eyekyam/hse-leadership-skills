---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-COMPETENCY, ELI-OBLIGATIONS, ELI-TEMPORAL, ELI-EVIDENCE]
  omits:
    ELI-SCORING: "a system design, not a scored assessment"
    ELI-EXPOSURE: "not a hazard-analysis artifact"
    ELI-BASELINE: "a prior scheme is captured by the sample-report question (Q10), not a separate baseline"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator is the location identity"
  branches:
    - when: Q2
      equals: Confidential
      activates_questions: [Q5]           # custodian/re-id-key handling — mandatory
    - when: Q2
      equals: Anonymous
      activates_output_section: suppress-Q5-no-key-bulletin-feedback-only
    - when: Q3
      equals: India
      activates_questions: [Q3a]
      activates_kb_row: KB-REG-IN-DGCA
      mandatory: true
    - when: Q3
      equals: Unknown
      activates_output_section: annex19-appx3-principles-flag-legal-review
    - when: Q4
      equals: VoluntaryPlusMandatory
      activates_output_section: distinct-mor-routing-path   # the two channels never blur
---

# Structured intake — aviation-confidential-reporting

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. De-identification is **load-bearing and runs first**: no
reporter detail (name, role/route/base/flight, exact dates, narrative re-identifiers) ever
enters the circulated design — a reporter-identity leak is the hard de-id auto-fail.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Name the operator/airport/AMO and the workforce the scheme covers. | free-text | refused if generic | ELI-SUBJECT | always |
| Q2 | What scheme type? (this sets the de-identification trigger) | MCQ | Confidential/identity known to a custodian, protected, Voluntary/de-identified at intake, Anonymous/no identity captured | ELI-OUTPUT | always |
| Q3 | What legal/regulatory protection basis applies? | MCQ | India/DGCA CAR, EU/Reg 376-2014, FAA/ASAP, Annex19/Appendix 3 principles only, Other, Unknown | ELI-JURIS / ELI-OBLIGATIONS | always |
| Q3a | *(India only)* Which Indian operations / which State Safety Programme layer frames the protection basis? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q3==India |
| Q4 | How does this interface with mandatory occurrence reporting (MOR)? | MCQ | SeparateVoluntary/scheme only, VoluntaryPlusMandatory/a distinct mandatory channel, MORElsewhere/handled elsewhere, Unsure | ELI-OBLIGATIONS | always |
| Q5 | Who is the custodian of any re-identification key, and the access controls? | free-text | a named custodian *role*, NOT the circulated document | ELI-COMPETENCY | Q2==Confidential |
| Q6 | Who triages reports and closes the feedback loop? | free-text | role labels (safety officer / review panel) | ELI-COMPETENCY | always |
| Q7 | What intake channels? | MCQ multi-select | Paper form · Web portal · App · Hotline · Via line manager | ELI-SUBJECT | always |
| Q8 | How do reporters learn the outcome? | MCQ | De-identified safety bulletin · Direct-to-reporter via custodian · Both | ELI-OUTPUT | always |
| Q9 | What feedback SLA and report-retention period? | free-text | e.g. acknowledge in N days; retain for M years | ELI-TEMPORAL | always |
| Q10 | A sample report to design against? | free-text | optional; **de-identify reporter detail (name, role/route/base/flight, exact dates) FIRST** | ELI-EVIDENCE | optional |

**Branch map.** `Q2==Confidential` → Q5 (mandatory); the re-id key lives in a separate
custodian artifact, never the circulated design. `Q2==Anonymous` → suppress Q5 (no identity
captured → no key); feedback defaults to the de-identified bulletin only. `Q3==India` → Q3a +
`KB-REG-IN-DGCA` (the mandatory India follow-up resolves the State Safety Programme layer).
`Q3==Unknown` → `[GAP]`, design to Annex 19 Appendix 3 principles, flag for legal review.
`Q4==VoluntaryPlusMandatory` → output adds a distinct MOR routing path so the two channels
never blur.

## Echo-back
Echo the captured facts back (role labels only — never a reporter name) and ask the user to
confirm before any drafting:
*"Confirmed: **{scheme type}** reporting scheme for **{named operator}**, protection basis
**{law}**, custodian **{role}**, feedback via **{channel}**, SLA **{…}**. No reporter is ever
named in the circulated design; no re-id key is embedded. Proceed?"*

## Refuse-on-vague anchors
- Q1 is the specificity anchor: a scheme request with no named operator → **refuse**.
- Any reporter detail entering the circulated design → **blocked** (load-bearing de-id).
- A custodian arrangement that puts the key in the circulated document → reject.
- No protection law identified → `[GAP]`; never assert immunity the framework doesn't grant.
