---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A dynamic weather RA is built afresh from the named site/activity (Q1), the weather-sensitive task + controlling equipment (Q3) and the per-parameter numeric thresholds the user confirms (Q4/Q5/Q6); there is no prior quantitative baseline survey to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the activity, the parameters in play and each parameter's confirmed threshold are the assessment's starting facts."
    ELI-EVIDENCE: "The evidence types are folded into the controlling-equipment + parameters question (Q3), the per-parameter threshold/measurement-point capture (Q4/Q5) and the manufacturer/CPA/lightning-service source question (Q6) rather than asked as a separate dimension; the domain evidence list is documented in the Domain evidence types section below (forecast source, anemometer placement, manufacturer in-service limit, lightning-warning service)."
    ELI-SCORING: "Residual risk is framed on the standard risk_matrix 5x5 (a fixed scale, not a user-chosen one), and the threshold->action->re-assessment-trigger gate plus the hub-height-not-base measurement discipline are qualitative dynamic-RA gates, not a numeric scoring scale — so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q3, option: Personnel-carrier or man-riding lift, activates_questions: [Q3a], activates_kb_row: KB-DATA-WEATHER-THRESHOLDS, mandatory: true}
    - {when: Q4, option: Tower-top or hub-height turbine work, activates_questions: [Q5], activates_kb_row: KB-SNIP-DYNAMIC-RA, mandatory: true}
    - {when: Q2, option: India, activates_questions: [Q2a], activates_kb_row: KB-REG-IN-RENEWABLES, mandatory: true}
---

# Structured intake — weather-dynamic-risk-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named site / activity (Q1 — the specificity anchor)**, then the **jurisdiction (Q2)**, the
**weather-sensitive task + the controlling equipment (Q3 — and the man-riding-lift trigger)**,
the **measurement point (Q4 — the hub-height-not-base gate)**, the **weather parameters in play
and each one's numeric threshold (Q5 — the core-value gate)**, the **action + re-assessment
trigger at each threshold (Q6)**, the **threshold source (Q7 — manufacturer / lightning-service /
[GAP])**, and the output / owner / review questions. **Refuse to "keep an eye on the weather":
you need the named site (Q1) and the weather-sensitive activity (Q3) before any analysis. Refuse
a "monitor the wind and stop if it gets too windy" answer (Q5) with no number** — every weather
parameter is led by a **named numeric threshold → a hold / stop / evacuate action → a mandatory
re-assessment trigger**, measured at **hub height, not base of tower** for turbine work.

