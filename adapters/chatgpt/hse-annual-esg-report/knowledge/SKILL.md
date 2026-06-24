---
name: hse-annual-esg-report
description: Produces a consultant-grade, assurance-ready annual ESG occupational-health-&-safety
  disclosure for a named organisation and reporting period — a GRI 403 / SASB / ESRS
  S1 OH&S report with defined boundaries, denominators, and no back-calculable small
  cell. Use this skill whenever a user asks to build or review an annual ESG / sustainability
  OH&S disclosure, a GRI 403 health-and-safety report, an ESRS S1 own-workforce safety
  section, a SASB workforce-health-and-safety metric set, or a board-facing annual
  safety-performance disclosure. It reuses the GRI 403 / SASB / ESRS S1 disclosure
  crosswalk, applies the ISAE 3000 / AA1000AS assurance method (level, boundary, data-quality,
  materiality), validates every lagging rate to a standard definition and denominator,
  and applies the strictest publication de-identification tier — mandatory <5 small-cell
  plus secondary suppression so no suppressed cell can be back-calculated from a total.
  Decision-support only; a competent person must review before publication.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: esg
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

# HSE Annual ESG Report

A consultant-grade HSE skill that produces a defensible, **assurance-ready annual ESG
occupational-health-&-safety disclosure** for a **named organisation and reporting
period** — a **GRI 403 / SASB / ESRS S1** OH&S report fit for external publication. It
forces the single lever that separates a defensible disclosure from copy-paste ESG
boilerplate: **every published figure carries its reporting boundary and a defined
denominator, and no small cell can be back-calculated from a published total.** The
disclosure crosswalk is **reused** from the shipped `KB-STD-ESG-GRI403` (it mints no
duplicate index); the **assurance method** (`KB-SNIP-ESG-ASSURANCE`) makes every figure
assurable — assurance level (limited/reasonable), reporting boundary (operational /
financial / equity, and **own-workforce vs non-employee/contractors** — ESRS S1 mandates
the split), per-metric data quality (definition + denominator + source + period +
completeness), and **double materiality**. Lagging injury / ill-health figures (TRIR,
LTIFR, DART, fatalities) are computed by the deterministic **`incident_rates`** engine to
standard definitions (anchors TRIR 2.07 / LTIFR 6.00) — never invented in prose. This is
the **strictest external-publication de-identification tier** in the bundle: aggregate
all, **mandatory `<5` small-cell suppression** on any injury/illness category (especially
fatalities/illness by site or demographic), and **secondary suppression** so a suppressed
cell cannot be reverse-engineered from a published total or the other cells. Because the
report is board-facing and publicly published, it is **decision-support that PRECEDES,
never replaces,** the assurance engagement and the competent-person review.

## When to use this skill

Use this skill when the user needs an **annual ESG / sustainability OH&S disclosure** for
a named organisation and reporting period — for example "build our FY2025 GRI 403 health-
and-safety disclosure", "draft the ESRS S1 own-workforce safety section for the annual
report", "assemble the SASB workforce health-and-safety metrics", or "produce the board-
facing annual safety-performance disclosure for publication". Trigger phrases: *annual ESG
report, ESG / sustainability OH&S disclosure, GRI 403 report, ESRS S1 own-workforce safety,
SASB workforce health & safety, annual safety-performance disclosure, assurance-ready
safety figures*. This skill produces an **externally-publishable** disclosure, so the de-id
tier is the strictest in the bundle and **no figure is published without its denominator
and reporting boundary**. If the request is vague ("write our ESG safety section"), the
Workflow intake below **refuses to proceed** until the organisation, the reporting period,
the boundary, the workforce split, the assurance-level intent, and the disclosures in scope
are captured — and it **refuses any rate with no denominator/definition** and any "GRI 403"
claim that omits a required 403 disclosure. It never reads as a final assured or legal
document.

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

<!-- The ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows this skill serves;
     rule-9 checks every path/ID resolves against the KB registries. -->

This skill **always** grounds in the reused disclosure crosswalk, the assurance method,
and the leadership clause-map, then resolves the jurisdiction only for the publication
framework in force:

