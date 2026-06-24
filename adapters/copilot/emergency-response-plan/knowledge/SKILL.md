---
name: emergency-response-plan
description: Produces a scenario-keyed emergency response plan (ERP) for a named site
  or facility — call-out tree, muster and evacuation arrangements, scenario response
  procedures, drill schedule, and external-responder integration. Use this skill whenever
  a user asks to write or review an emergency plan, evacuation plan, emergency procedures,
  crisis-response plan, or to plan emergency drills for a specific location. It grounds
  the plan in the site's credible emergency scenarios and the hierarchy of controls
  (prevention before response), assigns named roles with deputies, and schedules drills
  — emitted as a branded report. For continuity of critical activities after the emergency
  is controlled (RTO/RPO/MTPD) use business-continuity-plan; for mine-rescue-specific
  arrangements use mine-rescue-erp; for offshore use the marine-emergency-response
  skill. Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: emergency
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-operations
  bundled_in:
  - hse-marine-offshore
  - hse-utilities-power
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Emergency Response Plan

A consultant-grade HSE skill that produces a **scenario-keyed emergency response plan
(ERP)** for a **named site or facility** grounded in **ISO 45001 clause 8.2 (emergency
preparedness and response)**. It forces the single lever that separates a defensible
artifact from copy-paste paperwork: the plan is built from the site's **credible
emergency scenarios** and the **hierarchy of controls — prevention before response**
(eliminate/reduce the scenario at source first, then plan the response), never a generic
"evacuate" procedure. Every response role has a **named deputy**; muster points are
**named**; the **drill schedule is dated** (cadence from `KB-DATA-DRILL-FREQ`); external
responders are **integrated** with a site-interface sheet.

The ERP and `business-continuity-plan` are **adjacent but distinct** (D-07): this skill
plans the **immediate emergency response** (scenarios, muster, evacuation, call-out
tree); for **continuity of critical activities after the emergency is controlled**
(RTO / RPO / MTPD, recovery strategies) use **`business-continuity-plan`** — the ERP
output carries a one-line pointer to it. This generic ERP does **not** subsume
**`mine-rescue-erp`** (the distinct mining-rescue artifact) or the marine /
offshore-emergency skill — route those requests to their own skills.

## When to use this skill

Use this skill when the user needs an emergency response plan for a **concrete named
site or facility** — for example "write an ERP for the Plant 4 solvent-storage
warehouse", "review our evacuation plan for the head-office building", "build emergency
procedures for a chemical-release scenario at the bulk-tank farm", or "plan the fire and
medical drills for the distribution centre". Trigger phrases: *emergency response plan,
ERP, emergency plan, evacuation plan, emergency procedures, crisis-response plan,
call-out tree, muster point, emergency drill, emergency preparedness*.

**Route elsewhere:** for **continuity of critical activities** after the incident is
controlled (RTO/RPO/MTPD, recovery roles) use **`business-continuity-plan`**; for a
**mine-rescue** plan use **`mine-rescue-erp`**; for an **offshore/marine** emergency
plan use the marine-emergency-response skill. The intake's Q1 disambiguates ERP
(scenarios / muster / evacuation / immediate response) from BCP (critical activities /
RTO / RPO / MTPD). If the request is vague ("write me an emergency plan"), the Workflow
intake below **refuses to proceed** until the named site + at least one credible
scenario + muster/evacuation arrangements are captured.

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

