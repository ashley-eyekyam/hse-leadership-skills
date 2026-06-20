# toxic-release-dispersion-scenario

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

# Structured intake — toxic-release-dispersion-scenario

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | What is the scenario framing for — a bowtie, a LOPA, a QRA input, or an emergency-plan/siting study? | MCQ | bowtie / LOPA / QRA-input / emergency-plan-zone | ELI-SCOPE | always |
| Q2 | Released substance + CAS + the inventory at risk (mass). | free-text | substance + mass; refuse "a toxic gas" | ELI-SUBJECT | always |
| Q3 | Physical state + storage pressure/temperature. | MCQ + free-text | gas / liquefied-gas / liquid; P, T | ELI-EVIDENCE | always |
| Q4 | Release scenario. | MCQ | catastrophic (full-bore) / continuous (leak) / instantaneous (puff) | ELI-SUBJECT | always |
| Q5 | Do you hold a release rate / hole size, or should the modeller derive it? | MCQ + free-text | supplied (give value) / for-modeller (`[GAP]`) | ELI-EVIDENCE | always |
| Q6 | Toxicity benchmark you want zoned against. | MCQ | AEGL / ERPG / IDLH / SLOT-SLOD / unknown | ELI-EVIDENCE | always |
| Q7 | Release point + receptor distance/direction + typical weather (wind, stability). | free-text | scenario geometry for the modeller | ELI-LOCATION | always |
| Q8 | Receptors at risk. | MCQ multi-select | on-site workers / public / environment | ELI-EXPOSURE | always |
| Q9 | Output format / reader for the scenario brief. | MCQ | modelling-input brief / siting-study input / emergency-plan-zone framing | ELI-OUTPUT | always |
| Q10 | Org consequence band scheme for the qualitative consequence axis. | MCQ | org scheme / default 5×5 — qualitative band only, NOT a modelled result | ELI-SCORING | always |

**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent a dispersion

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
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the skill-specific
  persona, domain checklist, and boundary in `knowledge/sme-review.md`
  (consequence-modelling / dispersion specialist lens: is this honest SCENARIO FRAMING
  for the modelling team — source term captured not computed, no invented distance /
  concentration, downstream owners named). Decision-support only; precedes — never
  replaces — the human competent-person review.

Simple single-subject tasks run single-threaded — no subagents.

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| UK/EU | knowledge/dsear-atex.md (KB-STD-DSEAR) + standards/ccps-bowtie.md |
| Any   | knowledge/ccps-bowtie.md (KB-STD-CCPS-BOWTIE — consequence side via `bowtie-builder`) + standards/iec-61511.md (KB-STD-IEC-61511 — `lopa-worksheet`) |
| Any   | knowledge/hierarchy-of-controls.md (KB-SNIP-HOC) for mitigative barriers |
| Unknown | Ask before citing any specific law |

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
