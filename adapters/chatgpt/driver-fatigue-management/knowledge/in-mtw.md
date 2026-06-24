<!-- KB-REG-IN-MTW -->
# India — Motor Transport Workers Act 1961 + warehouse statutory framing (deferral pointer)

**Fragment ID:** `KB-REG-IN-MTW`
**What this is:** an India **deferral pointer** (CONV-8) for logistics/transport and
warehouse work — the Motor Transport Workers Act 1961 (hours/rest of transport
workers), the Factories Act where a warehouse is a "factory", and the flagged OSH
Code 2020 transition. It routes all statutory form/return content to the
`hse-india` engine after mandatory state detection.
**What this is NOT:** a national form-number lookup. **No national form number is
minted here** — unverified form content stays `[GAP]` and is resolved via
`hse-india` / `KB-REG-IN-STATEFORMS` after state detection.

> Source: Motor Transport Workers Act 1961 + Factories Act 1948 (warehouse-as-factory framing) + OSH Code 2020 transition note (deferral pointer; per-state cite via hse-india) · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true.

For India logistics/transport and warehousing, the federal framing is the Motor
Transport Workers Act 1961 (working hours, rest intervals, welfare of motor
transport workers) and — where a warehouse meets the threshold — the Factories
Act 1948. The OSH Code 2020 consolidates these and is **flagged as a transition**;
the legacy instrument the user files today governs until it commences for them.

## India deferral routing (CONV-8 — three-tier graceful degradation)

1. **State detection is mandatory** before citing any form, return or due date.
2. The skill **defers to the `hse-india` engine** for the state-specific form,
   rule, due date and portal — via a subagent where supported, else a main-thread
   inline read of the `hse-india` KB/engine, else a routing pointer + `[GAP]`.
3. **No national form number is asserted.** Any unverified form/return/register is
   `[GAP]` until `hse-india` resolves it for the detected state.

## How the skill uses this fragment
- LOG-01 / LOG-02 cite the Motor Transport Workers Act 1961 (and Factories Act for
  warehouse-as-factory) as the framing, then route to `hse-india` for any
  state-specific statutory artifact after state detection.
- The OSH Code 2020 transition is flagged, not assumed commenced.
- Driver-hours *compliance* is computed by the SUB-03 `fatigue.py` engine against
  FMCSA / EU 561 (`KB-REG-FMCSA-HOS`), not from this fragment; India statutory
  rest provisions are routed to `hse-india`.
