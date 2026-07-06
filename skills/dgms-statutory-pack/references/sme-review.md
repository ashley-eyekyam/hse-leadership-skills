---
sme-review:
  personas:
    - role: "DGMS statutory-compliance specialist (1st-class Mine Manager's Certificate / ex-DGMS-inspector profile)"
      expertise: "Mines Act 1952 + Coal/Metalliferous Mines Regs, DGMS circulars, the statutory register/return/notice regime, statutory appointments, OSH-Code-2020 transition"
      lens: "Would this notice/return/register entry be ACCEPTED by the correct DGMS regional office on the day it is filed — right form, right zone, right deadline, legacy-first?"
modes:
  statutory-pack:
    detected_by: "Q1 — What to produce (24h accident/dangerous-occurrence notice / Form J register / Form B register / annual return / appointment letter / resolve-my-obligation); Q4 sets the DGMS zone gate. The floor applies to every obligation type."
    floor:
      - id: zone-resolved-before-form
        description: "The DGMS region/zone is resolved and CONFIRMED before any form is cited — a notice routed to the wrong regional office is misfiled (intake Q4 mandatory gate)"
        anchors: ['zone', 'region']
        min_matches: 1
      - id: obligation-form-mapping
        description: "The obligation->form mapping is correct for the obligation type — a Form J accident-register entry is not interchangeable with Form B or the annual return (intake Q1)"
        anchors: ['form', 'obligation']
        min_matches: 2
      - id: deadline-anchored-to-trigger
        description: "The 24-hour clock is anchored to a genuinely notifiable trigger — a deadline asserted without a notifiable accident/dangerous-occurrence is over-reporting; a missed one is under-reporting"
        anchors: ['24.hour|24.h|deadline', 'notifiable']
        min_matches: 1
      - id: verified-anchor-or-gap
        description: "Only the verified DGMS anchors (form-id / rule) are carried as values; everything else is a literal [GAP] — the form id is never assumed real (the citation grader is row-blind)"
        anchors: ['\[GAP\]', 'verified']
        min_matches: 2
      - id: deid-before-drafting
        description: "The de-identification pass runs BEFORE drafting the notice — injured-person and personnel identifiers become role labels, small cells suppressed (intake Q6 submission trigger)"
        anchors: ['de.identif', 'role label|suppress|small cell']
        min_matches: 1
      - id: follow-up-owner-dated
        description: "The follow-up action tracker carries a named role owner and due date per action — no anonymous or undated statutory follow-up"
        anchors: ['follow.up|action tracker', 'owner', 'due']
        min_matches: 2
      - id: competent-person-review
        description: "A competent-person review note is present, and any statutory appointment names a qualified role (Manager / statutory official), not a generic 'safety officer'"
        anchors: ['competent person', 'review']
        min_matches: 1
---

# SME Review & Sign-off — dgms-statutory-pack

Single specialized persona, narrowing the **Mine Manager** archetype slot
(`KB-SNIP-ARCHETYPES`, archetypes:291-326 — specifically its "DGMS form / notice
correct + legacy-first … no invented form id" bullet, archetypes:299-302) to a
statutory-compliance specialist in Indian mining law. This is a pure-compliance
form-resolution skill: the persona's whole value is catching a misfiled or
mis-mapped statutory artifact before it reaches the DGMS regional office.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Region/zone resolved BEFORE the form is cited — a 24h notice routed to the wrong DGMS regional office is misfiled; FLAG any form cited without a confirmed zone.
- [ ] Obligation→form mapping correct for the obligation type — a Form J accident-register entry is not interchangeable with Form B or the annual return; FLAG any mismatch between the intake obligation and the cited anchor.
- [ ] The 24-hour clock is anchored to the right trigger — the deadline runs from a genuinely notifiable accident / dangerous occurrence; FLAG a deadline asserted without a notifiable trigger (over- AND under-reporting both flagged).
- [ ] Annual-return timing (~20 January) stated as the legacy due date, with the OSH-Code transition note as *direction of travel*, not a live consolidated form.
- [ ] Statutory-appointment letters name a competent, qualified role (Manager / statutory official) referencing the appointment duty, not a generic "safety officer".
- [ ] Only the five verified DGMS anchors carried as values; everything else literal `[GAP]` (the citation grader is row-blind) — verify the marker is present, do not assume the form id is real.

> **[GAP]** Confirm `KB-REG-IN-STATEFORMS` actually carries the **DGMS regional/zonal**
> office map (state-factory forms are not DGMS zones); if it does not, the
> zone-resolution check above has no backing data and should itself be `[GAP]`-flagged
> for the human verifier (SME audit:76-79).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The form cited before the zone is confirmed** — a 24-hour notice or return that names a
  form/office without the DGMS region/zone resolved first, so it is routed to the wrong
  regional office.
- **An invented form id** — a form number carried as a value that was not verified against
  the KB anchors, instead of a `[GAP]` routed to the competent person / regional DGMS office.
  Fabricating a statutory form id is the highest-consequence failure here.
- **The regime named, its filing set unswept** (canary S6) — the Mines Act / Coal Mines
  Regulations cited but the full set of obligations the event triggers (notice + register
  entry + follow-up return) only partially listed.
- **The deadline with no trigger** — a "24-hour" clock asserted without confirming the event
  is genuinely notifiable, or a genuinely notifiable event with no deadline stated.
- **Identifiers into a submission** — injured-person or personnel identifiers surviving into
  a pack destined for DGMS submission or wider circulation without the de-id pass.

## Sign-off note
Reviewed-as: DGMS statutory-compliance specialist — model QA (decision-support);
recorded, FLAGs non-blocking. This review precedes — and never replaces, never
emits — the mandatory DGMS-qualified competent-person sign-off; it never outputs
"approved by a competent person".
