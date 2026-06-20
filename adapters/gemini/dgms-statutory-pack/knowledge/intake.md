---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-TEMPORAL, ELI-COMPETENCY]
  omits:
    ELI-INDUSTRY: "coal-vs-metalliferous is captured inside ELI-LOCATION/ELI-SUBJECT (Q2) and surface-vs-UG as a region-context nuance (Q3), not a hazard branch — this is pure compliance form resolution, not a hazard assessment."
    ELI-SCORING: "no risk scoring — the pack resolves and drafts the prescribed statutory form, it does not rate risk."
    ELI-BASELINE: "existing-controls are irrelevant to statutory form filing; the obligation drives the form, not the control baseline."
    ELI-EVIDENCE: "register/notice facts only; the domain evidence each obligation needs is elicited inline per the Q5x obligation branch (Q5c figures source, Q5b counts), so no separate data-pull dimension is required."
  branches:
    - ask: ELI-JURIS
      when: Q4
      activates_kb_row: KB-REG-IN-STATEFORMS   # MANDATORY DGMS region/zone resolution gates any form citation
    - ask: ELI-OBLIGATIONS
      when: Q1
      option: "a) 24-hour accident"
      activates_questions: [Q5a]
    - ask: ELI-OBLIGATIONS
      when: Q1
      option: "b) Form J register entry"
      activates_questions: [Q5b]
    - ask: ELI-OBLIGATIONS
      when: Q1
      option: "d) Annual return (~20 Jan)"
      activates_questions: [Q5c]
    - ask: ELI-COMPETENCY
      when: Q1
      option: "e) Statutory appointment letter"
      activates_questions: [Q5d]
---

# Structured intake — dgms-statutory-pack

Run **one question at a time** (`KB-SNIP-INTAKE`). MCQ where the answer space is
enumerable, free-text where it is open; **branch on the answers**; **echo the captured
facts back before any drafting**; **refuse on a vague subject** — record `[GAP]` (and a
DGMS form id you cannot verify against the five anchors), **never invent a number**.

The **obligation (Q1) is the runtime gate** and the **DGMS region/zone (Q4) is a mandatory
gate** that must be resolved (infer-from-location-then-confirm) before any form is cited.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need to produce? | MCQ | a) 24-hour accident / dangerous-occurrence notice / b) Form J register entry / c) Form B employee register / d) Annual return (~20 Jan) / e) Statutory appointment letter / f) Not sure — resolve my obligation | ELI-SCOPE/ELI-OBLIGATIONS | always (gate) |
| Q2 | Named mine + commodity? | free-text | "Mine name, owner, commodity (coal / metalliferous / other)" — the specificity anchor | ELI-LOCATION/ELI-SUBJECT | always |
| Q3 | Surface or underground? | MCQ | a) Opencast / surface / b) Underground / c) Both | ELI-LOCATION | always |
| Q4 | DGMS region / zone? | MCQ→confirm | infer from the location, then confirm; if unknown offer the DGMS zone list — never silently assume | ELI-JURIS/ELI-LOCATION | always (mandatory gate) |
| Q5a | Event class + datetime? | MCQ+free-text | a) Fatal / b) Serious bodily injury / c) Dangerous occurrence — + exact date & time of the event | ELI-SUBJECT/ELI-TEMPORAL | Q1=a |
| Q5b | Personnel counts as at date? | free-text | "Headcount by category (employed / contractor / category of worker) as at the register date" | ELI-EXPOSURE | Q1=b/c |
| Q5c | Return period + figures source? | free-text | "Reporting year, and where the production / employment / accident figures come from" | ELI-TEMPORAL | Q1=d |
| Q5d | Appointment role + competent person? | MCQ+free-text | a) Manager / b) other statutory official — + the person as a role label, qualification held | ELI-COMPETENCY | Q1=e |
| Q6 | Where will this go? | MCQ | a) Internal record / b) DGMS submission / c) Wider circulation | ELI-OUTPUT | always (de-id trigger) |

## Branch map
- **Q4 region** activates the **`KB-REG-IN-STATEFORMS`** DGMS region/zone resolution
  (mandatory) → it **gates any form citation**. No zone confirmed → no form cited.
- **Q1=a** → Q5a → 24h-notice template + a 24-hour countdown anchored from the event
  date/time; only a verified anchor is carried as a value, else `[GAP]`.
- **Q1=b/c** → Q5b → register entry populated from the supplied counts.
- **Q1=d** → Q5c → annual-return (~20 Jan, legacy due date) section + figures provenance.
- **Q1=e** → Q5d → statutory-appointment letter naming the competent, qualified role.
- **Q1=f** → resolve via the `KB-REG-IN-MINES-ACT` duty row → drive to one of a–e.
- Any DGMS form id **not** among the five verified anchors (Form J · Form B · 24h notice ·
  annual return ~20 Jan · statutory Manager appointment) → `(DGMS-prescribed — verify per
  mine) [GAP]`, **never invented** (the no-fabrication rule, carried into every branch).

## Echo-back
"Producing **{obligation}** for **{mine, commodity, surface/UG}** in DGMS region
**{zone}**; event/period **{datetime / year}**; destination **{output}**. Confirm before
I draft." — echo the captured facts back and **confirm** before any drafting begins.

## Refuse-on-vague anchors
- **No region/zone** → "I can't cite a DGMS form without the region/zone — name it, or the
  location so I can infer and confirm." (the mandatory-gate refusal).
- **"Draft the accident notice"** with no event class / datetime → ask for the class and the
  exact date & time before drafting.
- **Never invent a numbered form** → an unverified DGMS form id stays literal
  `(DGMS-prescribed — verify per mine) [GAP]`; the citation grader is row-blind, so honesty
  rides on the literal `[GAP]` marker.

## Domain evidence types (per obligation)
Personnel registers / headcounts (Form B); production & employment figures and prior-year
accident counts (annual return); event datetime + classification (24h notice); appointment
qualification records (statutory appointment).

> **[GAP] for the human verifier:** confirm `KB-REG-IN-STATEFORMS` actually carries the
> **DGMS regional / zonal** office map (state-factory forms ≠ DGMS zones); if it does not,
> the Q4 zone-resolution check has no backing data and should itself be `[GAP]`-flagged.
