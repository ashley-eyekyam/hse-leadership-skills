---
name: lone-working-assessment
description: Produce a consultant-grade lone-working risk assessment for a named role/site
  and the specific solitary activity, grounded in HSE INDG73 (rev 4) and BS 8484:2022.
  Use this skill to assess lone or solo working, build a lone-working risk assessment,
  set up scheduled check-ins and a missed-check-in escalation path, specify a coverage-checked
  communication plan, or evaluate a lone-worker device/app for renewables and field
  work. It leads with ELIMINATING the solitary exposure first (pair up, re-schedule,
  remote monitoring), then a reliable scheduled check-in with a defined missed-check-in
  escalation path; a BS 8484 device SUPPLEMENTS but never replaces the procedure,
  and 'no mobile signal' is a control failure, not an accepted risk. It routes lone
  work at height to wind-turbine-work-at-height-rescue (REN-01) and lone electrical
  work to the cross-listed utilities skills, and de-identifies lone-worker contact
  / shift / location to role labels. Decision-support only; competent-person review
  required.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 2
  audience:
  - M
  - C
  industry:
  - Gen
  jurisdiction:
  - UK
  status: stable
  plugin: hse-renewables
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Lone Working Assessment

The **hse-renewables lone-working skill** — given a **named role / site** and the **specific solitary activity**, it produces a defensible **lone-working risk assessment** whose primary control is **removing the solitary exposure**, backed by a **reliable scheduled check-in with a defined missed-check-in escalation path** and a **coverage-checked communication plan**. It grounds the risk-assessment duty, the reliable-communication / scheduled-check-in / escalation requirement and the violence + stress/wellbeing considerations in `KB-REG-LONE-WORKING` (HSE INDG73 rev 4), and the lone-worker device-service discipline in `KB-STD-BS8484` (BS 8484:2022) — a **device supplements, never replaces, the check-in / escalation procedure**.

**It leads with eliminating the solitary exposure first, then a missed-check-in escalation path — not by issuing a device.** The primary control of every lone-working assessment this skill builds is to **avoid lone working for the task where reasonably practicable** (pair up, re-schedule, remote monitoring), then a **scheduled check-in at a defined interval + a defined missed-check-in escalation path** (who responds, how, in what time), with a **coverage-checked communication path** (`KB-SNIP-CHECKIN-ESCALATION`). A lone-working assessment "controlled" by handing out a panic-button app, with no scheduled check-in or escalation procedure, is the indefensible paperwork this skill rejects. **"No mobile signal in that area" is a control failure, not an accepted residual risk** — fix the comms or change the task.

**Lone work at height and lone electrical work are routed, never assessed solo here.** Lone **work at height** on a turbine is not acceptable: it routes to **`wind-turbine-work-at-height-rescue`** (REN-01)'s two-person / **tested-rescue** baseline (`KB-SNIP-RESCUE-PLAN`, shared with REN-01) — a climb is a two-person-minimum team with ground support able to initiate a timed, team-owned rescue, and "call 999" is never the rescue plan. Lone **electrical** work routes to the cross-listed utilities skills (`arc-flash-assessment` / `live-working-risk-assessment`) — named here as a routing pointer, never rebuilt (CONV-12; the cross-list wiring is deferred to Phase 17).

## When to use this skill

Use this skill when the user needs a **lone-working risk assessment** for a **named role / site** and a **specific solitary activity**. Trigger phrases: "assess our lone working / solo working", "build a lone-working risk assessment", "set up scheduled check-ins and an escalation procedure for a lone worker", "what comms / coverage does our field engineer need working alone", "evaluate a lone-worker device / panic-button app", "is it safe for one person to do this task alone". If the request is vague ("sort out our lone working"), the Workflow intake forces the named role/site and the specific solitary activity before any drafting. This skill assesses the lone-working procedure; lone **work at height** is **`wind-turbine-work-at-height-rescue`** (REN-01) and lone **electrical** work is the cross-listed utilities skills (`arc-flash-assessment` / `live-working-risk-assessment`) — routed here, never rebuilt.

<!-- hse:block:deid:start -->
## Data Protection & De-identification (MANDATORY — apply before drafting)

Apply this BEFORE you draft anything. Treat injury, illness, and any health
detail as the highest sensitivity. Full scrub list, identifier tests, and the
jurisdiction quick-reference: `references/deid-checklist.md`.