| Read on every run | File |
|---|---|
| **REUSED (D-02)** — GRI 403 / SASB / ESRS S1 OH&S disclosure→artifact crosswalk; select each required disclosure here. **Do NOT mint a duplicate disclosure index.** | ../../knowledge-base/standards/esg-gri-403.md (KB-STD-ESG-GRI403) |
| The assurance method — level · reporting boundary · per-metric data quality · double materiality · strictest-tier `<5` + secondary suppression | ../../knowledge-base/prompt-snippets/esg-assurance.md (KB-SNIP-ESG-ASSURANCE) |
| ISO 45001 leadership clause-map — this skill is **clause 9.1** (monitoring/measurement/performance evaluation = the disclosed figures) | ../../knowledge-base/prompt-snippets/leadership-clause-map.md (KB-SNIP-LEADERSHIP-CLAUSE-MAP) |
| Lagging-rate definitions/benchmarks (TRIR / DART / LTIFR) — every disclosed rate is computed by `incident_rates` to these definitions; quote `source`+`year` | ../../knowledge-base/data-points/incident-rates-benchmarks.md (KB-DATA-TRIR-BENCHMARKS) |
| ISO 45001:2018 — management-system structure for the disclosed governance/process disclosures (GRI 403-1…403-7) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001) |

| Jurisdiction / framework (Q-boundary) | Read for the publication framework |
|---|---|
| EU / CSRD | ../../knowledge-base/regulatory/eu-osh.md (ESRS S1 own-workforce H&S under the CSRD; resolve the assurance-level expectation in `KB-SNIP-ESG-ASSURANCE` at use time) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (UK reporting context; framework selection per the organisation's reporting standard) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (SASB workforce-H&S metrics; OSHA recordkeeping definitions underpin the lagging figures) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (defers to `hse-india` for any statutory return; **mandatory state detection**, never a national form number) |
| Unknown | Ask which reporting framework (GRI / SASB / ESRS S1) is in force before citing any specific disclosure code |

For the reused crosswalk, resolve each required disclosure ID in `KB-STD-ESG-GRI403` and
report it once to the right framework code; record any disclosure with no data as `[GAP]`,
never fabricated. For every rate, resolve `KB-DATA-TRIR-BENCHMARKS` and quote its
`source`+`year`. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table, the
echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run it
one question at a time, branch on the answers, **echo the captured facts back before any
analysis**, and **refuse to proceed on a vague request**. The hard refuse anchors:

1. **Organisation + reporting period** — a named entity and a defined period. Refuse "our
   ESG section" without the named org and period.
2. **Reporting boundary + workforce split** — operational / financial control / equity-share,
   AND **own-workforce vs non-employee/contractors** (ESRS S1 mandates the split). A figure
   with no stated boundary is **not assurable** — refuse it.
3. **Defined denominator per metric** — every disclosed rate needs definition + denominator +
   source + period + completeness. **A rate with no denominator/definition is refused** (no
   figure published without its basis).
4. **Disclosures in scope** — the GRI 403 / SASB / ESRS S1 disclosures claimed. A **"GRI 403"
   claim missing a required 403 disclosure is a `regulatory_citation_accuracy` hard-fail.**

The intake also captures the **assurance-level intent** (limited vs reasonable) and the
**materiality basis** (double materiality — impact + financial).

### The annual-ESG-disclosure method (reuse GRI403 + assurance method)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST (strictest tier)** — injury/illness figures, especially
   fatalities and ill-health by site or demographic, are highest-sensitivity and **publicly
   published**. Apply the `deid` block above + the reinforced `references/deid-checklist.md`
   + the De-identifier-runs-first orchestration rule: aggregate all; **suppress any
   injury/illness category with `<5` individuals**; apply **secondary suppression** so a
   suppressed cell cannot be back-calculated from a published total or the remaining cells;
   define denominators/boundaries so totals can't be reverse-engineered. Everything
   downstream consumes only the scrubbed, aggregated, suppression-safe figures.
2. **Select disclosures from the reused crosswalk** — resolve each required OH&S disclosure
   in `KB-STD-ESG-GRI403` (GRI 403-1…403-10 ↔ SASB ↔ ESRS S1). Do **not** author a duplicate
   index. A "GRI 403" claim must carry every required 403 disclosure or be flagged
   `[GAP]` — a missing required disclosure is a citation-accuracy hard-fail.
3. **Define boundary + workforce split for every figure** (`KB-SNIP-ESG-ASSURANCE` §2) —
   each figure states its consolidation boundary (operational/financial/equity) and the
   own-workforce vs non-employee split. A figure with no boundary is not assurable.
4. **Validate every lagging rate deterministically** — compute TRIR / DART / LTIFR /
   fatality rate via the `incident_rates` engine from the period's recordable counts and
   hours worked, to the standard definitions in `KB-DATA-TRIR-BENCHMARKS` (anchors TRIR 2.07
   / LTIFR 6.00). The rate and its denominator are the engine's, never prose. A rate with no
   denominator/definition is **refused**, not estimated.
5. **Apply the data-quality criteria** (`KB-SNIP-ESG-ASSURANCE` §3) — every published metric
   carries definition + denominator + source + period + completeness/accuracy note. No
   figure is published without its basis.
6. **State assurance level + materiality** — record the intended assurance level (limited /
   reasonable) so the evidence rigour matches it, and state the **double-materiality** basis
   for reporting own-workforce H&S.
7. **Narrate improvement commitments via the hierarchy of controls** — where the disclosure
   describes the OH&S programme/response, apply `KB-SNIP-HOC` (higher-order controls above
   PPE/admin) and assign owned + dated commitments via `smart_actions` — never a published
   "we will be more careful".
8. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check before output:
   every figure boundary-stated + denominator-defined; no `<5` cell published; secondary
   suppression applied (no back-calculable cell); every claimed GRI 403 disclosure present
   or `[GAP]`; lagging rates from `incident_rates`; assurance level + materiality stated;
   de-id applied; **no competent-person sign-off or assured-approval claimed** (decision-support / pre-assurance only).
9. **Assemble the branded report** — build `report.json` (see `assets/report.json`) and run
   the canonical `report-output` call below. The report carries an explicit
   **de-id/aggregation notice** and a **decision-support / pre-assurance** disclaimer.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled disclosure before deciding to fan out. The **deterministic rate validation (step
4 via `incident_rates`) is an A7 script call in every case** — never a fan-out job.

> **Boundary note** — this skill produces a *disclosure draft for assurance and
> publication*; it is **not** the assurance engagement itself and does not constitute a
> reasonable/limited assurance opinion. Route the assurance opinion to a competent ESG /
> Sustainability Assurance Specialist and the sign-off to a competent person.

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

This is the **moderate roster** (A6 "moderate = 2–3 fan-out") with the De-identifier as
the **sequential first gate** — and here it is **critical**: this disclosure is **externally
published**, so the De-identifier's aggregate-all + `<5` + **secondary** suppression is the
non-negotiable precondition of every downstream job. **Lagging-rate validation is a
deterministic A7 script call** (`incident_rates`) at Workflow step 4 — never an LLM fan-out
job. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer), and is the
  **most critical job in this skill**. Before any analysis: aggregate all injury/illness
  figures; treat fatalities/illness by site or demographic as highest-sensitivity;
  **suppress any category with fewer than 5 individuals** and apply **secondary suppression**
  so a suppressed cell cannot be back-calculated from a published total or the other cells;
  define denominators/boundaries so totals can't be reverse-engineered to a small cell.
  Return the re-identification mapping SEPARATELY to the orchestrator — never to a sibling,
  never in the document. Every job below consumes only this scrubbed, aggregated,
  suppression-safe output. SCOPE-OUT: does not select disclosures (Disclosure-Mapper) or
  compute rates (Figure-Validator).
