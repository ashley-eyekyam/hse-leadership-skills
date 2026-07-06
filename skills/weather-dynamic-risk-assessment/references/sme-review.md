---
sme-review:
  personas:
    - role: "Renewables-field / dynamic-RA competent person (wind O&M site safety lead)"
      expertise: "Point-of-work dynamic weather risk assessment for renewables, hub-height vs base-of-tower wind measurement, BS 7121-1 man-riding wind limits, NFPA 780 lightning stand-down practice, manufacturer/CPA in-service crane wind limits, ice-accretion / visibility / temperature triggers, and the WAH Regs 2005 weather-as-a-work-governor duty."
      lens: "would a wind-O&M competent person and the WAH Regs 2005 stand behind this — every weather parameter led by a NAMED NUMERIC threshold -> a hold/stop/evacuate action -> a mandatory re-assessment trigger (never 'monitor the weather'), wind measured at hub height not base of tower, the BS 7121-1 2016 7 m/s man-riding figure cited correctly, the 15 m/s hub-height cut-off flagged [ASSUMED]/proposed-and-confirmed and never asserted as a fixed standard, every other threshold user-confirmed or [GAP], zero prior-incident PII leak"
modes:
  assessment:
    detected_by: "Q = the requested deliverable (a weather-dynamic risk assessment for the named turbine/site activity) — single-output skill; this mode is always active"
    floor:
      - id: threshold-action-per-parameter
        description: "Every weather parameter is led by a named numeric threshold -> a hold/stop/evacuate action (never 'monitor the weather')"
        anchors: ['threshold', 'action|hold|stop|evacuate']
        min_matches: 2
      - id: reassessment-trigger
        description: "Each parameter carries a mandatory re-assessment trigger, not a one-off limit"
        anchors: ['re-assessment|reassessment|trigger', 'threshold|parameter|limit']
        min_matches: 2
      - id: hub-height-not-base
        description: "Wind for a tower-top / hub-height decision is measured at hub height, not the base of the tower"
        anchors: ['hub.height|hub height', 'measured|not.{0,12}base|tower']
        min_matches: 2
      - id: bs7121-cited-edition
        description: "Where a personnel-carrier / man-riding is involved, BS 7121-1 is cited correctly with the right edition"
        anchors: ['bs 7121|man.riding|personnel.carrier', 'edition|cited|crane|lift']
        min_matches: 1
      - id: cutoff-proposed-confirmed
        description: "The ~15 m/s hub-height cut-off is proposed-and-confirmed for the activity, never asserted as a fixed standard"
        anchors: ['15 m/s|cut-off|cut off', 'propos|confirm']
        min_matches: 1
      - id: eliminate-exposure-first
        description: "The control leads with eliminating the weather exposure (re-schedule / ground-level work) before the stop-limit"
        anchors: ['eliminat|hierarchy|re-schedule', 'first|exposure|before']
        min_matches: 1
      - id: owned-dated-actions
        description: "Every action carries a named role owner and a date; unresolved values are [GAP]"
        anchors: ['action|owner', 'date|\[gap|owner']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **"Monitor the weather" with no numbers (S5)** — a parameter with no named numeric threshold, no
  triggered action, and no re-assessment trigger is advice, not a control. Every parameter is a
  threshold → action → re-assessment triple.
- **Wind at the wrong height** — a hub-height/tower-top decision made on a base-of-tower or
  forecast wind understates the exposure; measure at hub height.
- **The cut-off asserted as a standard (S6)** — the ~15 m/s hub-height cut-off is proposed and
  confirmed for the specific activity, not quoted as a fixed rule; and BS 7121-1 is cited to the
  right edition where man-riding is involved.
- **Stop-limit before elimination** — leading with a stop-limit rather than first eliminating the
  weather exposure (re-schedule, ground-level work) inverts the hierarchy.

## Sign-off note
SME review: ran (persona: renewables-field / dynamic-RA competent person); this is decision-support;
competent-person review still required. A FLAG it raises is recorded, never merge-blocking — it
precedes and never replaces the human competent-person review.
