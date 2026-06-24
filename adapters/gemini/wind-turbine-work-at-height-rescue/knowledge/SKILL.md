---
name: wind-turbine-work-at-height-rescue
description: 'Produce a consultant-grade wind-turbine work-at-height + rescue plan
  for a named turbine/site and the specific WAH activity (nacelle/hub/blade/tower).
  Use this skill to plan work at height on a wind turbine, build a turbine WAH risk
  assessment, specify a mandatory tested rescue plan for a suspended worker, or set
  the two-person-minimum climb-team baseline. Control leads with the Work at Height
  Regulations 2005 reg-6 hierarchy (avoid work at height -> prevent a fall, collective
  before personal -> mitigate/arrest), and a tested rescue plan is mandatory before
  work begins: a suspended worker is recovered within minutes by the team''s own two-person-minimum
  capability -- ''call 999'' is NEVER the rescue plan. It cites GWO competence as
  a requirement (cite-only; licensed module/cert detail is [GAP]), names the weather
  thresholds weather-dynamic-risk-assessment (REN-03) owns, and de-identifies worker
  names + GWO certificate numbers to role labels. Decision-support only; competent-person
  review required.'
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

# Wind Turbine Work At Height Rescue

The **hse-renewables work-at-height + rescue skill** — given a **named turbine / site** and the **specific WAH activity** (nacelle / hub / blade / tower-internal), it produces a defensible **work-at-height plan + a MANDATORY tested rescue plan**. Control is led by the **Work at Height Regulations 2005 reg-6 hierarchy** (avoid work at height → prevent a fall, **collective protection before personal** → mitigate/arrest the distance and consequences), grounded in `KB-REG-WAH2005`. And the **rescue plan is mandatory before work begins** (`KB-SNIP-RESCUE-PLAN`, reg 4): a **suspended worker is recovered within minutes by the team's own competent, two-person-minimum capability** — **"call 999 / wait for emergency services" is NEVER the rescue plan**, only a supplement. GWO competence is cited as a **requirement** (`KB-STD-GWO-WAH-RESCUE`, cite-only — the licensed module curriculum + certificate detail is `[GAP]`).

**It leads with avoid-then-prevent, and the rescue is real and tested — not "the fire brigade will get them down".** The single failure mode this skill exists to kill is the WAH plan whose rescue arrangement is "phone 999 and wait": suspension trauma can be fatal in minutes, so the team's own tested two-person-minimum recovery is the rescue plan and emergency services are an addition to it. A WAH plan that jumps to fall-arrest/PPE where avoidance (do it at ground level, lower the component, use a man-rider/platform) or collective prevention (guardrails, a working platform) is reasonably practicable is the indefensible paperwork this skill rejects (reg 6/7).

**The weather thresholds it names are owned by REN-03; lone work at height routes back here.** This skill **names** the weather hold/stop thresholds (hub-height wind cut-off ≈ 15 m/s `[ASSUMED A4]`, lightning stand-down) but defers their ownership to **`weather-dynamic-risk-assessment`** (REN-03), which owns `KB-DATA-WEATHER-THRESHOLDS` — cite, never compute or embed as a hard standard (CONV-12). The ≈15 m/s anchor is **proposed-and-user-confirmed**, never invented. **`lone-working-assessment`** (REN-02) routes any lone work at height back to this skill's two-person / tested-rescue baseline — never a solo climb (the shared `KB-SNIP-RESCUE-PLAN`).

## When to use this skill

