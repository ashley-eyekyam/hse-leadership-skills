---
name: bbs-program-designer
description: Designs a non-punitive behaviour-based-safety (BBS) program for a named
  site, crew, or operation — ABC (antecedent-behaviour-consequence) analysis, an observable
  observation-card design, defined metrics (percent-safe, participation, trend-by-category),
  and at-risk behaviours trended to systemic causes and routed to hierarchy-ranked
  system fixes. Use this skill whenever a user asks to design, set up, or improve
  a behaviour-based safety / BBS / behavioural-safety / safe-behaviour-observation
  program, an observation card, peer-observation or safety-conversation scheme, or
  to define BBS metrics and feedback loops. Observation cards are non-punitive by
  design — role-labelled or anonymous, voluntary, used for trending and learning,
  never individual discipline; observable site-specific behaviours only (never 'work
  safely'); at-risk behaviours route to system fixes via the controls engine (hierarchy
  of controls), never to 'retrain the worker'. Decision-support only; a competent
  person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: culture
  tier: 2
  audience:
  - M
  - C
  - E
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-leadership
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# BBS Program Designer

A consultant-grade HSE skill that designs a **non-punitive behaviour-based-safety
(BBS) program** for a named site, crew, or operation. It forces the single lever
that separates a defensible program from generic safety paperwork: **observable,
site-specific behaviours** (never "work safely") and the **full hierarchy of
controls** — at-risk behaviours are trended to **systemic** causes and routed to
hierarchy-ranked **system fixes** via the deterministic A7 `controls` engine, never
to "retrain the worker" or discipline. The program is grounded in **ABC
(antecedent–behaviour–consequence) analysis** (`KB-SNIP-BBS-METHOD`), uses
**defined metrics** (percent-safe, participation, trend-by-category from
`KB-DATA-BBS-METRICS`, with its mandatory `<5` small-cell guardrail), and is
**non-punitive by design**: observation cards are **role-labelled or anonymous**,
**voluntary**, and used for **trending and learning, never individual sanction**. A
card that records a nameable individual for discipline is a `de_identification`
**hard-fail**. It maps to **ISO 45001 clause 5.4** (worker participation) via the
shared `KB-SNIP-LEADERSHIP-CLAUSE-MAP`. Decision-support only; a competent person
must review the output.

## When to use this skill

Use this skill when the user needs to **design, set up, or improve a behaviour-based
safety (BBS) / behavioural-safety program** for a concrete site, crew, or operation —
for example "design a BBS observation program for the warehouse picking crew at the
Leeds DC", "set up a peer-observation / safe-behaviour-observation scheme and its
metrics", or "our BBS cards have stalled — redesign the card and the feedback loop so
at-risk behaviours actually drive fixes". Trigger phrases: *behaviour-based safety,
BBS, behavioural safety, safe-behaviour observation, observation card, peer
observation, safety-conversation programme, ABC analysis, percent-safe / participation
metrics*. This skill **designs the program** (the card, the ABC routing rule, the
metrics, the feedback loop) — it does not run a full **safety-culture maturity
assessment** (see `safety-culture-assessment`), facilitate **leadership safety
walks / gemba** (see `safety-walk-gemba`), or build the **leading/lagging KPI
framework** (see `leading-lagging-kpi-framework`); intake Q1 disambiguates against
those siblings. If the request is vague, the Workflow intake below forces the
specific site/crew and **observable** behaviours before any drafting — it refuses a
non-observable card item such as "work safely".

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

This skill is **method-led**, not law-led: BBS is a participation method (ISO 45001
clause 5.4), so it **always** grounds in the BBS method + metrics + the bundle clause
map, then resolves the jurisdiction only for the worker-consultation legal duty.

| Read on every run | File |
|---|---|
| ABC analysis + non-punitive observation-card design + observer-feedback loop (the method) | ../../knowledge-base/prompt-snippets/bbs-method.md (KB-SNIP-BBS-METHOD) |
| Defined BBS metrics — percent-safe / participation / trend-by-category — with the mandatory `<5` small-cell suppression guardrail | ../../knowledge-base/data-points/bbs-metrics.md (KB-DATA-BBS-METRICS) |
| The bundle-shared ISO 45001 leadership clause cross-walk (5.4 worker participation → this skill) | ../../knowledge-base/prompt-snippets/leadership-clause-map.md (KB-SNIP-LEADERSHIP-CLAUSE-MAP) |
| Applied to every at-risk-behaviour treatment — system fixes ranked above admin/PPE, never "retrain the worker" | ../../knowledge-base/prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |

