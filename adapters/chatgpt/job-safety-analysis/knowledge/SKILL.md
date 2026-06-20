---
name: job-safety-analysis
description: Creates consultant-grade, task- and site-specific job safety analyses
  (JSA / JHA — job hazard analysis). Use this skill whenever a user asks to build
  or review a JSA, JHA, or job hazard analysis, break a job or task into steps and
  assess the hazards of each step, perform a task-step risk analysis, or produce a
  step-by-step safe-work analysis for a specific physical job — in manufacturing,
  oil & gas, construction, or mining. It decomposes the job into its ordered steps,
  identifies the hazards of each step, scores each step on the org's risk matrix,
  ranks controls by the hierarchy of controls per step (no PPE-only steps without
  justification), re-scores residual risk per step, and assigns SMART corrective actions
  with named owners and due dates — emitting a branded JSA report. For a whole-activity
  risk assessment use the risk-assessment skill; to investigate an event that occurred
  use incident-investigation. Decision-support only; a competent person must review
  the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 1
  audience:
  - M
  - F
  - C
  industry:
  - Mfg
  - O&G
  - Con
  - Min
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Job Safety Analysis (JSA / JHA)

A consultant-grade HSE skill that produces a task/site/asset-specific **step-by-step**
Job Safety Analysis (a.k.a. Job Hazard Analysis), grounded in **ISO 45001 clause 6.1.2**
applied *per step* and enforcing the **hierarchy of controls** (8.1.2) at step granularity.
Its distinctive spine is **task-step decomposition**: it breaks a physical job into its
ordered sequence of steps, then for **each step** identifies the hazards, scores the
initial risk, ranks controls (Elimination → … → PPE), and re-scores the residual risk —
finally consolidating the per-step controls into SMART actions with named owners and dates.
The deterministic scoring/ranking is the A7 `risk_matrix`/`controls` engines called **once
per step**, never prose judgement; the single lever the pack forces — task specificity plus
the full hierarchy of controls, never a PPE-only step — bites here at *step* granularity.

## When to use this skill

Use this skill when the user needs a **step-by-step** safety analysis of a **concrete
physical job** — for example "walk me through cleaning tank T-402 **step by step** and give
me a JSA", "build/review a JHA for working at height on the north roof", "break this welding
job into steps and assess the hazards of each step", or "produce a safe-work method statement
for the line changeover". Trigger phrases: *JSA, JHA, job safety analysis, job hazard
analysis, task-step analysis, step-by-step, safe work method, job steps, hazard per step,
hierarchy of controls, residual risk, risk matrix, controls*.

**When NOT to use this skill:**

- For a **whole-activity** risk assessment (one register, one row per *hazard*, not per
  *step*) use the **`risk-assessment`** skill (B1, HIRA/HIRARC) — that is its job, and a JSA
  would lose its reason to exist.
- To **investigate an event that already happened** (root-cause analysis, CAPA from an
  incident) use the **`incident-investigation`** skill (B5).

If the request is vague ("write me a JSA") or names a job with no steps, the Workflow intake
below **refuses to proceed** until the specific job *and its ordered step sequence* are
elicited — a JSA with no steps is not a JSA.

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

| Jurisdiction | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (construction → CDM 2015 reg. 13/15 + Construction Phase Plan rows, KB-REG-UK-HSWA) |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (**6.1.2** hazard identification &
assessment of risks, applied per step + **8.1.2** hierarchy of controls) and applies
`KB-SNIP-HOC` to every per-step control; for an India site it resolves the state via
`KB-REG-IN-STATEFORMS` (mandatory state detection — confirm the state before citing any
form, never a national form number); for UK construction work it cites the CDM 2015
rows in `KB-REG-UK-HSWA` (reg. 13 / reg. 15 / Construction Phase Plan). This is a
**safety-only** skill — there is **no ISO 14001 environmental branch** (for environmental
aspects use `risk-assessment`). The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(jurisdiction · industry · the job anchor Q3 · the **ordered step sequence Q4 — THE
SPINE** · tools/materials · SDS held · who-performs + competencies · environment ·
permits-to-work · location · likelihood/severity/matrix · review trigger), the
**mandatory India→state branch** (Q1 = India → Q1a), the **SDS-evidence branch** (Q5
names a substance → Q5b), the echo-back, and the refuse-on-vague anchors — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo
the captured facts back before any analysis**, and **refuse to proceed on a vague job or
an empty/one-line step list** (Q3/Q4 are the spine — record `[ASSUMPTION]` / `[GAP]`,
never invent a step). A JSA with no steps is not a JSA.

### The JSA method (ISO 45001 6.1.2 loop, run PER STEP)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Everything downstream consumes the
   scrubbed, role-labelled text.
2. **Confirm + normalise the step sequence** — restate the job's steps as an **ordered
   list** (Step 1, Step 2, …) exactly as the user described them; this ordered list is the
   skeleton the rest of the Workflow iterates over. If the sequence has obvious gaps (e.g.
   an isolation step missing before a maintenance step), **ask** rather than silently
   inserting — an unconfirmed step is recorded `[GAP]`, never invented.
3. **Per-step hazard identification** — **for each step in the confirmed sequence**,
   identify the specific, observable hazards *of that step* (the energy sources — gravity /
   electrical / mechanical / pressure / chemical / thermal / kinetic — substances, plant,
   environment, human factors introduced *by performing that step*), grounded in
   `KB-STD-ISO45001` 6.1.2; each hazard pairs **what** is hazardous in the step with **its
   energy source** and names **who/what is exposed**. Flag `[GAP]` where a step's hazards
   are uncertain — never invent.
