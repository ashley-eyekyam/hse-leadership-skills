# Pre-output Quality Checklist — Incident Rate Calculator (B10)

Validate every draft against this gate before producing the report. B10's defensibility
rests on one thing above all: **the number came from the engine, not from the model.**

## The no-arithmetic gate (load-bearing)

- [ ] Every rate shown was produced by a call to `incident_rates` (`compute_all` / `trir` /
      `dart` / `ltifr`) — **no rate was computed, estimated, or rounded by the model in prose.**
- [ ] No "sanity-recompute" of the engine's answer appears anywhere in the output.
- [ ] The base shown is the engine constant (200,000 for TRIR/DART, 1,000,000 for LTIFR) — not
      a user-supplied or model-derived number.

## The real-denominator gate

- [ ] Hours worked is present and `> 0`; the intake refused to proceed without it.
- [ ] A zero / missing / negative denominator was surfaced as the engine's honest `ValueError`
      — **never a fake `0.0`.**
- [ ] No implicit annualization: the figure is period-actual; the period is a label, not a
      scaling factor.
- [ ] Counts are non-negative integers; no count was silently coerced or guessed.

## The transparency-trail gate

- [ ] Each rate is presented **with** its formula, inputs, base, and period — a reviewer can
      re-run the same inputs and reproduce the number.
- [ ] Any benchmark comparison carries its source + year; a bare comparator is flagged `[GAP]`.
- [ ] Severity rate (if asked) is marked `[GAP]` — not computed in-prompt (D-03).

## The de-identification gate (hard-fail)

- [ ] The de-identification pass ran BEFORE computation; any pasted case log was reduced to
      aggregate counts only.
- [ ] No per-case line, no individual identifier, and no injury/illness sub-group with fewer
      than 5 individuals (small-cell suppression applied; no re-identification key embedded).
