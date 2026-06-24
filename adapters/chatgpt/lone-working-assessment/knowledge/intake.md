---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A lone-working assessment is built afresh from the named role/site, the specific solitary activity (Q1/Q3) and the supplied comms-coverage + check-in facts (Q4/Q5); there is no prior quantitative baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the activity and the comms/check-in arrangement are the assessment's starting facts."
    ELI-EVIDENCE: "The evidence types are folded into the activity (Q3), comms-coverage (Q4) and check-in/escalation (Q5) questions rather than asked as a separate dimension; the domain evidence list is documented in the Domain evidence types section below."
    ELI-SCORING: "Residual risk is framed on the standard risk_matrix 5x5 (a fixed scale, not a user-chosen one), and the lone-working control order is a qualitative hierarchy gate, not a numeric scoring scale — so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q3, option: Work at height, activates_questions: [Q3a], activates_kb_row: KB-SNIP-RESCUE-PLAN, mandatory: true}
    - {when: Q3, option: Electrical work, activates_questions: [Q3b], mandatory: true}
    - {when: Q2, option: India, activates_questions: [Q2a], activates_kb_row: KB-REG-IN-RENEWABLES, mandatory: true}
---

# Structured intake — lone-working-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where
the answer space is enumerable and free-text where it is open; branch on the answers; **echo
the captured facts back for confirmation before any analysis**. The intake opens with the
**named role / site (Q1 — the specificity anchor)**, then the **jurisdiction (Q2)**, the
**specific solitary activity (Q3 — and the routing trigger: work at height / electrical)**, the
**comms coverage at the work location (Q4 — the "no mobile signal is a control failure" check)**,
the **check-in interval + missed-check-in escalation path (Q5)**, the **proposed controls
(Q6 — the core-value gate)**, and the output / owner / review questions. **Refuse to "sort out
our lone working": you need the named role/site (Q1) and the specific solitary activity (Q3)
before any analysis. Refuse a "just issue a lone-worker device / panic-button app" treatment as
the headline control** — the assessment is led by eliminating the solitary exposure first, then a
scheduled check-in + a defined missed-check-in escalation path; a device is a residual supplement.

Two load-bearing branches: the **routing branch** (Q3 = Work at height → Q3a → route to REN-01
`wind-turbine-work-at-height-rescue`'s two-person / tested-rescue baseline, never a solo climb;
Q3 = Electrical work → Q3b → route to the cross-listed utilities skills, never assessed solo
here), and the **mandatory India→state branch** (Q2 = India → Q2a + `hse-india`; confirm the
state before citing any rule — never a national form number, emit `[GAP]` where a state return
is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | **Scope of this assessment** | mcq | A single lone-working task / activity / single lone worker / a role's whole lone-working pattern / a site-wide lone-working policy review | ELI-SCOPE | always |
| Q1 | **The named role / site** (the specificity anchor) | free-text | "Name the exact role + site / area (e.g. 'O&M technician, Wind Farm WF-7, met-mast inspection'). **Refuse 'our lone workers' / 'the team' — the assessment is role-and-task-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Jurisdiction** (selects the lone-working duty map) | mcq | UK (HSE INDG73) / India / Other / Unknown | ELI-JURIS | always |
| Q2a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q2 == India |
| Q3 | **The specific solitary activity** (and the routing trigger) | mcq+free-text | Ground-level field / inspection work alone / Work at height / Electrical work / Driving & remote site visits / Other (+ describe the task in steps) | ELI-EXPOSURE | always |
| Q3a | *(Work at height only)* Route to REN-01 | mcq→confirm | "Lone work at height is **not** assessed solo here — it routes to `wind-turbine-work-at-height-rescue` (REN-01)'s two-person / tested-rescue baseline (`KB-SNIP-RESCUE-PLAN`). Confirm to record the routing pointer." | ELI-OBLIGATIONS | Q3 == Work at height |
| Q3b | *(Electrical work only)* Route to the utilities skills | mcq→confirm | "Lone electrical work is **not** assessed solo here — it routes to the cross-listed utilities skills (`arc-flash-assessment` / `live-working-risk-assessment`). Confirm to record the routing pointer." | ELI-OBLIGATIONS | Q3 == Electrical work |
| Q4 | **Comms coverage at the work location** (the control-failure check) | free-text | "What communication is available AT the work location, and is the coverage checked there? **A 'no mobile signal in that area' answer is a control failure, not an accepted residual risk — fix the comms or change the task; record a `[GAP]` until coverage is confirmed.**" | ELI-LOCATION | always |
| Q5 | **Check-in interval + missed-check-in escalation path** | free-text | "What is the scheduled check-in interval, and what happens if a check-in is missed — who responds, how, and in what time? **An undefined responder or response time is a `[GAP]`, never left open; a device with no scheduled check-in / escalation procedure is rejected.**" | ELI-OBLIGATIONS | always |
| Q6 | **Proposed controls** (the core-value gate) | free-text | "What controls are proposed? **A 'we'll issue a lone-worker device / panic-button app' as the HEADLINE control is a FLAG pushed up the hierarchy** — lone working is led by eliminating the solitary exposure (pair up / re-schedule / remote monitoring); a BS 8484 device is at most a residual supplement on top of the check-in / escalation procedure." | ELI-OBLIGATIONS | always |
| Q7 | Industry / setting | mcq+free-text | Renewables (wind / solar O&M) / Utilities & infrastructure / Field service & maintenance / Mixed (+ detail) | ELI-INDUSTRY | always |
| Q8 | Output artifact wanted + its reader | mcq | full lone-working risk assessment (consultant) / lone-working procedure + check-in/escalation summary (manager) / the field check-in card (frontline) | ELI-OUTPUT | always |
| Q9 | **Action owner(s) + verifier** | free-text | "Who owns the eliminate-the-exposure / check-in-setup / `[GAP]`-closure actions and who is the competent person reviewing the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q10 | **Review cycle / next review** | mcq+free-text | on-task-change / on-comms-coverage-change / on-incident / quarterly (or sooner) / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `routing-wah` (Q3 = Work at height → Q3a → REN-01 two-person / tested-rescue
baseline, never a solo climb); `routing-electrical` (Q3 = Electrical work → Q3b → the
cross-listed utilities skills, never assessed solo here); `india-state` (Q2 = India → Q2a +
`hse-india`; **mandatory** — confirm the state before citing any rule; emit `[GAP]`, never a
national form number).

