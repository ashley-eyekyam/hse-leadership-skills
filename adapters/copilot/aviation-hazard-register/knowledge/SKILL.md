---
name: aviation-hazard-register
description: 'Build and maintain an aviation SMS hazard register: hazard identification,
  consequence, existing controls, risk classification via the ICAO Annex 19 5x5 Risk
  Classification Scheme (the shared A7 risk_matrix engine), and HoC-ranked mitigation
  with a named owner and date — each entry traced to evidence. Use this skill to create
  or review a hazard register for a named operator, airport, or AMO, or to risk-classify
  aviation hazards on the ICAO 5x5. Grounds in KB-STD-ICAO-ANNEX19 + KB-DATA-AVI-RISK-MATRIX,
  scores risk reproducibly via risk_matrix.score(), ranks mitigations through the
  hierarchy of controls (flagging PPE/admin-only), and validates owners/dates with
  smart_actions. Decision-support only; a competent person must review the output.'
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

# Aviation Hazard Register

The **SMS hazard-register** skill (ICAO Annex 19 Pillar 2 — Safety Risk Management). For a named operator, airport, or AMO it builds/maintains a register where each entry runs **hazard → consequence → existing controls → risk classification (the ICAO 5×5 Risk Classification Scheme) → HoC-ranked mitigation with a named owner and date**, every entry traced to evidence (the B5 `{hazard}→{evidence}` / `{mitigation}→{hazard}` discipline). Risk is classified by the **shared A7 `risk_matrix` engine** with the ICAO 5×5 `MatrixConfig` (`KB-DATA-AVI-RISK-MATRIX`) — never a forked matrix, so two assessors score the same hazard identically. Mitigations are HoC-ranked (`controls`) and validated for owner/date (`smart_actions`); a PPE/admin-only mitigation without justification is flagged.

## When to use this skill

Use this skill when the user needs an **SMS hazard register** built or maintained for a named operator/airport/AMO, or wants aviation hazards **risk-classified on the ICAO 5×5**. Trigger phrases: "build our hazard register", "risk-classify this aviation hazard", "rate this on the ICAO 5×5 matrix", "review our SMS hazard log". If the request is vague, the Workflow intake forces the named operator and the specific hazard(s) first. It builds the register; the whole-SMS manual is `aviation-sms-builder`, and a change assessment is `aviation-change-safety-assessment`.

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
| Any (SMS Pillar 2) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 2 Safety Risk Management) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Any (5×5 matrix) | ../../knowledge-base/data-points/aviation-risk-matrix.md (KB-DATA-AVI-RISK-MATRIX — the ICAO 5×5 MatrixConfig for risk_matrix.score()) |
| Unknown | Ask the operator's certificating authority before citing any State programme |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the build/add/review scope, the named operator/area,
the CAA/SSP jurisdiction branch (India → `KB-REG-IN-DGCA`, FAA/EASA → ask-the-reference, never
fabricate), each hazard + its evidence + how it was surfaced (reactive/proactive/predictive),
the exposed population, the consequence + existing controls, the ICAO 5×5 severity/likelihood
(the **band is the engine's, never the model's**), and the mitigation owner — lives in
**`references/intake.md`** (the `intake-coverage` manifest + echo-back + refuse-on-vague
anchors). Run it one question at a time, branch on the answers, and **echo the confirmed
operator + hazards back before scoring**. Then for each entry: call `risk_matrix.score(severity, likelihood, matrix=AVIATION_5X5)` (the `KB-DATA-AVI-RISK-MATRIX` config) for the initial rating, propose mitigations and HoC-rank them with `controls.rank_controls()` (flagging PPE/admin-only), score the residual rating and report the movement with `risk_matrix.residual_delta()`, and validate every mitigation owner/date with `smart_actions.validate_register()`.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the register build + 5×5 wiring) is in `references/METHODOLOGY.md`.

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

- **De-identifier** — runs FIRST; scrub any named individuals/reporters in the hazard
  evidence into role labels before any analysis. Returns the re-identification key SEPARATELY.
- **Researcher** — from the scrubbed inputs, assemble the hazards, their consequences, the
  existing controls, and the supporting evidence (each hazard traced to an evidence item); flag `[GAP]`.
  SCOPE-OUT: does not score risk (the Risk-Scorer owns it).
- **Risk-Scorer (A7 5×5)** — for each hazard call `risk_matrix.score()` with the ICAO 5×5
  `MatrixConfig` (`KB-DATA-AVI-RISK-MATRIX`) for the initial + residual ratings; never invents a
  band — the engine computes it. SCOPE-OUT: does not draft or select controls.
- **Drafter** — assemble the register, HoC-rank every mitigation (`controls`, flag PPE/admin-only),
  and validate owner/date (`smart_actions`). SCOPE-OUT: does not re-score risk.
- **Critic/QA** (MANDATORY) — the Aviation-SMS persona (`KB-SNIP-ARCHETYPES`): every hazard
  evidence-traced + 5×5-rated, no PPE/admin-only mitigation unjustified, every mitigation
  owner/date-stamped, and ZERO identity leak. Runs the per-skill SME sign-off checklist in
  `references/sme-review.md` (decision-support; precedes — never replaces — the human
  competent-person review).

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
