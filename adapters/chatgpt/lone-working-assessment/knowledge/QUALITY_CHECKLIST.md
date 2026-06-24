# Pre-output Quality Checklist — Lone Working Assessment

> The pre-output validation gate the Workflow runs before producing any output. The draft
> must pass every item; a FLAG it raises is fixed before the output is presented.

Before producing any output, validate the draft against this gate:

- [ ] **Eliminate-the-solitary-exposure leads** — the primary control avoids lone working for the task where reasonably practicable (pair up / re-schedule / remote monitoring); a lone-worker device / panic-button app is **not** the headline control (device-led treatment rejected).
- [ ] **Coverage-checked communication is required** — "no mobile signal in that area" is treated as a **control failure**, never an accepted residual risk; an unconfirmed coverage is a `[GAP]`.
- [ ] **A scheduled check-in AND a defined missed-check-in escalation path are present** — the responder, the method, and the response time are named (an undefined responder/time is a `[GAP]`, never left open).
- [ ] **A BS 8484 device appears only as a residual supplement** layered on top of the check-in / escalation procedure — never as a substitute for it.
- [ ] **Lone work at height is routed to REN-01** (`wind-turbine-work-at-height-rescue`)'s two-person / tested-rescue baseline (no solo climb; "call 999" is not a rescue plan); **lone electrical work is routed to the cross-listed utilities skills** — neither is assessed solo here.
- [ ] Violence-to-staff and the stress/wellbeing of working alone are considered (INDG73); residual risk scored 5×5 after the lead controls.
- [ ] Every finding traced to evidence (INDG73 / BS 8484 cited); no vague controls; the full hierarchy of controls walked; named **role** owner + target/review date on every action.
- [ ] De-identification pass complete BEFORE drafting; the lone worker's contact / shift / location is role-labelled; no identifier leak, no `<5` small cell, no embedded re-identification key.

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
