---
name: sop-writer
description: Creates clear, task-specific, version-controlled standard operating procedures
  (SOPs) and safe work procedures (SWPs) written to the reader's literacy level. Use
  this skill whenever a user asks to write, draft, or review an SOP, a standard operating
  procedure, a safe work procedure, an SWP, a work instruction, or a step-by-step
  procedure for a specific task, operation, or piece of equipment. Grounds the procedure
  in ISO 45001 clause 8.1 (operational control), embeds the hierarchy of controls
  into the individual steps (no procedure that relies on PPE or 'follow the rules'
  alone without justification), integrates with an existing risk assessment or JSA
  where one is supplied rather than re-scoring it, names responsibilities and required
  competencies by role, adds emergency provisions, and produces a revision-controlled,
  approval-ready, branded document. Decision-support only; a competent person must
  review the procedure before it is issued.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: ms-admin
  tier: 1
  audience:
  - M
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Safe Work Procedure / SOP Writer

A consultant-grade HSE skill that produces a **task-specific, version-controlled
SOP / safe work procedure** grounded in **ISO 45001 clause 8.1 (operational
control)**, written to the **reader's literacy level**, with the **hierarchy of
controls embedded INTO the procedure steps themselves** — not bolted on as a generic
PPE list at the end. It forces the single lever that separates a defensible artifact
from copy-paste paperwork: task/step specificity plus the full hierarchy of controls —
never a vague, "work safely" procedure that relies on PPE alone. A procedure is itself
an *administrative* control, so a defensible SOP surfaces the higher-order controls it
operates within and **ingests an existing risk assessment (B1) or JSA (B2) rather than
re-scoring risk** — it composes with the hazard analysis, it does not duplicate it.

## When to use this skill

Use this skill when the user needs a **standard operating procedure or safe work
procedure for a concrete task, operation, or asset** — for example "write an SOP for
the manual print-head changeover on Press 4", "draft a safe work procedure for
confined-space cleaning of Tank T-402", "turn this JSA into a step-by-step work
instruction", or "review our SOP for the abrasive-cutting task". Trigger phrases: *SOP,
standard operating procedure, safe work procedure, SWP, work instruction, procedure,
step-by-step, operational control, ISO 45001 8.1, version-controlled, hierarchy of
controls*. If the user already has a B1 risk assessment or a B2 JSA, this skill
**ingests it** as the hazard/control source and cross-references it by id; if not, it
elicits the hazards inline and flags that a formal RA/JSA is the more rigorous source.
If the request is vague ("write me an SOP") or the steps are generic ("work safely at
all times"), the Workflow intake below **refuses to proceed** until the real task and
its ordered steps are elicited.

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
| Operational-control standard (all jurisdictions) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001, clause 8.1 — operational control + 8.1.2 hierarchy of controls) |

This skill **always** grounds in `KB-STD-ISO45001` (clause **8.1** operational
control + **8.1.2** hierarchy of controls) and applies `KB-SNIP-HOC` to every control
it embeds in a step; it calibrates the procedure's reading level and register to the
stated reader via `KB-SNIP-AUDIENCE` (the literacy lever). For an India site it resolves
the state via `KB-REG-IN-STATEFORMS` (**mandatory state detection** — confirm the state
before citing any state-specific documented-procedure duty; an SOP is an internal
management-system document, so this skill cites **no statutory SOP form number**, only
the documented-procedure obligation the jurisdiction places on the procedure). The
rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(jurisdiction · industry · the task/operation anchor Q3 · the **ingest gate Q4** ·
location · hazards · controls/PPE/permits · standards/limits · the **procedure-steps
anchor Q8** · roles & competencies · literacy register · review cycle · output type),
the **ingest branches** (Q4 = have JSA / have RA → ingest hazards + rated controls, do
NOT re-score; Q4 = Neither → elicit Q6/Q7 inline), the **mandatory India→state branch**
(Q1 = India → Q1a), the **no-review branch** (Q11 blank → review-on-change `[ASSUMPTION]`),
the echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run
it one question at a time, branch on the answers, **echo the captured facts back before
authoring**, and **refuse to proceed on a vague task (Q3) or generic/missing steps
(Q8)** — record `[GAP]` / `[ASSUMPTION]`, never invent. (Worked examples + the full
intake rationale: `references/METHODOLOGY.md`.)

### The SOP-authoring method (ISO 45001 8.1 operational-control loop)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Everything downstream consumes the
   scrubbed, role-labelled text. No-op if the inputs carry no personal data, but always
   runs.
2. **Establish the task/operation, its scope/boundaries, and its hazards (ingest or
   elicit)** — fix what the SOP covers and explicitly what it does **not** (boundaries,
   Q3). Then establish the hazards: **if the user supplied a B2 JSA or B1 RA (Q4),
   ingest it** — read its hazards and its **rated controls** and carry them forward,
   **cross-referencing the source by id** in the SOP (the "method ↔ RA cross-referenced"
   bar). **Do NOT re-score risk** — this skill authors a procedure, it does not run a
   risk matrix (if no rating exists, point the user at B1/B2). **If no prior analysis
   exists, elicit the hazards + existing controls inline** (Q6/Q7) and **flag that a
   formal RA/JSA is the more rigorous source**. Flag `[GAP]` where a step's hazards are
   uncertain — never invent.
