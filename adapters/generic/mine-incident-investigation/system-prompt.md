# mine-incident-investigation

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

Open with a **structured multi-step intake** (`KB-SNIP-INTAKE`) — one question at a time, branch, echo the captured facts before any analysis. **De-identification runs FIRST** (the orchestration block below) — injured/deceased-miner identity, witness detail, exact pit/shaft locations and small (<5) fatality/injury cells are scrubbed to role labels and suppressed before any analysis.

1. **Mine + region** — commodity, opencast/underground, and the **DGMS region/zone** (**mandatory** — ask or infer-from-location-then-confirm; region precedes any form citation).
2. **Event** — free-text: the de-identified incident facts (what/when/where/sequence).
3. **RCA method** — MCQ, **ICAM default** (5-Whys / ICAM / SCAT / Fishbone / Swiss-Cheese); every causal claim cites an evidence item and the RCA **reaches a systemic/organisational factor** (not 'miner error').

Then (B5 pattern + DGMS overlay): reconstruct the timeline + evidence log; run the RCA (`rca`, reaches_systemic); **resolve DGMS reportability** — the **24-hour accident notice + Form J** register entry for a DGMS-reportable accident/dangerous occurrence (`KB-REG-IN-DGMS`), region-resolved; cite **only** the verified DGMS anchors as values, any other form id `[GAP]`, never invented; draft the **HoC-tagged CAPA** (`controls` / `smart_actions`), each tracing to a named cause with owner + due date. `incident_rates` is context only. Validate against `references/QUALITY_CHECKLIST.md`, then produce the output via the Output format section. A competent (DGMS-qualified) person reviews it.

## Agentic Execution (single-thread on this host)

Run the De-identifier FIRST (sequential gate — its scrubbed output feeds every later step), then work through the roster checklist sequentially in this one context, keeping the same decomposition discipline, and finish with the MANDATORY Critic/QA pass before delivery.

> Single-threaded fallback:

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

### Subagent roster for THIS skill
- **De-identifier** — runs FIRST (sequential dependency); scrub all PII/health detail —
  injured-party, witnesses, diagnoses, exact dates/locations, small injury cells — into role
  labels before any analysis. Returns the re-identification key SEPARATELY (to the orchestrator,
  not to any sibling). Everything below consumes only its scrubbed output.
- **A · Evidence & Timeline Reconstructor** — assemble the numbered, time-ordered event
  sequence and the numbered evidence log (E-1…) from the scrubbed inputs; flag [GAP].
  SCOPE-OUT: does not assign causes (B owns it) or decide reportability (C owns it).
- **B · Root-Cause Analyst** — apply the chosen method (5-Whys / ICAM / SCAT / Fishbone /
  Swiss-Cheese) via rca.py; every causal claim cites an evidence item (E-n); reach a
  systemic/organisational factor (rca.validate `reaches_systemic` true for whichever method).
  SCOPE-OUT: reportability (C owns it) and control selection (D owns it).
- **C · Regulatory Reportability Checker** — for the resolved jurisdiction (India → resolved
  STATE first), return verdict + clause/section + deadline + form (India state accident form
  via KB-REG-IN-STATEFORMS / UK RIDDOR / US OSHA 29 CFR 1904). Conservative — flag [GAP] and
  "ask a competent person" when unsure. SCOPE-OUT: does not draft the report or invent a form number.
- **D · Corrective-Action Drafter** — hierarchy-of-controls-tagged CAPAs, each tracing to a
  named cause (RC-n) with a named owner + ISO due date + measure; prefer higher-order controls,
  justify any PPE/admin-only. SCOPE-OUT: does not score causes (B) or check law (C).
- **Critic/QA** (MANDATORY) — adversarial read-only review: every cause evidence-backed, RCA
  reaches a systemic factor, reportability cited conservatively to the matched KB row, every
  CAPA traces to a cause with owner+date, no PPE/admin-only without justification, and ZERO
  PII/health leak (no residual identifier, no <5 cell, no re-id key in the output).

## Jurisdiction routing

| Jurisdiction | Read |
|---|---|
| India (mine) | ../../knowledge-base/regulatory/in-dgms.md (KB-REG-IN-DGMS — 24h notice + Form J; [GAP] elsewhere) + regulatory/in-mines-act.md (KB-REG-IN-MINES-ACT) |
| India (region) | ../../knowledge-base/regulatory/in-state-forms.md (KB-REG-IN-STATEFORMS — mandatory region/zone resolution before any form) |
| Any | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — 10.2 incident) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific DGMS form |

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
