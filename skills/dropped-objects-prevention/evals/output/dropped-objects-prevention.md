# Dropped Objects Prevention — Platform Bravo drilling derrick (DROPS survey & register)

**Installation / area:** Platform Bravo, drilling derrick — monkeyboard to drill floor (UKCS)
**Scope:** DROPS survey · dropped-object register (static vs dynamic) · reliable-securing controls · exclusion zones
**Standards basis:** DROPS Recommended Practice (2017) + DROPS Reliable Securing · IADC HSE Guidelines Section 16 · API RP 2D / RP 54
**Classification:** Internal — competent-person (DROPS / dropped-objects SME) review required
**De-identification:** Every accountability is recorded by role label (DROPS Coordinator, Derrick Supervisor, OIM). A prior dropped-object struck-by incident is carried at role level; names, contact and payroll numbers were pseudonymised before drafting and the re-identification key is held separately.

---

## 1. Lead posture — reliable securing, not "hard hats below"

The treatment as proposed reduced the control to *"issue hard hats to everyone working below the derrick."* That PPE-led posture is **rejected**. The lead controls for every at-height object are:

1. **DROPS survey + reliable securing** — every at-height item carries a primary fixing **plus secondary retention** (tethering/lanyard) to a reliable-securing standard, recorded in the register.
2. **Exclusion zone** — a red zone below the at-height work so people are not under suspended or potential dropped objects during tripping.

Hard hats are the **residual** for persons who must enter the drill floor — they supplement the survey, securing and exclusion controls and are never the headline.

## 2. Dropped-object register

| Object / location | Taxonomy | Mass (kg, user) | Fall height (m, user) | Impact energy E≈m·g·h | Consequence band | Securing status |
|---|---|---|---|---|---|---|
| Fingerboard latch pin, monkeyboard | Static | 4 | 28 | ≈ 1098 J | Major (user DROPS Calculator band); licensed thresholds [GAP] | Primary fixing only — secondary retention **[GAP]** (finding F-01) |
| Racking-board light fitting | Static | 2 | 30 | ≈ 589 J | **[GAP]** — no user band supplied | Primary fixing + tethered lanyard |
| Swung tubular during tripping | Dynamic | **[GAP]** — mass not supplied | 24 | **[GAP]** — mass [GAP] | **[GAP]** — band cannot be set without mass | Operational control + exclusion zone below the derrick |

Impact energy is the public method `E ≈ m · g · h` (`g = 9.81 m/s²`) computed only where the user supplied mass and fall height. The user's DROPS Calculator band is recorded where supplied; the **licensed consequence-band threshold values are not recomputed** — they stay `[GAP]` / user-confirmed (`[ASSUMPTION A1]`).

## 3. Hierarchy of controls (reliable securing first)

| Order | Control | Tier | Owner (role) |
|---|---|---|---|
| Lead | Remove non-essential items from the monkeyboard; design out the dropped-object source | Elimination | DROPS Coordinator |
| Lead | Fit secondary retention (tethered lanyard) to the fingerboard latch pin to the reliable-securing standard | Engineering | Derrick Supervisor |
| Support | DROPS survey + register, weekly at-height inspection, exclusion/red zone below the derrick during tripping | Administrative | OIM |
| Residual | Hard hats for persons who must enter the drill floor | PPE | Deck Crew Supervisor |

A "hard hats below" treatment offered as the headline control is flagged (`ppe_admin_only`) and pushed up the hierarchy — the engineering-led reliable securing + the exclusion zone are the controls.

## 4. Key findings

- **F-01 (High) — fingerboard latch pin has no secondary retention.** The monkeyboard fingerboard latch pin (4 kg, 28 m, ≈ 1098 J) has a primary fixing only. An at-height item with no recorded secondary-retention standard is an immediate high-priority finding.
- **F-02 (Medium) — swung-tubular mass not supplied.** The dynamic swung-tubular object has no supplied mass, so its impact energy and consequence band stay `[GAP]` — never invented. The mass must be confirmed before the consequence can be banded.

## 5. Residual risk (re-scored after reliable securing + exclusion zones)

| Object | Initial (5×5) | Control | Residual (5×5) |
|---|---|---|---|
| Fingerboard latch pin | 16 (High) | Secondary retention fitted + exclusion zone | 6 (Medium) — pending F-01 closure |
| Racking-board light | 9 (Medium) | Tethered lanyard in place | 4 (Low) |
| Swung tubular | [GAP] — band [GAP] | Operational control + exclusion zone | [GAP] — re-score on mass confirmation |

## 6. SMART actions

| Ref | Action | Owner (role) | Due | Measure |
|---|---|---|---|---|
| A-01 | Fit and record secondary retention on the fingerboard latch pin (close F-01) | Derrick Supervisor | 2026-07-10 | Register row shows recorded secondary-retention standard |
| A-02 | Obtain the swung-tubular mass and band its consequence via the public m·g·h method (close F-02 [GAP]) | DROPS Coordinator | 2026-07-24 | Mass recorded; energy + band populated |
| A-03 | Confirm the licensed DROPS Calculator consequence bands with the SME and close the racking-light band [GAP] | DROPS Coordinator | 2026-08-31 | User-confirmed bands recorded; thresholds remain cite-only |

## 7. Assumptions & gaps

- `[ASSUMPTION A1]` The licensed DROPS Calculator consequence-band threshold values stay `[GAP]` / user-confirmed; the user's bands are recorded as supplied and never recomputed from the licensed table.
- `[GAP]` Swung-tubular mass not supplied — impact energy and band cannot be set without it.
- `[GAP]` Racking-board light fitting has no user-confirmed DROPS band.

## 8. Regulatory basis

DROPS Recommended Practice (2017) + DROPS Reliable Securing (survey, static/dynamic taxonomy, reliable-securing hierarchy, exclusion zones); IADC HSE Guidelines Section 16 (Dropped Objects); API RP 2D (offshore crane O&M) / API RP 54 (drilling & servicing); ISO 45001 §8.1.2 (hierarchy of controls). Cited by topic; the practice text and the licensed DROPS Calculator threshold table are not reproduced. This DROPS survey + register feeds the offshore safety case (MAR-01) — cross-referenced, never rebuilt here.