## Echo-back

After the last applicable question (Q10, plus Q2a / Q3a / Q3b if their branches ran), **echo a
captured-facts summary** and confirm before any analysis:
"Assessing lone working for: O&M technician, Wind Farm WF-7, met-mast inspection (UK, INDG73);
solitary activity = ground-level inspection (not work at height — a WAH element would route to
REN-01); comms coverage at the met mast NOT confirmed → [GAP] (control failure until fixed);
proposed check-in = hourly with escalation to the site lead within 30 min of a missed check-in;
proposed controls led by re-scheduling to a paired window, device as a residual supplement; full
lone-working risk assessment; review on task change — correct?" The lone worker's contact / shift
/ location is then de-identified to role labels before drafting.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "our lone workers" / "the team"; ask again or record
  `[GAP]`, never invent the role or its task.
- **Eliminate the solitary exposure first, device last** — a treatment whose headline is "issue a
  lone-worker device / panic-button app" is **refused and pushed up the hierarchy**; lone working
  is led by eliminating the solitary exposure (pair up / re-schedule / remote monitoring), and a
  device is at most a residual supplement on top of the check-in / escalation procedure.
- **"No mobile signal" is a control failure** — a comms-coverage gap (Q4) is never accepted as a
  residual risk; record a `[GAP]` and require the comms fixed or the task changed.
- **A missed check-in needs a defined responder + time** — an undefined responder or response time
  (Q5) is a `[GAP]`, never left open. **Never proceed on a vague input.**
- **Lone WAH / electrical is routed, never assessed solo** — Q3 = Work at height routes to REN-01's
  two-person / tested-rescue baseline; Q3 = Electrical work routes to the cross-listed utilities
  skills; neither is assessed solo here.

## Domain evidence types (ELI-EVIDENCE)

The specific solitary activity broken into steps (Q3) · the comms coverage checked AT the work
location (Q4 — else a `[GAP]`) · the scheduled check-in interval + the missed-check-in escalation
path (Q5 — responder / method / response time, else a `[GAP]`) · the proposed controls (Q6 —
eliminate-first, device-led flagged) · any BS 8484 lone-worker device / monitored-response-chain
detail (residual supplement only; the specific device/service is a `[GAP]` until supplied) · any
prior lone-working incident / assault / collapse context (de-identified to role label) · the
lone worker's personal contact / shift / location (de-identified to role labels — moderate
sensitivity, scrubbed before drafting).
