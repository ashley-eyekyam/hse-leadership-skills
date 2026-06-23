# Dynamic Weather Risk Assessment — Blade rope-access, WTG-09, Wind Farm WF-7

**Site / activity:** WTG-09, Wind Farm WF-7 — blade rope-access at height
**Jurisdiction:** UK — Work at Height Regulations 2005 (SI 2005/735) reg 4 / 6 / 7 (weather governs whether work at height proceeds)
**Classification:** Internal — competent-person (renewables-field / dynamic-RA SME) review required
**De-identification:** Personnel are referred to by role label. Turbine IDs, anemometer placement and the numeric thresholds are asset data, not PII. The worker named in the prior high-wind near-miss is referred to by role; the re-identification key is held separately.

---

## 1. The proposed weather arrangement — and why it is rejected

The weather control proposed in the method statement was: *"monitor the wind and descend if it gets too strong"*, with the descend decision based on the anemometer at the **base of the tower**.

This is **rejected** on two counts:

- **No numeric threshold, no defined action point, no re-assessment trigger.** "Too strong" is decided on the day, under pressure, with the team already on the blade. A weather control with no number is not defensible.
- **Wrong measurement point.** A base-of-tower wind reading **understates** the hub-height exposure the rope-access team is actually working in. Using it for a tower-top decision is a **control failure**.

The arrangement is replaced below with a per-parameter **threshold → action → re-assessment trigger**, measured at **hub height**.

## 2. Weather working limits — threshold → action → re-assessment trigger

| Parameter | Threshold (measurement point) | Action | Re-assessment trigger | Owner |
|---|---|---|---|---|
| Wind (blade rope-access) | Hold at 13 m/s sustained; **stop and descend at ≈ 15 m/s** at **hub height** [ASSUMED — proposed-and-user-confirmed against the OEM in-service limit; not a fixed standard] | Hold, then stop and descend | Forecast change, a gust exceeding the hold value, or every 30 minutes | Site Lead (role) |
| Wind (man-riding lift to platform) | **7 m/s — BS 7121-1 man-riding ceiling (2016 edition) [VERIFIED]** | Stop the man-riding lift | Each lift and on a forecast change | Lift Supervisor (role) |
| Lightning | Any detected strike within 10 km [GAP — radius and all-clear time confirmed with the site lightning-warning service, per NFPA 780 practice] | Stand down, descend, evacuate exposed positions | On any strike detected within the radius | Site Lead (role) |
| Visibility / ice | Visibility below the safe-supervision distance, or any blade-surface ice [GAP — site-defined values] | Hold; do not commit to rope-access | Onset, or a forecast of freezing precipitation | Rope-Access Supervisor (role) |

Every parameter is led by a **named numeric threshold tied to its measurement point**, a **pre-decided action** (hold / stop / evacuate), and a **mandatory re-assessment trigger** — defined in advance, not on the day.

## 3. Anchors — what is verified, what is proposed, what is open

- **Verified:** the **BS 7121-1 man-riding ceiling of 7 m/s** (16 mph), 2016 edition — cited verbatim for the man-riding lift. This is the one citable wind figure.
- **Proposed-and-user-confirmed `[ASSUMED A4]`:** the **≈ 15 m/s hub-height cut-off** for blade rope-access — an industry baseline, not a single citable standard; confirmed here against the WTG-09 OEM in-service rope-access limit (stricter for less-experienced teams). It is never presented as a fixed standard.
- **`[GAP]`:** the lightning detection radius and all-clear time, the ice / visibility trigger values, and any manufacturer in-service crane wind limit — user / service-confirmed before the work, never invented.

## 4. Hierarchy of controls (eliminate the exposure first)

- **Eliminate:** where the blade inspection is not time-critical, reschedule the rope-access to a forecast low-wind window so the team is not exposed to the threshold at all (Site Lead (role)).
- **Engineering:** a **hub-height** anemometer feed with an automated stop alert at the hold and stop values (SCADA Lead (role)).
- **Administrative:** publish the weather working-limits matrix in the rope-access permit; lightning-detection stand-down procedure (Site Lead (role)).

A stop-limit-only treatment, with no attempt to reschedule out of the weather, is pushed up the hierarchy.

## 5. Key findings

| Finding | Risk | Basis |
|---|---|---|
| Method statement named no numeric wind limit for blade rope-access | High | Method statement MS-WTG09-blade revision 1 |
| Wind was read at the base of the tower for a tower-top decision (control failure) | High | Pre-task survey, WF-7 anemometer placement |

## 6. Actions (owned + dated)

| Action | Owner | Due |
|---|---|---|
| Confirm the hub-height wind hold/stop values against the WTG-09 OEM in-service rope-access limit and record the confirmed numbers | Site Lead (role) | within 2 weeks |
| Confirm the lightning detection radius and all-clear time with the site lightning-warning service and close the [GAP] | Site Lead (role) | within 2 weeks |
| Relocate / add a hub-height anemometer feed for the descend decision and wire the automated stop alert | SCADA Lead (role) | within 4 weeks |

## 7. Prior weather-incident context (role level)

The prior high-wind near-miss on this turbine is recorded at role level: the technician involved is referred to as Rope-Access Supervisor (role). Weather-related stand-down events for this operator/region this year are aggregated, with small cells (< 5) suppressed and secondary suppression applied so no suppressed value can be back-calculated from the total.

## 8. Regulatory & reference basis

- Work at Height Regulations 2005 (SI 2005/735) reg 4 / 6 / 7 — weather governs whether work at height proceeds.
- BS 7121-1 man-riding ceiling 16 mph / 7 m/s (2016 edition) [VERIFIED anchor].
- NFPA 780 — lightning stand-down practice (detection radius + time user/service-confirmed).
- Hub-height wind cut-off ≈ 15 m/s [ASSUMED A4 — industry baseline, proposed-and-user-confirmed, not a fixed standard].
- ISO 45001 cl 6.1.2 (dynamic / point-of-work risk assessment).

*Decision-support only; a competent person must review this assessment before use.*
