<!-- KB-SNIP-HEALTHCARE-CLAUSE-MAP -->
# hse-healthcare clause cross-walk — ISO 45001 6.1.2 + clinical PPE-last hierarchy → owning skill

**Fragment ID:** `KB-SNIP-HEALTHCARE-CLAUSE-MAP`
**This is prompt text, applied by the model — not a generator.** It is the
**bundle-shared** (CONV-10) cross-walk for `hse-healthcare`: ISO 45001:2018 clause
**6.1.2** (hazard identification & risk assessment) plus the clinical **PPE-last**
hierarchy of controls, mapped to the five healthcare skills. Every healthcare
skill's `kb-selection` references it so the bundle routes consistently and applies
one PPE-last spine.

> Source: ISO 45001:2018 (clause 6.1.2 hazard-id/risk-assessment) + the hierarchy of controls (`KB-SNIP-HOC`, PPE last) — bundle cross-walk · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the healthcare axis → owning skill

| Axis | Healthcare hazard | Owning hse-healthcare skill |
|---|---|---|
| ISO 45001 **6.1.2** + sharps engineering-first hierarchy | Bloodborne / needlestick exposure | `sharps-needlestick-management` (HC-01) |
| ISO 45001 **6.1.2** + IPC precautions by route | Infection transmission | `infection-control-plan` (HC-02) |
| ISO 45001 **6.1.2** + move-toward-zero handling | Patient-handling / MSD | `patient-handling-assessment` (HC-03) |
| ISO 45001 **6.1.2** + environmental/admin-before-reactive | Workplace violence | `workplace-violence-prevention` (HC-04) |
| ISO 45001 **6.1.2** + risk-group→BSL containment | Laboratory biological agents | `lab-biosafety-assessment` (HC-05) |

## The PPE-last spine (every skill applies it)
Each healthcare skill applies the hierarchy of controls — eliminate / substitute /
engineer the hazard first, then administrative controls, with **PPE always the
residual, documented last line** (`KB-SNIP-HOC`), never the headline control. A
treatment that leads with PPE (gloves/masks/respirators) without higher-order
controls is rejected.

## PHI / de-identification (every healthcare skill)
Patient and staff data is **de-identified** per the mandatory de-id block + the
healthcare PHI extension (in `references/deid-checklist.md`, NOT the block); small
populations are reported with **small-cell suppression** so no individual is
re-identifiable; the re-identification key is the competent person's, never an
emitted artifact.

## Adjacent pointers (not axis rows)
- **US grounding:** `KB-REG-OSHA-BBP` (BBP + Needlestick Act), `KB-REG-WPV-OSHA3148`
  (workplace violence). **EU/UK:** `KB-REG-EU-SHARPS-2010-32`, `KB-REG-UK-MHOR`.
- **Standards:** `KB-STD-IPC-CDC-WHO`, `KB-STD-SPHM`, `KB-STD-BIOSAFETY-BMBL-WHO`.
- **India** healthcare-waste content defers to the `hse-india` engine
  (`KB-REG-IN-BMW2016`; state detection mandatory; no national form numbers minted).

## How every healthcare skill uses this fragment
Each skill references `KB-SNIP-HEALTHCARE-CLAUSE-MAP` in its `kb-selection` so the
bundle presents one consistent hazard → skill map, the shared PPE-last spine, and
the PHI de-identification discipline. No skill restates the cross-walk in its own
body (anti-drift).
