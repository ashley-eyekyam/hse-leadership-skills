# Pre-output Quality Checklist — Weather Dynamic Risk Assessment

> The pre-output validation gate the SKILL.md Workflow runs before producing any output.

Before producing any output, validate the draft against this gate:

- [ ] **Named site / activity + controlling equipment** confirmed (no generic "the wind farm" /
      "keep an eye on the weather").
- [ ] **Every weather parameter is a THRESHOLD → ACTION → RE-ASSESSMENT TRIGGER** — each parameter
      in play (wind, lightning, ice, visibility, temperature) carries a **specific numeric
      threshold**, a **pre-decided action** (hold / stop / evacuate), and a **mandatory
      re-assessment trigger**; **a "monitor the wind / stop if too windy" control with no number is
      REJECTED**.
- [ ] **Wind measured at hub height, not base of tower** — a base-of-tower reading used for a
      tower-top decision is **flagged as a control failure**; every threshold is referenced to its
      measurement point.
- [ ] **BS 7121-1 (2016) 7 m/s man-riding ceiling cited correctly** where a personnel-carrier lift
      is used — the verified anchor, the 2016 edition (not 2006).
- [ ] **The ≈15 m/s hub-height cut-off is flagged `[ASSUMED A4]` / proposed-and-confirmed**, never
      asserted as a fixed standard; every other numeric threshold (manufacturer / CPA / lightning /
      ice / visibility / temperature) is **user-confirmed or `[GAP]`**, never invented.
- [ ] **Hierarchy of controls leads with eliminating the exposure** (reschedule / shelter) before
      the administrative stop-limit; a stop-limit-only treatment where rescheduling is practicable
      is pushed up the hierarchy.
- [ ] Every finding traced to evidence (cited source + year); no unsupported assertion.
- [ ] Named role owner + ISO due date on every action; residual risk re-scored on the 5×5.
- [ ] De-identification pass complete BEFORE drafting; **zero prior-incident PII / personal-contact
      leak** in the circulated copy; re-identification key held separately.

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores
against), hold it to three rules so it reads like a real deliverable, not a
rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("Site Lead (role)",
   "Rope-Access Supervisor (role)"). A personal name reads as a de-id leak; the role
   fully satisfies the "named owner" defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut
   "de-identification ran first" / "never narrated" / "(by design)" lines. KEEP
   the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real document density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7
(Golden eval-output authoring).
