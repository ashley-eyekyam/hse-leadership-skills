# HSE Skills Roadmap — re-roofing job (recommendation + run sheet)

> CANDIDATE golden output for the recommendation-accuracy eval. Role-based owners only,
> no personal names (golden-output authoring convention). The owner LOCKs this in Phase 17.

## HOW THIS WORKS — read me first

You have confirmed the job context below. This run sheet has been **saved as a durable
markdown file** so you can keep it open while you work — it is your Steps-2+ plan, and it
survives Step 1 filling this chat. We will run **STEP 1 right here in this chat** — but only
once you have the saved run sheet and say **go**, because the first skill does the heavy lifting
and fills this chat with detail. For each later step, open a **fresh chat** and paste the
**Context Capsule** so the new chat knows the site, crew, and jurisdiction without re-asking —
then attach the previous step's output where the step notes. That keeps each chat fast and
focused. Every output you carry forward is already de-identified by the skill that produced it,
so attach the skill's emitted output, not raw notes, and the chain stays clean.

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

*You confirmed this context as-is. If anything were wrong, you could edit it or re-scope, and
the recommended chain would re-run on the change (showing what it refined and why) before any
skill ran.*

## Recommended chain (ordered, with rationale)

| # | Skill | Bundle | WHY |
|---|---|---|---|
| 1 | risk-assessment | hse-core | Establishes the hazard/control baseline for fall-from-height before any method or permit is written. |
| 2 | job-safety-analysis | hse-core | Breaks the agreed control set into a step-by-step safe-work method the crew can follow. |
| 3 | permit-to-work | hse-core | Authorises the work-at-height task with the controls from Steps 1–2 as permit conditions. |
| 4 | toolbox-talk | hse-core | Briefs and signs off the night crew on the specific hazards and controls before they start. |

## Context Capsule  (paste this at the top of each fresh chat for Steps 2+)

> Job: strip-and-re-roof Block C at [SITE-1], fall-from-height from the eaves.
> Jurisdiction: UK · Industry: construction · Exposed: own workers + [CONTRACTOR].
> Lead: [ROLE: site manager]. Goal: risk assessment → safe-work method → permit → toolbox talk.
> SEQUENCE MAP:  risk-assessment → job-safety-analysis → permit-to-work → toolbox-talk
> (Role labels only — the re-identification key is held separately, not in this capsule.)

## Saved run sheet — review this before Step 1 runs

**Saved to:** `hse-run-sheet-re-roofing.md` — this complete run sheet (the Context Capsule, the
ordered chain, the Step-1 record, and every Steps-2+ continuation prompt below) has been written
as a durable markdown file. Keep it open in a separate tab; it is your Steps-2+ plan and it
survives Step 1 filling this chat. *(On a chat-only host with no file-write tool, the same run
sheet is presented as one clearly-delimited copy-paste save-block — "save this as your Steps-2+
run sheet" — instead of a written file.)*

**Clearance:** review this saved run sheet, then say **'go'** (or 'proceed' / 'run step 1') to
run Step 1 here, or **'edit'** to change the context or chain first. Step 1 does not start until
you clear it — on every host.

## Run sheet (asymmetric — Step 1 in place, Steps 2+ in fresh chats)

▶ **STEP 1 runs in THIS chat — no copy-paste, and only on your clearance.** Steps 2–4 each go to
a fresh chat with the Context Capsule above pasted at the top.

── STEP 1 — risk-assessment  (runs here, in place) ───────────
WHY:        Establishes the hazard/control baseline for the re-roofing task at height.
RUN:        /risk-assessment   (or: "use the risk-assessment skill") — in THIS chat.
DELTA:      full task steps (access → strip → load-out → re-lay → edge-protect), 5×5 matrix,
            baseline assessment.
DEPENDENCY: Independent — the first step.
FEEDS →:    Step 2 (the agreed control set + residual risks).

── STEP 2 — job-safety-analysis  (fresh chat) ────────────────
WHY:        Turns the agreed controls into a step-by-step safe-work method.
RUN:        /job-safety-analysis
REFERENCE:  Paste the Context Capsule above first — the skill's intake confirms it and asks
            only the JSA-specific details, so you do not re-enter the site or crew.
ATTACH:     the risk-assessment OUTPUT from Step 1 — the control set + residual risks (it is
            already de-identified by the risk-assessment skill). The JSA is built from these.
DELTA:      the agreed control set; the task broken into method steps.
DEPENDENCY: Dependent — run after Step 1.
FEEDS →:    Step 3 (the method steps + control owners).

── STEP 3 — permit-to-work  (fresh chat) ─────────────────────
WHY:        Authorises the work-at-height task with the Step 1–2 controls as conditions.
RUN:        /permit-to-work
REFERENCE:  Paste the Context Capsule above first — no need to re-enter the shared context.
ATTACH:     the job-safety-analysis OUTPUT from Step 2 — the method steps + control owners —
            and the risk-assessment residual risks from Step 1 (both already de-identified).
DELTA:      the working-at-height permit type and the validity window.
DEPENDENCY: Dependent — run after Steps 1 and 2.
FEEDS →:    Step 4 (the permitted controls + sign-on conditions).

── STEP 4 — toolbox-talk  (fresh chat) ───────────────────────
WHY:        Briefs and signs off the night crew on the specific hazards and controls.
RUN:        /toolbox-talk
REFERENCE:  Paste the Context Capsule above first — the crew, site, and chain are carried by it.
ATTACH:     the permit-to-work OUTPUT from Step 3 — the permitted controls + sign-on conditions
            the crew must acknowledge (already de-identified by the permit-to-work skill).
DELTA:      tonight's crew and the top three controls to brief.
DEPENDENCY: Dependent — run after Step 3.
FEEDS →:    (none — final step; the crew signs and starts work).

      ↳ Can't carry the capsule between chats? Ask to **expand any step to standalone** and the
        router inlines the full shared context into that one step so it self-runs without the
        capsule. The default lean form above keeps each chat short and the de-id surface small.

## How to run it

- **Step 1, here (only on your clearance):** once you have the saved run sheet, on a host with
  the Skill tool, say "go" and the router launches the risk-assessment skill in this chat seeded
  with the confirmed facts. Off-platform, paste the printed Step-1 block into this same chat and
  run the named skill — Step 1 is never a fresh-chat block, and it never auto-fires before you
  clear it.
- **Steps 2–4, fresh chat each:** open a new chat, paste the Context Capsule at the top, run
  the named skill, and attach the prior step's already-de-identified output as the step's
  ATTACH line notes. A fresh chat per step stays fast and focused.

Each target skill's own intake echoes the capsule facts back and asks only the deep,
per-artifact details this router deferred (scoring, baseline, evidence, obligations,
competency, cadence).

*Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com*
