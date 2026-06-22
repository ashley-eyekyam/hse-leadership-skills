# Pre-output Quality Checklist — electrical-permit-switching-program

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The program names the **exact apparatus** (not "the substation" / "the switchroom"). A vague
      request was **refused** at intake (the specificity anchor).
- [ ] **Every point of isolation** for the apparatus is enumerated, and the operating voltage and
      the **protective-earthing requirement** are recorded — a program that cannot enumerate its
      points of isolation is refused.

## De-energize-first / isolation integrity (the core lever)
- [ ] The **de-energization / isolation decision is recorded BEFORE work** — the Article 120 ESWC
      decision leads the program (`KB-SNIP-DEENERGIZE-FIRST`).
- [ ] The ordered switching sequence applies **isolate → prove dead → earth → sanction → restore**
      (`KB-SNIP-SWITCHING-SEQUENCE`) with **per-step authorisation**.
- [ ] **No work is authorised un-proven or un-earthed where required.** A sequence that would
      authorise work on apparatus isolated but not proven dead (no prove-test-prove), or that omits
      protective earthing where the procedure requires it, is a **FLAG pushed up the hierarchy**
      (`controls.validate_treatment`), never the program.
- [ ] The **sanction-to-test is kept DISTINCT from a permit-to-work** — controlled re-energization
      for testing is never issued as a work-on-dead permit, and vice versa.
- [ ] **Restoration is controlled** — the safety document is cancelled, earths removed, and
      locks/tags removed under the switching schedule before supply is restored.
- [ ] The qualitative **residual** is framed after the controls (`risk_matrix`); PPE is the
      documented last line, not the headline control.

## Citation accuracy
- [ ] Every cited duty resolves: NFPA 70E **Article 120** (establishing + verifying an ESWC) read
      with Annex K / 120.5; US **OSHA 1910.269** (269(d) LOTO / 269(n) protective grounding /
      269(m)) + **1910.333** + **1910.147**; UK **EAWR 1989 regs 12–13** + **HSG85**. A fabricated
      or mis-stated clause — or conflating sanction-to-test with a work permit — is a **citation
      hard-fail**.
- [ ] India: resolved via `hse-india` (CEA / state electricity rules); a literal **`[GAP]`** where
      a state return is owed — **no minted national form number**.

## Defensibility & de-identification
- [ ] Every step/finding is traced to evidence (the apparatus / the points of isolation / the
      incident); each action has a **named role owner + ISO due date + measure**
      (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no named injured operator** from a prior switching /
      electrocution incident, no embedded re-identification key, and **no `<5` injury cell** in the
      circulated output (a leak is a non-waivable `de_identification` hard-fail).
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