1. **DETECT & FLAG** every personal/health identifier in the inputs — names,
   employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise
   locations, job title / crew / shift, photos, and any medical detail.
   **List what you found before drafting.** If unsure whether something is
   identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** for any output that will circulate: replace
   identifiers with stable role labels ("Worker A", "Operator 1"). Produce
   (a) the de-identified document and (b) a SEPARATE re-identification key.
   **Never put the key or any name↔label mapping in the document.** Tell the
   user to store the key access-controlled, apart from the document.
3. **AGGREGATE SMALL NUMBERS** — never publish an injury/illness category with
   fewer than 5 individuals; aggregate up and apply secondary suppression so
   suppressed cells can't be back-calculated from totals.
4. **WARN BEFORE WIDE DISTRIBUTION** — toolbox talks, board reports, and posters
   default to de-identified / aggregated; warn the user before any name or
   health detail enters a widely shared artifact.
5. **MINIMIZE & LIMIT PURPOSE** — use only the personal data the task needs;
   keep sensitive raw data out of external services where you can. When in
   doubt, ask before including it.
<!-- hse:block:deid:end -->

<!-- hse:block:kb-selection:start -->
## Knowledge base (read ONE matching file — never load all)

Resolve the user's jurisdiction first. Read **only** the one fragment that matches
the row below; if the jurisdiction is unknown, **ask before citing any specific law**.
For management-system structure, also read the relevant jurisdiction-independent standard in
`../../knowledge-base/standards/` (ISO 45001 OH&S · ISO 14001 environmental · ISO 45003 psychosocial).
Always apply `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (KB-SNIP-HOC)
to every control recommendation. For any benchmark/figure, look up the ID in the relevant
`_registry.yaml`, then read ONLY the named file — and quote its `source`+`year`.
<!-- hse:block:kb-selection:end -->

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/renewables-clause-map.md` (`KB-SNIP-RENEWABLES-CLAUSE-MAP`) — it routes the renewables standard → artifact → owning skill (this skill owns the lone-working RA + check-in/escalation + device-service limb; **REN-01 `wind-turbine-work-at-height-rescue` owns the WAH plan + mandatory tested rescue this skill routes to, never rebuilt here**; REN-03 owns the weather thresholds). Always apply the lone-working control spine `../../knowledge-base/prompt-snippets/checkin-escalation.md` (`KB-SNIP-CHECKIN-ESCALATION`) — eliminate the solitary exposure first, then scheduled check-ins + a missed-check-in escalation path, with the device residual-only — the shared rescue spine `../../knowledge-base/prompt-snippets/rescue-plan.md` (`KB-SNIP-RESCUE-PLAN`, shared REN-01 + REN-02) wherever a rescue is foreseeable, and `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (`KB-SNIP-HOC`) to every control. Cross-reference the renewables hazard library `../../knowledge-base/hazard-library/renewables.md` for the lone-working / WAH / electrical hazard categories (single home; cross-referenced, never restated). Then resolve the jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| UK (the lone-working risk-assessment duty + reliable comms + scheduled check-ins + escalation) | ../../knowledge-base/regulatory/lone-working.md (`KB-REG-LONE-WORKING` — HSE INDG73 rev 4: explicit risk-assessment duty, reliable coverage-checked communication, scheduled check-ins + a missed-check-in escalation procedure, violence + stress/wellbeing) |
| All (lone-worker device-service conformance — device supplements, never replaces) | ../../knowledge-base/standards/bs8484.md (`KB-STD-BS8484` — BS 8484:2022: the conformant device, the monitored alarm-receiving/response chain, and the discipline that a device supplements — never replaces — the check-in / escalation procedure) |
| India (lone working) | ../../knowledge-base/regulatory/in-renewables.md (`KB-REG-IN-RENEWABLES` — deferral pointer; **state detection is mandatory** (CONV-8); defer statutory content to the `hse-india` engine; **no national form number invented**) |
| Unknown | Ask the jurisdiction / regulatory regime before citing any specific regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the **named role / site** (the specificity
anchor: a generic "our lone workers" is refused, because the assessment is
role-and-task-specific), the **specific solitary activity** (and whether it includes
**work at height** or **electrical work** — the routing trigger), the **comms
coverage** at the work location (the "no mobile signal is a control failure" check),
the **check-in interval + missed-check-in escalation path** (who responds, how, in
what time), the **proposed controls** (the core-value gate — refuse a device-led
treatment), the **violence + stress/wellbeing** considerations, and the jurisdiction
branch (UK → `KB-REG-LONE-WORKING` + `KB-STD-BS8484`; India → `KB-REG-IN-RENEWABLES` +
mandatory state detection) — lives in **`references/intake.md`** (the
`intake-coverage` manifest + echo-back + refuse-on-vague anchors). Run it one question
at a time, branch on the answers, and **echo the confirmed role + site + solitary
activity back before any drafting**.

**The de-identification step runs FIRST** (above): the lone worker's personal contact
/ shift / location data is scrubbed to role labels for the distributed copy before any
analysis (`references/deid-checklist.md`).

Then walk the **lone-working method** (`references/METHODOLOGY.md`): role / site / activity
scoping → the routing gate (lone **work at height** → REN-01's two-person / tested-rescue
baseline; lone **electrical** → the cross-listed utilities skills — never assessed solo
here) → **eliminate the solitary exposure as the lead control** (pair up / re-schedule /
remote monitoring via `controls.py` + `KB-SNIP-CHECKIN-ESCALATION`, **never a device as the
headline**) → **coverage-checked communication** ("no mobile signal" is a control failure,
not an accepted risk) → **scheduled check-ins + a defined missed-check-in escalation path**
(responder, method, response time — an undefined responder/time is a `[GAP]`) → the
**BS 8484 device as a residual supplement only** → violence + stress/wellbeing controls →
residual risk (`risk_matrix` 5×5) — recording `[GAP]` for any unsupplied basis (comms
coverage, response time, device/service) and closing each `[GAP]` with a SMART action
(`smart_actions`) carrying a named role owner and a due date. **Lone-worker personal
contact / shift / location is role-labelled, never named, in the circulated copy.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the eliminate-first control order + the routing gate + the check-in/escalation discipline) is in `references/METHODOLOGY.md`.

<!-- hse:block:orchestration:start -->
## Agentic Execution (Orchestration Block)
You are the ORCHESTRATOR for this skill. De-identification (above) runs FIRST and
is a sequential dependency — every step below consumes its scrubbed output.
Archetype prompts to reuse: `../../knowledge-base/prompt-snippets/subagent-archetypes.md` (KB-SNIP-ARCHETYPES).

### Step 0 — Triage: fan out at all?
Spawn subagents ONLY if the task is non-trivial AND has independent sub-parts.
Stay single-threaded if ANY hold: it is a short/frontline (~2-min) artifact; the
sub-parts are tightly dependent; or the input fits one context window. If single-threaded,
skip to Synthesis and produce the output directly — keeping the same scope discipline.

### Step 1 — Plan
Decompose into INDEPENDENT jobs. Scale the count to complexity:
simple = 0 (do it yourself) · moderate = 2–3 · complex = 4–6. Never exceed MAX=6.

### Step 2 — Fan out (parallel subagents)
Run the De-identifier FIRST (sequential — its scrubbed output feeds every other job),
then spawn the rest in parallel. Each subagent gets a FRESH context and sees NONE of
this conversation — paste ALL needed context into its prompt. Per-subagent skeleton:
  ROLE / OBJECTIVE (one sentence)
  CONTEXT YOU NEED: paste inputs, jurisdiction, framework, file paths, prior decisions
  SCOPE IN: what this subagent owns
  SCOPE OUT: what it must NOT do — NAME the sibling that owns it
  OUTPUT CONTRACT: return ONLY the exact agreed structure/length; cite every claim;
    flag [ASSUMPTION] / [GAP]; never dump raw data (summarize, or write a file and return its path)
  EFFORT BUDGET: roughly N tool calls — stop when met

### Step 3 — Synthesis (you)
Gather the outputs, resolve conflicts explicitly (state which source wins), de-duplicate,
and assemble the deliverable in this skill's output format.

### Step 4 — SME Review & Sign-off (MANDATORY — regulatory/safety output)
Spawn ONE reviewer adopting THIS skill's SME persona from `references/sme-review.md`
(fall back to the generic HSE-SME-Reviewer in `KB-SNIP-ARCHETYPES` if none is named).
Give it the draft + the inputs + the output contract. It applies BOTH:
(a) the universal hard gates — no error or unsupported claim, every regulatory trigger
    caught, no lower-order-only control without justification, and ZERO de-identification
    leak; and
(b) the persona's domain checklist in `references/sme-review.md`.
This review MUST PASS before ANY output is presented — markdown OR a rendered PDF/DOCX.
Fix everything it raises and re-run until clean. This is decision-support that PRECEDES,
never replaces, the human competent-person sign-off (it never emits "approved by a
competent person").

> Single-threaded fallback: if your host has no subagent capability, perform the SME
> Review & Sign-off pass yourself in THIS context — run the de-identification scrub
> first, keep the scope discipline, apply the persona checklist + universal gates, and
> pass the review before presenting any output (markdown or rendered).
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

Moderate fan-out for a full lone-working assessment (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub the lone worker's **name / personal contact
  number / shift pattern / home or precise work location** into **role labels** for the
  distributed copy, and scrub any prior lone-working incident / assault / collapse detail
  referenced for context. Returns the re-identification key SEPARATELY to the orchestrator,
  never to a sibling.
- **Routing-&-Scope-Triage** — confirm the named role / site / solitary activity and run
  the routing gate: lone **work at height** → point to REN-01
  `wind-turbine-work-at-height-rescue` (two-person / tested-rescue baseline,
  `KB-SNIP-RESCUE-PLAN`); lone **electrical** → point to the cross-listed utilities skills
  (`arc-flash-assessment` / `live-working-risk-assessment`). SCOPE-OUT: **does not assess a
  WAH or electrical task solo here** — it routes and stops.
- **Control-Order-Author** — author the control order with **eliminate-the-solitary-exposure
  as the lead** (pair up / re-schedule / remote monitoring via `controls.py` +
  `KB-SNIP-CHECKIN-ESCALATION`), then **coverage-checked communication** (a coverage gap is a
  control failure, not an accepted risk), then **scheduled check-ins + a defined
  missed-check-in escalation path** (responder / method / response time, else a `[GAP]`), with
  the **BS 8484 device as a residual supplement only** (`KB-STD-BS8484`). SCOPE-OUT: does not
  do the routing triage (the Routing-&-Scope-Triage owns it).
- **Residual-&-Actions-Author** — score residual risk (`risk_matrix` 5×5) after the lead
  controls, add the violence + stress/wellbeing controls, and write the owned/dated
  `[GAP]`-closure actions (`smart_actions`). SCOPE-OUT: does not set the control order.
- **Critic/QA** (MANDATORY) — the lone-working persona (`references/sme-review.md` /
  `KB-SNIP-ARCHETYPES`): the control leads with eliminating the solitary exposure (never a
  device as the headline); a coverage gap is treated as a control failure; a scheduled
  check-in + a defined missed-check-in escalation path is present (responder / time, never a
  `[GAP]` left open silently); lone WAH is routed to REN-01 (no solo climb) and lone
  electrical to the utilities skills; no PPE/admin-only control unjustified; and ZERO
  lone-worker contact / shift / location leak into the circulated copy. Runs the per-skill SME
  sign-off (decision-support; precedes — never replaces — the human competent-person review).

Simple single-activity assessments run single-threaded — no subagents.

<!-- hse:block:report-output:start -->## Output format

Assemble a `report.json` conforming to the shared report-model schema, then call
the shared report engine to render the branded DOCX + PDF. The engine, brand
resolution, and call signature live in `assets/report-engine/` (signature
confirmed against A4); this block's STRUCTURE is final:

1. Build `report.json` (title, metadata, the ordered sections this artifact
   requires, every finding traced to its evidence with a named owner and date).
2. Resolve branding: the user's `brand.yaml` overrides the Eyekyam default.
3. Render both DOCX and PDF from the one `report.json` via the shared engine.
4. Surface the output paths and a one-line provenance note to the user.
<!-- hse:block:report-output:end -->

<!-- hse:block:attribution:start -->
## Attribution (non-intrusive)

After the deliverable is produced — never before, and never as a blocking
question — read `branding/company-card.yaml` and surface the company card per
its `placement`:

- `footer` (default): one quiet line at the end, e.g.
  *"Built by Eyekyam · HSE Leadership, operationalised · eyekyam.com"*.
- `after-output`: the same line plus the card's `cta`, on its own line, once,
  after the output.
- `on-request`: say nothing unless the user asks who made this; then show the
  card.

If `show: false`, omit attribution entirely — no line, no footer. Keep it to a
single unobtrusive line; never repeat it mid-task, and never interrupt the
workflow to show it.
<!-- hse:block:attribution:end -->

## Reference material

On-demand pointers (read only when needed):

- `references/METHODOLOGY.md` — the domain method this skill applies.
- `references/intake.md` — the structured-intake coverage contract + Q-table.
- `references/sme-review.md` — the per-skill SME sign-off personas + checklist.
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
