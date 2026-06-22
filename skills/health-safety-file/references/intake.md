---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "The H&S File is a structured residual-risk record, not calculation — there is no risk-matrix scoring step (the residual hazards are recorded as located facts a future worker could not anticipate, not re-scored here; any quantitative scoring was done upstream in the CPP / RAMS). So no matrix-size question is asked."
    ELI-COMPETENCY: "The H&S File does not assign operatives or competency cards to tasks (that is the CPP / RAMS); the only named persons it carries are the deliberately-supplied principal designer / client duty-holders and the owners of open completion items (a contractual record), captured at gap/handover time, not a competency intake question."
  branches:
    - {when: Q2, option: Updating an existing file, activates_output_section: revision-control-append, mandatory: true}
    - {when: Q3, activates_output_section: residual-and-unusual-hazards, mandatory: true}
    - {when: Q5, option: Maintenance + refurbishment + demolition, activates_output_section: demolition-arrangements, mandatory: false}
    - {when: Q6, option: UK, activates_kb_row: KB-REG-CDM2015, activates_output_section: cdm-reg12-5-basis, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: bocw-state-gap, mandatory: true}
---

# Structured intake — health-safety-file

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**.

**The GATE (refuse-on-vague):** no Health & Safety File is produced until both **a named
structure + use (Q1)** AND **at least one residual/unusual hazard (Q3) — or a stated "none
beyond the obvious" justification** — are captured. The file is about **what a future worker
could NOT reasonably anticipate**, not a general-spec dump; the skill **refuses a generic "a
building"** — ask again, or record `[ASSUMPTION]` / `[GAP]`; never invent an as-built detail
or a residual hazard. **Q1 also disambiguates the CDM document**: this skill owns the
**Health & Safety File** (the *handover* record at completion); a request for the
Pre-Construction Information (CON-02) or the Construction Phase Plan (CON-01) is routed to its
CDM-chain sibling.

**The residual-only-discipline lever (Q3):** record **only** the residual & unusual hazards a
future worker could not reasonably anticipate, **each located**. A routine/anticipatable
hazard, or the full general specification dumped in instead of the residuals, is a
specificity/defensibility failure — flag it, do not file it.

**The update-append rule (Q2):** *updating an existing file* and *single-package addition*
**APPEND** to the file under revision control — they **never overwrite** prior residual-risk
content.

**Two jurisdiction paths:** the **UK → CDM 2015 Reg 12(5) branch** (Q6 = UK → `KB-REG-CDM2015`
+ the Reg 12(5)–(9) basis; non-mandatory) and the **mandatory India → state branch** (Q6 =
India → Q6a + `KB-REG-IN-STATEFORMS`, **defers to `hse-india` / `bocw-compliance`, mandatory
state detection, literal `[GAP]`, never a minted national form number**).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named structure & use** | free-text | "Which structure — name it, what was built, and its intended use (e.g. 'Tower B office fit-out, levels 3-9, occupied commercial use')?" — **specificity anchor; refuse 'a building'.** Also **disambiguates the CDM document**: this skill owns the **H&S File** (handover record); a request for the PCI or the CPP routes to its sibling. | ELI-SUBJECT / ELI-SCOPE | always |
| Q2 | **File purpose** | MCQ | Project completion handover / Updating an existing file / Single-package addition — **an update or a single-package addition APPENDS, never overwrites prior residual-risk content (revision control)** | ELI-OUTPUT / ELI-SCOPE | always |
| Q3 | **Residual & unusual hazards present** | MCQ multi-select + free-text | Hazardous materials left in situ · Confined spaces · Fragile surfaces · Structural loadings/limits · High-voltage or unusual services · Fall-from-height maintenance access · Cleaning-access hazards · Other (+ detail) — **each LOCATED**; record only what a future worker could NOT reasonably anticipate (the could-not-anticipate test) | ELI-EXPOSURE | always |
| Q4 | **As-built information available** | MCQ multi-select + free-text | As-built drawings · Services records & isolation points · Material specifications · Commissioning records · Other (+ detail) — **each missing item is a documented `[GAP]`**, never silently absent | ELI-EVIDENCE / ELI-BASELINE | always |
| Q5 | **Future-work scope the file must serve** | MCQ | Maintenance only / Maintenance + refurbishment / Maintenance + refurbishment + demolition / Other (note the activities) — sets which future activities the safety arrangements must cover; demolition pulls in the most onerous arrangements | ELI-TEMPORAL / ELI-SCOPE | always |
| Q6 | **Jurisdiction** | MCQ | UK / USA / India / EU / Unknown — UK → CDM 2015 (Reg 12(5)–(9) + L153 App 4); USA → 29 CFR 1926 as-built/record equivalents; India → Q6a + BOCW; Unknown → ask before citing | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india` / `bocw-compliance`; confirm the state before citing any form; emit a literal `[GAP]`, never a minted national form number** | ELI-JURIS | Q6 == India |
| Q7 | **Handover & open-item owners** | free-text | "Who prepares & hands over the file (the **principal designer** under Reg 12(5)), who is the **client** that retains it, and who owns any open completion item — with the date it must close? **Name the duty-holders for the record.**" — never invent an appointment (record `[GAP]`) | ELI-OBLIGATIONS | always |

*ELI-INDUSTRY thin-covered (always construction; Q1/Q3 detail). ELI-OUTPUT is the H&S File.*

**Branch map:** `update-append` (Q2 = updating / single-package addition → the file **appends**
under revision control, never overwrites — **mandatory**); `residual-hazards` (Q3 → the
**mandatory** located residual & unusual hazards section, could-not-anticipate test applied);
`demolition` (Q5 = + future demolition → the demolition safety arrangements); `uk-cdm` (Q6 =
UK → `KB-REG-CDM2015` + the Reg 12(5)–(9) basis; non-mandatory); `india-bocw` (Q6 = India →
Q6a + `KB-REG-IN-STATEFORMS`, **mandatory** state detection, defers to `hse-india`).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before any
analysis: "H&S File for the Tower B office fit-out (levels 3-9, occupied commercial use),
purpose = completion handover; residual/unusual hazards = fragile atrium glazing (level 9),
presumed-asbestos riser lagging (risers 3 & 5), no permanent edge protection at the roof plant
deck — each located; as-builts held, **`[GAP]` = no commissioning record for the AHU**;
future-work scope = maintenance + refurbishment; prepared by the principal designer, retained
by the client; UK / CDM 2015 Reg 12(5) — correct?" The file records the residual hazards as
located facts a future worker could not anticipate, not re-scored risk.

## Refuse-on-vague anchors

- **The GATE:** Q1 (named structure + use) and Q3 (at least one located residual/unusual
  hazard, or a stated "none beyond the obvious" justification) are load-bearing — **refuse a
  generic "a building"** and **refuse a general-spec dump** in place of the residuals; never
  invent an as-built detail or a residual hazard (record `[GAP]`).
- Q4 with a missing as-built source is **not** a refusal — the missing item is flagged as a
  `[GAP]` and the file proceeds on **stated assumptions** (gap discipline).

## Domain evidence types (ELI-EVIDENCE)

As-built drawings · services records & isolation points · material specifications · asbestos
register / refurbishment-&-demolition survey · commissioning records · the existing H&S file
(for an update) · the handover & open-item owners per Q7.
