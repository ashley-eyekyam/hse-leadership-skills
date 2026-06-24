---
name: driver-fatigue-management
description: Produces a consultant-grade driver-fatigue-management artifact for a
  named fleet/operation and a real driver duty log, led by schedule/roster (FRMS)
  redesign rather than 'stay alert'. Use this skill when a user asks to manage driver
  fatigue, check hours-of-service (HOS) compliance, assess a duty/driving log against
  FMCSA 49 CFR 395 or EU Regulation (EC) 561/2006, build a fatigue risk management
  system (FRMS), or review rosters. The HOS compliance flags (driving limit, on-duty
  window, break, cycle, rest) are COMPUTED by the deterministic fatigue.py engine,
  never narrated, and are authoritative; a separate fatigue index is a clearly-flagged
  advisory metric, not a regulatory threshold. Multi-day cycle and cross-shift rest
  claims absent from a single-shift log are a [GAP], never invented. It leads controls
  with roster redesign, rejects an alertness-training / in-cab-gadget treatment, and
  de-identifies driver name / CDL / medical / OSA data to role labels first. Decision-support
  only; review by a competent person.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: occ-health
  tier: 2
  audience:
  - M
  - C
  industry:
  - All
  jurisdiction:
  - US
  - EU
  - UK
  - IN
  status: stable
  plugin: hse-logistics-transport
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Driver Fatigue Management

A consultant-grade, **schedule/roster-redesign-first** driver-fatigue-management artifact for a
**named fleet / transport operation** and a **real driver duty log** — never a generic "manage
fatigue" briefing. Its entire reason to exist is that **fatigue is a scheduling and roster-design
problem before it is a "stay alert" problem**: the controls lead with **journey planning, roster
redesign, and built-in rest (a Fatigue Risk Management System — FRMS)**; an **alertness-training /
"stay alert" briefing or an in-cab fatigue-detection gadget treated as the headline control is a
FLAG pushed up the hierarchy**, never the primary treatment.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**hours-of-service compliance that is COMPUTED, not narrated, plus the full hierarchy of controls**.
The **HOS compliance flags** — FMCSA 49 CFR 395.3 (11 h driving / 14 h on-duty window / 30-min
break after 8 h / 60-70 h cycle / 34 h restart) and EU Regulation (EC) 561/2006 (9-10 h daily
driving / 45-min break after 4.5 h / 11 h daily rest / 56-90 h weekly) — are produced by the
**deterministic `fatigue.py` engine** (`scripts/hse_components/fatigue.py`, consumed via
`scripts/_shim.py`); the skill **never** asserts a PASS/FAIL from assumption. The **two output
classes are kept strictly distinct**: the **HOS compliance flags are the AUTHORITATIVE, primary
finding** (compliance-flags-primary), and the **fatigue index is a clearly-flagged ADVISORY,
secondary metric** (advisory-index-secondary) — a transparent weighted-stressor heuristic, never a
regulatory threshold. **A multi-day cycle (60/70 h, 34 h restart) or a cross-shift daily-rest claim
that is absent from the supplied single-shift log is recorded as a `[GAP]`** (collect the 7/8-day
cumulative figure or the cross-shift rest, or record the gap) — **never invented**. Grounded in
**FMCSA HOS (49 CFR 395)**, **EU 561/2006**, and **FRMS** principles. Decision-support only; a
competent person must review the output.

## When to use this skill

