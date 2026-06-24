---
name: iso45001-gap-analysis
description: Produces a clause-by-clause ISO 45001 gap analysis and certification-readiness
  assessment for a named organisation or site. Use this skill whenever a user asks
  to assess ISO 45001 readiness, run a gap analysis against ISO 45001, check management-system
  conformance, prepare for a certification or surveillance audit, or score maturity
  against the standard's clauses. It scores each clause's conformance from evidence
  on a 5-level maturity scale, prioritises gaps by risk and certification-blocking
  severity, and produces a costed remediation roadmap with named owners and dates
  — emitted as a branded report. Equally adaptable to ISO 14001 / ISO 45003 via the
  standard selector. Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: ms-admin
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
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# ISO 45001 Gap Analysis

A consultant-grade HSE skill that produces a **clause-by-clause ISO 45001 conformance
gap analysis and certification-readiness assessment** for a **named organisation or
site**, grounded in **ISO 45001:2018** (the full clause set 4–10) and framed by **ISO/IEC
17021-1** certification-audit principles. It scores each clause's conformance from the
supplied evidence on the shared **5-level maturity scale** (`KB-DATA-ISO45001-MATURITY`),
flags any mandatory clause at level ≤ 2 as a **certification-blocker** (never a minor gap),
prioritises gaps by severity × certification-blocking (`KB-SNIP-GAP-PRIORITISATION`), and
produces a **prioritised, costed remediation roadmap** of SMART actions with **named owners
and due dates**. It is equally adaptable to **ISO 14001:2015** / **ISO 45003:2021** via the
standard selector (Q1). It forces the single lever that separates a defensible artifact
from copy-paste paperwork: **no clause silently omitted, every gap traced to a clause +
evidence + a named owner + a date**, and the planning-clause controls ranked up the full
hierarchy of controls — never a vague, PPE-only treatment.

## When to use this skill

Use this skill when the user needs to **assess ISO 45001 readiness or run a gap analysis**
for a **concrete, named organisation or site** — for example "run an ISO 45001 gap analysis
for AcmeCo's Plant 2 ahead of stage-1 certification", "score our management-system
conformance against the standard's clauses", "are we certification-ready / surveillance-audit
ready?", or "map our OH&S maturity clause by clause". Trigger phrases: *ISO 45001 gap
analysis, certification readiness, surveillance-audit prep, management-system conformance,
clause-by-clause maturity, conformance scoring, remediation roadmap*. Use it **also** for an
**ISO 14001** (environmental) or **ISO 45003** (psychosocial) gap analysis via the standard
selector (Q1) — the same clause-walk method, the same maturity scale, the standard's own
clause set. This is **distinct from `safety-audit`** (which classifies findings against an
audit scope): this skill scores **clause conformance** and builds a **costed remediation
roadmap**. If the request is vague ("are we ISO-ready?"), the Workflow intake below **refuses
to score** until the standard, the named scope, and at least one evidence source per major
clause group are captured.

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

<!-- The selector ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). This skill is driven by the STANDARD
     SELECTOR (Q1), not a jurisdiction-law lookup — ISO 45001/14001/45003 are
     jurisdiction-independent management-system standards. rule-9 checks every path/ID
     resolves against the KB registries. -->

**Standard selector (Q1) → read the matching standards fragment + the shared scoring/method snippets:**

| Standard selected (Q1) | Read (the clause set to score against) |
|---|---|
| ISO 45001 (default — OH&S) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — clause set 4–10) |
| ISO 14001 (environmental) | ../../knowledge-base/standards/iso-14001.md (KB-STD-ISO14001 — same clause-walk, environmental clause set) |
| ISO 45003 (psychosocial) | ../../knowledge-base/standards/iso-45003.md (KB-STD-ISO45003 — psychosocial extension of 6.1.2) |
| Combined | read each selected standards fragment above and score each clause set in turn |

Always — for any selected standard — also read the shared scoring + method snippets and
apply them to every clause:

- `../../knowledge-base/data-points/iso45001-maturity.md` (**KB-DATA-ISO45001-MATURITY**) — the
  5-level conformance/maturity scale (0 Absent → 4 Measured); score **every** clause on it,
  quote its `source`+`year`. A mandatory clause at level ≤ 2 is a certification-blocker.
