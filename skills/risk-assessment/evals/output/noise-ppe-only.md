# Risk Assessment — Press-Shop Noise Exposure, Line 2 (PPE-only proposal escalated)

**Assessment type:** Issue-based (the noise hazard specifically).
**Activity:** Operating the mechanical power-press line during a production run — load blank -> press stroke -> eject -> stack. Continuous high-noise environment, measured ~92 dB(A) at the operator position over an 8-hour shift.
**Site:** Press shop, line 2. **Jurisdiction:** UK. **Industry:** Manufacturing — metal pressing.
**Exposed parties:** Own workers (the press operators, the stackers).
**Scoring engine:** org 5x5 matrix (multiply, score 1-25; bands Low 1-4 / Medium 5-9 / High 10-15 / Critical 16-25), per `risk_matrix.score`.
**Standard basis:** planning of controls per ISO 45001 clause 6.1.2; control-ranking discipline per KB-SNIP-HOC; defensible action assignment per KB-SNIP-DEFENSIBILITY.

> **Disclaimer.** Decision-support output. Must be reviewed and signed off by a competent person before use. Not legal advice.

## 1. De-identification status
De-id pass ran FIRST. No personal identifiers were present; personnel are carried as role labels only (the press operators, the stackers, Plant Manager, Maintenance Lead, the occupational-health adviser).

## 2. Hazard identification
| # | Hazard | Mechanism |
|---|--------|-----------|
| N1 | Noise-induced hearing loss (NIHL) | Sustained ~92 dB(A) exposure over an 8-hour shift at the press operator position; cumulative, irreversible cochlear damage; tinnitus. |

[GAP] No noise dosimetry by task element supplied; the ~92 dB(A) area figure is treated as the operator-position exposure pending a dosimetry survey (action N-A1). [ASSUMPTION] Exposure is daily and continuous across the production run.

## 3. Initial risk score (pre-control)

The intake proposes ONLY hearing protection (disposable ear plugs). Ranking the proposed treatment with `controls.rank_controls` returns **`ppe_admin_only = True`** and the flag *"PPE/admin-only — justify why higher-order controls aren't reasonably practicable"*. **This treatment is INADEQUATE as the sole control** — PPE sits at the BOTTOM of the hierarchy and relies on perfect, sustained worker compliance to attenuate an irreversible hazard.

| Hazard | Likelihood | Severity | Score (L x S) | Band | Band action |
|--------|-----------|----------|---------------|------|-------------|
| N1 NIHL (ear plugs only) | 4 (Likely) | 4 (Major) | 16 | Critical | Intolerable — work must not start or continue until risk is reduced |

## 4. Ranked controls — full hierarchy of controls (PPE-only ESCALATED)

The PPE-only proposal is rejected as the sole control. Higher-order controls are added so the treatment is no longer PPE-only; controls are ranked highest-order first and tier-tagged to hazard N1.

| Tier | Control | Why above PPE |
|------|---------|----------------|
| Elimination | Where a press operation can be automated/de-manned (robotic load/eject for the highest-volume jobs), remove the operator from the noise field entirely. | Removes the exposure rather than attenuating it. |
| Substitution | Substitute quieter tooling/process for the noisiest jobs — progressive die / servo (hydraulic) press in place of the mechanical flywheel press, low-noise die sets, damped tooling. | Reduces noise AT SOURCE; not compliance-dependent. |
| Engineering | Acoustic enclosure of the press; vibration damping of the bolster and die; anti-vibration mounts; close-fitting guarding lined with acoustic absorber; acoustic screens between line 2 and adjacent positions; LEV ducting silencers where pneumatic ejection contributes. | Attenuates noise at/near source for everyone, independent of worker behaviour. |
| Administrative | Job rotation to cap individual daily noise dose; mark a hearing-protection zone; reduce time at the press position; toolbox brief on NIHL; audiometry surveillance via the occupational-health adviser. | Reduces exposure DURATION; supports, does not replace, the above. |
| PPE | Hearing protection (ear plugs / ear defenders) selected to the residual exposure, fit-tested and maintained — retained as the LAST line, not the primary control. | Last line only; relies on correct, continuous use. |

**ppe_admin_only resolution:** with the Substitution and Engineering controls added, the treatment now contains higher-order controls; `controls.ppe_admin_only` clears. Where a specific legacy press cannot be enclosed or substituted in the near term, the explicit justification — *"higher-order controls not reasonably practicable on press [unit] because [structural/feed-access constraint]; interim PPE + rotation + audiometry applied; substitution scheduled at next die-set refresh"* — is recorded against that unit and surfaced (not hidden) in the report.

## 5. Residual risk (post-control re-score) — initial -> residual movement

| Hazard | Initial score / band | Residual score / band | Movement |
|--------|----------------------|------------------------|----------|
| N1 NIHL | 16 Critical (ear plugs only) | L2 x S4 = 8 Medium | Critical -> Medium (engineering enclosure + damping reduce noise at source; PPE + rotation hold the residual ALARP) |

Residual scoring uses the same `risk_matrix.score` engine; the values are risk scores (band movement), not injury counts. Full residual reduction to Low is contingent on the enclosure/substitution actions (N-A2, N-A3) completing — until then the interim residual is held at Medium with PPE + rotation + surveillance.

## 6. SMART actions (defensible — named role-label owner + ISO due date + hazard link + review trigger)

| ID | Action | Hazard | Owner (role label) | Due (ISO) | Review trigger |
|----|--------|--------|--------------------|-----------|----------------|
| N-A1 | Commission task-element noise dosimetry survey of line 2 | N1 | Plant Manager | 31 Jul 2026 | On any tooling change; annually |
| N-A2 | Design & install acoustic enclosure + bolster/die damping on the line-2 press | N1 | Maintenance Lead | 31 Oct 2026 | Post-install verification dosimetry |
| N-A3 | Evaluate quieter press/tooling (servo press, damped die sets) at next die-set refresh | N1 | Plant Manager | 15 Dec 2026 | Procurement / refresh cycle |
| N-A4 | Implement job rotation to cap individual daily noise dose; mark hearing-protection zone | N1 | Plant Manager | 15 Jul 2026 | On roster change |
| N-A5 | Enrol exposed roles in audiometric surveillance via occupational-health adviser | N1 | Plant Manager | 15 Aug 2026 | Annual audiometry |

## 7. Critic / QA pass
The Critic pass confirms: the PPE-only proposal was flagged (`ppe_admin_only = True`), higher-order controls (Substitution + Engineering) were ADDED above PPE, residual risk was re-scored Critical -> Medium, and every action carries a named owner + ISO due date + hazard link. This artifact is NOT shipped as ear-plugs-alone.

## 8. Branded report
A branded `report.json` is emitted and rendered to DOCX + PDF (`generate_report.py --formats docx,pdf`) using the site `brand.yaml` (Eyekyam default where unset). The ranked-controls table and the PPE-only-escalation note populate the report; the justification (where any unit retains interim PPE) is surfaced, not suppressed.

## 9. Review
Review trigger: on completion of N-A2/N-A3 (post-install verification dosimetry), on any tooling change, and at 12 months. Competent-person sign-off required before circulation.
