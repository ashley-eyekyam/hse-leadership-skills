---
name: psychosocial-risk-assessment
description: Produces a consultant-grade psychosocial risk assessment for a named
  team, role, or function — identifying work-related psychosocial hazards and recommending
  work-design controls. Use this skill whenever a user asks to assess psychosocial
  risk, work-related stress, mental-health hazards, burnout, or workload/work-design
  risks, or to apply ISO 45003 or the HSE Management Standards. It assesses the hazard
  at source (work design, not the individual), prioritises organisational controls
  over individual resilience training, protects respondent confidentiality, and assigns
  owners and dates — emitted as a branded report. Decision-support only; a competent
  person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: psychosocial
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
  plugin: hse-operations
  bundled_in:
  - hse-healthcare
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Psychosocial Risk Assessment

A consultant-grade HSE skill that produces a defensible **psychosocial risk
assessment for a named team, role, or function**, grounded in **ISO 45003:2021**
and the **UK HSE Management Standards** (demands · control · support ·
relationships · role · change). It forces the single lever that separates a
defensible artifact from copy-paste paperwork: it **assesses the hazard at source —
work design, not the individual** — and drives **organisational work-design
controls above individual resilience training** (the psychosocial hierarchy of
controls). Each domain is rated from **at least two data sources** (never a single
anecdote), respondent **confidentiality is protected** (special-category health
data: any domain/team breakdown with **fewer than 5 respondents is suppressed**, no
finding is attributed to a nameable individual), and every recommended control
carries a named owner and a due date. Scoring uses the **deterministic A7
`risk_matrix`** 5×5 — the same matrix as the physical RA, for consistency — and
control ranking the A7 `controls` engine; both are script calls, never prose
judgement.

## When to use this skill

Use this skill when the user needs a psychosocial risk assessment for a **named
team, role, or function** — for example "assess psychosocial risk for the night-shift
contact-centre team", "run an ISO 45003 / HSE Management Standards assessment of
work-related stress on the maintenance crew after the restructure", or "where is the
burnout / workload / work-design risk in the claims department, and what do we
change?". Trigger phrases: *psychosocial risk, work-related stress, mental-health
hazard, burnout, workload/work-design risk, ISO 45003, HSE Management Standards,
psychosocial hazard assessment*. This skill assesses the **work** (demands, control,
support, relationships, role, change), **not** the worker — it never produces a
clinical or individual-diagnosis output and never names an individual as "the risk".
If the request is vague ("assess the whole company's stress"), the Workflow intake
below **refuses to proceed** until the named unit and **at least two data sources**
are captured — it will not build an assessment on a single anecdote.

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

This skill **always** grounds in the psychosocial standard and the six-domain framework,
then resolves the jurisdiction for the legal duty:

| Read on every run | File |
|---|---|
| ISO 45003:2021 — managing psychosocial risk (work-design controls, confidentiality, multi-source) | ../../knowledge-base/standards/iso-45003.md (KB-STD-ISO45003) |
| The six HSE Management Standards + indicative work-design controls per domain | ../../knowledge-base/prompt-snippets/hse-mgmt-standards.md (KB-SNIP-HSE-MGMT-STANDARDS) |
| Indicator-tool benchmark bands (band each domain; quote source+year) | ../../knowledge-base/data-points/psychosocial-indicators.md (KB-DATA-PSYCHOSOCIAL-INDICATORS) |
| ISO 45001 clause 6.1.2 hazard identification (hazard-at-source discipline) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001) |
| The hse-operations clause cross-walk (operations clause → owning skill) | ../../knowledge-base/prompt-snippets/ops-clause-map.md (KB-SNIP-OPS-CLAUSE-MAP) |

| Jurisdiction (Q5) | Read for the legal duty |
|---|---|
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (HSWA 1974 + MHSWR 1999 reg. 3 — psychosocial risk is in scope) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (NIOSH Total Worker Health framing — no single OSHA psychosocial standard) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (OSH Framework Directive 89/391/EEC) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (emerging OSH Code 2020 welfare provisions — defers to `hse-india`; **mandatory state detection**, never a national form number) |
| Unknown | Ask before citing any specific law — ISO 45003 + the HSE Management Standards still apply as the method |

