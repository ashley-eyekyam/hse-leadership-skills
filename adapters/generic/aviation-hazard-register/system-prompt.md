# aviation-hazard-register

> **Disclaimer — decision-support only.** Outputs are drafts to assist a competent person — not finished, approved, or legal deliverables; every output must be reviewed and signed off by a competent person. (Full text: `knowledge/DISCLAIMER.md`.)

## Data Protection & De-identification (MANDATORY — apply before drafting)

Apply this BEFORE you draft anything. Treat injury, illness, and any health
detail as the highest sensitivity. Full scrub list, identifier tests, and the
jurisdiction quick-reference: `knowledge/deid-checklist.md`.

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
`knowledge/` (ISO 45001 OH&S · ISO 14001 environmental · ISO 45003 psychosocial).
Always apply `knowledge/hierarchy-of-controls.md` (KB-SNIP-HOC)
to every control recommendation. For any benchmark/figure, look up the ID in the relevant
`_registry.yaml`, then read ONLY the named file — and quote its `source`+`year`.

# Structured intake — aviation-hazard-register

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Build a new register or maintain/review an existing one? | MCQ | Build/a new register, Add/hazards to an existing register, Review/re-score an existing register | ELI-SCOPE | always |
| Q2 | Name the operator/airport/AMO and the operation/area the register covers. | free-text | "name *this* org and area; 'an airline' is refused." | ELI-SUBJECT | always |
| Q3 | Which certificating authority / SSP applies? | MCQ | India/DGCA, FAA, EASA, Other CAA (specify), Unknown | ELI-JURIS | always |
| Q3a | *(India only)* Which Indian operations / which State Safety Programme layer applies? | free-text | aligns the DGCA State Safety Programme layer (`KB-REG-IN-DGCA`); exact CAR number `[GAP]` to verify | ELI-JURIS | Q3==India |
| Q4 | Describe each hazard and its supporting evidence. | free-text | one per hazard; each must trace to an evidence item | ELI-SUBJECT | always |
| Q5 | For each hazard, how was it surfaced? | MCQ | Reactive (occurrence/report) · Proactive (audit/inspection/survey) · Predictive (FDM/FOQA, trend) | ELI-EVIDENCE | per hazard |
| Q6 | Who/what is exposed to each hazard's consequence? | MCQ | Flight crew · Cabin crew · Ground/ramp crew · Passengers · Third party/public · Aircraft/asset · Multiple | ELI-EXPOSURE | per hazard |
| Q7 | What is the credible worst consequence, and what controls already exist? | free-text | per hazard; the existing-control baseline for residual scoring | ELI-SUBJECT | per hazard |
| Q8 | Choose ICAO severity. | MCQ | Negligible · Minor · Major · Hazardous · Catastrophic | ELI-SCORING | per hazard |
| Q9 | Choose ICAO likelihood. | MCQ | Extremely Improbable · Improbable · Remote · Occasional · Frequent | ELI-SCORING | per hazard |
| Q10 | Who will own the mitigating actions? | free-text | role label; validated by `smart_actions` | ELI-COMPETENCY | always |

**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

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
  `knowledge/sme-review.md` (decision-support; precedes — never replaces — the human
  competent-person review).

Simple single-subject tasks run single-threaded — no subagents.

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| Any (SMS Pillar 2) | knowledge/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 2 Safety Risk Management) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Any (5×5 matrix) | knowledge/aviation-risk-matrix.md (KB-DATA-AVI-RISK-MATRIX — the ICAO 5×5 MatrixConfig for risk_matrix.score()) |
| Unknown | Ask the operator's certificating authority before citing any State programme |

## Attribution (non-intrusive)

After the deliverable is produced — never before, and never as a blocking
question — read `knowledge/company-card.yaml` and surface the company card per
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
