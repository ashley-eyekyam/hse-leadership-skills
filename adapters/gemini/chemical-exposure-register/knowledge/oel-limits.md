<!-- KB-DATA-OEL-LIMITS -->
# Chemicals — occupational exposure limits (OEL/WEL/PEL), each with source+year

**Fragment ID:** `KB-DATA-OEL-LIMITS`
**What this is:** the chemicals-pack **substance → exposure-limit map** that the
`chemical-exposure-register` skill reads to band exposure risk. Every value carries a
named **authority + year** (the KB-04 discipline) — a limit is never a bare number.
**What this is NOT:** a definitive or current OEL table. Exposure limits are
jurisdiction-specific and revised periodically; the **binding** value is resolved
from the cited authority for the user's jurisdiction at use time. The rows below are
**reference anchors with their source+year**, not a substitute for the authority. The
general resolution map (which authority to cite per jurisdiction) is
`exposure-limits.md` (`KB-DATA-EXPOSURE-LIMITS`); this fragment adds the
chemicals-substance anchors.

> Source: UK HSE EH40/2005 (WEL) · OSHA 29 CFR 1910.1000 (PEL) · ACGIH TLV — per-row authority+year below · Year: 2026 (framework; per-substance source+year on each row) · Reviewed: 2026-05-15 · Volatile: true (limits revised; resolve current value at use time).

Present every limit as: `<substance> <value> <unit> <TWA/STEL/Ceiling> — <authority>, <year>`.
Where a jurisdiction has **no statutory limit**, `[GAP]`-flag it and recommend the
**most protective** referenced value (with its source+year) — never invent a limit.
India lacks a single consolidated statutory OEL list (Factories Act 2nd Schedule +
state rules); for India sites, cite the referenced UK WEL / OSHA PEL / ACGIH TLV
anchor with source+year and flag that it is a referenced (not India-statutory) value.

## Reference anchors (each carries authority + year — resolve the binding value at use time)

| Substance (CAS) | Anchor limit (reference) | Type | Authority + year (the source line) |
|---|---|---|---|
| Toluene (108-88-3) | 50 ppm | TWA (8h) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Toluene (108-88-3) | 100 ppm | STEL (15 min) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Benzene (71-43-2) | 1 ppm | TWA (8h) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Benzene (71-43-2) | 1 ppm | TWA (8h) | "OSHA PEL, 29 CFR 1910.1028, 2020" |
| Ammonia (7664-41-7) | 25 ppm | TWA (8h) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Ammonia (7664-41-7) | 35 ppm | STEL (15 min) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Hydrogen sulfide (7783-06-4) | 5 ppm | TWA (8h) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Hydrogen sulfide (7783-06-4) | 10 ppm | STEL (15 min) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Respirable crystalline silica (14808-60-7) | 0.1 mg/m³ | TWA (8h) | "UK HSE EH40/2005 WEL, 2020 amendment" |
| Chlorine (7782-50-5) | 0.5 ppm | TWA (8h) | "ACGIH TLV-TWA, 2023" |
| Chlorine (7782-50-5) | 1 ppm | STEL (15 min) | "ACGIH TLV-STEL, 2023" |

*The anchors above are illustrative reference points for the exposure-register skill;
the binding limit for a named substance + jurisdiction is resolved from the cited
authority's current edition at use time, with its source+year carried into the
artifact.*

## How the skill uses this fragment
- `chemical-exposure-register` resolves each SEG/agent → the applicable OEL/WEL/PEL
  (with source+year) → exposure-risk band via `risk_matrix` → HoC control tier via
  `controls`; an unresolved or jurisdiction-absent limit is `[GAP]`-flagged with the
  most-protective referenced anchor, never a fabricated value.
