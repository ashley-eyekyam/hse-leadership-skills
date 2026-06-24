# Pre-output Quality Checklist — arc-flash-assessment

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The assessment names the **exact equipment** (not "a panel" / "the switchroom"). A vague
      request was **refused** at intake (the specificity anchor).
- [ ] The incident energy, the arc-flash boundary, and the PPE category are **COMPUTED by the
      `arcflash.py` engine** and traced to their IEEE 1584 inputs — **never narrated**, and never
      built on an invented fault current or clearing time.

## De-energize-first / hierarchy of controls (the core lever)
- [ ] The **de-energization decision is recorded BEFORE any PPE** — the Article 120 ESWC decision
      leads the assessment (`KB-SNIP-DEENERGIZE-FIRST`).
- [ ] **Energized work is justified, never assumed** — where the task is proposed energized, the
      justification meets OSHA 1910.333(a)(2) **or** EAWR reg 14; a "production can't stop / it's
      quicker" justification is **rejected**, and an energized-work permit (Annex J) is triggered.
- [ ] **Arc-rated PPE is the documented last line**, not the headline control. An arc-flash
      treatment that leads with arc-rated PPE when the task could be de-energized is a **FLAG pushed
      up the hierarchy** (`controls.validate_treatment` returning `ppe_admin_only=True`).
- [ ] The qualitative **residual** is framed after the controls (`risk_matrix`).

## Thresholds + label content
- [ ] The **arc-flash boundary** is the distance to **1.2 cal/cm²**; `>40 cal/cm²` flags energized
      work as **prohibited**; the PPE category maps the cal/cm² by the 1.2/4/8/25/40 breakpoints.
- [ ] The **NFPA 70E 130.5(H)** label content is present (nominal system voltage; arc-flash
      boundary; available incident energy + working distance *or* required PPE category; study date).

## Citation accuracy
- [ ] Every cited duty resolves: NFPA 70E **130.5** (arc-flash RA) / **130.5(G)** (incident-energy
      method) / **130.5(H)** (label) / **130.4** (shock + approach boundaries) / **130.7(C)(15)**
      (PPE-category table) / **Article 120** (ESWC); **IEEE 1584-2018** (the calculation, 208 V –
      15 kV); US **OSHA 1910.333 / 1910.269**; UK **EAWR 1989 reg 14** + **HSG85**. A fabricated or
      mis-stated clause/threshold is a **citation hard-fail**.
- [ ] India: resolved via `hse-india` (CEA / state electricity rules); a literal **`[GAP]`** where
      a state return is owed — **no minted national form number**.

## Defensibility & de-identification
- [ ] Every finding is traced to evidence (the IEEE 1584 computation / observation / incident); each
      action has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no named injured worker** from a prior arc-flash burn /
      electrocution incident, no embedded re-identification key, and **no `<5` injury cell** in the
      circulated output (a leak is a non-waivable `de_identification` hard-fail).
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
