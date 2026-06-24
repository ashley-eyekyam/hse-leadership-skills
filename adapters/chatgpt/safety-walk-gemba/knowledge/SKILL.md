---
name: safety-walk-gemba
description: Designs and runs a consultant-grade leadership safety walk / gemba walk
  (genchi-genbutsu "go and see") for a named area, task, or shift. Use this skill
  whenever a leader, manager, or supervisor wants to run a felt-leadership safety
  walk, a gemba walk, a leadership site visit, a safety conversation or engagement
  walk, or a worker-engagement / felt-leadership round — NOT a tick-box safety inspection
  or audit. It builds the walk from OPEN conversation prompts (engagement, never a
  closed yes/no checklist), captures worker concerns role-labelled to protect psychological
  safety, and converts every commitment made on the walk into an owned, dated smart_actions
  action tracked to closure — the count and closure-rate of which is itself a leading
  indicator. Grounded in ISO 45001:2018 clauses 5.1 (leadership and commitment) and
  5.4 (consultation and participation of workers) and HSE HSG65 felt leadership. Decision-support
  only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: culture
  tier: 2
  audience:
  - M
  - E
  - F
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-leadership
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Safety Walk Gemba

A consultant-grade HSE skill that designs and runs a **leadership safety walk / gemba
walk** (*genchi-genbutsu* — "go and see") for a **named area, task, or shift**, grounded
in **ISO 45001:2018 clauses 5.1** (leadership and commitment) and **5.4** (consultation
and participation of workers) and **HSE HSG65 felt leadership** (`KB-SNIP-GEMBA-PROMPTS`,
`KB-SNIP-LEADERSHIP-CLAUSE-MAP`). It forces the single lever that separates an engagement
walk from copy-paste paperwork: the walk is built from **OPEN conversation prompts** that
invite the worker's own account — **never a closed yes/no tick-box checklist** (a closed
checklist is an audit, not a gemba walk, and is **flagged** for specificity/defensibility).
Worker concerns are captured **role-labelled** to protect psychological safety — **no
concern is ever attributed to a nameable individual**. And every **commitment** the leader
makes on the walk becomes an **owned, dated `smart_actions` action tracked to closure** —
the **count and closure-rate of walk commitments is itself a leading indicator**
(`KB-DATA-LEADING-INDICATORS`). A walk that produces no tracked commitment fails the
defensibility gate: a walk is not a conversation that evaporates, it is commitments owned,
dated, and closed.

## When to use this skill

Use this skill when a leader, manager, or supervisor wants to run an **engagement** safety
walk for a **named area / task / shift** — for example "design a felt-leadership safety
walk for the night-shift warehouse pick-face", "run a gemba walk on the line-2 changeover
and capture what the operators actually deal with", or "I'm doing a leadership site visit
on the scaffold deck — give me open prompts and turn my commitments into tracked actions".
Trigger phrases: *safety walk, gemba walk, genchi-genbutsu, felt-leadership walk / round,
leadership site visit, safety conversation / engagement walk, worker-engagement walk,
walk-and-talk*. This skill is **not** a tick-box safety inspection or audit (that is a
`safety-audit`), **not** a behaviour-observation programme (that is `bbs-program-designer`),
**not** a maturity survey (that is `safety-culture-assessment`), and **not** a KPI
framework (that is `leading-lagging-kpi-framework`) — intake **Q1 disambiguates** the walk
from these siblings. If the request is vague, or asks for a closed yes/no checklist, the
Workflow intake below **refuses to proceed** and steers to open, area-specific prompts.

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

<!-- The rows below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for what this skill
     serves; rule-9 checks every path/ID resolves against the KB registries. -->

This skill **always** grounds the walk in the gemba prompt bank, the leadership clause
map, and the leading-indicator catalogue, then resolves the jurisdiction only for any
consultation/participation legal duty:

| Read on every run | File |
|---|---|
| The **open-question gemba prompt bank** by purpose/area (felt-leadership/engagement · hazard-spotting · control-verification · post-incident) — engagement, never a tick-box; concerns role-labelled; commitment-closure as a leading indicator | ../../knowledge-base/prompt-snippets/gemba-prompts.md (KB-SNIP-GEMBA-PROMPTS) |
| The **ISO 45001 leadership clause cross-walk** — this skill owns clauses **5.1** (leadership and commitment, felt leadership) and **5.4** (consultation and participation of workers) | ../../knowledge-base/prompt-snippets/leadership-clause-map.md (KB-SNIP-LEADERSHIP-CLAUSE-MAP) |
| The **leading/lagging indicator catalogue** (single-sourced) — read the **gemba-commitment closure-rate** entry; report walk-commitment closure as a leading indicator, quote `source`+`year` | ../../knowledge-base/data-points/leading-indicators.md (KB-DATA-LEADING-INDICATORS) |
| ISO 45001:2018 — the management-system backbone for clauses 5.1 / 5.4 | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001) |

| Jurisdiction (intake Q-juris) | Read for any consultation/participation legal duty |
|---|---|
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (HSWA 1974 + the consultation-of-employees duty) |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (OSH Framework Directive 89/391/EEC — worker consultation) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (safety-committee / worker-participation provisions; defers to `hse-india`; **mandatory state detection**, never a national form number) |
| Unknown | Ask before citing any specific law — the gemba method (open prompts, felt leadership, tracked commitments) still applies |

Always apply `KB-SNIP-HOC` to any control a commitment implies. For the
**commitment-closure leading indicator**, resolve the ID in `KB-DATA-LEADING-INDICATORS`
and quote its `source`+`year` — never a remembered figure. The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table,
the echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run
it one question at a time, branch on the answers, **echo the captured facts back before
any analysis**, and **refuse to proceed on a vague request**. The hard anchors:

