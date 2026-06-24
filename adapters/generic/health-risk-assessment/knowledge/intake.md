---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}
  branches:
    - {when: Q1, option: ergonomics, activates_questions: [Q5, Q5a], activates_kb_row: KB-STD-GHS-ERGO, mandatory: false}
    - {when: Q3, option: none-yet, activates_questions: [Q3a], mandatory: false}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
---

# Structured intake — health-risk-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the answers;
**echo the captured facts back for confirmation before any analysis**. The intake opens
with the **health-hazard type (Q1)**, which branches to that hazard's method, then captures
the **SEG basis (Q2 — the specificity anchor)**, the **exposure basis (Q3)**, the OEL
source, the ergonomics tool (only when ergonomics is selected at Q1), and the jurisdiction.
**Refuse to produce an exposure-vs-OEL comparison until the hazard type (Q1), the named SEG
tasks/roles (Q2), and an exposure basis (Q3) are captured** — ask again, or record
`[ASSUMPTION]` / `[GAP]`; never invent an exposure or a limit.

Three load-bearing branches: the **ergonomics-tool branch** (Q1 = ergonomics → Q5 tool +
Q5a engine inputs + the `KB-STD-GHS-ERGO` row + the `ergonomics` engine; non-mandatory); the
**no-data branch** (Q3 = none-yet → Q3a → recommend a monitoring strategy FIRST, no
fabricated comparison); and the **mandatory India→state branch** (Q6 = India → Q6a +
`KB-REG-IN-STATEFORMS`; confirm the state before citing any form — never a national form
number).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Health-hazard type** (the assessment scope) | mcq multi-select | chemical / inhalation / noise / vibration / ergonomics / thermal / biological — branch to that hazard's method | ELI-SCOPE | always |
| Q2 | **The named tasks/roles & SEG basis** | free-text | "Name the exact tasks/roles being assessed and the similar-exposure groups (e.g. 'press-shop operators on line 2: load → stroke → eject → stack'). **Refuse a generic SEG ('all staff') — this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q3 | **Exposure data** | mcq + free-text | measured / estimated / none-yet | ELI-EVIDENCE | always |
| Q3a | *(none-yet only)* Why no data, and is monitoring planned? | free-text | "No exposure data → I recommend a **monitoring strategy first** and will NOT fabricate an OEL comparison." | ELI-EVIDENCE | Q3 == none-yet |
| Q4 | **OEL source** | mcq | jurisdiction WEL/PEL / ACGIH TLV / other — resolved from KB-DATA-OEL-LIMITS / KB-DATA-EXPOSURE-LIMITS with source+year | ELI-OBLIGATIONS | always |
| Q5 | **Ergonomics tool** | mcq | RULA / REBA / NIOSH / manual-handling | ELI-SCORING | Q1 == ergonomics |
| Q5a | *(ergonomics only)* Confirm the engine inputs | free-text | "Provide the joint scores / lift geometry so the `ergonomics` engine computes RULA/REBA/NIOSH deterministically." | ELI-SCORING | Q1 == ergonomics |
| Q6 | **Jurisdiction** | mcq | India / UK / USA / EU / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm the state before citing any form** | ELI-JURIS | Q6 == India |
| Q7 | Industry / sector | mcq + free-text | Construction / Manufacturing / Oil-and-Gas / Chemicals / Mining / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site/area/process is each SEG exposed in?" | ELI-LOCATION | always |
| Q9 | Who is in each SEG (exposed population) | mcq multi-select | own workers / contractors / agency / vulnerable groups (young / new-or-expectant) | ELI-EXPOSURE | always |
| Q10 | Existing controls & current state | free-text | "What exposure controls and surveillance already exist for this SEG? (seeds the initial-vs-residual baseline)" | ELI-BASELINE | always |
| Q11 | Output artifact wanted + its reader | mcq | full HRA report (consultant) / SEG surveillance schedule (manager) / single-hazard check (frontline) | ELI-OUTPUT | always |
| Q12 | **Assessor + action owners** | free-text | "Who is the competent person (occupational hygienist / OH physician role) performing this, and who owns the controls & surveillance actions? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q13 | **Review cycle / next review** | mcq + free-text | annual / on-exposure-change / on-surveillance-trigger / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `ergonomics-tool` (Q1 = ergonomics → Q5 + Q5a + `KB-STD-GHS-ERGO` + the
engine; non-mandatory); `no-data` (Q3 = none-yet → Q3a → monitoring-strategy-first;
non-mandatory); `india-state` (Q6 = India → Q6a + `KB-REG-IN-STATEFORMS`; **mandatory**).

## Echo-back

After the last applicable question (Q13, and Q5/Q5a, Q3a, Q6a if their branch ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing: press-shop noise exposure for the line-2 operator SEG, Plant 3, Maharashtra,
own workers, measured 92 dB(A), UK WEL basis, full HRA report, review on surveillance
trigger — correct?" Each SEG/agent is compared to its cited OEL individually at the
comparison step.

## Refuse-on-vague anchors

- **Q2 is the specificity anchor** — refuse a generic SEG ("all staff", "the workforce") or
  a vague task; ask again or record `[ASSUMPTION]` / `[GAP]`, never invent a SEG.
- **No comparison without an exposure basis** — if Q1 (hazard), Q2 (named SEG tasks/roles)
  and Q3 (an exposure basis) are not all captured, **do not produce an exposure-vs-OEL
  comparison**; on Q3 = none-yet, recommend a monitoring strategy first. **Never proceed on
  a vague input.**

## Domain evidence types (ELI-EVIDENCE)

Personal/static exposure monitoring (noise dosimetry, dust/fume sampling, HAV magnitude) ·
SDS for any substance named in Q2 · prior health-surveillance outcomes (audiometry, lung
function — **special-category, de-identified by SEG**) · the org risk matrix if non-default ·
the ergonomics-engine inputs (joint scores / lift geometry).
