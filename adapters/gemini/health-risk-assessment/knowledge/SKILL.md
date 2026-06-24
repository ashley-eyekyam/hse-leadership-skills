---
name: health-risk-assessment
description: Produces an occupational-health risk assessment for named tasks or roles
  — similar-exposure-group definition, hazard-to-OEL comparison, ergonomic scoring
  (RULA/REBA/NIOSH), and a health-surveillance schedule. Use this skill whenever a
  user asks to assess occupational-health risk, chemical/noise/vibration/ergonomic
  exposure, build similar-exposure groups, compare exposures to OELs, set up health
  surveillance, or run an ergonomics assessment. It groups workers by exposure, compares
  measured/estimated exposure to occupational exposure limits, scores manual-handling
  and posture risk with recognised tools, prioritises controls up the hierarchy, and
  sets an OEL-linked surveillance schedule — emitted as a branded report. Decision-support
  only; a competent person (occupational hygienist/physician) must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: occ-health
  tier: 3
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
  bundled_in:
  - hse-manufacturing
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Health Risk Assessment

A consultant-grade occupational-health risk assessment for **named tasks or roles**. It
groups workers into **similar-exposure groups (SEGs)**, compares measured/estimated
exposure to a **cited occupational exposure limit (OEL/WEL/PEL)**, scores manual-handling
and posture risk **deterministically** with the `ergonomics` engine (RULA / REBA / NIOSH
lifting equation — never free-text scoring), ranks controls up the **hierarchy of
controls**, and sets an **OEL-linked health-surveillance schedule**. It forces the single
lever that separates a defensible artifact from copy-paste paperwork: task/SEG specificity
plus the full hierarchy of controls — never a vague, PPE-only or surveillance-only
treatment. Health-surveillance and exposure-monitoring data are **special-category health
data**: reported by SEG/role, `<5` health-outcome cells suppressed, never circulated with
names. Decision-support only; a competent person (occupational hygienist / OH physician)
must review the output.

## When to use this skill

Use this skill when the user needs an occupational-health risk assessment for a **concrete
task or role** — for example "assess the press-shop noise exposure for the operators",
"build SEGs for the solvent-degreasing line and compare to the WEL", "score the manual
handling on the despatch bay with NIOSH", or "set a health-surveillance schedule for the
welding bay". Trigger phrases: *health risk assessment, occupational-health risk, similar
exposure group / SEG, OEL / WEL / PEL comparison, exposure monitoring, RULA, REBA, NIOSH
lifting equation, manual handling, HAV/WBV, audiometry, health surveillance*. If the
request is vague ("do a health risk assessment"), the Workflow intake below **refuses to
proceed** until the **hazard type, the named SEG tasks/roles, and an exposure basis** are
captured — no exposure-vs-OEL comparison is produced before that.

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
| OEL comparison (every run) | ../../knowledge-base/data-points/oel-limits.md (KB-DATA-OEL-LIMITS) + ../../knowledge-base/data-points/exposure-limits.md (KB-DATA-EXPOSURE-LIMITS) — the ONLY OEL source; quote authority+year, never a parallel table |
| Ergonomics (when selected) | ../../knowledge-base/standards/ghs-ergo.md (KB-STD-GHS-ERGO) + the `ergonomics` engine — RULA/REBA/NIOSH method facts |
| Surveillance cadence | ../../knowledge-base/prompt-snippets/surveillance-triggers.md (KB-SNIP-SURVEILLANCE-TRIGGERS) |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and the operations clause cross-walk
`KB-SNIP-OPS-CLAUSE-MAP`, applies `KB-SNIP-HOC` to every control, and resolves **every**
exposure against a cited OEL/WEL/PEL from `KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS`
(the single OEL source — **no parallel OEL table**, two disagreeing OEL sources are a
defensibility risk). Ergonomic scores are the deterministic `ergonomics` engine's
(RULA/REBA/NIOSH) grounded in `KB-STD-GHS-ERGO`; surveillance cadence follows
`KB-SNIP-SURVEILLANCE-TRIGGERS`. For an India site resolve the state via
`KB-REG-IN-STATEFORMS` (mandatory state detection). The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the six-question table
(Q1 **health-hazard type** [chemical/inhalation · noise · vibration HAV/WBV · manual-handling
/ ergonomics · thermal · biological] · Q2 **tasks/roles & SEG basis** [the specificity
anchor — refuse generic] · Q3 **exposure data** [measured · estimated · none-yet → branch
to a monitoring-strategy-first recommendation] · Q4 **OEL source** · Q5 **ergonomics tool**
[RULA / REBA / NIOSH / manual-handling — asked only when ergonomics is selected] · Q6
**jurisdiction**), the **ergonomics-tool branch**, the **no-data → monitoring-strategy
branch**, the **mandatory India→state branch**, the echo-back, and the refuse-on-vague
anchors — lives in **`references/intake.md`**. Run it one question at a time, branch on the
answers, **echo the captured facts back before any analysis**, and **refuse to produce an
exposure-vs-OEL comparison until the hazard type (Q1), the named SEG tasks/roles (Q2), and
an exposure basis (Q3) are captured** (record `[ASSUMPTION]` / `[GAP]`, never invent).

