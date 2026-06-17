# Safety-audit methodology — the ISO 45001 9.2 internal-audit loop

The full audit method this skill applies. The SKILL.md Workflow is the lean step
list; this file holds the finding-classification rules, the sampling and
evidence-sufficiency guidance, and the criteria-resolution detail.

## 1. Method vs criteria (the distinction the whole skill turns on)

- **Method** = *how* the audit is conducted. Always **ISO 45001 clause 9.2**
  (internal audit): establish scope and criteria → plan → gather and assess
  objective evidence per criterion → record a finding per clause traced to
  evidence → rate conformity → drive corrective action through the hierarchy of
  controls → report. The method is jurisdiction-independent and never changes.
- **Criteria** = *what the audit is conducted against*. Chosen at intake (Q-Crit):
  ISO 45001 itself, a regulatory regime, or a custom checklist. The chosen
  criteria become the clause/checklist set the Workflow walks finding-by-finding.

The same 9.2 loop audits a site against ISO 45001, against the Factories Act,
or against a client's own checklist — only the criteria set changes.

## 2. Establishing the criteria set (step 2)

Resolve Q-Crit into a concrete, walkable list:

- **ISO 45001** → the relevant management-system clauses become the criteria
  (e.g. 6.1.2 hazard ID, 7.2 competence, 8.1 operational control, 9.1
  monitoring). These are distinct from 9.2 (the *method*).
- **A regulatory regime** → the applicable duties from the matched jurisdiction
  fragment (UK HSWA, US OSHA, EU OSH, India Factories Act + the resolved state).
  India: resolve the **state** (Q-Juris-a) before citing any form — mandatory
  state detection; never a national form number.
- **A custom checklist** → the user-supplied items, verbatim. A private checklist
  has no KB fragment, so the audit cites **no external clause** beyond the user's
  own items. The citation grader does not fire on this path.

Record `[GAP]` where the criteria set is incomplete. **Never invent a clause.**

## 3. Evidence assessment & sufficiency (step 3)

For each criterion, assess the available evidence **against that specific clause**:

- **What it shows** — the objective fact the evidence establishes.
- **Sufficiency** — is the evidence enough to judge conformity? A single document
  may show intent but not implementation; observation + records + interview by
  role together give a defensible picture.
- **What is missing** — name the gap explicitly.

**Sampling.** An audit is a point-in-time sample, not a census. State the sample
(e.g. "a sample of 12 issued permits across 3 shifts"); a finding generalises
from the sample with that caveat. Each assessment names its specific evidence
item (document id, observation, interview-role, record).

**Insufficient-evidence rule.** A criterion with absent evidence is recorded as a
**nonconformity or "insufficient evidence" — never a silent conformity.** This is
the defensibility core: you cannot assert conformity you did not evidence.

## 4. The 4-class finding classification (step 4, D-05)

Exactly one finding per criterion, classified with the conventional ISO-audit
scheme:

| Class | When | Risk-rated? |
|---|---|---|
| **Conformity** | Evidence demonstrates the requirement is met. | No |
| **Nonconformity — Major** | A systemic failure or total absence of a required arrangement (the system does not meet the criterion). | **Yes** |
| **Nonconformity — Minor** | An isolated lapse against an otherwise-conforming arrangement. | **Yes** |
| **Observation** | Conforming now, but a risk of drift / an early warning. | No (optional) |
| **Opportunity for improvement** | Conforming, but a better practice is available. | No |

Every finding names the **clause/checklist item, the objective evidence, and the
classification**. A finding with no evidence trail is a defect the Critic/QA pass
must catch.

**Risk-rating nonconformities (D-04 — default ON).** Every nonconformity (major
and minor) is risk-rated via `risk_matrix.load_matrix(config)` then
`risk_matrix.score(likelihood, severity, matrix)` (config from Q-NCrate, default
`DEFAULT_5X5`). The band (Low / Medium / High / Critical) is the engine's, not
prose — it lets the conformity summary prioritise which findings to close first.
Conformities and observations carry no score.

### Findings-register block form (the report layout knob)

In `assets/audit-report.template.json` the clause-by-clause findings render **by
default** as A4 `findings` risk-rated cards (richer — evidence per finding),
where `risk_level` is the `risk_matrix` band for a nonconformity and blank for a
conformity/observation/opportunity. For a **long criteria set (>~15 clauses)**,
swap that `findings` block for a `table` with a `risk_column` for density:
`{ "type": "table", "headers": ["Clause / item", "Classification", "Evidence",
"Risk band"], "rows": [ … one row per criterion … ] }` — the engine colours the
band cell off `palette.risk` (keep the Low/Medium/High/Critical band vocabulary
so the colours resolve). Both are A4-native; this is a presentation knob, not a
contract change.

## 5. Conformity rating (step 5)

Summarise from the per-finding ratings (not asserted in prose):

- Conformity % of assessed criteria.
- Count by class (conformity / NC-major / NC-minor / observation / opportunity).
- Highest residual nonconformity risk band.

## 6. Corrective actions + the CAPA register (step 6 — the B6→B7 seam)

For **every nonconformity** (and any actioned observation):

1. Apply `KB-SNIP-HOC`: rank Elimination → Substitution → Engineering →
   Administrative → PPE. Eliminate/substitute the root of the nonconformity
   before mitigating it.
2. Call `controls.rank_controls(controls)` + `controls.validate_treatment(controls)`.
   If `ppe_admin_only` is `True`, **add a higher-order control or record an
   explicit "higher-order controls not reasonably practicable because…"
   justification.** An un-justified lower-order-only treatment is a defect.
3. Make each action SMART — named (role-label) owner + ISO due date + a measure
   — and link it to its **finding id**.
4. Assemble the CAPA register and call `smart_actions.validate_register(actions)`.

**The CAPA register uses B5's schema verbatim** — each entry is
`{action, owner, due, measure, links_to_cause, hoc_tier}`, where
`links_to_cause` carries the **finding id** (the audit analogue of B5's RCA
cause id). Any action missing an owner, a valid date, a measure, or a finding
link is **invalid** and must be fixed — no anonymous actions, no "ASAP".

This validated register is the **producer side of the B6→B7 seam**:
`capa-manager` (B7) ingests this exact shape and runs the lifecycle (status,
overdue detection, effectiveness, closure) over it. B6 *creates and validates*;
B7 *tracks and closes*. Both call the one `smart_actions` engine, at different
points in the action's life — no duplicated logic, no schema fork.

## 7. Grounding

- `KB-STD-ISO45001` clause **9.2** (method, always), **8.1.2** (hierarchy of
  controls, for corrective actions), **10.2** (nonconformity & corrective action,
  the finding→CAPA loop). When Q-Crit = ISO 45001, the audited clauses become the
  criteria set.
- `KB-SNIP-HOC` — applied to every corrective action.
- `KB-SNIP-INTAKE` — the intake pattern.
- `KB-SNIP-ARCHETYPES` — the roster source.
- `KB-REG-IN-STATEFORMS` — India state-form resolution (mandatory state detection).
