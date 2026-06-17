# Methodology — India MSIHC MAH identification + emergency plan / safety report

## Method (India-facing — mandatory state detection)
1. **De-identify first** — any worker PII → role labels.
2. **Resolve the inventory + the STATE** from the intake. **State detection is mandatory** — ask or
   infer-from-address then **confirm before citing any form** (`KB-REG-IN-STATEFORMS`). Never assume a
   national form number.
3. **MAH identification** — compare the stored/handled hazardous-chemical quantities to the MSIHC
   Schedule threshold quantities (`KB-REG-IN-MSIHC`) → MAH yes/no verdict. An unresolved threshold is
   `[GAP]`-flagged, never an invented threshold.
4. **On-site emergency plan outline** + **safety-report outline** per MSIHC for an MAH installation;
   the state-resolved form is cited from the KB row.
5. **PESO pointers** — petroleum/explosives/gas/SMPV storage licensing from `KB-REG-IN-PESO`
   (referenced; hse-process owns it).
6. **OSH-Code transition note** appended (legacy-first — most states have not switched).
7. **Controls** HoC-ranked (`controls`); **emergency-plan actions** validated with `smart_actions`
   (owner + ISO date).

## Output discipline
- No hard-coded national form; no invented threshold/form. `[GAP]` + route to a competent person is
  honest. The state is confirmed before any citation.