Use this skill when the user needs a **wind-turbine work-at-height + rescue plan** for a **named turbine / site** and a **specific WAH activity**. Trigger phrases: "plan work at height on turbine WTG-12 / our wind farm", "build a turbine WAH risk assessment for nacelle / hub / blade work", "what's the rescue plan for a worker suspended in a harness on the tower", "set the climb-team / two-person baseline and GWO competence", "is our 'call 999' rescue arrangement acceptable" (it is not — the Workflow forces a tested team-owned rescue). If the request is vague ("sort out working at height on the turbines"), the Workflow intake forces the named turbine/site and the specific WAH activity before any drafting. This skill owns the WAH plan + mandatory tested rescue; the **weather thresholds** it names are **`weather-dynamic-risk-assessment`** (REN-03) and **lone working** is **`lone-working-assessment`** (REN-02) — cross-referenced, never rebuilt (CONV-12).

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

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/renewables-clause-map.md` (`KB-SNIP-RENEWABLES-CLAUSE-MAP`) — it routes the renewables standard → artifact → owning skill (**this skill owns the WAH plan + mandatory tested rescue + climb-team competence**; REN-02 `lone-working-assessment` owns the lone-working RA and routes lone WAH back here; **REN-03 `weather-dynamic-risk-assessment` owns the weather thresholds this skill only names**). Always apply the shared rescue spine `../../knowledge-base/prompt-snippets/rescue-plan.md` (`KB-SNIP-RESCUE-PLAN`, owned here, shared with REN-02) — a tested team-owned recovery-in-minutes rescue is mandatory and "call 999" is never the rescue plan — and `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (`KB-SNIP-HOC`) to every control, with the WAH-specific reg-6 avoid→prevent(collective)→mitigate order leading. Cross-reference the renewables hazard library `../../knowledge-base/hazard-library/renewables.md` for the WAH / dropped-object / weather hazard categories (single home; cross-referenced, never restated). When the user names a weather hold/stop threshold, **name it and defer to `../../knowledge-base/data-points/weather-thresholds.md` (`KB-DATA-WEATHER-THRESHOLDS`, owned by REN-03)** — the ≈15 m/s hub-height cut-off is `[ASSUMED A4]`, proposed-and-user-confirmed, never embedded as a citation. Then resolve the jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| UK (the work-at-height planning + avoid→prevent→mitigate hierarchy + collective-before-personal + inspection duty, incl. mandatory rescue planning) | ../../knowledge-base/regulatory/wah2005.md (`KB-REG-WAH2005` — Work at Height Regs 2005 SI 2005/735: reg 4 plan incl. emergencies & rescue, reg 6 avoid→prevent→mitigate, reg 7 collective-before-personal, reg 12 inspection) |
| All (wind climb-team competence + the timed team-owned rescue discipline) | ../../knowledge-base/standards/gwo-wah-rescue.md (`KB-STD-GWO-WAH-RESCUE` — GWO WAH / First Aid / ART: current GWO competence requirement, 2-yr refresh, two-person-minimum climb team, suspended-worker recovery in minutes, "emergency services alone is NOT a rescue plan"; **cite the competence requirement only — module curriculum / certificate detail is licensed → `[GAP]`**) |
| India (work at height) | ../../knowledge-base/regulatory/in-renewables.md (`KB-REG-IN-RENEWABLES` — deferral pointer; **state detection is mandatory** (CONV-8); defer statutory content to the `hse-india` engine; **no national form number invented**) |
| Unknown | Ask the jurisdiction / regulatory regime before citing any specific regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the **named turbine / site** (the
specificity anchor: a generic "the turbines" is refused, because the plan is
turbine-and-task-specific), the **specific WAH activity** (nacelle / hub / blade /
tower-internal — and the access method), whether **avoidance** has been tested (can
the work be done at ground level / the component lowered / a man-rider or platform
used — the reg-6 lead), the **fall-prevention then fall-arrest** arrangement
(collective before personal — reg 7), the **rescue plan** (the core-value gate: a
tested, team-owned recovery within minutes — a "call 999 / wait" answer is refused),
the **climb-team manning + GWO competence** (two-person-minimum; competence cited, not
numbered), the **weather hold/stop thresholds** (named here, owned by REN-03), and the
jurisdiction branch (UK → `KB-REG-WAH2005` + `KB-STD-GWO-WAH-RESCUE`; India →
`KB-REG-IN-RENEWABLES` + mandatory state detection) — lives in
**`references/intake.md`** (the `intake-coverage` manifest + echo-back +
refuse-on-vague anchors). Run it one question at a time, branch on the answers, and
**echo the confirmed turbine + site + WAH activity back before any drafting**.

**The de-identification step runs FIRST** (above): the climbers' **names + GWO
certificate numbers** are scrubbed to **role labels** for the distributed copy before
any analysis (`references/deid-checklist.md`).

