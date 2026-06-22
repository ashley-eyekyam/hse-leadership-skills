---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "An arc-flash assessment computes the incident energy from the IEEE 1584 electrical parameters (Q4) afresh per equipment; there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the de-energization decision (Q2) and the computed cal/cm² are the assessment's starting facts."
    ELI-SCORING: "The arc-flash result is COMPUTED by the deterministic IEEE 1584-2018 engine (incident energy / boundary / PPE category), not chosen on a qualitative scoring scale; risk_matrix is used only for a qualitative residual framing, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: "no", activates_questions: [Q3], activates_kb_row: KB-SNIP-DEENERGIZE-FIRST, mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-ELECTRICAL, mandatory: true}
---

# Structured intake — arc-flash-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named equipment (Q1 — the specificity anchor)**, then — **first among the controls** — the
**de-energization decision (Q2)** (de-energization is the primary control, not an afterthought),
the **energized-work justification (Q3, only if Q2 = no)**, the **IEEE 1584 electrical parameters
(Q4)**, the **PPE-selection method (Q5)**, and the **jurisdiction (Q6)**. **Refuse to assess "a
panel": you need the named equipment (Q1), the de-energization decision (Q2), and the IEEE 1584
required inputs (Q4) before any computation. Refuse a PPE-led "issue a CAT 2 suit" with no recorded
de-energization decision.** The incident energy is **never** narrated — it is computed by the
`arcflash.py` engine, and a missing required parameter is a `[GAP]`, never an invented fault current.

Two load-bearing branches: the **energized-work-justification branch** (Q2 = no → Q3, against OSHA
1910.333(a)(2) / EAWR reg 14 — a bare convenience reason is refused; non-mandatory) and the
**mandatory India→state branch** (Q6 = India → Q6a + `hse-india`; confirm the state before citing
any rule — never a national form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named equipment** (the panel / switchgear / MCC / transformer secondary / distribution board + manufacturer + function) | free-text | "Name the exact equipment + type + manufacturer + function (e.g. 'main switchboard MSB-1, 400 V, building incomer'). **Refuse 'a panel' / 'the switchroom' — the assessment is equipment-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Can the task be done de-energized?** (asked FIRST among the controls — de-energization is the primary control; yes → scope the ESWC per NFPA 70E Article 120, not energized PPE; no → must justify, branch to Q3) | mcq | yes / no | ELI-SCOPE | always |
| Q3 | *(energized only)* **Energized-work justification** | free-text | "Justify against OSHA 1910.333(a)(2) ('additional/increased hazard or infeasible') **or** EAWR reg 14 ('unreasonable to be dead'). **A bare 'it's quicker / production needs it' is REFUSED** — economic convenience alone does not justify energized work. Record verbatim; route to an energized-work permit (Annex J)." | ELI-OBLIGATIONS | Q2 == no |
| Q4 | **Electrical parameters** (the IEEE 1584 method inputs) | free-text | "Nominal system voltage, available bolted fault / short-circuit current, upstream protective-device clearing time, electrode configuration (VCB/VCBB/HCB/VOA/HOA), enclosure & gap dimensions, working distance. **Refuse to compute on a missing required parameter → record a `[GAP]` and request a power-system / short-circuit study; never invent a fault current or a clearing time.**" | ELI-EXPOSURE | always |
| Q5 | **PPE-selection method** | mcq | incident-energy analysis (130.5(G), via the engine) / arc-flash PPE category table (130.7(C)(15)) — **the two methods are not mixed on the same equipment** | ELI-EVIDENCE | always |
| Q6 | **Jurisdiction** | mcq | USA / UK / EU / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq+free-text | Generation / Transmission-Distribution / Industrial-Commercial / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / substation / switchroom is the equipment in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full arc-flash risk-assessment report (consultant) / equipment arc-flash label + PPE summary (manager) / quick boundary + PPE-category answer (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the label-install / study-refresh / remediation actions and who is the competent person (qualified electrical engineer) verifying the study (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-system-change / on-protection-change / 5-yearly (or sooner) / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `energized-justification` (Q2 = no → Q3 + `KB-SNIP-DEENERGIZE-FIRST`; OSHA
1910.333(a)(2) / EAWR reg 14; convenience refused; non-mandatory); `india-state` (Q6 = India → Q6a
+ `hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q3 / Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing arc flash for: main switchboard MSB-1, 400 V building incomer, Substation 2, Maharashtra;
task can be de-energized → ESWC scoped (Article 120); IEEE 1584 inputs Voc 400 V, Ibf 25 kA, gap 32 mm,
VCB, working distance 455 mm, clearing time 0.2 s; PPE-selection by incident-energy analysis; full
arc-flash report; review on protection change — correct?" The incident energy is then computed by the
`arcflash.py` engine, never narrated.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a panel" / "the switchroom"; ask again or record
  `[GAP]`, never invent the equipment or its rating.
- **De-energization first, PPE last** — a PPE-led treatment ("issue a CAT 2 arc-flash suit") with
  no recorded de-energization decision (Q2) is **refused and pushed up the hierarchy**; arc-rated
  PPE is the documented last line, never the headline control. Energized work (Q2 = no) is never
  authorised on convenience grounds (Q3).
- **No invented parameters** — a missing IEEE 1584 input (Q4) is a `[GAP]` and a request for a
  short-circuit / protection study; the skill **never** invents a fault current, a clearing time,
  or a cal/cm² value. **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The de-energization decision (Q2) and any energized-work justification (Q3 — OSHA 1910.333 / EAWR
reg 14) · the IEEE 1584 electrical parameters (Q4 — voltage, bolted fault current, clearing time,
electrode configuration, gap, working distance) · the PPE-selection method (Q5) · the computed
incident energy / boundary / PPE category from `arcflash.py` (not narrated) · a prior arc-flash
burn / electrocution incident referenced for context (de-identified to role label — injury/health
detail is highest-sensitivity).