4. **Per-step initial risk scoring** — **for each step's hazard(s)** call
   `risk_matrix.load_matrix(config)` once (Q11; default `DEFAULT_5X5`) then
   `risk_matrix.score(likelihood, severity, matrix)`. The score + band are the engine's,
   deterministically — not prose. Each step carries its own initial-risk rating.
5. **Per-step control selection (the hierarchy-of-controls lever)** — **for each step**
   propose controls and **apply `KB-SNIP-HOC`**: rank Elimination → Substitution →
   Engineering → Administrative → PPE; then call `controls.rank_controls` +
   `controls.validate_treatment`. If a step's `ppe_admin_only` is `True`, the Workflow
   **must** either add a higher-order control for that step **or** record an explicit
   per-step justification ("for this step, higher-order controls not reasonably practicable
   because…"). **A step left with a lower-order-only treatment and no justification is a
   defect the Critic/QA pass must catch** — the hard enforcement of the core value at step
   granularity, not a mention.
6. **Per-step residual re-scoring** — **for each step** re-score the step *with its
   selected controls applied* via `risk_matrix.score`, then
   `risk_matrix.residual_delta(initial, residual)` to show the movement for that step. A
   step whose residual remains High/Critical needs additional controls or a stop/hold
   decision before it is performed (not "accept and proceed").
7. **Consolidate per-step controls into SMART actions (named owners + dates)** — gather the
   controls that are *actions* (not already in place) across all steps into one register;
   for each produce a SMART action (specific, measurable, **assignable (named owner)**,
   relevant, **time-bound (ISO due date)**, **linked to the step + hazard it addresses**).
   Call `smart_actions.validate_register`; any action missing an owner, a valid date, a
   measure, or a step/hazard link is **invalid** and must be fixed — no anonymous actions,
   no "ASAP".
8. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check loop before
   output: every step decomposed + confirmed (none invented); every step's hazards
   identified + scored; every step's controls HoC-ranked; no step with an un-justified
   lower-order-only treatment; every action owned + dated + step/hazard-linked; every
   citation traced to the KB (ISO 45001 6.1.2 always; the jurisdiction fragment + India
   state form where raised); de-id applied; no conclusion on an unstated assumption.
9. **Assemble the branded JSA report** — build `report.json` (see
   `assets/jsa-report.template.json` — the **JSA table** is the core, plus the **sign-off /
   acceptance block**) and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **deterministic per-step scoring/ranking
steps (4, 5, 6 via `risk_matrix`/`controls`) are A7 script calls in every case — never a
fan-out job** (there is no "Risk-Scorer" / "Step-Scorer" subagent).

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

This is the **STANDARD moderate roster** (A6 "moderate = 2–3"), inherited from the B1
`risk-assessment` flagship: the De-identifier is the **sequential first gate** (not a
fan-out peer), the **3 fan-out jobs** are Researcher + Regulatory-Checker + Drafter, and
**Critic/QA is mandatory**. **There is no Risk-Scorer / Step-Scorer subagent** — per-step
scoring, residual re-scoring, and control ranking are deterministic A7 script calls at
Workflow steps 4/5/6 (`risk_matrix`, `controls`), never LLM fan-out work. Archetypes:
`KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all
  PII/health detail to role labels before any analysis (every fan-out job below consumes
  scrubbed text).
- **Researcher** — gather evidence for the hazards of the **named steps** from primary
  sources (equipment/substance/process data, prior-incident patterns for this task type);
  cited summary, flag `[GAP]`. SCOPE-OUT: law (Regulatory-Checker), drafting (Drafter).
  (Per-step scoring is NOT a subagent — it is the A7 `risk_matrix` script.)
- **Regulatory-Checker** — for the resolved jurisdiction, return the applicable duty +
  clause + (India) the state form via `KB-REG-IN-STATEFORMS`, and any permit-to-work
  triggers the steps imply (confined space, hot work, working at height); conservative,
  flag `[GAP]`. SCOPE-OUT: drafting the JSA, gathering hazard evidence (Researcher).
- **Drafter** — write the JSA table (step → hazards → initial risk → controls[HoC tier] →
  residual) + the consolidated control/action register + the sign-off block to the output
  template using **role placeholders** (no fabricated names); each control tagged its
  `KB-SNIP-HOC` tier (consumes the De-identifier's scrubbed text + the A7
  `risk_matrix`/`controls` per-step scores + the Regulatory-Checker's verdict). SCOPE-OUT:
  gathering evidence (Researcher), checking law (Regulatory-Checker).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (frontline safety / work-method & permit-to-work
  specialist) before any output: the job decomposed into REAL ordered steps, each step's
  hazards controlled at step granularity (no PPE-only step) and the right permits triggered.
- **Critic/QA** (MANDATORY) — every step decomposed + confirmed (none invented), every
  step's hazards scored (via the A7 engine), every step's controls HoC-ranked, no step left
  PPE/admin-only without justification, every action owned + dated + step/hazard-linked,
  every citation traces to the KB, zero PII leaked (including no fabricated names in the
  sign-off block). PASS/FAIL.

Researcher + Regulatory-Checker may merge to land at 2 fan-out jobs and stay in-band.
Simple two-step quick checks run single-threaded — no subagents — but the A7 per-step
scoring/ranking calls and the Critic/QA pass are still made. (B2 is *not* a
single-threaded-by-design skill like `toolbox-talk`; it ships this moderate roster.)

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
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