Use this skill when the user needs **driver-fatigue management for a concrete fleet / operation and
a real duty log** — for example "check this driver's duty log against the hours-of-service rules",
"is this roster FMCSA / EU 561 compliant?", "build a fatigue risk management system (FRMS) for our
night-trunk fleet", "review the long-haul rosters for fatigue risk", or "produce a driver-fatigue
assessment for depot R-204". It is **not** for a generic "how do I stop drivers getting tired?"
answer: the Workflow intake below forces the named operation, the jurisdiction, and the duty-log
inputs before any analysis, **refuses a vague "manage our fatigue" request**, and **refuses a
"just run a stay-alert toolbox talk" / "fit in-cab alertness alarms" treatment as the headline
control** — fatigue is led by roster redesign, and the HOS flags are computed, never narrated.

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
| Fatigue-control spine (every run) | ../../knowledge-base/prompt-snippets/fatigue-frms.md (KB-SNIP-FATIGUE-FRMS) — the **schedule-redesign-first** fatigue-control spine: redesign the roster / route / journey plan and build in rest FIRST; an "stay alert" briefing or an in-cab alertness gadget is **NOT** the primary control; HOS compliance is computed by `fatigue.py`, never narrated; a multi-day cycle / cross-shift claim without the cumulative log is a `[GAP]` |
| Logistics clause cross-walk (every run) | ../../knowledge-base/prompt-snippets/logistics-clause-map.md (KB-SNIP-LOGISTICS-CLAUSE-MAP) — the bundle-shared FMCSA HOS / EU 561 + FRMS → driver-fatigue-management cross-walk that keeps the logistics-transport skills consistent (HOS computed by `fatigue.py`; India via KB-REG-IN-MTW) |
| USA / EU / UK | ../../knowledge-base/regulatory/fmcsa-hos.md (KB-REG-FMCSA-HOS) — the **combined** US FMCSA Hours-of-Service (49 CFR Part 395) **+** EU Regulation (EC) 561/2006 drivers'-hours duty→limit-category→artifact citation map (a single fragment, never split); the numeric limits are LOCKED constants in `fatigue.py`, not pasted here — cite the part/article numbers + the ELD/tachograph record types only |
| India | ../../knowledge-base/regulatory/in-mtw.md (KB-REG-IN-MTW) — India Motor Transport Workers Act 1961 (+ Factories-Act-as-warehouse, flagged OSH Code 2020 transition); **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and leads every assessment with the
**schedule-redesign-first fatigue-control spine** `KB-SNIP-FATIGUE-FRMS` (roster / journey-plan /
built-in-rest redesign before any "stay alert" or in-cab gadget), applies `KB-SNIP-HOC` to every
control, and aligns with the other logistics skills through `KB-SNIP-LOGISTICS-CLAUSE-MAP`. The
**hours-of-service compliance flags are COMPUTED by the deterministic `fatigue.py` engine** (FMCSA
49 CFR 395.3 + EU 561/2006), never narrated — `KB-REG-FMCSA-HOS` is the cited structural reference
(the combined US+EU fragment, never split), never a substitute for the computation. The fatigue
index is rendered as a clearly-flagged **advisory** metric, never a regulatory threshold. For an
India site, resolve the state via `hse-india` (**mandatory state detection**) and emit a literal
`[GAP]` where a state return is owed — never a minted national form number. The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the driver-fatigue intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to "manage our fatigue": you need the named fleet/operation + the
jurisdiction + the driver duty log (the segment-by-segment `{status, hours}` shift record) before
any analysis. Refuse a "just run a stay-alert toolbox talk" / "fit in-cab alertness alarms"
treatment as the headline control** — fatigue is led by roster redesign.

**De-identify FIRST.** Before any analysis, run the `deid` block + `references/deid-checklist.md`:
this is the **highest de-id tier** — the driver's name, **CDL / licence number, medical-fitness /
DOT-medical certificate, obstructive-sleep-apnoea (OSA) / sleep-disorder note, and any
fatigue-event / sickness-absence count** are special-category occupational-health data. Reduce every
driver to a stable **role label** ("Driver A"), **suppress any `<5` fatigue-event / sickness-absence
small cell** (with secondary back-calc guard), and never circulate the re-identification key. The
De-identifier subagent runs FIRST; everything downstream consumes only its scrubbed output.

1. **The named fleet / operation** (free-text — the specificity anchor) — "Name the exact fleet /
   operation / route / depot (e.g. 'night-trunk fleet, route R-204, Midlands depot'). **Refuse
   'our drivers' / 'the fleet' — the assessment is operation-specific.**"
