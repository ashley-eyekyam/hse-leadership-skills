# Pre-output Quality Checklist — level-crossing-track-worker-safety

Before producing any output, validate the draft against this gate. The two HARD-fail
dimensions (`de_identification`, `regulatory_citation_accuracy`) cannot be waived.

## Core-value gates (the lever this skill exists for)
- [ ] **Crossing led by the remedial hierarchy** — closure → grade separation → engineering
      → signage/admin LAST. No crossing whose *lead* control is new signage / admin while a
      higher order is reasonably practicable (or, where it genuinely is not, a justified +
      SMART-actioned record of that).
- [ ] **Track work led by separation** — green-zone / line blockage / possession → SSOW →
      warning → lookout-only LAST. No track task led by a lookout alone while separation is
      reasonably practicable; red-zone working minimised.
- [ ] **ALCRM band RECORDED, never invented or recomputed** — the artifact records the
      user's supplied band (or `[GAP]`); it never fabricates a band, recomputes one, or
      hard-codes numeric ALCRM thresholds.

## Universal gates
- [ ] Every finding traced to evidence (no unsupported assertion); every conclusion cited.
- [ ] The full hierarchy of controls walked for every hazard/control (no lower-order-only
      treatment without a higher-order justification).
- [ ] Residual risk scored on the 5×5 matrix after the lead controls are applied.
- [ ] Named **role** owner + target/review date on every action and every `[GAP]` closure.
- [ ] De-identification pass complete BEFORE drafting; no identifier leak; COSS / Sentinel /
      lookout role-holders role-labelled; no `<5` incident cell on a named crossing.
- [ ] NR/L2/OHS/019 + ORR LX guidance + LXRMTK cited **by reference**, never reproduced;
      issue/date recorded as `[ASSUMED A3]`/`[GAP]` where unconfirmed.
- [ ] India content cites the Railways Act 1989 / CRS framing + defers to `hse-india` after
      mandatory state detection; no national form invented.
- [ ] Sibling boundary held — the rail SMS (RAIL-01) and ROGS application (RAIL-02) are
      referenced, never rebuilt (CONV-12).

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores
against), hold it to three rules so it reads like a real deliverable, not a
rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("COSS (role)", "PICOP
   (role)", "Lookout (role)"). A personal name reads as a de-id leak; the role fully
   satisfies the "named owner" defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut "de-identification ran
   first" / "never narrated" / "(by design)" lines. KEEP the honest `[ASSUMPTION]` /
   `[GAP]` flags (e.g. the `[GAP]` ALCRM band, the `[ASSUMED A3]` issue/date).
3. **Representative deliverable depth** — real document density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7
(Golden eval-output authoring).
