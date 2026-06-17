<!-- KB-STD-API-RP-754 -->
# API RP 754 — Process Safety Performance Indicators

**Fragment ID:** `KB-STD-API-RP-754`
**What this is:** a copyright-safe **tier → indicator-definition → counting-rule
map** for the API RP 754 process-safety performance-indicator pyramid — the tier
*structure*, the Tier-1/Tier-2 Process Safety Event (PSE) counting logic, and the
leading/lagging framing.
**What this is NOT:** a reproduction of the standard's normative text. API RP 754
is copyrighted; the user holds their own licensed copy. Cite the tier numbers and
indicator topics only — never paste the recommended-practice wording.

> Source: API RP 754 (2nd ed.) — indicator-tier structure (recommended practice; user holds the standard) · Year: 2021 · Reviewed: 2026-05-15 · Volatile: false (multi-year revision cycle; the per-year benchmark figures live in KB-DATA-* and are volatile).

The process-safety indicator pyramid separates **lagging** loss-of-containment
outcomes (Tier-1/Tier-2) from **leading** operating-discipline measures
(Tier-3/Tier-4). It grounds `process-safety-kpi`.

## Tier → indicator topic → use

| Tier | Indicator topic | Lagging / leading | Grounds |
|---|---|---|---|
| Tier 1 | Greatest-consequence loss of primary containment (LOPC) — above threshold | lagging | process-safety-kpi (Tier-1 PSE count + normalized rate) |
| Tier 2 | Lesser-consequence LOPC — above a lower threshold | lagging | process-safety-kpi (Tier-2 PSE count + rate) |
| Tier 3 | Challenges to safety systems (demands on IPLs, excursions) | leading | process-safety-kpi (leading indicator) |
| Tier 4 | Operating-discipline / management-system performance (e.g. PM completion) | leading | process-safety-kpi (leading indicator) |

## Counting + normalization discipline
- A Tier-1/Tier-2 PSE is counted by **threshold test** (material released, acute
  consequence) — the skill *structures* the count from the user's event facts; it
  does not invent events.
- Normalized rate = `count × base hours ÷ total work hours` (the same fail-loud
  denominator discipline as A7 `incident_rates`: a missing/zero hours denominator
  is `[GAP]`, never a fabricated figure).
- Benchmark comparison reads `KB-DATA-PSE-BENCHMARKS` (each figure `source`+`year`).

## How skills use this fragment
- `process-safety-kpi` grounds Tier-1/Tier-2 PSE counting + rate normalization and
  frames Tier-3/Tier-4 leading indicators; it is distinct from the occupational
  TRIR/LTIFR/DART family (incident-rate-calculator) — different metric family.