- `../../knowledge-base/prompt-snippets/gap-prioritisation.md` (**KB-SNIP-GAP-PRIORITISATION**) —
  severity × certification-blocking gap ordering; blockers first, then high-severity, then the rest.
- `../../knowledge-base/prompt-snippets/ops-clause-map.md` (**KB-SNIP-OPS-CLAUSE-MAP**) — the
  bundle clause cross-walk; route a user who asks for the wrong artifact for a clause to the owning sibling.
- `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (**KB-SNIP-HOC**) — applied to
  every control in the planning clauses (6.1) and in the remediation roadmap.

This skill always grounds in `KB-STD-ISO45001` (clause set 4–10) and scores every clause on
`KB-DATA-ISO45001-MATURITY`; ISO 14001 / ISO 45003 substitute the standard's own clause set via
the Q1 selector. The rule-9 manifest is `references/_skill-kb.md`. No jurisdiction-law lookup is
needed — these are jurisdiction-independent standards (`jurisdiction: [All]`).

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(Q1 **standard selector** · Q2 named scope/boundary · Q3 current state · Q4 **per-clause-group
evidence** · Q5 target · jurisdiction-context · review cadence · assessor/owners), the
**standard-selector branch** (Q1 = ISO 14001 / ISO 45003 / combined → swap the clause set the
walk scores against), and the **refuse-on-vague anchors** — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo the
captured facts back before any analysis**, and **refuse to score** until the **standard (Q1) +
the named scope (Q2) + at least one evidence source per major clause group (Q4)** are captured
— record `[ASSUMPTION]` / `[GAP]`, never invent a conformance level.

### The clause-walk gap-analysis method (ISO 45001 4–10; ISO 14001/45003 via the Q1 selector)

Full method in `references/METHODOLOGY.md`; the scoring scale is `KB-DATA-ISO45001-MATURITY`
and the prioritisation method is `KB-SNIP-GAP-PRIORITISATION`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Audit interview notes may name individuals
   and disclose conditions; everything downstream consumes only the scrubbed, role-labelled
   text. Supplier/commercial cost data in the roadmap is minimised.
2. **Resolve the standard + assemble the clause set** — from Q1, read the matching standards
   fragment (`KB-STD-ISO45001` default; `KB-STD-ISO14001` / `KB-STD-ISO45003` / combined via
   the selector) and enumerate **every** clause (4 context → 5 leadership → 6 planning → 7
   support → 8 operation → 9 performance evaluation → 10 improvement). **No clause is silently
   dropped** — each is scored or explicitly marked **N/A with a stated reason**.
3. **Score each clause's conformance from evidence** — for every clause, read the Q4 evidence
   and assign a **level 0–4 on `KB-DATA-ISO45001-MATURITY`** (0 Absent → 1 Ad-hoc → 2 Documented
   → 3 Implemented/conformant → 4 Measured & improving), applying the level's **evidence test**.
   A clause with **no evidence is a scored gap (level 0/1), not an omission**. The level is the
   scale's, traced to the evidence — not a prose guess. **Omitting a mandatory clause (e.g.
   6.1.2 hazard-id) fails the analysis.**
4. **Flag certification-blockers** — apply the `KB-DATA-ISO45001-MATURITY` certification-readiness
   rule: any **mandatory clause** (e.g. 5.2 policy, 6.1.2 hazard-id, 9.2 internal audit, 10.2
   incident/nonconformity) sitting at **level ≤ 2** is a **certification-blocker**, flagged
   explicitly in the gap register — **never downgraded to a minor gap**. This is the hard
   defensibility/`regulatory_citation_accuracy` enforcement of the core value.
5. **Classify & prioritise the gaps** — apply `KB-SNIP-GAP-PRIORITISATION`: classify each gap on
   **severity** (required − current maturity × the risk the clause governs) **and
   certification-blocking**; **prioritise blockers first** (by severity), then high-severity
   non-blockers, then the rest. Every gap traces to its **clause + a named owner**.
6. **Apply the hierarchy of controls to the planning clauses** — where clause 6.1 (planning /
   risk & opportunity) controls are assessed, rank them via **`KB-SNIP-HOC`** (Elimination →
   Substitution → Engineering → Administrative → PPE); a PPE/admin-only remediation with no
   higher-order option and no justification is a **defect the Critic/QA pass must catch**.
7. **Build the costed remediation roadmap (named owners + dates)** — turn each prioritised gap
   into a **SMART action** (specific, measurable, **assignable (named owner)**, relevant,
   **time-bound (ISO due date)**) via `smart_actions.validate_register`, **cost-estimated** and
   ordered blockers-first. Any action missing an owner, a valid date, a measure, or a clause
   link is **invalid** and must be fixed — no anonymous actions, no "ASAP".
8. **Validate against `references/QUALITY_CHECKLIST.md`** — every clause scored or N/A-with-reason;
   every gap traced to a clause + evidence + owner; every certification-blocker explicitly flagged;
   every clause/standard citation traced to the KB (no invented clause reference); de-id applied;
   no conformance level asserted on an unstated assumption.
9. **Assemble the branded report** — build `report.json` (see
   `assets/iso45001-gap-analysis-report.template.json`) and run the canonical `report-output`
   call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **conformance scoring (step 3) is a structured
rubric over the clause map, not a calculation — there is no scoring engine**; `smart_actions`
is the only A7 script call (step 7, the roadmap).

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

This is the **moderate-to-complex roster** (A6 "complex = 4–6") — a full management-system
review fans out **by clause group**, the heaviest fan-out in the bundle but **still within
MAX=6**. The **De-identifier is the sequential first gate** (not a fan-out peer); the
**Clause-Group-Assessors (3–6)** run in parallel; the **Roadmap-Synthesizer** consolidates;
**SME Reviewer** and **Critic/QA** are mandatory. **Conformance scoring is NOT a subagent** —
it is the structured `KB-DATA-ISO45001-MATURITY` rubric each assessor applies. Archetypes:
`KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub every name,
  disclosed condition, exact date/location, and any <5 personnel cell from the audit interview
  notes to role labels before any analysis (every assessor below consumes scrubbed text only).