### The occupational-health risk-assessment method (SEG → OEL → ergonomics → controls → surveillance)

Full method in `references/METHODOLOGY.md` (the method snippet is `KB-SNIP-SURVEILLANCE-TRIGGERS`). Steps:

1. **De-identify the inputs FIRST (special-category health data).** Before any drafting (the
   `deid` block above + `references/deid-checklist.md` + the De-identifier-runs-first
   orchestration rule). Exposure-monitoring and surveillance results (audiometry, lung
   function, biological monitoring, HAV scores) are **GDPR Art. 9 / DPDP special-category
   health data**: scrub names to role labels, **report by SEG/role not by individual**,
   apply `<5` small-cell suppression to **any** health-outcome breakdown, and **never
   circulate a surveillance result with a name**. Everything downstream consumes the
   scrubbed, SEG-labelled text.
2. **Define the similar-exposure groups (SEGs).** From the Q2 named tasks/roles, group
   workers with materially the same exposure into SEGs — the SEG is the unit of assessment
   and of surveillance. Refuse a generic SEG ("all staff"); a SEG names the task/role and
   the agent it is exposed to. Flag `[GAP]` where the basis is uncertain — never invent.
3. **Characterise exposure & compare to a CITED OEL.** For each SEG/agent, state the
   measured or estimated exposure (Q3) and compare it to the binding OEL/WEL/PEL resolved
   **with source+year** from `KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS` (the single
   OEL source). An exposure assessed with **no cited OEL** is a defect (specificity ·
   regulatory_citation_accuracy). If Q3 is *none-yet*, do **not** fabricate a comparison —
   recommend a monitoring strategy first and stop the comparison.
4. **Score ergonomic risk with the engine (deterministic).** When the hazard is
   manual-handling/ergonomics, call the `ergonomics` engine via the `scripts/hse_components`
   symlink — `ergonomics.rula_score(...)` / `ergonomics.reba_score(...)` /
   `ergonomics.niosh_rwl(...)` per the Q5 tool — then `ergonomics.to_report_blocks(result)`
   to drop the tool-named `[metrics, table]` pair (RULA grand score + action level / REBA
   final score / NIOSH RWL + Lifting Index) straight into `report.json`. The score is the
   engine's, **never narrated free-text**; grounded in `KB-STD-GHS-ERGO`.
5. **Rate residual health risk & rank controls up the hierarchy.** Rate the residual health
   risk on `risk_matrix.score`. Apply `KB-SNIP-HOC` and call `controls.rank_controls` +
   `controls.validate_treatment`: **substitution / engineering precede PPE — and precede
   surveillance**. Surveillance is **not a control**: a noise plan offering only hearing
   protection (no engineering/substitution) is a defect the Critic/QA pass must catch. If
   `ppe_admin_only` is `True`, add a higher-order control **or** record an explicit "not
   reasonably practicable because…" justification.
