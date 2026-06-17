# aviation-fdm-foqa-analysis

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

**Assistive boundary (D-05a) — state it up front:** this skill structures analysis from the **summaries the user supplies**. It does NOT ingest raw flight data and does NOT invent exceedance counts/values; an absent datum is `[GAP]`, routed to the competent FDM team.

The structured intake captures, one question at a time, the facts the analysis needs:

1. **Named operator/scope (free-text)** — the named operator and the fleet/period the FDM/FOQA programme covers.
2. **Supplied summaries (free-text)** — the exceedance / event summaries the user already holds (counts, event types, periods). **The skill works ONLY from these — it does not generate exceedance values.**
3. **Question (MCQ)** — frame findings / identify trends / propose SMS actions / all of these.
4. **De-identify (auto)** — any crew named in a summary is scrubbed to a role label first.

Echo the **confirmed operator + the supplied summaries** back. Then: frame each finding traced to a supplied summary item; identify trends ONLY across the supplied data; reach systemic SMS findings and HoC-ranked actions with named owners/dates. For any datum the user did NOT supply, record `[GAP]` and route it to the competent FDM team — **never fabricate an exceedance count or value.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the FDM/FOQA-informed analysis frame) is in `references/METHODOLOGY.md`.

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

- **De-identifier** — runs FIRST; scrub any crew named in the supplied summaries into role labels
  before any analysis.
- **Researcher** — from the SUPPLIED summaries only, assemble the exceedance/event items and their
  periods; record `[GAP]` for any datum the user did not supply. SCOPE-OUT: does NOT generate or
  infer exceedance values, and does not draft.
- **Drafter** — frame each finding traced to a supplied summary item, identify trends across the
  supplied data only, and reach systemic SMS actions (HoC-ranked, named owners/dates). SCOPE-OUT:
  does not invent exceedance counts/values.
- **Critic/QA** (MANDATORY) — the Aviation-SMS persona (`KB-SNIP-ARCHETYPES`): the load-bearing
  assistive check — does this read as structured analysis of user-supplied summaries, NOT autonomous
  analysis of raw flight data? Any invented exceedance count/value is a FLAG; every `[GAP]` is honest.
  And ZERO crew-identity leak.

Simple single-subject tasks run single-threaded — no subagents.

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| Any (SMS Pillar 3) | ../../knowledge-base/standards/icao-annex19.md (KB-STD-ICAO-ANNEX19 — Pillar 3 Safety Assurance / operational-data monitoring) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
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
