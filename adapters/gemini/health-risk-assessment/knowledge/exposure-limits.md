<!-- KB-DATA-EXPOSURE-LIMITS -->
# Occupational exposure limits (OELs) — where to resolve, with source+year

**Fragment ID:** `KB-DATA-EXPOSURE-LIMITS`
**Discipline:** exposure limits are jurisdiction-specific and revised periodically —
never quote a remembered value; resolve the binding limit from the cited authority for
the user's jurisdiction and present it with `source`+`year`.

> Volatile: true · last_reviewed: 2026-05-15 (review window 180 days, D-05).

---

## Limit types (stable concepts)

- **TWA** (Time-Weighted Average) — typically an 8-hour reference period.
- **STEL** (Short-Term Exposure Limit) — typically 15-minute reference period.
- **Ceiling** — must not be exceeded at any time.

*Source: standard OEL conventions (TWA/STEL/ceiling) · Year: 2026.*

## Where to resolve the binding limit (cite the jurisdiction's authority)

| Jurisdiction | Authority | Limit set | Source line to quote |
|---|---|---|---|
| US | OSHA | Permissible Exposure Limits (PELs), 29 CFR 1910.1000 | "OSHA PEL, 29 CFR 1910.1000, [year]" |
| US (recommended) | NIOSH | Recommended Exposure Limits (RELs) | "NIOSH REL, [year]" |
| US (consensus) | ACGIH | Threshold Limit Values (TLVs) | "ACGIH TLV, [year]" |
| UK | HSE | Workplace Exposure Limits (WELs), EH40 | "HSE EH40 WEL, [year]" |
| EU | EU-OSHA / Commission | Indicative & binding OELs (IOELVs/BOELVs) | "EU OEL Directive, [year]" |

**Always present a limit as:** `<substance> <value> <unit> <TWA/STEL/ceiling> — <authority>, <year>`.
Substance-specific values are resolved from the named authority at use time, not hard-coded here.

> Source: OSHA / NIOSH / ACGIH / UK HSE EH40 / EU OEL Directives (authorities named above) · Year: 2026 (framework); substance values resolved at use time.
