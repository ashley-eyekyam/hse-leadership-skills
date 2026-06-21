<!-- KB-REG-RENEWABLES-ELECTRICAL -->
# Cross-list — Renewables electrical-safety (wind / solar / BESS) map

**Fragment ID:** `KB-REG-RENEWABLES-ELECTRICAL`
**What this is:** a copyright-safe **asset → electrical-hazard → control map** for
electrical safety on renewable-energy assets — the per-facet content cross-listed
onto the renewables sector pack's electrical-safety, working-at-height and
isolation skills. It names the renewable asset classes, the electrical hazards
specific to each, and the control/isolation artifact, read alongside the
electrical-safety standard (`KB-STD-NFPA70E`) and `KB-REG-LOTO`.
**What this is NOT:** a reproduction of NFPA 70E, IEC, GWO, or any standard text.
Cite the standard/topic only — never paste standard wording.

> Source: renewables electrical-safety practice (cross-walks KB-STD-NFPA70E + KB-REG-LOTO + sector WAH/electrical practice) — practice map · Year: 2026 · Reviewed: 2026-06-21 · Volatile: true (sector standards drift; refresh on review).

## Asset → electrical hazard → control it grounds

| Asset | Electrical hazard (paraphrased) | Control / artifact it grounds |
|---|---|---|
| Wind turbine (nacelle/tower) | HV converter + stored energy at height | isolation (KB-REG-LOTO) + arc-flash boundary + rescue-at-height plan |
| Solar PV array | DC remains live in daylight (cannot fully de-energize) | DC-isolation procedure + live-working controls |
| Battery energy storage (BESS) | DC short-circuit + thermal-runaway energy | isolation + thermal-runaway emergency plan |
| Inverter / converter station | HV AC interface + arc-flash | arc-flash boundary (engine) + permit |
| Grid connection / substation | HV switching | switching procedure + permit |
| Cabling / collector works | buried + live cable strike | cable-avoidance / isolation procedure |

## How the skill uses this fragment
- A renewables electrical skill resolves the asset first, grounds the hazard and
  the isolation/control here, cross-walks `KB-REG-LOTO` for the isolation steps and
  the arc-flash engine for boundaries, and produces the permit/isolation artifact.
- Controls follow the hierarchy of controls; PV's "cannot de-energize in daylight"
  edge case is grounded explicitly. A missing input is `[GAP]`. `bundled_in`
  wiring deferred to Phase 17 (SEAM-01).
