---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-EXPOSURE, ELI-BASELINE]
  omits:
    ELI-SCORING: "no severity scoring — this is a transition briefing, not an incident artifact"
    ELI-EVIDENCE: "a briefing, not an assembled filing — no accident records ingested"
    ELI-COMPETENCY: "no signatory on a briefing"
    ELI-LOCATION: "the establishment + state is enough; no physical-environment elicitation"
    ELI-OBLIGATIONS: "the legacy obligation IS the subject (Q3); the consolidated clause is output"
    ELI-TEMPORAL: "state OSH-Rule notification status is output from the KB; planning horizon is optional, not a gate"
  branches:
    - when: Q1
      option: India
      activates_questions: [Q1b]
      mandatory: true
      activates_kb_row: KB-REG-IN-STATEFORMS
    - when: Q2
      activates_questions: [Q4]
    - when: Q4
      activates_questions: []
    - when: Q6
      activates_questions: []
      activates_kb_row: KB-REG-IN-OSH-CODE
---

# Structured intake — india-osh-code-pack

A forward-looking OSH Code 2020 transition briefing (`status: beta`): **legacy-first**, opt-in
mapping, and it never instructs filing an unnotified form. Run ONE question at a time, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo the
captured facts back before any mapping**; **refuse to proceed on a vague or unconfirmed state**
(commencement status is state-specific — record `[GAP]`, never invent a consolidated form).
Canonical runtime pattern: `KB-SNIP-INTAKE`.

**MANDATORY state detection (the family spine).** The Indian state is the FIRST, BLOCKING,
infer-then-confirm gate — it drives whether the state has notified its OSH Rules. The legacy
state form is **always** the primary, defensible answer; the OSH-Code mapping is a clearly-
labelled forward look. Unseeded/Unknown state → direction-of-travel only, never a state-specific
consolidated form. State MCQ set: `Tamil Nadu · Karnataka · Maharashtra · Delhi/Central ·
Gujarat · Other (specify) · Unknown` (GJ first-class — and GJ is one of the few states that has
notified its OSH Rules).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Which **jurisdiction** is the establishment in? *(India-default skill; a non-India jurisdiction is out of scope.)* | MCQ | India, Other / Unknown — India activates the mandatory state gate (Q1b) | ELI-JURIS | always |
| Q1b | **Which state** is the establishment in? *(commencement status is state-specific; infer-from-address allowed, I confirm before any mapping.)* | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown | ELI-JURIS | iff Q1 = India — **BLOCKING** |
| Q2 | What **kind of establishment** is it? *(each legacy regime maps differently under the Code.)* | MCQ | Factory · Construction (BOCW) · Mine · Other (specify) | ELI-INDUSTRY | always |
| Q3 | Which **legacy obligation** do you want mapped? | MCQ | Registration · Annual return · Safety-Officer threshold · Full regime | ELI-SUBJECT | always |
| Q4 | Roughly **how many workers**, and do you **use power**? *(the Code raises the factory threshold 10/20 → 20/40 and shifts the Safety-Officer trigger 1000 → 500/250 — this decides if you move in or out of scope.)* | free-text | headcount + power Y/N | ELI-EXPOSURE | always (esp. Factory) |
| Q5 | What do you **file today** under the legacy regime (which returns / registrations)? | free-text | current filings | ELI-BASELINE | always |
| Q6 | Do you want just the **legacy-first answer**, or also the **legacy → OSH-Code mapping** (with the live-or-not caveat)? | MCQ | Legacy answer only · + transition mapping | ELI-SCOPE | always |
| Q7 | Who is this **briefing for**? | MCQ | Internal / leadership · Client · Board | ELI-OUTPUT | always |

## Branch map (state detection prominent)

- **`state-detection`** (THE spine — `when: Q1 / option: India`, `mandatory: true`,
  `activates_questions:[Q1b]`, `activates_kb_row: KB-REG-IN-STATEFORMS` + `KB-REG-IN-OSH-CODE`
  for the notification status). Sub-branches: `{GJ, AR}` → OSH Rules **notified** → the
  consolidated form may be live (still verify); `{TN, KA, MH, DL, Other}` → **not notified** →
  render any consolidated form `[GAP]`, legacy-first remains the live answer, **never instruct
  filing an unnotified form**; Unknown → direction-of-travel only.
- **`establishment-type`** (`when: Q2`) — selects the legacy fragment to map from (Factories /
  BOCW / Mines) + the relevant threshold change.
- **`threshold-scope`** (`when: Q4`) — activates "under the Code you move **into / out of**
  Factories-Act scope" + the Safety-Officer trigger delta.
- **`transition-mode`** (`when: Q6`, opt-in, `activates_kb_row: KB-REG-IN-OSH-CODE`) — only when
  Q6 = + transition mapping: emit the legacy→consolidated map + the live-or-not warning. If Q6 =
  legacy-only, **skip the mapping entirely** (legacy answer from `KB-REG-IN-STATEFORMS` only).

## Echo-back

*"Confirming: a **{type}** in **{state}** with **~{n} workers**{ + power}, current filings
**{baseline}**, you want **{legacy-only / + mapping}**. Note: **{state}** has **{notified / NOT
notified}** its OSH Rules. Giving the legacy-first answer first. Correct?"* — echo the captured
facts back and wait for confirmation before any mapping.

## Refuse-on-vague anchors

- **State is the specificity anchor:** never assert a commencement claim on an unconfirmed or
  unseeded state — give direction-of-travel only; refuse to proceed on a vague state.
- **Never instruct filing an OSH form the state has not notified** → `[GAP]`; the legacy form is
  ALWAYS the primary, defensible answer.
- Honour the KB's 90-day staleness window — surface the freshness caveat rather than presenting
  the map as settled.
- Any threshold/notification value not in the KB = `[GAP]`; never recall or invent it.
