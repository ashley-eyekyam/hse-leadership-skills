---
name: incident-rate-calculator
description: Computes and presents OSHA-standard lagging incident rates — TRIR, DART,
  and LTIFR — for a named site, period, and exposure base by calling the shared, tested
  incident_rates engine and presenting its returned figures verbatim; the model never
  does the arithmetic itself, so the result is deterministic, reproducible, and audit-defensible.
  Use this skill whenever a user asks to calculate an incident rate, a TRIR / DART
  / LTIFR, a recordable or lost-time injury frequency rate, or to benchmark a safety
  rate against an industry figure. It runs a lean intake (recordable / DART / lost-time
  counts, mandatory hours worked, the period, the base), refuses to fabricate a denominator
  or annualize a partial period, surfaces a divide-by-zero as an honest error not
  a fake zero, de-identifies any pasted case log to aggregate counts only, and emits
  a branded report carrying each rate with its formula, inputs, base, and optional
  benchmark (source + year). Decision-support only; a competent person must review
  the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: performance
  tier: 1
  audience:
  - M
  - E
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Incident Rate Calculator

A deterministic OSHA-standard lagging-rate calculator: it turns a short structured intake
(recordable / DART / lost-time counts, the **mandatory** hours worked, the period, and the
base convention) into **TRIR, DART, and LTIFR computed by the shared `incident_rates` engine
and presented verbatim**, plus a branded report that carries each figure with its formula,
inputs, and base. The one thing to internalise: **the model never does the arithmetic.**
Determinism is the whole value — a rate is defensible only if anyone can re-run the same
inputs through the same tested code and get the same number. So this skill **calls the
engine and presents the returned dict verbatim**; it must not compute, estimate, or even
"recompute to sanity-check" a rate in prose. The denominator is real hours worked (never
fabricated, never annualized from a partial period); a zero/missing denominator surfaces the
engine's honest `ValueError`, never a fake `0.0` that would read as "perfect safety".

## When to use this skill

Use this skill whenever the user needs an OSHA-standard lagging incident rate for a named
site and period: a **TRIR** (Total Recordable Incident Rate), a **DART** (Days-Away/
Restricted/Transfer rate), an **LTIFR** (Lost-Time Injury Frequency Rate), a recordable or
lost-time injury **frequency rate**, or a **benchmark comparison** of a computed rate against
an industry figure. Trigger phrases: *calculate an incident rate, TRIR, DART, LTIFR,
recordable incident rate, lost-time injury frequency rate, injury frequency rate, benchmark
our safety rate*. If the request omits the hours worked, the Workflow intake below **refuses
to proceed** until that mandatory denominator is supplied — a rate without its exposure base
is meaningless.

**When NOT to use this skill** (keeping B10 lean): to write the board narrative *around* these
figures use `board-safety-report`; to investigate the event behind a count use
`incident-investigation`; to assess a hazard use `risk-assessment`. B10 computes and presents
the rates — it does not narrate, investigate, or assess. **Severity rate is out of scope** —
the shared engine has no `severity_rate()`, so the calculator marks it a deferred `[GAP]` and
never computes it in-prompt.

<!-- hse:block:deid:start -->
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
<!-- hse:block:deid:end -->

<!-- hse:block:kb-selection:start -->
## Knowledge base (read ONE matching file — never load all)

