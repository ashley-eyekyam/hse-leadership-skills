# Pre-output Quality Checklist — offshore-safety-case

Before producing any output, validate the draft against this gate. This is an **assistive** skill: the gate enforces the assistive boundary as hard as the universal HSE gates.

## Assistive-boundary gate (load-bearing — fail any of these and do NOT output)
- [ ] **Records, never produces.** The output is the structured claim → argument → evidence map of the duty-holder's content — not an autonomously authored safety case.
- [ ] **`[GAP]` for every unsupplied element/figure/claim.** Any Schedule 6/7 element, QRA number, consequence distance, MAH frequency, ALARP figure, or barrier/SCE-effectiveness claim not supplied is recorded `[GAP]` — never invented.
- [ ] **No computed/invented QRA.** No quantitative MAH frequency or consequence number is computed by the skill; external figures appear only with their stated provenance.
- [ ] **No un-evidenced barrier/SCE claim.** No barrier or SCE is asserted effective without a cited performance-standard evidence reference or a verifier finding.
- [ ] **No acceptance language.** The output contains no "accepted / approved / authorised" status (acceptance is the competent authority's — HSE + OPRED — act); the assistive disclaimer is present.
- [ ] **Current regime cited.** SI 2015/398 (SCR 2015) is cited as current; SCR 2005 appears only as the named legacy reference.
- [ ] **EER cross-referenced, not rebuilt.** The emergency-response element points to the sibling `marine-emergency-response` (MAR-03) plan.

## Universal gate
- [ ] Every finding traced to a named evidence reference (no unsupported assertion).
- [ ] No vague controls; no PPE-only / admin-only treatment without justification/escalation (HoC walked).
- [ ] Named role-owner + target/review date on every gap-closure action.
- [ ] De-identification pass complete BEFORE drafting; no identifier leak; prior-incident names and named station-bill role-holders pseudonymised to role labels.

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the exemplar the grader scores against), hold it to three rules so it reads like a real deliverable, not a rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("OIM (role)", "Technical Authority"). A personal name reads as a de-id leak; the role fully satisfies the "named owner" defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut "de-identification ran first" / "(by design)" lines. KEEP the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real argument-map density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7 (Golden eval-output authoring).