6. **Set the OEL-linked surveillance schedule.** Following `KB-SNIP-SURVEILLANCE-TRIGGERS`:
   where exposure is **at/above the action level or the OEL**, surveillance is required at
   the agent's cadence (noise ≥ action level → audiometry; respiratory sensitisers → lung
   function; HAV → HAV surveillance); **below** the action level set a monitoring/re-assessment
   cadence, surveillance not yet triggered. The schedule is keyed to the cited OEL, not asserted.
7. **SMART actions (named owners + dates).** Every control/surveillance action becomes a
   SMART action (named role owner + ISO due date + measure + SEG link), validated by
   `smart_actions.validate_register`. No anonymous or undated actions.
8. **Validate against `references/QUALITY_CHECKLIST.md`** then **assemble the branded report**
   (`assets/health-risk-assessment-report.template.json`) and run the canonical `report-output`
   call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **deterministic ergonomics/scoring steps
(4, 5 via `ergonomics`/`risk_matrix`/`controls`) are A7 script calls in every case** — never
a fan-out job that narrates a score.

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

This is a **moderate by-hazard fan-out**: the De-identifier is the **sequential first
gate** (special-category health data), the fan-out jobs are **per-hazard Exposure-Analysts**
+ a **Controls-&-Surveillance-Planner**, and **Critic/QA is mandatory**. Ergonomic and risk
scoring are deterministic A7 script calls (`ergonomics`, `risk_matrix`, `controls`), never
LLM fan-out work. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer). Scrub every
  identifier to a stable role label, and treat exposure-monitoring + **health-surveillance
  results as special-category health data**: report by SEG/role, apply `<5` suppression to
  any health-outcome breakdown, and strip every audiometry / biological-monitoring / HAV
  result that carries a name. Returns the re-identification key SEPARATELY (never to a
  sibling). Every job below consumes only its scrubbed, SEG-labelled output.
- **Exposure-Analyst · chemical/inhalation** — characterise each SEG's exposure and compare
  it to a cited OEL/WEL/PEL (source+year) from `KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS`;
  flag `[GAP]` on an unresolved limit. SCOPE-OUT: control selection (Planner), ergonomics.
- **Exposure-Analyst · noise / vibration (HAV/WBV)** — assess the SEG's noise/vibration
  exposure against the action-level/limit (cited), and name the surveillance trigger
  (audiometry / HAV surveillance). SCOPE-OUT: control selection (Planner).
- **Exposure-Analyst · ergonomics** — for the Q5 tool, call the `ergonomics` engine
  (`rula_score` / `reba_score` / `niosh_rwl`) then `ergonomics.to_report_blocks(result)` to
  return the tool-named `[metrics, table]` pair; the score is the engine's, never narrated.
  SCOPE-OUT: control selection (Planner), OEL comparison (chemical analyst).
- **Controls-&-Surveillance-Planner** — rank controls up the hierarchy via `controls` +
  `KB-SNIP-HOC` (substitution/engineering before PPE **and before surveillance**), then set
  the OEL-linked surveillance schedule per `KB-SNIP-SURVEILLANCE-TRIGGERS`; every action
  SMART (owner + ISO date). SCOPE-OUT: exposure assessment (the Analysts).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Occupational Hygienist / OH Physician) before any output:
  every exposure compared to a cited OEL, ergonomic scores from the engine, controls above
  PPE and above surveillance, and ZERO special-category-health leak (no named surveillance
  result, no `<5` health-outcome cell).
- **Critic/QA** (MANDATORY) — adversarial final pass: every SEG named, every exposure
  OEL-compared (cited), ergonomic scores from the `ergonomics` engine, no PPE/surveillance-only
  treatment without justification, every action owned + dated + SEG-linked, every citation
  traces to the KB, and zero special-category health leak. PASS/FAIL.

A single-hazard single-SEG check (e.g. one SEG's noise exposure) runs single-threaded — no
subagents — but the `ergonomics`/`risk_matrix`/`controls` calls and the Critic/QA + SME
passes are still made.

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
