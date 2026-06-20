---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION, ELI-EXPOSURE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL, ELI-COMPETENCY, ELI-SCORING]
  omits:
    ELI-BASELINE: "existing-controls are folded into the RCA/evidence step — the controls present-and-failed are part of the evidence (Q7), not a separate intake branch."
  branches:
    - ask: ELI-JURIS
      when: Q3
      activates_kb_row: KB-REG-IN-DGMS   # MANDATORY DGMS region/zone before any form citation
    - ask: ELI-SUBJECT
      when: Q4
      option: "a) Fatal"
      # DGMS-reportable -> 24h notice (datetime->countdown) + Form J entry
    - ask: ELI-SUBJECT
      when: Q4
      option: "c) Dangerous occurrence"
      # also DGMS-reportable
    - ask: ELI-SCORING
      when: Q8
      option: "**ICAM (default)**"
      # ICAM -> ask for organisational-factor evidence; all methods enforce reaches_systemic
---

# Structured intake — mine-incident-investigation

Run **one question at a time** (`KB-SNIP-INTAKE`). MCQ where the answer space is
enumerable, free-text where it is open; **branch on the answers**; **echo the captured
facts back before any analysis**; **refuse on a vague subject** — `[GAP]`, never invent a
form id or a missing fact.

**De-identification runs FIRST** (the orchestration block) — Q4/Q5/Q6 outputs are scrubbed
to **role labels** before any analysis; exact pit/shaft locations are scrubbed and small
(<5) fatality/injury cells suppressed. **The echo-back below shows personnel as role labels
only.** The **DGMS region/zone (Q3) is a mandatory gate** resolved (infer-then-confirm)
before any form is cited; **event class (Q4)** gates DGMS reportability *and* de-id intensity.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What outcome? | MCQ | a) Full investigation + RCA / b) RCA only / c) DGMS reportability check only / d) CAPA from an existing finding | ELI-SCOPE | always |
| Q2 | Commodity + mine type? | MCQ | a) Coal — UG / b) Coal — opencast / c) Metalliferous — UG / d) Metalliferous — opencast / e) Other | ELI-INDUSTRY | always |
| Q3 | DGMS region / zone? | MCQ→confirm | infer-then-confirm; mandatory before any form citation | ELI-JURIS/ELI-LOCATION | always (gate) |
| Q4 | Event class + datetime? | MCQ+free-text | a) Fatal / b) Serious bodily injury / c) Dangerous occurrence / d) Near-miss-other — + exact date & time | ELI-SUBJECT/ELI-TEMPORAL | always (gates DGMS + de-id) |
| Q5 | Who was involved + counts? | free-text | "Injured / deceased, contractors, rescue team, bystanders — counts by category (drives <5 suppression); persons as role labels" | ELI-EXPOSURE | always |
| Q6 | The incident facts (de-identified)? | free-text | "What / where / sequence — names → role labels; exact pit/shaft locations scrubbed" | ELI-SUBJECT | always (after de-id) |
| Q7 | Evidence you hold? | mcqmulti-select+free-text | gas readings · ventilation survey · strata-monitoring log · blast record · CCTV-SCADA · witness statements · prior-incident history · other | ELI-EVIDENCE | always |
| Q8 | RCA method? | MCQ | 5-Whys / **ICAM (default)** / SCAT / Fishbone / Swiss-Cheese | ELI-SCORING | always |
| Q9 | Investigation lead / competent person (role)? | free-text | "Role label of the appointed lead" | ELI-COMPETENCY | always |
| Q10 | Output + distribution? | MCQ | a) Internal investigation report / b) DGMS submission pack / c) Both | ELI-OUTPUT | always (de-id intensity) |

## Branch map
- **De-id runs FIRST** (orchestration block) — Q4 / Q5 / Q6 outputs are scrubbed to role
  labels and small cells suppressed **before** any analysis.
- **Q3 region** activates `KB-REG-IN-DGMS` resolution (mandatory) → it gates any form
  citation.
- **Q4=Fatal / Dangerous occurrence** → DGMS-reportable → 24h-notice (datetime → countdown)
  + Form J entry, region-resolved; else a reportability verdict "not reportable, with reason".
- **Q5 counts <5** → small-cell suppression + secondary suppression.
- **Q8=ICAM** → ask for organisational-factor evidence; **all** methods enforce
  `reaches_systemic`.
- Any DGMS form id beyond the verified anchors → `[GAP]`, **never invented**.

## Echo-back (role labels only — de-identified)
"Investigating a **{event class}** at **{mine, commodity / type}** (DGMS **{zone}**) on
**{datetime}**; **{n}** involved (**role labels only** — e.g. *Operator A, Contractor 1*);
RCA **{method}**; output **{dest}**. Confirm before analysis." — echo the captured facts
back (personnel as role labels only) and **confirm** before any analysis.

## Refuse-on-vague anchors
- **No event facts / "investigate the accident"** → ask for what / when / where / sequence
  (Q6 is the specificity anchor).
- **"Miner error"** offered as a stop point → reject; the RCA must reach a systemic /
  organisational factor (`reaches_systemic`).
- **No region** → can't cite the DGMS form; **never invent a form id** (`[GAP]`).

## Domain evidence types (ELI-EVIDENCE)
Gas / methane & CO readings; ventilation survey results; strata / convergence monitoring
logs; blast / shotfiring records; SCADA / CCTV / proximity-detection logs; witness
statements; prior incident & dangerous-occurrence history; shift / competency records.
