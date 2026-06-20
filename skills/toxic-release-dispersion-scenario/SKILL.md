---
name: toxic-release-dispersion-scenario
description: 'Frame toxic-release / dispersion scenarios — source term, release mode,
  receptors, and a consequence band — as structured input for a competent-person bowtie
  / LOPA / QRA study. It does NOT run quantitative dispersion modelling (no PHAST
  / ALOHA) and does NOT invent dispersion distances or concentrations; un-modelled
  values are recorded as [GAP] and the consequence side is developed with the bowtie-builder
  and lopa-worksheet. Use it to structure a release scenario, prepare dispersion input
  for a study, or frame the consequence side of a bowtie. Assistive decision-support:
  it structures the scenario for a competent team, never an autonomous quantitative
  result, which a competent person must produce and review.'
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
  - Chem
  - Process
  jurisdiction:
  - All
  status: assistive
  plugin: hse-chemicals
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Toxic Release Dispersion Scenario

An **assistive** (Tier-4) skill that frames toxic-release / dispersion **scenarios** — source term, release mode, receptors, and a consequence band — as structured input for a competent-person bowtie / LOPA / QRA. It **does NOT run quantitative dispersion modelling** (no PHAST, no ALOHA) and **does NOT invent dispersion distances or concentrations**: un-modelled values are recorded as `[GAP]`, and the consequence side is developed with the **`bowtie-builder`** and **`lopa-worksheet`** (grounded in `KB-STD-CCPS-BOWTIE` / `KB-STD-IEC-61511`). It structures the scenario for the team; it is never an autonomous quantitative result. `risk_matrix` provides the consequence band only.

## When to use this skill

Use this skill to structure a toxic-release scenario, prepare dispersion input for a study, or frame the consequence side of a bowtie/LOPA — for a named substance + inventory + release scenario. It is assistive: it frames input for a competent-person study, it does not produce a modelled dispersion result. If the request asks for a quantitative distance/concentration, it records `[GAP]` and hands to the modelling team.

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
| UK/EU | ../../knowledge-base/standards/dsear-atex.md (KB-STD-DSEAR) + standards/ccps-bowtie.md |
| Any   | ../../knowledge-base/standards/ccps-bowtie.md (KB-STD-CCPS-BOWTIE — consequence side via `bowtie-builder`) + standards/iec-61511.md (KB-STD-IEC-61511 — `lopa-worksheet`) |
| Any   | ../../knowledge-base/prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) for mitigative barriers |
| Unknown | Ask before citing any specific law |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**Run the full structured intake in `references/intake.md`** — the typed/branched
Q-table, its intake-coverage manifest, the echo-back, and the refuse-on-vague anchors
live there. This skill is **assistive-only and the most omit-heavy in the family** (its
short `omits` list is correct by design). It elicits the released substance + CAS +
inventory at risk (refuse "a toxic gas"), physical state + storage P/T, the release
scenario, whether a release rate is **supplied or `[GAP]` for the modeller** (never
computed here), the toxicity benchmark, the release/receptor geometry + weather, the
receptors, and the target study. **Echo back that the output is scenario framing for a
competent-person study / modelling, NOT a quantitative result.** It records `[GAP]` for
any un-modelled value, hands the consequence side to **`bowtie-builder`** /
**`lopa-worksheet`** by name, never runs PHAST/ALOHA or invents a dispersion figure;
`risk_matrix` gives a qualitative consequence band only.

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

For a non-trivial task the triage gate may fan out to:

- **Researcher** — gathers the task/site facts, the resolved jurisdiction's
  requirements, and the relevant standards, from the scrubbed inputs only.
- **Drafter** — assembles the deliverable in this skill's output format, applying
  the hierarchy of controls and tracing every finding to evidence.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety
  output: specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the skill-specific
  persona, domain checklist, and boundary in `references/sme-review.md`
  (consequence-modelling / dispersion specialist lens: is this honest SCENARIO FRAMING
  for the modelling team — source term captured not computed, no invented distance /
  concentration, downstream owners named). Decision-support only; precedes — never
  replaces — the human competent-person review.

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
