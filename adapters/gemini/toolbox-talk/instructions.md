# toolbox-talk

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

# Structured intake — toolbox-talk

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Topic / primary hazard** of this talk | MCQ + free-text | Working at height / Confined space / Manual handling / Electrical-LOTO / Hot work / Mobile plant-vehicles / Hazardous substances / Slips-trips-housekeeping / Lifting operations / Heat-cold stress / Other (free-text) — drives the `data-points/` hazard-fact lookup | ELI-SUBJECT / ELI-SCOPE | always |
| Q2 | **Trade / crew** receiving the talk | MCQ + free-text | Construction-general / Maintenance / Electrical / Mechanical-fitters / Operators-process / Drivers-logistics / Cleaners-housekeeping / Mixed crew / Other (free-text) — calibrates language + which controls are foregrounded | ELI-EXPOSURE / ELI-INDUSTRY | always |
| Q3 | **Site / area & the specific task today** | free-text | "Name the site/area and the exact task — e.g. 're-roofing Bay 3, cherry-picker out of service, working off the leading edge'." — **the load-bearing specificity anchor; refuse a vague answer** ("general site work") — ask again or record `[GAP]`; never proceed generic | ELI-SUBJECT / ELI-LOCATION | always |
| Q4 | **Duration target** for the talk | MCQ | **<5 min (default)** / 5–10 min / 10–15 min — caps script length; <5 min is the frontline norm | ELI-OUTPUT | always |
| Q5 | **A recent relevant incident / near-miss** | free-text (optional) | "Optional — a recent near-miss/incident relevant to this hazard, on this site or in your org. Leave blank and a clearly-labelled *typical* example is used instead." — if supplied, **de-id scrub before use** (Decision 6); if blank, a labelled illustrative example, **never a fabricated local event** | ELI-EVIDENCE | always |
| Q6 | **Reading level / language** for the crew | MCQ | Plain-simple English (default) / Standard / ESL-friendly (short sentences) / Other language (name it, free-text) | ELI-OUTPUT | always |
| Q7 | **Jurisdiction** (light-touch) | MCQ | India ; (which state?) / UK / USA / EU / **Not jurisdiction-specific (default)** — used only if the talk must name a local rule; India → ask the state (mandatory state detection) only if a statutory point is actually raised | ELI-JURIS | always |

anchor** — refuse a vague answer ("general site work"); `[GAP]` if absent; never proceed

## Agentic Execution (single-thread on this host)

Work through the roster checklist sequentially in this one context, keeping the same decomposition discipline.

Single-threaded fallback: if your host has no subagent capability, perform the SME Review & Sign-off pass yourself in THIS context — run the de-identification scrub first, keep the scope discipline, apply the persona checklist + universal gates, and pass the review before presenting any output (markdown or rendered).

## Output format

This host has no Code Interpreter, so emit the deliverable as a **structured markdown report** following the house section order (Cover → Classification → Executive summary → Scope & method → Key findings (risk-rated) → Hierarchy-of-controls table → Recommendations (owner/due) → Regulatory basis → Limitations & de-id notice). Apply the A7 logic as prompt-side discipline: rank every control by the hierarchy of controls (no PPE-only treatment without justification) and give every SMART action a named owner and a due date — by instruction, not a script call. The report stays specific, HoC-ranked, de-identified, and owner/date-bearing.

## Subagent roster (preserved as a sequential checklist)

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed). B3 is the CANONICAL single-thread exemplar:
     the roster is exactly one line. B10 (incident-rate-calculator) and any future
     ~2-min skill copy this line verbatim. -->

- Single-threaded by design — no subagents.
- **SME Reviewer** (MANDATORY pre-output gate, run inline) — the skill-specific SME sign-off
  in **`knowledge/sme-review.md`** (frontline safety supervisor / crew lead): is the talk
  about THIS task/crew/site today, deliverable in the target time, with real controls and a
  real (or clearly-labelled typical) incident — not generic patter? FLAG-only; does not block.

The Step-0 triage gate keeps B3 single-threaded (all three single-thread conditions
hold: it is a short/frontline ~2-min artifact, its parts are tightly dependent, and the
input fits one context window), so the orchestration block self-deactivates at runtime
and the skill assembles the talk directly. The inline **de-identification scrub still
runs first**, the inline **SME Reviewer pass** (`knowledge/sme-review.md`) runs before
output, and the **mandatory Critic/QA pass still runs** (a single adversarial
self-check that the talk is specific, HoC-ranked, evidence-based, and PII-free before
delivery). On a host with no subagent capability nothing changes — B3 was already
single-threaded, the cleanest demonstration that the block degrades to nothing while
preserving the de-id + Critic discipline.

## Jurisdiction routing

_Full detail moved to the knowledge upload (see `knowledge/`)._

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
