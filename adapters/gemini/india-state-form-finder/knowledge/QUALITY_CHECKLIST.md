# Pre-output Quality Checklist — india-state-form-finder

Before producing any output, validate the draft against this gate:

- [ ] **State was resolved FIRST and confirmed** (mandatory state detection, CT-8) — no
      form cited on an unconfirmed or inferred-but-unconfirmed state.
- [ ] For an **unseeded/unknown state**, the output records `[GAP]` and refuses a national
      form number (KB-02 legacy-first discipline).
- [ ] Every cited `form` / `rule` / `due` / `portal` traces to a resolved
      `KB-REG-IN-STATEFORMS` row by fragment ID — no value from model recall.
- [ ] A `[GAP]` form value (e.g. the GJ row) is reported **as `[GAP]`** — never a guessed
      Gujarat form number (the citation grader is row-blind).
- [ ] The **OSH-Code transition note** is appended (legacy-first) with a pointer to
      india-osh-code-pack.
- [ ] The portal pointer is the **state** pointer (`KB-REG-IN-PORTALS`) or "verify locally"
      — never a hard-coded national portal.
- [ ] De-identification pass complete BEFORE drafting; no Aadhaar/name/employee-ID/address
      leak; small injury cells (<5) aggregated.
- [ ] The output states it is legacy-first decision-support requiring a competent person's
      review.
