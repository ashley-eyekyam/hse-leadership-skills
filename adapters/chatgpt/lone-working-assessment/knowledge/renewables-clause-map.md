<!-- KB-SNIP-RENEWABLES-CLAUSE-MAP -->
# hse-renewables clause cross-walk — standard → artifact → owning skill

**Fragment ID:** `KB-SNIP-RENEWABLES-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** standard → artifact → skill cross-walk (CONV-10) for
`hse-renewables`: which renewables skill / artifact owns each work-at-height,
lone-working and weather standard. Every renewables skill's `kb-selection`
references it so a user asking "which skill covers X?" is routed consistently, and
each skill knows which sibling owns the shared rescue snippet. Single source, never
duplicated into per-skill `references/`.

> Source: Work at Height Regulations 2005 (SI 2005/735) reg 4/6/7 + GWO BST + HSE INDG73 / BS 8484:2022 + ISO 45001 cl 6.1.2 / BS 7121-1 (2016) weather thresholds · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the renewables standard → artifact → skill cross-walk

| Standard / clause | Artifact | Owning hse-renewables skill |
|---|---|---|
| **WAH 2005 reg 4 / 6 / 7** (`KB-REG-WAH2005`) | work-at-height plan + mandatory rescue plan | `wind-turbine-work-at-height-rescue` (REN-01) |
| **GWO BST / First Aid / ART** (`KB-STD-GWO-WAH-RESCUE`) | climb-team competence + timed team-owned rescue | `wind-turbine-work-at-height-rescue` (REN-01) |
| rescue discipline (`KB-SNIP-RESCUE-PLAN`) — **shared REN-01 + REN-02** | rescue-plan-mandatory gate | REN-01 + REN-02 |
| **HSE INDG73 (rev 4)** (`KB-REG-LONE-WORKING`) + **BS 8484:2022** (`KB-STD-BS8484`) | lone-working RA + check-in/escalation + device service | `lone-working-assessment` (REN-02) |
| check-in/escalation hierarchy (`KB-SNIP-CHECKIN-ESCALATION`) | scheduled-check-in + escalation gate | `lone-working-assessment` (REN-02) |
| **ISO 45001 cl 6.1.2 + BS 7121-1 (2016)** weather method (`KB-DATA-WEATHER-THRESHOLDS`) | dynamic weather RA (threshold→action→re-assessment) | `weather-dynamic-risk-assessment` (REN-03) |
| dynamic-RA hierarchy (`KB-SNIP-DYNAMIC-RA`) | threshold/action/re-assessment gate at hub height | `weather-dynamic-risk-assessment` (REN-03) |

## Currency + cross-bundle pointers
- **Crane man-riding ceiling = BS 7121-1 (2016 edition) 16 mph / 7 m/s** — never the
  2006 edition. The ≈15 m/s hub-height tower-top cut-off is a proposed-and-confirmed
  industry baseline (`[ASSUMED]`), never a hard citation.
- **Renewables hazards** are the single home of `KB-HAZ-RENEWABLES` (P11) — all three
  renewables skills **cross-reference** it; it is not rebuilt here.
- **India** statutory content defers to the `hse-india` engine via
  `KB-REG-IN-RENEWABLES` (state detection mandatory; no national form minted).

## How every renewables skill uses this fragment
Each skill references `KB-SNIP-RENEWABLES-CLAUSE-MAP` in its `kb-selection` so the
bundle presents one consistent standard → artifact → skill map. No skill restates
the cross-walk in its own body (anti-drift).
