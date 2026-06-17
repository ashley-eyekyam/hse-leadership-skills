# HAZID facilitation method — `hazid-facilitator`

Assistive: structures the broad early-stage sweep and records the live team's findings; never autonomous.

## Steps
1. **Bound the scope.** One named installation / project phase.
2. **Sweep the categories.** Process, mechanical, electrical, external/natural (flood, seismic, wind), environmental (land/water/air release), utilities loss, neighbouring-installation knock-on.
3. **Record the team's findings** per category: Hazard → Cause → Consequence → Existing controls → Recommendation. Team supplies; skill records. Unaddressed → `[GAP]`.
4. **Risk-rank** with `risk_matrix.score` (process-safety descriptors).
5. **HoC-rank** controls with `controls.rank_controls`; flag administrative/PPE-only sets.
6. **Track recommendations to closure** with `smart_actions.validate_register`.

## Assistive discipline (load-bearing)
- Never invent a hazard the team did not raise; record `[GAP]` for unaddressed categories.
- Name the **team participants & competencies**; carry the assistive disclaimer.
