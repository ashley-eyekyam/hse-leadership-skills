# Methodology — patient-handling-assessment (avoid-first, PHI-protected)

The domain method `patient-handling-assessment` applies. Its spine is **avoid the manual lift first**
(`KB-SNIP-TILE-PEOPLE` + `KB-SNIP-HOC`): avoid hazardous manual handling of people (substitute a
ceiling/mobile hoist, slide sheet, or transfer board), assess the unavoidable residual by the **TILE**
filter (Task, Individual, Load, Environment), then reduce with mechanical aids and environment design,
then safe systems of work, with **technique and PPE (a back belt) as the documented last lines**. A
patient-handling treatment that **leads with "use good technique / wear a back belt"** where the
manual lift could be avoided with a mechanical aid, or that **recommends a manual lift where a hoist /
aid is reasonably available**, is a **FLAG pushed up the hierarchy, never the headline control**.
There is **no calculation** — the TILE assessment and the mobility-and-equipment matrix are a
structured assessment frame over the named care task + the cited SPHM/MHOR standards; the residual
moving-and-handling risk reuses the standard `risk_matrix` 5×5 (the standard path applies here, unlike
arc flash) — there is **no new engine** (the NIOSH lifting equation is the manufacturing pack's
`ergonomics`, NOT this skill).

## 0. De-identify first (the highest-PHI step — patient + worker)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Patient mobility data and a
worker's musculoskeletal record are **special-category health data (PHI)**. Assess and record the
**patient by de-identified mobility / dependency level and weight band only** (never a name,
MRN/hospital number, ward/bay, diagnosis, or care-plan detail — "a bariatric, fully-dependent patient
on Ward 4 bay 2" is identifying; scrub the ward/bay and any clinical detail), assess the **worker's
capability** under TILE Individual **without** writing the worker's name or any fitness /
back-condition record into the circulated copy (role-label "Worker A"; the medical-fitness record held
confidentially + separately). Apply `<5` small-cell suppression (with secondary suppression) to every
handling-injury category aggregated across the unit. **The skill emits NO re-identification key file**
— the key is an instruction to the competent person (held separately, access-controlled). The
De-identifier subagent runs FIRST; everything downstream consumes only its scrubbed output.

## 1. Scope the named care task & setting (Q1)

- **Named care task & setting (Q1)** — the exact handling task (bed-to-chair transfer, repositioning,
  lateral transfer, falls recovery, bariatric move, ambulance loading) **and the setting** (ward,
  care home, community, ambulance). **Refuse "moving patients" / "the ward"** (the specificity
  anchor). A missing task or setting is a `[GAP]`, never invented.

## 2. Record the avoid-the-manual-lift decision — the move-toward-zero gate (the spine)

This question is asked **first among the controls** because avoiding the manual lift is the **primary
control**, not the technique:

- **Q2 = yes** → the assessment **leads with the mechanical aid**: substitute a ceiling/mobile hoist,
  slide sheet, or transfer board so the manual lift is removed (move-toward-zero, the SPHM/NIOSH
  principle). Manual lifting of the person is the hazard MHOR reg 4 requires avoiding first.
- **Q2 = no/partly** → branch to the **TILE assessment of the residual (Q3)**: assess the
  unavoidable handling against the four elements. **A control plan that defaults to "two staff lift"
  where a mechanical aid is reasonably available is FLAGGED** (move-toward-zero not applied).

## 3. TILE assessment of the residual handling (Q3) — all four elements

Assess the unavoidable handling against the MHOR Schedule 1 **TILE** filter — **refuse to score
without all four elements**:

- **Task** — what is being done (lift, transfer, reposition, hold), distance, posture, repetition,
  twisting.
- **Individual** — the handler's capability, training, and any limitation; the number of handlers
  (**never the worker's medical record** in the circulated copy — role-label).
- **Load** — the patient: weight band, dependency, cooperation, attachments (lines, drains),
  bariatric considerations, falling risk (the **patient assessed by mobility/dependency,
  de-identified**).
- **Environment** — space, floor, bed/chair height, ceiling-track availability, obstructions.

## 4. Mobility-and-equipment matrix (Q4) — the core artifact

Build the **mobility-and-equipment matrix**: the patient's mobility / dependency level → the matched
equipment + the number of handlers. The matrix is the deliverable's core artifact. A **"two-person
manual lift" recommended where a hoist or slide aid is reasonably available is FLAGGED** and pushed up
the hierarchy (the mechanical aid is the higher-order control).

## 5. Bariatric / falls plan (Q5)

Where the branch ran, add the **bariatric plan** (equipment safe-working-load (SWL), environmental
loading, extended planning) or the **falls plan** (post-fall handling plan). A bariatric move
addressed without the SWL and environmental-loading check is incomplete.

## 6. Rank the controls (the hierarchy gate) + the residual + SMART actions + report

Run the `controls` engine. The control narrative **always leads with eliminating the manual lift** →
engineer / mechanical aids (hoist, slide sheet, transfer board, environment design) → administrative
(safe systems of work, training, the matrix) → **technique + PPE (back belt) LAST**. A
patient-handling treatment that **leads with "use good technique / wear a back belt" where the manual
lift could be avoided**, or **recommends a manual lift where a mechanical aid is reasonably
available** (`controls.validate_treatment` returning `ppe_admin_only=True`), is a **FLAG pushed up the
hierarchy, never the headline control**. Frame the qualitative residual moving-and-handling risk via
`risk_matrix` (the standard 5×5). Every equipment-provision / training / environmental-modification
action becomes a SMART action (named role owner + ISO due date + measure), validated by
`smart_actions.validate_register`. Validate the draft against `references/QUALITY_CHECKLIST.md`, then
assemble `assets/patient-handling-assessment.report.json` and run the canonical `report-output` call.

## Jurisdiction

UK **Manual Handling Operations Regulations 1992 (MHOR)** — reg 4(1)(a) **avoid** → reg 4(1)(b)(i)
**assess** (suitable & sufficient, Schedule 1 **TILE**) → reg 4(1)(b)(ii) **reduce** → reg 4(2)
**review** — is the binding UK duty; the US/international leg grounds in **ANA SPHM (2021)** (the
move-toward-zero culture + the 8 standards) + **NIOSH safe-lifting guidance** (minimize manual patient
lifting) + **ISO/TR 12296:2012** (ergonomics — manual handling of people in healthcare). For India,
resolve the state via `hse-india` (**mandatory state detection**) per the factory/occupational
ergonomics provisions, and emit a literal `[GAP]` where a state return is owed — **never a minted
national form number**.