2. **Jurisdiction & rule-set** (mcq — asked early; it selects the HOS rules) — USA (FMCSA 49 CFR
   395) / EU (Reg 561/2006) / UK (GB drivers' hours — read with EU 561) / India / Other / Unknown.
   **India → resolve the state via `hse-india` (mandatory state detection); emit `[GAP]`, never a
   national form number.**
3. **The driver duty log** (free-text / structured — the computation input) — the shift as an
   ordered list of `{status, hours}` segments (`status` ∈ `driving | on_duty | off_duty | sleeper`;
   `hours` a float). **Refuse to compute on a missing or vague log → record a `[GAP]` and request
   the ELD / tachograph download; never invent driving hours, a rest segment, or a duty figure.**
4. **Multi-day cycle & cross-shift rest** (free-text — the `[GAP]` discipline) — the 7-/8-day
   cumulative on-duty figure (for the FMCSA 60/70 h cycle + 34 h restart) and the cross-shift daily
   rest. **A single-shift log cannot evidence the multi-day cycle or the cross-shift rest — if these
   figures are not supplied, record a literal `[GAP]`; NEVER assert the cycle/restart compliant from
   a single shift** (the engine defaults them to compliant only because no multi-day breach is
   *detectable*, not because compliance is *proven*).
5. **Proposed controls** (free-text — the core-value gate) — what fatigue controls are proposed.
   **A treatment whose headline is "stay alert" / a driver-alertness briefing / an in-cab
   fatigue-detection gadget is a FLAG pushed up the hierarchy** — fatigue is led by
   **roster / journey-plan / built-in-rest (FRMS) redesign** (`KB-SNIP-FATIGUE-FRMS`); alertness
   training and in-cab detection are at most administrative / engineering backstops, never the
   primary control.
6. **Output artifact wanted + its reader, action owners, review cycle** (mcq + free-text) — full
   fatigue-risk-management report (consultant) / HOS-compliance + FRMS summary (manager) / the
   roster fix-list (planner); the named owner(s) of the roster-redesign / [GAP]-closure actions and
   the competent person who reviews; the review trigger (on roster change / on ELD-exception / other).

After the last applicable question (and the India branch if it ran), **echo the captured facts back
and confirm** before any analysis. Never proceed on a vague or missing input — a missing duty-log
segment, cycle figure, or cross-shift rest is a `[GAP]`, never an invented value.

Then: run the **De-identifier scrub first** (highest tier — `references/deid-checklist.md`); compute
the **HOS compliance flags + the advisory fatigue index** via the **`fatigue.py` engine**
(`fmcsa_compliance` / `eu561_compliance` / `fatigue_index` → `to_report_blocks`, consumed through
`scripts/_shim.py` — never narrated; the flags are the authoritative finding, the index is flagged
advisory); record `[GAP]` for any unsupplied multi-day cycle / cross-shift rest; run the `controls`
hierarchy gate so **roster/journey-plan/built-in-rest (FRMS) redesign leads and a "stay alert" /
in-cab-gadget headline is a FLAG pushed up the hierarchy** (`KB-SNIP-FATIGUE-FRMS` + `KB-SNIP-HOC`) →
frame the residual via `risk_matrix` → make every action a SMART action via `smart_actions` (named
owner + ISO due date + measure, including [GAP]-closure) → validate the draft against
`references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The
domain method is in `references/METHODOLOGY.md`.

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

For a multi-driver / multi-route fatigue review the triage gate fans out to (the **De-identifier
runs FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. This is the **highest de-id tier**: scrub every personal /
  occupational-health identifier — **driver name, CDL / licence number, DOT-medical / fitness
  certificate, OSA / sleep-disorder note, and any `<5` fatigue-event / sickness-absence cell** — to
  role labels ("Driver A") before any analysis; **suppress `<5` small cells** with the secondary
  back-calc guard; return the re-identification key SEPARATELY to the orchestrator, never to a
  sibling.
- **HOS-&-Roster-Analyst** — per driver / route, capture the duty log and run the **`fatigue.py`
  engine** (`fmcsa_compliance` / `eu561_compliance` / `fatigue_index` → `to_report_blocks`, via
  `scripts/_shim.py`) to COMPUTE the HOS compliance flags (the authoritative finding) and the
  advisory fatigue index (rendered clearly-flagged advisory, never a threshold). **A multi-day cycle
  / cross-shift rest figure not in the supplied log is a `[GAP]`** (request the 7/8-day cumulative
  total or the ELD download) — never asserted compliant from a single shift, never an invented duty
  figure. SCOPE-OUT: does not select the controls or de-identify (the Controls-Author / the
  De-identifier).
- **Controls-&-FRMS-Author** — rank the controls up the hierarchy (**roster / journey-plan /
  built-in-rest redesign first** → engineered backstops → administrative "stay alert" / in-cab
  detection LAST) via the **`controls` engine** — a fatigue treatment that **leads with a
  driver-alertness briefing or an in-cab fatigue-detection gadget** (`ppe_admin_only=True`, the
  alertness-led FLAG) is **pushed up the hierarchy, never the headline control**
  (`KB-SNIP-FATIGUE-FRMS`); re-frame the residual via `risk_matrix`; make every action a SMART
  action (named owner + ISO due date + measure, incl. [GAP]-closure). SCOPE-OUT: does not compute the
  HOS flags or check the law (the HOS-Analyst / the SME persona).
- **Critic/QA** (MANDATORY) — adversarial final pass: the HOS flags are COMPUTED (never narrated)
  and traced to the duty log, the compliance flags are the authoritative finding and the fatigue
  index is clearly flagged advisory, every absent multi-day-cycle / cross-shift-rest figure is a
  `[GAP]` (never asserted compliant), roster / FRMS redesign leads and a "stay alert" / in-cab-gadget
  headline is flagged up the hierarchy, every action has a named owner + ISO date, and ZERO
  de-identification leak (no name / CDL / OSA detail, no `<5` fatigue-event cell, no re-id key).
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first** (highest tier), then the
`fatigue.py` HOS + index computation, the `controls` / `risk_matrix` / `smart_actions` calls inline
(roster/FRMS-led, alertness-led FLAGGED), then the mandatory Critic/QA + SME pass — same scope
discipline, no subagents.

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
