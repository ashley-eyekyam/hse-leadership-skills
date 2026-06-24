<!-- KB-SNIP-MARINE-CLAUSE-MAP -->
# hse-marine-offshore clause cross-walk — standard → artifact → owning skill

**Fragment ID:** `KB-SNIP-MARINE-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** standard → artifact → skill cross-walk (CONV-10) for
`hse-marine-offshore`: which marine skill / artifact owns each offshore safety-case,
dropped-object and emergency-response standard. Every marine skill's `kb-selection`
references it so a user asking "which skill covers X?" is routed consistently.
Single source, never duplicated into per-skill `references/`.

> Source: Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regs 2015 (SI 2015/398) Sch 6/7 + DROPS RP 2017 + PFEER 1995 (SI 1995/743) + SOLAS Ch III / LSA Code · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the marine standard → artifact → skill cross-walk

| Standard / clause | Artifact | Owning hse-marine-offshore skill |
|---|---|---|
| **SI 2015/398 Schedule 6** (production) / **Schedule 7** (non-production) (`KB-REG-OFFSHORE-SCR`) | offshore safety case (assistive assembly) | `offshore-safety-case` (MAR-01) |
| **DROPS RP 2017 / IADC Sec 16 / API RP 2D/54** (`KB-REG-DROPS`) | dropped-object survey + reliable-securing plan | `dropped-objects-prevention` (MAR-02) |
| DROPS impact-energy `m·g·h` method (`KB-DATA-DROPS-IMPACT`) | consequence-band classification (band recorded, not recomputed) | `dropped-objects-prevention` (MAR-02) |
| **PFEER 1995 (SI 1995/743) + HSE L65** (`KB-REG-PFEER`) | muster / TR-integrity / EER / reg-17 recovery plan | `marine-emergency-response` (MAR-03) |
| **SOLAS Ch III + LSA Code** (`KB-REG-SOLAS-LSA`) | survival-craft + station-bill (role-labelled) | `marine-emergency-response` (MAR-03) |
| EER hierarchy (`KB-SNIP-EER-MUSTER`) / dropped-objects gate (`KB-SNIP-DROPS-SECURING`) | escalation-prevention-first / securing-first control gates | MAR-03 / MAR-02 |

## Currency + cross-bundle pointers
- **Current safety-case regime = SI 2015/398** (implements EU Dir 2013/30/EU);
  **SCR 2005 (SI 2005/3117) is the named legacy reference only** — never cited as
  current.
- **MAR-01 is assistive:** it assembles the Schedule 6/7 argument, records external
  QRA figures with provenance, and **never computes QRA / asserts a barrier
  effective / emits "accepted or approved"** (acceptance is the competent
  authority's act).
- **India** statutory content defers to the `hse-india` engine via
  `KB-REG-IN-OFFSHORE` (state detection for shore-base; no national form minted).

## How every marine skill uses this fragment
Each skill references `KB-SNIP-MARINE-CLAUSE-MAP` in its `kb-selection` so the
bundle presents one consistent standard → artifact → skill map. No skill restates
the cross-walk in its own body (anti-drift).
