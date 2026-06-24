---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING,
           ELI-COMPETENCY, ELI-TEMPORAL]
  omits: {}
  branches:
    - {when: Q5, option: India, activates_questions: [Q5a], activates_kb_row: KB-REG-IN-FACTORIES, mandatory: true}
---

# Structured intake — training-needs-analysis

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**scope gate (Q1)**, captures the **named roles + headcounts (Q2 — the specificity anchor;
refuse "everyone")** and **at least one competence source (Q3)**, then the drivers,
jurisdiction, scoring scale, owners and review cadence. The **mandatory India→state branch**
(Q5 = India → Q5a) resolves the state and **defers to `hse-india`** — never a national form
number.

**The two load-bearing refuse-on-vague anchors:** Q2 (named roles — refuse "everyone") and Q3
(at least one competence source). **No role×competence matrix is produced** until both are
captured.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Scope of this TNA | MCQ | Whole site / Single function or team / Specific project / New-hire cohort | ELI-SCOPE | always |
| Q2 | **Roles in scope (+ headcounts)** | free-text | "List the **named roles** and headcounts (e.g. 'Scaffolding Supervisor ×1, Advanced Scaffolder ×2, Labourer ×2'). **'Everyone' is refused** — give the named roles." — the specificity anchor; refuse a vague answer | ELI-SUBJECT | always |
| Q2b | How many people / who is in scope | free-text | "Total headcount across the roles in Q2, and any contractors/agency staff included?" (sizes the matrix + the costed plan) | ELI-EXPOSURE | always |
| Q3 | **Competence sources available** | MCQ multi-select | Job descriptions / Legal-required competencies / Training records / Appraisal data / Incident-driven gaps — **at least one required; branch: if none, ask which can be supplied** | ELI-EVIDENCE | always |
| Q3b | Existing competence / current state | free-text | "What is already known about current competence (current certificates held, who is signed off for what)? — seeds the current-vs-required baseline (or 'none' → I'll flag `[GAP]`)" | ELI-BASELINE | always |
| Q4 | Driver for this TNA | MCQ | Legal/statutory / New equipment or process / Post-incident / Audit finding / Refresher cycle | ELI-OUTPUT | always |
| Q4b | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / General-Other (+ detail) — selects the role-hazard set | ELI-INDUSTRY | always |
| Q4c | Site / location | free-text | "Which specific site/area/asset does this workforce operate on?" (grounds the task hazards the competencies gate) | ELI-LOCATION | always |
| Q5 | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown (India → Q5a) — resolves the **legal-required-competency** row | ELI-JURIS | always |
| Q5a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defers to `hse-india`, never a national form number** | ELI-JURIS | Q5 == India |
| Q5b | Legal-required competencies / obligations | free-text | "Any statutory competence or training duties for these roles (e.g. scaffold-inspection competent person, LOTO authorised person, first-aid cover ratio, plant tickets)?" — never omitted from the matrix | ELI-OBLIGATIONS | always |
| Q6 | Required-level / competence-scale basis | MCQ | Use the 4-level scale (aware/trained/competent/expert) default / Supply our competence framework | ELI-SCORING | always |
| Q6b | Analysis owner + action owners | free-text | "Who is the competent person performing this TNA (role), and who owns the training actions? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q6c | Review cycle / refresher horizon (+ budget) | MCQ + free-text | Annual / On change / Other (+date); plus an optional budget/time envelope — feeds the expiry tracker + the costed plan | ELI-TEMPORAL | always |

**Branch map:** `india-state` (Q5 = India → Q5a + `KB-REG-IN-FACTORIES`; **mandatory** state
detection, defers to `hse-india`).

## Echo-back

After the last applicable question (Q6c, and Q5a if the branch ran), **echo a captured-facts
summary** and confirm before any analysis:
"Analysing: training needs for the **scaffolding crew (Supervisor ×1, Advanced Scaffolder ×2,
Labourer ×2)** on the **north-tower project**, UK construction, driver = audit finding,
competence sources = job descriptions + training records, 4-level scale, review annual —
correct?" Only on confirmation does the role×competence matrix get built.

## Refuse-on-vague anchors

- **Q2 is the primary specificity anchor — "everyone" is refused.** No matrix is produced until
  the **named roles + headcounts** are captured; ask again or record `[GAP]`, never invent a
  role set.
- **Q3 is the evidence anchor — at least one competence source is required.** Without a
  competence source no current-state level can be evidenced; refuse to proceed (branch: ask
  which source can be supplied).
- A statutory competence requirement (Q5b) is **never omitted** and **never downgraded to
  "pass"**.

## Domain evidence types (ELI-EVIDENCE)

Job descriptions / role profiles · legal-required-competency records (statutory tickets,
authorised-person registers) · dated training records with assessor sign-off · appraisal /
competence-assessment data · incident/near-miss-driven competence gaps · current certification
register (for the expiry tracker).
