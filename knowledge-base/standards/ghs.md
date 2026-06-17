<!-- KB-STD-GHS -->
# UN GHS Rev.10 — classification + 16-section SDS map (clause→artifact)

**Fragment ID:** `KB-STD-GHS`
**What this is:** a copyright-safe **hazard-class → SDS-section map** — the UN GHS
hazard-class structure, the pictogram set, the H/P-statement *structure*, and the
16-section Safety Data Sheet order, plus how each grounds chemicals work.
**What this is NOT:** a reproduction of the GHS "Purple Book" normative text or the
verbatim H/P-statement wording. GHS is a UN reference; the user resolves the exact class
criteria and the official statement text from their licensed copy. Cite the class /
category / section *numbers* only — never paste the normative wording.

> Source: UN GHS Rev.10 (2023, class/section structure; user holds the licensed text) · Year: 2023 · Reviewed: 2026-05-15 · Volatile: false (multi-year revision cycle).

GHS is the **jurisdiction-independent** classification backbone the chemicals pack
leans on (CLP, OSHA HazCom and India HazCom-equivalents all build on it). Apply it
alongside the one statutory jurisdiction fragment a skill reads
(`../regulatory/eu-clp.md`, `../regulatory/us-osha.md`, …). A classification is only
as good as its data — an absent hazard datum is **`[GAP]`-flagged and routed to a
competent person / further testing**, never invented (the citation grader fails a
fabricated GHS class).

## Hazard-class families (structure only)

| Family | Class group (cite the class/category number) | Grounds (skill / artifact) |
|---|---|---|
| Physical | explosives, flammable gas/aerosol/liquid/solid, oxidisers, self-reactive, pyrophoric, organic peroxides, corrosive-to-metal, … | ghs-classification-sds-author; reactive-dust-explosion-assessment |
| Health | acute toxicity, skin corrosion/irritation, eye damage, sensitisation, mutagenicity, carcinogenicity, reproductive tox, STOT (single/repeat), aspiration | ghs-classification-sds-author; chemical-exposure-register |
| Environmental | hazardous to the aquatic environment (acute/chronic), hazardous to the ozone layer | ghs-classification-sds-author (§12 ecological) |

Each hazard class carries a **category** (severity rank), a **pictogram**, a
**signal word** (Danger / Warning), an **H-statement** (hazard) and **P-statements**
(precautionary) — resolved by class+category from the user's licensed GHS/CLP text,
never quoted from memory.

## The 16-section SDS order (the artifact map)

| § | SDS section | Renders as | Note |
|---|---|---|---|
| 1 | Identification | heading + table | product + supplier + emergency contact |
| 2 | Hazard identification | table + callout | GHS class + pictogram + signal word + H/P statements |
| 3 | Composition / information on ingredients | table | hazardous components + CAS + concentration |
| 4 | First-aid measures | findings | route-by-route |
| 5 | Fire-fighting measures | findings | suitable media, special hazards |
| 6 | Accidental release measures | findings | containment + clean-up |
| 7 | Handling and storage | findings | segregation, incompatibilities |
| **8** | **Exposure controls / personal protection** | **hoc_table** | **HoC-ranked — engineering/ventilation before PPE, never PPE-first; OEL/WEL/PEL with source+year** |
| 9 | Physical and chemical properties | table | — |
| 10 | Stability and reactivity | findings | incompatibilities, hazardous reactions (reactive-chemistry hand-off) |
| 11 | Toxicological information | findings | links to the exposure-register hazard rows |
| 12 | Ecological information | findings | aquatic hazard category |
| 13 | Disposal considerations | findings | — |
| 14 | Transport information | table | UN number / class / packing group — cross-walk via `chemical-transport-safety` (ADR/DOT/IMDG) |
| 15 | Regulatory information | findings | jurisdiction fragment (CLP/REACH/HazCom/MSIHC) |
| 16 | Other information | findings | revision/version, the de-identification + limitations notice |

## How the skills use this fragment
- `ghs-classification-sds-author` resolves substance/mixture data → GHS class+category
  → the 16-section SDS, with §8 rendered as an `hoc_table` (HoC-ranked handling
  controls, not PPE-first) and §14 cross-walked through `chemical-transport-safety`.
- `chemical-transport-safety` reads the §14 class/UN-number map for the road/sea cross-walk.
- An un-evidenced hazard datum is `[GAP]`-flagged (no invented class/category) — the
  SME-persona review and citation grader enforce this.
