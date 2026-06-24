# driver-fatigue-management

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

# Structured intake — driver-fatigue-management

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named fleet / operation** (the fleet / route / depot / operation + function) | free-text | "Name the exact fleet / route / depot / operation + function (e.g. 'night-trunk fleet, route R-204, Midlands depot'). **Refuse 'our drivers' / 'the fleet' — the assessment is operation-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **Jurisdiction & rule-set** (selects the HOS rules) | mcq | USA (FMCSA 49 CFR 395) / EU (Reg 561/2006) / UK (GB drivers' hours — read with EU 561) / India / Other / Unknown | ELI-JURIS | always |
| Q2a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q2 == India |
| Q3 | **The driver duty log** (the IEEE-of-this-skill computation input) | free-text | "Give the shift as an ordered list of `{status, hours}` segments (`status` ∈ driving / on_duty / off_duty / sleeper; `hours` a float), or attach the ELD / tachograph download. **Refuse to compute on a missing or vague log → record a `[GAP]` and request the ELD/tachograph download; never invent driving hours, a rest segment, or a duty figure.**" | ELI-EXPOSURE | always |
| Q4 | **Multi-day cycle & cross-shift rest** (the `[GAP]` discipline) | free-text | "The 7-/8-day cumulative on-duty figure (for the FMCSA 60/70 h cycle + 34 h restart) and the cross-shift daily rest. **A single-shift log cannot evidence the multi-day cycle or the cross-shift rest — if not supplied, record a literal `[GAP]`; NEVER assert the cycle/restart compliant from one shift.**" | ELI-EVIDENCE | always |
| Q5 | **Proposed controls** (the core-value gate) | free-text | "What fatigue controls are proposed? **A 'stay alert' briefing / driver-alertness training / an in-cab fatigue-detection gadget as the HEADLINE control is a FLAG pushed up the hierarchy** — fatigue is led by roster / journey-plan / built-in-rest (FRMS) redesign; alertness measures are at most administrative / engineering backstops." | ELI-OBLIGATIONS | always |
| Q6 | Industry / setting | mcq+free-text | Road haulage / Last-mile & distribution / Passenger transport / Mixed-fleet (+ detail) | ELI-INDUSTRY | always |
| Q7 | Location / depot / operating area | free-text | "Which specific depot / operating area / route network is this?" | ELI-LOCATION | always |
| Q8 | Output artifact wanted + its reader | mcq | full fatigue-risk-management report (consultant) / HOS-compliance + FRMS summary (manager) / the roster fix-list (planner) | ELI-OUTPUT | always |
| Q9 | **Action owner(s) + verifier** | free-text | "Who owns the roster-redesign / FRMS / [GAP]-closure actions and who is the competent person reviewing the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q10 | **Review cycle / next review** | mcq+free-text | on-roster-change / on-ELD-exception / quarterly (or sooner) / other (+date) | ELI-TEMPORAL | always |

| Q3 | **The driver duty log** (the IEEE-of-this-skill computation input) | free-text | "Give the shift as an ordered list of `{status, hours}` segments (`status` ∈ driving / on_duty / off_duty / sleeper; `hours` a float), or attach the ELD / tachograph download. **Refuse to compute on a missing or vague log → record a `[GAP]` and request the ELD/tachograph download; never invent driving hours, a rest segment, or a duty figure.**" | ELI-EXPOSURE | always |

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

