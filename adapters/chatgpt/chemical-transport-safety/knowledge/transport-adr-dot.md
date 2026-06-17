<!-- KB-REG-EU-ADR -->
<!-- KB-REG-US-DOT-HMR -->
# Transport of dangerous goods — ADR (EU road) + US DOT HMR (road) map

**Fragment IDs:** `KB-REG-EU-ADR`, `KB-REG-US-DOT-HMR`
**What this is:** a copyright-safe **class → marking/placarding/segregation map** for
the two road dangerous-goods regimes the chemicals pack reads: ADR (the European
Agreement concerning the international carriage of Dangerous goods by Road) and the
US DOT Hazardous Materials Regulations (49 CFR 100–185).
**What this is NOT:** a reproduction of the ADR / 49 CFR text or the dangerous-goods
tables. Cite the class / packing-group / placard structure only; the user resolves
the binding entry from the official ADR table / 49 CFR §172.101 HMT.

> Source: ADR (UNECE) + US DOT HMR 49 CFR 100–185 — class/marking/placarding structure (user holds the official text) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (ADR biennial; HMR amendments).

ADR + DOT HMR are the **road** legs of the transport cross-walk; IMDG
(`../standards/imdg.md`) is the sea leg. Rail (RID) and air (IATA/ICAO-TI) are
**out of scope** for v1.0 (deferred — rail to `hse-rail` remit, air a distinct
regime); `chemical-transport-safety` flags them as `[GAP]`/out-of-scope rather than
guessing. The GHS class (`../standards/ghs.md`) feeds the UN classification; the
binding UN number + proper shipping name come from the user's regime table, never
assumed.

## `KB-REG-EU-ADR` — EU road

| ADR element | Topic | Grounds (skill / artifact) |
|---|---|---|
| Classification | UN classes 1–9, packing group | chemical-transport-safety |
| Packaging | approved packaging / IBC / tank codes | chemical-transport-safety |
| Marking / labelling | UN number, hazard labels | chemical-transport-safety |
| Placarding | orange plates / placards on the unit | chemical-transport-safety |
| Segregation / mixed loading | separation of incompatible goods | chemical-transport-safety |
| Documentation | transport document, instructions in writing | chemical-transport-safety |

## `KB-REG-US-DOT-HMR` — US road (49 CFR)

| HMR element | Topic | Grounds (skill / artifact) |
|---|---|---|
| Classification | hazard class + division (49 CFR 173) | chemical-transport-safety |
| Hazardous Materials Table | §172.101 entry (PSN, class, ID, PG, label) | chemical-transport-safety |
| Marking / labelling | §172 subpart D/E | chemical-transport-safety |
| Placarding | §172 subpart F | chemical-transport-safety |
| Shipping papers | §172 subpart C | chemical-transport-safety |

## How the skill uses these fragments
- `chemical-transport-safety` resolves the substance → UN number + class + packing
  group → the marking/placarding/segregation requirements for the selected mode
  (ADR road / DOT road / IMDG sea), cross-walked from the GHS class; rail/air are
  flagged out-of-scope, unknown entries `[GAP]`-flagged.
