---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-COMPETENCY, ELI-OBLIGATIONS, ELI-EVIDENCE]
  omits:
    ELI-SCORING: "a policy, not a scored assessment"
    ELI-EXPOSURE: "not a hazard-level artifact"
    ELI-TEMPORAL: "policy review cadence is a single optional line, not a branch"
    ELI-BASELINE: "existing-culture is captured by Q4, not a separate baseline"
    ELI-LOCATION: "folded into ELI-SUBJECT — the named operator is the location identity"
  branches:
    - when: Q3
      equals: India
      activates_questions: [Q3a]
      activates_kb_row: KB-REG-IN-DGCA
      activates_output_section: protection-clause-framing
      mandatory: true
    - when: Q3
      equals: Unknown
      activates_output_section: annex19-appx3-principles-flag-legal-review   # never assert protection the law doesn't give
    - when: Q4
      equals: NoneYet
      activates_output_section: cross-ref-aviation-confidential-reporting
    - when: Q7
      equals: DrugAlcohol
      activates_output_section: culpability-ladder-boundary-expansion
---

# Structured intake — aviation-just-culture-policy

Run one question at a time — MCQ where the answer space is enumerable, free-text where it
is open. Branch on the answers, **echo the captured facts back before any analysis**, and
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. The policy's enforceable line rests on the reporter-
protection law — where it is unknown, draft to ICAO Annex 19 Appendix 3 principles and **flag
for legal review; never assert a protection the jurisdiction's law does not grant**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Draft a new policy, or review/revise an existing one? | MCQ | First policy · Revising an existing one | ELI-SCOPE | always |
| Q2 | Name the operator/airport/AMO and the workforce it covers. | free-text | de-identified; refused if generic | ELI-SUBJECT | always |
| Q3 | What legal/regulatory protection basis does the policy rest on? | MCQ | India/DGCA CAR protection-of-safety-data, EU/Reg 376-2014, FAA/ASAP voluntary-disclosure, Annex19/Appendix 3 principles only, Other (specify), Unknown | ELI-JURIS / ELI-OBLIGATIONS | always |
| Q3a | *(India only)* Which Indian operations / which State Safety Programme layer frames the protection clause? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q3==India |
| Q4 | Is a confidential reporting system already in place? | MCQ | Established/yes, BeingBuilt/`aviation-confidential-reporting`, NoneYet/none yet | ELI-EVIDENCE | always |
| Q5 | What is the decision-tree basis? | MCQ | Substitution test · Culpability ladder (honest error → at-risk → reckless → negligent) · Both | ELI-SUBJECT | always |
| Q6 | Who applies the decision tree and signs the policy? | free-text | role labels (e.g. Accountable Manager + just-culture panel) | ELI-COMPETENCY | always |
| Q7 | What behaviours are in scope? | MCQ multi-select | Safety reporting only, DrugAlcohol/interface, Security, Disciplinary boundary | ELI-SUBJECT | always |
| Q8 | A representative (de-identified) scenario to test the tree against? | free-text | optional; no individual named | ELI-SUBJECT | optional |

**Branch map.** `Q3==Unknown` → `[GAP]`, draft to ICAO Annex 19 Appendix 3 principles, instruct
legal review — **never assert a protection the law doesn't give**. `Q3==India` → Q3a +
`KB-REG-IN-DGCA` protection-clause framing (the mandatory India follow-up resolves the State
Safety Programme layer; exact CAR number `[GAP]`). `Q4==NoneYet` → output cross-references
`aviation-confidential-reporting` as a prerequisite. `Q7` selections expand the
culpability-ladder boundaries section.

## Echo-back
Echo the captured facts back and ask the user to confirm before any drafting:
*"Confirmed: just-culture policy for **{named operator}**, protection basis **{law}**,
decision-tree **{basis}**, applied by **{role}**, covering **{behaviours}**. Proceed?"*

## Refuse-on-vague anchors
- Q2 is the specificity anchor: "we have a just culture" with no decision line → **refuse**;
  the policy must carry an explicit acceptable/unacceptable line, not a slogan.
- A worked example that names an individual → de-identify (role labels) first.
- No protection law identified → `[GAP]`; do not assert legal immunity the framework
  doesn't grant.
