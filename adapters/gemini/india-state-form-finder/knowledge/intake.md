---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-TEMPORAL]
  omits:
    ELI-EXPOSURE: "a pure finder runs no worker-count math; headcount belongs to the assembling sibling skills (factories-act-returns / bocw-compliance)"
    ELI-BASELINE: "does not assemble a return — no prior filings needed to locate the form"
    ELI-EVIDENCE: "minimal — a site address + establishment name only; no document ingest"
    ELI-SCORING: "no severity scoring in a lookup"
    ELI-COMPETENCY: "no named owner on a lookup; the memo names the reviewing competent person generically"
    ELI-LOCATION: "establishment name is enough; no registration-cert / environment ingest"
    ELI-OBLIGATIONS: "the obligation IS the subject (Q4); the clause/penalty is output, not separately elicited"
  branches:
    - when: Q1a
      option: India
      activates_questions: [Q2]
      mandatory: true
      activates_kb_row: KB-REG-IN-STATEFORMS
    - when: Q3
      activates_questions: [Q4]
      activates_kb_row: KB-REG-IN-MINES-ACT
    - when: Q4
      activates_questions: [Q4a]
    - when: Q1
      activates_questions: []
---

# Structured intake — india-state-form-finder

This is the **state-resolution engine itself** — its intake *is* the (law, state, obligation)
detection, so the India→state branch must be exemplary for the family. Run ONE question at a
time, MCQ where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back before any resolution**; **refuse on a vague or
unconfirmed state** (a wrong state is a wrong statutory form — record `[GAP]`, never invent a
form). Canonical runtime pattern: `KB-SNIP-INTAKE`.

**MANDATORY state detection (the family spine).** The Indian state is the FIRST, BLOCKING,
infer-then-confirm gate. You may infer the state from a supplied site address, but you MUST
echo it back and **confirm before citing any form**. Anything outside the seeded set
(`TN · KA · MH · DL · GJ`) → literal `[GAP]` + a refusal to emit a national form. The GJ form
value ships as `[GAP]` (verified-absent, not invented).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — *which* form applies, or help *assembling/filing* it? | MCQ | Identify the form (stay here) · Assemble a Factories return (→ `factories-act-returns`) · Assemble an accident notice (→ `india-accident-notice`) · Understand the OSH-Code change (→ `india-osh-code-pack`) | ELI-SCOPE | always (first) |
| Q1a | Which **jurisdiction** is the establishment in? *(this skill is India-default; a non-India jurisdiction is out of scope and routed onward.)* | MCQ | India, Other / Unknown — India activates the mandatory state gate (Q2) | ELI-JURIS | always |
| Q2 | **Which Indian state** is the establishment in? *(I may infer it from an address you give me, but I will confirm before citing any form — a wrong state is a wrong statutory form.)* | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown | ELI-JURIS | iff Q1a = India — **BLOCKING gate** |
| Q3 | What **kind of establishment** is it? *(this decides which law's form applies — a mine routes to DGMS, not a Factories form.)* | MCQ | Factory (Factories Act) · Construction site (BOCW) · Mine (Mines Act / DGMS) · Other (specify) | ELI-INDUSTRY | always |
| Q4 | Which **statutory obligation** are you resolving? | MCQ | Annual return · Half-yearly return · Accident / dangerous-occurrence notice · Statutory register · Licence/registration | ELI-SUBJECT | always |
| Q4a | Which **half-year period**? | MCQ | 1st half (Jan–Jun) · 2nd half (Jul–Dec) · Not sure | ELI-TEMPORAL | iff Q4 = half-yearly |
| Q5 | For which **filing year / period** do you need the due date? | free-text | e.g. "annual return for CY2025" | ELI-TEMPORAL | always |
| Q6 | Name the **establishment** (for the memo header — I will de-identify any worker PII). | free-text | establishment name only | ELI-SUBJECT | always |
| Q7 | Who is this **for**, and how will it circulate? | MCQ | Internal note · Client/consultant memo · Filed with the document | ELI-OUTPUT | always |

## Branch map (state detection prominent)

- **`state-detection`** (THE spine — `when: Q1a / option: India`, `mandatory: true`,
  `activates_questions:[Q2]`, `activates_kb_row: KB-REG-IN-STATEFORMS`, topic `state-detection`).
  Sub-branches: `{TN, KA, MH, DL}` → resolve the seeded row; `GJ` → resolve the row but render
  `form` as literal `[GAP]` (verified-absent), never a number; `Other / Unknown` → **STOP**:
  emit `[GAP]`, advise competent-person verification, refuse to invent a national form;
  inferred-from-address → **echo + confirm before citing**.
- **`establishment-type`** (`when: Q3`, `activates_questions:[Q4]`) — Factory →
  `KB-REG-IN-FACTORIES` + state-forms · Construction → `KB-REG-IN-BOCW` · Mine →
  `KB-REG-IN-MINES-ACT` / DGMS (hand off to `india-accident-notice` for a mine accident — a
  finder does not assemble).
- **`obligation`** (`when: Q4`) — half-yearly → activates Q4a.
- **`scope-handoff`** (`when: Q1`, `option: Assemble a Factories return`) — routes to the named
  sibling skill; this finder does not proceed to assemble.

## Echo-back

*"Confirming before I resolve the form: state = **{state}** (confirmed{ from-address}),
establishment type = **{type}**, law = **{law}**, obligation = **{obligation}** for
**{period}**. Resolving against the `KB-REG-IN-STATEFORMS` row for ({law}, {state},
{obligation}). Correct?"* — echo the captured facts back and wait for confirmation before
any resolution.

## Refuse-on-vague anchors

- **State is the specificity anchor:** never cite a form on an unconfirmed or inferred-but-
  unconfirmed state; refuse to proceed on a vague state.
- Unseeded state (outside TN/KA/MH/DL/GJ) → literal `[GAP]` + a refusal to emit a national
  form number; never invent a row.
- GJ form = `[GAP]` (verified-absent, not invented) — surface it explicitly.
- Any field absent from the matched row = `[GAP]`; route to a competent person — never fabricate.
