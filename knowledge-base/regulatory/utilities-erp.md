<!-- KB-REG-UTILITIES-ERP -->
# Cross-list — Utilities / power emergency-response-plan (ERP) map

**Fragment ID:** `KB-REG-UTILITIES-ERP`
**What this is:** a copyright-safe **scenario → response-element → artifact map**
for emergency response in the utilities / power-generation & distribution sector —
the per-facet content cross-listed onto the utilities sector pack's emergency-plan
and arc-flash/electrical-safety skills. It names the emergency scenario classes,
the response-plan elements each demands, and the artifact produced, read alongside
the electrical-safety standard (`KB-STD-NFPA70E`) and the jurisdiction map.
**What this is NOT:** a reproduction of NFPA 70E, NERC, or any standard text. Cite
the standard/topic only — never paste standard wording.

> Source: utilities emergency-response practice (cross-walks KB-STD-NFPA70E arc-flash boundaries + sector ERP practice) — practice map · Year: 2026 · Reviewed: 2026-06-21 · Volatile: true (sector guidance drift; refresh on review).

## Emergency scenario → response element → artifact it grounds

| Scenario | Response element (paraphrased) | Artifact it grounds |
|---|---|---|
| Arc-flash / electrical incident | shock + arc-flash boundary control; rescue without contact | electrical emergency procedure |
| Loss of supply / blackout | switching / restoration sequence + safe-to-work | restoration plan |
| Substation / transformer fire | isolation + fire response + exclusion zone | facility ERP section |
| Downed conductor (public exposure) | exclusion + public safety + isolation request | downed-conductor response card |
| Confined-space / vault entry rescue | atmosphere + standby + rescue plan | confined-space rescue plan |
| Severe-weather / storm response | mutual-aid + crew safety + restoration triage | storm-response plan |

## How the skill uses this fragment
- A utilities ERP skill resolves the scenario class first, grounds the response
  elements here, cross-walks arc-flash boundaries from `KB-STD-NFPA70E` (the arc-
  flash engine supplies the numeric boundaries), and produces the ERP artifact.
- Controls follow the hierarchy of controls; a missing input is `[GAP]`.
  `bundled_in` wiring deferred to Phase 17 (SEAM-01).
