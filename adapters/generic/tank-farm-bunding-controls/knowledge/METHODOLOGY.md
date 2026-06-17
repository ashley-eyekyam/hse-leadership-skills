# Methodology — tank-farm / bulk-storage / bunding controls

## Method
1. **De-identify first** — any PII → role labels.
2. **Resolve storage facts** from the intake: substances + volumes + configuration + existing
   containment. Note incompatibilities (segregation driver).
3. **Containment sizing basis** — state the basis explicitly (e.g. the largest-tank + freeboard rule,
   or the applicable local/PESO rule) — **resolved from the rule, never an assumed percentage**.
4. **Controls** — secondary containment, segregation, overfill protection (independent high-level
   trip), drainage/firewater containment — HoC-ranked with `controls`; flag any admin-only control.
5. **Flammable atmosphere** — DSEAR area control (`KB-STD-DSEAR`) for flammable bulk storage.
6. **India** — storage/petroleum licensing pointers from `KB-REG-IN-PESO` (referenced); **resolve the
   state** (mandatory) for state interactions via `KB-REG-IN-STATEFORMS`.
7. **Consequence band** via `risk_matrix`; **actions** via `smart_actions` (owner + ISO date).

## Output discipline
- The containment basis is traced to the rule, never an unstated assumption; `[GAP]` where the local
  rule is unresolved, routed to a competent person.
