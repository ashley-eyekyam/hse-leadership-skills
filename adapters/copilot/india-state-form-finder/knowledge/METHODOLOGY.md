# Methodology — India state-form resolution (legacy-first, state-detection-first)

The domain method is a deterministic lookup over `KB-REG-IN-STATEFORMS`, gated by
**mandatory state detection** (CT-8). It never reproduces statute text and never
invents a form value.

## The resolution algorithm

1. **Resolve the state (BLOCKING gate).** Obtain the state explicitly, or infer it
   from a supplied address and **confirm it back**. If the state is Unknown or outside
   the seeded set (TN/KA/MH/DL/GJ), STOP: record `[GAP]`, advise "verify the state form
   with a competent person", and refuse to cite a national form number (KB-02).
2. **Resolve the law + obligation.** `factories-act` or `bocw` (other laws defer to
   their owning sector pack — PESO→hse-process, MSIHC→hse-chemicals, Mines/DGMS→hse-mining).
3. **Read the matched row** in `KB-REG-IN-STATEFORMS` for `(law, state, obligation)`.
   Return its `form` / `rule` / `due` / `portal` as the **primary, legacy-first** answer.
   - If the row's `form` is a literal `[GAP]` (e.g. the GJ annual-return row), say so
     explicitly — never substitute a guessed value (the citation grader is row-blind; a
     fabricated value would pass the automated gate but fail a regulator).
4. **Append the OSH-Code transition note** from the row's `osh_transition` field and
   point to `india-osh-code-pack` for the legacy→consolidated mapping (`KB-REG-IN-OSH-CODE`).
5. **Surface the portal pointer** from `KB-REG-IN-PORTALS` (state portal — verify
   locally; never a hard-coded national portal as the filing target).

## Evidence discipline
- Every cited form/rule/due/portal traces to a resolved `KB-REG-IN-STATEFORMS` row by
  its fragment ID — never to model recall.
- Any unverified value is a literal `[GAP]`, routed to a competent person.
- De-identify worker/establishment PII (Aadhaar, employee ID, address, health detail)
  BEFORE drafting; aggregate small injury cells (<5).
