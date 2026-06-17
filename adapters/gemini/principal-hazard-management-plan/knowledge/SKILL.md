---
name: principal-hazard-management-plan
description: 'Structures a principal-hazard management plan (PHMP) for a named mining
  principal hazard — ground/strata failure, inrush, fire/explosion, ventilation, mobile-plant
  interaction and others: hazard analysis, a hierarchy-ranked control suite, critical-control
  linkage to ICMM CCM, and monitoring. Use it to develop a PHMP for a mine''s principal
  hazard or structure the PHMP workshop. Assistive: it structures the multidisciplinary
  workshop and never an autonomous artifact — the mine team owns the engineering judgement.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 4
  audience:
  - M
  - C
  industry:
  - Min
  jurisdiction:
  - All
  status: assistive
  plugin: hse-mining
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Principal Hazard Management Plan

An **assistive** (Tier-4) skill that structures a **principal-hazard management plan (PHMP)** for a **named mining principal hazard** — ground/strata failure, inrush, fire/explosion, ventilation failure, mobile-plant interaction, fall from height, hazardous energy or respirable dust: hazard analysis (HIRA structure + `risk_matrix`), a **hierarchy-ranked control suite** (`controls`, critical controls flagged), **critical-control linkage to ICMM CCM** (`icmm-critical-control-management`), and monitoring (`smart_actions`). It grounds in `KB-STD-ICMM-CCM` / `KB-DATA-MINING-HAZARDS`. It **structures the multidisciplinary workshop, never an autonomous artifact** — the mine team owns the engineering judgement.

## When to use this skill

Use this skill to develop a **PHMP** for a mine's principal hazard or structure the PHMP workshop — for a named principal hazard. It is **assistive**: it frames and records the team's analysis, never an autonomous plan. It builds on `icmm-critical-control-management` for the critical-control linkage. If the request is vague, the Workflow intake forces the named principal hazard first.

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

| Jurisdiction | Read |
|---|---|
| Any | ../../knowledge-base/data-points/mining-hazards.md (KB-DATA-MINING-HAZARDS — principal-hazard library) |
| Any | ../../knowledge-base/standards/icmm-ccm.md (KB-STD-ICMM-CCM — critical-control linkage) |
| Any | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — 6.1.2 HIRA) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before naming the principal hazard |

## Workflow

Open with a **structured multi-step intake** (`KB-SNIP-INTAKE`) — one question at a time, branch, echo the captured facts before any structuring.

1. **Principal hazard** — MCQ from `KB-DATA-MINING-HAZARDS`: strata failure · inrush · fire/explosion · ventilation failure · mobile-plant interaction · fall from height · hazardous energy · respirable dust.
2. **Mine context** — free-text: the specific mine and the hazard scenario.

Then (PHMP structure):
- Run the **HIRA structure** for the named hazard; risk-rate on the org matrix (`risk_matrix`).
- Build the **control suite** hierarchy-ranked (`controls` / `KB-SNIP-HOC`), critical controls flagged; a PPE/admin-only treatment of a principal hazard is flagged, not accepted.
- **Link the critical controls** to the ICMM CCM (`icmm-critical-control-management` / `KB-STD-ICMM-CCM`) — performance + verification carried over.
- Define **monitoring** with owner + due date (`smart_actions`).

Where the team has not supplied an engineering value, record `[GAP]` — never fabricate. Validate against `references/QUALITY_CHECKLIST.md`, then produce the PHMP via the Output format section. This is workshop structuring for the team, not an autonomous plan.

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
