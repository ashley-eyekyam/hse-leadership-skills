<!-- KB-REG-LOTO -->
# Cross-list — Lockout/Tagout (control of hazardous energy) map

**Fragment ID:** `KB-REG-LOTO`
**What this is:** a copyright-safe **energy-source → isolation-step → artifact
map** for the control of hazardous energy (lockout/tagout) during servicing and
maintenance — the per-facet content cross-listed onto permit, isolation and
maintenance skills. It names the energy classes, the isolation steps, and the
verification a LOTO procedure must produce, read alongside the jurisdiction map
(US 29 CFR 1910.147 / 1926.417; UK EAWR / safe-isolation practice).
**What this is NOT:** a reproduction of 29 CFR 1910.147, EAWR, or any standard
text. Cite the CFR/regulation/topic only — never paste standard wording.

> Source: control-of-hazardous-energy practice (cross-walks OSHA 29 CFR 1910.147 / 1926.417 + UK EAWR 1989 safe-isolation) — practice map · Year: 2026 · Reviewed: 2026-06-21 · Volatile: false (stable practice; refresh on review).

## Energy source → isolation step → artifact it grounds

| Energy source | Isolation step (paraphrased) | Artifact it grounds |
|---|---|---|
| Electrical | Disconnect + lock + verify dead | electrical isolation certificate |
| Stored mechanical / spring | Block / restrain stored energy | mechanical isolation record |
| Hydraulic / pneumatic | Bleed + isolate + verify zero pressure | pressure-isolation record |
| Thermal | Cool / drain + isolate supply | thermal isolation record |
| Gravity / suspended load | Block / pin / support the load | load-control record |
| Process / chemical | Isolate + drain + slip-blind / line-break | line-isolation permit |

## Procedure steps it grounds
- Identify all energy sources → notify affected workers → shut down → isolate →
  apply locks/tags → release/restrain stored energy → **verify zero energy** →
  perform work → controlled re-energization. Group/shift-transfer and removal of
  another worker's lock are explicit edge cases the procedure must cover.

## How the skill uses this fragment
- A permit/isolation/maintenance skill enumerates every energy source per the
  table, grounds the isolation step and the verify-zero-energy gate, and produces
  the isolation artifact. Controls follow the hierarchy of controls; a missing
  input is `[GAP]`. `bundled_in` wiring deferred to Phase 17 (SEAM-01).
