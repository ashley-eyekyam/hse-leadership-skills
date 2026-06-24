---
name: dropped-objects-prevention
description: 'Produces a consultant-grade dropped-objects-prevention artifact for
  a named offshore installation, vessel, or at-height area — a DROPS survey + dropped-object
  register + reliable-securing controls + exclusion zones per the DROPS Recommended
  Practice (2017) / IADC HSE Guidelines Section 16 / API RP 2D & 54. Use it to run
  or review a DROPS survey, build a dropped-object register, classify static vs dynamic
  objects, set reliable-securing standards, or set exclusion zones below at-height
  work — not a generic ''wear hard hats below''. It is reliable-securing-led: the
  survey, reliable securing and exclusion zones are the primary controls; a ''hard
  hats below'' treatment is flagged and pushed up the hierarchy. Consequence banding
  uses the PUBLIC impact-energy method (energy approx. mass x g x fall height) with
  user-supplied mass and fall height; the licensed DROPS Calculator threshold values
  stay cite-only / [GAP]. It refuses a vague ''the platform'' or ''looks secured''.
  Decision-support only; competent-person review.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 2
  audience:
  - M
  - C
  industry:
  - O&G
  jurisdiction:
  - All
  - UK
  status: stable
  plugin: hse-marine-offshore
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Dropped Objects Prevention

The **hse-marine-offshore DROPS builder** — given a **named offshore installation, vessel, or
at-height work area** and the **dropped-object survey scope**, it produces a defensible
dropped-objects-prevention artifact: the **DROPS survey**, the **dropped-object register**
(static vs dynamic taxonomy), the **reliable-securing controls** (primary fixing + secondary
retention/tethering) and the **exclusion (red) zones** below at-height work. It grounds the
survey → taxonomy → securing-hierarchy → exclusion-zone duty in `KB-REG-DROPS` (DROPS
Recommended Practice 2017 / DROPS Reliable Securing / IADC HSE Guidelines Section 16 / API RP 2D
& RP 54) and ranks every control through `KB-SNIP-DROPS-SECURING`.

**It is reliable-securing-led — not "hard hats for the people below".** The primary controls of
every artifact this skill builds are the **DROPS survey, reliable securing (secondary retention)
and exclusion zones**; a treatment that leads with **"hard hats below"** for the people
underneath an unsecured at-height item is **flagged and pushed up the hierarchy of controls** —
PPE is the residual, never the headline. A dropped-objects artifact reduced to "wear hard hats"
with no survey or reliable securing is the indefensible paperwork this skill rejects.

**Consequence banding traces to the PUBLIC `m·g·h` method, never to invented or licensed
numbers.** Impact energy is the public physics (`E ≈ mass × g × fall height`,
`KB-DATA-DROPS-IMPACT`) computed with **user-supplied mass and fall height** — never invented. The
**licensed DROPS Calculator consequence-band threshold VALUES are cite-only**: the skill **records
the user's band** (from their licensed Calculator) or reports the `m·g·h` energy with the band
left **`[GAP]` / user-confirmed** (A1 `[ASSUMED]`, surfaced for the SME). It never reproduces the
licensed threshold table or hard-codes band boundaries. Decision-support only; a competent person
must review the output.

## When to use this skill

Use this skill when the user needs a **dropped-objects-prevention artifact for a concrete
offshore installation, vessel, or at-height work area** — for example "run a DROPS survey for the
drilling derrick on Platform Bravo", "build a dropped-object register for the crane boom and
monkeyboard", "set the reliable-securing standard for the at-height equipment on the riser deck",
or "establish the exclusion zone below the flare-tip maintenance". It is **not** for a generic
"how do I stop dropped objects?" answer: the Workflow intake below forces the named installation,
the survey scope, and the at-height items before any drafting, and refuses a vague "the platform"
or "looks secured" request. For the offshore safety-case context this artifact feeds, see the
sibling `offshore-safety-case` (MAR-01); for the EER/muster response, see `marine-emergency-response`
(MAR-03) — cross-referenced, never rebuilt here.

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