| Jurisdiction (worker-consultation duty) | Read |
|---|---|
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (HSWA 1974 + the Safety Representatives / Consultation Regs — worker participation) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (employee involvement under the OSH Act / VPP) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (OSH Framework Directive 89/391/EEC — worker consultation) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (safety-committee worker participation; **mandatory state detection** for any form, defers to `hse-india`, never a national form number) |
| Unknown | Ask before citing any specific law — the BBS method (ABC, non-punitive cards, system-fix routing) still applies |

Always apply `KB-SNIP-HOC` to every at-risk-behaviour treatment: **system fixes
(eliminate / substitute / engineer / administrate) rank ABOVE "retrain the worker"**,
and a discipline-only response is rejected. For any metric, resolve the ID in
`KB-DATA-BBS-METRICS` and honour its `<5` small-cell suppression — a percent-safe for a
4-person crew is suppressed. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question
table, the **mandatory India→state branch**, the echo-back, and the refuse-on-vague
anchors — lives in **`references/intake.md`**. Run it one question at a time, branch
on the answers, **echo the captured facts back before any analysis**, and **refuse to
proceed on a vague request**. The two hard refuse anchors:

1. **Q1 (program scope + sibling disambiguation)** — a named **site / crew /
   operation** to design the BBS program for. **Refuse "improve our safety culture"
   in the abstract**; if the user actually wants a culture-maturity assessment, a
   leadership gemba walk, or a KPI framework, route to the sibling
   (`safety-culture-assessment` / `safety-walk-gemba` /
   `leading-lagging-kpi-framework`) instead of building a BBS card.
2. **Q3 (observation-card behaviours)** — the card items must be **observable and
   site-specific** (tied to a named task/area). **Refuse a vague, non-observable item
   such as "work safely" / "be careful"** — record `[GAP]` and elicit the observable
   behaviour; never publish a card item that cannot be observed and counted.

### The BBS-program design method (ABC + non-punitive cards + system-fix routing)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST** — any prior observation cards, incident notes, or
   participation logs are scrubbed to **role/group labels** before any analysis (the
   `deid` block above + `references/deid-checklist.md` + the De-identifier-runs-first
   orchestration rule). **No nameable individual is ever recorded on a card for
   discipline** — observation data is role-labelled or anonymous. Everything
   downstream consumes only the scrubbed text.
2. **ABC analysis** (`KB-SNIP-BBS-METHOD`) — for each target behaviour, map the
   **antecedent** (the real trigger, not a slogan), the **observable behaviour**, and
   the **consequence**, and **design the system so the safe behaviour carries the
   soon / certain / positive consequence**.
3. **Design the observation card (non-punitive, observable)** — each item is
   **observable and site-specific**, tied to a named task/area; the card is
   **role-labelled or anonymous, voluntary**, and its data is used for **trending and
   learning, never individual sanction**. A non-observable item ("work safely") is
   refused at this step.
