# Methodology — Pre-Construction Information (PCI) compilation (CDM 2015 Reg 4)

The PCI is **information assembly + gap documentation, not calculation** — there is no risk
matrix in this skill (the significant hazards it surfaces are scored downstream in the CPP /
RAMS). The method is grounded in the **L153 Appendix-1 PCI content checklist**
(`KB-SNIP-PCI-CHECKLIST`) and the **client's Reg 4 duty** (`KB-REG-CDM2015`). Its single
lever is **gap discipline**: every missing existing-structure source is a documented `[GAP]`
with an owner + date, never silently omitted.

## Step 1 — De-identify the inputs (FIRST)
Run the `deid` block + `references/deid-checklist.md` before any drafting. Existing-structure
surveys routinely name an **occupier / resident with a health or vulnerability detail** — scrub
to role labels; a leak is an auto-fail. Set the **restricted-distribution flag** where the
pack carries sensitive site detail. The user-supplied gap-action owners + client/principal-
designer duty-holders stay named (a legitimate record).

## Step 2 — Inventory the information sources (Q2)
For each PCI content head in `KB-SNIP-PCI-CHECKLIST` — **existing structure · services ·
ground · surroundings · significant hazards** — record **what is known versus what is a
documented gap**. The inventory is the spine of the pack; nothing is left implicit.

## Step 3 — Capture the existing-structure hazard information
- **Asbestos / ACMs & hazardous materials** — survey status (present-and-surveyed,
  presumed-pending-survey, or `[GAP]`); never silently absent on a refurbishment/demolition.
- **Buried & overhead services** — electricity, gas, water, telecoms; location & isolation, or
  a `[GAP]`.
- **Ground conditions** — geotechnical / contamination / water table / previous use, or a
  `[GAP]`.
- **Structural form & stability** — drawings / as-builts / structural surveys, or a `[GAP]`.
- **The existing health & safety file** — its content, or a `[GAP]`.

Each is **cited to its stated source**; flag `[ASSUMPTION]` / `[GAP]` where uncertain — **never
invent a survey result**.

## Step 4 — Document the surroundings (Q3)
Adjacent occupancies, boundaries, access/egress, the public interface, neighbouring activities.

## Step 5 — Build the information-gaps register (the gap-discipline lever)
**Every missing source becomes an explicit register row** stating the gap and the assumption
carried in its place. A PCI that drops a missing asbestos survey instead of flagging it is a
**defensibility failure** — the register is what makes the unknowns visible to the designers
and contractors.

## Step 6 — Turn every gap into an owned/dated action (`smart_actions`)
For each `[GAP]` produce a SMART action via `smart_actions.validate_register`: specific,
**assignable (named owner / role)**, **time-bound (ISO due date)**, linked to the gap. Any
action missing an owner, a valid date, or a gap link is **invalid** and must be fixed — no
anonymous gaps, no "ASAP". An information gap that blocks construction (e.g. an outstanding
asbestos survey before strip-out) is flagged as a **hold-point**.

## Step 7 — Cross-reference the CDM document chain (loose coupling)
Add the one-line **PCI → CPP → H&S File** (Reg 4 → 12 → 12(5)) cross-reference sourced from
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **without assuming the CPP or H&S File skill ran**. State
the **client's Reg 4 duty and timing** (as soon as practicable; before appointments/start);
omitting it is a `regulatory_citation_accuracy` hard-fail.

## Step 8 — Validate & assemble
Validate against `references/QUALITY_CHECKLIST.md`, then build
`assets/pre-construction-information.report.json` and render via the `report-output` block.

## Jurisdiction
- **UK** — CDM 2015 Reg 4 + L153 Appendix 1 (`KB-REG-CDM2015`).
- **USA** — 29 CFR 1926 site-condition disclosure equivalents (`KB-REG-OSHA1926`).
- **India** — BOCW pre-work site information; **defers to `hse-india` / `bocw-compliance`**,
  mandatory state detection, literal `[GAP]`, **never a minted national form number**.