| Jurisdiction / scope | Read |
|---|---|
| Dropped-objects duty (every run) | ../../knowledge-base/regulatory/drops.md (KB-REG-DROPS) — the **survey → static/dynamic taxonomy → reliable-securing hierarchy → exclusion-zone** map (DROPS Recommended Practice 2017 / DROPS Reliable Securing / IADC HSE Guidelines Section 16 / API RP 2D & RP 54). Citation map only; the DROPS Calculator consequence-band table is **licensed → cite-only** (see KB-DATA-DROPS-IMPACT) |
| Consequence band (every banded object) | ../../knowledge-base/data-points/drops-impact.md (KB-DATA-DROPS-IMPACT) — the **public impact-energy method** `E ≈ m·g·h` (mass + fall height **user-supplied**) + **generic band labels only**; the licensed DROPS Calculator threshold VALUES stay **`[GAP]` / user-confirmed** (A1 `[ASSUMED]`). The skill **records the user's band; it never recomputes the licensed table or hard-codes boundaries** |
| Control order (every control) | ../../knowledge-base/prompt-snippets/drops-securing.md (KB-SNIP-DROPS-SECURING) — the **survey + reliable securing + exclusion zones FIRST** control spine; a "hard hats for those below" treatment is **rejected** (PPE-led), an at-height item with no recorded securing standard is **rejected**, a band asserted with hard-coded licensed thresholds is **rejected** |
| Marine/offshore clause cross-walk | ../../knowledge-base/prompt-snippets/marine-clause-map.md (KB-SNIP-MARINE-CLAUSE-MAP) — the bundle-shared standard → artifact → owning-skill cross-walk (DROPS RP → dropped-objects-prevention MAR-02; PFEER/SOLAS → MAR-03; SI 2015/398 → MAR-01) |
| UK / offshore regime | ../../knowledge-base/regulatory/drops.md (KB-REG-DROPS) read with the UKCS duty-holder regime; the DROPS survey + reliable-securing standard are the recommended-practice basis cited by topic, never reproduced |
| India | ../../knowledge-base/regulatory/in-offshore.md (KB-REG-IN-OFFSHORE) — **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** (CONV-8) |
| Unknown | Ask before citing any specific practice / standard |

This skill always grounds the survey → taxonomy → reliable-securing hierarchy → exclusion-zone
duty in `KB-REG-DROPS`, ranks every control through `KB-SNIP-DROPS-SECURING` (a "hard hats below"
treatment is rejected, never the headline), classifies consequence with the **public** `m·g·h`
method in `KB-DATA-DROPS-IMPACT` (mass + fall height **user-supplied**; the licensed DROPS
Calculator threshold VALUES stay `[GAP]` / user-confirmed — A1), places this artifact on the
marine/offshore cross-walk via `KB-SNIP-MARINE-CLAUSE-MAP`, and applies `KB-SNIP-HOC` to every
recommendation. For an India-touching installation, resolve the state via `hse-india` (**mandatory
state detection**) and emit a literal `[GAP]` where a state form/return is owed — never a minted
national form number (`KB-REG-IN-OFFSHORE`, CONV-8). The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the dropped-object survey walk one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "the platform" or "looks secured": you need the named
installation/area (Q1), the survey scope and at-height items (Q2–Q3), and the existing-securing
status (Q4) before any drafting.**

