<!-- KB-REG-IN-PORTALS -->
# India — statutory filing-portal pointers (Shram Suvidha + state portals)

**Fragment ID:** `KB-REG-IN-PORTALS`
**What this is:** the **filing-portal pointer layer** for India statutory returns and
notices — the central Shram Suvidha portal plus the per-state factory/labour-department,
BOCW Welfare Board, and DGMS portals. **This is data, not code** — pointers a skill
surfaces *after* it has resolved the state and the obligation.
**What this is NOT:** a live, verified URL directory, and NOT a substitute for resolving
the state first. Where the filing target is state-specific, the pointer is
**"verify locally"** — the skill confirms the live portal with the user.

> Source: Shram Suvidha (https://shramsuvidha.gov.in/) + per-state factory/labour-department & BOCW Welfare Board portals + DGMS (https://www.dgms.gov.in/) — pointer map · Year: 2026 · Reviewed: 2026-06-17 · Volatile: true (portals migrate; URLs verified per filing).

**Mandatory state detection first.** A wrong-state portal = a misfiled statutory
return. Resolve the state via `KB-REG-IN-STATEFORMS` BEFORE surfacing any portal, and
**never present a single national portal as the filing target** for a state-specific
obligation.

## Pointer table

| Filing context | Portal pointer | Note |
|---|---|---|
| Central labour-law compliance / unified returns | **Shram Suvidha** — https://shramsuvidha.gov.in/ | Central single-window; the OSH-Code direction of travel. Coverage varies by law/state — verify the specific return is filed here for the user's state. |
| Factories Act state annual/half-yearly returns | **State factory / labour-department portal** | State-specific (e.g. the state Directorate of Industrial Safety & Health). `[GAP]` / verify locally — resolve the state first. |
| BOCW registration / cess / Form XXV | **State Construction Welfare Board portal** | State-specific. Verify locally; the welfare board administers BOCW filings per state. |
| Mines Act / DGMS notices & returns | **DGMS** — https://www.dgms.gov.in/ | Regional/zonal offices; resolve the mine's region first (`KB-REG-IN-STATEFORMS`). |
| PESO licensing | **PESO portal** | See `KB-REG-IN-PESO` for the licence/form cluster. |

## How the skills use this fragment
- Each India skill surfaces the portal pointer **only after** resolving the state and
  the obligation; a state-specific obligation gets the state-portal pointer (or a
  literal `[GAP]` / "verify locally"), never a hard-coded national portal.
- Shram Suvidha is offered as the **central** single-window where coverage exists, with
  the caveat that per-state factory/BOCW filings may still route through the state
  portal during the OSH-Code transition (`KB-REG-IN-OSH-CODE`).
- The pointers are confirmed live with the user before any filing instruction is relied
  on (the URLs migrate; this fragment is a pointer map, not a verified directory).
