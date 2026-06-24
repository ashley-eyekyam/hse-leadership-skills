<!-- KB-REG-IN-RAIL -->
# India — rail safety (CRS / Railways Act 1989) deferral pointer

**Fragment ID:** `KB-REG-IN-RAIL`
**What this is:** an India **deferral pointer** (CONV-8) for rail work — the
Commissioner of Railway Safety (CRS) and the Railways Act 1989. It routes
statutory references to the `hse-india` engine after mandatory state detection (for
non-railway depot activity).
**What this is NOT:** a national form-number lookup. **No national form number is
minted here** — unverified statutory content stays `[GAP]` and resolves via
`hse-india`.

> Source: Commissioner of Railway Safety (CRS) + Railways Act 1989 (deferral pointer; per-state non-railway depot cite via hse-india) · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true.

For India rail the framing is the Railways Act 1989 and the Commissioner of Railway
Safety (CRS). A rail SMS / authorisation / level-crossing artifact cites this as the
Indian framing and defers state-specific statutory content (for non-railway depot /
supporting activity) to the `hse-india` engine.

## India deferral routing (CONV-8 — three-tier graceful degradation)

1. **State detection is mandatory** for any non-railway depot / supporting
   statutory obligation before citing a form or due date.
2. The skill **defers to the `hse-india` engine** for state-specific content — via
   subagent, else main-thread inline read, else routing pointer + `[GAP]`.
3. **No national form number is asserted.** Any unverified statutory reference is
   `[GAP]` until `hse-india` resolves it.

## How the skill uses this fragment
- RAIL-01 / RAIL-02 / RAIL-03 cite the Railways Act 1989 + CRS as the Indian
  framing, then route any state-specific non-railway statutory artifact to
  `hse-india` after state detection; no national form is minted.
