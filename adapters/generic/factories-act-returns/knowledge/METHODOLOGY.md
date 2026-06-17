# Methodology — Factories Act state-return assembly (legacy-first, state-detection-first)

A return-assembly method over `KB-REG-IN-STATEFORMS`, gated by **mandatory state
detection** (CT-8). It assembles only the fields the source supplies and marks every
unverified field — including the **GJ** form id — a literal `[GAP]`.

## The assembly method

1. **Resolve the state (BLOCKING gate).** Ask, or infer-from-address then confirm. An
   unseeded/unknown state → `[GAP]` + refuse to assemble a national form (KB-02).
2. **Resolve the obligation.** annual-return / half-yearly-return / register.
3. **Read the matched `KB-REG-IN-STATEFORMS` row** and assemble the return under its
   prescribed `form` / `rule` / `due`:
   - **TN** Form 22 · **KA** Form 20 · **MH** Form 27 · **DL** Form 21 (verified anchors).
   - **GJ** annual-return → the row's `form` is a literal `[GAP]`: assemble the verified
     fields but render the form id as `[GAP]` (verify the Gujarat form with a competent
     person). NEVER substitute a guessed Gujarat form number — the citation grader is
     row-blind, so a fabricated value would pass the automated gate but fail a regulator.
4. **Fill the prescribed fields** from the elicited (de-identified) return data; every
   field absent from the source is a literal `[GAP]`, never fabricated.
5. **Append the OSH-Code transition note** (`KB-REG-IN-OSH-CODE`, pointer to
   `india-osh-code-pack`) and the state factory-department portal pointer
   (`KB-REG-IN-PORTALS`).

## Evidence discipline
- Every form id / rule / due / portal traces to the resolved `KB-REG-IN-STATEFORMS` row
  by fragment ID — never to model recall. Unverified values are `[GAP]`.
- De-identify occupier/worker PII (Aadhaar, employee ID, address, injury detail) BEFORE
  drafting; aggregate small accident cells (<5) before they enter the return.
