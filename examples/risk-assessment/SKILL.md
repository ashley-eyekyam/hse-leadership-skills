---
name: risk-assessment
description: >
  Produce a task- and site-specific HIRA with a calibrated risk matrix, the
  hierarchy of controls, an ALARP justification, named owners, and a review date.
  Use when a manager, consultant, or supervisor needs a defensible risk assessment
  for a specific work task, site, or activity — never for generic or template-only
  output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: "1.0"
  category: risk-assessment
  tier: 1
  audience: [M, C, F]
  industry: [All]
  jurisdiction: [All]
  status: stable
  plugin: hse-core
  hse_reviewed_by: ""
  hse_reviewed_date: ""
---

# Risk Assessment (HIRA)

A consultant-grade HSE skill that produces a defensible Hazard Identification &
Risk Assessment for a named task, site, or asset. It forces the single lever that
separates a defensible artifact from copy-paste paperwork: task/site specificity
plus the full hierarchy of controls — never a vague, PPE-only treatment.

## When to use this skill

Use this skill when the user needs a risk assessment for a concrete task, site, or
asset — for example "assess the risk of working at height on the Site-X roof",
"HIRA for confined-space entry into Tank-3", or "risk-assess the new packing line".
If the request is vague ("write me a risk assessment"), the Workflow intake below
forces the task/site/asset specifics before any drafting begins, so the output is
always traceable to a real activity rather than a generic template.

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

<!-- Per-skill jurisdiction rows (below :end — presence-only, never byte-diffed).
     This HIRA skill grounds in ISO 45001 6.1.2 regardless of jurisdiction; for an
     India site it resolves the state via in-state-forms.md (mandatory state
     detection). references/_skill-kb.md is the rule-9 manifest. -->

| Jurisdiction | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 HIRA) and applies
`KB-SNIP-HOC`; for an India site it resolves the state via `KB-REG-IN-STATEFORMS`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is
enumerable, free-text where it is open. Ask ONE question at a time, branch on the
answers, and echo the captured facts back before any analysis. Never proceed on
vague or missing inputs; this intake is the operational core of *forcing
specificity*. (Intake is a Workflow convention, not a sixth block.)

For this skill, the intake captures, one question at a time:

1. **Task / activity** (free-text) — the specific job being assessed.
2. **Site / asset** (free-text) — where it happens; the named location or asset.
3. **Hazard categories present** (MCQ, multi-select) — e.g. work-at-height,
   confined space, manual handling, electrical, chemical, mechanical, thermal,
   noise, vehicle/plant movement, psychosocial.
4. **Workers exposed & duration** (free-text) — roles (de-identified) and exposure.
5. **Existing controls already in place** (free-text) — so residual risk is real.

Then apply the domain method (see `references/METHODOLOGY.md`):

- Identify hazards for the named task/site (never a generic checklist alone).
- Score each hazard on the calibrated risk matrix (likelihood × severity) to an
  **initial** risk rating.
- For every hazard, walk the **full hierarchy of controls** in order — eliminate →
  substitute → engineer → administrate → PPE — and record the chosen controls; a
  PPE-only treatment is rejected by the quality gate.
- Re-score each hazard to a **residual** risk rating after controls; justify ALARP.
- Assign a **named owner** and a **target/review date** to every action.

Validate the draft against `references/QUALITY_CHECKLIST.md` before output: every
finding traced to evidence, no vague controls, no PPE-only treatment, residual risk
justified, owners and dates present. Then produce the output via the Output format
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

For a multi-hazard or complex assessment, the triage gate may fan out to:

- **Risk Scorer** — applies the calibrated risk matrix to each identified hazard,
  producing initial and residual ratings.
- **Control Adviser** — walks the full hierarchy of controls per hazard and
  rejects any PPE-only treatment.
- **Regulatory Checker** — verifies the controls against the resolved
  jurisdiction's applicable requirements.
- **Critic/QA** — mandatory final pass for any regulatory/safety output, checking
  specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.

Simple single-hazard assessments run single-threaded — no subagents.

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

- `references/METHODOLOGY.md` — the HIRA method this skill applies.
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
