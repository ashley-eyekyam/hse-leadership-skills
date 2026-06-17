# Mechanical integrity — `mechanical-integrity`

Grounds in `KB-STD-PSM` element (j).

## Steps
1. **Bound the equipment population / unit.**
2. **Criticality rank** each item with `risk_matrix.score` (consequence of failure × likelihood).
3. **ITPM schedule** — inspection/test/PM intervals + methods (RBI where used); integrity-operating-windows.
4. **Deficiency management** — open deficiencies, interim risk, remediation HoC-ranked (`controls`).
5. **Track** with `smart_actions` (owner + ISO due date + measure + equipment link).
6. **Register** — one row per item: equipment · criticality band · ITPM interval · deficiency status · owner.

## Discipline
- An item with no integrity basis is `[GAP]`, never assumed fit-for-service.
- A deficiency without a higher-order remediation control is flagged.
