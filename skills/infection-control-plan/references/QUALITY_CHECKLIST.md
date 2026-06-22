# Pre-output Quality Checklist — infection-control-plan

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The plan names the **exact service / unit** (not "a hospital" / "the ward") and the **agent(s)
      and their transmission route(s)**. A vague request was **refused** at intake (the specificity
      anchor).
- [ ] Transmission-based IPC is a **structured route-driven precaution-selection method** over the
      named unit + agents + the cited CDC/WHO/Spaulding frameworks — not a narrated generic plan; a
      missing agent, route, or count is a `[GAP]`, never invented.

## Engineering/administrative-before-PPE / hierarchy of controls (the core lever)
- [ ] **Standard Precautions are applied to every patient**, and the **correct Transmission-Based
      precautions are layered by route** (contact / droplet / airborne) — `KB-SNIP-IPC-PRECAUTIONS`.
- [ ] **Engineering controls (ventilation, AIIR / negative pressure, single rooms) and administrative
      controls (cohorting, screening, signage, hand-hygiene audit) are recorded BEFORE PPE.** A plan
      whose only airborne control is a respirator with no AIIR / ventilation provision is a **FLAG
      pushed up the hierarchy** (`controls.validate_treatment` returning `ppe_admin_only=True`).
- [ ] **PPE is the documented last line**, not the headline control — gown+gloves (contact), surgical
      mask (droplet), fit-tested respirator (airborne) as the residual barrier.
- [ ] The **Spaulding reprocessing decision** is correct per device class — critical → sterilization;
      semi-critical → high-level disinfection; non-critical → low-level. **High-level disinfection of a
      critical device is a Spaulding mis-application and fails.**
- [ ] The qualitative **residual** transmission risk is framed after the controls (`risk_matrix`).

## Programme + surveillance discipline
- [ ] The **WHO IPC programme** is structured against the core components (programme/team, guidelines,
      education, surveillance, multimodal strategy, monitoring/feedback, workload/staffing, built
      environment).
- [ ] The **surveillance** (HAI / outbreak / cluster) is **de-identified / aggregated** in the
      circulated artifact (never line-level); **no outbreak is reported on a named ward in a way that
      re-identifies a patient**.

## Citation accuracy
- [ ] Every cited framework resolves: the **CDC Guideline for Isolation Precautions** (Standard +
      Transmission-Based), the **WHO Core Components of IPC**, the **Spaulding classification**; the
      **UK Hygiene Code**; the **OSHA bloodborne-pathogens** confidentiality discipline; India **BMW
      Rules 2016** segregation. A fabricated or mis-stated framework / precaution is a **citation
      hard-fail**.
- [ ] India: resolved via `hse-india` (BMW Rules 2016 / state norms); a literal **`[GAP]`** where a
      state return is owed — **no minted national form number**.

## Defensibility & de-identification (PHI — highest tier)
- [ ] Every finding is traced to evidence (the agent/route, the control state, the cited framework);
      each action has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no patient infection / colonisation status attributed to a
      named person**, **no named patient or staff member**, **no `<5` case / cluster cell** (with the
      secondary back-calculation guard — a 3-case cluster on a named ward is a leak), and **no embedded
      re-identification key** in the circulated output (a leak is a non-waivable `de_identification`
      hard-fail).
- [ ] **The re-identification key is held SEPARATELY, access-controlled, OUTSIDE the tool** — the skill
      emits **no key file** (documented-procedure model); the key is an instruction to the competent
      person to maintain the mapping apart from the plan, and **no new report field** is added (the
      banner is the existing `meta.deid_notice` header).
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
