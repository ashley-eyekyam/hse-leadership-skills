---
name: ergonomics-assessment
description: Produces a quantified ergonomics / manual-handling assessment for named
  tasks or workstations — posture scoring with RULA/REBA, manual-lifting evaluation
  with the NIOSH lifting equation, and a hierarchy-ranked control plan. Use this skill
  whenever a user asks to assess ergonomics, manual handling, posture, repetitive
  strain, lifting risk, a workstation/MSD risk, or to run a RULA, REBA, or NIOSH lifting-index
  assessment for a specific task or role. It scores each task with the recognised
  deterministic method, compares the result against the method's action bands, prioritises
  engineering and task-redesign controls above PPE/training, and emits a branded report
  with an owned/dated action plan. Grounded in the NIOSH Lifting Equation, RULA/REBA,
  and ISO 11228. Decision-support only; a competent person (ergonomist / occupational-health
  professional) must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: occ-health
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - Mfg
  jurisdiction:
  - All
  status: stable
  plugin: hse-manufacturing
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Ergonomics Assessment

A consultant-grade **quantified ergonomics / manual-handling assessment** for a **named task
or workstation**. It scores each task **deterministically** with the `ergonomics` engine —
**RULA** (upper-limb / posture), **REBA** (whole-body posture), and the **NIOSH lifting
equation** (Recommended Weight Limit + Lifting Index) — compares the result against the
method's published **action bands**, ranks controls up the **hierarchy of controls**, and
sets an owned/dated action plan. It forces the single lever that separates a defensible
artifact from copy-paste paperwork: **task-level specificity plus the full hierarchy of
controls** — every RULA/REBA/NIOSH number is the engine's, never narrated free-text and never
a copied band table, and a missing required parameter is recorded as a `[GAP]`, never an
invented posture angle or load weight. Controls **redesign the task / workstation first**
(elimination → engineering / mechanical aids → administrative rotation → **training last**) —
manual-handling training is **not** a control for a biomechanical overload. Worker MSD
symptoms and fitness detail are **special-category health data**: reported by role/SEG, `<5`
small-cell suppression applied, never a named medical-fitness note in the output. Grounded in
the **NIOSH Lifting Equation, RULA/REBA, and ISO 11228** (ISO 11228-1/-2/-3 + ISO/TR 12296).
Decision-support only; a competent person (ergonomist / occupational-health professional)
must review the output.

## When to use this skill

