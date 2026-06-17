# India PESO licensing + MSIHC on-site emergency plan — `peso-licensing-assistant`

Grounds in `KB-REG-IN-PESO` (+ references `KB-REG-IN-MSIHC`, hse-chemicals home, for the MSIHC plan). Legacy-first, state-aware.

## Steps
1. **Bound the installation** + capacity.
2. **Resolve the licence** — match the PESO instrument (Petroleum/Explosives/Gas-Cylinder/SMPV(U)) → form (Form E/F, LS-1A) from the KB row. NEVER hard-code a national form number.
3. **State detection (MANDATORY where state-specific)** — resolve the site state (ask / infer-then-confirm) for siting / state-consent interactions via `KB-REG-IN-STATEFORMS`.
4. **MSIHC on-site emergency plan** — if the installation is a MAH (MSIHC thresholds), structure the on-site emergency plan (reads KB-REG-IN-MSIHC).
5. **OSH-Code transition note** — appended (legacy-first).
6. **Track** the package actions with `smart_actions`.

## Discipline (load-bearing)
- No hard-coded national form number — every form from the KB row.
- State detection is mandatory where the obligation is state-specific — ask, never silently assume.
- The india-osh-code transition SKILL is hse-india's; this skill only appends the transition note.
