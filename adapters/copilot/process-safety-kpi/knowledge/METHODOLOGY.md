# Process-safety KPIs (API RP 754) — `process-safety-kpi`

Grounds in `KB-STD-API-RP-754`.

## Steps
1. **Bound** the facility & reporting period.
2. **Count PSEs** — apply the Tier-1/Tier-2 threshold test to the user's events (structured from facts, never invented).
3. **Normalize** — rate = count × base hours ÷ total work hours, using the fail-loud denominator discipline (missing/zero denominator → `[GAP]`, never a fabricated rate). The count is still reported when the denominator is absent.
4. **Leading indicators** — frame Tier-3 (challenges to safety systems) and Tier-4 (operating discipline).
5. **Benchmark** — compare against KB-DATA benchmarks where available (figures cited source+year).

## Discipline (load-bearing)
- Never fabricate a denominator or a rate — a missing denominator is `[GAP]`.
- Distinct from occupational TRIR/LTIFR/DART (route those to incident-rate-calculator).
