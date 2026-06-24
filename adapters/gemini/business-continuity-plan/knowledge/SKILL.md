---
name: business-continuity-plan
description: 'Produces an ISO 22301 business continuity plan for a named organisation
  — business impact analysis, recovery objectives (RTO/RPO/MTPD), continuity strategies,
  and a plan with named recovery roles. Use this skill whenever a user asks to write
  a business continuity plan, BCP, BIA, disaster-recovery or resilience plan, or to
  set RTO/RPO recovery objectives. It runs a BIA to find time-critical activities
  and their dependencies, derives RTO/RPO within the MTPD (RTO < MTPD, never asserted
  alone), selects continuity strategies, and documents the plan with named owners,
  deputies, and review dates — emitted as a branded report. It complements (not duplicates)
  the emergency-response-plan: ERP handles the incident response; BCP handles continuity
  of critical activities. Decision-support only; a competent person must review the
  output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: ms-admin
  tier: 3
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
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Business Continuity Plan

A consultant-grade HSE skill that produces a named-organisation **ISO 22301 business
continuity plan**: it runs a **Business Impact Analysis (BIA)** to find the time-critical
activities and their dependencies, derives **recovery objectives** — MTPD, then **RTO
strictly inside that MTPD** (never an RTO asserted alone) plus an **RPO** — per critical
activity, selects **continuity strategies** that cover every stated dependency, and
documents the plan with **named recovery roles, deputies, an exercise/test schedule, and
review dates**. It forces the single lever that separates a defensible artifact from
copy-paste paperwork: **specificity** — every RTO/RPO/strategy traced to the BIA's
evidence with an owner and a recovery role; preventive continuity controls are ranked by
the **hierarchy of controls** (`KB-SNIP-HOC`), never a token treatment. Grounded in
`KB-STD-ISO22301` (clauses 8.2.2 BIA · 8.2.3 risk assessment · 8.3 strategies · 8.4 plans
· 8.5 exercise programme). It **complements, never duplicates,** `emergency-response-plan`
— ERP owns the immediate incident response (muster, evacuation, scenario procedures); BCP
owns continuity of critical activities after the incident is controlled.

## When to use this skill

Use this skill when the user needs a **business continuity plan for a named organisation,
site, or function** — for example "write a BCP for our claims-processing operation", "run
a BIA and set RTO/RPO for the order-fulfilment function", "build a disaster-recovery /
resilience plan for the data centre", or "what's our MTPD for payroll and what continuity
strategy covers a single-supplier dependency?". Trigger phrases: *business continuity
plan, BCP, BIA, business impact analysis, RTO, RPO, MTPD, recovery objectives, continuity
strategy, disaster recovery, resilience plan*.

**BCP vs ERP (the D-07 boundary — disambiguate at intake Q1).** If the request is about
the **immediate incident response** — fire/evacuation, muster points, the call-out tree,
scenario response procedures, emergency drills — that is **`emergency-response-plan`**, not
this skill; route there. This skill owns the *continuity* leg: **critical activities,
MTPD/RTO/RPO, dependencies, recovery strategies, recovery roles**. The two are adjacent and
cross-referenced, never merged. If the request is vague ("write me a continuity plan"), the
Workflow intake below **refuses to proceed** until the named critical activities and their
dependencies are captured.

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

<!-- The rows below live BELOW the :end marker: per-skill, presence-only (rule-2
     presence check, never byte-diffed). rule-9 checks every path/ID resolves against
     the KB registries. The rule-9 reference manifest is references/_skill-kb.md. -->

This skill is grounded in a **jurisdiction-independent management-system standard** — ISO
22301 carries no national forms — so the table below is a **fragment-resolution map**, not
a jurisdiction selector. Read **only** the fragment a given step needs:

| What you need | Read (fragment) |
|---|---|
| ISO 22301 clause → artifact map (BIA · RTO · RPO · strategies · plans · exercise) | ../../knowledge-base/standards/iso-22301.md (KB-STD-ISO22301) |
| The BIA → impact-over-time → MTPD → RTO/RPO derivation method | ../../knowledge-base/prompt-snippets/bia-method.md (KB-SNIP-BIA-METHOD) |
| Recovery-objective banding + the **RTO < MTPD** margin discipline | ../../knowledge-base/data-points/rto-rpo-guidance.md (KB-DATA-RTO-RPO-GUIDANCE) |
| Which hse-operations sibling owns an adjacent ISO 45001 operations clause | ../../knowledge-base/prompt-snippets/ops-clause-map.md (KB-SNIP-OPS-CLAUSE-MAP) |
| The hierarchy of controls for any **preventive** continuity control | ../../knowledge-base/prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |

