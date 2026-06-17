# PSM program management — `psm-program-manager`

Grounds in `KB-STD-PSM` (the 14-element framework) + `KB-REG-US-OSHA` (the US statute).

## Steps
1. **Bound the facility** and the covered process(es).
2. **Assess each element** (or the in-scope subset): status compliant / gap / overdue, with evidence.
3. **Gap-risk band** each gap with `risk_matrix.score`.
4. **Remediation** — HoC-rank the remediation controls (`controls`); a gap without a higher-order control is flagged.
5. **Track** the remediation plan with `smart_actions.validate_register` (owner + ISO due date + measure + element link).
6. **Status matrix** — one row per element: element · status · evidence · gap-risk band · owner.

## Discipline
- Status is evidence-based, never asserted; a gap with no evidence is `[GAP]`.
- A US user cites both KB-STD-PSM (framework) and KB-REG-US-OSHA (statute) — keep aligned.
