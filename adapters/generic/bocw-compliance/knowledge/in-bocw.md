<!-- KB-REG-IN-BOCW -->
# India — BOCW Act 1996 + BOCW Rules (construction-worker welfare/safety, legacy-first)

**Fragment ID:** `KB-REG-IN-BOCW`
**What this is:** the duty→artifact **citation map** for the Building & Other
Construction Workers (Regulation of Employment & Conditions of Service) Act 1996
and the BOCW Central Rules 1998 (plus the per-state BOCW Rules) — registration,
cess, Welfare Board returns, the safety-officer/committee thresholds, and accident
notification. **This is data, not the rules text** — a skill (or its
Regulatory-Checker subagent) reads it *after* resolving the user's state.
**What this is NOT:** a reproduction of the BOCW Rules, and NOT a single nationwide
form catalogue — the operative returns/portal are **state Welfare Board** specific.

> Source: Building & Other Construction Workers Act 1996 + BOCW (RE&CS) Central Rules 1998 + state BOCW Rules — per-row cite below · Year: 2026 · Reviewed: 2026-06-17 · Volatile: true (BOCW among the laws subsumed by the OSH Code 2020 — transition in flux).

**Legacy-first + mandatory state detection.** BOCW is administered through **state
Construction Welfare Boards**; the registration/cess/return target is state-specific.
An India construction skill **resolves the state first** (`KB-REG-IN-STATEFORMS`,
mandatory) before citing any form or portal, returns the legacy state-Board return as
the primary answer, and appends the OSH-Code transition note. **No BOCW form is ever
cited as a single nationwide number** — the central Form XXV annual return is the
verified anchor; everything state-specific resolves per state or is `[GAP]`-marked.

## Trigger → duty → artifact

| Trigger | Statutory duty | Artifact / instrument | Cite |
|---|---|---|---|
| Establishment employing ≥10 building workers | Register the establishment | Registration application to the state Board | BOCW Act s.7; Central Rules |
| Building worker (age 18–60, ≥90 days/yr) | Register the worker as a beneficiary | Beneficiary registration with the Welfare Board | BOCW (Cess) Act 1996; s.12 |
| Cost of construction (notified threshold) | Pay the welfare **cess** (1% of cost) | Cess assessment / payment to the Board | Building & Other Construction Workers' Welfare Cess Act 1996 |
| Workforce above the notified threshold | Appoint a **Safety Officer** / constitute a Safety Committee | Appointment + committee record | BOCW Central Rules (safety-officer threshold — verify state notification) |
| Annual filing | File the annual return | **Form XXV** (annual return) to the state Welfare Board, by ~15 Feb | BOCW Central Rules; row in `KB-REG-IN-STATEFORMS` |
| Fatal / serious accident on site | Notify the prescribed authority | Accident notice (state-prescribed timing/form) | BOCW Act s.39; state Rules — resolve per state |

## Verified anchors vs `[GAP]`

- **Verified anchor:** the central **Form XXV annual return** (by ~15 Feb) and the
  **1% welfare cess** are concrete — cite them as values (also seeded as the `bocw`
  row in `KB-REG-IN-STATEFORMS`).
- **`[GAP]` (resolve per state, never invent):** the safety-officer headcount
  threshold, the accident-notice form id and timing, and the cess due-date vary by
  **state** notification — emit a literal `[GAP]` and route to the state Board where
  the source does not supply a verified value. The citation grader is **row-blind**;
  a fabricated state form value passes the automated gate, so honesty is enforced by
  the `[GAP]` marker + the per-skill no-fabrication eval + the SME FLAG.

## How the skills use this fragment
- `bocw-compliance` grounds in this fragment for the registration / cess / return /
  safety-officer duty set; it **resolves the state first** (`KB-REG-IN-STATEFORMS`)
  and cites the Form XXV anchor, marking any state-specific value `[GAP]`.
- The OSH-Code transition note is appended legacy-first: the OSH Code 2020 subsumes
  BOCW, but commencement is state-by-state and largely **pending**; the savings
  clause keeps legacy BOCW filings valid (see `KB-REG-IN-OSH-CODE`).
- Filing-portal pointers resolve through `KB-REG-IN-PORTALS` (state Welfare Board
  portal — verify locally), never a hard-coded national portal.

## OSH-Code transition note
The OSH Code 2020 consolidates BOCW (with 12 other labour laws) into a single
registration + consolidated return **in principle**; most states have not notified
their OSH Rules, so legacy BOCW filings remain valid. Offer the consolidated mapping
only as an explicit transition mode (warn the form/portal may not be live).
