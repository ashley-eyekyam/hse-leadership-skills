# Methodology — Occupational-health risk assessment (SEG → OEL → ergonomics → controls → surveillance)

This is the domain method `health-risk-assessment` applies. The SKILL.md Workflow is the
operational summary; this file is the full reference. The method snippet is
`KB-SNIP-SURVEILLANCE-TRIGGERS`. Every conclusion is traced to a cited source (OEL with
authority+year; ergonomic score from the engine), every control is ranked through the
hierarchy of controls, and every action carries a named owner and a date — never a vague,
PPE-only, or surveillance-only treatment.

## 0. De-identify first — special-category health data

Exposure-monitoring and **health-surveillance results (audiometry, lung function, biological
monitoring, HAV scores) are GDPR Art. 9 / India DPDP special-category health data**. Before
any drafting (the `deid` block + `references/deid-checklist.md`): scrub names to stable role
labels, **report by SEG/role not by individual**, apply `<5` small-cell suppression to any
health-outcome breakdown, and **never circulate a surveillance result with a name**. The
re-identification key is held separately, never embedded.

## 1. Define the similar-exposure groups (SEGs)

From the Q2 named tasks/roles, group workers with materially the same exposure (same agent,
same task, same controls) into SEGs. The SEG is the **unit of assessment and of
surveillance**. Refuse a generic SEG ("all staff"); each SEG names the task/role and the
agent. Where the basis is uncertain, flag `[GAP]` — never invent a SEG.

## 2. Characterise exposure & compare to a cited OEL

For each SEG/agent, state the measured or estimated exposure (Q3) and compare it to the
**binding OEL/WEL/PEL** resolved **with source+year** from `KB-DATA-OEL-LIMITS` /
`KB-DATA-EXPOSURE-LIMITS` (the single OEL source — **no parallel OEL table**; two disagreeing
OEL sources are a defensibility risk). Express each row as `<agent> <exposure> vs <OEL> <unit>
<TWA/STEL> — <authority>, <year>` and state whether exposure is below / at-action-level /
above the limit. An exposure assessed with **no cited OEL** fails (specificity ·
regulatory_citation_accuracy). If Q3 is *none-yet*, **do not fabricate a comparison** —
recommend a monitoring strategy first and stop.

> India lacks a single consolidated statutory OEL list; for India sites cite the referenced
> UK WEL / OSHA PEL / ACGIH TLV anchor (with source+year) and flag it as a referenced — not
> India-statutory — value. India defers to `hse-india`; resolve the state first.

## 3. Score ergonomic risk with the engine (deterministic)

When the hazard is manual-handling/ergonomics, call the `ergonomics` engine via the
`scripts/hse_components` symlink for the Q5 tool — **the score is the engine's, never narrated
free-text** (grounded in `KB-STD-GHS-ERGO`):

```python
from hse_components import ergonomics
result = ergonomics.rula_score(upper_arm=3, lower_arm=2, wrist=2, wrist_twist=1,
                               neck=2, trunk=2, legs=1, muscle_use_a=1, force_a=0)
# or ergonomics.reba_score(...) / ergonomics.niosh_rwl(weight=, h=, v=, d=, ...)
blocks = ergonomics.to_report_blocks(result)   # -> exactly a [metrics, table] pair
```

`to_report_blocks(result)` returns the tool-named **`[metrics, table]`** pair (RULA grand
score + action level / REBA final score / NIOSH RWL + Lifting Index) that drops straight into
`report.json`'s "Ergonomic scores" section. Out-of-range inputs raise
`ErgonomicsInputError` — fix the input, never a silent clamp.

## 4. Rate residual health risk & rank controls up the hierarchy

Rate the residual health risk on `risk_matrix.score`. Apply `KB-SNIP-HOC` and call
`controls.rank_controls` + `controls.validate_treatment`: **substitution / engineering
precede PPE — and precede surveillance**. Surveillance is **monitoring, not a control**: a
noise plan offering only hearing protection (no engineering/substitution) is a defect the
Critic/QA pass must catch. If `ppe_admin_only` is `True`, add a higher-order control **or**
record an explicit "higher-order controls not reasonably practicable because…" justification.

## 5. Set the OEL-linked health-surveillance schedule

Following `KB-SNIP-SURVEILLANCE-TRIGGERS`: where exposure is **at/above the action level or
the OEL**, surveillance is required at the agent's cadence (noise ≥ action level → audiometry;
respiratory sensitisers → lung function; HAV → HAV surveillance); **below** the action level
set a monitoring / re-assessment cadence, surveillance not yet triggered. The schedule is
**keyed to the cited OEL comparison**, not asserted. Surveillance outcomes are reported by
SEG/role with `<5` suppression.

## 6. SMART actions (named owners + dates)

Every control and every surveillance action becomes a SMART action (named role owner + ISO
due date + measure + SEG link), validated by `smart_actions.validate_register`. No anonymous
or undated actions, no "ASAP".

## 7. Output / report assembly

Assemble one `report.json` (`hse-report-model/v1`) from
`assets/health-risk-assessment-report.template.json` and run the canonical `report-output`
call. Section order: Scope & SEGs → Hazards & exposure characterisation → Exposure-vs-OEL
comparison → **Ergonomic scores (tool-named — the engine `[metrics, table]` pair)** → Risk
rating → Controls (hierarchy) → Health-surveillance schedule → Review & sign-off.

## 8. Evidence & defensibility

Every SEG named; every exposure compared to a cited OEL (authority+year); every ergonomic
score the engine's; every control HoC-ranked above PPE and above surveillance; every action
owned + dated; every citation traced to the KB. The output is **decision-support**; a
competent person (occupational hygienist / OH physician) must review it.
