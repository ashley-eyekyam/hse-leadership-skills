<!-- KB-REG-IN-ELECTRICAL -->
# India — electrical safety (CEA Regulations + state electricity rules, legacy-first)

**Fragment ID:** `KB-REG-IN-ELECTRICAL`
**What this is:** the duty → artifact **citation map** for India's electrical-safety
regime — the Central Electricity Authority (Measures relating to Safety and
Electric Supply) Regulations 2010 (CEA Safety Regulations) under the Electricity
Act 2003, plus the **state** electricity / factory-electrical rules that operate
the day-to-day permit, isolation and notification requirements. **This is data,
not the rules text** — a skill (or its Regulatory-Checker subagent) reads it
*after* resolving the user's state.
**What this is NOT:** a reproduction of the regulations, and NOT a single
nationwide form catalogue — operative permit-to-work / accident-notification
instruments are **state** specific.

> Source: CEA (Measures relating to Safety and Electric Supply) Regulations 2010 under the Electricity Act 2003 + state electricity / electrical-inspectorate rules — per-row cite below · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true (state notifications + OSH Code transition in flux).

**Legacy-first + mandatory state detection.** Electrical-safety enforcement in
India runs through **state Electrical Inspectorates** and state rules; the
permit-to-work, isolation register, and electrical-accident-notification target is
state-specific. An India electrical-power skill **resolves the state first**
(`KB-REG-IN-STATEFORMS`, mandatory) before citing any form or portal, returns the
legacy state requirement as the primary answer, and appends the OSH-Code
transition note. The detailed state form/permit content is held in the
**`hse-india`** engine, which the skill defers to (subagent → inline → `[GAP]`
pointer); **no electrical accident form is ever cited as a single nationwide
number**.

## Trigger → duty → artifact

| Trigger | Statutory duty | Artifact / instrument | Cite |
|---|---|---|---|
| Work on / near energized installation | De-energize and establish a safe working condition; permit-to-work | Electrical permit-to-work (state-prescribed) | CEA Safety Regs 2010; state rules — resolve per state |
| Isolation of HT/LT supply | Isolate, lock, earth, prove dead before work | Isolation + earthing record | CEA Safety Regs 2010 (work on lines/apparatus) |
| Competence of electrical worker | Engage a person holding the requisite electrical competency certificate | Competency / licence record | state Electrical Licensing Board — resolve per state |
| Electrical accident (fatal / non-fatal / animal) | Notify the Electrical Inspector within the prescribed time | Electrical-accident notice (state-prescribed form/timing) | CEA Safety Regs 2010 reg on accident reporting; state rules — `[GAP]` per state |
| Periodic inspection / energization approval | Obtain inspection / energization sanction | Inspection report / energization approval | state Electrical Inspectorate — resolve per state |

## Verified anchors vs `[GAP]`
- **Verified anchor:** the **CEA Safety Regulations 2010** establish the national
  safety-measure framework and the duty to notify electrical accidents to the
  Electrical Inspector — cite the framework.
- **`[GAP]` (resolve per state, never invent):** the electrical-accident notice
  **form id and timing**, the permit-to-work format, and the competency-licence
  particulars vary by **state** notification — emit a literal `[GAP]` and route to
  the state Electrical Inspectorate via the **`hse-india`** engine. The citation
  grader is row-blind; a fabricated state form value passes the automated gate, so
  honesty is enforced by the `[GAP]` marker + the per-skill no-fabrication eval +
  the SME FLAG.

## How the skills use this fragment
- India electrical-power / utilities skills ground here for the de-energize-first /
  permit / isolation / accident-notification duty set; they **resolve the state
  first** (`KB-REG-IN-STATEFORMS`) and defer state-specific form content to the
  **`hse-india`** engine, marking any unverified value `[GAP]`.

## OSH-Code transition note
The Occupational Safety, Health and Working Conditions Code 2020 consolidates
several labour/safety laws; most states have not notified their OSH Rules, so
legacy CEA / state electrical-rule filings remain valid. Offer the consolidated
mapping only as an explicit transition mode (warn the form/portal may not be live).
