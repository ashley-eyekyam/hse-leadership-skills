---
name: training-needs-analysis
description: Produces a consultant-grade, role-by-competence Training Needs Analysis
  (TNA) for a named site, function, or project. Use this skill whenever a user asks
  to identify training gaps, build a competence or training matrix, map roles to required
  competencies, plan a training programme, track certification expiry, or run a TNA
  grounded in ISO 45001 clause 7.2 (competence). It builds a role×competence matrix,
  scores current-vs-required competence from evidence, flags single-points-of-failure
  and expiring certifications, and emits a prioritised, costed training plan with
  named owners and due dates as a branded report. Decision-support only; a competent
  person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: training
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
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Training Needs Analysis

A consultant-grade HSE skill that produces a **role-by-competence Training Needs
Analysis (TNA)** for a named site, function, or project, grounded in **ISO 45001
clause 7.2 (competence)** and **7.3 (awareness)**. It builds a **role×competence
gap matrix** (each cell scored current-vs-required on the shared 4-level competence
scale `KB-DATA-COMPETENCE-LEVELS`, from a named evidence source), flags
**single-points-of-failure** (a critical competence held by only one person),
tracks **certification expiry/refresher dates**, and emits a **prioritised, costed
training plan** with named owners and due dates. It forces the single lever that
separates a defensible artifact from copy-paste paperwork: **named roles + an
evidence source for every gap** — it refuses "train everyone", and it never ships
"more training" as the sole control of a hazard that admits a higher-order control
(training is an **administrative** control under `KB-SNIP-HOC`).

## When to use this skill

