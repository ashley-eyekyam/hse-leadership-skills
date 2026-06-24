---
name: contractor-prequalification
description: Produces a risk-tiered contractor prequalification questionnaire (PQQ)
  and an evidence-based scoring/evaluation of a contractor's HSE capability for a
  named scope of work. Use this skill whenever a user asks to prequalify, vet, or
  approve a contractor or subcontractor, build a PQQ or contractor-approval questionnaire,
  score a contractor's safety credentials, or set up contractor HSE management. It
  tiers the rigour to the work's risk, asks for verifiable evidence (not claims),
  scores against defined criteria, and produces an approve/conditional/reject recommendation
  with named conditions and review dates — emitted as a branded report. Decision-support
  only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: contractor
  tier: 2
  audience:
  - M
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-operations
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Contractor Prequalification

A consultant-grade HSE skill that produces a **risk-tiered contractor prequalification
questionnaire (PQQ)** and an **evidence-based scorecard** of a contractor's HSE capability
for a **named scope of work**, grounded in **ISO 45001 clause 8.1.4 (procurement /
contractors / outsourcing)**. It forces the single lever that separates a defensible
appointment from a rubber-stamp: it **tiers the rigour of questioning to the work's risk**
and **scores only against verifiable evidence — never a self-asserted claim**. Missing or
unverifiable evidence becomes a `[GAP]` that blocks an unconditional pass; high-hazard
work cannot pass on PPE/competence claims alone. The output is an
**approve / conditional / reject** recommendation with **named conditions, owners, and a
review date** — emitted as a branded report.

The risk-tier → PQQ-depth → pass-threshold map (`KB-DATA-CONTRACTOR-TIERS`) and the
evidence-anchored question bank (`KB-SNIP-PQQ-BANK`) are **cited rubrics applied as
structured prose** — there is **no `contractor_score` engine**; the discipline is that
every score is tied to a verified evidence item.

## When to use this skill

Use this skill when the user needs to **prequalify, vet, or approve a contractor or
subcontractor** for a concrete scope of work on a named site — for example "prequalify
 acme scaffolding for the work-at-height package on the Plant 3 turnaround", "build a PQQ
for our mechanical-install subcontractor", "score this contractor's safety credentials",
or "set up contractor HSE management for the demolition phase". Trigger phrases:
*contractor prequalification, PQQ, contractor approval, vet a subcontractor, contractor
HSE management, SSIP, approve/reject a contractor, contractor scorecard*. It tiers the
depth of questioning to the work's risk (T1 low/admin · T2 medium · T3 high-hazard), asks
for **verifiable evidence not claims**, and produces an approve/conditional/reject
recommendation. If the request is vague ("approve this contractor"), the Workflow intake
below **refuses to score** until the scope+risk tier and the core evidence set are captured.

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
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (HSWA s.3/s.4 + **CDM 2015 reg. 8** where the work is construction) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (OSHA **multi-employer worksite policy CPL 02-00-124** — controlling-employer duty) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` **clause 8.1.4** (procurement / contractors /
outsourcing) and applies `KB-SNIP-HOC` to every control it evaluates in the contractor's
proposed safe system of work. It sets PQQ depth and the pass threshold from the
**risk-tier map `KB-DATA-CONTRACTOR-TIERS`** (T1 low / T2 medium / T3 high-hazard — tier set
by the *highest-risk activity* in the scope), and draws the evidence-anchored questions from
**`KB-SNIP-PQQ-BANK`** (each question tied to its required evidence). It locates itself in
the bundle via the operations clause cross-walk **`KB-SNIP-OPS-CLAUSE-MAP`** (8.1.4 →
contractor-prequalification). For an India site it resolves the state via
`KB-REG-IN-STATEFORMS` (mandatory state detection — never a national form number). The
rule-9 manifest is `references/_skill-kb.md`. Quote each fragment's `source`+`year`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(scope & risk tier Q1 · contractor & work package Q2 · evidence available Q3 · jurisdiction
Q4 · decision type Q5), the **risk-tier branch** (Q1 = high-hazard → the T3 high-hazard
PQQ module + the higher pass threshold), the **mandatory India→state branch** (Q4 = India →
Q4a), the echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**.
Run it one question at a time, branch on the answers, **echo the captured facts back before
any analysis**, and **refuse to score** until the scope+risk tier and at least the core
evidence set (insurance + accident/enforcement history + relevant competence) are captured.
Q1 (scope & risk) is the **specificity anchor** — it sets the tier, the PQQ depth, and the
pass threshold; Q3 missing evidence becomes a **`[GAP]`** (never invent, never score a
self-asserted claim). A `[GAP]` blocks an unconditional pass.

### The prequalification method (ISO 45001 8.1.4 — risk-tiered, evidence-anchored)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST** — before any scoring (the `deid` block above + the
   De-identifier-runs-first orchestration rule). A contractor's **accident / enforcement
   history can name injured persons** (prosecutions, RIDDOR/OSHA records); scrub names,
   exact dates, and locations to role labels and **apply small-cell suppression to a small
   contractor's injury counts** *before* the evidence reaches the scorer. Everything
   downstream consumes only the scrubbed text.
2. **Assign the risk tier** — from Q1, band the scope into **T1 / T2 / T3 per
   `KB-DATA-CONTRACTOR-TIERS`**. The tier is set by the **highest-risk activity** in the
   scope, not the average — a single hot-work / confined-space / work-at-height / lifting /
   energised-electrical / demolition task lifts the whole package to **T3**. The tier sets
   the PQQ depth and the pass threshold.
3. **Build the tiered PQQ** — select the question set for the tier from **`KB-SNIP-PQQ-BANK`**
   (Core for T1+ → Task-specific for T2+ → the high-hazard module for T3). **Each question
   names the verifiable evidence that answers it** — a signed policy, a current insurance
   certificate, the RAMS, an in-date accreditation certificate (SSIP / ISO 45001), the
   activity-specific competence certification, the de-identified accident-rate data.
4. **Build the evidence register & verify** — for every PQQ item, record the claim, the
   evidence supplied, and a **verification status** (verified / unverified / not-supplied).
   A **self-asserted claim with no supporting evidence is `[GAP]` — never scored as met**
   (the core integrity gate). Evaluate the contractor's proposed controls against the
   hierarchy via **`controls.rank_controls` / `controls.validate_treatment`** + `KB-SNIP-HOC`:
   **high-hazard (T3) work cannot pass on PPE/competence claims alone** — higher-order
   controls must be evidenced.
5. **Score against the threshold** — score each criterion **only on its verified evidence**,
   then apply the tier's pass threshold (`KB-DATA-CONTRACTOR-TIERS`). This is **cited-rubric
   structured prose, not a deterministic engine** (§8 anti-sprawl — there is no
   `contractor_score` engine). Any score must trace to a named evidence item; an unverified
   or `[GAP]` criterion cannot clear the threshold.
6. **Recommend approve / conditional / reject** — `approve` only when every threshold
   criterion is met on **verified** evidence; `conditional` when gaps are closeable — each
   condition is a **SMART action** (`smart_actions.validate_register`: named owner + ISO due
   date + measure, tied to the gap it closes) **plus a review date**; `reject` when a
   threshold criterion fails irrecoverably (e.g. unresolved serious enforcement, no
   high-hazard competence for T3 work). Never "approve and proceed" over an open `[GAP]`.
7. **Validate against `references/QUALITY_CHECKLIST.md`** — every score tied to a verified
   evidence item; no score on a self-asserted claim; high-hazard work not passed on
   PPE/competence claims alone; every condition owned + dated; the de-id pass ran first and
   no injured person is named; ISO 45001 8.1.4 (and CDM reg. 8 / OSHA multi-employer where
   relevant) cited accurately.
8. **Assemble the branded report** — build `report.json` (see
   `assets/contractor-prequalification-report.template.json`) and run the canonical
   `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. A **single low-risk (T1) contractor runs
