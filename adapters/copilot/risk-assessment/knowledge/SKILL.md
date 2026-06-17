---
name: risk-assessment
description: Creates consultant-grade, task- and site-specific risk assessments (HIRA
  / HIRARC). Use this skill whenever a user asks to assess risk, build or review a
  risk assessment, perform a hazard identification and risk assessment, score likelihood
  and severity on a risk matrix, select or rank controls by the hierarchy of controls,
  or produce a HIRA, HIRARC, or risk register for a specific task, activity, site,
  or asset. Optionally assesses environmental aspects and impacts (ISO 14001 clause
  6.1.2) when the user asks for an environmental risk or aspects/impacts assessment.
  Grounds the assessment in ISO 45001 clause 6.1.2 (and ISO 14001 6.1.2 for environmental
  scope), enforces the hierarchy of controls (no PPE-only treatments without justification),
  re-scores residual risk after controls, and assigns SMART corrective actions with
  named owners and due dates — emitting a branded report. Decision-support only; a
  competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 1
  audience:
  - M
  - C
  - F
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Risk Assessment (HIRA)

A consultant-grade HSE skill that produces a task/site/asset-specific Hazard
Identification & Risk Assessment grounded in **ISO 45001 clause 6.1.2**, enforcing
the **hierarchy of controls**, with an optional **ISO 14001 clause 6.1.2
environmental-aspects branch**. It forces the single lever that separates a
defensible artifact from copy-paste paperwork: task/site specificity plus the full
hierarchy of controls — never a vague, PPE-only treatment. Likelihood × severity
scoring, residual re-scoring, and control ranking are **deterministic** (the A7
`risk_matrix`/`controls` engines), never prose judgement; every action carries a
named owner and a due date.

## When to use this skill

Use this skill when the user needs a risk assessment for a **concrete task, site, or
asset** — for example "assess the risk of confined-space entry to clean Tank T-402",
"build/review a HIRA for working at height on the north roof", "score this hazard on
our 5×5 matrix", or "rank the controls by the hierarchy of controls". Trigger
phrases: *risk assessment, HIRA, HIRARC, hazard identification, risk matrix,
likelihood and severity, hierarchy of controls, residual risk, risk register*. Use
it **also** for an **environmental aspects/impacts assessment** (ISO 14001 6.1.2) —
"assess the environmental aspects of the solvent degreasing line", "environmental
risk of the discharge" — via the scope gate (Q0) in the intake. If the request is
vague ("write me a risk assessment"), the Workflow intake below **refuses to
proceed** until the specific task/activity is elicited.

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
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Environmental scope (Q0 = Environmental/Both) | ../../knowledge-base/standards/iso-14001.md (KB-STD-ISO14001, clause 6.1.2 — environmental aspects & impacts) |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 HIRA + 8.1.2 hierarchy of
controls) and applies `KB-SNIP-HOC` to every control; for an India site it resolves
the state via `KB-REG-IN-STATEFORMS` (mandatory state detection — confirm the state
before citing any form, never a national form number); when Q0 selects the
environmental scope it also grounds in `KB-STD-ISO14001` 6.1.2. The rule-9 manifest
is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The intake opens with the **scope gate (Q0)**, then runs the safety questions; the
**environmental-aspects branch (Q-E1…Q-E5)** is asked *only* when Q0 selects
*Environmental* or *Both*. Echo the captured facts back for confirmation before any
analysis. **Refuse to proceed on a vague task** (Q3 is the specificity anchor) — ask
again, or record `[ASSUMPTION]` / `[GAP]`; never invent.