Resolve the user's jurisdiction first. Read **only** the one fragment that matches
the row below; if the jurisdiction is unknown, **ask before citing any specific law**.
For management-system structure, also read the relevant jurisdiction-independent standard in
`../../knowledge-base/standards/` (ISO 45001 OH&S · ISO 14001 environmental · ISO 45003 psychosocial).
Always apply `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (KB-SNIP-HOC)
to every control recommendation. For any benchmark/figure, look up the ID in the relevant
`_registry.yaml`, then read ONLY the named file — and quote its `source`+`year`.
<!-- hse:block:kb-selection:end -->

<!-- The jurisdiction ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). Author the rows for the jurisdictions
     this skill serves; rule-9 checks every path/ID resolves against the KB registries. -->

<!-- B10 jurisdiction rows are LEAN: a rate is a number, not a statutory notice. The
     load-bearing rows are the STANDARD (ISO 45001 9.1 — the measurement basis) and the
     BENCHMARK (KB-DATA-TRIR-BENCHMARKS — never a bare number). The per-jurisdiction reads
     are CONSULTED ONLY to settle a recordability/countability definition (what counts as a
     recordable, a DART case, a lost-time injury) — they never change the maths. -->

| Jurisdiction / scope | Read |
|---|---|
| Standard (always) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — clause 9.1 monitoring, measurement, analysis & performance evaluation — the basis for measuring a rate) |
| Performance benchmark | ../../knowledge-base/data-points/incident-rates-benchmarks.md (KB-DATA-TRIR-BENCHMARKS — quote body + year + sector, never a bare comparator number) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (context only — recordability/notifiable-injury definition; resolve the state via in-state-forms.md if a statutory count is cited; mandatory state detection) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (context for RIDDOR-reportable counts feeding the rate) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (context for OSHA-recordable / DART counts under 29 CFR 1904) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (context for the EU counting framework) |
| Unknown | Ask before citing any specific recordability rule |

This skill always grounds in `KB-STD-ISO45001` clause **9.1** (monitoring, measurement,
analysis & performance evaluation — the basis for a defensible rate), reads every benchmark
from `KB-DATA-TRIR-BENCHMARKS` **with its source + year** (never a bare number), and
instantiates the `KB-SNIP-INTAKE` pattern in its lean intake. The per-jurisdiction rows are
consulted **only** to settle what *counts* (recordable / DART / lost-time) — they never alter
the engine's fixed bases. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Lean structured intake (run first, one question at a time)

B10 runs a lean, MCQ-heavy intake — the counts, the **mandatory** denominator, the period,
and the recordability standard. The full typed, branched intake — the `intake-coverage`
manifest, the question table (which rate(s) · **site/scope & period [anchor]** · recordability
standard → **India→state** · counts · **total hours worked [HARD refuse if blank/≤0]** · base
convention · optional benchmark), the **mandatory hours-gate** (Q4 blank/≤0 → hard refuse, no
rate without the denominator), the **mandatory India→state branch** (Q2b = India → Q2c), the
**severity-rate deferred `[GAP]`** discipline (D-03), the echo-back, and the refuse-on-vague
anchors — lives in **`references/intake.md`**. Run it one question at a time, branch on the
answers, **echo the captured facts back** before computing, and **never invent a count or a
denominator** — the hours worked is not optional; without it there is no rate, and **the model
never does the arithmetic** (the figure is the engine's returned value, verbatim).

### The calculation method (single-threaded — the model NEVER computes a rate)

This is the whole discipline of B10: **the maths lives only in the tested
`scripts/hse_components/incident_rates` engine, never in the prose.** Do not compute,
estimate, round, or "recompute to sanity-check" any rate — call the function and present
the returned dict **verbatim**.

1. **De-identify first** — if the user pasted a case log, the `deid` block above scrubs it to
   **aggregate counts only** before anything else: no per-case line, no individual identifier,
   and no injury/illness sub-group with fewer than 5 individuals (small-cell suppression).
   Only the aggregate counts reach Step 3.
2. **Confirm the denominator is real** — hours worked must be present and `> 0`. If it is
   missing, zero, or negative, do NOT compute: surface the engine's `ValueError`
   ("hours_worked must be > 0") honestly and ask for the real figure. **Never emit a fake
   `0.0`.** Never implicitly annualize a partial period — the period label is recorded, never
   used as a scaling factor.
3. **Call the engine** — for the selected rates call
   `incident_rates.compute_all(counts, hours_worked, period)` (or the individual
   `incident_rates.trir(...)` / `incident_rates.dart(...)` / `incident_rates.ltifr(...)`).
   The bases are the engine's locked constants (`OSHA_BASE = 200000`, `MILLION_BASE =
   1000000`) — they are NOT config and NOT recomputed in prose. On a host with **no Python
   sandbox**, do NOT fabricate a rate in-prompt: state that the deterministic calculator is
   unavailable and that the figure must be produced by running the engine.
4. **Benchmark (optional)** — only if Q6 supplied a benchmark WITH its source + year, call
   `incident_rates.benchmark_delta(rate, industry_rate)` and present the returned delta +
   direction. A bare comparator with no source is recorded `[GAP]`, never used.
5. **Severity rate — deferred `[GAP]` (D-03)** — the intake may list severity rate, but the
   shared engine has **no** `severity_rate()`; mark it `[GAP] — not computed (no validated
   engine in v1.0)` and **never compute it in-prompt**.
6. **Present the dict verbatim + the transparency trail** — surface each returned rate exactly
   as the engine returned it, alongside its formula (e.g. *TRIR = recordables × 200,000 ÷
   hours_worked*), the inputs, the base, and the period label — so a reviewer can re-run the
   same inputs and reproduce the number.

Then **validate against `references/QUALITY_CHECKLIST.md`** (the rate-defensibility self-check)
and **produce the output** via the Output format section below.

<!-- hse:block:orchestration:start -->
## Agentic Execution (Orchestration Block)
You are the ORCHESTRATOR for this skill. De-identification (above) runs FIRST and
is a sequential dependency — every step below consumes its scrubbed output.
Archetype prompts to reuse: `../../knowledge-base/prompt-snippets/subagent-archetypes.md` (KB-SNIP-ARCHETYPES).

### Step 0 — Triage: fan out at all?
Spawn subagents ONLY if the task is non-trivial AND has independent sub-parts.
Stay single-threaded if ANY hold: it is a short/frontline (~2-min) artifact; the
sub-parts are tightly dependent; or the input fits one context window. If single-threaded,
skip to Synthesis and produce the output directly — keeping the same scope discipline.

### Step 1 — Plan
Decompose into INDEPENDENT jobs. Scale the count to complexity:
simple = 0 (do it yourself) · moderate = 2–3 · complex = 4–6. Never exceed MAX=6.

### Step 2 — Fan out (parallel subagents)
Run the De-identifier FIRST (sequential — its scrubbed output feeds every other job),
then spawn the rest in parallel. Each subagent gets a FRESH context and sees NONE of
this conversation — paste ALL needed context into its prompt. Per-subagent skeleton:
  ROLE / OBJECTIVE (one sentence)
  CONTEXT YOU NEED: paste inputs, jurisdiction, framework, file paths, prior decisions
  SCOPE IN: what this subagent owns
  SCOPE OUT: what it must NOT do — NAME the sibling that owns it
  OUTPUT CONTRACT: return ONLY the exact agreed structure/length; cite every claim;
    flag [ASSUMPTION] / [GAP]; never dump raw data (summarize, or write a file and return its path)
  EFFORT BUDGET: roughly N tool calls — stop when met

### Step 3 — Synthesis (you)
Gather the outputs, resolve conflicts explicitly (state which source wins), de-duplicate,
and assemble the deliverable in this skill's output format.

### Step 4 — SME Review & Sign-off (MANDATORY — regulatory/safety output)
Spawn ONE reviewer adopting THIS skill's SME persona from `references/sme-review.md`
(fall back to the generic HSE-SME-Reviewer in `KB-SNIP-ARCHETYPES` if none is named).
Give it the draft + the inputs + the output contract. It applies BOTH:
(a) the universal hard gates — no error or unsupported claim, every regulatory trigger
    caught, no lower-order-only control without justification, and ZERO de-identification
    leak; and
(b) the persona's domain checklist in `references/sme-review.md`.
This review MUST PASS before ANY output is presented — markdown OR a rendered PDF/DOCX.
Fix everything it raises and re-run until clean. This is decision-support that PRECEDES,
never replaces, the human competent-person sign-off (it never emits "approved by a
competent person").

> Single-threaded fallback: if your host has no subagent capability, perform the SME
> Review & Sign-off pass yourself in THIS context — run the de-identification scrub
> first, keep the scope discipline, apply the persona checklist + universal gates, and
> pass the review before presenting any output (markdown or rendered).
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed). B10 copies B3's canonical single-thread
     line VERBATIM (it is a short deterministic wrapper), the one difference from
     B3 being that B10 DOES wire the incident_rates engine via scripts/. -->

- Single-threaded by design — no subagents.
- **SME Reviewer** (MANDATORY pre-output gate, run inline) — the skill-specific SME sign-off
  in **`references/sme-review.md`** (OSHA/RIDDOR recordability & safety-statistics SME): is
  each count classified to the right recordability rule, the denominator real and period-actual
  (not annualized), the base correct, and the figure presented as the engine returned it —
  never re-computed in prose? FLAG-only; does not block.

The Step-0 triage gate keeps B10 single-threaded (all three single-thread conditions hold: it
is a short deterministic ~2-min artifact, its parts are tightly dependent — the rate cannot be
presented before the engine returns it — and the input fits one context window), so the
orchestration block self-deactivates at runtime and the skill computes and presents the rates
directly. The inline **de-identification scrub still runs first** (any pasted case log is
reduced to aggregate counts before computation), the inline **SME Reviewer pass**
(`references/sme-review.md`) runs before output, and the **mandatory Critic/QA pass still runs**
inline (a single adversarial self-check that the figure came from the engine — not from
in-prompt arithmetic — that the denominator is real, and that no per-case line or <5 cell
leaked). On a host with no subagent capability nothing changes — B10 was already
single-threaded; on a host with no Python sandbox the calculator refuses to fabricate a rate
rather than degrade to in-prompt maths.

<!-- hse:block:report-output:start -->## Output format

Assemble a `report.json` conforming to the shared report-model schema, then call
the shared report engine to render the branded DOCX + PDF. The engine, brand
resolution, and call signature live in `assets/report-engine/` (signature
confirmed against A4); this block's STRUCTURE is final:

1. Build `report.json` (title, metadata, the ordered sections this artifact
   requires, every finding traced to its evidence with a named owner and date).
2. Resolve branding: the user's `brand.yaml` overrides the Eyekyam default.
3. Render both DOCX and PDF from the one `report.json` via the shared engine.
4. Surface the output paths and a one-line provenance note to the user.
<!-- hse:block:report-output:end -->

<!-- hse:block:attribution:start -->
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
<!-- hse:block:attribution:end -->

## Reference material

On-demand pointers (read only when needed):

- `references/METHODOLOGY.md` — the domain method this skill applies.
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