| Jurisdiction / scope | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (s.41B on-site emergency plan for MAH installations; + in-state-forms.md for the user's state — defers to `hse-india`) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (Regulatory Reform (Fire Safety) Order 2005 art. 15; DSEAR 2002 where flammable atmospheres) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (29 CFR 1910.38 Emergency Action Plans; 1910.157/1910.165 alarms & extinguishers) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Scenario catalogue & procedure skeletons (always) | ../../knowledge-base/prompt-snippets/erp-scenarios.md (KB-SNIP-ERP-SCENARIOS) |
| Drill frequencies by scenario / site-class (always) | ../../knowledge-base/data-points/drill-freq.md (KB-DATA-DRILL-FREQ — quote source+year; [GAP] where unresolved) |
| Operations clause cross-walk (always) | ../../knowledge-base/prompt-snippets/ops-clause-map.md (KB-SNIP-OPS-CLAUSE-MAP — ISO 45001 8.2 → this skill) |

This skill always grounds in `KB-STD-ISO45001` (clause **8.2** emergency preparedness &
response) and applies `KB-SNIP-HOC` so **prevention precedes response** on every
scenario; it builds the scenario menu and per-scenario procedure skeletons from
`KB-SNIP-ERP-SCENARIOS` and sets the **dated drill cadence** from `KB-DATA-DRILL-FREQ`
(quote `source`+`year`; `[GAP]` where unresolved — never a bare number). For an India
site it resolves the state via the `hse-india` engine (mandatory state detection — never
a national form number). The bundle clause cross-walk is `KB-SNIP-OPS-CLAUSE-MAP`. The
rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table,
the **ERP-vs-BCP disambiguation at Q1**, the per-scenario branch (Q2), and the
refuse-on-vague anchors — lives in **`references/intake.md`**. Run it one question at a
time, branch on the answers, **echo the captured facts back before any analysis**, and
**refuse to proceed on a vague request** (record `[ASSUMPTION]` / `[GAP]`, never invent).
The six questions:

1. **Q1 — Site & occupancy + ERP/BCP disambiguation** *(the specificity anchor; refuse
   generic).* The named site/facility + headcount/shift pattern. **This skill plans the
   immediate emergency response (scenarios, muster, evacuation, call-out tree).** If the
   user actually wants **continuity of critical activities after the emergency is
   controlled** (RTO / RPO / MTPD, recovery strategies), route them to
   **`business-continuity-plan`** — do not produce a generic plan here.
2. **Q2 — Credible scenarios** *(multi-select, branch per scenario):* fire/explosion ·
   chemical/gas release · medical · structural/collapse · severe weather/flood ·
   security/violence · loss of utilities. Each selected scenario activates a
   scenario-specific procedure stub from `KB-SNIP-ERP-SCENARIOS`.
3. **Q3 — On-site response capability** *(MCQ):* first-aiders only / trained ERT / fire
   team / none — capability must be **proven before the plan relies on it**.
4. **Q4 — External responders & site interface** *(free-text):* fire/ambulance access,
   isolation points, assembly/muster points.
5. **Q5 — Jurisdiction** (for the legal ERP baseline; India → mandatory state detection
   via `hse-india`, never a national form number).
6. **Q6 — Drill history** *(free-text, optional)* — seeds the dated drill schedule
   against `KB-DATA-DRILL-FREQ`.

**Refuse-on-vague anchor:** no plan until the **named site** + **≥1 credible scenario** +
**muster/evacuation arrangements** are captured. A generic "evacuate" plan with no
scenario-keyed steps is explicitly refused.

Then: apply the ERP method (`references/METHODOLOGY.md`) — **scenario selection →
prevention-first (hierarchy) → response procedure → roles + deputies → drill cadence →
responder integration** → validate the draft against `references/QUALITY_CHECKLIST.md` →
produce the output via the Output format section below.

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

This is a **moderate roster** (A6 "moderate = 2–4"): the De-identifier is the
**sequential first gate** (the call-out tree holds real names + phone numbers — a
legitimate internal operational record, but role + duty-phone labels in any widely
distributed copy). The fan-out is **per-scenario** for a multi-scenario facility; a
small single-scenario site runs single-threaded. The **prevention-first hierarchy** is
applied via the A7 `controls` engine + `KB-SNIP-HOC` (prevention/elimination before the
plan relies on response), and the **dated drill schedule** is built with `smart_actions`
against `KB-DATA-DRILL-FREQ` — these are deterministic script calls, not fan-out jobs.
Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub responder
  names / personal mobile numbers / health detail in the call-out tree to **role +
  duty-phone labels** for any circulated copy (the internal master may hold the real
  contacts as a legitimate operational record). Every job below consumes the scrubbed text.
- **Scenario-Analyst** — for each credible scenario from Q2, build the per-scenario
  response procedure from `KB-SNIP-ERP-SCENARIOS` — **prevention controls first** (apply
  `controls` + `KB-SNIP-HOC`), then detection/alarm → immediate actions → escalation. Each
  procedure is **scenario-keyed**, never a generic "evacuate". SCOPE-OUT: roles/muster
  (Roles-&-Logistics), drill cadence (Drill-Planner).
- **Roles-&-Logistics** — build the **call-out tree & roles with named deputies**, the
  **named muster/assembly points** and evacuation routes, and the **external-responder
  integration sheet** (access, isolation points, site interface). SCOPE-OUT: per-scenario
  procedures (Scenario-Analyst).
- **Drill-Planner** *(optional)* — set the **dated drill schedule** by scenario/site-class
  from `KB-DATA-DRILL-FREQ` (quote source+year; `[GAP]` where unresolved) as `smart_actions`
  with named owners + dates. Merge into Roles-&-Logistics for a small site.
- **SME Reviewer** (MANDATORY pre-output gate) — runs the **Emergency Planning Officer**
  sign-off in `references/sme-review.md` before any output: prevention precedes response,
  every role has a deputy, muster points named, drills dated, the response capability is
  proven (not assumed), and the ERP→BCP boundary is honoured.
- **Critic/QA** (MANDATORY) — adversarial final pass: prevention-before-response (no
  response-only plan), scenario-keyed procedures (no generic evacuate), every role
  deputised, muster named, drills dated, citations trace to the KB (8.2 / 1910.38), and
  ZERO de-id leak (no personal mobile number in a circulated copy). PASS/FAIL.

Simple single-scenario sites run single-threaded — no subagents — but the De-identifier
scrub, the `controls`/`smart_actions` calls, and the Critic/QA + SME passes are still made.

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
