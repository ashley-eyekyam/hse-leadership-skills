<!-- KB-STD-IMDG -->
# IMDG Code — sea transport of dangerous goods (classification→artifact)

**Fragment ID:** `KB-STD-IMDG`
**What this is:** a copyright-safe **class → packing → segregation map** for the
International Maritime Dangerous Goods (IMDG) Code — the structure of the dangerous-goods
classes, packing groups, and segregation table used for sea transport, and how it
cross-walks the GHS class to a UN number / packing group / marine-pollutant marking.
**What this is NOT:** a reproduction of the IMDG Code normative text or its
dangerous-goods list.
The user holds the current (biennially amended) Code and resolves the binding entry
from the official Dangerous Goods List; cite the class / packing-group structure only.

> Source: IMDG Code (IMO) — class/packing/segregation structure (user holds the current amendment) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (biennial amendment cycle).

IMDG is the **sea** leg of the transport cross-walk that `chemical-transport-safety`
assembles; ADR (road, EU) and US DOT 49 CFR HMR (road, US) are the road legs
(`../regulatory/transport-adr-dot.md`). The GHS class (`ghs.md`) feeds the UN
classification; the binding UN number + proper shipping name are resolved from the
user's Dangerous Goods List, never assumed.

## Class → topic → artifact

| IMDG element | Topic | Grounds (skill / artifact) |
|---|---|---|
| UN classes 1–9 | explosives, gases, flammable liquids/solids, oxidisers, toxic/infectious, radioactive, corrosive, misc + marine pollutant | chemical-transport-safety |
| Packing groups | PG I/II/III (high/medium/low danger) | chemical-transport-safety |
| Segregation table | required separation between incompatible classes | chemical-transport-safety; tank-farm-bunding-controls (storage segregation analogue) |
| Marine pollutant | marking for environmentally hazardous substances | chemical-transport-safety (§14 SDS link) |

## How the skill uses this fragment
- `chemical-transport-safety` resolves the substance → UN number + class + packing
  group (from the user's DG List) → IMDG sea requirements + segregation, cross-walked
  with the road regimes; an unknown UN entry is `[GAP]`-flagged, never invented.
