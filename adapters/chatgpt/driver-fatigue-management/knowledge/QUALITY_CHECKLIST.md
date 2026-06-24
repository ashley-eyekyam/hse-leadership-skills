# Pre-output Quality Checklist — driver-fatigue-management

Validate the draft against this gate BEFORE producing any output (markdown or rendered PDF/DOCX).
A failing item is fixed and the draft re-validated — never shipped with a known gap.

## Specificity
- [ ] The assessment names the **exact fleet / operation / route / depot** (not "our drivers" /
      "the fleet"). A vague request was **refused** at intake (the specificity anchor).
- [ ] The **HOS compliance flags are COMPUTED by the `fatigue.py` engine** (`fmcsa_compliance` /
      `eu561_compliance`) and traced to the supplied duty log — **never narrated**, and never built
      on an invented driving hour or rest segment.

## Compliance-flags-primary / advisory-index-secondary (the output-class split)
- [ ] The **HOS compliance flags are presented as the AUTHORITATIVE, primary finding** (per-rule
      PASS/FAIL).
- [ ] The **fatigue index is rendered as a clearly-flagged ADVISORY metric** (it carries
      `advisory: True` + a note) — **never** a regulatory threshold and never a compliance verdict.

## Multi-day `[GAP]` discipline
- [ ] The FMCSA **60/70 h cycle**, the **34 h restart**, and any **cross-shift daily-rest** claim
      are **NOT** asserted compliant from a single-shift log — an absent cumulative / cross-shift
      figure is a literal **`[GAP]`** (the engine's single-shift default is "no breach detectable",
      not "compliance proven").

## Roster-redesign-first / hierarchy of controls (the core lever)
- [ ] The treatment **leads with schedule / roster / journey-plan / built-in-rest (FRMS)
      redesign** (`KB-SNIP-FATIGUE-FRMS` + `KB-SNIP-HOC`).
- [ ] A **"stay alert" briefing / driver-alertness training / an in-cab fatigue-detection gadget
      taken as the headline control** is a **FLAG pushed up the hierarchy**
      (`controls.validate_treatment` returning `ppe_admin_only=True`), never the primary control.
- [ ] The qualitative **residual** is framed after the controls (`risk_matrix`).

## Citation accuracy
- [ ] Every cited duty resolves: FMCSA **49 CFR Part 395** (the part/section numbers + the ELD
      record), EU **Regulation (EC) 561/2006** + the **Reg (EU) 165/2014** tachograph; India via
      `hse-india`. A fabricated or mis-stated clause is a **citation hard-fail**.
- [ ] India: resolved via `hse-india` (Motor Transport Workers Act 1961 / state rules); a literal
      **`[GAP]`** where a state return is owed — **no minted national form number**.

## Defensibility & de-identification (HIGHEST tier)
- [ ] Every finding is traced to evidence (the `fatigue.py` computation / the duty log); each action
      has a **named role owner + ISO due date + measure** (`smart_actions.validate_register`).
- [ ] De-identification ran **first**; **no named driver**, no **CDL / DOT-medical / OSA /
      sleep-disorder** detail, no embedded re-identification key, and **no `<5` fatigue-event /
      sickness cell** in the circulated output (a leak is a non-waivable `de_identification`
      hard-fail). The re-identification key is held SEPARATELY — the skill emits no key file.
- [ ] The output is **decision-support** — it never claims "approved by a competent person".

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores
against), hold it to three rules so it reads like a real deliverable, not a
rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("Site Manager
   (role)", "Appointed Person"). A personal name reads as a de-id leak; the role
   fully satisfies the "named owner" defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut
   "de-identification ran first" / "never narrated" / "(by design)" lines. KEEP
   the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real document density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7
(Golden eval-output authoring).