| # | Question | Type | Options / prompt |
|---|---|---|---|
| **Q0** | **Scope of this assessment** | MCQ | **Occupational safety (default) · Environmental aspects · Both** — *Environmental*/*Both* activates the Q-E branch + the `KB-STD-ISO14001` row |
| Q1 | Jurisdiction | MCQ | India · UK · USA · EU · Other/Unknown (India → Q1a) |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Other — **mandatory state detection; confirm before citing any form** |
| Q2 | Industry / sector | MCQ + free-text | Construction · Manufacturing · Oil & Gas · Chemicals · Mining · General/Other (+ detail) |
| Q3 | **The task/activity being assessed, broken into steps** | **free-text** | "Describe the exact task and its steps (e.g. 'confined-space entry to clean tank T-402: isolate → purge → gas-test → enter → clean → exit')." — **the specificity anchor; refuse a vague answer** |
| Q4 | Location / site | free-text | "Which specific site/area/asset?" |
| Q5 | Who is exposed? | MCQ multi-select | Own workers · Contractors · Public/visitors · Nearby community |
| Q6 | Existing controls already in place | free-text | "What controls already exist for this task?" (seeds the initial-vs-residual baseline) |
| Q7 | Likelihood band (org scale) | MCQ | 1 Rare · 2 Unlikely · 3 Possible · 4 Likely · 5 Almost certain |
| Q8 | Severity band (org scale) | MCQ | 1 Negligible · 2 Minor · 3 Moderate · 4 Major · 5 Catastrophic |
| Q9 | Org risk-matrix size | MCQ | 3×3 · 4×4 · **5×5 (default)** · Supply our matrix |
| Q10 | Assessment type | MCQ | Baseline (whole task) · Issue-based (a change/hazard) · Continuous (review of an existing RA) |

**Environmental-aspects branch (asked only when Q0 = Environmental/Both; ISO 14001 6.1.2):**

| # | Question | Type | Options / prompt |
|---|---|---|---|
| Q-E1 | The activity / product / service under environmental review | free-text | "Describe the exact activity (e.g. 'solvent degreasing line at Plant 3: load → spray → drain → dry')." — the environmental specificity anchor; refuse a vague answer |
| Q-E2 | Environmental aspects | MCQ multi-select + free-text | Emissions to air · Releases to water · Waste generation · Land contamination · Resource use · Energy use · Noise/odour/other |
| Q-E3 | Associated environmental impacts | free-text | "For each aspect, what is the resulting impact? (e.g. solvent vapour → air quality/VOC; spent solvent → water contamination)." |
| Q-E4 | Operating condition | MCQ multi-select | Normal · Abnormal (start-up/shutdown/maintenance) · Emergency (spill/fire/upset) |
| Q-E5 | Compliance obligations | free-text | "Any environmental permits, consent limits, or obligations (discharge consents, emission limits, waste licences)?" |

After the last applicable question (Q10, and Q-E5 if the branch ran), **echo a
captured-facts summary** ("Assessing: confined-space entry to tank T-402, Plant 3,
Maharashtra, own workers + contractors, 5×5 matrix, baseline — correct?") and only
then proceed. Q7/Q8 establish the org scale; each hazard **and each environmental
aspect** is scored individually at step 3.

### The HIRA method (ISO 45001 6.1.2 loop + the optional ISO 14001 6.1.2 environmental loop)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Everything downstream consumes the
   scrubbed, role-labelled text.
2. **Hazard identification (and, if in scope, environmental-aspect identification)** —
   for each task step from Q3, identify the specific, observable hazards (energy
   sources, substances, environment, human factors) grounded in `KB-STD-ISO45001`
   6.1.2; each names **what** is hazardous and **who/what is exposed**. If the
   environmental branch is active, **also** identify, per activity/product/service,
   the **aspect → impact** pairs grounded in `KB-STD-ISO14001` 6.1.2 (air/water/
   waste/land/resource-energy), tagged with the Q-E4 operating condition (normal /
   abnormal / emergency). Flag `[GAP]` where uncertain — never invent.
3. **Initial risk scoring (and environmental significance scoring)** — for each
   hazard call `risk_matrix.load_matrix(config)` then `risk_matrix.score(likelihood,
   severity, matrix)` (Q9 config; default 5×5). For each environmental aspect, score
   **significance with the SAME `risk_matrix.score`** engine, reading the axes
   against **environmental consequence descriptors** (scale/extent of release,
   reversibility, duration) — **no new engine**. The score + band are the engine's,
   deterministically — not prose.
4. **Control selection (the hierarchy-of-controls lever — safety hazards AND
   environmental aspects)** — propose controls and **apply `KB-SNIP-HOC`**: rank
   Elimination → Substitution → Engineering → Administrative → PPE; then call
   `controls.rank_controls` + `controls.validate_treatment`. For an environmental
   aspect this means **eliminate or substitute the aspect** (switch to a
   non-hazardous solvent, close-loop the process) **before mitigating**. If
   `ppe_admin_only` is `True`, the Workflow **must** add a higher-order control **or**
   record an explicit justification ("higher-order controls not reasonably
   practicable because…"). A lower-order-only treatment with no justification is a
   **defect the Critic/QA pass must catch** — this is the hard enforcement of the
   core value, not a mention.
5. **Residual re-scoring** — re-score each hazard (and each aspect) *with the selected
   controls applied* via `risk_matrix.score`, then `risk_matrix.residual_delta(initial,
   residual)` to show the movement. If a residual safety risk or environmental
   significance remains High/Critical, flag that additional controls or a
   stop-work / cease-the-aspect decision are required (not "accept and proceed").
6. **SMART actions (named owners + dates)** — for every control that is an action,
   produce a SMART action (specific, measurable, **assignable (named owner)**,
   relevant, **time-bound (ISO due date)**) and call `smart_actions.validate_register`.
   Any action missing an owner, a valid date, a measure, or a hazard link is
   **invalid** and must be fixed — no anonymous actions, no "ASAP".
7. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check loop before
   output: every hazard (and in-scope aspect) scored; every control HoC-ranked; no
   un-justified lower-order-only treatment; every action owned + dated + hazard-linked;
   every citation traced to the KB (ISO 45001 6.1.2 always; ISO 14001 6.1.2 when the
   branch ran); de-id applied; no conclusion on an unstated assumption.
8. **Assemble the branded report** — build `report.json` (see `assets/hira-report.template.json`)
   and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge
the assembled work before deciding to fan out. The **deterministic scoring/ranking
steps (3, 4, 5 via `risk_matrix`/`controls`) are A7 script calls in every case —
never a fan-out job** (there is no "Risk-Scorer" subagent).

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
     is presence-only (never diffed), so each skill names its own jobs here. -->

This is the **STANDARD moderate roster** (A6 "moderate = 2–3"): the De-identifier is
the **sequential first gate** (not a fan-out peer), the **3 fan-out jobs** are
Researcher + Regulatory-Checker + Drafter, and **Critic/QA is mandatory**. **There is
no Risk-Scorer subagent** — scoring, residual re-scoring, and control ranking are
deterministic A7 script calls at Workflow steps 3/4/5 (`risk_matrix`, `controls`),
never LLM fan-out work. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all
  PII/health detail to role labels before any analysis (every fan-out job below
  consumes scrubbed text).
- **Researcher** — gather evidence for the identified hazards from primary sources
  (substance/process/equipment data, prior-incident patterns); cited summary, flag
  `[GAP]`. SCOPE-OUT: law (Regulatory-Checker), drafting (Drafter). (Scoring is NOT a
  subagent — it is the A7 `risk_matrix` script.)
- **Regulatory-Checker** — for the resolved jurisdiction, return the applicable RA
  duty + clause + (India) the state form via `KB-REG-IN-STATEFORMS`; conservative,
  flag `[GAP]`. SCOPE-OUT: drafting the RA, gathering hazard evidence (Researcher).
- **Drafter** — write the risk register + control plan + action register to the
  output template using role placeholders; each control tagged its `KB-SNIP-HOC`
  tier (consumes the De-identifier's scrubbed text + the A7 `risk_matrix`/`controls`
  scores + the Regulatory-Checker's verdict). SCOPE-OUT: gathering evidence
  (Researcher), checking law (Regulatory-Checker).
- **Critic/QA** (MANDATORY) — every hazard scored (via the A7 engine), every control
  HoC-ranked, no PPE/admin-only treatment without justification, every action owned +
  dated + hazard-linked, every citation traces to the KB, zero PII leaked. PASS/FAIL.

Researcher + Regulatory-Checker may merge to land at 2 fan-out jobs and stay in-band.
Simple single-hazard assessments run single-threaded — no subagents — but the A7
scoring/ranking calls and the Critic/QA pass are still made.

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
