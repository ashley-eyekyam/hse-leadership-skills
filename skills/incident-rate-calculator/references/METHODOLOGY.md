# Methodology — Incident Rate Calculator (B10)

The domain method this skill applies. The single discipline that makes B10 defensible:
**the maths lives only in the tested `incident_rates` engine — the model never computes,
estimates, or rounds a rate in prose.** A lagging rate is only defensible if anyone can
re-run the same inputs through the same code and reproduce the number to the dp.

## 1. The rates and their fixed denominators

All three rates are *frequency-per-standard-exposure* figures. The base is a **locked
engine constant** (`OSHA_BASE`, `MILLION_BASE`) — never configuration, never user-arithmetic.

| Rate | Definition | Formula | Base |
|---|---|---|---|
| **TRIR** | Total Recordable Incident Rate | recordables × 200,000 ÷ hours worked | 200,000 |
| **DART** | Days-Away / Restricted / Transfer rate | DART cases × 200,000 ÷ hours worked | 200,000 |
| **LTIFR** | Lost-Time Injury Frequency Rate | lost-time injuries × 1,000,000 ÷ hours worked | 1,000,000 |

The **200,000** base = 100 full-time workers × 40 h × 50 weeks (the OSHA convention for
TRIR/DART). The **1,000,000** base is the LTIFR convention. Both are module constants in
`scripts/hse_components/incident_rates.py` (D5 — not config). Rates round to **2 dp** at the
engine boundary.

### Worked anchor (locked, the eval asserts it)

```
incident_rates.trir(3, 290_000) == 2.07      # 3 recordables / 290,000 hours, base 200,000
incident_rates.ltifr(6, 1_000_000) == 6.00   # 6 lost-time injuries / 1,000,000 hours
```

`3 × 200,000 ÷ 290,000 = 2.0689… → 2.07`. The model presents `2.07` **because the engine
returned it** — it does not perform this division itself.

## 2. The no-LLM-arithmetic discipline (the whole value)

- **Call, do not compute.** Use `incident_rates.compute_all(counts, hours_worked, period)`
  for all three at once, or the individual `trir` / `dart` / `ltifr` functions. Present the
  returned dict **verbatim**.
- **No sanity-recompute.** Do not "check the engine's answer" with your own division — that
  reintroduces a non-reproducible figure and defeats the point.
- **No rounding or reformatting of the number.** The engine already rounds to 2 dp; present
  that value as-is.
- **No Python sandbox → refuse.** If the host cannot run the engine, state that the
  deterministic calculator is unavailable and that the figure must be produced by running
  `incident_rates`. Do **not** fabricate a rate in prose.

## 3. The denominator must be real (fail-loud edges)

- **Hours worked is mandatory.** It is the denominator; there is no rate without it. The
  intake refuses to proceed if it is blank.
- **Zero / negative hours → honest `ValueError`.** The engine raises
  `ValueError("hours_worked must be > 0")`; surface that honestly and ask for the real
  figure. **Never emit a fake `0.0`** — a 0.0 rate reads as "perfect safety" and is a lie.
- **No implicit annualization.** The caller passes the *actual* hours-to-date and the period
  label. A partial-period figure is reported as period-actual (the engine records this in
  `notes`); the period is **never** used as a scaling factor.
- **Counts are non-negative integers.** A negative or non-integer count is a `ValueError`
  from the engine, surfaced honestly — never silently coerced into a plausible-looking number.

## 4. Benchmarking (optional, sourced only)

If the user supplies an industry benchmark, it must carry its **publishing body + year +
sector** (per A3's KB discipline). Call `incident_rates.benchmark_delta(rate, industry_rate)`
to get the signed delta and direction (a lower rate is better → `better_than_industry` is
true when `rate < industry_rate`). A **bare** comparator with no source is recorded `[GAP]`,
never used. The benchmark figures themselves come from `KB-DATA-TRIR-BENCHMARKS`, quoted with
source + year.

## 5. Severity rate — deferred `[GAP]` (D-03)

A severity rate (days lost per standard exposure) is **out of scope for v1.0**: the shared
engine deliberately has **no** `severity_rate()`. If the user asks for it, mark it
`[GAP] — severity rate not computed (no validated engine in v1.0)` and **never** compute it
in-prompt. (Confirmed: `incident_rates.__all__` exposes only `trir`, `dart`, `ltifr`,
`compute_all`, `benchmark_delta`, `OSHA_BASE`, `MILLION_BASE`.)

## 6. De-identification (runs first)

If the user pastes a case log, the `deid` block scrubs it to **aggregate counts only** before
any computation: no per-case line, no individual identifier, and no injury/illness sub-group
with fewer than 5 individuals (small-cell suppression, with secondary suppression so a
suppressed cell cannot be back-calculated from a total). Only the aggregate counts reach the
engine. A per-case line or a <5 cell in the output is a de-identification hard-fail.
