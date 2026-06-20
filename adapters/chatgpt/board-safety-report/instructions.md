# board-safety-report

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

# Structured intake — board-safety-report

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Reporting period** | free-text + MCQ | "Which period does this report cover?" — Monthly / Quarterly / Half-year / Annual / Other (+ the exact dates, e.g. 'FY2025' or 'Q2 2026'). Sets the subtitle + the `period` label passed to `incident_rates`; the comparison baseline. | ELI-TEMPORAL | always |
| Q2 | **Audience body** | MCQ | Board of directors / Executive committee / Senior leadership team. Tunes register/depth (board = most strategic, least operational) — the narrative altitude. *(The audience facet stays `[E]`; this only tunes the register.)* | ELI-OUTPUT | always |
| Q3 | **Safety data / metrics available** | free-text (structured) | "Provide the period's safety metrics — recordable / lost-time / DART counts **and hours worked** (for rates), plus any leading indicators: training %, audit/inspection closure, near-miss reporting rate, action closure." The **hours + counts gate the `incident_rates` call**; leading indicators are synthesized. | ELI-EVIDENCE | always |
| Q4 | **Key events of the period** | free-text | "Summarize the significant HSE events of the period (serious incidents, notable near-misses, regulatory contacts, audits). **These will be de-identified AND aggregated — do not name individuals; a single event will be rolled up, never narrated as an anecdote.**" Flagged for **immediate** de-id + aggregation (step 1). | ELI-SUBJECT | always |
| Q5 | **HiPo / SIF events** | free-text | "List any **high-potential (HiPo) incidents** and **serious-injury-or-fatality (SIF) precursors** in the period — events that *could* have been life-altering regardless of actual outcome." Drives the **D-01 HiPo/SIF lens** (step 4); de-identified + aggregated like Q4. | ELI-SUBJECT | always |
| Q6 | **Strategic priorities** | free-text | "What are the organisation's current HSE strategic priorities or objectives?" Frames the narrative against objectives (ISO 45001 9.3) + the strategic-actions section. | ELI-SUBJECT | always |
| Q6b | **Accountability for strategic asks** | free-text | "For each strategic priority/ask, which executive is accountable? (role-level — sharpens the governance asks; optional)" — accountability sharpens the *output* ask (ELI-COMPETENCY is omitted by design: a board paper names asks, not an action register). | ELI-OUTPUT | always |
| Q7 | **Prior-period comparison data** | free-text | "Provide the prior period's figures for trend comparison (or say if unavailable)." Absent → trends flagged `[GAP]`, never invented. | ELI-EVIDENCE | always |
| Q8 | **Benchmark target** | free-text | "Which benchmark should performance be compared against (industry/sector average, an internal target)? If you have a figure, state it **with its source**; otherwise the skill reads the KB benchmark with its source + year." Resolves `KB-DATA-TRIR-BENCHMARKS`; absent → `[GAP]`. | ELI-OBLIGATIONS | always |
| Q9 | **Environmental metrics?** (optional) | MCQ + free-text | No / Yes ; (if Yes, list them) — "Are environmental events/metrics in scope for this board paper?" then a **single** optional ISO 14001 9.1.2 env-performance line (D-02); **not** a full ESG branch. | ELI-EXPOSURE | always |
| Q10 | **Jurisdiction** | MCQ | India / UK / USA / EU / Other-or-Unknown. Mostly context (B9 is narrative); **India → resolve the state (Q10a)** only if a statutory figure is cited. | ELI-JURIS | always |
| Q10a | *(India only, if a statutory figure is cited)* **Which state?** | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other — **mandatory state detection; confirm the state before citing any statutory figure or form** (never a national form number). | ELI-JURIS | Q10 == India |

## Refuse-on-vague anchors

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

Assemble a `report.json` conforming to the shared report-model schema, then run `generate_report.py` in Code Interpreter on the assembled `report.json` to render the branded DOCX + PDF (the A4 engine + bundled fonts are uploaded as Code-Interpreter assets). Resolve branding from the user's `brand.yaml` (Eyekyam default); surface the output paths and a one-line provenance note. Rank every control by the hierarchy of controls (no PPE-only treatment without justification); give every SMART action a named owner and a due date.

## Subagent roster (preserved as a sequential checklist)

_Full detail moved to the knowledge upload (see `knowledge/`)._

## Jurisdiction routing

_Full detail moved to the knowledge upload (see `knowledge/`)._

## Attribution (non-intrusive)

_Full detail moved to the knowledge upload (see `knowledge/`)._

