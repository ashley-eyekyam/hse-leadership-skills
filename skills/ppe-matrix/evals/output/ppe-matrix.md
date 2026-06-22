<!-- CANDIDATE golden output for ppe-matrix (MFG-04). Generated from eval case 1's scenario
     (line-3 fettling cell, fettler + grinder roles, Plant 3). It demonstrates the controls-first
     gate: PPE is specified ONLY for the residual hazard surviving the higher-order controls
     (eye/face, noise, dust), and the hand/arm hazard — which had NO higher-order control
     recorded — is returned as a CONTROLS-FIRST FLAG with the PPE row WITHHELD (not invented).
     The EN/ANSI conformity standards are cited with a [year] placeholder (the conformity-year is
     the user's to confirm against the in-force edition). NOT owner-LOCKED — the owner reviews +
     locks in P17. -->

# PPE Matrix — Line-3 Fettling Cell (fettler + grinder roles, Plant 3)

*Decision-support only. A competent person must review and sign off this PPE hazard assessment.
Special-category respiratory medical-clearance / fitness data — reported by role with `<5`
small-cell suppression; the re-identification key is held separately.*

## 1. Scope & tasks

De-identification ran first: worker names and the individual respiratory medical-clearance /
fitness note were scrubbed to role labels; no named clearance note and no `<5` health-outcome
cell appears below.

- **Scope:** line-3 fettling cell — fettler + grinder roles, Plant 3 (task-specific; not a
  site-wide PPE sheet).
- **Tasks:** manual grinding and dry deburring of cast components.

## 2. Hazard assessment by body region (OSHA 1910 Subpart I)

| Body-region hazard | Risk | Basis |
|---|---|---|
| Eye/face — grinding spark & fragment | High | OSHA 1910.133; task observation |
| Hearing — sustained grinding noise | Medium | OSHA Subpart I; area noise survey |
| Respiratory — metal/silica dust | High | OSHA Subpart I; dust monitoring `[GAP — sample pending]` |
| Hand/arm — abrasion & vibration | Medium | OSHA 1910.138; task observation |

## 3. Higher-order controls considered — the controls-first gate

`controls.validate_treatment` was run for **each** body-region hazard before any PPE row. PPE is
specified **only** for the residual hazard surviving the higher-order controls; a hazard with no
higher-order control recorded is a **controls-first flag** and its PPE cell is **withheld**.

| Body-region hazard | Higher-order controls applied / justified | Gate outcome |
|---|---|---|
| Eye/face — sparks/fragments | Fixed grinding screen + tool-mounted guard (engineering); rotation (administrative) | Residual hazard remains → **PPE specified** |
| Hearing — grinding noise | Damped grinding bench + enclosure panels (engineering); rotation (administrative) | Residual hazard remains → **PPE specified** |
| Respiratory — metal/silica dust | LEV at the grinding bench (engineering); wet-fettling substitution under trial (substitution) | Residual hazard remains → **PPE specified** |
| Hand/arm — abrasion/vibration | **None recorded** | **CONTROLS-FIRST FLAG** — higher-order controls not considered; assess + apply (anti-vibration mounts, low-vibration tools, exposure limits) before specifying PPE. **PPE row WITHHELD.** |

> **Controls-first flag (hand/arm):** no PPE row is issued for this hazard until its higher-order
> controls are assessed and applied or justified. PPE-first is not permitted — this is the failure
> mode the matrix exists to prevent.

## 4. PPE selection matrix (residual hazard → PPE type + cited standard)

| Task / role | Residual hazard | PPE type | Conformity standard (cite + year) |
|---|---|---|---|
| Fettling/grinding — grinder | Eye/face spark & fragment (residual after screen/guard) | Safety glasses + face shield over | EN 166 / ANSI Z87.1, `[year]` |
| Fettling/grinding — grinder | Noise (residual after damping/enclosure) | Ear defenders selected to residual exposure | EN 352 / ANSI S3.19, `[year]` |
| Dry fettling — fettler | Metal/silica dust (residual after LEV) | FFP3 / N95 respirator (fit-test + clearance, role level) | EN 149 / NIOSH 42 CFR 84, `[year]` |
| Hand/arm — both roles | *[controls-first flag — PPE withheld]* | — not specified until higher-order controls applied — | — (gate not passed) |

No protection level is asserted without its cited conformity standard + year.

## 5. Fit, compatibility & training notes

- Respiratory PPE (FFP3/N95) requires fit-testing and medical clearance — recorded at **role
  level** only; no named worker's clearance result is carried here (`<5` cells suppressed).
- Face shield + safety glasses + ear defenders + respirator checked for mutual compatibility (no
  respirator seal break from eyewear arms).
- PPE training (donning/doffing, inspection, replacement) is administrative support — **not** a
  substitute for the higher-order controls.

## 6. Written hazard-assessment certification (OSHA 1910.132(d)(2))

| Certification field | Value |
|---|---|
| Workplace assessed | Plant 3 — line-3 fettling cell (fettler + grinder roles) |
| Hazards assessed | Eye/face, hearing, respiratory, hand/arm (OSHA 1910 Subpart I) |
| Certifying competent person (role) | Site HSE Manager (named role; no individual identifier) |
| Certification date | 2026-06-22 |

The written certification is **mandatory and is never omitted**.

## 7. Owned & dated actions

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Assess + apply higher-order controls for the hand/arm hazard (anti-vibration mounts, low-vibration tools, exposure limits) — clears the controls-first flag | P1 | Process Engineer | 2026-07-06 |
| Complete respirator fit-testing + medical clearance for the fettler role (role-level record) | P1 | Occupational Health | 2026-07-13 |
| Collect the pending dust sample to confirm the respiratory residual (`[GAP]` closed) | P2 | HSE Manufacturing | 2026-07-20 |

## 8. Review & sign-off

- Review trigger: on task change / on PPE change / annual — whichever is first.
- Regulatory basis: OSHA 29 CFR 1910 Subpart I (1910.132 + .133/.135/.136/.138); ISO 45001
  §6.1.2 / §8.1.2; PPE conformity standards (EN / ANSI) cited per row.
- Decision-support only — a competent person must review before use.
