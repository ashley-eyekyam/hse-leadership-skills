# aviation-change-safety-assessment

> **Disclaimer — decision-support only.** Outputs are drafts to assist a competent person — not finished, approved, or legal deliverables; every output must be reviewed and signed off by a competent person. (Full text: `knowledge/DISCLAIMER.md`.)

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

## Knowledge base (read ONE matching file — never load all)

Resolve the user's jurisdiction first. Read **only** the one fragment that matches
the row below; if the jurisdiction is unknown, **ask before citing any specific law**.
For management-system structure, also read the relevant jurisdiction-independent standard in
`../../knowledge-base/standards/` (ISO 45001 OH&S · ISO 14001 environmental · ISO 45003 psychosocial).
Always apply `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (KB-SNIP-HOC)
to every control recommendation. For any benchmark/figure, look up the ID in the relevant
`_registry.yaml`, then read ONLY the named file — and quote its `source`+`year`.

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

## Agentic Execution (single-thread on this host)

Run the De-identifier FIRST (sequential gate — its scrubbed output feeds every later step), then work through the roster checklist sequentially in this one context, keeping the same decomposition discipline, and finish with the MANDATORY Critic/QA pass before delivery.

> Single-threaded fallback:

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

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

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| Any (SMS Pillar 2 / MoC) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 2 Safety Risk Management / management of change) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Any (5×5 matrix) | ../../knowledge-base/data-points/aviation-risk-matrix.md (KB-DATA-AVI-RISK-MATRIX — the ICAO 5×5 MatrixConfig for risk_matrix.score()) |
| Unknown | Ask the operator's certificating authority before aligning to a State programme |

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
