<!-- KB-REG-IN-RENEWABLES -->
# India — renewables / electrical (CEA regulations + state rules) deferral pointer

**Fragment ID:** `KB-REG-IN-RENEWABLES`
**What this is:** an India **deferral pointer** (CONV-8) for renewables / wind /
solar work — CEA (Central Electricity Authority) regulations, state electricity
rules and factory/establishment registration. It routes statutory references to the
`hse-india` engine after mandatory state detection.
**What this is NOT:** a national form-number lookup. **No national form number is
minted here** — unverified statutory content stays `[GAP]` and resolves via
`hse-india`.

> Source: CEA (Central Electricity Authority) regulations + state electricity rules + factory/establishment registration (deferral pointer; per-state cite via hse-india) · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true.

For India renewables the framing is the CEA regulations (electrical safety) plus
state electricity rules and factory/establishment registration. A wind WAH /
lone-working / weather artifact cites this as the Indian framing and defers
state-specific statutory content to the `hse-india` engine.

## India deferral routing (CONV-8 — three-tier graceful degradation)

1. **State detection is mandatory** before citing any form, return or due date.
2. The skill **defers to the `hse-india` engine** for state-specific content — via
   subagent, else main-thread inline read, else routing pointer + `[GAP]`.
3. **No national form number is asserted.** Any unverified statutory reference is
   `[GAP]` until `hse-india` resolves it.

## How the skill uses this fragment
- REN-01 / REN-02 / REN-03 cite the CEA regulations + state electricity rules as the
  Indian framing, then route any state-specific statutory artifact to `hse-india`
  after state detection; no national form is minted.
