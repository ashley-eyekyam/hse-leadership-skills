# Pre-output Quality Checklist — Wind Turbine Work at Height + Rescue

> The pre-output validation gate the SKILL.md Workflow runs before producing any output.

Before producing any output, validate the draft against this gate:

- [ ] **Named turbine / site + specific WAH activity** confirmed (no generic "the turbines").
- [ ] **Reg-6 control order leads** — work at height avoided where practicable; collective
      fall-prevention selected **before** personal fall-arrest (reg 7); no fall-arrest/PPE-only
      treatment where avoidance / collective prevention is reasonably practicable.
- [ ] **A MANDATORY tested rescue plan is present** — a tested, team-owned, two-person-minimum
      recovery of a suspended worker **within minutes**; **"call 999 / wait for emergency services"
      is NOT the rescue plan** (only a supplement); an untested capability / unstated recovery time
      is flagged `[GAP]`.
- [ ] **Two-person-minimum climb team** with ground support (no solo climb).
- [ ] **GWO competence cited as a requirement**, not reproduced — no licensed module text or
      certificate number in the output; certificate detail `[GAP]`.
- [ ] **Weather thresholds named but deferred to REN-03** — the ≈15 m/s hub-height cut-off flagged
      `[ASSUMED]` / proposed-and-confirmed, never a hard citation.
- [ ] Every finding traced to evidence (cited source + year); no unsupported assertion.
- [ ] Named role owner + ISO due date on every action; residual risk re-scored on the 5×5.
- [ ] De-identification pass complete BEFORE drafting; **zero climber name / GWO certificate-number
      leak** in the circulated copy; re-identification key held separately.

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
