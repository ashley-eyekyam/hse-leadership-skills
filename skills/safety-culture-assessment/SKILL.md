---
name: safety-culture-assessment
description: Produces a consultant-grade safety-culture assessment for a named organisation,
  site, or business unit — designing a survey, mapping results to a maturity model
  (DuPont Bradley / Hudson Hearts-and-Minds / Westrum) or the Schein three-levels
  diagnostic lens, triangulating at least two data sources, and emitting a defensible
  advancement roadmap. Use this skill whenever a user asks to assess, diagnose, benchmark,
  or measure safety culture or safety climate, run a culture-maturity assessment,
  design a culture survey, or place an organisation on a Bradley/Hudson/Westrum ladder
  or against Schein's three levels of culture. It refuses to produce a maturity rating
  from a single survey (requiring a model, a named population, and >=2 triangulated
  data sources), suppresses any sub-5 respondent cohort to protect confidentiality,
  drives a systemic advancement roadmap with named owners and dates, and emits a branded
  report. Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: culture
  tier: 2
  audience:
  - M
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-leadership
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Safety Culture Assessment

A consultant-grade HSE skill that produces a defensible **safety-culture assessment
for a named organisation, site, or business unit**. It designs (or interprets) a
culture survey, maps the result to a recognised **maturity model** — DuPont **Bradley**
Curve, **Hudson** / Parker "Hearts & Minds" ladder, or **Westrum** typology — or, where
the user wants a *diagnosis* rather than a *rating*, applies the **Schein three-levels
lens** (artifacts · espoused beliefs & values · basic underlying assumptions), and
emits a systemic **advancement roadmap** with named owners and dates.

It forces the single lever that separates a defensible artifact from copy-paste
paperwork: it **refuses to produce a maturity rating from a single survey** — a rating
requires a named model, a **named population**, and **at least two triangulated data
sources** (survey · observation/walk data · records). Respondent **confidentiality is
protected**: any cohort/sub-group breakdown with **fewer than 5 respondents is
suppressed** (with secondary suppression), no finding is attributed to a nameable
individual, and no verbatim respondent quote is reproduced in a way that identifies the
speaker. Improvement actions are ranked through the full **hierarchy of controls** (a
systemic work-design fix, never "tell people to care more") with a named owner and an
ISO due date.

## When to use this skill

Use this skill when the user needs a **safety-culture assessment for a named
organisation, site, or unit** — for example "assess the safety culture at the
Northgate distribution centre", "where are we on the Bradley Curve / Hudson ladder and
how do we advance?", "design a safety-culture survey for the maintenance division", or
"run a Schein three-levels diagnosis of why our 'safety first' value isn't enacted on
the floor". Trigger phrases: *safety culture, safety climate, culture maturity, culture
survey, Bradley Curve, Hudson / Hearts & Minds ladder, Westrum typology, Schein three
levels, espoused-vs-enacted gap, culture advancement roadmap*.

**This skill assesses the organisation's culture, not an individual.** It is **distinct
from its siblings** — `bbs-program-designer` (designs a behaviour-observation programme),
`safety-walk-gemba` (structures a single leadership walk), and
`leading-lagging-kpi-framework` (designs the balanced KPI set). Intake-Q1 disambiguates
which of these the user actually needs. If the request is vague — "rate our culture" off
one pulse survey — the Workflow intake below **refuses to produce a rating** until a
model, a named population, and **≥2 data sources** are captured; it will not place an
organisation on a ladder from a single survey.

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
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

This skill **always** grounds in the culture-model library, the maturity-band data, the
leading-indicator catalogue, and the ISO 45001 leadership clause map — then resolves the
jurisdiction only for the underlying legal duty (culture assessment is method-led, not
form-led).

| Read on every run | File |
|---|---|
| The four culture lenses — Bradley / Hudson / Westrum maturity ladders **+ the Schein three-levels diagnostic lens** (descriptors + diagnostic probes; Schein is selectable and combinable, not a 4th ladder) | ../../knowledge-base/prompt-snippets/culture-models.md (KB-SNIP-CULTURE-MODELS) |
| Maturity-band descriptors for the ladders **+ the Schein espoused-vs-enacted GAP rubric** (band each model; standalone Schein = a diagnosis, not a rating; quote source+year) | ../../knowledge-base/data-points/culture-maturity.md (KB-DATA-CULTURE-MATURITY) |
| The curated leading/lagging indicator catalogue (so the advancement roadmap is tracked to real leading indicators, not vibes) | ../../knowledge-base/data-points/leading-indicators.md (KB-DATA-LEADING-INDICATORS) |
| ISO 45001 leadership clause cross-walk (5.1 leadership & commitment · 5.4 consultation & participation — the clauses this assessment evidences) | ../../knowledge-base/prompt-snippets/leadership-clause-map.md (KB-SNIP-LEADERSHIP-CLAUSE-MAP) |
| ISO 45001:2018 clause 5.1 / 5.4 (the leadership & worker-participation duties a culture assessment evidences) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001) |

