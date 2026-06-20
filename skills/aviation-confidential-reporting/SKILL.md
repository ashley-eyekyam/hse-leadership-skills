---
name: aviation-confidential-reporting
description: 'Design a voluntary / confidential aviation safety reporting system:
  the intake form, the de-identification and handling workflow, the feedback loop,
  and the reporter-protection assurances — per the ICAO Annex 19 Safety Promotion
  pillar. Use this skill to build or review a confidential safety reporting scheme
  for a named operator, airport, or AMO. Grounds in KB-STD-ICAO-ANNEX19, runs the
  de-identification scrub FIRST (reporter identity protection is load-bearing — names,
  role/route/base/flight, and narrative re-identifiers are tokenised to role labels,
  the re-identification key held separately), and makes the reporter-protection promise
  a mechanical pre-condition. Decision-support only; a competent person must review
  the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: culture
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

# Aviation Confidential Reporting

The **voluntary / confidential safety reporting** skill (ICAO Annex 19 Pillar 4 — Safety Promotion). For a named operator, airport, or AMO it designs the reporting system: the **intake form**, the **de-identification and handling workflow**, the **feedback loop**, and the **reporter-protection assurances**. De-identification is **load-bearing** here — reporter names, the reporter's role/route/base/flight, exact dates, and any narrative detail that could re-identify a reporter are tokenised to role labels *before* the skill reasons about the content, and any re-identification key is held in a separate custodian artifact, never in the circulated design. The just-culture promise — "you can report without being identified" — becomes a mechanical pre-condition, not a hope.

## When to use this skill

Use this skill when the user needs a **confidential / voluntary safety reporting system** designed or reviewed for a named operator/airport/AMO. Trigger phrases: "design our confidential reporting scheme", "build a voluntary safety reporting system", "how do we protect reporter identity", "set up our hazard reporting intake and feedback loop". If the request is vague, the Workflow intake forces the named operator and the reporting scope first. It designs the reporting system; the just-culture policy is `aviation-just-culture-policy`, and the whole SMS is `aviation-sms-builder`.

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
| Any (SMS Pillar 4) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 4 Safety Promotion / confidential reporting) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**De-identification is LOAD-BEARING and runs FIRST — reporter-identity protection is the point of the artifact:**

The full typed/branched intake Q-table — the named operator, the **scheme-type** branch
(confidential/voluntary/anonymous — the de-identification trigger), the protection-basis
jurisdiction branch (India → `KB-REG-IN-DGCA`, Unknown → Annex 19 Appendix 3 + legal-review
flag, never assert immunity the law doesn't grant), the MOR interface, the named custodian +
re-id-key handling, the feedback loop, the SLA/retention, and the optional de-identified sample
report — lives in **`references/intake.md`** (the `intake-coverage` manifest + de-id-aware
echo-back, role labels only + refuse-on-vague anchors). Run it one question at a time, branch on
the answers, and **echo the confirmed operator + scheme type + custodian arrangement back
(role labels only, never a reporter name) before any drafting**. Then design (a) the intake form, (b) the de-identification + handling workflow (de-id at the earliest point; the re-identification key held by the named custodian, apart from the circulated design), (c) the feedback loop, and (d) the reporter-protection assurances. **No reporter is ever named in the circulated design; no re-identification key is embedded.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the reporting-system design) is in `references/METHODOLOGY.md`.

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

Moderate fan-out (the De-identifier runs FIRST as a sequential dependency — and here it is
the load-bearing job, not a formality):

- **De-identifier** — runs FIRST; scrub EVERY reporter identifier (name, role/route/base/flight,
  exact dates, narrative re-identifiers) into role labels before any sibling sees the content.
  Returns the re-identification key SEPARATELY to the orchestrator (for the named custodian), never
  to a sibling and never into the design.
- **Researcher** — from the SCRUBBED inputs only, gather the operator/scheme facts and the Annex 19
  Pillar 4 confidential-reporting criteria (`KB-STD-ICAO-ANNEX19`). SCOPE-OUT: does not draft.
- **Drafter** — design the intake form, the de-id/handling workflow, the feedback loop, and the
  reporter-protection assurances; no reporter named, no key embedded. SCOPE-OUT: does not re-identify.
- **Critic/QA** (MANDATORY) — the Aviation-SMS persona (`KB-SNIP-ARCHETYPES`): the design protects
  reporter identity (role labels, no narrative re-identification, key held separately), the feedback
  loop is real, and ZERO reporter-identity leak (a leak is a de-id hard-fail, not a FLAG). Runs the
  per-skill SME sign-off checklist in `references/sme-review.md` (decision-support; precedes —
  never replaces — the human competent-person review).

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
