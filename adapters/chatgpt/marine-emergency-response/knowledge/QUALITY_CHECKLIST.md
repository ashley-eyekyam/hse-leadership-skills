# Pre-output Quality Checklist (TODO — author the gate)

> Standalone-fallback scaffold emitted by `hse-skill-forge`. This file exists so the
> SKILL.md Workflow reference (linter rule 8) resolves on disk; the author writes the
> skill's real pre-output validation gate here.

Before producing any output, validate the draft against this gate:

- [ ] Every finding traced to evidence (no unsupported assertion).
- [ ] No vague controls; no PPE-only treatment without justification/escalation.
- [ ] The full hierarchy of controls walked for every hazard/control.
- [ ] Named owner + target/review date on every action.
- [ ] De-identification pass complete BEFORE drafting; no identifier leak.

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
