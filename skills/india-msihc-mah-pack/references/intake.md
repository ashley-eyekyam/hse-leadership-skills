---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "always the chemical-storage/MAH sector — the MSIHC regime fixes the sector; no sector branch to elicit"
  branches:
    - {when: Q4, option: India, activates_questions: [Q5], mandatory: true}
    - {when: Q6, option: PESO, activates_questions: [Q7]}
---

# Structured intake — india-msihc-mah-pack

> **Always-India skill — `ELI-JURIS` is the spine. India→state detection is MANDATORY
> and load-bearing; be rigorous in this branch.**

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a threshold or
a national form). Canonical runtime pattern: `KB-SNIP-INTAKE`.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What do you need — MAH-status verdict, on-site emergency-plan outline, safety-report outline, or the full MSIHC pack? | MCQ | MAH-verdict / on-site-plan / safety-report / full-pack | ELI-SCOPE | always |
| Q2 | Name the site and list each stored/handled hazardous chemical + max quantity on site. | free-text | per-chemical max inventory; refuse "various chemicals" | ELI-SUBJECT | always |
| Q3 | Is each quantity isolated storage or in-process, and are there multiple storage points? | MCQ + free-text | isolated / in-process / both — drives MSIHC aggregation | ELI-SUBJECT | always |
| Q4 | Jurisdiction — this pack is the Indian MSIHC/MAH regime (always India; the next question resolves the state). | MCQ | India | ELI-JURIS | always |
| Q5 | **Which Indian state is the site in?** (MANDATORY — the spine; resolved via `KB-REG-IN-STATEFORMS`, confirm before citing any form) | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other · Unknown — mandatory state detection; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | always — mandatory |
| Q6 | Which storage/handling licences are held? | MCQ multi-select | PESO / SMPV / gas-cylinder / state Factories registration / consent-to-operate (PCB) / none | ELI-OBLIGATIONS | always |
| Q7 | Is the site already a registered/notified MAH? Any MSIHC notifications already filed? | MCQ | yes / no / partial | ELI-BASELINE | always |
| Q8 | Population/receptors within the credible off-site impact zone? | MCQ + free-text | residential / public / none / unknown | ELI-EXPOSURE | always |
| Q9 | Existing on-site emergency plan? | MCQ | yes / no / partial | ELI-BASELINE | always |
| Q10 | Site plot plan / population map — held, and the site location for off-site framing? | free-text | plot plan + receptor proximity | ELI-LOCATION | always |
| Q11 | Who is the occupier / factory manager named for statutory duties? | free-text | role-label owner | ELI-COMPETENCY | always |
| Q12 | Any upcoming statutory deadlines — safety-report due, mock-drill, licence renewal? | free-text | dates | ELI-TEMPORAL | always |
| Q13 | Org rating/priority scheme for the MAH-tier verdict and `[GAP]` escalation. | MCQ | org scheme / default — flag every unresolved threshold/form | ELI-SCORING | always |

**Branch map (all India)**
- **`Q5` is the spine** → resolves the state form set via `KB-REG-IN-STATEFORMS`; **confirm state before citing any form**; activates the state's notification/return KB rows. "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback.
- `Q2/Q3` inventory vs MSIHC Schedule (`KB-REG-IN-MSIHC`) → computes the **MAH tier**:
  - below threshold → not-MAH verdict, advisory only;
  - storage-notification tier → activates notification questions + form;
  - MAH tier → activates on-site emergency plan + safety report output sections (**mandatory**);
  - + off-site receptors present (`Q8≠none`) → activates off-site-plan pointer to the District authority.
- `Q6 ∈ {PESO, SMPV, gas}` → activate `KB-REG-IN-PESO` licensing pointers (hse-process owns; referenced by ID).
- Unresolved threshold/form → `[GAP]`, never invent a threshold or national form (METHODOLOGY). Unverified MSIHC/MAH form-id stays literal `[GAP]` + reason + verification path; never invented.
- OSH-Code transition note appended in all cases (legacy-first).

## Echo-back
> "Site **{site}**, **state {state} (confirmed)**; inventory **{chemicals/qty}**, storage **{isolated/in-process}**; existing MAH status **{y/n/partial}**; licences **{list}**; off-site receptors **{y/n}**; existing plan **{status}**; occupier **{role}**; deadlines **{dates}**. I will compare the inventory to the MSIHC Schedule to set the MAH tier, cite only the **{state}**-resolved form, outline the required plan/report, and flag any unresolved threshold `[GAP]`. The OSH-Code transition is noted. Confirm before I proceed."

Echo the captured facts back and **confirm before the MAH verdict**. The occupier /
factory manager is held as a role label in the echo-back (DPDP de-id).

## Refuse-on-vague anchors
- **No state → cannot proceed; state detection is mandatory** (METHODOLOGY step 2); the state is the specificity anchor for every citation — **never proceed on a vague subject**.
- "various hazardous chemicals" → demand named chemical + quantity (the MAH verdict is quantity-driven).
- No statutory national form assumed — only the state-resolved form is cited; an unverified form-id is literal `[GAP]`.

**Domain evidence types (`ELI-EVIDENCE`)**
Chemical inventory register with max quantities, MSIHC Schedule entries, existing MAH notifications / Form filings, PESO/SMPV licences, PCB consent-to-operate, site plot plan + population map, prior safety report / on-site emergency plan.

**[GAP]** "Other"/"Unknown" state branch — `KB-REG-IN-STATEFORMS` seeds TN/KA/MH/DL/GJ for v1.0 (India-breadth deferral; the GJ annual-return form itself ships as a literal `[GAP]` pending owner verification). For an "Other"/"Unknown" state the form resolution is **literal `[GAP]` + route-to-competent-person**, never a silent national-form fallback. Any unverified MSIHC/MAH form-id stays literal `[GAP]` + reason. Verification path: owner verifies the state legacy form pre-launch; do not fabricate state form numbers (intake audit `:239`).
