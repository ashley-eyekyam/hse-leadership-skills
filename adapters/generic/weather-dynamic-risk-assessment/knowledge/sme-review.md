---
sme-review:
  personas:
    - role: "Renewables-field / dynamic-RA competent person (wind O&M site safety lead)"
      expertise: "Point-of-work dynamic weather risk assessment for renewables, hub-height vs base-of-tower wind measurement, BS 7121-1 man-riding wind limits, NFPA 780 lightning stand-down practice, manufacturer/CPA in-service crane wind limits, ice-accretion / visibility / temperature triggers, and the WAH Regs 2005 weather-as-a-work-governor duty."
      lens: "would a wind-O&M competent person and the WAH Regs 2005 stand behind this — every weather parameter led by a NAMED NUMERIC threshold -> a hold/stop/evacuate action -> a mandatory re-assessment trigger (never 'monitor the weather'), wind measured at hub height not base of tower, the BS 7121-1 2016 7 m/s man-riding figure cited correctly, the 15 m/s hub-height cut-off flagged [ASSUMED]/proposed-and-confirmed and never asserted as a fixed standard, every other threshold user-confirmed or [GAP], zero prior-incident PII leak"
---

# SME Review & Sign-off — weather-dynamic-risk-assessment

The reviewer adopts the **renewables-field / dynamic-RA competent person** persona and reads the
draft against the nuanced things only a wind-O&M competent person catches — not just the universal
hard gates.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Threshold → action → re-assessment trigger, per parameter.** Every weather parameter in
      play (wind, lightning, ice, visibility, temperature) carries a **specific numeric threshold**,
      a **pre-decided action** (hold / stop / evacuate), and a **mandatory re-assessment trigger** —
      defined in advance, not on the day. **A "monitor the wind / stop if it gets too windy" control
      with no number is REJECTED** (`KB-SNIP-DYNAMIC-RA`).
- [ ] **Hub-height, not base of tower.** Wind for a tower-top / hub-height decision is measured at
      **hub height**; a base-of-tower reading used for a tower-top decision is **flagged as a
      control failure** (it understates the exposure).
- [ ] **BS 7121-1 cited correctly + the right edition.** Where a personnel-carrier (man-riding)
      lift is used, the **BS 7121-1 (2016 edition) 16 mph / 7 m/s** man-riding ceiling is cited as
      the verified anchor — **not** the 2006 edition; it is the one citable wind figure.
- [ ] **The ≈15 m/s cut-off is proposed-and-confirmed, never a fixed standard.** The hub-height
      tower-top cut-off ≈ 15 m/s is flagged `[ASSUMED A4]` / proposed-and-user-confirmed — never
      asserted as a hard citation. Every other numeric threshold (manufacturer / CPA crane limit,
      lightning detection radius/time, ice / visibility / temperature) is **user-confirmed or
      `[GAP]`**, never invented.
- [ ] **Eliminate the weather exposure before the stop-limit.** The control leads with eliminating
      / substituting the exposure (reschedule to a forecast low-weather window, shelter the work)
      before the administrative stop-limit (`KB-SNIP-HOC`); a stop-limit-only treatment where
      rescheduling is practicable is pushed up the hierarchy.
- [ ] **Specificity + defensibility.** Every threshold is specific to the named site / activity /
      equipment and tied to its measurement point; every conclusion traces to a cited source + year
      (`KB-DATA-WEATHER-THRESHOLDS`, `KB-SNIP-DYNAMIC-RA`, `KB-REG-WAH2005`); each action carries a
      named role owner + a due date; residual risk is re-scored on the 5×5 after the thresholds +
      actions.
- [ ] **De-identification.** Zero prior weather-incident PII / personal-contact leak into the
      circulated copy; any prior-incident context is role-labelled; the re-identification key is
      held separately, never embedded.

## Sign-off note
SME review: ran (persona: renewables-field / dynamic-RA competent person); this is decision-support;
competent-person review still required. A FLAG it raises is recorded, never merge-blocking — it
precedes and never replaces the human competent-person review.
