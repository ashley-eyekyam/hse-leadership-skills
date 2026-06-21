<!-- KB-STD-NFPA70E -->
# NFPA 70E / IEEE 1584 — arc-flash boundary & PPE category (clause→artifact map)

**Fragment ID:** `KB-STD-NFPA70E`
**What this is:** a copyright-safe **clause/table-number → output-artifact map** for
NFPA 70E (electrical-safety-in-the-workplace) and the IEEE 1584 arc-flash
incident-energy method — the structure of the arc-flash study and how its outputs
ground HSE work.
**What this is NOT:** a reproduction of the standard's tables or normative text.
Cite the clause / table numbers and the PPE-category *structure* only — never paste
the table cells or wording (user holds the licensed copy).

> Source: NFPA 70E (electrical safety in the workplace) + IEEE 1584-2018 (arc-flash calculation) — citation/structure map · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false (multi-year cycle).

NFPA 70E governs the **practical safeguarding of workers from electrical hazards**
— shock and arc-flash. The arc-flash assessment quantifies the **incident energy**
at the working distance (IEEE 1584-2018 incident-energy method) and sets the
**arc-flash boundary** and the **PPE** required. It pairs with the SUB-02 arc-flash
engine (`scripts/hse_components/arcflash.py`), which implements the IEEE 1584-2018
calculation route; this fragment is the structural reference the engine and skills cite.

## Element → what it grounds

| Element / clause topic | Focus | Artifact it grounds |
|---|---|---|
| Arc-flash risk assessment | likelihood + incident energy at working distance | the arc-flash study record |
| Incident energy (IEEE 1584-2018) | calculated cal/cm² at the working distance | the labelled incident-energy value |
| Arc-flash boundary | distance at which incident energy = 1.2 cal/cm² (second-degree-burn onset) | the boundary marked on the equipment label |
| PPE category selection | category 1–4 by incident-energy band (structure only) | the PPE specification + warning label |
| Justification for energized work | shock/arc-flash hazard analysis + energized-work permit | the energized-work permit |

## PPE-category structure (paraphrased — never the table)

NFPA 70E **Table 130.7(C)(15)(a)/(c)** maps the calculated incident energy (cal/cm²)
to a PPE category by ascending energy bands with the published threshold breakpoints
**1.2 / 4 / 8 / 25 / 40 cal/cm²** — i.e. below 1.2 no arc-flash PPE is required;
categories 1–4 cover the successive bands up to 40 cal/cm²; above 40 cal/cm² no
table PPE applies and engineering controls / de-energization are required. This
fragment cites those breakpoint *numbers* and the band *structure* only; the actual
category-to-clothing tables are copyrighted — read them in the licensed standard.
The incident-energy method and the PPE-category method are distinct routes in
NFPA 70E; the engine implements the incident-energy → category mapping.

## How the skill uses this fragment
- Grounds arc-flash assessment work and any energized-electrical-work analysis;
  the calculated cal/cm² and boundary come from the engine, never invented.
- Missing inputs (gap, working distance, electrode config, clearing time) are
  recorded as `[GAP]`, never assumed.
