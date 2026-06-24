<!-- KB-SNIP-LOGISTICS-CLAUSE-MAP -->
# hse-logistics-transport clause cross-walk — standard → artifact → owning skill

**Fragment ID:** `KB-SNIP-LOGISTICS-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** standard → artifact → skill cross-walk (CONV-10) for
`hse-logistics-transport`: which logistics skill / artifact owns each driver-hours
and warehouse standard. Every logistics skill's `kb-selection` references it so a
user asking "which skill covers X?" is routed consistently, and each skill knows
which sibling owns an adjacent duty. Single source, never duplicated into per-skill
`references/`.

> Source: FMCSA HOS 49 CFR 395 + EU Reg 561/2006 + BS EN 15635:2008 / SEMA + OSHA 1910.178 / PUWER / HSE L117 + Motor Transport Workers Act 1961 · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the logistics standard → artifact → skill cross-walk

| Standard / clause | Artifact | Owning hse-logistics-transport skill |
|---|---|---|
| **FMCSA HOS 49 CFR 395** / **EU Reg 561/2006** (`KB-REG-FMCSA-HOS`) | driver fatigue / hours-of-service management plan | `driver-fatigue-management` (LOG-01) |
| **NAFMP FRMS** layering (`KB-SNIP-FATIGUE-FRMS`) | fatigue-control hierarchy (schedule-redesign-first) | `driver-fatigue-management` (LOG-01) |
| **BS EN 15635:2008 / SEMA** (`KB-STD-EN15635-SEMA`) | racking inspection regime + SEMA RAG action | `warehouse-racking-mhe-safety` (LOG-02) |
| **OSHA 1910.178 / PUWER / HSE L117 / HSG136** (`KB-REG-MHE-PIT`) | MHE competence + engineered pedestrian-vehicle segregation | `warehouse-racking-mhe-safety` (LOG-02) |
| racking/MHE control hierarchy (`KB-SNIP-RACKING-MHE`) | design/inspection/segregation-first gate | `warehouse-racking-mhe-safety` (LOG-02) |

## Engine + cross-bundle pointers
- **Hours-of-service computation** runs on the SUB-03 `fatigue.py` engine
  (FMCSA + EU 561), **not** a KB calculation — LOG-01 owns the engine call.
- **Road-safety KPIs** are the single home of `KB-DATA-ROAD-SAFETY-INDICATORS`
  (LEAD-06, ISO 39001:2012) — logistics skills **cross-reference**, they do not
  rebuild it.
- **India** statutory content defers to the `hse-india` engine via
  `KB-REG-IN-MTW` (state detection mandatory; no national form minted).

## How every logistics skill uses this fragment
Each skill references `KB-SNIP-LOGISTICS-CLAUSE-MAP` in its `kb-selection` so the
bundle presents one consistent standard → artifact → skill map. No skill restates
the cross-walk in its own body (anti-drift).