3. **Derive the hierarchy-of-controls-aware control set** — for each hazard tied to a
   step, establish the control(s) and **apply `KB-SNIP-HOC`**: rank Elimination →
   Substitution → Engineering → Administrative → PPE; then call
   `controls.rank_controls` + `controls.validate_treatment` (the **only** A7 engine this
   skill calls) on the full control set. The SOP **must** surface the higher-order
   controls the procedure operates within (e.g. "the line is de-energised and locked out
   [Engineering/Admin isolation] *before* this procedure begins") — the procedure is an
   administrative control and must not be presented as the sole defence. If
   `ppe_admin_only` is `True`, the Workflow **must** either add a higher-order control
   **or** record an explicit justification ("higher-order controls not reasonably
   practicable because…"). An un-justified PPE/admin-only treatment is a **defect the
   Critic/QA pass must catch** — this is the hard enforcement of the core value.
4. **Author the step-by-step procedure (controls embedded INTO each step)** — write the
   procedure as **real, ordered, task-specific steps** (from Q8), one action per step,
   to the target literacy level (Q10, via `KB-SNIP-AUDIENCE`). Each risk-bearing step
   names, **inline**, the **controls / PPE / checks / hold-points** that make *that*
   step safe — e.g. "Step 4 — Open valve V-12 slowly. *Control: stand clear of the
   discharge line (engineering guard in place); wear face shield + chemical gloves
   [PPE]; confirm pressure gauge reads <2 bar [check/hold-point].*" The Workflow
   **refuses to emit generic "work safely" steps** — controls are embedded into the
   steps, never appended as a flat list at the end.
5. **Add responsibilities, competencies, equipment/materials, emergency provisions** —
   name the **roles** responsible (who authorises, who executes, who verifies — role
   labels only, de-identified), the **required competencies/training** tied to those
   roles (the "tied to training records" bar), the **equipment/materials/permits**
   required (and any link to a permit-to-work / isolation regime), and the
   **emergency/abnormal-condition provisions** (stop conditions, what to do if a
   hold-point fails, rescue/spill/first-aid arrangements).
6. **References + revision/approval control** — cite the references the SOP rests on
   (ISO 45001 8.1; the jurisdiction fragment for any documented-procedure duty; **the
   ingested RA/JSA by id**; any standards/manufacturer instructions/permits), and build
   the **revision-control + approval block**: SOP id/number, version, effective date,
   author role, reviewer role, approver role, review cycle / next-review trigger (the
   "version-controlled" bar). No real names — role labels and signature-block
   placeholders only.
7. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check loop before
   output: every step specific and ordered (no generic boilerplate); every risk-bearing
   step has its controls/PPE/checks embedded; no un-justified lower-order-only treatment;
   higher-order controls the procedure sits within are surfaced; responsibilities +
   competencies named (roles, not names); emergency provisions present; references cited
   and traced to the KB (ISO 45001 8.1 always; the ingested RA/JSA by id); revision/
   approval block complete; de-id applied; written to the stated literacy level; no
   conclusion on an unstated assumption.
8. **Assemble the branded SOP document** — build `report.json` (see
   `assets/sop-report.template.json`) and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge
the assembled work before deciding to fan out. The **deterministic control-ranking step
(step 3 via `controls`) is an A7 script call in every case — never a fan-out job**
(there is **no Control-Ranker subagent**). This skill calls **only** `controls`; it
does **not** call `risk_matrix` (it ingests a rating, never re-scores) or
`smart_actions`/`rca`/`incident_rates` (a SOP carries steps + responsibilities, not a
SMART action register, an RCA, or a rate — those are B5/B7).

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
the **sequential first gate** (not a fan-out peer), the **2 fan-out jobs** are
Researcher + Drafter, and **Critic/QA is mandatory**. **There is no Control-Ranker
subagent** — control ranking is the deterministic A7 `controls` script call at Workflow
step 3, never LLM fan-out work. (Scoring is **not** a subagent and not this skill's —
point the user at B1/B2 if no rating exists.) Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub any
  PII/health detail (a task description, an ingested incident-derived RA, or named roles
  may carry it) to role labels before any authoring (every fan-out job below consumes
  scrubbed text). No-op if the inputs carry no personal data, but always present.
- **Researcher** — gather evidence for the task's hazards, the higher-order controls
  available, and the applicable standard/manufacturer/permit references; cited summary,
  flag `[GAP]`. SCOPE-OUT: authoring the SOP (Drafter); ranking controls (that is the A7
  `controls` script, not a subagent); scoring risk (this skill does not score — point at
  B1/B2).
- **Drafter** — write the step-by-step procedure with controls/PPE/checks embedded per
  step, plus responsibilities, competencies, emergency provisions, references, and the
  revision/approval block, to the target literacy level, using role placeholders
  (consumes the De-identifier's scrubbed text + any ingested RA/JSA + the A7 `controls`
  ranking + the Researcher's evidence). SCOPE-OUT: gathering evidence (Researcher);
  ranking controls (A7 `controls` script).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (operations / technical-procedure author) before any
  output: controls embedded INTO each risk-bearing step (not a generic PPE list at the
  end), the higher-order controls the procedure sits within surfaced, RA/JSA ingested (not
  re-scored), and written to the stated reader's literacy level.
- **Critic/QA** (MANDATORY) — every step specific and ordered (no generic boilerplate);
  every risk-bearing step has its controls/PPE/checks embedded; the higher-order controls
  the procedure sits within are surfaced; no PPE/admin-only treatment without
  justification; responsibilities + competencies named as roles; emergency provisions
  present; every citation traces to the KB (ISO 45001 8.1; the ingested RA/JSA by id);
  revision/approval block complete; written to the stated literacy level; zero PII
  leaked. PASS/FAIL.

A **short single-task work instruction (Q12)** legitimately stays single-threaded via
the Step-0 triage gate — but it still ships the full identical block, the
De-identifier-first scrub still runs inline, and the A7 `controls` call + the Critic/QA
pass are still made.

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
