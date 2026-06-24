<!-- KB-HAZ-RENEWABLES -->
# Renewables hazard library — turbine WAH / rescue / weather (hazard→artifact map)

**Fragment ID:** `KB-HAZ-RENEWABLES`
**What this is:** a copyright-safe **hazard library** for the renewable-energy sector
(wind/solar) — a structured menu of the recurring high-consequence hazards of turbine
and array work, each routed to the assessment/control artifact it grounds. A seeding
list for HIRA / JSA / permit-to-work intake, not a substitute for the site assessment.
**What this is NOT:** a reproduction of any licensed standard (GWO/IEC) text. Cite
the hazard category and the standard's number/topic only — never paste the wording.

> Source: renewable-energy-sector hazard taxonomy (turbine WAH/rescue, weather thresholds) — hazard-category structure · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false.

This library seeds the hazard-identification step for wind/solar tasks, where the
defining failure modes are **work at height with confined rescue** and **weather-driven
stop conditions**. It grounds the risk assessment and the hierarchy-of-controls selection.

## Hazard → typical controls (hierarchy-of-controls framing) → artifact

| Hazard category | Examples | Higher-order controls it grounds | Artifact |
|---|---|---|---|
| **Work at height (WAH)** | nacelle/tower climbs, ladders, hub work | fixed climb-assist/lifts (engineering), fall arrest, exclusion zones | WAH risk assessment / permit |
| **Confined-space / tower rescue** | rescue from nacelle, tower, blade | rescue-plan design, evacuation devices, trained rescuers, comms | rescue plan + permit-to-work |
| **Weather-threshold stop conditions** | wind speed, lightning, ice, low visibility | defined stop limits (wind/lightning thresholds), task scheduling | weather hold/stop criteria in the method statement |
| **Electrical / arc-flash** | HV connections, converters, array DC | isolation/LOTO, arc-flash study | electrical-safety assessment (routes to `KB-STD-NFPA70E`) |
| **Stored / mechanical energy** | rotor lock, hydraulics, pitch/yaw | LOTO, rotor-lock procedure | LOTO procedure |
| **Lifting operations** | component lifts, crane work | lift-plan design, exclusion zones, competent slinger | lift plan |
| **Lone / remote working** | offshore, remote arrays | comms, check-in, emergency response coverage | lone-working / ERP arrangement |

## How the skill uses this fragment
- Seeds renewables HIRA / JSA / permit hazard identification; every listed hazard is
  confirmed against the actual task/site — listed ≠ present.
- Weather-threshold stop conditions are site-specific limits the duty-holder sets,
  recorded — never invented; controls ranked via `KB-SNIP-HOC`.
- A hazard with no site-specific control captured is recorded as `[GAP]`, never invented.