1. **The named installation / vessel / area** (free-text — the specificity anchor) — "Name the
   exact installation, vessel, or at-height work area + its operator/field (e.g. 'Platform Bravo
   drilling derrick, monkeyboard to drill floor'). **Refuse 'the platform' / 'offshore' — the
   survey is installation- and area-specific.**"
2. **Survey scope & at-height structures** (mcq, multi-select) — derrick / mast / crane boom &
   pedestal / monkeyboard & fingerboard / flare tip & boom / riser & wellhead deck / piping &
   small-bore fittings / lighting & instruments / other (+ detail) — the at-height inventory the
   DROPS survey covers.
3. **Object taxonomy** (mcq, multi-select; static vs dynamic) — static dropped object (falls from
   a static position — fitting, light, bolt) / dynamic dropped object (knocked, swung, or dropped
   during an operation — lifted load, swung tubular, tool). Every register entry is classified.
4. **Existing securing & condition** (free-text) — "What primary fixing + secondary retention
   (tethering/lanyards) is in place per at-height item, and its condition / last DROPS inspection?
   **An at-height item with no recorded securing standard is flagged immediately as a high-priority
   finding** — never assume an item is secured because it 'looks secured'."
5. **Consequence inputs** (free-text → `[GAP]` where unsupplied) — "For each banded object, the
   **mass (kg)** and the **fall height (m)** — both **user-supplied** (impact energy `E ≈ m·g·h`,
   `KB-DATA-DROPS-IMPACT`). If you have a DROPS Calculator consequence band, give it; **the skill
   records your band and leaves the licensed threshold values `[GAP]` — it never recomputes the
   licensed table or invents a mass/height.**"
6. **Jurisdiction** (mcq) — UK / UKCS / Norway / US / India / Other / Unknown. **India → resolve
   the state via `hse-india` (mandatory state detection); emit `[GAP]`, never a national form
   number (`KB-REG-IN-OFFSHORE`).**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
mass/height is a `[GAP]`, never an invented number; a missing securing standard is a finding.

Then: run the dropped-object survey + register, rank every control through `KB-SNIP-DROPS-SECURING`
(the `controls` engine — a "hard hats below" / PPE-led treatment is a FLAG pushed up the
hierarchy), compute the public `m·g·h` energy where mass + height are supplied and record the
user's DROPS band (thresholds `[GAP]`), re-score the residual on the `risk_matrix` 5×5, assign
`smart_actions` (owned + dated, incl. each `[GAP]`-closure), validate the draft against
`references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The
domain method is in `references/METHODOLOGY.md`.

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

For a multi-area DROPS survey the triage gate fans out to (the **De-identifier runs FIRST —
sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier — esp. a **named worker
  from a prior struck-by / fatality dropped-object incident** cited as context — to role labels
  before any analysis; return the re-identification key SEPARATELY to the orchestrator, never to a
  sibling. Most inputs are asset/installation data (this is the **lower de-id tier**), but the
  prior-incident context is special-category health data.
- **Survey-&-Register-Analyst** — enumerate the at-height items per area (derrick, monkeyboard,
  crane boom, flare tip, piping/fittings, lighting/instruments), classify each as **static vs
  dynamic** (`KB-REG-DROPS`), and record the existing primary-fixing + secondary-retention status
  per item — flag an at-height item with **no recorded securing standard** immediately as a
  high-priority finding. SCOPE-OUT: does not rank the control (the Securing-Controls-Engineer owns
  it) or compute the consequence band.
- **Securing-Controls-Engineer** — for each object, drive `KB-SNIP-DROPS-SECURING` (eliminate →
  reliable securing [primary fixing + secondary retention] → administrative [survey/register,
  inspection, exclusion zones] → PPE residual) and run the **`controls` engine** — a treatment led
  by **"hard hats for those below"** (`ppe_admin_only=True`) is a **FLAG pushed up the hierarchy,
  never the headline control**. Re-score the residual via `risk_matrix`. SCOPE-OUT: does not
  de-identify (De-identifier) or check the practice/standard (the SME persona).
- **Consequence-Band-Author** — for each banded object, compute the **public** `m·g·h` impact
  energy (`KB-DATA-DROPS-IMPACT`) with the **user-supplied** mass + fall height, and **record the
  user's DROPS Calculator band**; the **licensed threshold VALUES stay `[GAP]` / user-confirmed**
  (A1 `[ASSUMED]`) — never reproduce the licensed table, never invent a mass/height or a band
  boundary. SCOPE-OUT: does not select the securing control (the Securing-Controls-Engineer).
- **Critic/QA** (MANDATORY) — adversarial final pass: every at-height object has a reliable-securing
  control or a recorded FLAG, no "hard hats below" / PPE-led treatment accepted as the headline,
  every consequence band traces to its `m·g·h` inputs (no invented mass/height, no licensed
  threshold table), every citation resolves (DROPS RP / IADC §16 / API RP 2D/54), and ZERO
  de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the A7 `controls` /
`risk_matrix` / `smart_actions` calls and the per-object securing selection + `m·g·h` banding
inline, then the mandatory Critic/QA + SME pass — same scope discipline, no subagents.

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
