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
## Knowledge base

Read exactly ONE matching knowledge-base fragment per invocation. Resolve it from
the `(jurisdiction × industry × audience)` facets declared in this skill's
`metadata`; if the matching fragment is unknown or ambiguous, ASK the user one
clarifying question rather than guessing. Whatever the jurisdiction, ALWAYS apply
the hierarchy of controls (eliminate → substitute → engineer → administrate →
PPE) — never a PPE-only treatment.

<!-- PLACEHOLDER → A3 Phase 2: the jurisdiction resolution ROWS below are a
     byte-identical Phase-1 placeholder. A3 fills the `(law, state) → fragment`
     rows via `hse-skill-forge --sync`; this header + rubric are FINAL. -->

| Jurisdiction | Knowledge-base fragment to read |
| ------------ | ------------------------------- |
| (rows resolved by A3) | `../../knowledge-base/<facet>/<fragment>.md` |
<!-- hse:block:kb-selection:end -->

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
## Agentic Execution

This block governs **runtime fan-out** (decomposing the work of a single
invocation). It is platform-neutral: it never names a host API, only the pattern.

**Step 0 — Triage gate.** First judge the work. Map complexity to a subagent
budget, with MAX=6 fixed: simple → 0 subagents (single-threaded); moderate → 2–3
subagents; complex → 4–6 subagents. Never exceed MAX=6.

**Fan-out contract (when the triage gate calls for subagents).** For each job:
spin up a subagent with **fresh context**; **paste in all the context it needs**
(it cannot see this conversation); state its **scope-in / scope-out** explicitly
and name the sibling jobs so work is not duplicated; require a **bounded, cited
output** (findings traced to evidence, within a stated effort budget); then
**synthesize** the returned outputs into one coherent artifact.

**If your host has no subagent capability, execute each job sequentially in this
same context — keep the scope discipline and the required Critic/QA pass.**

**Critic/QA pass is mandatory** for any regulatory/safety/legal output (every
skill in this pack): after synthesis, run a dedicated critic that checks
specificity, the hierarchy of controls, defensibility, de-identification, and
citation accuracy before the artifact is returned.
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

<!-- hse:block:report-output:start -->
## Output format

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
