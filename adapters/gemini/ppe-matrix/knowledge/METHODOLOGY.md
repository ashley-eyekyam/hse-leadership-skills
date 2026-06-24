# Methodology — ppe-matrix (the controls-first gate, then residual-only PPE)

The domain method `ppe-matrix` applies. Its spine is the **controls-first gate**
(`KB-SNIP-PPE-MATRIX-LOGIC` + `KB-SNIP-HOC`): PPE is the **residual-only, last line** after
the higher-order controls — never the headline control. Every PPE row is task-specific, cites
its EN/ANSI conformity standard + year, and the run always emits the **OSHA 1910.132(d)(2)
written hazard-assessment certification**. The controls-first gate is a **deterministic
`controls`-engine check**, never a narrated judgment.

## 0. De-identify first (special-category respiratory medical-clearance / fitness data)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Respiratory
medical-clearance / fitness-for-respirator results are **GDPR Art. 9 / India DPDP
special-category health data**: reduce every named worker to a role label, report any health
breakdown by role with `<5` small-cell suppression, and **never circulate a named clearance /
fitness note**. The De-identifier subagent runs FIRST; everything downstream consumes only its
scrubbed output.

## 1. Capture the named scope and the body-region hazards (Q1 → Q2)

- **Scope (Q1)** — the exact area / line / role set + the tasks performed. **Refuse a generic
  or site-wide PPE sheet** ("PPE for the whole plant"); the matrix is task-specific (the
  specificity anchor). A missing scope is a `[GAP]`, never an invented task.
- **Body-region hazards (Q2)** — per OSHA 29 CFR 1910 Subpart I, by region: eye/face (.133) ·
  head (.135) · hearing · respiratory · hand/arm (.138) · foot/leg (.136) · body/torso —
  selected per task in scope and grounded on `KB-REG-OSHA1910-I` + the manufacturing clause
  cross-walk `KB-SNIP-MANUFACTURING-CLAUSE-MAP`.

## 2. Run the controls-first gate, per hazard (Q3 — the spine, deterministic)

For **each** body-region hazard, capture the higher-order controls in place or justified
(elimination / substitution / engineering / administrative), then call the engine:

```python
from controls import rank_controls, validate_treatment   # via scripts/hse_components symlink
verdict = validate_treatment(controls_for_this_hazard)    # {passed, ppe_admin_only, highest_order, flag, ranked}
```

- If higher-order controls are applied/justified and a **residual** hazard survives → proceed
  to PPE selection (step 3) for that residual hazard only.
- If the treatment is **PPE/administrative only** (`ppe_admin_only=True`) **or no higher-order
  control is recorded at all** → this is a **controls-first FLAG**. **Emit the flag, NOT a PPE
  row.** The matrix records "controls-first: higher-order controls not considered / not
  justified — assess and apply before specifying PPE", and the PPE cell is withheld. **Never
  invent a PPE row to fill the gate.**

This is the failure mode the skill exists to prevent: PPE specified for a hazard whose
higher-order controls were never considered.

## 3. Select the residual-only PPE + cite the conformity standard

For each residual hazard that survived the gate, select the PPE **type** and **cite the EN/ANSI
conformity standard + year** from `KB-DATA-PPE-STANDARDS` (reused, never re-authored). Present
each row as: `<PPE type> against <named residual hazard>, conforming to <standard>, <year>`
(e.g. "safety glasses against grinding-spark eye hazard, conforming to EN 166 / ANSI Z87.1,
[year]"). **Never assert a protection level without the cited standard + year** — that is a
`regulatory_citation_accuracy` hard-fail. For respiratory PPE, the fit/clearance need (Q4)
drives a fit-test / medical-clearance action, recorded at role level.

## 4. Emit the written hazard-assessment certification (1910.132(d)(2) — mandatory)

Produce the certification block grounded on `KB-REG-OSHA1910-I`: the **workplace assessed**,
the **certifier** (named role), and the **date**. **The certification is always produced —
omitting it is a `regulatory_citation_accuracy` hard-fail.** A missing required input is a
`[GAP]`, never a fabricated certifier or date.

## 5. SMART actions + report

Every PPE-gap, fit-test, and controls-first action becomes a SMART action (named role owner +
ISO due date + measure), validated by `smart_actions.validate_register`. Validate the draft
against `references/QUALITY_CHECKLIST.md`, then assemble `assets/ppe-matrix.report.json` and run
the canonical `report-output` call.

## Jurisdiction

US OSHA 1910.132 + ANSI is the default; UK/EU is PPE at Work Regs 1992 (amended 2022) + EN.
For India, resolve the state via `hse-india` (**mandatory state detection**) and emit a literal
`[GAP]` where a state form/return is owed — **never a minted national form number**.
