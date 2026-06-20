---
name: board-safety-report
description: 'Produces an executive, board-level HSE safety report: synthesizes a
  reporting period''s leading and lagging safety indicators (TRIR / LTIFR / DART,
  training and audit closure), key events, trends, and benchmark comparisons into
  a board-ready narrative — what changed, why it matters, and what leadership must
  decide. Use this skill whenever a user asks to write a board safety report, an executive
  safety report or summary, a leadership or board HSE performance report, a quarterly
  or annual safety performance review, or a management-review safety input. Grounds
  the report in ISO 45001 clause 9.1 (monitoring & performance evaluation) and 9.3
  (management review), de-identifies and aggregates incident detail so no individual
  is identifiable, compares performance to a benchmark with its source and year, and
  frames strategic decisions for the board — emitting a branded report. It is an executive
  narrative, not a data dump. Decision-support only; a competent person must review
  the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: governance
  tier: 1
  audience:
  - E
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Board Safety Report (Executive HSE Narrative)

Synthesizes a reporting period's HSE performance into a **board-level safety
narrative** — an exec-grade, branded document grounded in ISO 45001 clause **9.1**
(monitoring & performance evaluation) and **9.3** (management review). The one lever
to internalise is **exec narrative, not data dump**: every figure it surfaces is
paired with *what it means* (the trend vs the prior period; the position vs a
benchmark *with its source + year*) and *what leadership must decide*. A board paper
that is a wall of TRIR/LTIFR tables with no story, no "so what," and no decision ask
has failed its only job — that is the failure mode this skill exists to kill. It
de-identifies **and aggregates** every incident detail so no individual event or
person is identifiable, surfaces a HiPo/SIF lens (high-potential incidents and
serious-injury/fatality precursors, *interpreted* not merely listed), and emits a
branded board report. This is the pack's only executive-audience skill.

## When to use this skill

Use this skill whenever a user needs an executive, board-facing HSE narrative:
preparing a **board or executive-committee safety paper**, a **quarterly or annual
HSE performance report**, a **leadership / board HSE performance review**, or a
**management-review safety input** (ISO 45001 9.3). Trigger phrases: *board safety
report, executive safety report / summary, leadership or board HSE performance
report, quarterly / annual safety performance review, management-review safety
input, leading & lagging indicators, TRIR / LTIFR / DART, benchmark comparison*. If
the request is vague, the Workflow intake below **refuses to proceed** until the
period, audience, and available metrics are elicited.

