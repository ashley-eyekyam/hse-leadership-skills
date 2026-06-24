---
name: regulatory-returns
description: Determines and prepares mandatory HSE regulatory returns for a named
  organisation across jurisdictions — OSHA recordkeeping (Forms 300/300A/301) and
  electronic submission, UK RIDDOR reports, and EU equivalents. Use this skill whenever
  a user asks which incidents are recordable or reportable, how to complete OSHA 300/300A/301,
  whether something is RIDDOR-reportable, what the reporting deadlines are, or to
  prepare a periodic statutory return. It applies the jurisdiction's recordability/reportability
  tests, identifies the correct form and deadline, and prepares a de-identified return
  with the evidence trail. For India, it defers entirely to the hse-india skills (state
  forms, accident notices) and never hard-codes national form numbers; state detection
  is mandatory. Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 3
  audience:
  - M
  - C
  - F
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-operations
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Regulatory Returns

A consultant-grade HSE skill that determines and prepares a **mandatory statutory
return** for a named organisation, with a **jurisdiction branch** — **US OSHA 29 CFR
1904** recordkeeping (Forms **300** log / **300A** annual summary / **301** incident
report + the 1904.41 electronic submission), **UK RIDDOR 2013** (specified injuries,
over-7-day incapacitation, reportable diseases, dangerous occurrences, the
report-within-15-days rule), **EU member-state equivalents**, and **India → defers
entirely to the `hse-india` skills** (state forms, accident notices) with **mandatory
state detection and no hard-coded national form numbers**. It forces the single lever
that separates a defensible return from guesswork: every recordability/reportability
decision is **traced to the named test it applied**, tied to the **correct form + the
exact deadline**, and prepared as a **de-identified return with an evidence trail**.
A statutory return holds injured-person identity **by law** — so this is one of the
highest-de-identification-sensitivity skills (see `references/deid-checklist.md`).

## When to use this skill

Use this skill when the user needs to determine or prepare a **specific statutory HSE
return** for a named organisation and a real incident or reporting period. Trigger
scenarios that reinforce the `description`:

- "Is this incident **recordable** on the OSHA 300 log?" / "Complete our **300A**
  annual summary." / "Fill the **301** incident report." / "Do we have to **submit
  300A electronically** this year?"
- "Is this **RIDDOR-reportable**?" / "Which RIDDOR category — specified injury,
  over-7-day, disease, dangerous occurrence — and **what's the deadline**?"
- "Prepare our **periodic statutory return**" / "What's the **300A posting window**?"
- For **India**: "Prepare our state Factories Act return / accident notice" → this
  skill **runs state detection and routes to `hse-india`** (`factories-act-returns` /
  `india-accident-notice` / `india-state-form-finder`); it **never mints a national
  form number**.

If the request is vague, the Workflow intake below **refuses to give a
reportable/recordable yes-or-no until the incident facts the test needs are captured**,
and **never asserts a deadline without the jurisdiction**.

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

Resolve the jurisdiction FIRST (intake Q1), then read **only** that row. The
recordability/reportability decision logic + the per-jurisdiction deadlines live in
`KB-DATA-RECORDABILITY-TESTS` (each test cited); the determine→form→deadline→prepare
method is `KB-SNIP-RETURNS-METHOD`; the operations clause cross-walk is
`KB-SNIP-OPS-CLAUSE-MAP`. For **India**, do **not** read a national form value from
here — run **mandatory state detection** and **route to `hse-india`** (the three-tier
degrade below); an unverified form is a `[GAP]`, **never a minted number**.

| Jurisdiction / scope | Read |
|---|---|
| USA — OSHA 1904 (300 / 300A / 301 + electronic) | ../../knowledge-base/regulatory/us-osha.md (KB-REG-US-OSHA — the 1904 recordkeeping leg) |
| UK — RIDDOR 2013 | ../../knowledge-base/regulatory/uk-hswa.md (KB-REG-UK-HSWA — RIDDOR specified injuries / over-7-day / disease / dangerous occurrence) |
| EU — member-state equivalent | ../../knowledge-base/regulatory/eu-osh.md (KB-REG-EU-OSH) |
| India — DEFERS to `hse-india` (state detection MANDATORY) | ../../knowledge-base/regulatory/in-factories-act.md + ../../knowledge-base/regulatory/in-state-forms.md (for the detected state) + ../../knowledge-base/regulatory/in-portals.md — route to the `hse-india` skills `factories-act-returns` / `india-accident-notice` / `india-state-form-finder`; never a national form number; unverified → `[GAP]` |
| Unknown | Ask before citing any specific law, form, or deadline |

