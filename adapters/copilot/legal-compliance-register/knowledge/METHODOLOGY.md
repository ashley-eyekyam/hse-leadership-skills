# Methodology — multi-jurisdiction legal & other-requirements compliance register

The domain method for `legal-compliance-register`, grounded in **ISO 45001 clause 6.1.3**
(determination of legal and other requirements) + **clause 9.1.2** (evaluation of
compliance), applying `KB-SNIP-LEGAL-REGISTER-METHOD` over `KB-DATA-OBLIGATION-FAMILIES`.
The core-value lever for this skill is **applicability rigour**: an obligation is listed
only after it is *confirmed applicable to a named in-scope activity* — a copy-paste
register of inapplicable law is the defect this method exists to prevent.

## 0. De-identify first
Before any drafting, run the `deid` block. Named compliance owners and any
enforcement/disciplinary detail are role-labelled in the shared register; the
re-identification key is held separately, never in the register.

## 1. Applicability determination (confirm, do not just list)
For each jurisdiction and each activity/hazard profile from the intake:
1. Look up the candidate obligation families in `KB-DATA-OBLIGATION-FAMILIES` (the
   activity → obligation-family lookup per jurisdiction).
2. **Confirm applicability against the named activity.** An obligation pulled for an
   activity the organisation does not perform (e.g. a construction or confined-space reg
   for a pure office) is **flagged inapplicable and excluded** — with a one-line rationale
   — not listed. Every listed obligation carries an **applicability rationale** tied to a
   named activity.

## 2. Obligation extraction + citation (UK / US / EU)
For the applicable obligations, cite the source instrument from the resolved
jurisdiction's KB fragment:
- **UK** — `KB-REG-UK-HSWA`: HSWA 1974 s.2/s.3 general duties + MHSWR 1999 (reg. 3 risk
  assessment, principles of prevention).
- **US** — `KB-REG-US-OSHA`: OSH Act General Duty Clause + the applicable 29 CFR
  1910/1926 standards for the named activities (cite the specific standard, not "OSHA").
- **EU** — `KB-REG-EU-OSH`: Framework Directive 89/391/EEC Art. 5/6; **cite the
  member-state transposition** for any binding form or numbered duty.

Never invent a citation; an uncertain obligation is `[GAP]`.

## 3. India leg — DEFER to `hse-india` (three-tier graceful degradation)
India is **not** cited inline. Run **mandatory state detection** (intake Q1a /
`KB-REG-IN-STATEFORMS`) first, then defer:
- **Tier 1 (subagents available):** the India-Obligation-Mapper subagent runs the
  `hse-india` skills — `india-state-form-finder` (resolve the state form/return/portal)
  and/or `factories-act-returns` (the return obligations) — for the resolved state.
- **Tier 2 (no subagents):** the main thread reads the `hse-india` KB INLINE
  (`KB-REG-IN-FACTORIES` + `KB-REG-IN-STATEFORMS`, flagging the `KB-REG-IN-OSH-CODE`
  transition) and integrates the India rows itself.
- **Tier 3 (`hse-india` not installed):** emit **routing prose + a KB pointer + `[GAP]`**
  — name the skill to run (`india-state-form-finder` / `factories-act-returns`) and mark
  the state-specific form `[GAP]`.

At **every tier**: the legacy state form is the **primary answer**, the OSH-Code direction
is **flagged**, **no national form number is ever minted** (unverified → `[GAP]`), and the
India leg **never hard-blocks** the rest of the register.

## 4. Evidence mapping + gap / owner / review-date (9.1.2)
For each applicable obligation, map the **compliance evidence** the org holds (permit,
certificate, statutory-examination record, procedure) and mark **Compliant / Gap /
[GAP-evidence]**. Every row carries:
- an **applicability rationale** (from step 1),
- a **compliance-evidence cell**,
- a **named (role-label) owner**, and
- a **review date**.

A **gap** raises a control via `KB-SNIP-HOC` (eliminate the non-compliant activity or
engineer the control before an administrative reminder) **plus a SMART action** —
`smart_actions.validate_register` rejects any action missing an owner, a valid date, a
measure, or an obligation link.

## 5. Compliance-evaluation summary + grouping
Summarise applicable-obligation counts, compliant-vs-gap, and the overdue-for-review set
(9.1.2). Group the register **by jurisdiction**; the **India deferral note** (state-detection
result + the `hse-india` routing + any `[GAP]`) is its own section.

## 6. Validate + assemble
Run `references/QUALITY_CHECKLIST.md`, then build `report.json` from
`assets/legal-compliance-register-report.template.json` and render via the shared engine.

## Update cadence
The register is a living document — each obligation's review date drives re-verification;
a legal change (or the India OSH-Code commencement in the resolved state) triggers an
out-of-cycle review.
