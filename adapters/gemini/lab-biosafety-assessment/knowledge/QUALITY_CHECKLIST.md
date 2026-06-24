# Pre-output Quality Checklist — lab-biosafety-assessment

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The assessment names the **exact laboratory** (not "a lab") and its **specific agent /
      material**. A vague request was **refused** at intake (the specificity anchor).
- [ ] The biosafety determination is a **structured risk-group → BSL method** over the named agent +
      procedure + the cited BMBL / WHO LBM classification — not a narrated generic plan; a missing
      agent, risk group, or BSL is a `[GAP]`, never invented.

## Risk-group → BSL determination + the [GAP]-not-invent lever (the core lever)
- [ ] The **agent's risk group (RG1–RG4) is determined FIRST**, before the BSL — the risk group is
      the primary input (`KB-SNIP-BIOSAFETY-RA`).
- [ ] **An unknown / unlisted agent risk group is a literal `[GAP]` routed to a competent biosafety
      officer** — the assessment **NEVER invents a risk group or a BSL** (an invented BSL is an
      indefensible containment decision; a BSL selected from a guessed risk group is rejected).
- [ ] The **selected BSL matches the established risk group + the procedure** — a BSL selected from
      the agent alone, ignoring aerosolization, is FLAGGED; the determination (risk group → procedure
      → BSL) is recorded traceably.

## Engineering containment first / hierarchy of controls
- [ ] **Primary containment (engineering) is selected BEFORE PPE** — the biosafety-cabinet **class**
      (matched to the aerosol potential and agent), directional airflow / ventilation, and waste
      decontamination are specified before any PPE.
- [ ] **PPE is the documented residual barrier**, matched to the BSL, not the headline control. A
      treatment that **substitutes gloves/respirator for a biosafety cabinet or the BSL facility** is
      a **FLAG pushed up the hierarchy** (`controls.validate_treatment` returning `ppe_admin_only=True`).
- [ ] The qualitative **residual** biosafety risk is framed after the controls (`risk_matrix`).

## Biosecurity + surveillance + exposure response
- [ ] The **biosecurity / access-control** measures are present where the agent warrants them
      (restricted access, inventory / accountability).
- [ ] The **immunisation / serological-surveillance offer** (held confidentially) and the
      **confidential exposure-response pathway** (first aid → confidential report →
      occupational-health follow-up) are present.

## Citation accuracy
- [ ] Every cited classification resolves: **CDC/NIH BMBL 6th ed** BSL-1–4 + biosafety-cabinet
      classes; **WHO LBM 4th ed** risk groups RG1–RG4; the **NIH Guidelines** (recombinant work);
      **OSHA 1910.1030** where human blood/OPIM; **COSHH 2002 / ACDP hazard groups** (EU/UK); India
      **BMW Rules 2016** lab-waste. A fabricated or mis-stated level / class / risk group is a
      **citation hard-fail**.
- [ ] India: resolved via `hse-india` (BMW Rules 2016 / state norms); a literal **`[GAP]`** where a
      state return is owed — **no minted national form number**.

## Defensibility & de-identification (PHI — highest tier)
- [ ] Every finding is traced to evidence (the agent / risk group / procedure / cited classification);
      each action has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no specimen-source-patient identity**, **no named worker** or
      serological-surveillance / OH detail, **no `<5` lab-incident cell** (with the secondary
      back-calculation guard), and **no embedded re-identification key** in the circulated output (a
      leak is a non-waivable `de_identification` hard-fail).
- [ ] **The re-identification key is held SEPARATELY, access-controlled, OUTSIDE the tool** — the
      skill emits **no key file**; the key is an instruction to the competent person to maintain the
      mapping apart from the assessment, per OSHA 1910.1030(f) / GDPR Art. 9.
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