- **Clause-Group-Assessor · Leadership & Planning** — score clauses **4 (context) · 5
  (leadership, incl. 5.2 policy) · 6 (planning, incl. 6.1.2 hazard-id, 6.1.3 legal)** on
  `KB-DATA-ISO45001-MATURITY` from the scrubbed evidence; flag any mandatory clause at level ≤ 2
  as a certification-blocker; rank 6.1 controls via `KB-SNIP-HOC`. SCOPE-OUT: support/operation
  clauses (the next assessor), the roadmap (Roadmap-Synthesizer).
- **Clause-Group-Assessor · Support & Operation** — score clauses **7 (support: 7.2 competence,
  7.3 awareness, 7.4 communication, 7.5 documented info) · 8 (operation: 8.1 controls, 8.1.4
  contractors, 8.2 emergency)**; same scale, same blocker rule. SCOPE-OUT: leadership/planning
  (prior assessor), performance/improvement (next assessor).
- **Clause-Group-Assessor · Performance Evaluation & Improvement** — score clauses **9
  (9.1 monitoring/measurement, 9.1.2 compliance evaluation, 9.2 internal audit, 9.3 management
  review) · 10 (improvement: 10.2 incident/nonconformity, 10.3 continual improvement)**; same
  scale, same blocker rule. SCOPE-OUT: the earlier clause groups, the roadmap.
- **Roadmap-Synthesizer** — consolidate the three assessors' clause scores into one
  conformance matrix, classify + prioritise the gaps via `KB-SNIP-GAP-PRIORITISATION`
  (blockers first), and build the **costed SMART remediation roadmap** with named owners +
  dates via `smart_actions`. SCOPE-OUT: re-scoring a clause (the assessors own the levels),
  checking de-id (Critic/QA).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Lead Auditor / Management-Systems Consultant) before any
  output: no clause silently omitted, every certification-blocker correctly flagged (not
  downgraded), every gap traced to clause + owner, the roadmap ordered blockers-first.
- **Critic/QA** (MANDATORY) — every clause scored or N/A-with-reason, every blocker flagged,
  every roadmap action owned + dated + clause-linked, no PPE/admin-only remediation without
  justification, every clause/standard citation traces to the KB, zero PII/health leak. PASS/FAIL.

For a **narrow single-clause check** (e.g. "are we conformant on 6.1.2 only?") the skill runs
**single-threaded** — no clause-group fan-out — but the de-id scrub, the `KB-DATA-ISO45001-MATURITY`
scoring, and the SME + Critic/QA passes are still made. The three Clause-Group-Assessors may
split further (up to 6) for a large multi-site management system, never exceeding MAX=6.

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
