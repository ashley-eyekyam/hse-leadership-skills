# Pre-output Quality Checklist — patient-handling-assessment

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The assessment names the **exact care task** (not "moving patients" / "the ward") and its
      **setting**. A vague request was **refused** at intake (the specificity anchor).
- [ ] The TILE assessment + the mobility-and-equipment matrix are a **structured assessment frame**
      over the named care task + the cited SPHM/MHOR standards — not a narrated generic plan; a
      missing weight band, dependency level, or count is a `[GAP]`, never invented.

## Avoid-first / hierarchy of controls (the core lever)
- [ ] The **avoid-the-manual-lift decision is recorded BEFORE any equipment or technique** — the
      assessment leads with avoiding the manual lift / a mechanical aid (`KB-SNIP-TILE-PEOPLE`,
      move-toward-zero).
- [ ] **No manual lift is recommended where a mechanical aid (hoist, slide sheet, transfer board) is
      reasonably available** — a "two-person manual lift" where a hoist is available is a FLAG pushed
      up the hierarchy.
- [ ] The **four TILE elements (Task, Individual, Load, Environment) are ALL assessed** — a TILE
      assessment missing any element is not suitable and sufficient and is rejected.
- [ ] The **mobility-and-equipment matrix** (dependency level → equipment + handler count) is present
      — it is the core artifact.
- [ ] **Technique and PPE (a back belt) are the documented last lines**, not the headline control. A
      treatment that leads with "use good technique / wear a back belt" where the manual lift could be
      avoided is a **FLAG pushed up the hierarchy** (`controls.validate_treatment` returning
      `ppe_admin_only=True`).
- [ ] The qualitative **residual** moving-and-handling risk is framed after the controls via the
      standard `risk_matrix` 5×5 (NOT a NIOSH-equation engine).

## Bariatric / falls + standard discipline
- [ ] Where the branch ran, the **bariatric plan** addresses equipment **safe-working-load (SWL)** and
      **environmental loading**, or the **falls plan** addresses post-fall handling.
- [ ] The **SPHM move-toward-zero principle** and the **MHOR avoid → assess → reduce duty** are
      stated, not mis-stated.

## Citation accuracy
- [ ] Every cited duty resolves: UK **MHOR 1992** reg 4 (avoid → assess (Schedule 1 TILE) → reduce);
      **ANA SPHM (2021)** 8 standards + the move-toward-zero principle; **NIOSH** safe-lifting
      guidance; **ISO/TR 12296:2012**. A fabricated or mis-stated clause/duty/principle is a
      **citation hard-fail**.
- [ ] India: resolved via `hse-india` (factory/occupational ergonomics / state norms); a literal
      **`[GAP]`** where a state return is owed — **no minted national form number**.

## Defensibility & de-identification (PHI — highest tier)
- [ ] Every finding is traced to evidence (the TILE assessment / equipment matrix / cited duty); each
      action has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; the **patient is recorded by de-identified mobility /
      dependency / weight band only** (no name, MRN, ward/bay, or diagnosis), **no named worker** or
      back-condition / OH-record detail, **no `<5` handling-injury cell** (with the secondary
      back-calculation guard), and **no embedded re-identification key** in the circulated output (a
      leak is a non-waivable `de_identification` hard-fail).
- [ ] **The re-identification key is held SEPARATELY, access-controlled, OUTSIDE the tool** — the
      skill emits **no key file**; the key is an instruction to the competent person to maintain the
      mapping apart from the assessment.
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