| Jurisdiction | Read for the legal duty |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state — **mandatory state detection**; defers to `hse-india`, never a national form number) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (HSWA 1974 — leadership/worker-participation duties) |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (OSH Framework Directive 89/391/EEC — worker consultation) |
| Unknown | Ask before citing any specific law — the culture models + ISO 45001 5.1/5.4 still apply as the method |

Always apply `KB-SNIP-HOC` to every advancement action: a culture gap is closed by a
**systemic work-design / leadership-system fix**, never by "tell workers to care more".
For any maturity band, resolve the model in `KB-DATA-CULTURE-MATURITY` and quote its
`source`+`year` — never a remembered cut-off. The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table,
the **sibling-disambiguation Q1**, the **model-selection Q2** (Bradley · Hudson ·
Westrum · **Schein three-levels** · combined), the **mandatory India→state branch**, the
echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run it
one question at a time, branch on the answers, **echo the captured facts back before any
analysis**, and **refuse to proceed on a vague request**. The hard refuse anchors:

1. **Q1 (unit + sibling disambiguation)** — a **named organisation / site / business
   unit**, and a confirmation that the user wants a *culture assessment* (not a BBS
   programme → `bbs-program-designer`, a single leadership walk → `safety-walk-gemba`, or
   a KPI set → `leading-lagging-kpi-framework`). **Refuse "the whole company" without a
   named scope or sampling plan.**
2. **Q3 (data sources — the triangulation gate)** — **at least two** data sources
   (validated culture survey · leadership-walk/observation data · records such as
   reporting/participation/turnover). **Never produce a maturity rating on a single
   survey or a single source.** A standalone Schein output is allowed as a *diagnosis*
   (named gaps) but still requires the named population and ≥2 sources to be defensible.

Q2 selects the **model/lens** (and whether Schein is combined with a ladder as a
triangulation lens), Q4 captures the **confidentiality threshold** (default ≥5
respondents per published cohort cell), and Q5 the **jurisdiction** (India → mandatory
state branch).

### The culture-assessment method (maturity models + the Schein lens)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST** — survey responses, focus-group/walk notes, and any
   records are **sensitive personnel data** (the `deid` block above + the reinforced
   `references/deid-checklist.md` + the De-identifier-runs-first orchestration rule).
   **Suppress any cohort/sub-group breakdown with <5 respondents**, apply secondary
   suppression, scrub every nameable individual to a role/group label, and **never
   reproduce a verbatim respondent quote** that identifies the speaker in a small group.
   Everything downstream consumes only the scrubbed, aggregated text.
2. **Confirm model + named population + ≥2 sources (the refuse gate)** — verify a named
   model/lens (Q2), a named population (Q1), and **≥2 triangulated data sources** (Q3)
   are present. If only a single survey is available, **refuse to produce a maturity
   rating** — record `[GAP]`, ask for corroborating observation/records, and offer a
   Schein *diagnosis* of named gaps instead of a rating. Do not invent a band.
3. **Map to the model (rating) or run the Schein lens (diagnosis)** — for a ladder model
   (Bradley/Hudson/Westrum), band the triangulated evidence against
   `KB-DATA-CULTURE-MATURITY` (quote `source`+`year`) using the descriptors/probes in
   `KB-SNIP-CULTURE-MODELS`. For **Schein** (selectable as the primary lens, or combinable
   with a ladder as a triangulation lens), apply the **espoused-vs-enacted GAP rubric**:
   compare the **espoused values** (level 2 — slogans, policy, "safety first") against the
   **underlying assumption enacted** in artifacts and behaviour (levels 1 & 3 — what
   actually wins when schedule and safety collide). A wide gap is a named diagnostic
   finding, **not** a maturity band — standalone Schein produces a *three-levels
   diagnosis*, never a ladder rating.
4. **Locate the systemic drivers** — for each band/gap, name **what in the leadership
   system / work design** holds the culture where it is (ownership of safety, how
   information flows — Westrum, how bad news is treated, consultation under ISO 45001 5.4).
   Attribute to roles/groups and systems, **never to a nameable individual**. Flag `[GAP]`
   where the evidence is thin.
5. **Advancement controls (the hierarchy lever)** — propose the moves that advance the
   culture and **apply `KB-SNIP-HOC`**, then call `controls.rank_controls` +
   `controls.validate_treatment`. **Systemic leadership-system / work-design changes**
   (visible felt-leadership cadence, fixing the consequence system so the safe choice is
   the easy choice, genuine worker consultation, closing the espoused-vs-enacted gap) rank
   **above** "awareness campaigns" or "tell people to care more". A roadmap whose only
   move is a poster campaign is a **defect the Critic/QA + SME pass must catch**.
