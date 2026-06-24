# Pre-output Quality Checklist — dropped-objects-prevention (MAR-02)

> The pre-output validation gate the SKILL.md Workflow points to. Validate the draft against this
> gate (and run the mandatory Critic/QA + SME pass) before producing any output.

## Core-value gate (the lever this skill exists to enforce)

- [ ] **Reliable-securing-led, not "hard hats below"** — every at-height item has the survey +
  reliable securing (primary fixing + secondary retention) + exclusion-zone control as the
  headline; a "hard hats for the people below" treatment is FLAGGED and pushed up the hierarchy
  (`KB-SNIP-DROPS-SECURING`), never the primary control.
- [ ] **An at-height item with no recorded securing standard** is recorded as an immediate
  high-priority finding — not silently assumed secured.

## Survey & register

- [ ] The DROPS survey covers the named installation's at-height structures (Q2) — not a generic
  checklist.
- [ ] Every register entry is classified **static vs dynamic** per `KB-REG-DROPS`.

## Consequence banding (the integrity gate)

- [ ] Every consequence band **traces to its user-supplied mass + fall height** via the public
  `E ≈ m·g·h` method (`KB-DATA-DROPS-IMPACT`).
- [ ] **No mass/height is invented** — a missing input is a `[GAP]`.
- [ ] The **licensed DROPS Calculator threshold VALUES are NOT reproduced** — the user's band is
  recorded and the thresholds stay `[GAP]` / user-confirmed (A1 `[ASSUMED]`). A hard-coded licensed
  band boundary is a D-03 violation — reject it.

## Citations & jurisdiction

- [ ] DROPS RP / IADC §16 / API RP 2D & RP 54 cited by topic (the practice text is never
  reproduced).
- [ ] An India installation defers to `hse-india` with state detection (`KB-REG-IN-OFFSHORE`);
  emit `[GAP]`, never a national form number.

## Defensibility & de-id

- [ ] Every finding traced to its survey evidence (no unsupported assertion).
- [ ] The full hierarchy of controls walked; residual re-scored on the `risk_matrix` 5×5 after
  reliable securing + exclusion zones.
- [ ] Named **role** owner + target/review date on every action (incl. each `[GAP]`-closure).
- [ ] De-identification pass complete BEFORE drafting; the prior struck-by / fatality context is at
  role level only; no named worker, no `<5` injury cell, no re-identification key.

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores against), hold it
to three rules so it reads like a real deliverable, not a rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("DROPS Coordinator (role)", "OIM
   (role)"). A personal name reads as a de-id leak; the role fully satisfies the "named owner"
   defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut "de-identification ran first" /
   "(by design)" lines. KEEP the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real DROPS register density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7 (Golden eval-output
authoring).