**When NOT to use this skill** (compose, don't overlap): to *compute or dashboard*
the rates themselves use `incident-rate-calculator` (B9 *consumes* a computed rate as
context and wraps it in a narrative); to *investigate* a single event use
`incident-investigation` (B9 *summarizes* its de-identified, aggregated outputs at
board altitude, it never re-investigates). B9 produces the **board narrative around**
the numbers — not the calculation, not the investigation.

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

<!-- B9 is a NARRATIVE skill, not a statutory-notice skill: the jurisdiction rows are
     CONTEXT (only consulted when a counted figure — an OSHA-recordable, a RIDDOR-
     reportable — needs its definitional source). The load-bearing rows are the
     STANDARD (ISO 45001 9.1/9.3) and the BENCHMARK (KB-DATA-TRIR-BENCHMARKS). -->

| Jurisdiction / scope | Read |
|---|---|
| Standard (always) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — clause 9.1 monitoring & performance evaluation + 9.3 management review) |
| Performance benchmark | ../../knowledge-base/data-points/incident-rates-benchmarks.md (KB-DATA-TRIR-BENCHMARKS — quote body + year + sector, never a bare number) |
| Environmental (optional, only if env metrics supplied) | ../../knowledge-base/standards/iso-14001.md (KB-STD-ISO14001 — clause 9.1.2 evaluation of compliance; a single optional env-performance line, NOT a full ESG branch) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (context only — resolve the state via in-state-forms.md if a statutory figure is cited; mandatory state detection) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (context for any RIDDOR-counted figures) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (context for OSHA-recordable counts feeding TRIR/DART) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` clause **9.1** (the indicators) +
**9.3** (the management-review structure the board narrative serves), reads every
benchmark from `KB-DATA-TRIR-BENCHMARKS` **with its source + year**, and instantiates
the `KB-SNIP-INTAKE` pattern in its intake. `KB-STD-ISO14001` 9.1.2 is consulted
**only** for the optional environmental-performance line when env metrics are
supplied. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run first, one question at a time)

The full typed, branched B9 intake — the `intake-coverage` manifest, the question table
(reporting period · audience body · safety data/metrics + **hours-gate** · **key events
[IMMEDIATE de-id + aggregation]** · **HiPo/SIF [D-01 lens]** · strategic priorities ·
accountability · prior-period comparison · benchmark · optional env metrics · jurisdiction →
**India→state**), the **hours+counts rates-guard**, the **HiPo/SIF interpret-not-list lens**,
the optional **ISO 14001 9.1.2 env-performance line** (D-02), the **mandatory India→state
branch** (Q10 = India → Q10a), the **de-identified + aggregated echo-back**, and the
refuse-on-vague anchors — lives in **`references/intake.md`**. Run it one question at a time,
branch on the answers, and **never proceed on a vague period or audience** (record
`[ASSUMPTION]` / `[GAP]` — never invent a figure or a benchmark). **Q4 (key events) and Q5
(HiPo/SIF) are de-identified AND aggregated in Workflow step 1 *before* any analysis**, so the
echo-back in `references/intake.md` shows aggregated facts only — no individual incident, no
named site (ELI-LOCATION is omitted by design), no `<5` cell.

### The synthesis-to-narrative method (the core lever: insight, not data dump)

Full method + the leading/lagging-indicator taxonomy + the HiPo/SIF methodology note:
`references/METHODOLOGY.md`. Run these steps in order:

1. **De-identify AND aggregate the inputs FIRST** (the `deid` block above is a
   sequential dependency, with B9's **aggregation twist**). Run the De-identifier over
   every intake input — especially the free-text **key events** (Q4) and **HiPo/SIF**
   (Q5) fields: pseudonymize to role labels, and **aggregate** any individual incident
   / injury / illness so **no single event, person, or <5 cell is identifiable**
   (the board-report leak vector is re-identification via a vivid single-incident
   anecdote — a name is not required to re-identify). The re-identification key is
   returned **separately** to the user, never in the report or any subagent prompt.
   Every step below consumes only scrubbed, aggregated text.
2. **Assemble the leading & lagging indicators.**
   - **Lagging** (outcome) — recordable / lost-time / DART cases, fatalities,
     environmental events. Compute the rates deterministically via
     `incident_rates.compute_all(counts, hours_worked, period)` — **GUARDED: only if
     Q3 captured hours + counts** (the engine raises on zero/negative hours, so the
     call sits inside a guard). If hours are absent, take a **pre-computed rate** as an
     input (e.g. from `incident-rate-calculator`) or flag `[GAP]` — **never fabricate a
     denominator.**
   - **Leading** (predictive) — training completion %, audit/inspection closure,
     near-miss reporting rate, action on-time closure, leadership tours. User-supplied
     figures (no A7 engine — synthesized, not computed).
3. **Identify trends & insights (vs prior period, vs benchmark WITH source + year).**
   For each indicator compute the movement vs the prior period (Q7) and the position
   vs the benchmark via `incident_rates.benchmark_delta(rate, industry_rate)`, reading
   `industry_rate` from `KB-DATA-TRIR-BENCHMARKS` (or the user-supplied figure)
   **with its source + year**. Flag `[GAP]` where prior-period or benchmark data is
   absent — never invent a comparator. This step produces *readings* ("LTIFR fell 18%
   vs FY24 and now sits below the [body, year] sector average"), not bare numbers.
4. **Draft the executive narrative — THE core lever.** Turn the readings into the
   board narrative: **what changed** (the trend story), **why it matters** (the
   risk/exposure/cultural implication), and **what leadership must decide** (the
   explicit asks). Surface the **HiPo/SIF lens explicitly and INTERPRETED** (D-01):
   what the high-potential incidents and SIF precursors *reveal* about exposure and
   where the next serious event is most likely — not merely a list of events
   (methodology note in `references/METHODOLOGY.md`). Every figure in the narrative
   carries its meaning; the indicator tables are *supporting evidence behind* the
   narrative, never the narrative itself.
5. **Strategic actions / asks.** Governance-level decisions, resource asks, and
   direction the board is being asked to set (resource allocation, policy direction,
   accountability) with an owner where one exists — **not** operational task lists
   (those live in incident-investigation / capa-manager CAPAs). Tie to ISO 45001 9.3
   management-review outputs.
6. **Outlook.** Emerging risks, the next-period focus, and the trajectory the
   indicators imply. *(Optional ISO 14001 9.1.2 environmental-performance line here —
   D-02 — ONLY when Q9 supplied env metrics; a single line, never a full ESG branch.)*
7. **Validate against `references/QUALITY_CHECKLIST.md`** — de-id + aggregation clean
   (no individual incident/person/<5 cell identifiable, no key in output); every
   figure carries a reading (no naked table); every benchmark carries source + year;
   the report leads with insight + decisions, not data; HiPo/SIF surfaced and
   interpreted; trends vs the stated prior period; every claim traces to an input or
   is flagged `[ASSUMPTION]`/`[GAP]`; grounded in ISO 45001 9.1/9.3.
8. **Assemble the branded board report** — build `report.json`
   (`assets/board-report.template.json` shape) and run the `report-output` call; the
   A4 engine produces the exec-grade docx + pdf and auto-stamps the limitations/de-id
   notice.

The **deterministic rate computation (step 2 via `incident_rates`) is an A7 script
call in every case — never a fan-out subagent's judgement.**

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

### Step 4 — Critic / QA (MANDATORY — this is regulatory/safety output)
Spawn ONE Critic: give it the draft + the inputs + the output contract. It finds errors,
unsupported claims, missed regulatory triggers, lower-order-only controls, and any
de-identification leak. Fix everything it raises before delivery.

> Single-threaded fallback: if your host has no subagent capability, execute each job
> sequentially in THIS context — run the de-identification scrub first, keep the scope
> discipline, and still perform the required Critic/QA pass before delivery.
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed). B9 ships the A6 MODERATE (2-3) roster: the
     De-identifier is the sequential first gate (with B9's aggregation twist), the
     2 fan-out jobs are the Data-Synthesizer + the Narrative-Drafter, Critic/QA is
     mandatory. There is NO rate-computation subagent — the rate maths is the
     deterministic incident_rates A7 call, never LLM fan-out work. -->

For a full board report the triage gate fans out to the moderate roster:

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all
  PII/health detail AND **aggregate** the period's key events + HiPo/SIF (Q4/Q5) so no
  individual incident, injured party, or small (<5) cell is identifiable, before any
  analysis. Returns the re-identification key SEPARATELY. Every job below consumes only
  its scrubbed, aggregated output.
- **Data-Synthesizer** — assemble the period's leading & lagging indicators from the
  scrubbed inputs; call `incident_rates.compute_all` for the lagging rates **IF hours +
  counts present** (else take the rate as a pre-computed input or flag `[GAP]` — never
  fabricate a denominator); compute the trend delta vs the prior period and the
  benchmark delta (`incident_rates.benchmark_delta`) against `KB-DATA-TRIR-BENCHMARKS`,
  quoting every benchmark's **source + year**. SCOPE-OUT: does not write the board
  narrative (the Narrative-Drafter owns it). *(Rate maths is the A7 `incident_rates`
  script, NOT this subagent's judgement.)*
- **Narrative-Drafter** — turn the Synthesizer's figures + deltas into the board
  narrative: what changed, why it matters, what leadership must decide; the **HiPo/SIF
  lens interpreted** (D-01); the strategic actions/asks; the outlook. Insight, not
  tables. SCOPE-OUT: does **not** compute or alter the figures (consumes the
  Synthesizer's numbers verbatim) — it must not invent or "round" a metric.
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (board-level HSE governance advisor + safety-performance
  statistician) before any output: does the paper let a board GOVERN (decision-grade
  narrative, leading/lagging balance, explicit asks — not a wall of numbers), are the
  indicators read HONESTLY (no false assurance from a falling lagging rate while HiPo/SIF
  precursors say otherwise), and is every single-incident anecdote aggregated away? FLAG-only;
  does not block on a flag.
- **Critic/QA** (MANDATORY) — adversarial read-only review: is this INSIGHT, not a data
  dump (every figure carries a reading; the report leads with the narrative +
  decisions)? Is the HiPo/SIF lens present AND interpreted, not merely listed? Does
  every benchmark carry source + year? Are trends computed against the stated prior
  period? Is the aggregation airtight (no individual incident or <5 cell identifiable,
  no re-id key)? Are figures consistent with the Synthesizer's deterministic output
  (the Drafter changed nothing)? PASS/FAIL.

That is **2 fan-out LLM jobs** (Data-Synthesizer + Narrative-Drafter) behind the
sequential De-identifier gate, plus the mandatory Critic/QA — squarely A6's "moderate
= 2–3". **Single-thread fallback:** on a host with no subagent capability the same jobs
run sequentially in one context — the de-id/aggregation scrub first, the
`incident_rates` call still made deterministically, the synthesis-then-narrative scope
discipline kept, the Critic/QA pass still performed.

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
