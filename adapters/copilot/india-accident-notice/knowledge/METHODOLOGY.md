# Methodology — India statutory accident-notice assembly (legacy-first, state-detection-first)

A notification-assembly method over `KB-REG-IN-STATEFORMS` (and the Mines/DGMS layer for a
mine), gated by **mandatory state detection** (CT-8). It produces the **filled notice itself**
and never re-runs the RCA (that is `incident-investigation`).

## The assembly method

1. **Resolve the state (BLOCKING gate).** Ask, or infer-from-address then confirm. An
   unseeded/unknown state → `[GAP]` + refuse to cite a national form (KB-02).
2. **Resolve the establishment type.** factory / construction / **mine** / other. For a
   **mine**, resolve the **DGMS region/zone first** and cross-reference `KB-REG-IN-MINES-ACT`
   / `KB-REG-IN-DGMS` (the verified 24h notice duty + Form J register; any un-verified DGMS
   numbered form id is a literal `[GAP]`, never invented).
3. **Resolve severity** (fatal / serious / dangerous occurrence) — drives the form + deadline.
4. **Read the matched accident-notice row** and assemble the filled notice under its prescribed
   `form` / `rule` / `due`:
   - **MH** Form 24 (within 24h) + Form 24A (dangerous occurrence); **TN** Form 18 + Form 26
     register; **DL** Form 23/27; **mine** → DGMS 24h notice + Form J register.
   - Every form id / field absent from the source is a literal `[GAP]`, never fabricated.
5. **Validate the follow-up actions** with `smart_actions`: each notification action carries a
   named owner + a deadline (the **24h timing** is the load-bearing one).
6. **Append the OSH-Code transition note** (the accident-notice duty is retained), surface the
   `KB-REG-IN-PORTALS` pointer, and **point to `incident-investigation` for the RCA**.

## Evidence discipline
- Every form id / rule / due / portal traces to `KB-REG-IN-STATEFORMS` (or the DGMS layer) by
  fragment ID — never to model recall. Unverified values are `[GAP]`.
- De-identify injured-party/witness PII (Aadhaar, employee ID, address, diagnosis) BEFORE
  drafting; aggregate small injury cells (<5) before they enter the notice.
- This skill does NOT perform root-cause analysis — it defers to `incident-investigation`.
