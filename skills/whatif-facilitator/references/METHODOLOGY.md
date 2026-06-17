# What-If method — `whatif-facilitator`

Assistive: structures the systematic question set and records the team's answers; never autonomous.

## Steps
1. **Bound the scope.** One named process / operation / procedure.
2. **Seed the question set.** Systematic 'What if …?' prompts: loss of utility, wrong sequence, wrong material, human error, external event, equipment failure.
3. **Record the team's answers** per question: Hazard/consequence → Existing safeguards → Recommendation. Team supplies; skill records. Unaddressed → `[GAP]`.
4. **Risk-rank** with `risk_matrix.score` (process-safety descriptors).
5. **HoC-rank** safeguards with `controls.rank_controls`; flag administrative/PPE-only sets.
6. **Track recommendations** with `smart_actions.validate_register`.

## Assistive discipline (load-bearing)
- Never invent a consequence the team did not raise; record `[GAP]`.
- Name the **team participants & competencies**; carry the assistive disclaimer.