- **Disclosure-Mapper** — select each required OH&S disclosure from the **reused**
  `KB-STD-ESG-GRI403` (GRI 403-1…403-10 ↔ SASB ↔ ESRS S1), define each figure's reporting
  boundary + own-workforce/non-employee split (`KB-SNIP-ESG-ASSURANCE`), and flag any
  claimed-but-absent 403 disclosure as `[GAP]`. Does **not** author a duplicate index.
  SCOPE-OUT: rate computation (Figure-Validator), de-identification (De-identifier).
- **Figure-Validator** — compute/validate every lagging rate (TRIR / DART / LTIFR /
  fatality rate) via `incident_rates` to the `KB-DATA-TRIR-BENCHMARKS` definitions
  (anchors TRIR 2.07 / LTIFR 6.00); attach definition + denominator + source + period +
  completeness to each figure; refuse any rate with no denominator. SCOPE-OUT: selecting
  disclosures (Disclosure-Mapper), de-identification (De-identifier).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (ESG / Sustainability Assurance Specialist) before any
  output: every figure boundary-stated + denominator-defined, no `<5` cell published,
  secondary suppression applied (no back-calculable cell), every claimed GRI 403 disclosure
  present or `[GAP]`, assurance level + materiality stated — and the disclosure never reads
  as a final assured/legal document.
- **Critic/QA** (MANDATORY) — adversarial final pass: every figure boundary-stated +
  denominator-defined, lagging rates from `incident_rates`, every claimed 403 disclosure
  present, assurance level + materiality stated, and **ZERO de-identification leak** (no
  residual identifier, no `<5` cell, **no back-calculable suppressed cell**, no re-id
  mapping in the output). PASS/FAIL.

A single-entity disclosure with one figure set may run single-threaded — no subagents — but
the De-identifier aggregate-all + `<5` + secondary suppression, the A7 `incident_rates`
validation, and the Critic/QA pass are **still made**.

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
