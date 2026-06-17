# Methodology — reactive-chemistry & combustible-dust / explosive-atmosphere assessment

## Method
1. **De-identify first** — any worker PII → role labels.
2. **Resolve material + hazard scope** from the intake; branch DSEAR vs NFPA 652/660 vs ATEX.
3. **Dust Hazard Analysis** (`KB-STD-NFPA-652`/`660`): materials inventory, process/equipment review,
   credible fire/deflagration/explosion scenarios, safeguards, management systems. Resolve
   **Kst/Pmax/MIE/MIT with a lab source+year, or `[GAP]`** — never an invented dust figure.
4. **Basis of safety** (`KB-STD-DSEAR`): avoid the explosive atmosphere OR avoid ignition OR
   mitigate — stated explicitly, justified, HoC-ranked (`controls`).
5. **Area classification** (`KB-STD-ATEX`): justify the zone (0/1/2 or 20/21/22) + EPL from release
   grade + ventilation — **never defaulted** (an unjustified zone is a SME FLAG).
6. **Hand off the structured study** — the reactive/deflagration nodes go to the
   **`hazop-facilitator`** (HAZOP/DHA, grounded in `KB-STD-IEC-61882`); this skill frames the nodes,
   it does not run the workshop or invent safeguards.
7. **Consequence band** via `risk_matrix`; **actions** via `smart_actions` (owner + ISO date).

## Output discipline
- No fabricated dust parameter; `[GAP]` is honest. The zone is justified, not defaulted.
