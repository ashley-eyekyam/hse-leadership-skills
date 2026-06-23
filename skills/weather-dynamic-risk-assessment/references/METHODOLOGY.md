# Methodology — Weather Dynamic Risk Assessment

The domain method this skill applies: a point-of-work / dynamic weather risk assessment whose
every control is a **NAMED NUMERIC threshold → a hold / stop / evacuate ACTION → a MANDATORY
re-assessment TRIGGER** (`KB-SNIP-DYNAMIC-RA`, `KB-DATA-WEATHER-THRESHOLDS`), measured at **hub
height, not base of tower** for turbine work, and grounded in the weather-as-a-work-at-height-
governor duty of the Work at Height Regs 2005 (`KB-REG-WAH2005`). The single failure mode this
method exists to kill is "monitor the wind and stop if it gets too windy".

## 0. De-identification FIRST

Before any analysis, scrub any **prior weather-incident context** (a named worker / crew involved
in a previous weather-related event) and any personal contact to role labels
(`references/deid-checklist.md`). Lower de-id tier — asset/site data dominates — but role-labelling
is mandatory.

## 1. Scope to the named site / activity / equipment

Confirm the named site + activity (the specificity anchor) and the weather-sensitive task broken
into steps (tower-top / nacelle work, blade rope-access, crane or man-riding lift, outdoor
switching) and its controlling equipment. Refuse a generic "the wind farm" / "keep an eye on the
weather". Identify which weather parameters are in play (wind, lightning, ice, visibility,
temperature).

## 2. The dynamic-RA control spine — per parameter (the core-value gate)

For **each** weather parameter, build the control as a **THRESHOLD → ACTION → RE-ASSESSMENT
TRIGGER** (`KB-SNIP-DYNAMIC-RA`):

1. **Threshold.** A specific numeric trigger for the parameter. A weather control with **no
   number** ("stop if too windy") is **REJECTED**.
2. **Action.** What happens when the threshold is reached — **hold / stop / evacuate** — defined in
   advance, not decided on the day. A threshold with **no defined action** is REJECTED.
3. **Re-assessment trigger.** A defined event / interval that forces a fresh point-of-work
   assessment (forecast change, threshold approached, fixed interval). A threshold with **no
   re-assessment trigger** is REJECTED.

## 3. Measurement discipline — hub height, not base of tower

Wind is measured at **hub height, not base of tower** for tower-top / hub-height turbine work — a
base-of-tower reading understates the exposure. A base-of-tower reading used for a tower-top
decision is **flagged as a control failure**; every threshold is referenced to its measurement
point.

## 4. The anchors — propose-and-user-confirms, never invented (D-03)

- The **BS 7121-1 (2016 edition)** man-riding ceiling of **16 mph / 7 m/s** for a personnel-carrier
  (man-riding) lift is the one **verified public anchor** — cite it verbatim where a man-riding
  lift is used (the 2016 edition, **not** the 2006 edition).
- The hub-height tower-top wind cut-off of **≈ 15 m/s** is an **`[ASSUMED A4]` industry baseline —
  not a single citable standard**; it is **proposed and the user confirms it** (stricter for
  less-experienced teams), never embedded as a hard citation.
- **Lightning** stand-down follows **NFPA 780** practice / a lightning-warning service — the
  detection radius + time is user / service-confirmed → `[GAP]`.
- **Manufacturer / CPA** in-service crane wind limits, **ice-accretion**, **visibility** and
  **temperature** triggers are **user-confirmed or `[GAP]`** — never invented as a fixed standard.

## 5. Hierarchy of controls — eliminate the exposure first

Apply `controls.py` + `KB-SNIP-HOC` so the control leads with **eliminating / substituting the
weather exposure** (reschedule to a forecast low-weather window, do the work in shelter, choose a
lower-exposure method) **before** the administrative stop-limit. A stop-limit-only treatment where
rescheduling / sheltering is reasonably practicable is a FLAG pushed up the hierarchy. Cross-
reference the renewables hazard library (`../../knowledge-base/hazard-library/renewables.md`) for
the weather / WAH / dropped-object hazard categories — single home, never restated.

## 6. Residual risk + SMART actions

Re-score residual risk on the `risk_matrix` 5×5 **after** the thresholds + actions. Record `[GAP]`
for any unsupplied numeric basis (manufacturer/site limits, lightning detection radius + time, ice
/ visibility / temperature trigger points), and close each `[GAP]` with a SMART action
(`smart_actions`) carrying a **named role owner + an ISO due date + a measure**. Prefer higher-
order controls; justify any administrative-only.

## 7. CONV-12 — this skill OWNS the thresholds REN-01 names

`wind-turbine-work-at-height-rescue` (REN-01) **names** the hub-height wind hold / lightning
stand-down and **defers their ownership here**. This skill owns `KB-DATA-WEATHER-THRESHOLDS` and
the dynamic-RA method; the WAH plan + tested rescue stays REN-01's, lone working stays REN-02's —
cross-referenced, never merged.

## 8. India deferral (CONV-8)

For an India jurisdiction, defer statutory content to the `hse-india` engine via
`KB-REG-IN-RENEWABLES`: **state detection is mandatory**; never invent a national form number —
emit `[GAP]` where a state return is owed.

Every conclusion traces to a cited source + year (`KB-DATA-WEATHER-THRESHOLDS`, `KB-SNIP-DYNAMIC-RA`,
`KB-REG-WAH2005`); every action carries a named role owner and a due date.
