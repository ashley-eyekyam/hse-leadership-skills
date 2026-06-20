---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-BASELINE,
           ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "The finding text (Q2) carries operational context; sector is not load-bearing for HoC ranking or verification."
    ELI-EXPOSURE: "A CAPA addresses a finding/cause; the at-risk population is upstream in the audit/incident that produced it."
  branches:
    - {when: Q0, option: Incident, activates_questions: [Q0a], mandatory: false}
    - {when: Q0, option: Audit, activates_questions: [Q0a], mandatory: false}
    - {when: Q0a, option: "Yes", activates_output_section: ingested-finding-cause-capa, mandatory: false}
    - {when: Q1, option: India, activates_questions: [Q1a], activates_kb_row: KB-REG-IN-STATEFORMS, mandatory: true}
    - {when: Q3, activates_output_section: light-5whys, mandatory: false}
    - {when: Q8, option: Multi-action register, activates_output_section: capa-register-fanout, mandatory: false}
---

# Structured intake — capa-manager

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open, branching on the
answers. **Never proceed on a vague finding**; record `[GAP]` for missing facts and
`[ASSUMPTION]` for anything inferred — **never invent a cause or an action**. The intake
opens with the **source gate (Q0)**; when a sibling `incident-investigation`/`safety-audit`
output is supplied it runs the **INGEST branch (Q0a)** — lifting the finding + cause
id(s) + any first CAPA + the de-identified facts instead of re-eliciting them.

Branches: the **ingest branches** (Q0 = Incident / Audit → Q0a; Q0a = Yes →
ingested-finding-cause-capa, skips Q2/Q3 re-elicitation — the B6→B7 CAPA-schema seam);
the **mandatory India→state branch** (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`); the
**no-root-cause branch** (Q3 absent → light 5-Whys); and the **register branch** (Q8 =
Multi-action register → the CAPA-register fan-out).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | **Source of the finding/cause this CAPA addresses** | MCQ | Audit / Incident / Inspection / Near-miss / Other — *Incident* → offer the INGEST branch (an `incident-investigation` output?); *Audit* → offer the INGEST branch (a `safety-audit` finding set?); all others → the capture path | ELI-SCOPE | always |
| Q0a | *(if a sibling output exists)* **Supply it to ingest?** — *Yes* runs the **INGEST branch**: lift the finding + cause id(s) + any first CAPA + de-identified facts, skip Q2/Q3 re-elicitation, proceed to confirm + complete; *No* → capture manually | MCQ + free-text | Yes / No | ELI-EVIDENCE | Q0 == Audit / Incident |
| Q1 | **Jurisdiction** | MCQ | India / UK / USA / EU / Other / Unknown — India → Q1a (state) → the §kb-selection row + the documented corrective-action duty | ELI-JURIS | always |
| Q1a | *(India only)* **Which state?** | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — resolves `KB-REG-IN-STATEFORMS`; **mandatory state detection** — confirm before citing | ELI-JURIS | Q1 == India |
| Q2 | **The finding / nonconformity / incident cause** (the anchor) | free-text | "State the exact finding, nonconformity, or incident cause this CAPA addresses, and against which requirement/clause." The **specificity anchor** — refuse to proceed on "general non-compliance" | ELI-BASELINE | Q0a == No (manual capture) |
| Q2b | **Where / which area the finding applies to** | free-text | "Which specific site/area/asset does this finding apply to? (if not already clear in Q2)" | ELI-LOCATION | Q0a == No and location absent from Q2 |
| Q3 | **Root cause (if known)** | free-text | "Is the root cause established? If yes, state it (or the ingested cause id RC-n). If no, I'll run a brief 5-Whys to establish one." If absent → step 3 light `rca`; if a cause id is ingested → reuse | ELI-EVIDENCE | always |
| Q4 | **Proposed actions, if any** | free-text | "Any corrective or preventive actions already proposed? (I'll rank them by the hierarchy of controls and fill the gaps.)" Seeds step 4; flags any PPE/admin-only proposal for higher-order escalation | ELI-OBLIGATIONS | always |
| Q5 | **Owners** | free-text | "Who owns each action? (named role/person — no 'TBD'.)" → `smart_actions` owner field; refuse anonymous owners | ELI-COMPETENCY | always |
| Q6 | **Due dates** | free-text | "Target completion date for each action (ISO date — no 'ASAP'.)" → `smart_actions` `due`; validated ISO-8601 | ELI-TEMPORAL | always |
| Q7 | **Verification / effectiveness-check method** | MCQ + free-text | Re-audit / Re-inspection / Metric-KPI trend / Observation-walkdown / Document-record check / Other (+ free-text) → the `verification.method` (the lifecycle step this skill owns) | ELI-OUTPUT | always |
| Q8 | **CAPA scope** — single = single-threaded triage; register = fan-out | MCQ | Single action (close-out) / Multi-action register | ELI-SCORING | always |

**Branch map:** `ingest-incident`/`ingest-audit` (Q0 = Incident / Audit → Q0a);
`ingest-yes` (Q0a = Yes → ingested-finding-cause-capa, skips Q2/Q3); `india-state`
(Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`; **mandatory**); `no-root-cause` (Q3 absent →
light-5whys); `register` (Q8 = Multi-action register → capa-register-fanout).

## Echo-back

After the last applicable question, **echo a captured-facts summary** and confirm before
proceeding: "Managing CAPA for Audit NC-07 (emergency lighting, Bay 3, Maharashtra) →
cause RC-1 (no PM schedule for life-safety systems); 1 corrective + 1 preventive action,
owners and dates as given, verification by re-inspection in 30 days — correct?" On the
INGEST branch the echo confirms what was lifted from the sibling output before this skill
completes/manages it.

## Refuse-on-vague anchors

- Q2 is the anchor — refuse "general non-compliance"; never invent a cause or action;
  refuse anonymous owners (Q5) and "ASAP" dates (Q6).

## Domain evidence types (ELI-EVIDENCE)

The sibling `safety-audit` register or `incident-investigation` RCA to ingest (Q0a, by
finding/cause id, **using the verbatim B5/B6 CAPA schema** `{action, owner, due, measure,
links_to_cause, hoc_tier}`) · any already-proposed actions · the requirement/clause the
finding is against.

*The **B6→B7 CAPA-schema seam** is the one cross-skill data contract in this family — the
`ingest-audit`/`ingest-incident` branches reference the shared schema; the De-identifier
re-checks ingested facts (not assumed clean).*
