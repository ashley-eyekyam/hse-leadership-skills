---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A turbine work-at-height + rescue plan is built afresh from the named turbine/site (Q1), the specific WAH activity broken into steps (Q3) and the proposed access/rescue arrangement (Q5/Q6); there is no prior quantitative baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the activity, the access method and the rescue arrangement are the plan's starting facts."
    ELI-EVIDENCE: "The evidence types are folded into the WAH activity (Q3), the avoid-then-prevent control arrangement (Q4), the rescue arrangement (Q5) and the climb-team/competence (Q6) questions rather than asked as a separate dimension; the domain evidence list is documented in the Domain evidence types section below."
    ELI-SCORING: "Residual risk is framed on the standard risk_matrix 5x5 (a fixed scale, not a user-chosen one), and the reg-6 control order (avoid -> prevent collective -> mitigate/arrest) plus the mandatory-tested-rescue gate are qualitative hierarchy gates, not a numeric scoring scale — so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q3, option: Lone single-climber activity, activates_questions: [Q3a], activates_kb_row: KB-SNIP-RESCUE-PLAN, mandatory: true}
    - {when: Q7, option: Weather-sensitive hold-or-stop threshold needed, activates_questions: [Q7a], activates_kb_row: KB-DATA-WEATHER-THRESHOLDS, mandatory: true}
    - {when: Q2, option: India, activates_questions: [Q2a], activates_kb_row: KB-REG-IN-RENEWABLES, mandatory: true}
---

# Structured intake — wind-turbine-work-at-height-rescue

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named turbine / site (Q1 — the specificity anchor)**, then the **jurisdiction (Q2)**, the
**specific WAH activity (Q3 — nacelle/hub/blade/tower-internal, and the lone-climber routing
trigger)**, the **avoid-then-prevent control arrangement (Q4 — the reg-6/7 gate: has avoidance
been tested? is collective protection used before personal?)**, the **rescue arrangement (Q5 —
the core-value gate: a tested, team-owned recovery in minutes; "call 999" is refused)**, the
**climb-team manning + GWO competence (Q6)**, the **weather hold/stop thresholds (Q7 — named
here, owned by REN-03)**, and the output / owner / review questions. **Refuse to "sort out
working at height on the turbines": you need the named turbine/site (Q1) and the specific WAH
activity (Q3) before any analysis. Refuse a "call 999 / wait for emergency services" rescue
arrangement (Q5) as the rescue plan** — the plan is led by avoiding work at height first, then
preventing a fall (collective before personal), then a MANDATORY tested two-person recovery in
minutes; emergency services are a supplement, never the rescue plan.

