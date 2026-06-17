# LOPA method (IEC 61511) — `lopa-worksheet`

Assistive: structures one scenario and records the engineer-supplied values; **never computes a PFD or allocates a SIL**.

## Steps
1. **One scenario.** Name the consequence scenario.
2. **Initiating event** + engineer-supplied frequency.
3. **IPLs** — list each with its **independence test** result (independent of the IE and of other IPLs; not double-counted).
4. **PFD per IPL** — engineer-supplied; `[GAP]` if absent. The skill records, never computes.
5. **Residual gap** — band the residual risk with `risk_matrix` (tolerable vs not). This gap banding is the ONLY arithmetic; PFD multiplication is the engineer's verified input.
6. **SIL** — engineer-supplied target recorded, never allocated by the skill.
7. **HoC-rank** the IPLs (`controls`); **track** recommendations (`smart_actions`).

## Assistive discipline (load-bearing)
- NEVER compute a PFD or allocate a SIL — record `[GAP]` for unsupplied values.
- IPL independence is the team's judgement; the skill prompts the test, never declares independence itself.
- Name the competent engineer/team; carry the assistive disclaimer.