**India three-tier deferral (the D-04 graceful degrade — never hard-blocks):**

1. **Subagent** — where subagents are supported, spawn one that runs the relevant
   `hse-india` skill (`factories-act-returns` for the state return, `india-accident-notice`
   for the statutory accident notice, `india-state-form-finder` to resolve the form),
   and fold its output into the integrated return.
2. **Main-thread inline** — on hosts without subagents, the main thread reads
   `KB-REG-IN-FACTORIES` / `KB-REG-IN-STATEFORMS` / `KB-REG-IN-PORTALS` inline and
   produces the India leg single-threaded.
3. **Routing prose + `[GAP]`** — if `hse-india` is not installed at all, emit routing
   prose naming the skill to run (`factories-act-returns` / `india-accident-notice` /
   `india-state-form-finder`) + the KB pointer + a `[GAP]` for any unverified form
   value. **At every tier: mandatory state detection first; never mint a national form
   number; never hard-block.**

The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table,
and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run it one
question at a time, branch on the answers, and **echo the captured facts back before
any analysis**. The five questions (per the build spec):

1. **Jurisdiction** (MCQ: US OSHA · UK RIDDOR · EU member-state · **India → defers to
   `hse-india`, runs mandatory state detection**). Branch per jurisdiction's tests.
2. **Return type** (MCQ per jurisdiction: US — 300 log / 300A summary / 301 incident
   report / electronic 300A; UK — specified injury / over-7-day / disease / dangerous
   occurrence).
3. **Incident facts** (free-text: nature, outcome, days away/restricted, whether a
   specified injury — these **drive** the recordability/reportability test; the
   specificity anchor).
4. **Organisation profile** (size / SIC — for OSHA electronic-submission applicability).
5. **Period** (for periodic returns / the 300A posting window).

**Refuse-on-vague anchors (the core-value lever):**

- **Never give a "reportable / recordable yes-or-no" until the incident facts the test
  needs (Q3) are captured** — ask again, or record `[ASSUMPTION]` / `[GAP]`; never
  invent a fact to force a determination.
- **Never assert a deadline without the jurisdiction (Q1)** — the deadline is a
  function of the jurisdiction's test (e.g. RIDDOR 15-day rule vs OSHA 300A posting
  window); stating one without the other is a defect.
- For **India**, Q1 = India → **mandatory state detection** then route to `hse-india`;
  never cite a national form number.

### The recordability/reportability method (determine → form → deadline → prepare)

Full method in `references/METHODOLOGY.md` (`KB-SNIP-RETURNS-METHOD`). Steps:

1. **De-identify the inputs FIRST** — before any drafting (the `deid` block above +
   the De-identifier-runs-first orchestration rule). A statutory return holds
   injured-person identity **by law**: the legally-required submission is named and
   access-controlled; every internal/shared/working copy is **role-labelled**, with
   `<5` suppression on any aggregated summary, and **no re-identification key embedded**
   (the reinforced `references/deid-checklist.md`).
2. **Apply the jurisdiction's recordability/reportability test** — for the resolved
   jurisdiction (Q1), run the cited decision logic in `KB-DATA-RECORDABILITY-TESTS`
   against the incident facts (Q3): OSHA 1904 recordability (work-relatedness, new
   case, beyond first-aid, days-away/restricted); RIDDOR reportability (specified
   injury reg. 4/Sch. 1, over-7-day reg. 4, disease reg. 8/9, dangerous occurrence
   reg. 7/Sch. 2). State the verdict **with the test cited**; flag `[GAP]` where a
   fact is missing — never assume to force a "yes" or a "no".
