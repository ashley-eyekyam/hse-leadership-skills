---
name: aviation-spi-spt-framework
description: 'Design a Safety Performance Indicator (SPI) and Safety Performance Target
  (SPT) framework per the ICAO Annex 19 Safety Assurance pillar: define leading/lagging
  SPIs, set alert and target levels, and map each SPI to an owning hazard or safety
  objective. Use this skill to build or review an SPI/SPT framework for a named operator,
  airport, or AMO, or to align SPIs to a State Safety Programme''s acceptable level
  of safety performance (the DGCA SSP in India). Grounds in KB-STD-ICAO-ANNEX19, uses
  incident_rates for trend context, forces every SPI to carry a defined threshold
  and an owner, and never invents performance figures. Decision-support only; a competent
  person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: performance
  tier: 2
  audience:
  - M
  - E
  - C
  industry:
  - Avi
  jurisdiction:
  - All
  status: stable
  plugin: hse-aviation
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Aviation SPI / SPT Framework

The **Safety Performance Indicator / Target** skill (ICAO Annex 19 Pillar 3 — Safety Assurance). For a named operator, airport, or AMO it designs a set of **leading and lagging SPIs**, sets each one an **alert level and a target level**, and **maps every SPI to an owning hazard or safety objective** — so safety performance is monitored against defined thresholds, not a vibe. Trend context comes from the shared A7 `incident_rates` engine; performance figures are never invented. Where the jurisdiction is India the framework aligns SPIs to the **DGCA SSP**'s acceptable-level-of-safety-performance (ALoSP) expectations (`KB-REG-IN-DGCA`).

## When to use this skill

Use this skill when the user needs an **SPI/SPT framework** designed or reviewed for a named operator/airport/AMO, or wants SPIs aligned to a State Safety Programme's ALoSP. Trigger phrases: "design our SPIs", "set safety performance targets", "build our safety assurance metrics", "what alert and target levels should our SPIs have". If the request is vague, the Workflow intake forces the named operator and the hazards/objectives the SPIs must track. It designs the indicator framework; the whole SMS is `aviation-sms-builder`, the hazard register is `aviation-hazard-register`, and the SRB review of the SPIs is `aviation-srb-minutes`.

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
| Any (SMS Pillar 3) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 3 Safety Assurance) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Any (rate/trend context) | ../../knowledge-base/data-points/incident-rates-benchmarks.md (KB-DATA-TRIR-BENCHMARKS — quote source+year; never a bare number) |
| India (ALoSP) | ../../knowledge-base/regulatory/in-dgca.md (KB-REG-IN-DGCA — align SPIs to the DGCA SSP's acceptable level of safety performance) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the design/review scope, the named operator, the
CAA/SSP ALoSP-basis jurisdiction branch (India → `KB-REG-IN-DGCA` DGCA SSP ALoSP, FAA/EASA →
ask-the-reference, never fabricate), the hazards/objectives each SPI tracks, leading-vs-lagging
per SPI, the measurement period, the baseline data (via `incident_rates`; quote
`KB-DATA-TRIR-BENCHMARKS` source+year, never invent), the alert/target-derivation branch
(HistoricalBaseline → baseline data becomes required), and the per-SPI owner — lives in
**`references/intake.md`** (the `intake-coverage` manifest + echo-back + refuse-on-vague
anchors). Run it one question at a time, branch on the answers, and **echo the confirmed
operator + the hazards/objectives back before any analysis**. Then for each SPI: define it, set an **alert level** and a **target level** (the SPT), map it to its owning hazard/objective, and use `incident_rates` for the trend context. **Every SPI must carry a defined threshold and an owner** — an SPI with no alert/target level or no owning hazard is flagged. Never invent a performance figure; an absent datum is `[GAP]`.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the SPI/SPT design) is in `references/METHODOLOGY.md`.

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

Moderate fan-out (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub any named individuals in the occurrence/rate inputs
  into role labels before any analysis.
- **Researcher** — from the scrubbed inputs, assemble the hazards/objectives the SPIs must
  track and any baseline rate data (trend context via `incident_rates`; quote source+year, never
  a bare number). SCOPE-OUT: does not set thresholds (the Drafter owns it).
- **Drafter** — design each SPI with a defined alert level + target level (SPT), map it to its
  owning hazard/objective, and flag any SPI lacking a threshold or an owner. Records `[GAP]` for
  any absent figure — never invents one. SCOPE-OUT: does not review SRB decisions.
- **Critic/QA** (MANDATORY) — the Aviation-SMS persona (`KB-SNIP-ARCHETYPES`): every SPI has an
  alert/target level and an owning hazard/objective, no performance figure is fabricated, and ZERO
  identity leak. Runs the per-skill SME sign-off checklist in `references/sme-review.md`
  (decision-support; precedes — never replaces — the human competent-person review).

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