4. **Define the metrics** (`KB-DATA-BBS-METRICS`) — percent-safe = (safe ÷ total) ×
   100; participation = (active ÷ trained pool) × 100; **trend by behaviour category,
   never by person**. Apply the **`<5` small-cell suppression** to any team breakdown
   (a 4-person crew's percent-safe is suppressed; secondary suppression applied).
5. **Route at-risk behaviours to SYSTEM fixes (the hierarchy lever)** — an at-risk
   behaviour is a signal of a **system gap**. Apply `KB-SNIP-HOC` and call
   `controls.rank_controls` + `controls.validate_treatment` to route it to a
   **hierarchy-ranked system fix** (eliminate / substitute / engineer / administrate
   before PPE). **Never "retrain the worker", "be more careful", or discipline** — a
   treatment whose only response to a trended at-risk category is retraining or
   sanction is a **defect the Critic/QA and SME passes must catch** (the hard
   enforcement of the core value).
6. **Trend at-risk categories to systemic causes** — aggregate cards by behaviour
   category, identify the recurring **systemic** driver, and feed it to owned/dated
   actions (`smart_actions.validate_register`: a named role-label owner + an ISO due
   date + a measure). No anonymous actions, no "ASAP".
7. **Close the observer-feedback loop** — two-way, immediate feedback (positive AND
   at-risk discussed on the spot); learning fed back to observers and the workforce so
   the program produces systemic improvement, not a tally.
8. **Validate against `references/QUALITY_CHECKLIST.md`** — observable site-specific
   behaviours only; cards non-punitive / role-labelled / voluntary; no `<5` cell
   published; at-risk behaviours routed to system fixes (no retrain-the-worker-only
   treatment); metrics defined; every action owned + dated; ISO 45001 clause 5.4 cited
   accurately; de-id applied.
9. **Assemble the branded report** — build `report.json` (see `assets/report.json`)
   and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge
the assembled work before deciding to fan out. The **deterministic control-ranking
step (5 via `controls`) and metric computation (4 via `KB-DATA-BBS-METRICS`) are
A7/script-grounded in every case** — never a fan-out judgement call.

> **Scope note** — this skill **designs** the BBS program; it does not run a
> safety-culture maturity assessment (`safety-culture-assessment`), facilitate a
> leadership gemba walk (`safety-walk-gemba`), or own the leading/lagging KPI
> framework (`leading-lagging-kpi-framework`). It supplies the BBS percent-safe
> leading indicator to that KPI framework, but does not build it here.

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

This is the **moderate roster** (A6 "moderate = 2–3 fan-out") with the De-identifier
as the **sequential first gate** — here it is critical, because observation cards and
participation data are exactly the place a nameable individual can be re-identified and
punished. **Control-ranking is a deterministic A7 `controls` call** (Workflow step 5)
and **metric computation is grounded in `KB-DATA-BBS-METRICS`** (step 4) — never an LLM
fan-out job. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer). Before any
  analysis: scrub every nameable individual on any input card / log to a **role/group
  label**; ensure **no card records a named individual for discipline**; apply the
  **`<5` small-cell suppression** + secondary suppression to any team breakdown. Return
  the re-identification key SEPARATELY to the orchestrator — never to a sibling, never
  in the document. Every job below consumes only this scrubbed output.
  SCOPE-OUT: does not design the card (Program-Designer) or rank the fixes (the A7
  `controls` call).
- **Program-Designer** — build the **ABC map**, the **non-punitive observation card**
  (observable, site-specific items only), the **defined metrics** (percent-safe /
  participation / trend-by-category from `KB-DATA-BBS-METRICS`), and the
  **observer-feedback loop**. Refuse any non-observable item ("work safely").
  SCOPE-OUT: the deterministic control-ranking of at-risk behaviours (the A7 `controls`
  call), the SMART action register (Action-Planner).
- **Action-Planner** — turn each **trended at-risk category** into a **system fix**
  routed through the `controls` engine (hierarchy-ranked, never "retrain the worker"),
  then into a SMART action with a named **role-label** owner + an ISO due date + a
  measure (`smart_actions.validate_register`). SCOPE-OUT: designing the card
  (Program-Designer), de-identification (De-identifier).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off
  in **`references/sme-review.md`** (**Behavioural Safety Consultant**) before any
  output: cards non-punitive and observable, at-risk behaviours routed to system fixes
  (no retrain-the-worker-only treatment), metrics defined with `<5` suppression, no
  individual named on a card.
- **Critic/QA** (MANDATORY) — adversarial final pass: every card item observable and
  site-specific, cards role-labelled/voluntary, at-risk behaviours routed to
  hierarchy-ranked system fixes (no retrain-the-worker-only treatment), metrics defined
  and `<5`-suppressed, every action owned + dated, ISO 45001 clause 5.4 cited
  accurately, and **ZERO de-identification leak** (no named-individual discipline card,
  no `<5` cell, no re-id key in the output). PASS/FAIL.

A single crew with one card set may run single-threaded — no subagents — but the
De-identifier scrub + `<5` suppression, the A7 `controls` ranking call, and the
Critic/QA pass are **still made**.

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