single-threaded**; a complex multi-package or high-hazard evaluation fans out (the De-identifier
runs first as a sequential gate). The de-identification and evidence-verification steps are
mandatory in **every** case, single-threaded or fanned-out.

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

This is the **moderate roster** (A6 "moderate = 2–3") for a complex multi-package or
high-hazard contractor evaluation. The **De-identifier is the sequential first gate** (not a
fan-out peer); there is **no `contractor_score` subagent** — the scoring is the cited
weighted rubric (`KB-DATA-CONTRACTOR-TIERS` / `KB-SNIP-PQQ-BANK`) applied as structured prose
by the Scorer-&-Recommender, with the hierarchy check via the A7 `controls` engine and the
conditions via `smart_actions`. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer); scrub the
  contractor's accident/enforcement history — **named injured persons, witnesses, exact
  dates/locations** — to role labels, and **suppress any injury cell < 5** on a small
  contractor, before any analysis. Returns the re-identification key SEPARATELY (to the
  orchestrator, never to a sibling). Every job below consumes only its scrubbed output.
- **Evidence-Verifier** — for each PQQ item, **checks the contractor's claim against the
  supplied evidence** and records the verification status; **flags `[GAP]`** for every
  unverified or not-supplied claim (a self-asserted accreditation with no certificate is a
  `[GAP]`, never "met"). SCOPE-OUT: does not score or recommend (Scorer-&-Recommender owns
  it), does not draft the report.
- **Scorer-&-Recommender** — assigns the **risk tier** (`KB-DATA-CONTRACTOR-TIERS`), scores
  **only on verified evidence** against the tier's pass threshold, evaluates the proposed
  controls up the hierarchy via `controls` (T3 cannot pass on PPE/competence alone), and
  produces the **approve / conditional / reject** recommendation with conditions as dated
  `smart_actions` + a review date. SCOPE-OUT: does not re-verify evidence (Evidence-Verifier
  owns it) or scrub PII (De-identifier owns it).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (**Procurement HSE Lead**) before any output: the tier is
  set by the highest-risk activity, no score rests on a self-asserted claim, high-hazard work
  is not passed on PPE/competence alone, and every condition is owned + dated.
- **Critic/QA** (MANDATORY) — adversarial final pass: every score tied to a verified evidence
  item, every `[GAP]` blocks an unconditional pass, the hierarchy applied to the proposed
  controls, every condition owned + dated, ISO 45001 8.1.4 (and CDM reg. 8 / OSHA
  multi-employer where relevant) cited accurately, and **zero PII leak** (no named injured
  person, no < 5 cell, no re-id key in the output). PASS/FAIL.

A single low-risk (T1) contractor runs single-threaded — no subagents — but the
de-identification scrub, the evidence-verification step, and the Critic/QA + SME pass are
still made.

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