Use this skill when the user needs a Training Needs Analysis for a **named site,
function, or project** — for example "identify the training gaps for the
scaffolding crew on the north tower", "build a competence/training matrix for the
warehouse despatch team", "map our supervisor roles to required competencies",
"track which forklift and first-aid certificates are expiring", or "plan a costed
training programme after the audit finding". Trigger phrases: *training needs
analysis, TNA, training gaps, competence matrix, training matrix, role-to-competence
mapping, certification/expiry tracking, training plan, refresher schedule,
single-point-of-failure competence*. It pairs with **`induction-pack` (#14)** for
clause 7.3 awareness/induction (this skill owns clause **7.2 competence**; see
`KB-SNIP-OPS-CLAUSE-MAP`). If the request is vague ("write a training plan", "train
everyone") the Workflow intake below **refuses to proceed** until the **named roles
+ at least one competence source** are captured.

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

The jurisdiction row resolves the **legal-required competencies** (the Q5 legal-competence
row of the matrix) — statutory training/competence duties that can never be omitted or
downgraded to "pass". Resolve the jurisdiction first; for India, resolve the **state** and
defer to `hse-india` (never mint a national form number).

| Jurisdiction | Read | Legal-competence duty |
|---|---|---|
| UK    | ../../knowledge-base/regulatory/uk-hswa.md | MHSWR 1999 reg. 13 (capabilities & training); HSWA s.2(2)(c) |
| USA   | ../../knowledge-base/regulatory/us-osha.md | Standard-specific training (29 CFR 1910.132(f) PPE; 1910.147(c)(7) LOTO; etc.) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) | Factories Act 1948 s.7A(2)(c) — **defers to `hse-india`**, resolve the state |
| EU    | ../../knowledge-base/regulatory/eu-osh.md | Framework Directive 89/391/EEC art. 12 (training) |
| Unknown | Ask before citing any specific law | — |

This skill always grounds in `KB-STD-ISO45001` (7.2 competence + 7.3 awareness), bands every
role×competence cell on `KB-DATA-COMPETENCE-LEVELS` (the shared 4-level scale), follows the
gap-scoring + prioritisation method in `KB-SNIP-TNA-METHOD`, and applies `KB-SNIP-HOC` so
training is framed as an **administrative** control (never the sole treatment). It references
`KB-SNIP-OPS-CLAUSE-MAP` for the bundle clause cross-walk (TNA owns clause 7.2). The rule-9
manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(Q1 scope · Q2 roles-in-scope · Q3 competence sources · Q4 drivers · Q5 jurisdiction ·
Q6 budget/time, plus the headcount, location, evidence, scoring-scale, owners and
review-cadence anchors), the **mandatory India→state branch** (Q5 = India → Q5a), the
echo-back, and the **refuse-on-vague anchors** — lives in **`references/intake.md`**. Run
it one question at a time, branch on the answers, **echo the captured facts back before any
analysis**, and **refuse to proceed** until at least the **named roles (Q2 — refuse
"everyone") and one competence source (Q3)** are captured. No matrix is produced on "train
everyone" or an unnamed role set.

### The TNA method (ISO 45001 7.2 competence + the `KB-SNIP-TNA-METHOD` gap-scoring loop)

Full method in `references/METHODOLOGY.md`; the gap-scoring + prioritisation rules are
`KB-SNIP-TNA-METHOD`, banded against `KB-DATA-COMPETENCE-LEVELS`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Competence/appraisal data is **personal
   data**: every name becomes a **role label**; the matrix circulates by role, not identity.
   Everything downstream consumes the scrubbed, role-labelled text.
2. **Profile the named roles** — for each role in scope (Q2; **refuse "everyone"**), derive
   the **required competencies** from job profile, the task's real hazards, and any
   **legal-required competency** (resolve the Q5 jurisdiction row and **cite the statutory
   source** — e.g. UK MHSWR 1999 reg. 13, US 29 CFR 1910.147(c)(7) LOTO, India Factories Act
   1948 s.7A(2)(c) via `hse-india`). A statutory competence requirement is **never omitted**.
3. **Establish current state from evidence** — band each role×competence cell's **current
   level** on `KB-DATA-COMPETENCE-LEVELS` (aware → trained → competent → expert) from a
   **named evidence source** (Q3: job descriptions / legal-required competencies / training
   records / appraisal data / incident-driven gaps). **Never assert a level without
   evidence** — flag `[GAP]` where evidence is absent.
4. **Score the gap = required level − current level** — a statutory competence requirement
   that is unmet is a gap against its named legal source and is **never downgraded to pass**
   to green the matrix.
5. **Flag single-points-of-failure** — a critical competence held by **only one** named
   person is a SPOF: report it **by role, not identity** (small-cell suppression where one
   named person is the sole holder — report the gap, not the person).
6. **Frame training in the hierarchy of controls** — apply `KB-SNIP-HOC` + `controls`:
   training is an **administrative** control. Where a hazard admits a higher-order control
   (eliminate/substitute/engineer), **"more training" is never the sole treatment** — call
   `controls.validate_treatment`; an admin-only treatment with no higher-order control and no
   justification is a **defect the Critic/QA pass must catch**.
7. **Prioritise** by `gap size × (risk of the task it gates) × legal-mandate` — statutory and
   high-hazard competence gaps rank first; build the **certification/expiry tracker** (which
   certificates expire when, and the refresher due date).
8. **Plan as SMART actions (named owners + dates)** — for every prioritised gap produce a
   SMART action via `smart_actions.validate_register` (specific, measurable, **assignable
   (named owner)**, relevant, **time-bound (ISO due date)**) with an indicative cost. Any
   action missing an owner, a valid date, a measure, or a gap link is **invalid** — no "TBD",
   no "ASAP".
9. **Validate against `references/QUALITY_CHECKLIST.md`** — every gap traced to a named role
   + an evidence source; every legal-required competency present + cited; no admin-only
   treatment without justification; every action owned + dated; the matrix circulates by role
   label; de-id applied; no conclusion on an unstated assumption.
10. **Assemble the branded report** — build `report.json` (see
    `assets/training-needs-analysis-report.template.json`) and run the canonical
    `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **deterministic `smart_actions` /  `controls`
calls (steps 6, 8) are A7 script calls in every case** — never a fan-out job.

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

This is a **moderate roster** (A6 "moderate = 2–3") — the triage gate fans out only for a
**large or multi-function TNA (≥10 roles or multiple functions)**; a single function runs
single-threaded. The De-identifier is the **sequential first gate** (not a fan-out peer).
Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub every name in
  the training/appraisal records to **role labels** before any analysis. Competence/appraisal
  data is personal data; the matrix circulates by role, not identity; suppress small cells
  where one named person is the sole holder of a competence. Every job below consumes only its
  scrubbed output, and the re-identification key is returned **separately** to the
  orchestrator (never to a sibling, never into the matrix).
- **Competence-Requirement-Mapper** — for the resolved jurisdiction, map each named role
  (Q2) to its **required competencies**, including the **legal-required competencies** (cite
  the statutory source via the Q5 jurisdiction row; India → resolved STATE via `hse-india`).
  Flag `[GAP]` and "ask a competent person" when a statutory requirement is unclear — never
  invents a competence requirement or a form number. SCOPE-OUT: scoring the gaps + planning
  (Gap-Scorer-&-Planner owns it).
- **Gap-Scorer-&-Planner** — band each role×competence cell current-vs-required on
  `KB-DATA-COMPETENCE-LEVELS` from the named evidence (Q3), score the gap, flag
  single-points-of-failure (by role), build the certification/expiry tracker, and draft the
  **prioritised costed training plan** as SMART actions (`smart_actions`) with owners + dates,
  framing training as an administrative control (`controls` + `KB-SNIP-HOC`). SCOPE-OUT:
  deriving the requirements (Competence-Requirement-Mapper) or checking the law.
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (**Competence & Training Manager**) before any output: gaps
  evidence-traced, legal-required competencies never omitted, no individual's gap published by
  name, no training-only treatment of a higher-order-controllable hazard.
- **Critic/QA** (MANDATORY) — adversarial final pass: every gap traced to a named role + an
  evidence source, every legal-required competency present + cited, no admin-only control
  without justification, every action owned + dated, the matrix by role label, zero PII leak.
  PASS/FAIL.

Simple single-function analyses run single-threaded — no subagents — but the `smart_actions` /
`controls` calls and the Critic/QA + SME passes are still made.

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
