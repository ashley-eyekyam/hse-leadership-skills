# HSE Skills Roadmap — re-roofing job (recommendation + run sheet)

> CANDIDATE golden output for the recommendation-accuracy eval. Role-based owners only,
> no personal names (golden-output authoring convention). The owner LOCKs this in Phase 17.

## Captured facts (echoed back, de-identified)

De-identification ran FIRST, before this run sheet was written. The pasted handoff note
carried a site lead's name, home address, phone, national ID, and a health condition;
all were detected, listed, and pseudonymized to role labels. The re-identification key is
held in a SEPARATE access-controlled artifact and is NOT reproduced here.

- **Intent / scope:** make a re-roofing job safe end to end (multi-deliverable).
- **Subject:** strip-and-re-roof Block C at [SITE-1], working at height from the eaves.
- **Output / success:** a risk assessment, a safe-work method, a permit, and a toolbox
  talk the crew can sign — "done" = the night crew can start work with all four in hand.
- **Jurisdiction:** UK.  **Industry:** construction.
- **Exposed:** own workers + [CONTRACTOR] roofing crew.  **Lead:** [ROLE: site manager].

Routing for: re-roofing fall-from-height at [SITE-1], own workers + [CONTRACTOR], UK,
construction, deliverables = RA + JSA + permit + toolbox talk — confirmed.

## Recommended chain (ordered, with rationale)

| # | Skill | Bundle | WHY |
|---|---|---|---|
| 1 | risk-assessment | hse-core | Establishes the hazard/control baseline for fall-from-height before any method or permit is written. |
| 2 | job-safety-analysis | hse-core | Breaks the agreed control set into a step-by-step safe-work method the crew can follow. |
| 3 | permit-to-work | hse-core | Authorises the work-at-height task with the controls from Steps 1–2 as permit conditions. |
| 4 | toolbox-talk | hse-core | Briefs and signs off the night crew on the specific hazards and controls before they start. |

## Run sheet (copy-paste — portable across fresh chats or this session)

SEQUENCE MAP:  risk-assessment → job-safety-analysis → permit-to-work → toolbox-talk

── STEP 1 — risk-assessment ──────────────────────────────────
WHY:        Establishes the hazard/control baseline for the re-roofing task at height.
RUN:        /risk-assessment   (or: "use the risk-assessment skill")
THEN PASTE: [shared context: strip-and-re-roof Block C at [SITE-1], fall-from-height,
            own workers + [CONTRACTOR], UK, construction; lead = [ROLE: site manager]]
            + delta: full task steps (access → strip → load-out → re-lay → edge-protect),
            5×5 matrix, baseline assessment.
CARRY-IN:   (none — first step)
DEPENDENCY: Independent.
FEEDS →:    Step 2 (the agreed control set + residual risks).

── STEP 2 — job-safety-analysis ──────────────────────────────
WHY:        Breaks the control set into a step-by-step safe-work method for the crew.
RUN:        /job-safety-analysis
THEN PASTE: [same shared context: re-roofing Block C at [SITE-1], own workers +
            [CONTRACTOR], UK, construction; lead = [ROLE: site manager]]
            + delta: the agreed control set from Step 1.
CARRY-IN:   ⚠ attach the risk-assessment OUTPUT from Step 1 — the control set + residual risks.
DEPENDENCY: Dependent — run after Step 1.
FEEDS →:    Step 3 (the safe-work method steps + control owners).

── STEP 3 — permit-to-work ───────────────────────────────────
WHY:        Authorises the work-at-height task with the Step 1–2 controls as conditions.
RUN:        /permit-to-work
THEN PASTE: [same shared context: re-roofing Block C at [SITE-1], own workers +
            [CONTRACTOR], UK, construction; lead = [ROLE: site manager]]
            + delta: working-at-height permit type, validity window.
CARRY-IN:   ⚠ attach the job-safety-analysis OUTPUT from Step 2 — the method steps + control
            owners — and the risk-assessment residual risks from Step 1.
DEPENDENCY: Dependent — run after Steps 1 and 2.
FEEDS →:    Step 4 (the permitted controls + sign-on conditions).

── STEP 4 — toolbox-talk ─────────────────────────────────────
WHY:        Briefs and signs off the night crew on the specific hazards and controls.
RUN:        /toolbox-talk
THEN PASTE: [same shared context: re-roofing Block C at [SITE-1], own workers +
            [CONTRACTOR], UK, construction; lead = [ROLE: site manager]]
            + delta: tonight's crew, the top three controls to brief.
CARRY-IN:   ⚠ attach the permit-to-work OUTPUT from Step 3 — the permitted controls +
            sign-on conditions the crew must acknowledge.
DEPENDENCY: Dependent — run after Step 3.
FEEDS →:    (none — final step; the crew signs and starts work).

## How to run it

- **On a host with the Skill tool:** say "go" and the router launches Step 1's skill seeded
  with that block; after each step's output returns, it offers the next step.
- **Off-platform / fresh chat:** copy a step block into a new chat and run the named skill;
  for Steps 2–4, attach the prior step's output as the CARRY-IN instructs.

Each target skill's own intake will echo these facts back and ask only the deep, per-artifact
details this router deferred (scoring, baseline, evidence, obligations, competency, cadence).

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
