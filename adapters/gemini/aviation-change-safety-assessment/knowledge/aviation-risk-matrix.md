<!-- KB-DATA-AVI-RISK-MATRIX -->
# Aviation 5×5 Risk Classification Scheme (ICAO Annex 19) — A7 MatrixConfig

**Fragment ID:** `KB-DATA-AVI-RISK-MATRIX`
**Discipline:** the ICAO Annex 19 **Risk Classification Scheme (RCS)** — the
severity × likelihood **5×5 safety-risk matrix** — shipped as a named A7
`MatrixConfig` (data, not code). The consuming skills load this config and pass it
to the **shared** `risk_matrix.score()` engine (`scripts/hse_components/risk_matrix.py`);
the engine is **never forked** — it is consequence-descriptor-agnostic, so aviation
supplies axis labels + acceptability bands, not new maths.

> Source: ICAO Annex 19 (2nd ed., 2016) + ICAO Doc 9859 Safety Management Manual (4th ed.) — the Safety Risk Assessment Matrix (severity / likelihood scheme); user holds the licensed documents · Year: 2016 · Reviewed: 2026-05-15 · Volatile: false (multi-year ICAO revision cycle).

## The ICAO axes (standard Annex 19 labels)

- **Severity** (the A7 `rows` axis, low → high): **Negligible · Minor · Major ·
  Hazardous · Catastrophic** (ICAO severity classes E → A; index 1 = Negligible,
  5 = Catastrophic).
- **Likelihood** (the A7 `cols` axis, low → high): **Extremely Improbable · Improbable ·
  Remote · Occasional · Frequent** (ICAO likelihood 1 → 5).

## The acceptability bands (the red/amber/green RCS regions)

`risk_matrix.score()` multiplies (severity × likelihood) → a 1..25 raw score, then
maps it to one of the three ICAO acceptability regions. The bands are **contiguous**
and cover the full 1..25 range (A7 `MatrixConfig` contract):

| Region | Score range | Action |
|---|---|---|
| **Acceptable** (green) | 1–4 | Acceptable — monitor; no further mitigation required |
| **Tolerable with mitigation** (amber) | 5–12 | Tolerable only with risk mitigation — reduce so far as reasonably practicable before proceeding |
| **Intolerable** (red) | 13–25 | Intolerable — cease / do not proceed until risk is mitigated to acceptable |

The three-region split (Acceptable / Tolerable-with-mitigation / Intolerable) is the
ICAO RCS acceptability structure; the numeric cut-offs are the pack's calibration of
that structure over the 5×5 multiply scale (recorded here for competent-person
confirmation). The exact ICAO matrix-cell colouring is the user's licensed document —
this config gives a defensible, reproducible band map, not a reproduction of the ICAO
table.

## The MatrixConfig (consumed by `risk_matrix.score(matrix=AVIATION_5X5)`)

```yaml
# AVIATION_5X5 — ICAO Annex 19 Risk Classification Scheme as an A7 MatrixConfig.
rows: [Negligible, Minor, Major, Hazardous, Catastrophic]   # severity E->A (low->high)
cols: [Extremely Improbable, Improbable, Remote, Occasional, Frequent]  # likelihood 1->5
scoring: multiply
bands:
  - {name: Acceptable, min: 1, max: 4, action: "Acceptable — monitor; no further mitigation required"}
  - {name: Tolerable with mitigation, min: 5, max: 12, action: "Tolerable only with risk mitigation — reduce so far as reasonably practicable before proceeding"}
  - {name: Intolerable, min: 13, max: 25, action: "Intolerable — cease / do not proceed until risk is mitigated to acceptable"}
```

## Usage note

`aviation-hazard-register` and `aviation-change-safety-assessment` call
`risk_matrix.score(severity, likelihood, matrix=AVIATION_5X5)` for the initial and
residual ratings (then `risk_matrix.residual_delta()` for the movement), and run
`controls.rank_controls()` + `smart_actions.validate_register()` on every mitigation
(HoC-ranked, owner/date/hazard-traced). The model only *chooses* severity/likelihood;
the engine does the scoring — two assessors score the same input identically. The
aviation 5×5 is **data**; the engine is **shared** (Don't-Hand-Roll).
