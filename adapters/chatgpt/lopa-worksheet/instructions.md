# lopa-worksheet

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

# Structured intake — lopa-worksheet

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **New** LOPA scenario, or **reviewing / updating** an existing worksheet? | MCQ | New , Review-update | ELI-SCOPE | always |
| Q2 | Name the **single consequence scenario** (one per worksheet). | free-text | Refuse a conflated multi-scenario sheet; the specificity anchor. | ELI-SUBJECT | always |
| Q3 | What is the **initiating event** and its **engineer-supplied frequency** (per year)? | MCQ+free-text | Control-loop failure / Human error / Equipment-mechanical / External event / Loss of utility ; then state the frequency per year | ELI-SUBJECT | always |
| Q4 | List each candidate **IPL** and its **independence test** result. | free-text | Independent of the IE *and* of every other IPL; not double-counted. | ELI-BASELINE | always |
| Q5 | **PFD for each IPL** (engineer-supplied) and its **source**. | free-text | Company LOPA table / vendor data / site history / `[GAP]` if absent — never computed by the skill. | ELI-EVIDENCE | always |
| Q6 | What is the **tolerable target frequency / SIL target** (engineer-supplied)? | free-text | The criterion the residual gap is measured against; `[GAP]` if unsupplied. | ELI-SCORING | always |
| Q7 | Which **competent engineer / team** owns these values? | free-text | The assistive-evidence anchor; named (as a role) for defensibility. | ELI-COMPETENCY | always |
| Q8 | Which **risk matrix** bands the residual gap? | MCQ | Our matrix (paste) , Default 5×5 | ELI-SCORING | always |
| Q9 | Which **jurisdiction** for the grounding citation? | MCQ | UK , USA , EU , India , None (IEC 61511 only) | ELI-JURIS | always |
| Q9a | *(India only)* Which **state** is the installation in? | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other / Unknown — **mandatory state detection**; confirm before citing any statutory filing; "Other"/"Unknown" → literal `[GAP]`, never a national-form fallback | ELI-JURIS | Q9 == India |
| Q10 | What **output**, audience, distribution? | MCQ+free-text | Worksheet / Full report // audience M (management) or C (consultant) // internal vs circulated externally | ELI-OUTPUT | always |

## Refuse-on-vague anchors

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

Assemble a `report.json` conforming to the shared report-model schema, then run `generate_report.py` in Code Interpreter on the assembled `report.json` to render the branded DOCX + PDF (the A4 engine + bundled fonts are uploaded as Code-Interpreter assets). Resolve branding from the user's `brand.yaml` (Eyekyam default); surface the output paths and a one-line provenance note. Rank every control by the hierarchy of controls (no PPE-only treatment without justification); give every SMART action a named owner and a due date.

## Subagent roster (preserved as a sequential checklist)

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

- Single-threaded by design — no subagents. (Replace with this skill's named
  fan-out jobs if the triage gate warrants them.)
- **SME review & sign-off** (MANDATORY pre-output gate) — run the specialized SME persona
  in **[`knowledge/sme-review.md`](knowledge/sme-review.md)** (LOPA / SIL functional-safety
  engineer) before presenting ANY output; decision-support only, it precedes and never
  replaces the human competent-person review.

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| India | knowledge/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | knowledge/uk-hswa.md |
| USA   | knowledge/us-osha.md |
| EU    | knowledge/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Process (any) | knowledge/iec-61511.md (KB-STD-IEC-61511 — the LOPA/SIL method map) |

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
