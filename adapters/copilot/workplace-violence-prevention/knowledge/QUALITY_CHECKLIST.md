# Pre-output Quality Checklist — workplace-violence-prevention

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The program names the **exact service** (not "a hospital" / "the ward") and **where / when
      violence occurs**. A vague request was **refused** at intake (the specificity anchor).
- [ ] WPV control is a **structured environmental-and-administrative-control-first method** over the
      named service's worksite analysis + the cited OSHA 3148 / §5(a)(1) / Cal-OSHA framework — not a
      narrated generic plan; a missing incident or count is a `[GAP]`, never invented.

## Worksite analysis + environmental/administrative-first (the core lever)
- [ ] The **worksite hazard analysis is recorded FIRST, before any control** (de-identified,
      aggregated; `KB-REG-WPV-OSHA3148` element 2) — a program with no worksite analysis fails.
- [ ] The exposure is **classified by the type-1-4 taxonomy** (each type drives a different control
      set); mis-applying the taxonomy is a citation hard-fail.
- [ ] The program **leads with environmental / engineering controls** (controlled access,
      sightlines, alarms / duress, secure design) **and administrative controls** (staffing /
      skill-mix, lone-working, de-identified flagging, reporting culture) **before any reactive /
      PPE measure**.
- [ ] **De-escalation, response training, and personal alarms are the documented last lines**, not
      the headline control. A program whose headline control is "issue personal alarms / run
      self-defence training" with no environmental or administrative control is a **FLAG pushed up
      the hierarchy** (`controls.validate_treatment` returning `ppe_admin_only=True`).
- [ ] The qualitative **residual** violence risk is framed after the controls (`risk_matrix`).

## Response + log discipline
- [ ] The **de-escalation / response protocol + post-incident support + training plan** are present
      (the residual lines).
- [ ] The **WPV incident log** (the OSHA 3148 recordkeeping element / Cal-OSHA 8 CCR 3342
      violent-incident log) is present and is **de-identified / aggregated** in the circulated
      artifact (never line-level).

## Citation accuracy
- [ ] Every cited duty resolves: the **OSHA 3148** five program elements + the **OSH Act §5(a)(1)**
      General Duty Clause basis; **Cal/OSHA 8 CCR 3342** as the binding standard in California; the
      **UK HSE work-related-violence** guidance + **NICE NG10**. A fabricated or mis-stated
      clause/duty, or a mis-applied type-1-4 taxonomy, is a **citation hard-fail**.
- [ ] India: resolved via `hse-india` (state provisions); a literal **`[GAP]`** where a state return
      is owed — **no minted national form number**.

## Defensibility & de-identification (PHI — highest tier)
- [ ] Every finding is traced to evidence (the worksite analysis / control state / cited duty); each
      action has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no named victim, assailant, or known-risk patient**, **no
      behavioural-health flag tied to a person**, **no `<5` incident cell** (with the secondary
      back-calculation guard), and **no embedded re-identification key** in the circulated output (a
      leak is a non-waivable `de_identification` hard-fail).
- [ ] **The re-identification key is held SEPARATELY, access-controlled, OUTSIDE the tool** — the
      skill emits **no key file**; the key is an instruction to the competent person to maintain the
      mapping apart from the program.
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
