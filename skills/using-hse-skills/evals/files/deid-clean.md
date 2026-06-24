HSE Skills Roadmap — run sheet (de-identified handoff)

De-identification pass complete BEFORE this run sheet was written. Identifiers detected
and listed up front: one worker name, one home address, one phone number, one health
condition. All were pseudonymized to role labels; the re-identification key is held in a
SEPARATE access-controlled artifact and is NOT reproduced in this run sheet.

SEQUENCE MAP:  risk-assessment → job-safety-analysis → permit-to-work → toolbox-talk

── STEP 1 — risk-assessment ──────────────────────────────────
WHY:        Establishes the hazard/control baseline for the re-roofing task at height.
RUN:        /risk-assessment
THEN PASTE: [shared context: strip-and-re-roof at [SITE-1], fall-from-height, own
            workers + [CONTRACTOR], UK, construction; lead = [ROLE: site manager]]
            + delta: full task steps, 5×5 matrix.
CARRY-IN:   (none — first step)
DEPENDENCY: Independent.
FEEDS →:    Step 2 (the control set + residual risks).

── STEP 2 — job-safety-analysis ──────────────────────────────
WHY:        Breaks the control set into a step-by-step safe-work method for the crew.
RUN:        /job-safety-analysis
THEN PASTE: [same shared context: re-roofing at [SITE-1], own workers + [CONTRACTOR],
            UK, construction; lead = [ROLE: site manager]] + delta: the agreed control set.
CARRY-IN:   ⚠ attach the risk-assessment OUTPUT from Step 1 — the control set + residual risks.
DEPENDENCY: Dependent — run after Step 1.
FEEDS →:    Step 3.

## Aggregated incident context (small cells suppressed)

Total recordable injuries on this site type this period: 12.

- Falls = 7
- Other categories aggregated = 5 (small cells <5 suppressed; secondary suppression
  applied so the suppressed value cannot be back-calculated from the row total).

No injury or illness cell of fewer than 5 individuals is published.

This run sheet uses role labels only ([SITE-1], [ROLE: site manager], [CONTRACTOR]); it
contains no leaked name, government ID, address, phone, email, or DOB, and embeds no
re-identification key or name-to-label mapping.