Then walk the **work-at-height + rescue method** (`references/METHODOLOGY.md`): turbine /
site / activity scoping → **reg-6 control order leading with AVOID work at height**
(do it at ground level / lower the component / use a man-rider or platform via
`controls.py` + `KB-SNIP-HOC`), then **PREVENT a fall by collective protection before
personal** (guardrails / working platform before personal fall-arrest — reg 7), then
**mitigate/arrest** → the **MANDATORY tested rescue plan** (`KB-SNIP-RESCUE-PLAN`,
`KB-STD-GWO-WAH-RESCUE`): a **two-person-minimum** competent team with ground support
able to **recover a suspended worker within minutes** — **"call 999 / emergency
services alone" is REJECTED as the rescue plan**, recorded only as a supplement → the
**GWO competence requirement** (cited, not the licensed module/cert detail — `[GAP]`)
→ the **weather hold/stop thresholds named and deferred to REN-03** (the ≈15 m/s
hub-height cut-off `[ASSUMED A4]`, proposed-and-user-confirmed) → residual risk
(`risk_matrix` 5×5) — recording `[GAP]` for any unsupplied basis (anchor points, rescue
recovery time, manufacturer/site weather limits) and closing each `[GAP]` with a SMART
action (`smart_actions`) carrying a named role owner and a due date. **Climber names +
GWO certificate numbers are role-labelled / cited-only, never named, in the circulated
copy.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the reg-6 avoid-then-prevent control order + the mandatory tested-rescue gate + the GWO competence requirement) is in `references/METHODOLOGY.md`.

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

Moderate fan-out for a full turbine WAH + rescue plan (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub the climbers' / rescuers' **names + GWO
  certificate numbers + personal contact** into **role labels** ("Climber A",
  "Rescue Lead"), and scrub any prior fall / suspension / rescue incident referenced
  for context. **GWO certificate numbers are cited as a competence *requirement*, never
  reproduced as a number** in the circulated copy. Returns the re-identification key
  SEPARATELY to the orchestrator, never to a sibling.
- **WAH-Control-Order-Author** — author the control order with the **reg-6 hierarchy
  leading**: AVOID work at height first (ground-level work / lower the component /
  man-rider / platform), then PREVENT a fall with **collective protection before
  personal** (reg 7 — guardrails / working platform before personal fall-arrest), then
  mitigate/arrest, via `controls.py` + `KB-SNIP-HOC` + `KB-REG-WAH2005`. SCOPE-OUT:
  does not author the rescue plan (the Rescue-Plan-Author owns it) or the weather
  thresholds (REN-03 owns them — name and defer only).
- **Rescue-Plan-Author** — author the **MANDATORY tested rescue plan**
  (`KB-SNIP-RESCUE-PLAN`, `KB-STD-GWO-WAH-RESCUE`): a **two-person-minimum** competent
  team with ground support that **recovers a suspended worker within minutes**;
  **REJECT any "call 999 / wait for emergency services" arrangement as the rescue plan**
  (it is a supplement only); record the recovery method, equipment and time (an
  untested capability / unstated time is a `[GAP]`). SCOPE-OUT: does not set the
  fall-control order (the WAH-Control-Order-Author owns it).
- **Residual-&-Actions-Author** — score residual risk (`risk_matrix` 5×5) after the
  reg-6 controls + tested rescue, name the GWO competence requirement (cited, not
  numbered) and the named weather hold/stop thresholds (deferred to REN-03), and write
  the owned/dated `[GAP]`-closure actions (`smart_actions`). SCOPE-OUT: does not own the
  weather thresholds (REN-03) or set the control order.
- **Critic/QA** (MANDATORY) — the wind-WAH-rescue persona (`references/sme-review.md` /
  `KB-SNIP-ARCHETYPES`): the control leads with avoid-then-prevent (collective before
  personal — no fall-arrest/PPE-only where avoidance/collective prevention is
  practicable); a **tested two-person recovery-in-minutes rescue is present and "call
  999" is never the rescue plan**; GWO competence is cited as a requirement (no licensed
  module/cert text reproduced); the weather thresholds are named but deferred to REN-03
  (the ≈15 m/s anchor flagged `[ASSUMED]`, not a citation); and ZERO climber name / GWO
  certificate-number leak into the circulated copy. Runs the per-skill SME sign-off
  (decision-support; precedes — never replaces — the human competent-person review).

Simple single-activity plans run single-threaded — no subagents.

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
