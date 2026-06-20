---
name: icmm-critical-control-management
description: 'Structures ICMM Critical Control Management for a material unwanted
  event in a mine — identifies the critical controls, sets performance requirements,
  verification activities + frequencies, and accountabilities, and frames the bowtie
  via the shared bowtie-builder facilitator (referenced, not re-authored). It authors
  the mining CCM overlay (criticality, the principal-hazard taxonomy) itself. Use
  it to set up critical-control management for a mining principal hazard or structure
  a CCM workshop. Assistive: it structures the workshop and never an autonomous artifact
  — a competent mine team owns the engineering judgement and the live verification.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: process-safety
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

# Icmm Critical Control Management

An **assistive** (Tier-4) skill that structures **ICMM Critical Control Management (CCM)** for a **material unwanted event** in a mine: it identifies the **critical controls** (the controls that, if they fail or are absent, allow the event), sets **performance requirements + verification activities + frequencies + accountabilities**, and hierarchy-ranks the controls (`controls`, critical ones flagged). For the **bowtie diagram itself** (top event -> threats/barriers -> consequences, barrier performance standards) it **references the shared `bowtie-builder` facilitator** (owned by hse-process, bundled into hse-mining via `KB-STD-CCPS-BOWTIE`) — it does **NOT** re-author a bowtie engine. It authors the mining CCM overlay itself (criticality, the principal-hazard taxonomy in `KB-STD-ICMM-CCM` / `KB-DATA-MINING-HAZARDS`). It **structures the workshop, never an autonomous artifact** — a competent mine team owns the engineering judgement and the live verification.

## When to use this skill

Use this skill to set up **critical-control management** for a mining principal hazard, structure a CCM workshop, or define verification activities for critical controls — for a named material unwanted event. It is **assistive**: it frames and records the team's CCM decisions, it is never an autonomous artifact. For the bowtie diagram it points you at **`bowtie-builder`** by name. If the request is vague, the Workflow intake forces the specific unwanted event first.

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
| Any | ../../knowledge-base/standards/icmm-ccm.md (KB-STD-ICMM-CCM — CCM framing + principal-hazard taxonomy) |
| Any | ../../knowledge-base/standards/ccps-bowtie.md (KB-STD-CCPS-BOWTIE — bowtie technique, developed via `bowtie-builder`) |
| Any | ../../knowledge-base/data-points/mining-hazards.md (KB-DATA-MINING-HAZARDS) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) + standards/iso-45001.md (KB-STD-ISO45001) |
| Unknown | Ask before framing the material unwanted event |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open; one question at a time, branch on the answers, echo the captured facts before any structuring; refuse on a vague subject and never invent (`KB-SNIP-INTAKE`).

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched Q-table — the commodity × mine-type branch driver, the MUE
selection, the per-control performance / verification / accountability loop (Q5→Q6→Q7),
the criticality-scheme confirm, the echo-back and the refuse-on-vague anchors — lives in
**`references/intake.md`** (self-contained; it shares ~80% of its surface with
`principal-hazard-management-plan` per D-04 but is kept as a separate file). Must-ask
dimensions: the **commodity / mine type** (sets the candidate MUE set + control families),
the **nominated critical controls + their performance/verification evidence**, and the
**verification accountability role**. Then (CCM structure, `KB-STD-ICMM-CCM`): identify the
critical controls (those that, if absent/failed, allow the event), hierarchy-rank via
`controls` (`KB-SNIP-HOC`) — a PPE/admin-only 'critical control' for a principal hazard is
flagged, not accepted; set **performance + verification activity + frequency +
accountability** per control; **reference `bowtie-builder`** by name (do NOT re-author it).
Where the team has not supplied performance evidence, record `[GAP]` — never fabricate an
engineering value. Validate against `references/QUALITY_CHECKLIST.md`, then produce the CCM
register. This is workshop structuring for the team, not an autonomous result.

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

**Step 4 — SME review & sign-off (MANDATORY, before any output):** run the skill-specific
SME persona sign-off in **`references/sme-review.md`** (the ICMM critical-control-management
practitioner, with the assistive autonomy test) — model QA, decision-support, FLAGs
non-blocking; workshop-structuring only, it never replaces the mine team's engineering
judgement nor the competent-person sign-off.

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
