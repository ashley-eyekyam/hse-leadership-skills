---
name: reactive-dust-explosion-assessment
description: Assess reactive-chemistry hazards and combustible-dust / explosive-atmosphere
  risk and produce a DSEAR-/NFPA-/ATEX-aligned basis of safety with area zoning. Use
  it to run a dust hazard analysis (DHA), assess reactive chemistry or incompatibility,
  classify a hazardous area into ATEX zones, or set the basis of safety for a flammable
  atmosphere. Dust parameters (Kst/Pmax/MIE/MIT) are resolved with source+year or
  flagged [GAP], never invented; the structured reactive/deflagration study is handed
  to the hazop-facilitator; controls are hierarchy-of-controls ranked (eliminate/substitute
  and inherently-safer design before engineering, engineering before admin/PPE). Decision-support
  only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: process-safety
  tier: 2
  audience:
  - M
  - C
  industry:
  - Chem
  - Process
  jurisdiction:
  - All
  status: stable
  plugin: hse-chemicals
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Reactive Dust Explosion Assessment

A consultant-grade skill that assesses reactive-chemistry hazards and combustible-dust / explosive-atmosphere risk and produces a DSEAR-/NFPA-/ATEX-aligned **basis of safety** with area zoning. It runs the Dust Hazard Analysis elements (`KB-STD-NFPA-652`/`660`), resolving the dust parameters (Kst/Pmax/MIE/MIT) with source+year or `[GAP]` (never invented), sets the DSEAR basis of safety and the ATEX zone + EPL (`KB-STD-DSEAR`/`KB-STD-ATEX`), bands consequence with `risk_matrix`, and HoC-ranks controls with `controls`. The structured reactive / deflagration study is handed to the **`hazop-facilitator`** (HAZOP/DHA node input) — this skill frames the nodes, it does not run the workshop.

## When to use this skill

Use this skill to run a Dust Hazard Analysis (DHA), assess reactive chemistry/incompatibility, classify a hazardous area into ATEX zones, or set a basis of safety for a flammable atmosphere — for a named process/material and area. If the request is vague, the intake forces the material, hazard scope, available test data and the area to be zoned.

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

| Jurisdiction | Read |
|---|---|
| UK/EU | ../../knowledge-base/standards/dsear-atex.md (KB-STD-DSEAR basis of safety + KB-STD-ATEX zoning) |
| USA   | ../../knowledge-base/standards/nfpa-652-660.md (KB-STD-NFPA-652/660 DHA) + us-osha.md |
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md) + standards/nfpa-652-660.md |
| Any   | ../../knowledge-base/standards/nfpa-652-660.md (DHA + dust parameters) + standards/dsear-atex.md + prompt-snippets/hierarchy-of-controls.md |
| Process/dust (any) | ../../knowledge-base/standards/iec-61882.md (KB-STD-IEC-61882 — hand the reactive/deflagration nodes to `hazop-facilitator`) |
| Unknown | Ask before citing any specific law |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

For a reactive / dust-explosion assessment the intake elicits the material and scope BEFORE any basis of safety:

1. **Process / material** — the named process and material(s) (free-text; specific).
2. **Hazard scope** — MCQ: reactive chemistry / combustible dust / explosive vapour atmosphere / combination. Branches to DSEAR vs NFPA 652·660 vs ATEX rows.
3. **Available test data** — MCQ: have Kst/Pmax/MIE/MIT (with lab source) / `[GAP]`. **`[GAP]` → the parameter is not invented; route to testing.**
4. **Area for zoning** — the area/equipment to classify (free-text).
5. **Jurisdiction** — DSEAR/ATEX (UK/EU) vs NFPA (US) emphasis.

Echo material + hazard scope + data availability + area back before setting the basis of safety. Dust parameters are resolved with source+year or `[GAP]`; the **reactive/deflagration study is handed to `hazop-facilitator`** (grounded in `KB-STD-IEC-61882`); controls are HoC-ranked — eliminate/substitute and inherently-safer design before engineering, engineering before admin/PPE.

Then: analyse / apply the domain method → validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. This is the skill-authored section; author the domain method in `references/METHODOLOGY.md`.

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

For a non-trivial task the triage gate may fan out to:

- **Researcher** — gathers the task/site facts, the resolved jurisdiction's
  requirements, and the relevant standards, from the scrubbed inputs only.
- **Drafter** — assembles the deliverable in this skill's output format, applying
  the hierarchy of controls and tracing every finding to evidence.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety
  output: specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.

Simple single-subject tasks run single-threaded — no subagents.

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
