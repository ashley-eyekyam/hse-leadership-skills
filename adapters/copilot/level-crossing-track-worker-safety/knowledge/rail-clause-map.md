<!-- KB-SNIP-RAIL-CLAUSE-MAP -->
# hse-rail clause cross-walk — standard → artifact → owning skill

**Fragment ID:** `KB-SNIP-RAIL-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** standard → artifact → skill cross-walk (CONV-10) for `hse-rail`:
which rail skill / artifact owns each ROGS SMS element, the CSM-RA method and the
level-crossing/track-worker standard. Every rail skill's `kb-selection` references it
so a user asking "which skill covers X?" is routed consistently, and RAIL-02 knows
it **references** RAIL-01's SMS rather than rebuilding it. Single source, never
duplicated into per-skill `references/`.

> Source: Railways and Other Guided Transport Systems (Safety) Regulations 2006 (SI 2006/599) + ORR Guide to ROGS + Reg (EU) 402/2013 CSM-RA + NR/L2/OHS/019 · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the rail standard → artifact → skill cross-walk

| Standard / element | Artifact | Owning hse-rail skill |
|---|---|---|
| **ROGS SMS element set** (policy, accountabilities, risk-control, CSM-RA interface, competence/Sentinel, asset/ECM maintenance, emergency, monitoring/audit, continuous improvement) (`KB-REG-ROGS`) | safety management system (for acceptance, not "accepted") | `rail-safety-management-system` (RAIL-01) |
| **ROGS** safety certificate / safety authorisation / Part-3 verification (`KB-REG-ROGS`) | the application pack — **references RAIL-01's SMS, never rebuilds it** | `safety-authorisation` (RAIL-02) |
| **Reg (EU) 402/2013 CSM-RA** (`KB-REG-CSM-RA`) | significance test + risk-acceptance + AsBo assessment | RAIL-01 (SMS change element) + RAIL-02 (change evidence) |
| **NR/L2/OHS/019 + ORR LX guidance + LXRMTK** (`KB-REG-LX-TRACKWORKER`) | level-crossing remediation + track-worker SSOW | `level-crossing-track-worker-safety` (RAIL-03) |
| **ALCRM** band (`KB-DATA-ALCRM-BANDS`) | crossing risk-band classification (band recorded, not recomputed) | `level-crossing-track-worker-safety` (RAIL-03) |
| crossing/track control hierarchy (`KB-SNIP-LX-HIERARCHY`) | closure/separation-first gate | `level-crossing-track-worker-safety` (RAIL-03) |

## Route discipline + cross-bundle pointers
- **Route test (eval-enforced):** transport operator (mainline) → **safety
  certificate**; infrastructure manager (mainline) → **safety authorisation**;
  non-mainline (tram/metro/heritage) → **Part-3 safety verification**. ORR is the
  Safety Authority; **never emit "accepted by ORR"** — the application is *for
  submission*, acceptance is the authority's act.
- **RAIL-02 references RAIL-01's SMS** (does not rebuild it) — sibling-overlap
  discipline (CONV-12).
- **India** statutory content defers to the `hse-india` engine via
  `KB-REG-IN-RAIL` (state detection for non-railway depot; no national form minted).

## How every rail skill uses this fragment
Each skill references `KB-SNIP-RAIL-CLAUSE-MAP` in its `kb-selection` so the bundle
presents one consistent standard → artifact → skill map. No skill restates the
cross-walk in its own body (anti-drift).
