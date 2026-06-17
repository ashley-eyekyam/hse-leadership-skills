<!-- KB-REG-IN-PESO -->
# India — PESO licensing (statutory map, legacy-first)

**Fragment ID:** `KB-REG-IN-PESO`
**What this is:** a copyright-safe **rule → licence/form map** for the Petroleum
and Explosives Safety Organisation (PESO) instruments — Petroleum Rules 2002,
Explosives Rules 2008, Gas Cylinder Rules 2016, and SMPV(U) Rules 2016 — the
licence type → form → authority cluster `peso-licensing-assistant` reads.
**What this is NOT:** a reproduction of the rules' text. Cite the rule numbers and
the form references only — never paste the statutory wording. Forms are resolved
**from this KB row**, never a hard-coded national form number assumed elsewhere.

> Source: PESO — Petroleum Rules 2002 / Explosives Rules 2008 / Gas Cylinder Rules 2016 / SMPV(U) Rules 2016 — citation map · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (rules + the OSH-Code transition drift; refresh on review).

PESO is a **central** authority; most licences are central pathways. The skill
still resolves the **site state** for state-interacting obligations (factory
siting near a Major Accident Hazard unit, state pollution-control consents) and
appends the OSH-Code transition note (legacy-first — most states have not
switched). State-form interactions resolve via `KB-REG-IN-STATEFORMS`. The MSIHC
on-site emergency plan instrument is **`KB-REG-IN-MSIHC`** (authored by
hse-chemicals; referenced here, not authored here).

## Rule → licence → form → use

| Instrument | Licence / scope | Form (cite from this row) | Grounds |
|---|---|---|---|
| Petroleum Rules 2002 | Storage/handling of petroleum (Class A/B/C) | licence forms per rule (resolve from the matched row) | peso-licensing-assistant |
| Explosives Rules 2008 | Manufacture/storage/transport of explosives | licence forms per rule | peso-licensing-assistant |
| Gas Cylinder Rules 2016 | Compressed-gas cylinders | Form E / Form F | peso-licensing-assistant |
| SMPV(U) Rules 2016 | Static & mobile pressure vessels (unfired) | Form LS-1A | peso-licensing-assistant |
| OSH Code transition | Subsumes these instruments (state-by-state) | transition note appended (legacy-first) | peso-licensing-assistant |

## How the skill uses this fragment
- `peso-licensing-assistant` resolves the installation + licence type → the matched
  row → verdict + form + authority + the OSH-Code transition note.
- State detection is mandatory where the obligation is state-specific (siting,
  state consents) — ask or infer-from-address-then-confirm, never silently assume.
- The MSIHC MAH on-site emergency plan reads `KB-REG-IN-MSIHC` (hse-chemicals home).
