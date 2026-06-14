# HIRA Methodology (placeholder)

> **Phase-1 placeholder.** The full Hazard Identification & Risk Assessment method
> — calibrated risk matrix, hierarchy-of-controls walk, ALARP justification, and
> the jurisdiction-resolved control catalog — is authored by **A3 / A5 / A6** in
> Phase 2 (via `hse-skill-forge --sync`). This file exists so the contract's
> folder layout (A2 §3.4) and the SKILL.md reference links (linter rule 8) resolve
> on disk from Phase 1.

## Method outline (to be expanded)

1. **Hazard identification** for the named task/site/asset — task-specific, not a
   generic checklist alone.
2. **Initial risk scoring** — likelihood × severity on the calibrated risk matrix
   (the `risk_matrix` deterministic component, A4).
3. **Control selection** — walk the full hierarchy of controls per hazard:
   eliminate → substitute → engineer → administrate → PPE. A PPE-only treatment is
   rejected by the quality gate.
4. **Residual risk scoring** — re-score after controls; justify **ALARP**.
5. **Action assignment** — every action carries a named owner and a review date.
