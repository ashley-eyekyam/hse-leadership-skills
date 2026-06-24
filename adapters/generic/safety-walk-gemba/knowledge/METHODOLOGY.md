# Methodology — Safety Walk / Gemba (felt leadership · genchi-genbutsu)

The domain method the `safety-walk-gemba` skill applies. It designs and runs a
**leadership safety walk** as an act of **engagement, not inspection** — *genchi-genbutsu*
("go and see") plus **HSG65 felt leadership** — grounded in **ISO 45001:2018 clauses 5.1**
(leadership and commitment) and **5.4** (consultation and participation of workers)
(`KB-SNIP-LEADERSHIP-CLAUSE-MAP`). The prompt bank is `KB-SNIP-GEMBA-PROMPTS`; the
commitment-closure leading indicator is `KB-DATA-LEADING-INDICATORS`. These are cited as
**method, not law**.

## Principle 1 — Open conversation, never a tick-box checklist

A gemba walk uses **open, area-specific, non-interrogative** questions that invite the
worker's own account ("Walk me through what could go wrong in this task." · "What's the one
thing that makes your job harder or riskier than it needs to be?"). A **closed yes/no
tick-box checklist is not a gemba walk — it is an audit**, and it is **flagged** for
specificity and defensibility. If the user asks for a closed checklist, refuse and steer
them to the open prompt bank (or to `safety-audit` if they genuinely want an inspection).
The open prompts are selected by **purpose** (felt-leadership/engagement · hazard-spotting ·
control-verification · post-incident) and **anchored to the specific area/task** in scope.

## Principle 2 — Capture worker concerns role-labelled (psychological safety)

Worker concerns raised on a walk are **captured against role/group labels only** — never
attributed to a **nameable individual**. Attributing a concern to a named person breaks
psychological safety and re-identifies the worker; it is a `de_identification` **hard-fail**
(see `references/deid-checklist.md`). The De-identifier scrub runs **FIRST**, before any
drafting. Where the walk did not reach an area in scope, record `[GAP]` rather than invent.

## Principle 3 — Every commitment becomes an owned, dated, tracked action

A walk is **not a conversation that evaporates** — it is **commitments owned, dated, and
closed**. Every commitment the leader makes on the walk is converted to a **SMART action**:
specific, measurable, **assignable (a named role-label owner)**, relevant, and **time-bound
(an ISO due date)** — validated via `smart_actions.validate_register`. **No anonymous
commitments and no "ASAP".** Any control a commitment implies is ranked through the
hierarchy of controls (`KB-SNIP-HOC` + the `controls` engine), higher-order first — never a
PPE-only or "retrain the worker" default.

## Principle 4 — Commitment closure-rate is itself a leading indicator

The **count and closure-rate of walk commitments** is a **leading indicator** — a forward,
active measure of visible leadership and worker engagement (`KB-DATA-LEADING-INDICATORS`;
quote its `source`+`year`). A walk that produces **no tracked commitment fails the
defensibility gate** — it is recorded as `[GAP]`, not signed off as complete. Walk-commitment
closure feeds the broader leading-indicator set single-sourced in `KB-DATA-LEADING-INDICATORS`.

## The method loop

1. **De-identify first** — scrub every nameable individual to a role/group label; capture
   concerns role-labelled; hold any re-identification key separately (Principle 2).
   Everything downstream consumes scrubbed text.
2. **Select open prompts by purpose + area** — pick the prompt family for the walk's purpose
   and anchor each prompt to the specific area/task (Principle 1); refuse a closed checklist.
3. **Run the conversation, capture concerns role-labelled** — record what workers raise
   against role/group labels; flag `[GAP]` for areas not reached.
4. **Convert commitments to SMART actions** — each commitment → owned + dated +
   measurable action (`smart_actions.validate_register`); rank any implied control via
   `KB-SNIP-HOC` (Principle 3).
5. **Report commitment closure as a leading indicator** — count + closure-rate, banded /
   defined against `KB-DATA-LEADING-INDICATORS` (quote source+year) (Principle 4).
6. **Validate** against `QUALITY_CHECKLIST.md`.
7. **Assemble** the branded report (`assets/report.json`).

## Citations

*genchi-genbutsu* / gemba ("go and see" — Toyota Production System / lean) · HSE HSG65
"felt leadership" / visible safety leadership · ISO 45001:2018 clauses 5.1 (leadership and
commitment) and 5.4 (consultation and participation of workers). Quote each indicator's
`source`+`year` from `KB-DATA-LEADING-INDICATORS`; never invent a standard reference. These
are recognised method, not statute.
