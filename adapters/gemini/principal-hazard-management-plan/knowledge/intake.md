---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-INDUSTRY, ELI-LOCATION, ELI-BASELINE, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY]
  omits:
    ELI-JURIS: "framework/ICMM-led, jurisdiction-independent — no statutory form output; the statutory linkage is handed off to dgms-statutory-pack."
    ELI-OBLIGATIONS: "workshop structuring, not a deadline-bound filing — no numbered-form deadline."
    ELI-TEMPORAL: "beyond the monitoring review cycle (captured under monitoring, Q5) there is no statutory deadline."
    ELI-EXPOSURE: "the exposed population is implicit in the named principal hazard + mine scenario (Q3/Q4); the PHMP manages the hazard pathway and its controls, not a separately-elicited exposed-population census."
  branches:
    - ask: ELI-INDUSTRY
      when: Q2
      # commodity × mine-type sets the hazard mechanisms + control families
      # (coal-UG strata vs opencast highwall; coal fire/explosion -> methane/coal-dust).
    - ask: ELI-BASELINE
      when: Q5
      # existing controls + monitoring seed the HoC-ranked control suite (KB-SNIP-HOC);
      # a PPE/admin-only treatment of a principal hazard is flagged.
    - ask: ELI-SCORING
      when: Q6
      option: "b) Default 5×5 (D-02 bands) — confirm"
      activates_kb_row: D-02-bands   # echo the default bands for confirmation
---

# Structured intake — principal-hazard-management-plan

> **Sibling note (D-04):** this intake shares ~80% of its surface with
> `icmm-critical-control-management` (the same commodity/mine-type branch driver, and the
> ICMM critical-control linkage carried over for performance + verification). By the
> per-skill contract decision (Rule 11 reads one file per skill) the two are **kept as
> separate self-contained files**, not a shared fragment — maintain them in step but do not
> extract a shared intake fragment.

Run **one question at a time** (`KB-SNIP-INTAKE`). MCQ where the answer space is
enumerable, free-text where it is open; **branch on the answers**; **echo the captured
facts back before any structuring**; **refuse on a vague subject** — a PPE/admin-only
treatment of a principal hazard is flagged not accepted, and an un-supplied engineering
value is `[GAP]`, **never invented**.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Develop a full PHMP or structure the workshop? | MCQ | a) Full PHMP / b) Structure the multidisciplinary workshop | ELI-SCOPE | always |
| Q2 | Commodity + mine type? | MCQ | a) Coal — UG / b) Coal — opencast / c) Metalliferous — UG / d) Metalliferous — opencast / e) Other | ELI-INDUSTRY | always (branch driver) |
| Q3 | Which principal hazard? | MCQ | strata failure / inrush-inundation / fire-explosion / ventilation failure / mobile-plant interaction / fall from height / hazardous energy / respirable dust (`KB-DATA-MINING-HAZARDS`) | ELI-SUBJECT | always |
| Q4 | Named mine + hazard scenario? | free-text | "Mine, location, and the specific hazard mechanism / scenario" — the refuse-on-vague anchor | ELI-LOCATION/ELI-SUBJECT | always |
| Q5 | Existing controls + monitoring? | free-text | "Controls already in place + the monitoring activities / data the team holds" | ELI-BASELINE/ELI-EVIDENCE | always |
| Q6 | Risk-rating scheme + criticality threshold? | MCQ | a) Org's existing matrix / scheme / b) Default 5×5 (D-02 bands) — confirm | ELI-SCORING | always |
| Q7 | Contributing disciplines / owners (roles)? | free-text | "Geotech / ventilation / mining engineer / mine manager — the workshop participants, as role labels" | ELI-COMPETENCY | always |
| Q8 | Output + audience? | MCQ | a) PHMP document / b) Workshop record / c) Both | ELI-OUTPUT | always |

## Branch map
- **Q2** sets the hazard mechanisms and control families (coal-UG strata vs. opencast
  highwall; coal fire/explosion → methane / coal-dust).
- **Q3** selects the principal hazard → HIRA structure + `risk_matrix` rating.
- **Q5** seeds the control suite (hierarchy-ranked, `KB-SNIP-HOC`); a PPE/admin-only
  treatment of a principal hazard → flagged, **not accepted**.
- **Q6=b** applies the default 5×5 (D-02 bands), echoed for confirmation.
- **Critical controls** → linked to ICMM CCM (`icmm-critical-control-management` /
  `KB-STD-ICMM-CCM`), carrying performance + verification.
- Any unsupplied engineering value → `[GAP]`, never fabricated.

## Echo-back
"PHMP for principal hazard **{hazard}** at **{mine, commodity / type}** ({full / workshop});
existing controls **{n}**; rating scheme **{scheme}**; disciplines **{roles}**; output
**{type}**. Confirm before I structure." — echo the captured facts back and **confirm**
before any structuring.

## Refuse-on-vague anchors
- **"Manage strata risk"** with no mine / scenario → ask for the specific hazard mechanism
  (Q4 is the specificity anchor).
- A **PPE/admin-only control of a principal hazard** → flag, do not accept (`KB-SNIP-HOC`);
  require a higher-order control or an explicit justified-or-escalated reliance.
- **Missing engineering value** → `[GAP]`, never invent.

## Domain evidence types (ELI-EVIDENCE)
Hazard-analysis data (geotech, gas, hydrogeology per hazard); the existing control
inventory; monitoring activities + data; the criticality / risk-rating scheme; the ICMM CCM
critical-control performance + verification (carried over).
