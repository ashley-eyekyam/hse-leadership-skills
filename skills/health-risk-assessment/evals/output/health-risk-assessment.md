# Occupational Health Risk Assessment — Plant 3 (Press shop · Degrease line · Despatch bay)

*Decision-support only. A competent person (occupational hygienist / OH physician) must
review and sign off this assessment. Special-category health data — reported by SEG/role with
`<5` small-cell suppression; the re-identification key is held separately.*

## 1. Scope & similar-exposure groups (SEGs)

Assessed per ISO 45001 §6.1.2. Three SEGs, each named by task/role and agent:

- **Press-shop operator SEG** — mechanical power press, line 2 (noise).
- **Degrease-line SEG** — solvent (toluene) vapour, manual degreasing (inhalation).
- **Despatch-bay picker SEG** — manual handling of palletised cartons, floor-to-conveyor (ergonomics).

De-identification ran first: worker names and individual surveillance results were scrubbed to
SEG/role labels; no individual audiometry result and no `<5` health-outcome cell appears below.

## 2. Hazards & exposure characterisation

| SEG / agent | Exposure (measured/estimated) | Route |
|---|---|---|
| Press-shop operator SEG / noise | 92 dB(A) LEP,d (measured dosimetry) | Auditory |
| Degrease-line SEG / toluene | ~70 ppm 8h TWA (estimated, modelled) | Inhalation |
| Despatch-bay picker SEG / manual handling | 18 kg lift, floor origin, 4 lifts/min, 8h | Musculoskeletal |

## 3. Exposure-vs-OEL comparison

| SEG / agent | Exposure | OEL / WEL / PEL | Authority + year | Status |
|---|---|---|---|---|
| Press-shop operator SEG / noise | 92 dB(A) LEP,d | 85 dB(A) upper action value | UK Control of Noise at Work Regulations 2005 | **Above** the upper action value |
| Degrease-line SEG / toluene | ~70 ppm 8h TWA | 50 ppm TWA (8h) | UK HSE EH40/2005 WEL, 2020 amendment | **Above** the WEL |

Every exposure is compared to a cited OEL/WEL/PEL (authority+year) resolved from
`KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS` — the single OEL source, no parallel table.

## 4. Ergonomic scores (tool-named — deterministic `ergonomics` engine)

Despatch-bay picker SEG, scored with the engine (`ergonomics.to_report_blocks()` `[metrics,
table]` pairs — engine output, not narrated):

**RULA** — grand score **6**, action level **3** ("Investigation and changes are required soon").

| Step | Value |
|---|---|
| posture_a | 4 |
| score_a | 6 |
| posture_b | 4 |
| score_b | 5 |

**REBA** — final score **9**, action level **4** ("High risk — investigate and implement change").

| Step | Value |
|---|---|
| posture_a | 5 |
| score_a | 6 |
| posture_b | 5 |
| score_b | 6 |
| score_c | 8 |

**NIOSH lifting equation** — Recommended Weight Limit **5.39 kg**, Lifting Index **3.34**
(LI > 1.0 → lifting demand exceeds the recommended limit).

| Step | Value |
|---|---|
| HM | 0.83 |
| VM | 0.90 |
| DM | 0.86 |
| AM | 0.90 |
| FM | 0.45 |
| CM | 0.90 |

## 5. Risk rating (residual)

| SEG | Health hazard | Initial | Residual (post-control) | Movement |
|---|---|---|---|---|
| Press-shop operator SEG | Noise-induced hearing loss | High | Medium | ↓ after enclosure |
| Degrease-line SEG | Solvent inhalation | High | Medium | ↓ after substitution + LEV |
| Despatch-bay picker SEG | Manual-handling MSD | High | Medium | ↓ after lift redesign |

## 6. Controls (hierarchy of controls — substitution/engineering before PPE AND surveillance)

| Control | Tier | Owner |
|---|---|---|
| Substitute an aqueous degreaser for toluene | Substitution | Process Lead |
| Acoustic enclosure on press line 2; LEV on the degrease line; powered lift assist on the despatch bay | Engineering | Engineering Lead |
| Restricted-access exposure zones + job rotation | Administrative | Shift Manager |
| Hearing protection + RPE as a backstop only | PPE | HSE Lead |

> Hearing protection and audiometry are **not** controls — substitution and engineering
> precede PPE and precede surveillance. A hearing-protection-only plan would be flagged.

## 7. Health-surveillance schedule (OEL-linked)

| SEG | Trigger | Surveillance | Cadence | Owner |
|---|---|---|---|---|
| Press-shop operator SEG | Exposure ≥ upper action value | Audiometry | Baseline + annual | OH Physician |
| Degrease-line SEG | Exposure > WEL | Respiratory / biological monitoring | Per regime | OH Physician |
| Despatch-bay picker SEG | LI > 1.0 / RULA action level 3 | MSD symptom surveillance | Baseline + on report | OH Nurse |

Surveillance outcomes are reported by SEG with `<5` small-cell suppression; no individual
result is circulated.

## 8. Recommendations (SMART — named owners + ISO dates)

| Action | Priority | Owner | Due |
|---|---|---|---|
| Install the acoustic enclosure on press line 2 | P1 | Engineering Lead | 2026-08-01 |
| Trial the aqueous-degreaser substitution | P1 | Process Lead | 2026-07-15 |
| Fit powered lift assist on the despatch bay | P1 | Engineering Lead | 2026-08-10 |
| Baseline audiometry for the press-shop SEG | P2 | OH Physician | 2026-07-30 |

## 9. Review & sign-off

Review on exposure change or on a surveillance trigger. Regulatory basis: ISO 45001 §6.1.2 +
the UK surveillance regime (COSHH 2002 / Control of Noise at Work Regs 2005). Decision-support
only — a competent person (occupational hygienist / OH physician) must review and sign off.

---
*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
