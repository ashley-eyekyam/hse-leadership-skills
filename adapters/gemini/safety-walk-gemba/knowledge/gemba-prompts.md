<!-- KB-SNIP-GEMBA-PROMPTS -->
# Gemba / leadership-walk prompt bank — open conversation, not a tick-box

**Fragment ID:** `KB-SNIP-GEMBA-PROMPTS`
**This is prompt text, applied by the model — not a generator.** It is the open-question
conversation-prompt bank the `safety-walk-gemba` skill uses to design a felt-leadership safety walk —
engagement, **not a tick-box audit**. Every commitment made on a walk becomes a `smart_actions`
owned/dated action tracked to closure; the count/closure-rate of walk commitments is itself a leading
indicator (consumes `KB-DATA-LEADING-INDICATORS`). Cited as **method, not law**.

> Source: gemba / genchi-genbutsu "go and see" — Toyota Production System / lean · HSE HSG65 "felt leadership"/visible-commitment · ISO 45001:2018 clauses 5.1 & 5.4 · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction — open, area-specific, non-interrogative prompts

A closed yes/no checklist is **not** a gemba walk — it is flagged (specificity · defensibility). Use
**open** questions, anchored to the **specific area/task**, that invite the worker's own account.
Capture worker concerns **role-labelled** (psychological safety) — never attributed to a nameable
individual.

### Prompt bank by purpose

| Purpose | Sample open prompts |
|---|---|
| **Felt-leadership / engagement** | "What's the one thing that makes your job harder or riskier than it needs to be?" · "What safety improvement would you make if it were your call?" · "When did you last stop a job — what happened?" |
| **Hazard-spotting** | "Walk me through what could go wrong in this task." · "What controls do you rely on here, and have any ever failed you?" |
| **Verification of a specific control** | "Show me how this control works in practice." · "When is it hardest to follow this procedure?" |
| **Post-incident reassurance** | "Since the incident, what's changed for you here?" · "Do you trust that raising a concern leads to action?" |

**Guardrail:** open · area-specific · non-interrogative. Worker concerns recorded role-labelled.

## Commitment tracked as a leading indicator (SC-1)

Every commitment made on a walk → a `smart_actions` **owned + dated** action → tracked to closure. The
**count and closure-rate of walk commitments** is a leading indicator in `KB-DATA-LEADING-INDICATORS`.
A walk that produces **no tracked commitment** fails the defensibility gate — a walk is not a
conversation that evaporates; it is commitments owned, dated, and closed.

## How the skill uses this fragment

`safety-walk-gemba` selects prompts by purpose/area, runs the open conversation, role-labels concerns,
converts each commitment into an owned/dated `smart_actions` action, and reports walk-commitment
closure as a leading indicator (single-sourced from `KB-DATA-LEADING-INDICATORS`).
