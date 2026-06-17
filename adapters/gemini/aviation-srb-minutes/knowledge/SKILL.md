---
name: aviation-srb-minutes
description: 'Produce Safety Review Board (SRB) / Safety Action Group minutes for
  an aviation operator: the agenda, the SPI/SPT review, the hazard and risk decisions,
  the actions with owner and due date, and a defensible decision log with rationale.
  Use this skill to draft or review SRB/SAG minutes for a named operator, airport,
  or AMO. Grounds in KB-STD-ICAO-ANNEX19, runs the de-identification scrub first so
  attendees appear as role labels and no reporter is named, and produces a decision
  log where every decision carries a rationale and an accountable person. Ships an
  attendance/decision table with empty rows for the meeting. Decision-support only;
  a competent person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: governance
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

# Aviation SRB Minutes

The **Safety Review Board / Safety Action Group minutes** skill (ICAO Annex 19 Pillar 3 — Safety Assurance / management review). For a named operator it produces minutes with: the **agenda**, the **SPI/SPT review**, the **hazard and risk decisions**, the **actions** with owner and due date, and a **defensible decision log** where every decision carries a rationale and an accountable person (the B6 evidence-traced + decision/action-log discipline). Attendees appear as **role labels** (chair = Accountable Manager) — de-identification runs first so no reporter named in a hazard item is identified. It ships an **attendance / decision table with empty rows** for the meeting to fill. Single-threaded by design (structured minute-taking — Archetype 4); no `scripts/`.

## When to use this skill

Use this skill when the user needs **SRB / SAG minutes** drafted or reviewed for a named operator. Trigger phrases: "minute our Safety Review Board", "Safety Action Group minutes", "record the SRB decisions and actions", "build the SRB decision log". If the request is vague, the Workflow intake forces the named operator and the meeting agenda first. It records the meeting; the SPIs themselves are designed by `aviation-spi-spt-framework`, and the hazard register is `aviation-hazard-register`.

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
| Any (SMS Pillar 3) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 3 Safety Assurance / management review) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The structured intake captures, one question at a time, the facts the minutes need:

1. **Named operator + meeting (free-text)** — the named operator and the SRB/SAG meeting date/scope.
2. **Attendees (free-text → role labels)** — who attended; the chair (typically the Accountable Manager). De-identify any individual per the block above — attendees appear as **role labels** in the minutes.
3. **SPI/SPT status (free-text)** — each SPI reviewed vs its alert/target level, the trend, the breach status (from `aviation-spi-spt-framework` where it exists).
4. **Hazard / risk decisions (free-text)** — each hazard item, its current 5×5 rating, and the decision taken.
5. **Actions (free-text)** — each action with an owner and a due date.

Echo the **confirmed operator + meeting** back. Then assemble the minutes: meeting metadata (attendees as role labels, quorum), the SPI/SPT review, the hazard & risk decisions, the actions ({action, owner, due}), and the **decision log** ({decision, rationale, accountable person}) — every decision MUST carry a rationale and an accountable person. Where the meeting inputs are not yet supplied, render the attendance / decision / action tables with **empty rows** for the meeting to fill. De-identification runs first: no reporter named in a hazard item is identified.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the minute structure + decision log) is in `references/METHODOLOGY.md`.

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

- **Single-threaded by design — no subagents** (Archetype 4: structured minute-taking is one
  tightly-coupled job). The de-identification scrub runs FIRST inline (attendees → role labels;
  no reporter in a hazard item is identified), then the minutes + decision log are assembled, then
  the MANDATORY Critic/QA pass runs in this same context — the Aviation-SMS persona
  (`KB-SNIP-ARCHETYPES`) checks every decision has a rationale + an accountable person, every action
  has an owner + due date, and no individual is named.

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
