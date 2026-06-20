---
name: aviation-just-culture-policy
description: Author a just-culture policy and its decision tree — the culpability
  / substitution-test line between acceptable and unacceptable behaviour — per the
  ICAO Annex 19 Safety Promotion pillar. Use this skill to draft or review a just-culture
  policy for a named aircraft operator, airport, or AMO, including the decision-tree
  that distinguishes honest error and at-risk behaviour from reckless/negligent conduct.
  Grounds in KB-STD-ICAO-ANNEX19, runs the de-identification scrub first so no reporter
  is named in an example, and produces a policy with an explicit decision line — never
  a vague slogan-only statement. Decision-support only; a competent person
  must review the output.
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

# Aviation Just Culture Policy

The **just-culture policy + decision-tree** skill (ICAO Annex 19 Pillar 4 — Safety Promotion). For a named operator, airport, or AMO it authors a just-culture policy **and** its **decision tree** — the culpability / substitution-test line that distinguishes honest error and at-risk behaviour from reckless or negligent conduct. The policy is never a vague "we have a just culture" statement: it carries an explicit decision line a reviewer can apply. De-identification runs first so no individual is named in any worked example. Single-threaded by design (policy + decision-tree drafting — Archetype 4); no `scripts/`.

## When to use this skill

Use this skill when the user needs a **just-culture policy** drafted or reviewed for a named operator/airport/AMO, including the **decision tree** between acceptable and unacceptable behaviour. Trigger phrases: "draft our just culture policy", "build the culpability decision tree", "where is the line between error and recklessness". If the request is vague, the Workflow intake forces the named operator and the policy scope first. It authors the policy; the confidential reporting system is `aviation-confidential-reporting`, and the whole SMS is `aviation-sms-builder`.

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
| Any (SMS Pillar 4) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 4 Safety Promotion / just culture) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the first-policy/revise scope, the named operator +
workforce, the **legal protection-basis** jurisdiction branch (India → `KB-REG-IN-DGCA`,
EU Reg 376/2014, FAA ASAP, Annex 19 Appendix 3 principles only, or Unknown → `[GAP]` + legal-
review flag, **never assert a protection the law doesn't grant**), the existing-reporting-system
status, the decision-tree basis (substitution test / culpability ladder / both), who applies +
signs it, the in-scope behaviours, and an optional de-identified scenario — lives in
**`references/intake.md`** (the `intake-coverage` manifest + echo-back + refuse-on-vague
anchors). Run it one question at a time, branch on the answers, and **echo the confirmed
operator + the decision-tree basis back before any drafting**. Then author (a) the just-culture policy statement, and (b) the **decision tree** with the explicit acceptable/unacceptable line (substitution test + the culpability ladder). De-identification runs first: any example uses role labels only.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the just-culture policy + decision tree) is in `references/METHODOLOGY.md`.

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

- **Single-threaded by design — no subagents** (Archetype 4: policy + decision-tree
  drafting is one tightly-coupled job). The de-identification scrub runs FIRST inline (any
  worked example uses role labels only), then the policy + decision tree are drafted, then the
  MANDATORY Critic/QA pass runs in this same context — the Aviation-SMS persona
  (`KB-SNIP-ARCHETYPES`) checks the policy carries an explicit acceptable/unacceptable line (not
  a slogan) and that no individual is named. The Critic/QA pass runs the per-skill SME sign-off
  checklist in `references/sme-review.md` (the human-factors + employment-law lenses;
  decision-support; precedes — never replaces — the human competent-person review).

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
