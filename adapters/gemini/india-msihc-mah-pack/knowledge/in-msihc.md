<!-- KB-REG-IN-MSIHC -->
# India — MSIHC Rules 1989 (MAH identification + emergency plan map, legacy-first)

**Fragment ID:** `KB-REG-IN-MSIHC`
**What this is:** a copyright-safe **threshold → duty → artifact map** for the
Manufacture, Storage and Import of Hazardous Chemicals (MSIHC) Rules 1989 — Major
Accident Hazard (MAH) installation identification against the Schedule threshold
quantities, the on-site emergency plan, and the safety report — the cluster the
`india-msihc-mah-pack` skill reads. This is the **chemicals-owned** India fragment
(master-plan §5 single-source table: `KB-REG-IN-MSIHC` is authored here; PESO —
`KB-REG-IN-PESO` — is authored by `hse-process` and only referenced here).
**What this is NOT:** a reproduction of the Rules' Schedules or the threshold tables.
Cite the Rule / Schedule references only — never paste the statutory wording; the
user resolves the binding threshold and the state form from the source. **No
hard-coded national form number** is assumed — forms resolve **from this map +
`KB-REG-IN-STATEFORMS`** after **mandatory state detection**.

> Source: MSIHC Rules 1989 (under the Environment (Protection) Act / Factories Act) — Rule/Schedule structure (user holds the text) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: true (rules + the OSH-Code / Chemicals-Management transition drift; refresh on review).

MSIHC operates **with** the state machinery: MAH identification is against the
central Schedule threshold quantities, but the on-site emergency plan filing, factory
licensing interaction, and inspectorate are **state-administered**. The skill
therefore resolves the **site state** (mandatory — ask or infer-from-address then
**confirm before citing**) and appends the **OSH-Code transition note** (legacy-first:
the Code on Occupational Safety, Health and Working Conditions subsumes these
obligations state-by-state; most states have not switched). State-form interactions
resolve via `KB-REG-IN-STATEFORMS`. The PESO petroleum/explosives/SMPV licensing
pointers are read from **`KB-REG-IN-PESO`** (hse-process home; referenced, not
authored here).

## Threshold → duty → form → use

| Trigger | Duty | Form / instrument (resolve from this row + the state) | Grounds |
|---|---|---|---|
| Hazardous chemical ≥ Schedule threshold qty | MAH installation status | MAH notification to the State authority | india-msihc-mah-pack |
| MAH installation | On-site emergency plan | prepared + rehearsed; filed with the State factory inspectorate | india-msihc-mah-pack |
| MAH installation (upper threshold) | Safety report | safety report prepared + updated | india-msihc-mah-pack |
| Any hazardous-chemical handling | Safety data sheet + import notification | SDS per the Rules; import declaration | india-msihc-mah-pack; ghs-classification-sds-author |
| State-specific obligation | Factory licence / siting near MAH unit | state form via KB-REG-IN-STATEFORMS (state-detected) | india-msihc-mah-pack |
| OSH Code transition | Subsumes these obligations (state-by-state) | transition note appended (legacy-first) | india-msihc-mah-pack |

## How the skill uses this fragment
- `india-msihc-mah-pack` resolves the site inventory + Schedule thresholds → MAH
  yes/no verdict → the on-site emergency plan outline + safety-report outline + the
  state-resolved form, with the OSH-Code transition note.
- **State detection is mandatory** where the obligation is state-specific — ask or
  infer-from-address-then-confirm, never silently assume; the form is resolved from
  `KB-REG-IN-STATEFORMS`, never a hard-coded national number.
- Petroleum/explosives/gas/SMPV storage licensing pointers are read from
  `KB-REG-IN-PESO` (referenced; hse-process owns that fragment).
- An MAH threshold or form that cannot be resolved is `[GAP]`-flagged and routed to a
  competent person — never an invented threshold or form number.
