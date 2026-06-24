# Methodology — workplace-violence-prevention (environmental-and-administrative-first, PHI-protected)

The domain method `workplace-violence-prevention` applies. Its spine is **the worksite hazard
analysis and environmental-and-administrative controls first** (`KB-SNIP-WPV-CONTROLS` +
`KB-SNIP-HOC`): record the de-identified worksite analysis, then design out the exposure with
environmental / engineering controls (controlled access, sightlines, alarms / duress, secure
design), then administrative controls (staffing / skill-mix, lone-working, flagging, procedures),
with **de-escalation, response training, and personal alarms as the documented last lines**. A WPV
program that **leads with "personal alarms / self-defence training"** where the exposure could be
designed out is a **FLAG pushed up the hierarchy, never the headline control**. There is **no
calculation** — WPV control is a structured environmental-and-administrative-control-first method
over the named service's worksite analysis + the cited OSHA 3148 / §5(a)(1) / Cal-OSHA framework.

## 0. De-identify first (the highest-PHI step — named victim / assailant / known-risk patient)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Workplace-violence
incident data is **special-category health data (PHI)**. Scrub any **named victim, assailant, or
known-risk patient** (role labels only — "Worker A", "the patient", "a visitor"; never circulated),
any **behavioural-health flag** (reduced to a de-identified clinical mechanism held in a separate
confidential record), and any **patient identifier**. Apply `<5` small-cell suppression (with
secondary suppression) to every incident category — a 2-incident category on a named ward
de-anonymizes the people involved. **The skill emits NO re-identification key file** — the key is an
instruction to the competent person (held separately, access-controlled). The De-identifier subagent
runs FIRST; everything downstream consumes only its scrubbed output.

## 1. Scope the named service & exposure (Q1)

- **Named service & exposure (Q1)** — the exact unit/service (ED, mental-health unit, reception /
  triage, community / lone home-visit, ambulance, care home) **and where / when violence occurs**.
  **Refuse "a hospital" / "the ward"** (the specificity anchor). A missing service or exposure is a
  `[GAP]`, never invented.

## 2. Classify the violence type(s) — the type-1-4 taxonomy (Q2)

Classify the exposure by the **OSHA / NIOSH type-1-4 taxonomy** because each type drives a different
control set: **type 1** criminal-intent (robbery / intrusion — secure design, access control),
**type 2** customer / patient / client (the dominant healthcare type — triage design, flagging,
staffing, de-escalation), **type 3** worker-on-worker (reporting culture, behavioural standards),
**type 4** personal-relationship (domestic violence spilling into work — workplace safety planning,
access control). Mis-applying the taxonomy is a citation hard-fail.

## 3. Worksite hazard analysis — de-identified, the basis of every control (Q3)

Record the **worksite hazard analysis** (`KB-REG-WPV-OSHA3148` element 2) — the records / incident
review, the walkthrough findings, the employee survey — using **de-identified, aggregated incident
data, never a named victim or assailant**. A program with **no worksite hazard analysis fails** —
the analysis is the basis of every control and the defensibility anchor.

## 4. Rank the controls — environmental & administrative BEFORE reactive (the spine) (Q4/Q5)

This is the core lever. Run the `controls` engine. The control narrative **always leads with the
worksite analysis** → **environmental / engineering** (controlled access & egress, sightlines /
reception design, alarm / duress / panic systems, CCTV, secure design of high-risk areas) →
**administrative** (staffing / skill-mix, lone-working procedures, de-identified
known-risk-patient flagging, visitor management, no-retaliation reporting culture, post-incident
support) → **de-escalation / response training + personal alarms LAST**. A WPV program whose
headline control is **"issue personal alarms + self-defence training" with no access-control,
sightline, alarm-system, or staffing / lone-working control** (`controls.validate_treatment`
returning `ppe_admin_only=True`) is a **FLAG pushed up the hierarchy, never the headline control**.
Frame the qualitative residual violence risk via `risk_matrix`.

## 5. De-escalation, response, training & the de-identified incident log (Q5)

Author the **de-escalation & response protocol** (de-escalation procedure, response / security
protocol, response teams), the **post-incident support** (debrief, occupational-health / EAP
referral, no-retaliation), and the **training plan** — as the documented **residual** lines. Build
the **confidential WPV incident log structure** per the OSHA 3148 recordkeeping element / Cal-OSHA
8 CCR 3342 violent-incident log — the fields (date, type, location, antecedents, controls in place,
outcome) — but in the **circulated** artifact the log is **structural / aggregated**, never
line-level identified. Apply the `<5` small-cell suppression with the secondary back-calculation
guard to every category (by unit, ward, job, type, or period).

## 6. SMART actions + the report

Every access-control install / alarm provision / staffing change / de-escalation-training action
becomes a SMART action (named role owner + ISO due date + measure), validated by
`smart_actions.validate_register`. Validate the draft against `references/QUALITY_CHECKLIST.md`,
then assemble `assets/workplace-violence-prevention.report.json` and run the canonical
`report-output` call.

## Jurisdiction

US **OSHA Publication 3148 (2016)** (the five program elements — management commitment & worker
participation / worksite analysis / hazard prevention & control / training / recordkeeping &
evaluation) enforced under the **OSH Act §5(a)(1) General Duty Clause** is the default duty;
in **California** cite **Cal/OSHA 8 CCR 3342** as the **binding standard** (written plan, type-1-4
taxonomy, employee involvement, violent-incident log). The UK leg is the **HSE management of
work-related violence** guidance + **NICE NG10** (violence & aggression: short-term management).
For India, resolve the state via `hse-india` (**mandatory state detection**) per the occupational
-safety provisions, and emit a literal `[GAP]` where a state return is owed — **never a minted
national form number**.