3. **Identify the correct form** — from the verdict + return type (Q2): OSHA 300 / 300A
   / 301 (+ 1904.41 electronic where the org profile (Q4) triggers it); the RIDDOR
   category; the EU member-state equivalent. For **India**, **do not name a form here**
   — route to `hse-india` (three-tier degrade above); unverified → `[GAP]`.
4. **Calculate the deadline** — from the jurisdiction's rule (RIDDOR within 15 days;
   OSHA 300A posted Feb 1–Apr 30 and electronically submitted by the 1904.41 date) and
   the period (Q5). Never assert a deadline without the jurisdiction.
5. **Prepare the de-identified return + the evidence trail** — assemble the return
   from the role-labelled facts, each determination linked to the **evidence item**
   that supports it; any follow-up action carries a **named owner + an ISO due date**
   (`smart_actions.validate_register`). No anonymous actions, no "ASAP".
6. **Validate against `references/QUALITY_CHECKLIST.md`** — every determination cites
   the test it applied; the correct form + the exact deadline; India routes to
   `hse-india` (no national form number); the output is de-identified with `<5`
   suppression and no embedded key; every conclusion traces to evidence.
7. **Assemble the branded report** — build `report.json` (see
   `assets/regulatory-returns-report.template.json`) and run the canonical
   `report-output` call below.

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
     is presence-only (never diffed), so each skill names its own jobs here. -->

**Single-threaded by default** — a single determination + form-prep is a focused,
tightly-dependent task (the De-identifier scrub still runs FIRST). For a **multi-incident
periodic return batch** the triage gate fans out to **2** (De-identifier FIRST →
Determination-&-Form-Preparer), then the mandatory review gates. Archetypes:
`KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer). A statutory
  return holds injured-person identity **by law**: scrub names, government IDs (SSN /
  NI / Aadhaar), contacts, exact dates/locations, and **all health detail** to stable
  role labels in every internal/shared/working copy; apply `<5` suppression to any
  aggregated summary (e.g. a 300A by department); **return the re-identification key
  SEPARATELY to the orchestrator — never embed it** in the return. Distinguish the
  legally-required submission (named, access-controlled) from the circulated copy
  (role-labelled) per `references/deid-checklist.md`. Everything below consumes only
  its scrubbed output.
- **Determination-&-Form-Preparer (India → `hse-india`)** — for the resolved
  jurisdiction, apply the cited recordability/reportability test
  (`KB-DATA-RECORDABILITY-TESTS`) to the scrubbed incident facts, return the verdict +
  the correct form + the exact deadline + the prepared de-identified return, each
  determination traced to its evidence item. **For India this job DEFERS to `hse-india`
  via the three-tier degrade:** (1) run the relevant `hse-india` skill
  (`factories-act-returns` / `india-accident-notice` / `india-state-form-finder`) as a
  subagent; (2) on no-subagent hosts, the main thread reads `KB-REG-IN-FACTORIES` /
  `KB-REG-IN-STATEFORMS` / `KB-REG-IN-PORTALS` inline; (3) if `hse-india` is not
  installed, emit routing prose naming `factories-act-returns` + a KB pointer + a
  `[GAP]`. **State detection is mandatory first; it NEVER mints a national form number;
  it NEVER hard-blocks.** SCOPE-OUT: de-identification (the De-identifier owns it).
- **Critic/QA** (MANDATORY) — adversarial final pass: every determination cites the
  test it applied; the correct form + the exact deadline; India routed to `hse-india`
  with no minted national form number; specificity (no reportable yes/no on missing
  facts); ZERO de-identification leak (no residual identifier, no `<5` cell, no
  embedded re-id key). PASS/FAIL.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md` (the **Regulatory Reporting
  Specialist**); decision-support that precedes — never replaces — the human
  competent-person review.

Simple single-incident determinations run single-threaded — no subagents — but the
De-identifier scrub, the cited-test discipline, and the Critic/QA + SME passes still run.

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
- `references/intake.md` — the structured-intake coverage contract + Q-table.
- `references/sme-review.md` — the per-skill SME sign-off personas + checklist.
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