6. **SMART advancement roadmap (named owners + dates + leading indicators)** — for every
   advancement move produce a SMART action (specific, measurable, **assignable (named
   role-label owner)**, relevant, **time-bound (ISO due date)**) via
   `smart_actions.validate_register`, and tie progress to a **leading indicator** drawn
   from `KB-DATA-LEADING-INDICATORS` (e.g. consultation-meeting cadence, leadership-walk
   commitment closure-rate, near-miss reporting rate) — so advancement is *measured*, not
   asserted. No anonymous actions, no "ASAP".
7. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check before output:
   a named model/lens; a named population; **≥2 triangulated sources** for any rating; no
   <5-cohort cell published; no individual named; no verbatim identifying quote; every
   advancement action owned + dated + tied to a leading indicator; Schein treated as a
   gap diagnosis not a band; the culture models cited as method (not law).
8. **Assemble the branded report** — build `report.json` (see `assets/report.json`) and
   run the canonical `report-output` call below. The report carries an explicit
   **confidentiality statement** section and a **sibling cross-reference** one-liner (see
   the roster note) so the reader knows which companion skill operationalises each move.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **control-ranking / action-register steps
(5, 6 via `controls`/`smart_actions`) are A7 script calls** — never a fan-out job.

> **Sibling cross-reference (emit in the output):** "This is a culture *diagnosis*; to
> operationalise it use **`bbs-program-designer`** (observation programme),
> **`safety-walk-gemba`** (leadership walks), and **`leading-lagging-kpi-framework`** (the
> balanced KPI set that tracks advancement)." — companion skills, D-03 / CONV-12.

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

This is the **moderate roster** (A6 "moderate = 2–3 fan-out") with the **De-identifier
as the sequential first gate** — critical here because culture-survey responses,
focus-group/walk notes and verbatim quotes are **sensitive personnel data** that can
re-identify a respondent in a small cohort. **Control-ranking and the SMART advancement
register are deterministic A7 script calls** (`controls`, `smart_actions`) at Workflow
steps 5/6 — never an LLM fan-out job. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer), and is the
  **most critical job in this skill**. Before any analysis: scrub every nameable
  individual to a role/group label; **suppress any cohort/sub-group breakdown with fewer
  than 5 respondents** and apply **secondary suppression** so a suppressed cell cannot be
  back-calculated from totals; **never reproduce a verbatim respondent quote** that
  identifies the speaker in a small group; ensure **no finding is attributed to a nameable
  individual**. Apply `references/deid-checklist.md` (the reinforced <5 / small-cohort
  checklist) in full. Return the re-identification key SEPARATELY to the orchestrator —
  never to a sibling, never in the document. Every job below consumes only this scrubbed,
  aggregated output. SCOPE-OUT: does not map maturity (Culture-Analyst) or draft the
  roadmap (Roadmap-Planner).
- **Culture-Analyst** — map the triangulated evidence to the chosen model via
  `KB-SNIP-CULTURE-MODELS`, banding against `KB-DATA-CULTURE-MATURITY` (quote
  source+year) across **≥2 sources** (never a single survey); for **Schein**, run the
  **espoused-vs-enacted GAP** diagnosis (named gaps, not a band). Names roles/groups and
  systems, never individuals. SCOPE-OUT: control ranking (the A7 `controls` call), the
  SMART roadmap (Roadmap-Planner).
- **Roadmap-Planner** — turn each accepted advancement move into a SMART action with a
  named **role-label** owner + an ISO due date + a measure + a tied **leading indicator**
  from `KB-DATA-LEADING-INDICATORS` (`smart_actions.validate_register`). SCOPE-OUT:
  mapping maturity (Culture-Analyst), de-identification (De-identifier).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (**Safety Culture / OD Consultant**) before any output:
  no rating from a single survey (model + named population + ≥2 sources), Schein used as a
  gap diagnosis not a ladder band, systemic advancement controls above awareness
  campaigns, no individual named, no <5-cohort cell or identifying quote published.
- **Critic/QA** (MANDATORY) — adversarial final pass: a named model/lens; ≥2 triangulated
  sources for any rating; advancement controls ranked through `KB-SNIP-HOC` (no
  poster-campaign-only roadmap); every action owned + dated + tied to a leading indicator;
  culture models cited as method accurately; and **ZERO de-identification leak** (no
  residual identifier, no <5 cohort cell, no identifying verbatim quote, no individual
  named, no re-id key in the output). PASS/FAIL.

A single small unit with one clean data set may run single-threaded — no subagents — but
the De-identifier scrub + <5 suppression, the A7 control/action calls, and the
Critic/QA + SME passes are **still made**.

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
