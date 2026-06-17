# Pre-output Quality Checklist — factories-act-returns

Before producing any output, validate the draft against this gate:

- [ ] **State resolved FIRST and confirmed** (mandatory state detection, CT-8) — no return
      assembled on an unconfirmed state.
- [ ] An **unseeded/unknown state** yields `[GAP]` and refuses a national form (KB-02).
- [ ] The form id traces to the resolved `KB-REG-IN-STATEFORMS` row (TN Form 22 / KA Form 20
      / MH Form 27 / DL Form 21).
- [ ] The **GJ** annual-return form id is rendered **as `[GAP]`** — never a guessed Gujarat
      form number (the citation grader is row-blind).
- [ ] Every return field absent from the source is a literal `[GAP]` — never fabricated.
- [ ] **OSH-Code transition note** appended (legacy-first) + the state factory-department
      portal pointer (`KB-REG-IN-PORTALS`).
- [ ] De-identification pass complete BEFORE drafting; no Aadhaar/name/employee-ID/address
      leak; small accident cells (<5) aggregated before entering the return.
- [ ] Output states it is legacy-first decision-support requiring a competent person's review
      before filing.
