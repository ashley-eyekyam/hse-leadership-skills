# Methodology — Lone Working Assessment (HSE INDG73 + BS 8484)

The domain method this skill applies. It grounds the lone-working risk-assessment duty in
`KB-REG-LONE-WORKING` (HSE INDG73 rev 4), the device-service discipline in `KB-STD-BS8484`
(BS 8484:2022), the control order in `KB-SNIP-CHECKIN-ESCALATION`, and the shared rescue spine in
`KB-SNIP-RESCUE-PLAN` (shared with REN-01). Every conclusion is traced to a cited source (INDG73 /
BS 8484) with a named **role** owner and a date; the hierarchy of controls is applied to every
control; no vague or device-only treatment is accepted.

## Step 0 — De-identification FIRST

Before any analysis, the De-identifier scrubs the lone worker's **personal contact number, shift
pattern, and precise work / home location** to **role labels** for the distributed copy
(`references/deid-checklist.md`), and holds the re-identification key separately. This is a
sequential dependency — every step below consumes only the scrubbed inputs.

## Step 1 — Scope the named role / site / solitary activity

Capture (intake Q1/Q3) the **named role + site** and the **specific solitary activity broken into
steps**. Refuse a vague "our lone workers"; the assessment is role-and-task-specific.

## Step 2 — The routing gate (route, do not assess solo)

Run the routing gate before assessing any control:

- **Lone work at height** → route to **`wind-turbine-work-at-height-rescue` (REN-01)**'s
  two-person / **tested-rescue** baseline (`KB-SNIP-RESCUE-PLAN`). A climb is a two-person-minimum
  team with ground support able to initiate a timed, team-owned rescue within minutes (suspension
  trauma); "call 999/112" is **never** the rescue plan. **Lone work at height on a turbine is not
  acceptable** — this skill records the routing pointer and does not assess a solo climb.
- **Lone electrical work** → route to the cross-listed utilities skills (`arc-flash-assessment` /
  `live-working-risk-assessment`). Named as a routing pointer (CONV-12; cross-list wiring deferred
  to Phase 17), never rebuilt or assessed solo here.

## Step 3 — Eliminate the solitary exposure as the lead control

The primary control is to **avoid lone working for the task where reasonably practicable**
(`KB-SNIP-CHECKIN-ESCALATION` step 1, via `controls.py`): pair up, re-schedule to a manned window,
or use remote monitoring so the worker is no longer solitary. A treatment whose headline is
"issue a lone-worker device / panic-button app" is **rejected** and pushed up the hierarchy — the
device is at most a residual supplement, never the control.

## Step 4 — Coverage-checked communication

Specify a **reliable, coverage-checked** communication path AT the work location. **"No mobile
signal in that area" is a control failure, not an accepted residual risk** — fix the comms (a
different bearer, a satellite messenger, a relocated task) or change the task. An unconfirmed
coverage is a `[GAP]` until checked on site.

## Step 5 — Scheduled check-ins + a defined missed-check-in escalation path

Define a **scheduled check-in at a stated interval** AND a **missed-check-in escalation path**: who
responds, by what method, and in what time. An undefined responder or response time is a `[GAP]`,
never left open. A device with no scheduled check-in / escalation procedure is rejected (INDG73 +
`KB-SNIP-CHECKIN-ESCALATION`).

## Step 6 — BS 8484 device as a residual supplement only

Where a lone-worker device is used, ground it on **BS 8484:2022 conformance** (the device + the
monitored alarm-receiving / response chain — `KB-STD-BS8484`), layered **on top of** the check-in /
escalation procedure, never instead of it. The specific device / service is a `[GAP]` until
supplied.

## Step 7 — Violence + stress/wellbeing, residual risk, and SMART actions

Add the **violence-to-staff** and **stress/wellbeing of working alone** controls (INDG73). Score
residual risk on the **`risk_matrix` 5×5** after the lead controls are applied. Close each `[GAP]`
(comms coverage, response time, device/service) with a **SMART action** (`smart_actions`) carrying
a named **role** owner and a due date. Every conclusion cites INDG73 / BS 8484; lone-worker
contact / shift / location is role-labelled, never named, in the circulated copy.

## Cross-references (CONV-12, kept distinct)

- `wind-turbine-work-at-height-rescue` (REN-01) — the WAH plan + mandatory tested rescue this skill
  routes lone work at height to; shares `KB-SNIP-RESCUE-PLAN`.
- `arc-flash-assessment` / `live-working-risk-assessment` — the utilities skills this skill routes
  lone electrical work to.
- `weather-dynamic-risk-assessment` (REN-03) — owns the weather thresholds; this skill defers to it
  for weather-driven stop limits.
- India statutory content defers to the `hse-india` engine via `KB-REG-IN-RENEWABLES` (mandatory
  state detection; no national form minted).
