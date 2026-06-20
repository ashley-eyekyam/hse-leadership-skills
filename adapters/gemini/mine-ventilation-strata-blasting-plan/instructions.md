# mine-ventilation-strata-blasting-plan

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

# Structured intake — mine-ventilation-strata-blasting-plan

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | Which plan + new or review? | MCQ | ventilation / strata-ground-control / blasting-shotfiring / draft-new / review-existing | ELI-SCOPE | always |
| Q2 | Commodity + mine type? | MCQ | a) Coal — UG / b) Coal — opencast / c) Metalliferous — UG / d) Metalliferous — opencast / e) Other | ELI-INDUSTRY | always (branch driver) |
| Q3 | DGMS region / state (India)? | MCQ→confirm | infer-then-confirm the DGMS region and the **state** if the jurisdiction is India | ELI-JURIS/ELI-LOCATION | India |
| Q4V | Ventilation parameters | free-text | "Gas regime / seam gassiness category, required air quantity & quality, method (forcing/exhausting/booster), districts, gas-monitoring setup" | ELI-SUBJECT/ELI-EVIDENCE | Q1=ventilation |
| Q4S | Strata parameters | free-text | "Seam/orebody geology + depth, roof/highwall conditions, support regime (bolt/prop/standing), geotech/convergence data" | ELI-SUBJECT/ELI-EVIDENCE | Q1=strata |
| Q4B | Blasting parameters | free-text | "Explosive type, blast design (burden/spacing/charge/delay), exclusion zone, misfire procedure, vibration/flyrock limits" | ELI-SUBJECT/ELI-EVIDENCE | Q1=blasting |
| Q5 | Principal hazards to address? | mcqmulti-select | confirm from `KB-DATA-MINING-HAZARDS` for the selected plan type | ELI-SUBJECT | always |
| Q6 | Sign-off competent person (role)? | free-text | "Ventilation officer / shotfirer / geotech engineer / mine manager — as a role label" | ELI-COMPETENCY | always |
| Q7 | Risk-rating scheme? | MCQ | a) Org's existing matrix / b) Default 5×5 (D-02 bands) — confirm | ELI-SCORING | always |
| Q8 | Output + distribution? | MCQ | a) Plan document / b) Plan + gap-check / c) Review notes | ELI-OUTPUT | always |

facts back before any drafting**; **refuse on a vague subject** — a generic-template request

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

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

**Step 4 — SME review & sign-off (MANDATORY, before any output):** run the skill-specific
SME persona sign-off in **`knowledge/sme-review.md`** — this skill carries **two** justified
lenses (a ventilation / strata-control engineer and a shotfirer / blasting engineer, distinct
DGMS competencies). **Matching-lens scoping:** when the user selects only one plan type, run
only the matching lens (MAX-2 discipline). Model QA, decision-support, FLAGs non-blocking; a
competent person owns the engineering judgement and signs off.

Simple single-subject tasks run single-threaded — no subagents.

## Jurisdiction routing

| Jurisdiction | Read |
|---|---|
| India (mine) | knowledge/in-mines-act.md (KB-REG-IN-MINES-ACT — ventilation/strata/blasting plan duties) |
| Any | knowledge/icmm-ccm.md (KB-STD-ICMM-CCM — principal-hazard framing) + data-points/mining-hazards.md (KB-DATA-MINING-HAZARDS) |
| Any | knowledge/iso-45001.md (KB-STD-ISO45001 — 6.1.2 HIRA) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific plan duty |

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
