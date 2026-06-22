# Methodology — Training Needs Analysis (role×competence)

The systematic TNA method this skill applies. The gap-scoring + prioritisation rules are
`KB-SNIP-TNA-METHOD`; the competence banding is `KB-DATA-COMPETENCE-LEVELS`; the legal-required
competencies are resolved from the jurisdiction row (UK MHSWR 1999 reg. 13 · US OSHA
standard-specific · India Factories Act 1948 s.7A(2)(c) via `hse-india`). Grounded in **ISO
45001:2018 clause 7.2 (competence)** and **7.3 (awareness)**.

> Core value: **every gap traces to a named role + an evidence source**, with a required
> competence, a named owner, and a target date. Refuse "train everyone"; never present
> "more training" as the sole control of a higher-order-controllable hazard.

---

## 1. Role profiling (refuse "everyone")

For each **named role** in scope (Q2 — refuse the vague "everyone"; require named roles +
headcounts), build a role profile from:

- the job description / role definition,
- the **real hazards** of the tasks that role performs (pull from a risk assessment / JSA
  where one exists),
- the **drivers** in scope (Q4: legal/statutory · new equipment or process · post-incident ·
  audit finding · refresher cycle).

A role with no named tasks/hazards is under-specified — ask, or record `[GAP]`; never invent.

## 2. Competence requirement derivation

For each role, derive its **required competencies** and, for each, the **required level**
(1 aware → 2 trained → 3 competent → 4 expert on `KB-DATA-COMPETENCE-LEVELS`). The required
level is set by the **task's risk, not the person**: a high-hazard task (hot work,
confined-space entry, LOTO, work at height) requires **level 3 (competent)** with a current
valid certification where the jurisdiction mandates one.

**Legal-required competencies are mandatory rows.** Resolve the Q5 jurisdiction and cite the
statutory source for every legally-mandated competence (e.g. a scaffolding supervisor's
statutory competence, a LOTO-authorised-person under 29 CFR 1910.147(c)(7), an MHSWR reg. 13
duty). A legal-required competence is **never omitted** from the matrix and **never downgraded
to "pass"**.

## 3. Current-state evidence

Band each **role×competence cell's current level** on `KB-DATA-COMPETENCE-LEVELS` from a
**named evidence source** (Q3): job descriptions · legal-required-competency records · training
records (dated, with assessor sign-off) · appraisal data · incident-driven gaps. Apply each
level's **evidence test** — e.g. level 3 (competent) needs independent assessment against
defined criteria + valid certification where the law names one. **Never assert a level without
evidence** — band as `[GAP]` and treat the cell as unmet until evidenced.

## 4. Gap scoring

For each cell, **gap = required level − current level**. Tabulate the **role×competence gap
matrix** (rows = roles, columns = competencies, cells = current/required + gap). A statutory
competence requirement that is unmet is a gap against its **named legal source** and ranks as a
mandatory gap regardless of headcount.

## 5. Single-point-of-failure (SPOF) flags

A **critical competence held by only one named person** is a single-point-of-failure: if that
person is absent, the competence — and any task it gates — is uncovered. Flag every SPOF **by
role, not identity** (small-cell suppression: where one named person is the sole holder, report
the gap and the resilience risk, never the person's name). SPOFs feed the priority order and the
training plan (cross-train a second holder).

## 6. Certification / expiry tracking

Build the **certification/expiry tracker**: each competence with a time-limited certificate
(first aid, forklift, IPAF/PASMA, confined-space, etc.) → the holder role, the expiry date, and
the **refresher due date** (lead-time before expiry). An expired or soon-to-expire statutory
certificate is a high-priority gap.

## 7. Prioritisation (risk × legal × gap size)

Rank the gaps by **gap size × (risk of the task the competence gates) × legal-mandate**.
Statutory and high-hazard competence gaps, expired statutory certificates, and SPOFs on
critical competences rank **first**. Low-risk awareness gaps rank last.

## 8. The prioritised, costed training plan (SMART, owned, dated)

For each prioritised gap produce a **SMART action** (`smart_actions.validate_register`):
specific intervention · measurable competence outcome · **assignable (named owner role)** ·
relevant to the gap · **time-bound (ISO due date)**, with an **indicative cost** (course/day-rate
/ internal-time estimate, flagged `[ASSUMPTION]` if not supplied). **Training is an administrative
control** (`KB-SNIP-HOC` + `controls`): where the underlying hazard admits a higher-order control
(eliminate/substitute/engineer), the plan must say so — "more training" is **never** the sole
treatment, and an admin-only treatment with no higher-order control and no justification is a
defect the Critic/QA pass catches.

## 9. Validate, then report

Run `references/QUALITY_CHECKLIST.md` before output, then assemble the branded report from
`assets/training-needs-analysis-report.template.json` (Scope & method → role×competence matrix →
scored gaps → SPOF register → expiry tracker → prioritised training plan → assumptions →
review & sign-off) and render via the `report-output` block.

## Worked example (competence-matrix slice)

A **scaffolding crew (5 roles)** on a UK construction project, driver = audit finding:

| Role | Scaffold inspection (req. L3) | Work-at-height rescue (req. L3) | Manual handling (req. L2) |
|---|---|---|---|
| Scaffolding Supervisor | **L2 (gap 1)** — statutory competent-person requirement unmet `[LEGAL]` | L3 ✓ | L3 ✓ |
| Advanced Scaffolder ×2 | L3 ✓ (sole inspection-competent on nights → **SPOF**) | L2 (gap 1) | L2 ✓ |
| Labourer ×2 | L1 (gap — supervised only) | L1 (gap 2) | L1 (gap 1) |

→ Priority 1: the **Supervisor's statutory scaffold-inspection competence** (legal + high-hazard).
Priority 2: cross-train a second night-shift inspection-competent scaffolder (resolve the SPOF).
Each becomes a SMART action with a named owner role and a due date; training is paired with the
higher-order site controls (edge protection, exclusion zones), never offered as the sole control.
