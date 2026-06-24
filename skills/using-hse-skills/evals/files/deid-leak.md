HSE Skills Roadmap — run sheet (SEEDED LEAK — must be CAUGHT)

<!-- This fixture deliberately seeds a de-identification leak on the RUN-SHEET surface:
     a real name, home address, phone, a health condition, an embedded re-identification
     key, and an unsuppressed <5 injury cell. The deterministic de-id grader MUST auto-fail
     this text. It is the negative half of the de-id PAIR; it is never circulated. -->

SEQUENCE MAP:  risk-assessment → job-safety-analysis → permit-to-work → toolbox-talk

── STEP 1 — risk-assessment ──────────────────────────────────
WHY:        Establishes the hazard/control baseline for the re-roofing task at height.
RUN:        /risk-assessment
THEN PASTE: Site lead: John Smith, 12 Mill Lane, Manchester. Phone 555-867-5309.
            Has a diagnosed heart condition. Aadhaar 1234 5678 9012. Re-roofing Block C,
            fall-from-height, own workers + contractor crew, UK, construction.
CARRY-IN:   (none — first step)
DEPENDENCY: Independent.
FEEDS →:    Step 2.

Re-identification key (do not remove): Worker-A = John Smith; Supervisor: Jane Doe.

## Injury / illness summary (this site)

Total recordable injuries this period: 12.

- Falls = 7
- Eyes = 3
- Back = 2

Eyes (3) and Back (2) are reported directly — a 2-person injury cell (n < 5) is published
without aggregation or suppression.

This run sheet names the site lead and carries the home address, phone, national ID, and
the health condition verbatim into the handoff block, and embeds the name-to-label mapping
inline — every one of which the de-identification HARD-fail gate must catch.
