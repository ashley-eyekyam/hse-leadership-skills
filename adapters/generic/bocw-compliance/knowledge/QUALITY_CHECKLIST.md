# Pre-output Quality Checklist — bocw-compliance

Before producing any output, validate the draft against this gate:

- [ ] **State resolved FIRST and confirmed** (mandatory state detection, CT-8) — no
      Welfare-Board return/portal cited on an unconfirmed state.
- [ ] An **unseeded/unknown state** yields `[GAP]` for state-specific values and refuses a
      national form (KB-02).
- [ ] **Form XXV annual return + 1% cess** cited as the verified anchors; every other
      state-specific value (safety-officer headcount, accident-notice form/timing, cess due
      date) the KB does not verify is `[GAP]` — never invented.
- [ ] Every cited duty/rule traces to `KB-REG-IN-BOCW` / `KB-REG-IN-STATEFORMS` by fragment
      ID.
- [ ] Each gap carries a **HoC-ranked corrective control** (engineering/admin before PPE), a
      named owner, and a date.
- [ ] **OSH-Code transition note** appended (BOCW subsumed; legacy-first) + the state
      Welfare Board portal pointer (`KB-REG-IN-PORTALS`).
- [ ] De-identification pass complete BEFORE drafting; no Aadhaar/name/employee-ID/address
      leak; small injury cells (<5) aggregated.
- [ ] Output states it is legacy-first decision-support requiring a competent person's review.