1. **Q1 (purpose + which skill)** — confirm this is an **engagement walk**, and
   **disambiguate** it from the siblings: a tick-box **inspection/audit** → `safety-audit`;
   a structured **behaviour-observation programme** → `bbs-program-designer`; a **maturity
   survey** → `safety-culture-assessment`; a **KPI framework** → `leading-lagging-kpi-framework`.
   **If the user asks for a closed yes/no checklist, refuse** — a gemba walk is open prompts,
   not a tick-box, and steer them to the open prompt bank (or to `safety-audit` if they truly
   want an inspection).
2. **Q-subject (named area / task / shift)** — the **specificity anchor**. Refuse a vague
   "do a site walk" — name the **specific area, task, or shift** the walk covers, because
   the prompt families are selected per area.
3. **Q-evidence (walk purpose → prompt family)** — felt-leadership/engagement ·
   hazard-spotting · control-verification · post-incident reassurance — selects the open
   prompts from `KB-SNIP-GEMBA-PROMPTS`.

### The gemba-walk method (felt leadership / genchi-genbutsu)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST** — any worker concerns, names, or shift/role detail the
   user brings are scrubbed to **role labels** before any drafting (the `deid` block above +
   `references/deid-checklist.md` + the De-identifier-runs-first orchestration rule). Worker
   concerns are captured **role-labelled** (psychological safety) — **never attributed to a
   nameable individual**. A named-worker→concern attribution is a `de_identification`
   **hard-fail**.
2. **Select the open prompts by purpose + area** — from `KB-SNIP-GEMBA-PROMPTS`, pick the
   prompt family for the walk's purpose (Q-evidence) and anchor each prompt to the **specific
   area/task** (Q-subject). Prompts are **open, area-specific, non-interrogative** — they
   invite the worker's own account. **A closed yes/no tick-box checklist is refused** and
   flagged (specificity · defensibility).
3. **Run the conversation, capture concerns role-labelled** — record what workers raise
   against role/group labels only; no individual is named. Flag `[GAP]` where the walk did
   not reach an area in scope.
4. **Convert every commitment to an owned/dated action** — each commitment the leader makes
   on the walk becomes a **SMART action** (specific, measurable, **assignable (named
   role-label owner)**, relevant, **time-bound (ISO due date)**) via
   `smart_actions.validate_register`. **No anonymous commitments, no "ASAP".** Any control a
   commitment implies is ranked via `KB-SNIP-HOC` (`controls`), higher-order first.
5. **Report commitment closure as a leading indicator** — the **count and closure-rate of
   walk commitments** is a leading indicator (resolve `KB-DATA-LEADING-INDICATORS`, quote
   `source`+`year`). A walk that produces **no tracked commitment fails the defensibility
   gate** — it is recorded as `[GAP]`, not signed off as complete.
6. **Validate against `references/QUALITY_CHECKLIST.md`** — open prompts (not tick-box);
   every concern role-labelled (no individual named); every commitment owned + dated +
   tracked to closure; commitment closure surfaced as a leading indicator; ISO 45001 5.1/5.4
   cited accurately; de-id applied.
7. **Assemble the branded report** — build `report.json` (see `assets/report.json`) and run
   the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled walk before deciding to fan out. The **De-identifier runs FIRST** as a sequential
gate in every case.

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

This is the **moderate roster** with the **De-identifier as the sequential first gate** —
critical here because worker concerns raised on a walk are sensitive: attributing a concern
to a nameable individual breaks psychological safety. **Commitment-to-action conversion is a
deterministic `smart_actions` call** at Workflow step 4 — never an LLM fan-out job.
Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer). Before any
  drafting: scrub every nameable individual to a **role/group label**; capture worker
  concerns role-labelled (psychological safety); ensure **no concern is attributed to a
  nameable individual**. Apply `references/deid-checklist.md` in full. Return the
  re-identification key SEPARATELY to the orchestrator — never to a sibling, never in the
  document. Every job below consumes only this scrubbed output. SCOPE-OUT: does not select
  prompts (Walk-Designer) or draft actions (Commitment-Tracker).
- **Walk-Designer** — for the walk's purpose + area (intake Q-evidence / Q-subject), select
  the **open conversation prompts** from `KB-SNIP-GEMBA-PROMPTS`; anchor each to the specific
  area/task; keep them open, area-specific, non-interrogative. **Refuse a closed tick-box
  checklist.** Consumes only the scrubbed output; names roles/groups, never individuals.
  SCOPE-OUT: converting commitments to actions (Commitment-Tracker).
- **Commitment-Tracker** — turn **each commitment** made on the walk into a **SMART action**
  with a named **role-label** owner + an ISO due date + a measure (`smart_actions.validate_register`),
  and surface the **commitment count / closure-rate as a leading indicator**
  (`KB-DATA-LEADING-INDICATORS`). SCOPE-OUT: selecting prompts (Walk-Designer),
  de-identification (De-identifier).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (HSE Leadership / Engagement Coach) before any output: open
  prompts (not a tick-box), worker concerns role-labelled (no individual named), every
  commitment owned + dated + tracked to closure, commitment closure surfaced as a leading
  indicator.
- **Critic/QA** (MANDATORY) — adversarial final pass: open prompts not a closed checklist,
  every commitment owned + dated + tracked to closure (no untracked commitment), commitment
  closure reported as a leading indicator, ISO 45001 5.1/5.4 cited accurately, and **ZERO
  de-identification leak** (no concern attributed to a nameable individual, no re-id key in
  the output). PASS/FAIL.

A single short walk with one area may run single-threaded — no subagents — but the
De-identifier scrub, the `smart_actions` commitment conversion, and the Critic/QA pass are
**still made**.

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
