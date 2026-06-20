---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "An audit assesses conformity against criteria, not a pre-existing controls baseline; the criteria set (Q-Crit) is the reference."
    ELI-EXPOSURE: "Who a nonconformity affects is derived per-finding from the evidence, not a separate gate."
  branches:
    - {when: Q-Juris, option: India, activates_questions: [Q-Juris-a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
    - {when: Q-Crit, option: ISO 45001, activates_kb_row: KB-STD-ISO45001, activates_output_section: clause-criteria-set, mandatory: false}
    - {when: Q-Crit, option: A regulatory regime, activates_output_section: duty-criteria-set, mandatory: false}
    - {when: Q-Crit, option: A custom checklist, activates_output_section: custom-items-no-external-clause, mandatory: false}
---

# Structured intake — safety-audit

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**.
**Q-Scope and Q-Crit are load-bearing** — refuse to proceed on a vague scope ("general
site audit") or an undeclared criteria set: ask, or record `[GAP]`. An audit with no
defined boundary is unauditable; an audit with no criteria set cannot classify a finding;
**never invent a clause.**

Branches: the **mandatory India→state branch** (Q-Juris = India → Q-Juris-a +
`KB-REG-IN-STATEFORMS`; confirm the state before citing a form) and the **criteria gate**
(Q-Crit = ISO 45001 → `KB-STD-ISO45001` clause-criteria-set; A regulatory regime → the
jurisdiction-fragment duty-criteria-set; A custom checklist → the user's items, no
external clause cited).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q-Juris | Jurisdiction | MCQ | India / UK / USA / EU / Other / Unknown | ELI-JURIS | always |
| Q-Juris-a | *(India only)* Which state? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; confirm before citing a form** | ELI-JURIS | Q-Juris == India |
| Q-Scope | **The site / system / process audited, and its boundary** | free-text | "Describe the exact subject and its boundary (e.g. 'the permit-to-work system at the Plant 3 maintenance shop — issuance → isolation → sign-off → close-out; excludes hot-work permits')." — **the specificity anchor; refuse a vague answer** | ELI-SCOPE / ELI-SUBJECT | always |
| Q-Crit | **The standard / criteria to audit against** — **the criteria gate** resolving the clause/checklist set walked finding-by-finding (*A regulatory regime* = OSHA / Factories Act / HSWA leans on the Q-Juris fragment; *A custom checklist* = free-text items, no external clause cited) | MCQ + free-text | ISO 45001 / A regulatory regime / A custom checklist | ELI-OBLIGATIONS | always |
| Q-Type | **Audit type** | MCQ | Compliance (vs law) / Management-system (vs ISO 45001) / Process (vs an SOP-spec) — tunes the evidence-sufficiency bar + classification lens | ELI-OUTPUT | always |
| Q-Evid | Evidence available | free-text | "What evidence can you provide or did you gather? (documents/records, observations, interview notes by role, photos, prior audit/CAPA history)." | ELI-EVIDENCE | always |
| Q-Industry | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / General-Other | ELI-INDUSTRY | always |
| Q-NCrate | Org risk-matrix size (rating nonconformities) | MCQ | 3×3 / 4×4 / **5×5 (default)** / Supply our matrix | ELI-SCORING | always |
| **Q-Team** | **Audit team / lead auditor + CAPA owners** | free-text | "Who is conducting this audit (lead auditor role/competence, ISO 19011)? Who will own corrective actions for nonconformities? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| **Q-When** | **Audit date + CAPA cycle** | free-text | "Audit date (or window), and the default corrective-action due window for nonconformities (e.g. 30 days for major, 90 for minor)?" | ELI-TEMPORAL | always |
| Q-Loc | Physical location / environment of the audited subject | free-text | "Which specific site/area/asset/line is in the audit boundary? (the physical setting the walkdown covers)" | ELI-LOCATION | always |

**Branch map:** `india-state` (Q-Juris = India → Q-Juris-a + `KB-REG-IN-STATEFORMS`;
**mandatory**); `crit-iso`/`crit-regulatory`/`crit-custom` (Q-Crit → the matching
criteria-set path; ISO → `KB-STD-ISO45001`, A regulatory regime → jurisdiction-fragment,
A custom checklist → no external clause cited).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
any analysis: "Auditing: the PTW system at Plant 3 maintenance shop (issuance →
isolation → sign-off → close-out, hot-work excluded), against ISO 45001 clause 8.1 + the
org's PTW procedure, management-system type, Maharashtra, 5×5 matrix, lead auditor
[role], audit date [date], CAPA window 30/90 days — correct?"

## Refuse-on-vague anchors

- Q-Scope (boundary) and Q-Crit (criteria set) are both load-bearing — refuse a "general
  site audit" with no boundary (unauditable) or an undeclared criteria set (a finding
  cannot be classified). `[GAP]` where the criteria set is incomplete; never invent a
  clause.

## Domain evidence types (ELI-EVIDENCE)

Documents/records (procedures, permits, training records, maintenance logs) · observations
(walkdown notes) · interview notes **by role** · photos · **prior audit + CAPA history** ·
the org's procedure when Q-Type = Process · the criteria document when Q-Crit = A custom
checklist.

*The emitted CAPA register feeds the **B6→B7 seam** (verbatim B5 schema) — the same data
contract `capa-manager` ingests.*