This skill **always** grounds in `KB-STD-ISO22301` and follows `KB-SNIP-BIA-METHOD`; it
**reuses the Phase-11-shipped `KB-STD-ISO22301`** and never re-authors it. The **RTO < MTPD
rule is a checklist constraint** (`KB-DATA-RTO-RPO-GUIDANCE`, `references/QUALITY_CHECKLIST.md`),
not a deterministic engine. For continuity of the *incident-response* leg, the BIA method
itself carries a one-line cross-reference to **`emergency-response-plan`** — BCP complements,
never duplicates, the ERP (`KB-SNIP-OPS-CLAUSE-MAP`, D-07). For a specific jurisdiction's
statutory continuity duty (e.g. India Factories Act s.41B on-site emergency plan for MAH
installations), ask the user before citing any specific law.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table, the
**BCP-vs-ERP disambiguation at Q1**, the echo-back, and the refuse-on-vague anchors — lives
in **`references/intake.md`**. Run it one question at a time, branch on the answers, **echo
the captured facts back before any analysis**, and **refuse to proceed on a vague scope**.
The five domain questions:

1. **Q1 — Scope (free-text, the specificity anchor + BCP-vs-ERP gate).** The named
   organisation / site / function this BCP covers. **First disambiguate:** if the user
   actually wants the *immediate incident response* (muster, evacuation, scenario
   procedures, the call-out tree, emergency drills), **route to `emergency-response-plan`**
   and stop — that is the ERP, not the BCP. This skill owns *continuity of critical
   activities* (critical activities / RTO / RPO / MTPD / recovery). **Refuse a generic
   scope** ("the whole company" with no named function).
2. **Q2 — Critical activities + their outputs (free-text list).** The time-critical
   activities and what each must keep producing. This **drives the BIA**; refuse to set any
   recovery objective until these are captured.
3. **Q3 — Disruption scenarios (multi-select):** loss of site · loss of IT · loss of key
   supplier · loss of key staff · utility failure — branch per selected scenario.
4. **Q4 — Current recovery capability (MCQ):** none / informal / documented-DR /
   tested-BCP.
5. **Q5 — Objectives basis (free-text):** any known MTPD/RTO/RPO, and the **dependencies**
   (people · IT/systems · suppliers · premises · equipment) per critical activity. **RTO
   must be derived under a stated MTPD, never asserted alone** (`KB-DATA-RTO-RPO-GUIDANCE`).

**Refuse-on-vague anchor:** no recovery objectives until the **named critical activities
and their dependencies** are captured; an RTO with no stated MTPD basis, or RTO ≥ MTPD, is
invalid.

Then: run the BIA method (`references/METHODOLOGY.md` / `KB-SNIP-BIA-METHOD`) → validate the
draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format
section below.

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

This is the **STANDARD moderate roster** (A6 "moderate = 2–4"). The **De-identifier is the
sequential first gate** (not a fan-out peer); the fan-out jobs are **BIA-Analyst →
Strategy-&-Objectives → Plan-Assembler**; **SME Reviewer + Critic/QA are mandatory**.
Archetypes: `KB-SNIP-ARCHETYPES`. The exercise/test schedule and recovery actions are
**`smart_actions`** calls (owners + ISO dates), not a fan-out job.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all
  PII/health detail into role labels before any analysis. **Recovery roles legitimately
  name individuals**, but a recovery-role holder's **home address / medical note** must
  never enter a shared copy — role-label it (every fan-out job below consumes scrubbed text).
- **BIA-Analyst** — from the scrubbed inputs, identify the **critical activities + their
  outputs**, map **impact over time** to derive each **MTPD**, and capture every
  **dependency** (people · IT · suppliers · premises · equipment); flag `[GAP]`.
  SCOPE-OUT: setting RTO/RPO or strategies (Strategy-&-Objectives owns it).
- **Strategy-&-Objectives** — derive **RTO strictly under the stated MTPD (with margin) +
  RPO** per activity (`KB-DATA-RTO-RPO-GUIDANCE` — an RTO with no MTPD basis, or RTO ≥ MTPD,
  is invalid), and select **continuity strategies covering every stated dependency**;
  preventive controls ranked via `KB-SNIP-HOC`. SCOPE-OUT: the BIA (BIA-Analyst), assembling
  the plan (Plan-Assembler).
- **Plan-Assembler** — assemble the plan: **recovery roles each with a deputy**, the
  **exercise/test schedule** (`smart_actions`, owners + ISO dates), the review cycle, and
  the **one-line cross-reference to `emergency-response-plan`** for the incident-response
  leg (BCP complements, does not duplicate, the ERP). SCOPE-OUT: deriving objectives
  (Strategy-&-Objectives).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (**Business Continuity Manager (ISO 22301)**): every RTO
  under a stated MTPD, every strategy covering the stated dependencies, every recovery role
  with a deputy, an exercise schedule present, and no recovery-role personal detail in a
  shared copy.
- **Critic/QA** (MANDATORY) — adversarial final pass: every recovery objective traced to the
  BIA, no RTO ≥ MTPD / no RTO without an MTPD basis, every dependency covered by a strategy,
  every citation traces to `KB-STD-ISO22301`, and ZERO PII/health leak. PASS/FAIL.

Simple single-function plans run single-threaded — no subagents — but the `smart_actions`
call and the SME + Critic/QA passes are still made.

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