Use this skill when the user needs a **task-level ergonomics or manual-handling assessment**
for a concrete task, workstation, or role — for example "run a NIOSH lifting assessment on
the despatch-bay carton lift", "score the line-2 assembly posture with RULA", "REBA the
warehouse picking task", or "assess the MSD risk on the packing station". Trigger phrases:
*ergonomics assessment, manual handling, posture, repetitive strain, lifting risk, MSD /
musculoskeletal-disorder risk, workstation / DSE assessment, RULA, REBA, NIOSH lifting index /
Recommended Weight Limit, push/pull (ISO 11228-2)*. If the request is vague ("do an ergonomics
assessment"), the Workflow intake below **refuses to score** until the **assessment method
(Q1)**, the **named task/workstation (Q2)**, and the method's **required input parameters
(Q3)** are captured — it never invents a posture angle or a load weight. For broad SEG-based
exposure-vs-OEL occupational-health assessment with a surveillance schedule, use
`health-risk-assessment` (the complementary skill that shares this same `ergonomics` engine).

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
| UK | ../../knowledge-base/regulatory/uk-hswa.md — Manual Handling Operations Regs 1992 + Health and Safety (DSE) Regs 1992 |
| USA | ../../knowledge-base/regulatory/us-osha.md — OSHA general-duty clause 5(a)(1) + NIOSH lifting-equation guidance |
| India | ../../knowledge-base/regulatory/in-factories-act.md — Factories Act 1948 health provisions; **defers to `hse-india`, mandatory state detection (+ in-state-forms.md for the user's state); emit `[GAP]`, never a national form number** |
| EU | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Ergonomics method (every run) | ../../knowledge-base/standards/iso11228.md (KB-STD-ISO11228) — ISO 11228-1/-2/-3 method scope + the manual-handling decision flow — **and the `ergonomics` engine** for the RULA/REBA/NIOSH numbers (the scores are the engine's, never a band-table copy) |
| MSD controls (every run) | ../../knowledge-base/prompt-snippets/ergo-controls.md (KB-SNIP-ERGO-CONTROLS) — the MSD control hierarchy (eliminate the handling → engineer the workstation/aid/mechanisation → administrative rotation/limits → training, with "training is not a control for a biomechanical overload") |
| Manufacturing clause cross-walk | ../../knowledge-base/prompt-snippets/manufacturing-clause-map.md (KB-SNIP-MANUFACTURING-CLAUSE-MAP) — the ISO-45001 §6.1.2 / §8.1.2 manufacturing clause cross-walk |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and the manufacturing clause cross-walk
`KB-SNIP-MANUFACTURING-CLAUSE-MAP`, applies `KB-SNIP-HOC` + `KB-SNIP-ERGO-CONTROLS` to every
control (task/workstation redesign before PPE/training), and resolves the method facts against
`KB-STD-ISO11228`. **Every RULA/REBA/NIOSH score is the deterministic `ergonomics` engine's
output — never an LLM judgment and never a copied KB band table**; there is no ergonomics-score
data fragment, because the engine is the single source of the numbers. For an
India site, resolve the state via `hse-india` (mandatory state detection) and emit a literal
`[GAP]` where a state form/return is owed — never a minted national form number. The rule-9
manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the six-question table, the
**per-method Q1 branch** (NIOSH / RULA / REBA / push-pull / repetitive / DSE → that method's
required parameters), the **mandatory India→state branch**, the echo-back, and the
refuse-on-vague anchors — lives in **`references/intake.md`**. Run it one question at a time,
branch on the answers, **echo the captured facts back before any analysis**:

- **Q1 — assessment type** (multi-select): manual lifting/lowering (NIOSH) · upper-limb/posture
  (RULA) · whole-body posture (REBA) · push/pull (ISO 11228-2) · repetitive task (ISO 11228-3)
  · DSE/workstation — **branch to that method**.
- **Q2 — named task / workstation** (free-text): the exact task + role + workstation. **Refuse
  a generic task ("general handling") — ergonomics is task-specific; this is the specificity anchor.**
- **Q3 — task parameters** (method-driven): for **NIOSH** — load weight, horizontal/vertical
  origin & destination, asymmetry angle, frequency, coupling, duration; for **RULA/REBA** —
  observed joint angles/posture, force/load, muscle-use/repetition. **Refuse to score on a
  missing required parameter** — record a `[GAP]` and request the measurement; **never invent a
  posture angle or a load weight.**
- **Q4 — exposure pattern**: occasional / regular / continuous shift-long (sets the NIOSH
  frequency multiplier and the surveillance linkage).
- **Q5 — affected population** (free-text): role/SEG + any reported MSD symptoms — **de-identified
  to role/SEG** (special-category health data; small-cell `<5` suppression on any symptom breakdown).
- **Q6 — jurisdiction**: US OSHA general-duty / NIOSH default · UK Manual Handling Operations
  Regs 1992 + DSE Regs 1992 · **India Factories Act health provisions via `hse-india` —
  mandatory state detection, emit `[GAP]`, never a national form number**.

**Scoring is a deterministic engine call, never an LLM judgment and never a KB band-table
copy.** Per the Q1 method, the Workflow runs `ergonomics.niosh_rwl(...)` (lifting) /
`ergonomics.rula_score(...)` (upper-limb) / `ergonomics.reba_score(...)` (whole-body) via the
`scripts/hse_components` symlink, then `ergonomics.to_report_blocks(result)` to drop the
tool-named `[metrics, table]` pair (NIOSH RWL + Lifting Index / RULA grand score + action level
/ REBA final score + action level) straight into `report.json`. A missing required parameter
is a `[GAP]`, not a guessed input.

### The ergonomics-assessment method (method → parameters → engine score → action band → controls → surveillance)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST (special-category MSD/fitness health data).** Before any
   drafting (the `deid` block above + `references/deid-checklist.md` + the De-identifier-runs-first
   orchestration rule): scrub names to role/SEG labels, **report reported MSD symptoms by
   role/SEG**, apply `<5` small-cell suppression to any symptom/outcome breakdown, and **never
   circulate a named medical-fitness or back-injury note**. Everything downstream consumes the
   scrubbed text.
2. **Select the method and capture its required parameters (Q1 → Q3).** Refuse a generic task;
   refuse to score on a missing required parameter — record `[GAP]` and request the measurement.
3. **Score deterministically with the engine.** Call `ergonomics.niosh_rwl/rula_score/reba_score`
   for the Q1 method, then `ergonomics.to_report_blocks(result)`. The score is the engine's,
   **never narrated**; out-of-range inputs raise `ErgonomicsInputError` — fix the input, never
   a silent clamp. Interpret against the method's action band (grounded in `KB-STD-ISO11228`).
4. **Rate residual MSD risk & rank controls up the hierarchy.** Rate residual risk on
   `risk_matrix.score`. Apply `KB-SNIP-HOC` + `KB-SNIP-ERGO-CONTROLS` and call
   `controls.rank_controls` + `controls.validate_treatment`: **eliminate the handling →
   engineer the workstation / mechanise / add an aid → administrative rotation/limits →
   training LAST**. A high RULA/REBA/LI whose only control is manual-handling training is
   **training-led** and inadequate — push it up the hierarchy (task/workstation redesign first)
   or record an explicit "higher-order controls not reasonably practicable because…" justification.
5. **Link symptoms to a surveillance / re-assessment cadence.** Reported MSD symptoms (Q5) and
   the exposure pattern (Q4) drive a symptom-surveillance / re-assessment cadence, reported by
   role/SEG with `<5` suppression.
6. **SMART actions (named owners + dates).** Every control/surveillance action becomes a SMART
   action (named role owner + ISO due date + measure), validated by `smart_actions.validate_register`.
7. **Validate against `references/QUALITY_CHECKLIST.md`** then **assemble the branded report**
   (`assets/ergonomics-assessment.report.json`) and run the canonical `report-output` call below.

The **deterministic scoring/rating steps (3, 4 via `ergonomics`/`risk_matrix`/`controls`) are
A7 script calls in every case** — never a fan-out job that narrates a score.

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

This is a **moderate by-method fan-out** for a multi-task survey: the De-identifier is the
**sequential first gate** (special-category MSD/fitness health data), the fan-out jobs are
**per-method Scoring-Analysts** (lifting · posture) that call the `ergonomics` engine, plus a
**Controls-&-Surveillance-Planner**, and **Critic/QA + SME Review are mandatory**. The
RULA/REBA/NIOSH scoring and the residual-risk rating are **deterministic A7 script calls**
(`ergonomics`, `risk_matrix`, `controls`), never LLM fan-out work. Archetypes:
`KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer). Scrub every identifier
  to a stable role/SEG label, and treat **reported MSD symptoms and medical-fitness notes as
  special-category health data**: report by role/SEG, apply `<5` suppression to any
  symptom/outcome breakdown, and strip every named fitness/back-injury note. Returns the
  re-identification key SEPARATELY (never to a sibling). Every job below consumes only its
  scrubbed, role/SEG-labelled output.
- **Scoring-Analyst · manual lifting (NIOSH)** — for a lifting/lowering task, take the captured
  parameters (load weight, horizontal/vertical origin & destination, asymmetry angle,
  frequency, coupling, duration) and call `ergonomics.niosh_rwl(...)` then
  `ergonomics.to_report_blocks(result)` to return the RWL + Lifting Index `[metrics, table]`
  pair. **Refuse to score on a missing required parameter** — record `[GAP]` and request the
  measurement; never invent a weight or a distance. SCOPE-OUT: control selection (Planner),
  posture scoring (the posture analyst).
- **Scoring-Analyst · posture (RULA / REBA)** — for an upper-limb/whole-body posture task, take
  the observed joint angles + force/load + muscle-use/repetition and call
  `ergonomics.rula_score(...)` / `ergonomics.reba_score(...)` then
  `ergonomics.to_report_blocks(result)` to return the grand/final score + action-level
  `[metrics, table]` pair. **Refuse to score on a missing required joint score** — record
  `[GAP]`, never invent an angle. SCOPE-OUT: control selection (Planner), lifting (the NIOSH analyst).
- **Controls-&-Surveillance-Planner** — rank controls up the hierarchy via `controls` +
  `KB-SNIP-HOC` + `KB-SNIP-ERGO-CONTROLS`: **eliminate the handling → engineer the
  workstation / mechanise / add an aid → administrative rotation/limits → training LAST**;
  flag any training-led treatment of a high RULA/REBA/LI as inadequate (training is not a
  control for a biomechanical overload), then link reported symptoms to a surveillance /
  re-assessment cadence. Every action SMART (owner + ISO date). SCOPE-OUT: scoring (the Analysts).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Chartered Ergonomist (CIEHF) / Occupational-Health
  Professional) before any output: every score from the engine with its inputs shown, action
  bands cited to source, controls above PPE/training, and ZERO special-category-health leak
  (no named fitness note, no `<5` symptom cell).
- **Critic/QA** (MANDATORY) — adversarial final pass: every score traces to its `ergonomics`
  engine inputs (no narrated number, no band-table copy), every missing parameter is a `[GAP]`
  not a guess, controls redesign the task before they train the worker, every action owned +
  dated, every citation traces to the KB, and zero MSD/fitness leak. PASS/FAIL.

A single-task single-method check (e.g. one RULA on one workstation) runs single-threaded — no
subagents — but the **De-identifier runs first**, the `ergonomics`/`risk_matrix`/`controls`
calls are still made deterministically, and the Critic/QA + SME passes are still run.

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
