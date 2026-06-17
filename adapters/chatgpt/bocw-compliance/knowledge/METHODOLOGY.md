# Methodology — BOCW compliance assessment (legacy-first, state-detection-first)

A duty-gap method over `KB-REG-IN-BOCW`, gated by **mandatory state detection** (CT-8).
It never reproduces statute text and never invents a state-specific value.

## The assessment method

1. **Resolve the state (BLOCKING gate).** Ask, or infer-from-address then confirm. An
   unseeded/unknown state → `[GAP]` for any state-specific value + a refusal to cite a
   national form (the Welfare Board return/portal is state-specific).
2. **Capture the establishment profile.** Nature of work, worker headcount (the ≥10
   registration trigger + the Safety-Officer/Committee thresholds), and cost of
   construction (the 1% cess). De-identify; aggregate small counts.
3. **Walk the BOCW duty set** (`KB-REG-IN-BOCW`): establishment registration; beneficiary
   registration; 1% welfare cess; **Form XXV annual return** (by ~15 Feb — the verified
   anchor, also a `KB-REG-IN-STATEFORMS` row); Safety-Officer/Committee appointment;
   accident notice.
4. **Produce the gap-list.** For each duty, PASS or a gap with: the cited rule, a
   **HoC-ranked corrective control** (`controls` — engineering/admin before PPE), a
   role-label owner, and a date. Any state-specific value the KB does not verify
   (safety-officer headcount, accident-notice form/timing, cess due date) is a literal
   `[GAP]`, never invented (the citation grader is row-blind).
5. **Append the OSH-Code transition note** (BOCW subsumed; commencement state-by-state and
   largely pending; savings clause keeps legacy filings valid) and the state Welfare Board
   portal pointer (`KB-REG-IN-PORTALS`).

## Evidence discipline
- Every cited duty/form/threshold traces to `KB-REG-IN-BOCW` / `KB-REG-IN-STATEFORMS` by
  fragment ID — never to model recall. Unverified values are `[GAP]`.
- De-identify worker/establishment PII (Aadhaar, employee ID, address, health) BEFORE
  drafting; aggregate small injury cells (<5).
