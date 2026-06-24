---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-SCORING: "The PCI is information assembly + gap documentation, not calculation — there is no risk-matrix scoring step in this skill (the significant hazards it surfaces are scored downstream in the CPP / RAMS). So no matrix-size question is asked up front."
    ELI-COMPETENCY: "The PCI does not assign operatives or competency cards to tasks (that is the CPP / RAMS); the only named persons it carries are the deliberately-supplied gap-action owners + client/principal-designer duty-holders (a contractual record), captured at gap-documentation time, not a competency intake question."
  branches:
    - {when: Q2, activates_output_section: information-gaps-register, mandatory: true}
    - {when: Q5, option: feasibility, activates_output_section: stage-known-limits, mandatory: false}
    - {when: Q6, option: UK, activates_kb_row: KB-REG-CDM2015, activates_output_section: cdm-reg4-basis, mandatory: false}
    - {when: Q6, option: USA, activates_kb_row: KB-REG-OSHA1926, activates_output_section: osha-1926-basis, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: bocw-state-gap, mandatory: true}
---

# Structured intake — pre-construction-information

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**.

**The GATE (refuse-on-vague):** no Pre-Construction Information pack is produced until both
**a named project + client (Q1)** and **the existing-structure information status — present
or `[GAP]` (Q2)** are captured. The skill **refuses a generic "a project"** — ask again, or
record `[ASSUMPTION]` / `[GAP]`; never invent a survey result. **Q1 also disambiguates the
CDM document**: this skill owns the **Pre-Construction Information**; a request for the
Construction Phase Plan (CON-01) or the Health & Safety File (CON-03) is routed to its
CDM-chain sibling.

**The gap-discipline lever (Q2):** for each existing-structure information source the user
does **not** have, the missing source is recorded as a documented `[GAP]` with a named owner
+ due date — **never silently omitted**. A PCI that drops a missing asbestos survey instead
of flagging it is a defensibility failure.

**Two jurisdiction paths:** the **UK → CDM 2015 Reg 4 branch** (Q6 = UK → `KB-REG-CDM2015` +
the Reg 4 basis; non-mandatory) and the **mandatory India → state branch** (Q6 = India → Q6a
+ `KB-REG-IN-STATEFORMS`, **defers to `hse-india` / `bocw-compliance`, mandatory state
detection, literal `[GAP]`, never a minted national form number**).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named project & client** | free-text | "Which project — name it, its scope/works, and the **client's role** (e.g. 'Tower B brownfield refurbishment: strip-out + reclad levels 3–5, occupied lower floors; client = the building owner')?" — **specificity anchor; refuse 'a project'.** Also **disambiguates the CDM document**: this skill owns the **PCI**; a request for the CPP or the H&S File routes to its sibling. | ELI-SUBJECT / ELI-SCOPE | always |
| Q2 | **Existing-structure information sources** | MCQ multi-select + free-text | Asbestos survey / Existing H&S file / As-built & services drawings / Ground investigation / Structural surveys / Contaminated-land report / Other (+ detail) — **for EACH source the user does NOT have, it becomes a documented `[GAP]` with an owner + date, never silently omitted** | ELI-EVIDENCE / ELI-BASELINE | always |
| Q3 | **Site & surroundings** | free-text | "What's around the site — adjacent occupancies, the public interface, access/egress constraints, overhead/buried services, neighbouring activities, boundaries?" | ELI-LOCATION / ELI-EXPOSURE | always |
| Q4 | **Known significant hazards** | MCQ multi-select + free-text | Asbestos / ACMs · Buried/overhead services · Contaminated ground · Unstable structures · Confined spaces · Traffic / public interface · Other (+ detail) — the significant design/construction hazards a designer/contractor must be told of | ELI-EXPOSURE | always |
| Q5 | **Project stage** | MCQ | Feasibility / Pre-tender / Design-in-progress — **sets how much can reasonably be known**; an early stage with little surveyed is still PCI, with the unknowns recorded as `[GAP]` | ELI-TEMPORAL / ELI-SCOPE | always |
| Q6 | **Jurisdiction** | MCQ | UK / USA / India / EU / Unknown — UK → CDM 2015 (Reg 4 + L153 App 1); USA → 29 CFR 1926; India → Q6a + BOCW; Unknown → ask before citing | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india` / `bocw-compliance`; confirm the state before citing any form; emit a literal `[GAP]`, never a minted national form number** | ELI-JURIS | Q6 == India |
| Q7 | **Gap-action owners & timing** | free-text | "Who owns closing each information gap (e.g. the client commissions the asbestos survey), and by when must it close before the dependent works can start? **Name the owners for the gaps register.**" — never invent an appointment (record `[GAP]`) | ELI-OBLIGATIONS | always |

*ELI-INDUSTRY thin-covered (always construction; Q1/Q4 detail). ELI-OUTPUT is the PCI pack.*

**Branch map:** `missing-source` (Q2 any source absent → the **mandatory** information-gaps
register row + owned/dated action); `early-stage` (Q5 = feasibility → the stage's known
limits are stated); `uk-cdm` (Q6 = UK → `KB-REG-CDM2015` + the Reg 4 basis; non-mandatory);
`us-osha` (Q6 = USA → `KB-REG-OSHA1926`; non-mandatory); `india-bocw` (Q6 = India → Q6a +
`KB-REG-IN-STATEFORMS`, **mandatory** state detection, defers to `hse-india`).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
any analysis: "PCI for the Tower B brownfield refurbishment (strip-out + reclad levels 3–5,
occupied lower floors), client = building owner; sources held = existing H&S file +
as-builts; **`[GAP]` = no asbestos survey, no ground investigation** (owners + dates set);
surroundings = public footpath + adjacent occupier; known hazards = asbestos + buried
services; pre-tender stage; UK / CDM 2015 Reg 4 — correct?" The significant hazards surfaced
here are scored downstream in the CPP / RAMS, not in this pack.

## Refuse-on-vague anchors

- **The GATE:** Q1 (named project + client) and Q2 (existing-structure information status —
  present or `[GAP]`) are load-bearing — **refuse a generic "a project"**; never invent a
  survey result or a gap-action owner (record `[GAP]`).
- Q2 with a missing source is **not** a refusal — the missing source is flagged as a `[GAP]`
  with an owner + date and the pack proceeds on **stated assumptions** (gap discipline).

## Domain evidence types (ELI-EVIDENCE)

Asbestos / refurbishment-&-demolition survey · the existing health & safety file · as-built
& services drawings · ground investigation / contaminated-land report · structural surveys ·
the project programme / stage · the gap-action owners per Q7.
