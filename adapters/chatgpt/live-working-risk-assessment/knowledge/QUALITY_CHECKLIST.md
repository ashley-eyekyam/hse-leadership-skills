# Pre-output Quality Checklist — live-working-risk-assessment

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The assessment names the **exact task + the live conductors/apparatus + the operating voltage**
      (not "work near the live parts" / "a panel"). A vague request was **refused** at intake (the
      specificity anchor).
- [ ] The **limited and restricted approach boundaries** are defined for the working position — "work
      carefully near the live parts" is not an approach boundary.

## De-energize-first / live-working justification (the core lever)
- [ ] The **de-energization evaluation is recorded BEFORE any live-work justification** — the ESWC
      default (Article 120 / `KB-SNIP-DEENERGIZE-FIRST`) leads the assessment, and live work is the
      rare, fully-justified exception, not the default.
- [ ] Where live work is proposed, the **statutory three-part test is met** — ALL of (a) unreasonable
      to be dead + (b) reasonable to work live + (c) suitable precautions are recorded
      (`KB-SNIP-LIVE-WORK-JUSTIFICATION`). **A justification of mere convenience / cost / schedule
      ("production cannot stop / it's quicker") is REFUSED** — never accepted as an adequate EAWR reg
      14 / 1910.333 justification.
- [ ] **Arc-rated PPE is the documented LAST line, not the headline control.** A plan whose only
      control is arc-rated PPE with no de-energization evaluation is a **FLAG pushed up the
      hierarchy** (`controls.validate_treatment`).
- [ ] The **arc-flash incident energy + PPE category at the working position are CROSS-REFERENCED
      from `arc-flash-assessment` (#1) — never re-derived here**; a narrated/estimated incident energy
      or an invented fault current is a FLAG. Where the incident energy exceeds **40 cal/cm²**, the
      work is flagged **prohibited**.
- [ ] The qualitative **residual** is framed after the controls (`risk_matrix`).

## Energized-work permit
- [ ] Where live work is authorised, the **energized-work permit carries the NFPA 70E Annex J
      content** — the justification + precautions + approach boundaries + PPE + the **authorising
      signature**. A live-work narrative with no energized-work permit content is a failure.

## Citation accuracy
- [ ] Every cited duty resolves: NFPA 70E **110.5/130.2** (energized-work justification + permit) /
      **130.4** (shock risk assessment + approach boundaries) / **Annex J** (the permit) / **Article
      120** (the ESWC default); US **OSHA 1910.333(a)(2)** (de-energize-first / justification) +
      **1910.269** (T&D approach distances) + **1910.147**; UK **EAWR 1989 reg 14** (the three-part
      test) + **HSG85** + **HSR25**. A fabricated or mis-stated clause — or a mis-stated reg-14
      three-part test, or an omitted 1910.333 de-energize-first rule — is a **citation hard-fail**.
- [ ] India: resolved via `hse-india` (CEA / state electricity rules); a literal **`[GAP]`** where a
      state return is owed — **no minted national form number**.

## Defensibility & de-identification
- [ ] Every finding/precaution is traced to evidence (the task / the live conductors / the incident);
      each action has a **named role owner + ISO due date + measure**
      (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no named injured worker** from a prior contact / electrocution
      / arc-flash burn incident, no embedded re-identification key, and **no `<5` injury cell** in the
      circulated output (a leak is a non-waivable `de_identification` hard-fail).
- [ ] The output is **decision-support** — it never claims "approved by a competent person" and never
      asserts that live work is sanctioned.
