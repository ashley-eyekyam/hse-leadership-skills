# Pre-output Quality Checklist (TODO — author the gate)

> Standalone-fallback scaffold emitted by `hse-skill-forge`. This file exists so the
> SKILL.md Workflow reference (linter rule 8) resolves on disk; the author writes the
> skill's real pre-output validation gate here.

Before producing any output, validate the draft against this gate:

- [ ] **Racking controls are SWL-design / inspection-regime led** — the SWL-rated configuration, column
      protection, and the BS EN 15635 inspection regime lead; "inspect carefully" / a hi-vis briefing
      is **not** the headline control (it is flagged and pushed up the hierarchy).
- [ ] **MHE/pedestrian controls are engineered-segregation led** — barriers / one-way systems / marked
      and protected walkways and crossings lead; hi-vis and "look out for forklifts" are residual only.
- [ ] **The EN 15635 inspection regime is complete** — a named PRRS, the weekly visual, and the
      ≥12-monthly expert inspection; an absent expert inspection / unappointed PRRS is a high-priority
      finding.
- [ ] **Every damage finding is on the correct SEMA RAG band with the matching action** — Green =
      monitor; Amber = repair within 4 weeks + auto-escalate to Red; **Red = immediate off-load +
      isolate** (a Red down-rated to "monitor" is rejected).
- [ ] **No SWL / tolerance / inspection interval assumed** — every unsupplied site-specific value is a
      literal `[GAP]` with a request for the SWL load notice / rack-design drawing.
- [ ] The full hierarchy of controls walked for every racking/MHE hazard; named owner + target/review
      date on every action.
- [ ] India site → state resolved via `hse-india` (mandatory state detection); `[GAP]`, never a
      national form number (CONV-8).
- [ ] De-identification pass complete BEFORE drafting; any prior struck-by / rack-collapse incident is
      cited at role level only; no name / phone / `<5` injury cell / re-identification key leak.

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