Three load-bearing branches: the **lone-climber routing branch** (Q3 = lone / single-climber →
Q3a → the two-person-minimum baseline is restored; a solo climb is refused, `KB-SNIP-RESCUE-PLAN`),
the **weather-threshold branch** (Q7 = weather-sensitive → Q7a → name the threshold but defer its
ownership to REN-03 `weather-dynamic-risk-assessment`; the ≈15 m/s hub-height cut-off is
`[ASSUMED A4]`, proposed-and-user-confirmed, never invented), and the **mandatory India→state
branch** (Q2 = India → Q2a + `hse-india`; confirm the state before citing any rule — never a
national form number, emit `[GAP]` where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | **Scope of this plan** | mcq | A single WAH task on one turbine / a campaign of WAH tasks across a site / a turbine WAH + rescue procedure / a site-wide WAH+rescue standard review | ELI-SCOPE | always |
| Q1 | **The named turbine / site** (the specificity anchor) | free-text | "Name the exact turbine + site / area (e.g. 'WTG-12, Wind Farm WF-7, nacelle gearbox inspection'). **Refuse 'the turbines' / 'our wind farm' — the plan is turbine-and-task-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Jurisdiction** (selects the work-at-height duty map) | mcq | UK (WAH Regs 2005) / India / Other / Unknown | ELI-JURIS | always |
| Q2a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q2 == India |
| Q3 | **The specific WAH activity** (and the lone-climber routing trigger) | mcq+free-text | Nacelle or drivetrain work / Hub or spinner work / Blade access (rope or platform) / Tower-internal (ladder or lift) / Lone single-climber activity / Other (+ describe the task in steps) | ELI-EXPOSURE | always |
| Q3a | *(Lone single-climber only)* Restore the two-person baseline | mcq→confirm | "A solo climb is **not** acceptable here — turbine WAH is a **two-person-minimum** team with ground support able to initiate a tested rescue (`KB-SNIP-RESCUE-PLAN`). Confirm to restore the two-person baseline (this aligns with REN-02 `lone-working-assessment`, which routes lone WAH here)." | ELI-OBLIGATIONS | Q3 == Lone single-climber activity |
| Q4 | **Avoid-then-prevent control arrangement** (the reg-6/7 gate) | free-text | "Has **avoiding work at height** been tested (do it at ground level / lower the component / use a man-rider or platform)? Where work at height is unavoidable, is **collective fall-prevention** (guardrails / working platform) used **before personal fall-arrest**? **A jump straight to fall-arrest/PPE where avoidance or collective prevention is reasonably practicable is a FLAG pushed up the hierarchy** (reg 6/7); record a `[GAP]` until the avoidance test is evidenced." | ELI-OBLIGATIONS | always |
| Q5 | **Rescue arrangement** (the core-value gate) | free-text | "What is the rescue plan for a worker suspended in a harness? **A 'call 999 / wait for the emergency services' answer is REJECTED as the rescue plan** — it is a supplement only. The rescue must be a **tested, team-owned capability that recovers a suspended worker within minutes** (suspension trauma) by a two-person-minimum team with ground support (`KB-SNIP-RESCUE-PLAN`, `KB-STD-GWO-WAH-RESCUE`). An untested capability or an unstated recovery time is a `[GAP]`, never left open." | ELI-OBLIGATIONS | always |
| Q6 | **Climb-team manning + GWO competence** | free-text | "Who is on the climb team (two-person-minimum + ground support), and what is their GWO competence? **Cite the GWO competence *requirement* (current WAH / First Aid / ART, 2-yr refresh) — do NOT record certificate numbers in the circulated copy** (licensed; de-identified to role labels, `[GAP]` for the cert detail)." | ELI-COMPETENCY | always |
| Q7 | **Weather hold or stop thresholds** (named here, owned by REN-03) | mcq+free-text | Weather-sensitive hold-or-stop threshold needed / Not weather-sensitive for this task (+ which conditions: wind, lightning, ice, visibility) | ELI-LOCATION | always |
| Q7a | *(Weather-sensitive only)* Name + defer to REN-03 | mcq→confirm | "Name the hold or stop threshold (e.g. hub-height wind cut-off ≈ **15 m/s** `[ASSUMED A4]`, lightning stand-down) but **defer its ownership to REN-03 `weather-dynamic-risk-assessment` (`KB-DATA-WEATHER-THRESHOLDS`)** — the ≈15 m/s value is proposed-and-user-confirmed, never embedded as a citation. Confirm the site value or record `[GAP]`." | ELI-OBLIGATIONS | Q7 == Weather-sensitive hold-or-stop threshold needed |
| Q8 | Industry / setting | mcq+free-text | Onshore wind / Offshore wind / Solar (elevated structures) / Mixed renewables (+ detail) | ELI-INDUSTRY | always |
| Q9 | Output artifact wanted + its reader | mcq | full WAH + rescue plan / risk assessment (consultant) / WAH method + rescue-plan summary (manager) / the pre-climb / rescue brief card (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the avoid-the-height / collective-protection / tested-rescue / `[GAP]`-closure actions and who is the competent person reviewing the plan (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | on-task-change / on-equipment-or-anchor-change / on-incident / before-each-campaign (or sooner) / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `routing-lone-climber` (Q3 = lone / single-climber → Q3a → restore the
two-person-minimum baseline, never a solo climb, `KB-SNIP-RESCUE-PLAN`); `weather-threshold`
(Q7 = weather-sensitive → Q7a → name the threshold + defer to REN-03 `KB-DATA-WEATHER-THRESHOLDS`;
the ≈15 m/s value is `[ASSUMED]`, proposed-and-confirmed); `india-state` (Q2 = India → Q2a +
`hse-india`; **mandatory** — confirm the state before citing any rule; emit `[GAP]`, never a
national form number).

## Echo-back

After the last applicable question (Q11, plus Q2a / Q3a / Q7a if their branches ran), **echo a
captured-facts summary** and confirm before any analysis:
"Producing a work-at-height + rescue plan for: WTG-12, Wind Farm WF-7, nacelle gearbox inspection
(UK, WAH Regs 2005); WAH activity = nacelle / drivetrain work (two-person climb confirmed);
avoidance tested = component cannot be lowered → work at height unavoidable, collective platform
used before personal fall-arrest; rescue = tested team-owned recovery within ~10 min by a
two-person team with ground support ('call 999' is a supplement only); GWO competence cited
(certificate numbers de-identified); hub-height wind hold ≈ 15 m/s [ASSUMED — confirm with REN-03,
proposed-and-user-confirmed]; full WAH + rescue plan; review before each campaign — correct?" The
climbers' names + GWO certificate numbers are then de-identified to role labels before drafting.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "the turbines" / "our wind farm"; ask again or record
  `[GAP]`, never invent the turbine or its WAH task.
- **Avoid the height first, collective before personal** — a treatment whose headline is
  fall-arrest / PPE where avoidance or collective prevention is reasonably practicable is
  **refused and pushed up the hierarchy** (reg 6/7); the plan is led by avoiding work at height,
  then collective fall-prevention, then personal fall-arrest.
- **"Call 999" is never the rescue plan** — a rescue arrangement whose lead is "phone the
  emergency services and wait" is **refused**; the rescue must be a tested, team-owned recovery in
  minutes by a two-person-minimum team, with emergency services as a supplement only. An untested
  capability or unstated recovery time is a `[GAP]`.
- **GWO competence is cited, certificate numbers are not** — the GWO competence requirement is
  cited; certificate numbers are licensed and de-identified to role labels (`[GAP]` for the cert
  detail). **Never proceed on a vague input.**
- **Weather thresholds are named, never owned here** — Q7 names a hold/stop threshold and defers
  its ownership to REN-03; the ≈15 m/s hub-height cut-off is `[ASSUMED]`, proposed-and-confirmed,
  never invented as a hard citation.

## Domain evidence types (ELI-EVIDENCE)

The specific WAH activity broken into steps (Q3) · the avoidance test (Q4 — can it be done at
ground level / lowered / man-rider, else a FLAG/`[GAP]`) · the collective-before-personal
fall-protection arrangement (Q4 — reg 7) · the rescue arrangement (Q5 — tested, team-owned,
recovery time; an "emergency-services-alone" answer is refused, an unstated time is a `[GAP]`) ·
the climb-team manning + GWO competence (Q6 — two-person-minimum; certificate detail de-identified
/ `[GAP]`) · the named weather hold/stop thresholds (Q7 — owned by REN-03; ≈15 m/s `[ASSUMED]`) ·
the anchor points / fall-protection / rescue equipment (`[GAP]` until supplied) · any prior fall /
suspension / rescue incident context (de-identified to role label) · the climbers' names + GWO
certificate numbers (de-identified to role labels — moderate sensitivity, scrubbed before drafting).
