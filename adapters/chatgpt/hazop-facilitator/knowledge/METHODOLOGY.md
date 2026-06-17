# HAZOP facilitation method (IEC 61882) — `hazop-facilitator`

The method map is `KB-STD-IEC-61882`. This skill is **assistive**: it structures the study and records the live team's findings; it never performs the study autonomously.

## Steps
1. **Bound the node.** One named P&ID section / node at a time. Capture the design intent (normal flow/pressure/temperature/level/composition).
2. **Build the matrix.** Guidewords (No, More, Less, Reverse, As-well-as, Part-of, Other-than) × parameters (flow, pressure, temperature, level, composition).
3. **Record the team's findings** for each meaningful cell: Deviation → Cause → Consequence → Existing safeguards → Recommendation. The team supplies these; the skill records them. Unaddressed → `[GAP]`.
4. **Risk-rank** each line with `risk_matrix.score` (process-safety consequence descriptors).
5. **HoC-rank** safeguards with `controls.rank_controls`; flag any administrative/PPE-only safeguard set (`controls.ppe_admin_only`) without a higher-order barrier.
6. **Track recommendations to closure** with `smart_actions.validate_register` (owner + ISO due date + measure + node link).

## Assistive discipline (load-bearing)
- Never invent a deviation the team did not raise.
- Never assign a consequence severity the team did not judge — record `[GAP]`.
- The report names the **team participants & competencies** and carries the assistive disclaimer: the AI structured and recorded the workshop; the analysis was performed by the named competent team and must be reviewed by a competent person.
