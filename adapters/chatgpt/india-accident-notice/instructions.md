# india-accident-notice

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

# Structured intake — india-accident-notice

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | Which **jurisdiction** did the incident occur in? *(India-default skill; a non-India jurisdiction is out of scope.)* | MCQ | India, Other / Unknown — India activates the mandatory state gate (Q1) | ELI-JURIS | always |
| Q1 | **Which state** did the incident occur in? *(infer-from-address allowed; I confirm before citing the notice form.)* | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown | ELI-JURIS | iff Q0 = India — **BLOCKING** |
| Q2 | What **kind of establishment**? | MCQ | Factory, Construction site, Mine, Other (specify) | ELI-INDUSTRY | always |
| Q2a | Which **DGMS region/zone** is the mine in? *(a mine notice resolves through DGMS, not the state factory dept.)* | free-text / MCQ-if-enumerable | DGMS zone | ELI-JURIS | iff Q2 = mine — **BLOCKING** |
| Q3 | **Severity / class** of the event (this sets the form and the deadline). | MCQ | Fatal · Serious bodily injury · Dangerous occurrence (no injury) · Reportable disease | ELI-SCORING | always |
| Q4 | **When did it happen** (date & time)? *(this starts the statutory clock — e.g. the 24-hour notice.)* | free-text (date-time) | exact date-time of the event | ELI-TEMPORAL | always |
| Q5 | **How many persons** were injured / killed? (counts only — I de-identify identities; I aggregate any cell < 5 in wider distribution.) | free-text | counts by outcome | ELI-EXPOSURE | always |
| Q6 | **What happened** — incident particulars (I will scrub names, exact location detail, and health detail). | free-text | narrative | ELI-SUBJECT | always |
| Q7 | Who is the **statutory notifier / signatory** (occupier, factory manager, mine manager/agent)? | free-text → role | role label | ELI-COMPETENCY | always |
| Q8 | What **records** do you already hold (medical/first-aid record, witness statements, prior register entry)? | MCQ multi | Medical record · Witness statements · Register entry · None yet | ELI-EVIDENCE | always |
| Q9 | Who is the assembled notice **for**, and how will it circulate? | MCQ | Internal record · Filed with the inspectorate / DGMS · Client/consultant memo | ELI-OUTPUT | always |

before any assembly**; **refuse to proceed on a vague or unconfirmed state (and, for a mine, an

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

Assemble a `report.json` conforming to the shared report-model schema, then run `generate_report.py` in Code Interpreter on the assembled `report.json` to render the branded DOCX + PDF (the A4 engine + bundled fonts are uploaded as Code-Interpreter assets). Resolve branding from the user's `brand.yaml` (Eyekyam default); surface the output paths and a one-line provenance note. Rank every control by the hierarchy of controls (no PPE-only treatment without justification); give every SMART action a named owner and a due date.

## Subagent roster (preserved as a sequential checklist)

_Full detail moved to the knowledge upload (see `knowledge/`)._

## Jurisdiction routing

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

| Jurisdiction | Read |
|---|---|
| India (state notice) | knowledge/in-state-forms.md (KB-REG-IN-STATEFORMS — the accident-notice rows; **mandatory state detection**) + in-factories-act.md |
| India (mine notice) | knowledge/in-mines-act.md (KB-REG-IN-MINES-ACT) + in-dgms.md (KB-REG-IN-DGMS — 24h notice + Form J register; region-resolved) |
| India (OSH transition) | knowledge/in-osh-code.md (KB-REG-IN-OSH-CODE — accident-notice duty retained; legacy-first note) |
| India (portal) | knowledge/in-portals.md (KB-REG-IN-PORTALS — state authority / DGMS portal; verify locally) |
| Any   | knowledge/iso-45001.md + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific law (confirm the **state** first) |

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