Always apply `KB-SNIP-HOC` to every control: **work-design organisational controls
rank above individual resilience training**. For any benchmark band, resolve the ID in
`KB-DATA-PSYCHOSOCIAL-INDICATORS` and quote its `source`+`year` — never a remembered
cut-off. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question
table, the **mandatory India→state branch**, the echo-back, and the refuse-on-vague
anchors — lives in **`references/intake.md`**. Run it one question at a time, branch
on the answers, **echo the captured facts back before any analysis**, and **refuse to
proceed on a vague request**. The two hard refuse anchors:

1. **Q1 (unit in scope)** — a named team / role / function. **Refuse "the whole
   company" without a sampling plan**; the assessment must be anchored to a named unit.
2. **Q3 (data sources)** — **at least two** data sources (validated survey · focus
   groups · sickness-absence/turnover · grievance/incident data). **Never build the
   assessment on a single anecdote**, and never name an individual as "the risk".

Q2 selects the psychosocial **domains** (demands · control · support · relationships ·
role · change — branch per selected domain), Q4 captures known **triggers**
(restructuring, workload spikes, bereavement clusters), and Q5 the **jurisdiction**
(India → mandatory state branch).

### The psychosocial-RA method (ISO 45003 + the HSE Management Standards)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST** — survey/focus-group responses and
   sickness-absence are **special-category health data** (the `deid` block above + the
   reinforced `references/deid-checklist.md` + the De-identifier-runs-first
   orchestration rule). Suppress any domain/team breakdown with **<5 respondents**,
   apply secondary suppression, and scrub every nameable individual to a role label
   **before any analysis**. Everything downstream consumes only the scrubbed,
   aggregated text. **No individual is ever named as "the risk".**
2. **Confirm multi-source coverage (the refuse gate)** — verify **≥2 data sources**
   are present for the named unit. If only a single anecdote is available, **refuse to
   produce a rating** — record `[GAP]` and ask for corroborating data; do not invent.
3. **Hazard identification at source, by domain** — for each domain selected in Q2,
   identify the specific **work-design** hazard grounded in
   `KB-SNIP-HSE-MGMT-STANDARDS` (demands = workload/patterns/environment; control =
   decision latitude; support = manager/peer/resource support; relationships =
   conflict/bullying/harassment; role = clarity/conflict; change = how change is
   managed). Each finding names **what in the work design** is hazardous and **which
   role/group** is exposed — never an individual. Flag `[GAP]` where uncertain.
4. **Risk rating (deterministic, triangulated)** — band each domain's result against
   `KB-DATA-PSYCHOSOCIAL-INDICATORS` (quote `source`+`year`), triangulating across the
   ≥2 sources, then rate the domain hazard on the org 5×5 via
   `risk_matrix.load_matrix(config)` + `risk_matrix.score(likelihood, severity,
   matrix)` — the **same engine** as the physical RA. The band is the engine's, not
   prose.
5. **Work-design controls (the hierarchy lever)** — propose controls and **apply
   `KB-SNIP-HOC`**, then call `controls.rank_controls` + `controls.validate_treatment`.
   **Organisational work-design controls (achievable workloads, decision latitude,
   manager-support systems, anti-bullying enforcement, role clarity, early
   change-consultation) rank ABOVE individual resilience training.** Individual
   resilience / EAP referral is the **last** resort, never the primary control. An
   assessment whose only control is "resilience training" is a **defect the Critic/QA
   pass must catch** — this is the hard enforcement of the core value.
6. **Residual re-scoring** — re-score each domain *with the work-design controls
   applied* via `risk_matrix.score`, then `risk_matrix.residual_delta(initial,
   residual)`. A residual that stays High/Critical needs further work-design controls
   or escalation — not "offer counselling and proceed".
7. **SMART action plan (named owners + dates)** — for every control that is an action,
   produce a SMART action (specific, measurable, **assignable (named role-label
   owner)**, relevant, **time-bound (ISO due date)**) and call
   `smart_actions.validate_register`. No anonymous actions, no "ASAP".
8. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check before
   output: every selected domain rated from ≥2 sources; no <5-respondent cell
   published; no individual named as a hazard; work-design controls above individual
   resilience; every action owned + dated + domain-linked; ISO 45003 / HSE Management
   Standards cited accurately; de-id applied.
9. **Assemble the branded report** — build `report.json` (see
   `assets/psychosocial-risk-assessment-report.template.json`) and run the canonical
   `report-output` call below. The report carries an explicit **confidentiality
   statement** section.

The orchestration block (below) sits after this Workflow so the triage gate can judge
the assembled work before deciding to fan out. The **deterministic rating/ranking
steps (4, 5, 6 via `risk_matrix`/`controls`) are A7 script calls in every case** —
never a fan-out job.

> **ERP / BCP boundary note** — this skill assesses *work-related psychosocial risk*;
> it is not a clinical or individual mental-health assessment, and it does not replace
> occupational-health referral for an individual in distress (route that to a
> competent OH professional).

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
as the **sequential first gate** — and here it is **critical**: psychosocial survey,
focus-group and sickness-absence data is **special-category health data**, so the
De-identifier's scrub + small-cell suppression is the non-negotiable precondition of
every downstream job. **Rating and control-ranking are deterministic A7 script calls**
(`risk_matrix`, `controls`) at Workflow steps 4/5/6 — never an LLM fan-out job.
Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer), and is the
  **most critical job in this skill**. Before any analysis: scrub every nameable
  individual to a role/group label; treat all survey/focus-group/sickness-absence
  detail as **special-category health data**; **suppress any domain/team breakdown with
  fewer than 5 respondents** and apply **secondary suppression** so a suppressed cell
  cannot be back-calculated from totals; ensure **no finding is attributed to a
  nameable individual** ("no individual named as the hazard"). Apply
  `references/deid-checklist.md` (the reinforced <5 / special-category checklist) in
  full. Return the re-identification key SEPARATELY to the orchestrator — never to a
  sibling, never in the document. Every job below consumes only this scrubbed,
  aggregated output. SCOPE-OUT: does not rate domains (Domain-Analyst) or draft actions
  (Action-Planner).
- **Domain-Analyst** (per selected domain) — for each Q2 domain, identify the
  **work-design** hazard grounded in `KB-SNIP-HSE-MGMT-STANDARDS`, band the result
  against `KB-DATA-PSYCHOSOCIAL-INDICATORS` (quote source+year), **triangulate across
  ≥2 sources** (never a single anecdote), and propose **work-design controls ranked
  above individual resilience** via `KB-SNIP-HOC`. Consumes only the scrubbed output;
  names roles/groups, never individuals. SCOPE-OUT: the deterministic 5×5 score (the
  A7 `risk_matrix` call), the SMART action register (Action-Planner).
- **Action-Planner** — turn each accepted work-design control into a SMART action with
  a named **role-label** owner + an ISO due date + a measure + a domain link
  (`smart_actions.validate_register`). SCOPE-OUT: identifying hazards (Domain-Analyst),
  de-identification (De-identifier).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off
  in **`references/sme-review.md`** (Occupational Health / Psychosocial Specialist)
  before any output: hazard assessed **at source** (work design, not the individual),
  every domain rated from ≥2 sources, work-design controls above individual resilience,
  no individual named as a hazard, no <5-respondent cell published.
- **Critic/QA** (MANDATORY) — adversarial final pass: every selected domain rated via
  the A7 engine from ≥2 sources, work-design controls above individual resilience (no
  resilience-training-only treatment), every action owned + dated + domain-linked, ISO
  45003 / HSE Management Standards cited accurately, and **ZERO de-identification leak**
  (no residual identifier, no <5 cell, no individual named as a hazard, no re-id key in
  the output). PASS/FAIL.

A single small team with one data set may run single-threaded — no subagents — but the
De-identifier scrub + <5 suppression, the A7 rating/ranking calls, and the Critic/QA
pass are **still made**.

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
