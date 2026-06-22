---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY,
           ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-LOCATION: "A statutory return is determined by the incident facts + jurisdiction, not the physical work environment; the site is captured only as the establishment identity inside the incident record, not as a hazard-environment dimension."
    ELI-EXPOSURE: "Recordability/reportability turns on the injured person's outcome (the incident facts, Q3), not on an exposed-population enumeration; there is no population-scoping question for a return."
    ELI-BASELINE: "A return reports what occurred; there is no existing-controls / current-state baseline to elicit (this skill does not assess or score risk)."
    ELI-SCORING: "No risk-matrix or likelihood/severity scoring — recordability/reportability is a cited binary test (KB-DATA-RECORDABILITY-TESTS), not a scored risk; there is no matrix to configure."
  branches:
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — regulatory-returns

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
intake opens with the **jurisdiction (Q1)** — the load-bearing branch — then the return
type, the incident facts, the org profile, and the period.

The one load-bearing branch is the **mandatory India→state branch** (Q1 = India → Q1a +
`KB-REG-IN-STATEFORMS`): **state detection is mandatory** and the India leg **defers to
`hse-india`** — confirm the state before citing any form, and **never a national form
number**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Jurisdiction | MCQ | US OSHA / UK RIDDOR / EU member-state / India / Unknown (India → Q1a) | ELI-JURIS | always |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing any form; defers to `hse-india`** | ELI-JURIS | Q1 == India |
| Q2 | Return type (per jurisdiction) | MCQ per endpoint | US: 300 log / 300A summary / 301 incident report / electronic 300A · UK: specified injury / over-7-day / disease / dangerous occurrence | ELI-OUTPUT / ELI-SCOPE | always |
| Q3 | **Incident facts (the recordability/reportability test inputs)** | free-text | "Describe the incident: nature, outcome, days away / restricted, whether a specified injury, work-relatedness, treatment beyond first aid (or 'none' → I'll flag `[GAP]`)." — **the specificity anchor; refuse a reportable yes/no until these are captured** | ELI-SUBJECT / ELI-EVIDENCE | always |
| Q4 | Organisation profile | MCQ + free-text | Size band / SIC (industry sector) — for OSHA electronic-submission applicability + the obligation set | ELI-INDUSTRY / ELI-OBLIGATIONS | always |
| Q5 | Reporting period / posting window | free-text (date-time) | "Which period or calendar year is this return for? (drives periodic returns + the 300A posting window + the deadline)" | ELI-TEMPORAL | always |
| Q5b | **Preparer + action owner** | free-text→role | "Who is the competent person preparing this return (role), and who will own any follow-up action? (named role — no 'TBD')" | ELI-COMPETENCY | always |

**Branch map:** `india-state` (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`; **mandatory** —
defers to `hse-india`, never a national form number).

## Echo-back

After the last applicable question (Q5b, and Q1a if the India branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Preparing: an OSHA 300-log recordability determination for the despatch-bay laceration,
work-related, treated beyond first aid, US — reporting year 2025, prepared by the HSE
Lead — correct?" Never proceed until the user confirms.

## Refuse-on-vague anchors

- **Q3 is the specificity anchor** — **refuse to give a recordable/reportable
  yes-or-no until the incident facts the test needs are captured**; ask again, or
  record `[ASSUMPTION]` / `[GAP]`, never invent a fact to force a determination.
- **Never assert a deadline without the jurisdiction (Q1)** — the deadline is a
  function of the jurisdiction's rule (RIDDOR 15-day vs OSHA 300A posting window).
- For **India** (Q1 = India), **mandatory state detection** runs first (Q1a) and the
  leg routes to `hse-india`; never cite a national form number.

## Domain evidence types (ELI-EVIDENCE)

The incident report / first-aid log / medical note (de-identified) · the days-away /
restricted-work record · prior 300-log entries (for new-case vs continuation) · the SDS
or exposure record where an occupational disease is alleged · the establishment's
SIC / size record for 1904.41 electronic-submission applicability.
