# Methodology — Wind Turbine Work at Height + Rescue

The domain method this skill applies: a turbine work-at-height plan whose control order is led by
the **Work at Height Regulations 2005 reg-6 hierarchy** (`KB-REG-WAH2005`) and whose rescue is a
**mandatory, tested, team-owned recovery in minutes** (`KB-SNIP-RESCUE-PLAN`,
`KB-STD-GWO-WAH-RESCUE`). The single failure mode this method exists to kill is the WAH plan whose
rescue is "call 999 and wait".

## 0. De-identification FIRST

Before any analysis, scrub the climbers' / rescuers' **names and GWO certificate numbers** to role
labels (`references/deid-checklist.md`); cite the GWO competence **requirement**, never the
certificate number (`[GAP]`).

## 1. Scope to the named turbine / site / WAH activity

Confirm the named turbine + site (the specificity anchor) and the specific WAH activity broken into
steps (nacelle / hub / blade / tower-internal) and its access method. Refuse a generic "the
turbines". A lone / single-climber activity restores the two-person-minimum baseline (a solo climb
is rejected; REN-02 routes lone WAH here).

## 2. Control order — reg-6 avoid → prevent (collective before personal) → mitigate/arrest

Apply `controls.py` + `KB-SNIP-HOC` with the WAH-specific reg-6 order **leading**:

1. **AVOID work at height** where reasonably practicable — do the work at ground level, lower the
   component to ground, or use a man-rider / MEWP / platform so the worker is not exposed at height.
   The avoidance test is evidenced or recorded `[GAP]`.
2. **PREVENT a fall — collective before personal (reg 7).** Where work at height is unavoidable,
   select **collective fall-prevention** (guardrails, a working platform, fall-prevention nets)
   **before personal fall-arrest**. A jump straight to a harness/lanyard where collective
   prevention is practicable is a FLAG pushed up the hierarchy.
3. **MITIGATE / ARREST.** Personal fall-arrest (harness + energy-absorbing lanyard + a rated
   anchor) and fall-distance minimisation only after avoidance and collective prevention are
   exhausted; anchor points / system detail are `[GAP]` until supplied (reg 8 / Schedules).

## 3. The MANDATORY tested rescue plan (the core-value gate)

A WAH plan with **no** tested rescue is rejected (reg 4 makes rescue planning part of the work).
The rescue plan (`KB-SNIP-RESCUE-PLAN`, `KB-STD-GWO-WAH-RESCUE`) must be:

- **Planned before work begins** and resourced as part of the WAH plan — not improvised after a fall.
- **Team-owned and timed** — the team has the competence (GWO ART / equivalent), equipment and
  method to recover a suspended worker **within minutes** (suspension trauma), not after an external
  response arrives. The recovery method and time are stated; an untested capability or unstated time
  is a `[GAP]`.
- **Two-person-minimum + ground support** — a climb is a two-person-minimum team with ground support
  able to initiate the rescue.
- **Emergency services a supplement, never the plan.** Calling 999/112 is an addition to the team's
  own tested rescue. **A rescue arrangement whose lead is "call the emergency services and wait" is
  REJECTED.**

## 4. GWO competence (cited, not reproduced)

Record the **GWO competence requirement** — current GWO Working at Heights / First Aid / Advanced
Rescue Training, **refreshed every 2 years** — as a requirement of the climb team. **Do not
reproduce the licensed module curriculum or the certificate numbers**; certificate detail is
`[GAP]`, climber identities de-identified to role labels.

## 5. Weather thresholds — named here, owned by REN-03 (CONV-12)

Where the task is weather-sensitive, **name** the hold/stop thresholds (hub-height wind cut-off
≈ 15 m/s `[ASSUMED A4]`, lightning stand-down, ice/visibility) but **defer their ownership to
REN-03 `weather-dynamic-risk-assessment`** (`KB-DATA-WEATHER-THRESHOLDS`). The ≈15 m/s anchor is
**proposed-and-user-confirmed**, never embedded as a hard citation; the BS 7121-1 (2016) 7 m/s
man-riding ceiling is the only verified public anchor. Cross-reference the renewables hazard library
(`../../knowledge-base/hazard-library/renewables.md`) for the WAH / dropped-object / weather hazard
categories — single home, never restated.

## 6. Residual risk + SMART actions

Re-score residual risk on the `risk_matrix` 5×5 **after** the reg-6 controls + the tested rescue.
Record `[GAP]` for any unsupplied basis (anchor points, rescue recovery time, manufacturer/site
weather limits), and close each `[GAP]` with a SMART action (`smart_actions`) carrying a **named
role owner + an ISO due date + a measure**. Prefer higher-order controls; justify any PPE/admin-only.

## 7. India deferral (CONV-8)

For an India jurisdiction, defer statutory content to the `hse-india` engine via
`KB-REG-IN-RENEWABLES`: **state detection is mandatory**; never invent a national form number — emit
`[GAP]` where a state return is owed.

Every conclusion traces to a cited source + year (`KB-REG-WAH2005`, `KB-STD-GWO-WAH-RESCUE`,
`KB-SNIP-RESCUE-PLAN`); every action carries a named role owner and a due date.
