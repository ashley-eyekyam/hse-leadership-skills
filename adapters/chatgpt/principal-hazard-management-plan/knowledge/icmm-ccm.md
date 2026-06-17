<!-- KB-STD-ICMM-CCM -->
# ICMM Critical Control Management (CCM) — framing map (jurisdiction-independent)

**Fragment ID:** `KB-STD-ICMM-CCM`
**What this is:** a copyright-safe **framing map** for the ICMM Critical Control
Management methodology — the *structure* of CCM (material unwanted events,
critical-control identification, control criticality, performance requirements,
verification activities + frequencies, accountabilities) plus the **mining
principal-hazard taxonomy** this pack owns. It is mining-authored framing, like
the ISO clause maps.
**What this is NOT:** a reproduction of ICMM's guidance text (the ICMM
publications are copyrighted; the user holds their own licensed copy — cite the
method structure + topics only), and **NOT a bowtie engine**. For the **bowtie
diagram technique itself** (top event → threats/preventive barriers → consequences/
mitigative barriers, with barrier performance standards) this fragment
**references `KB-STD-CCPS-BOWTIE`** (the shared method map) and the
**`bowtie-builder`** facilitator (owned by hse-process, bundled into hse-mining) —
it does NOT redefine the bowtie. CCM is the mining overlay *on top of* that shared
technique.

> Source: ICMM Critical Control Management — method structure (user holds the guidance) · Year: 2026 · Reviewed: 2026-05-15 · Volatile: false (multi-year revision cycle, like the ISO standards).

ICMM CCM is the global hard-barrier framing for mining principal hazards: it
identifies the **critical controls** — the controls that, if they fail or are
absent, allow a **material unwanted event** to occur or escalate — and sets
explicit performance requirements + verification for each. It is
**jurisdiction-independent** (`jurisdiction: [All]`, like the ISO standards), so a
mine in any country can apply it; the India statutory layer (`KB-REG-IN-MINES-ACT`
/ `KB-REG-IN-DGMS`) is applied alongside it where the mine is in India.

## CCM method structure → element

| CCM element | Topic | What the skill produces |
|---|---|---|
| Material unwanted event (MUE) | the credible high-consequence event for a principal hazard | named, specific (from the taxonomy below) |
| Critical control | a control that, if absent/failed, lets the MUE occur/escalate | identified + flagged critical (vs. non-critical) |
| Control criticality | why this control is critical (not just present) | justified against the MUE pathway |
| Performance requirement | the standard the control must meet to be effective | stated, measurable |
| Verification activity + frequency | how/when effectiveness is confirmed | activity + frequency + responsible role |
| Accountability | the named role accountable for the control | role label (de-identified) |

For the **bowtie diagram** (threats → preventive barriers → top event →
consequences → mitigative barriers, barrier performance standards): reference
`KB-STD-CCPS-BOWTIE` and use the **`bowtie-builder`** facilitator — then overlay
the mining CCM criticality. Hierarchy-of-controls ranking applies
(`KB-SNIP-HOC`): a PPE/admin-only "critical control" for a principal hazard is
flagged, not accepted.

## Mining principal-hazard taxonomy (mining-owned)

The principal hazards a CCM / PHMP addresses (full library + benchmark figures in
`KB-DATA-MINING-HAZARDS`):

- ground / strata failure (roof/side/highwall instability)
- inrush / inundation (water, slurry, gas)
- fire / explosion (coal-dust, methane/firedamp, diesel, conveyor)
- ventilation failure (irrespirable / flammable atmosphere)
- mobile-plant / vehicle interaction (haul-truck, light-vehicle, pedestrian)
- fall from height (highwall, shaft, raise)
- hazardous energy (electrical, stored, isolation)
- respirable dust / occupational health exposure

## How the skills use this fragment
- `icmm-critical-control-management` structures the CCM for a named MUE
  (critical-control identification → performance requirement → verification →
  accountability) and **references `bowtie-builder`** for the diagram (never
  re-authors it).
- `principal-hazard-management-plan` takes a named principal hazard from the
  taxonomy, runs the HIRA structure, and links its control suite to the critical
  controls CCM identifies.
- Both are `status: assistive` — they structure the multidisciplinary mine
  workshop; the mine team owns the engineering judgement and the live verification.
