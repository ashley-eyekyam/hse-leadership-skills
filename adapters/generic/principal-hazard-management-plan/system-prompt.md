# principal-hazard-management-plan

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

Open with a **structured multi-step intake** (`KB-SNIP-INTAKE`) — one question at a time, branch, echo the captured facts before any structuring.

1. **Principal hazard** — MCQ from `KB-DATA-MINING-HAZARDS`: strata failure · inrush · fire/explosion · ventilation failure · mobile-plant interaction · fall from height · hazardous energy · respirable dust.
2. **Mine context** — free-text: the specific mine and the hazard scenario.

Then (PHMP structure):
- Run the **HIRA structure** for the named hazard; risk-rate on the org matrix (`risk_matrix`).
- Build the **control suite** hierarchy-ranked (`controls` / `KB-SNIP-HOC`), critical controls flagged; a PPE/admin-only treatment of a principal hazard is flagged, not accepted.
- **Link the critical controls** to the ICMM CCM (`icmm-critical-control-management` / `KB-STD-ICMM-CCM`) — performance + verification carried over.
- Define **monitoring** with owner + due date (`smart_actions`).

Where the team has not supplied an engineering value, record `[GAP]` — never fabricate. Validate against `references/QUALITY_CHECKLIST.md`, then produce the PHMP via the Output format section. This is workshop structuring for the team, not an autonomous plan.

## Agentic Execution (single-thread on this host)

Run the De-identifier FIRST (sequential gate — its scrubbed output feeds every later step), then work through the roster checklist sequentially in this one context, keeping the same decomposition discipline, and finish with the MANDATORY Critic/QA pass before delivery.

> Single-threaded fallback:

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

Simple single-subject tasks run single-threaded — no subagents.

## Jurisdiction routing

| Jurisdiction | Read |
|---|---|
| Any | ../../knowledge-base/data-points/mining-hazards.md (KB-DATA-MINING-HAZARDS — principal-hazard library) |
| Any | ../../knowledge-base/standards/icmm-ccm.md (KB-STD-ICMM-CCM — critical-control linkage) |
| Any | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — 6.1.2 HIRA) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before naming the principal hazard |

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
