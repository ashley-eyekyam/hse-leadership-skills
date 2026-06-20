---
name: aviation-fdm-foqa-analysis
description: Structure a flight-data-monitoring (FDM/FOQA) INFORMED safety analysis
  from the exceedance and event summaries the user supplies — frame the findings,
  the trends, and the SMS actions per the ICAO Annex 19 Safety Assurance pillar. It
  does NOT ingest or analyse raw flight data and does NOT invent exceedance counts
  or values; absent data is recorded as [GAP] and routed to the competent FDM team.
  Use this skill to structure an FDM/FOQA-informed analysis for a named operator from
  summaries the user provides. Grounds in KB-STD-ICAO-ANNEX19, traces every finding
  to a supplied summary item, reaches systemic SMS actions, and is explicitly assistive.
  Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: performance
  tier: 4
  audience:
  - M
  - E
  - C
  industry:
  - Avi
  jurisdiction:
  - All
  status: assistive
  plugin: hse-aviation
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Aviation FDM / FOQA Analysis (assistive)

The **FDM/FOQA-informed analysis** skill (ICAO Annex 19 Pillar 3 — Safety Assurance; `status: assistive`). For a named operator it **structures a safety analysis from the exceedance and event summaries the user supplies** — framing the findings, the trends, and the SMS actions, each traced to a supplied summary item, reaching systemic SMS findings (the B5 evidence-traced discipline). **It does NOT ingest or analyse raw flight data, and it does NOT invent exceedance counts or values** — an absent datum is recorded as `[GAP]` and routed to the competent FDM team. This honest `assistive` boundary is the point: an LLM skill cannot analyse raw FDM/FOQA parameter data, so it structures the *output* of that analysis, never the raw data itself.

## When to use this skill

Use this skill when the user has **FDM/FOQA exceedance / event summaries already** and needs them **structured** into findings, trends, and SMS actions for a named operator. Trigger phrases: "structure our FOQA exceedance summary into SMS findings", "frame these flight-data-monitoring events", "turn our FDM summary into actions". Do NOT use it expecting raw-data analytics — it analyses neither raw parameter data nor invents exceedance values. If the request is vague, the Workflow intake forces the named operator and the supplied summaries first.

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
| Any (SMS Pillar 3) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 3 Safety Assurance / operational-data monitoring) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**Assistive boundary (D-05a) — state it up front:** this skill structures analysis from the **summaries the user supplies**. It does NOT ingest raw flight data and does NOT invent exceedance counts/values; an absent datum is `[GAP]`, routed to the competent FDM team.

The full typed/branched intake Q-table — the named operator/fleet, the CAA/SSP jurisdiction
branch (India → `KB-REG-IN-DGCA`, FAA/EASA → ask-the-reference, never fabricate), the audience,
the **supplied exceedance summaries** (the skill works ONLY from these — never raw flight data,
never an invented count/value), the one-off-vs-trend branch (a trend needs ≥2 supplied periods),
the period, and the SMS-action owner — lives in **`references/intake.md`** (the `intake-coverage`
manifest + de-id-aware echo-back, role labels only + refuse-on-vague anchors). Crew detail is
de-identified to role labels FIRST. Run it one question at a time, branch on the answers, and
**echo the confirmed operator + supplied summaries back (crew detail de-identified) before any
analysis**. Then: frame each finding traced to a supplied summary item; identify trends ONLY across the supplied data; reach systemic SMS findings and HoC-ranked actions with named owners/dates. For any datum the user did NOT supply, record `[GAP]` and route it to the competent FDM team — **never fabricate an exceedance count or value.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the FDM/FOQA-informed analysis frame) is in `references/METHODOLOGY.md`.

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

Moderate fan-out (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub any crew named in the supplied summaries into role labels
  before any analysis.
- **Researcher** — from the SUPPLIED summaries only, assemble the exceedance/event items and their
  periods; record `[GAP]` for any datum the user did not supply. SCOPE-OUT: does NOT generate or
  infer exceedance values, and does not draft.
- **Drafter** — frame each finding traced to a supplied summary item, identify trends across the
  supplied data only, and reach systemic SMS actions (HoC-ranked, named owners/dates). SCOPE-OUT:
  does not invent exceedance counts/values.
- **Critic/QA** (MANDATORY) — the Aviation-SMS persona (`KB-SNIP-ARCHETYPES`): the load-bearing
  assistive check — does this read as structured analysis of user-supplied summaries, NOT autonomous
  analysis of raw flight data? Any invented exceedance count/value is a FLAG; every `[GAP]` is honest.
  And ZERO crew-identity leak. Runs the per-skill SME sign-off checklist in
  `references/sme-review.md` (FDM analyst + line-pilot lenses; decision-support; precedes —
  never replaces — the human competent-person / FDM-team review).

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
