---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-LOCATION, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-JURIS: "CCM is the ICMM framework, jurisdiction-independent — no DGMS form output; statutory linkage is handed off to dgms-statutory-pack / principal-hazard-management-plan."
    ELI-OBLIGATIONS: "no statutory deadline — CCM is workshop structuring, not a deadline-bound filing."
    ELI-TEMPORAL: "review cadence beyond verification frequency is out of scope; verification frequency itself is captured under ELI-EVIDENCE (Q6)."
    ELI-EXPOSURE: "the exposed population is implicit in the material-unwanted-event definition (Q3/Q4) — CCM manages the controls that prevent the MUE, not a separately-elicited exposed-population census."
  branches:
    - ask: ELI-INDUSTRY
      when: Q2
      # commodity × mine-type sets the candidate MUE list and control families
      # (coal -> methane/coal-dust/inrush; metalliferous -> ground-control/ventilation).
    - ask: ELI-BASELINE
      when: Q5
      activates_questions: [Q6, Q7]   # per-control performance/verification + accountability loop
    - ask: ELI-SCORING
      when: Q8
      option: "b) ICMM default — confirm"
      # applies + echoes the ICMM default criticality for confirmation.
---

# Structured intake — icmm-critical-control-management

> **Sibling note (D-04):** this intake shares ~80% of its surface with
> `principal-hazard-management-plan` (same commodity/mine-type branch driver, the same
> ICMM critical-control linkage). By the per-skill contract decision (Rule 11 reads one
> file per skill) the two are **kept as separate self-contained files**, not a shared
> fragment — author/maintain them in step but do not extract a shared intake fragment.

Run **one question at a time** (`KB-SNIP-INTAKE`). MCQ where the answer space is
enumerable, free-text where it is open; **branch on the answers**; **echo the captured
facts back before any structuring**; **refuse on a vague subject** — a nominated
'critical control' that is PPE/admin-only for a principal hazard is flagged not accepted,
and an un-supplied performance value is `[GAP]`, **never invented**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Set up CCM for one event, or structure a CCM workshop? | MCQ | a) One material unwanted event / b) Full CCM workshop across hazards | ELI-SCOPE | always |
| Q2 | Commodity class + mine type? | MCQ | a) Coal — UG / b) Coal — opencast / c) Metalliferous — UG / d) Metalliferous — opencast / e) Other | ELI-INDUSTRY | always (branch driver) |
| Q3 | Which material unwanted event? | MCQ | strata failure / inrush-inundation / fire-explosion / ventilation failure / mobile-plant interaction / fall from height / hazardous energy / respirable-dust OH (`KB-DATA-MINING-HAZARDS`) | ELI-SUBJECT | always |
| Q4 | Named mine + the specific scenario? | free-text | "Mine, location, and the precise unwanted-event scenario" — the refuse-on-vague anchor | ELI-LOCATION/ELI-SUBJECT | always |
| Q5 | Which critical controls does the team already nominate? | free-text | "List the controls that, if absent or failed, allow the event" | ELI-BASELINE | always |
| Q6 | Performance & verification data you hold? | free-text | "Per control: performance requirement, current verification activity + frequency, last-verified evidence" | ELI-EVIDENCE | per nominated control |
| Q7 | Verification accountability (role)? | free-text | "Who owns each control's verification (role label only)" | ELI-COMPETENCY | per control |
| Q8 | Criticality rating scheme? | MCQ | a) Org's existing principal-hazard / critical-control scheme / b) ICMM default — confirm | ELI-SCORING | always |
| Q9 | Output + audience? | MCQ | a) CCM register (workshop record) / b) Board / exec summary / c) Both | ELI-OUTPUT | always |

## Branch map
- **Q2** sets the candidate MUE list and control families (coal → methane / coal-dust /
  inrush; metalliferous → ground-control / ventilation).
- **Q3** selects the MUE → the bowtie is **referenced** from `bowtie-builder` (by name, not
  re-authored) → overlay the mining criticality.
- **Q5 → Q6 → Q7** loop **per nominated critical control**; any missing performance value →
  `[GAP]`, never fabricated.
- **Q8=b** applies the ICMM default criticality, echoed for confirmation.
- A nominated 'critical control' that is PPE/admin-only for a principal hazard → flagged via
  `KB-SNIP-HOC`, **not accepted** as a critical control.

## Echo-back
"CCM for MUE **{event}** at **{mine}** ({commodity / type}); **{n}** critical controls
nominated; criticality scheme **{scheme}**; output **{type}**. Confirm before I structure."
— echo the captured facts back and **confirm** before any structuring.

## Refuse-on-vague anchors
- **"Set up CCM for fire"** with no mine / scenario → ask for the specific MUE scenario
  (Q4 is the specificity anchor).
- A nominated **'critical control' that is PPE/admin-only** for a principal hazard → flag, do
  not accept (`KB-SNIP-HOC`); require a higher-order critical control or an explicit
  justified-or-escalated reliance.
- **No performance evidence** → `[GAP]`, never invent an engineering / PFD value.

## Domain evidence types (ELI-EVIDENCE)
Nominated critical controls; performance requirements / specifications; verification
activities + frequencies + last-verified records; the criticality / risk-rating scheme;
bowtie barriers (carried from `bowtie-builder`, not re-authored).
