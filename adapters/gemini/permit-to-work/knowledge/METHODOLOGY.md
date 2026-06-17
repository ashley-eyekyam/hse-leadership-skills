# Permit-to-work + SIMOPS — `permit-to-work`

Grounds in `KB-STD-PSM` (element (k) hot work; permit/coordination controls). SIMOPS is a SECTION within this skill (D-01) — never a separate skill.

## Steps
1. **Specify the task** + exact location.
2. **Hazards & isolations** — energy isolation (LOTO), atmosphere (gas test), safeguards, HoC-ranked (`controls`).
3. **SIMOPS detection** — if concurrent operations exist in the area, build the **SIMOPS coordination section**: conflicting activities, coordination controls (sequencing, exclusion zones, single point of coordination, cross-permit references), authorizing authority.
4. **Permit conditions** + validity period.
5. **Track** the permit actions with `smart_actions`.

## Discipline (load-bearing)
- SIMOPS is a permit/coordination control WITHIN this skill — no standalone SIMOPS workflow (D-01).
- An isolation that relies on the permit alone (administrative) without an engineered isolation is flagged.
- The permit is not valid until isolations + (where SIMOPS) the coordination controls are in place.
