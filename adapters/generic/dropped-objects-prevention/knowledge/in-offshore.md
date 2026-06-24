<!-- KB-REG-IN-OFFSHORE -->
# India — offshore operations (OISD + PNG Safety Rules) deferral pointer

**Fragment ID:** `KB-REG-IN-OFFSHORE`
**What this is:** an India **deferral pointer** (CONV-8) for offshore/marine work —
the OISD (Oil Industry Safety Directorate) standards and the Petroleum and Natural
Gas (Safety in Offshore Operations) Rules. It routes statutory references to the
`hse-india` engine after mandatory state detection (for shore-base activity).
**What this is NOT:** a national form-number lookup. **No national form number is
minted here** — unverified statutory content stays `[GAP]` and resolves via
`hse-india`.

> Source: OISD standards + Petroleum and Natural Gas (Safety in Offshore Operations) Rules (deferral pointer; per-state shore-base cite via hse-india) · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true.

For India offshore operations the framing is OISD standards plus the PNG (Safety in
Offshore Operations) Rules. The safety-case-style assistive output (MAR-01) and
the marine emergency-response output cite these as the Indian framing and defer
state-specific shore-base statutory content to the `hse-india` engine.

## India deferral routing (CONV-8 — three-tier graceful degradation)

1. **State detection is mandatory** for any shore-base / onshore-supporting
   statutory obligation before citing a form or due date.
2. The skill **defers to the `hse-india` engine** for state-specific content — via
   subagent, else main-thread inline read, else routing pointer + `[GAP]`.
3. **No national form number is asserted.** Any unverified statutory reference is
   `[GAP]` until `hse-india` resolves it.

## How the skill uses this fragment
- MAR-01 / MAR-03 cite OISD + the PNG offshore rules as the Indian framing, then
  route any state-specific shore-base statutory artifact to `hse-india` after state
  detection; no national form is minted.