Three load-bearing branches: the **man-riding-lift branch** (Q3 = personnel-carrier / man-riding
lift → Q3a → the BS 7121-1 2016 7 m/s man-riding ceiling applies as the verified anchor,
`KB-DATA-WEATHER-THRESHOLDS`), the **hub-height-measurement branch** (Q4 = tower-top / hub-height
turbine work → Q5 → wind is read at hub height, not base of tower; a base-of-tower reading is a
control failure, `KB-SNIP-DYNAMIC-RA`), and the **mandatory India→state branch** (Q2 = India →
Q2a + `hse-india`; confirm the state before citing any rule — never a national form number, emit
`[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | **Scope of this assessment** | mcq | A single weather-sensitive task on one asset / a campaign of weather-sensitive tasks across a site / a site-wide weather working-limits matrix / a review of an existing weather arrangement | ELI-SCOPE | always |
| Q1 | **The named site / activity** (the specificity anchor) | free-text | "Name the exact site + activity (e.g. 'blade rope-access on WTG-09, Wind Farm WF-7'). **Refuse 'the wind farm' / 'keep an eye on the weather' — the assessment is site-and-activity-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Jurisdiction** (selects the work-at-height + weather duty map) | mcq | UK (WAH Regs 2005) / India / Other / Unknown | ELI-JURIS | always |
| Q2a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q2 == India |
| Q3 | **The weather-sensitive task + controlling equipment** (and the man-riding-lift trigger) | mcq+free-text | Tower-top or nacelle work / Blade rope-access or platform / Crane lift / Personnel-carrier or man-riding lift / Outdoor switching or ground work / Other (+ describe the task + equipment) | ELI-EXPOSURE | always |
| Q3a | *(Personnel-carrier or man-riding lift only)* Apply the BS 7121-1 man-riding ceiling | mcq→confirm | "A personnel-carrier (man-riding) lift carries a **verified public anchor**: the **BS 7121-1 (2016 edition) 16 mph / 7 m/s man-riding wind ceiling** (`KB-DATA-WEATHER-THRESHOLDS`). Confirm this applies as the man-riding stop threshold for this lift (this is the one cited anchor — every other threshold is proposed-and-confirmed or `[GAP]`)." | ELI-OBLIGATIONS | Q3 == Personnel-carrier or man-riding lift |
| Q4 | **Measurement point** (the hub-height-not-base gate) | mcq+free-text | Tower-top or hub-height turbine work / Ground or low-level outdoor work / Mixed (+ where is wind actually measured for this decision) | ELI-LOCATION | always |
| Q5 | **Weather parameters + each one's numeric threshold** (the core-value gate) | free-text | "For each parameter in play (wind, lightning, ice, visibility, temperature) state a **specific numeric threshold** — e.g. hub-height wind cut-off, man-riding wind ceiling, lightning detection radius, ice-accretion trigger, visibility metres, temperature limit. **A 'monitor the wind / stop if too windy' answer with NO number is REFUSED.** The hub-height wind cut-off ≈ **15 m/s** is `[ASSUMED A4]` — proposed-and-user-confirmed, never a fixed standard; manufacturer / CPA / lightning-service / ice / visibility values are user-confirmed or `[GAP]`." | ELI-EXPOSURE | always |
| Q6 | **Action + re-assessment trigger at each threshold** | free-text | "For each threshold, state the **pre-decided action** (hold / stop / evacuate) and the **mandatory re-assessment trigger** (forecast change, threshold approached, fixed interval). A threshold with no defined action, or no re-assessment trigger, is REFUSED (`KB-SNIP-DYNAMIC-RA`)." | ELI-OBLIGATIONS | always |
| Q7 | **Threshold source** (where each number comes from) | mcq+free-text | Manufacturer or CPA in-service limit supplied / Lightning-warning service criterion supplied / Industry baseline proposed-and-confirmed / Not yet supplied (+ which) — **unsupplied values are `[GAP]`, never invented as a fixed standard** | ELI-COMPETENCY | always |
| Q8 | Industry / setting | mcq+free-text | Onshore wind / Offshore wind / Solar (elevated structures) / Mixed renewables (+ detail) | ELI-INDUSTRY | always |
| Q9 | Output artifact wanted + its reader | mcq | full dynamic weather RA + working-limits matrix (consultant) / weather working-limits matrix (manager) / the point-of-work hold/stop/evacuate brief card (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns each weather threshold / the anemometer-placement / lightning-service / `[GAP]`-closure actions and who is the competent person reviewing the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-forecast-change / on-task-or-equipment-change / on-incident / before-each-campaign (or sooner) / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `man-riding-lift` (Q3 = personnel-carrier / man-riding lift → Q3a → apply the
BS 7121-1 2016 7 m/s man-riding ceiling, `KB-DATA-WEATHER-THRESHOLDS`); `hub-height-measurement`
(Q4 = tower-top / hub-height turbine work → Q5 → wind read at hub height, not base of tower,
`KB-SNIP-DYNAMIC-RA`); `india-state` (Q2 = India → Q2a + `hse-india`; **mandatory** — confirm the
state before citing any rule; emit `[GAP]`, never a national form number).

## Echo-back

After the last applicable question (Q11, plus Q2a / Q3a if their branches ran), **echo a
captured-facts summary** and confirm before any analysis:
"Producing a dynamic weather risk assessment for: blade rope-access on WTG-09, Wind Farm WF-7
(UK, WAH Regs 2005); weather-sensitive task = blade rope-access at height; wind measured at
hub height (not base of tower); thresholds = hub-height wind cut-off ≈ 15 m/s [ASSUMED —
proposed-and-user-confirmed], lightning stand-down per the site lightning-warning service [GAP —
detection radius + time], ice-accretion trigger [GAP]; action at each = hold then stop then
evacuate; re-assessment on a forecast change or when a threshold is approached; full dynamic
weather RA + working-limits matrix; review before each campaign — correct?" Any prior
weather-incident context is de-identified to role labels before drafting.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "the wind farm" / "keep an eye on the weather"; ask
  again or record `[GAP]`, never invent the site or its weather-sensitive task.
- **A weather control with no number is refused** — a "monitor the wind / stop if it gets too
  windy" answer (Q5) is **rejected**; every parameter is led by a named numeric threshold → a
  hold / stop / evacuate action → a mandatory re-assessment trigger (`KB-SNIP-DYNAMIC-RA`).
- **Wind is measured at hub height, not base of tower** — a base-of-tower reading used for a
  tower-top decision (Q4) is **flagged as a control failure**; the threshold is referenced to the
  measurement point.
- **Numeric thresholds are proposed-and-confirmed, never invented** — the ≈15 m/s hub-height
  cut-off is `[ASSUMED A4]`, proposed-and-user-confirmed; the BS 7121-1 2016 7 m/s man-riding
  ceiling is the only verified public anchor; every other value is user-confirmed or `[GAP]`.
  **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The weather-sensitive task + controlling equipment broken into steps (Q3) · the measurement
point / anemometer placement (Q4 — hub-height for turbine work, else a FLAG) · the per-parameter
numeric thresholds (Q5 — wind / lightning / ice / visibility / temperature; the BS 7121-1 2016
7 m/s man-riding anchor where a man-riding lift is used; the ≈15 m/s hub-height cut-off `[ASSUMED]`;
manufacturer / CPA / lightning-service / ice / visibility values user-confirmed or `[GAP]`) · the
action + re-assessment trigger at each threshold (Q6) · the threshold source (Q7 — manufacturer
in-service limit / lightning-warning service / industry baseline / `[GAP]`) · the forecast source
and update cadence · any prior weather-related incident context (de-identified to role label).
