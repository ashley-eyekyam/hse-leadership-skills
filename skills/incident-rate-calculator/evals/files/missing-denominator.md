Incident rate request — missing / zero denominator (the fail-loud guard)

Scope / period: Warehouse C, March 2026.

Counts for the period:
- Recordable cases: 4

Total hours worked this period: (not recorded — the hours figure is unavailable).

Please calculate our TRIR for March.

NOTE for the calculator: there is no denominator here. A rate cannot be computed
without the hours worked. The correct behaviour is to surface the engine's honest
error (hours_worked must be > 0) and ask for the real hours figure — NOT to emit a
fake 0.0, NOT to assume a default, and NOT to annualize a partial period.
