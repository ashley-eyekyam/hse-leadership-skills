---
name: aviation-change-safety-assessment
description: 'Conduct an aviation SMS change-management safety assessment (ICAO Annex
  19 management of change): describe the change, identify new and changed hazards,
  assess risk on the ICAO 5x5 Risk Classification Scheme (the shared A7 risk_matrix
  engine), mitigate through the hierarchy of controls, and approve or decline with
  a recorded rationale. Use this skill to assess the safety of a change for a named
  operator, airport, or AMO. Grounds in KB-STD-ICAO-ANNEX19 + KB-DATA-AVI-RISK-MATRIX,
  scores risk reproducibly via risk_matrix.score(), HoC-ranks mitigations (flagging
  PPE/admin-only), and validates owners/dates with smart_actions. Decision-support
  only; a competent person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
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

# Aviation Change Safety Assessment

The **SMS management-of-change** skill (ICAO Annex 19 Pillar 2 — Safety Risk Management). For a named operator, airport, or AMO it runs a change-management safety assessment: **describe the change → identify new and changed hazards → assess risk on the ICAO 5×5 → mitigate through the hierarchy of controls → approve or decline with a recorded rationale**. Risk is scored by the **shared A7 `risk_matrix` engine** with the ICAO 5×5 `MatrixConfig` (`KB-DATA-AVI-RISK-MATRIX`) — never a forked matrix. A change assessed without identifying its new hazards is the failure mode this skill exists to prevent.

## When to use this skill

Use this skill when the user needs a **change safety assessment** (management of change) for a named operator/airport/AMO — a new route, a fleet/equipment change, a procedure change, an organisational change. Trigger phrases: "assess the safety of this change", "management of change for our SMS", "what new hazards does this change introduce", "approve/decline this change with a safety rationale". If the request is vague, the Workflow intake forces the named operator and the specific change first. It assesses a change; the standing hazard register is `aviation-hazard-register`, and the whole SMS is `aviation-sms-builder`.

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
| Any (SMS Pillar 2 / MoC) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 2 Safety Risk Management / management of change) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Any (5×5 matrix) | ../../knowledge-base/data-points/aviation-risk-matrix.md (KB-DATA-AVI-RISK-MATRIX — the ICAO 5×5 MatrixConfig for risk_matrix.score()) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The structured intake captures, one question at a time, the facts the change assessment needs:

1. **Named operator/scope (free-text)** — the named operator/airport/AMO. A generic "an airline" is refused.
2. **The change (free-text)** — describe the specific change (new route, fleet/equipment, procedure, organisation). Be concrete — a vague "we're changing things" is refused.
3. **New / changed hazards (free-text)** — the hazards the change introduces or alters. **A change assessed without new hazards is flagged.**
4. **Severity + likelihood per hazard (MCQ on the ICAO axes)** — severity (Negligible / Minor / Major / Hazardous / Catastrophic) × likelihood (Extremely Improbable / Improbable / Remote / Occasional / Frequent). The model only *chooses*; `risk_matrix.score()` does the rest.
5. **Approval authority (free-text)** — who approves/declines the change.

Echo the **confirmed operator + the change + its new hazards** back. Then for each new/changed hazard: score it via `risk_matrix.score(severity, likelihood, matrix=AVIATION_5X5)` (`KB-DATA-AVI-RISK-MATRIX`), propose mitigations and HoC-rank them with `controls.rank_controls()` (flagging PPE/admin-only), score the residual rating and report the movement with `risk_matrix.residual_delta()`, and validate every mitigation owner/date with `smart_actions.validate_register()`. Conclude with an **approve / decline decision and a recorded rationale**.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the MoC assessment + 5×5 wiring) is in `references/METHODOLOGY.md`.

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

- **De-identifier** — runs FIRST; scrub any named individuals in the change inputs into role
  labels before any analysis.
- **Researcher** — from the scrubbed inputs, describe the change and enumerate the new/changed
  hazards it introduces (the B5 hazard→evidence discipline). SCOPE-OUT: does not score risk.
- **Risk-Scorer (A7 5×5)** — for each new/changed hazard call `risk_matrix.score()` with the ICAO
  5×5 `MatrixConfig` (`KB-DATA-AVI-RISK-MATRIX`) for the initial + residual ratings; never invents a
  band. SCOPE-OUT: does not draft or select controls.
- **Drafter** — assemble the assessment, HoC-rank every mitigation (`controls`, flag PPE/admin-only),
  validate owner/date (`smart_actions`), and record the approve/decline decision + rationale.
  SCOPE-OUT: does not re-score risk.
- **Critic/QA** (MANDATORY) — the Aviation-SMS persona (`KB-SNIP-ARCHETYPES`): the change identifies
  new hazards, each is 5×5-rated, no PPE/admin-only mitigation unjustified, the decision carries a
  rationale, and ZERO identity leak.

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
