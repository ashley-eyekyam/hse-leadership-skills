# Pre-output Quality Checklist — machine-guarding-assessment

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The assessment names the **exact machine / line / cell** (not "a machine" / "the factory").
      A vague or site-wide request was **refused** at intake (the specificity anchor).
- [ ] Every **danger zone** (point of operation, in-running nip, rotating parts, power-transmission,
      flying chips/sparks, crush/trap) is assessed individually — **no "guard all moving parts"**
      blanket statement.

## Hierarchy of controls (the core lever)
- [ ] Guard/device selection ran the **engineering-led order** (fixed → interlocked →
      presence-sensing → two-hand/hold-to-run → trip) against the **access-frequency rule** for
      every zone.
- [ ] **No mechanical-zone control is left PPE-only or admin-only.** A control recorded as
      "operators to keep hands clear / wear gloves" with no fixed/interlocked guard is a **FLAG
      pushed up the hierarchy** (`controls.validate_treatment` returning `ppe_admin_only=True`),
      never the headline control.
- [ ] A **defeated / missing / overridden** guard (Q4) is recorded as an **immediate high-priority
      finding**.
- [ ] The **residual risk** per zone is re-scored after the selected guard (`risk_matrix`).

## Maintenance interaction (LOTO)
- [ ] If a **maintenance** interaction mode is in scope, the assessment **cross-references
      `KB-REG-LOTO`** — energy sources identified, isolated, and **verify-zero-energy** before
      access.

## Citation accuracy
- [ ] Every cited duty resolves: US **1910.212** (point of operation / general) and **1910.219**
      (power-transmission shafts/belts/gears), UK **PUWER 1998 Regs 11–12**, the ISO 12100/14120
      method/taxonomy. A power-transmission zone that omits 1910.219 / ISO 14120, or a
      point-of-operation that omits 1910.212, is a **citation hard-fail**.
- [ ] India: grounded on Factories Act §21 via `hse-india`; a literal **`[GAP]`** where a state
      return is owed — **no minted national form number**.

## Defensibility & de-identification
- [ ] Every finding is traced to evidence (observation / photo / incident); each action has a
      **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no named injured operator** from a prior amputation /
      crush incident, no embedded re-identification key, and **no `<5` injury cell** in the
      circulated output (a leak is a non-waivable `de_identification` hard-fail).
- [ ] The output is **decision-support** — it never claims "approved by a competent person".
