# Pre-output Quality Checklist — sharps-needlestick-management

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The plan names the **exact service** (not "a clinic" / "the ward") and its **real sharps
      inventory**. A vague request was **refused** at intake (the specificity anchor).
- [ ] Sharps control is a **structured engineering-control-first method** over the named device
      inventory + the cited OSHA/EU hierarchy — not a narrated generic plan; a missing device or
      count is a `[GAP]`, never invented.

## Engineering-first / hierarchy of controls (the core lever)
- [ ] The **elimination/substitution decision is recorded BEFORE any device or PPE** — the plan
      leads with eliminating unnecessary sharps (`KB-SNIP-SHARPS-HIERARCHY`).
- [ ] **Every non-engineered device carries a recorded justification** — a non-engineered device
      left in use without one is a FLAG; the **documented annual safer-device consideration with
      non-managerial frontline-worker input** is present (OSHA (c)(1)(iv) / Needlestick Act).
- [ ] The **no-recapping rule** is present; recapping by hand is **not** permitted; point-of-use
      sharps containers are specified.
- [ ] **PPE and PEP are the documented last lines**, not the headline control. A treatment that
      leads with "be careful / wear gloves" where the sharp could be eliminated or engineered out is
      a **FLAG pushed up the hierarchy** (`controls.validate_treatment` returning
      `ppe_admin_only=True`).
- [ ] The qualitative **residual** sharps-exposure risk is framed after the controls (`risk_matrix`).

## Exposure response + log discipline
- [ ] The **confidential post-exposure (PEP) pathway** is present (first-aid → confidential report →
      **consented** source-patient testing → PEP timing for HBV/HCV/HIV → follow-up); the
      **HBV-vaccination status** is recorded.
- [ ] The **Sharps Injury Log** (OSHA (h)(5) fields — device type, brand, work area, how) is present
      and is **de-identified / aggregated** in the circulated artifact (never line-level).

## Citation accuracy
- [ ] Every cited duty resolves: OSHA **1910.1030** (c) / (c)(1)(iv) / (d)(2) / (f) / (h)(5) + the
      **Needlestick Safety and Prevention Act**; **EU Directive 2010/32/EU** + the **UK Sharps Regs
      2013** / COSHH; India **BMW Rules 2016** sharps segregation. A fabricated or mis-stated
      clause/duty is a **citation hard-fail**.
- [ ] India: resolved via `hse-india` (BMW Rules 2016 / state norms); a literal **`[GAP]`** where a
      state return is owed — **no minted national form number**.

## Defensibility & de-identification (PHI — highest tier)
- [ ] Every finding is traced to evidence (the device inventory / control state / cited duty); each
      action has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no source-patient identity or serostatus**, **no named
      injured worker** or PEP medical detail, **no `<5` injury cell** (with the secondary
      back-calculation guard), and **no embedded re-identification / exposure key** in the circulated
      output (a leak is a non-waivable `de_identification` hard-fail).
- [ ] **The re-identification / exposure key is held SEPARATELY, access-controlled, OUTSIDE the
      tool** — the skill emits **no key file**; the key is an instruction to the competent person to
      maintain the mapping apart from the plan, per OSHA 1910.1030(f).
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
