---
name: lift-plan
description: Creates consultant-grade, site- and lift-specific lifting plans grounded
  in LOLER 1998 Reg 8 and BS 7121. Use this skill whenever a user asks to plan, build,
  or review a lifting plan, a crane lift plan, or a lifting operation, to classify
  a lift as basic / standard / complex per BS 7121, to confirm a crane's SWL at radius
  and utilisation against the manufacturer's rated-capacity chart, to set exclusion
  zones near overhead power lines / structures / the public, to sequence a lift method
  with appointed-person / operator / slinger roles, or to set contingency and abort
  criteria. Reads SWL-at-radius and utilisation from the rated-capacity chart (transcribed,
  checked) — never computed. Refuses to plan without a confirmed load weight (incl.
  rigging), an equipment SWL at the working radius, and at least an appointed person.
  Enforces the hierarchy of controls (eliminate the lift / reduce the load / engineer
  an exclusion before PPE) and re-scores residual risk. Decision-support only; competent-person
  review required.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - Con
  jurisdiction:
  - All
  status: stable
  plugin: hse-construction
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Lift Plan (LOLER Reg 8 / BS 7121)

A consultant-grade HSE skill that produces a task/site-specific **lifting plan** for a
named lifting operation, grounded in **LOLER 1998 Regulation 8** (lifting operations
planned by a competent person, appropriately supervised, carried out safely) and **BS
7121** *Safe Use of Cranes* (the basic / standard / complex lift categorisation that sets
the planning depth and whether an appointed-person written plan is mandatory). The
**risk half** runs the standard HIRA loop grounded in **ISO 45001 clause 6.1.2** (the same
loop the `risk-assessment` flagship uses, reused verbatim) and re-scores residual risk on
the deterministic `risk_matrix` engine; the **lift half** sequences the safe method,
exclusion zones, roles, and abort criteria. It forces the single lever that separates a
defensible plan from copy-paste paperwork: a **confirmed load** on a **real crane at a real
radius** plus the full **hierarchy of controls** — never a PPE-only overhead-line control,
never a "should-be-fine" ground assumption.

**SWL-at-radius and utilisation are READ from the manufacturer's rated-capacity chart**
(transcribed by the user and checked against `KB-DATA-LIFT-CATEGORIES` thresholds), **never
computed** — this skill carries **no lifting calculator and no crane-capacity engine**
(D-08a). An unconfirmed load weight, a missing SWL-at-radius, or an absent appointed person
is a **refuse-to-plan** gate, not an assumption.

## When to use this skill

Use this skill when the user needs a **lifting plan for a concrete lift on a named site** —
for example "build a lift plan to set a 12 t AHU onto the level-6 plant deck with a 50 t
mobile crane", "classify this tandem lift over an occupied car park per BS 7121", "set the
exclusion zone for a lift adjacent to an 11 kV overhead line", or "review this appointed
person's lift plan". Trigger phrases: *lift plan, lifting plan, crane lift plan, lifting
operation, LOLER, LOLER Reg 8, BS 7121, basic/standard/complex lift, appointed person, SWL
at radius, utilisation, exclusion zone, tandem lift, blind lift, contingency / abort*. The
two load-bearing inputs are the **confirmed load weight (incl. rigging)** and the
**equipment SWL at the working radius**; if either is missing — or no appointed person is
named for a standard/complex lift — the Workflow intake below **refuses to proceed** until
they are elicited (never plans on an unconfirmed weight or unknown ground).

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
| UK    | ../../knowledge-base/regulatory/loler-bs7121.md (`KB-REG-LOLER-BS7121` — **LOLER 1998 Reg 8** plan/organise/supervise + **Reg 9** thorough examination + **BS 7121** lift categorisation, appointed-person, SWL-at-radius / exclusion-zone method) — pairs with ../../knowledge-base/regulatory/cdm-2015.md (CDM 2015 where the lift is part of construction works) |
| USA   | ../../knowledge-base/regulatory/osha-1926.md (**29 CFR 1926 Subpart CC** cranes & derricks in construction + Subpart H rigging) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) — **mandatory state detection; defers to `hse-india`; the IS / state crane-rules form is a literal `[GAP]`, never a minted national form number** |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Lift categorisation (every run) | ../../knowledge-base/data-points/lift-categories.md (`KB-DATA-LIFT-CATEGORIES` — BS 7121 basic / standard / complex thresholds + the SWL-at-radius utilisation + overhead-line / ground proximity tests, each a **transcribed-and-cited input**, never computed) |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 HIRA + 8.1.2 hierarchy of controls)
and applies `KB-SNIP-HOC` to every control. The lifting-specific grounding is **LOLER 1998
Reg 8 / Reg 9 + BS 7121** (`KB-REG-LOLER-BS7121`, read
`../../knowledge-base/regulatory/loler-bs7121.md` — the
lift-planning / appointed-person / SWL-at-radius citation map) together with
`KB-DATA-LIFT-CATEGORIES` (the BS 7121 category thresholds + the utilisation / proximity
tests — **values are read from the manufacturer's rated-capacity chart and checked against
these thresholds, never computed**). Where the lift is part of construction works it also
cites **CDM 2015** (`KB-REG-CDM2015`) and the bundle clause cross-walk
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP` (LOLER Reg 8 / BS 7121 → Lifting Plan row). For a **US**
lift it cites **29 CFR 1926 Subpart CC** via `KB-REG-OSHA1926`. For an **India** site it
resolves the state via `KB-REG-IN-STATEFORMS` (**mandatory state detection** — defers to
`hse-india`; confirm the state before citing any form; emit a literal `[GAP]`, **never a
national form number**) with the Factories Act framing in `KB-REG-IN-FACTORIES`. The rule-9
manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table (Q1
lift classification per BS 7121 [basic / standard / complex — complex / tandem / blind
mandates an appointed-person written plan + contingency] · Q2 the load [item, **weight incl.
rigging**, dimensions, centre of gravity, lifting points] · Q3 the equipment [crane type,
configuration, **SWL at the working radius**, utilisation] · Q4 site & proximity hazards
[overhead power lines · adjacent structures · public / highway · poor / unknown ground ·
confined radius · SIMOPS] · Q5 personnel & competence [appointed person, operator, slinger /
signaller — all named with the competence basis] · Q6 jurisdiction), the **mandatory India →
state branch** (Q6 = India → Q6a + `KB-REG-IN-STATEFORMS`, defers to `hse-india`, literal
`[GAP]`, never a national form number), the echo-back, and the refuse-on-vague anchors —
lives in **`references/intake.md`**. Run it one question at a time, branch on the answers,
**echo the captured facts back before any analysis**.

**The GATE (refuse-on-vague):** **no lift plan is produced** until **a confirmed load weight
(incl. rigging, Q2)**, **the equipment SWL at the working radius (Q3)**, and **at least an
appointed person (Q5, for a standard / complex lift)** are captured. The skill **refuses to
plan on an unconfirmed weight, an unknown SWL-at-radius, or a "should-be-fine" ground** — ask
again, or record `[ASSUMPTION]` / `[GAP]`; never invent a chart value, a weight, or a
clearance. **SWL-at-radius and utilisation are READ from the manufacturer's rated-capacity
chart** (transcribed at Q3 and checked against `KB-DATA-LIFT-CATEGORIES`) — **the skill never
computes a crane capacity** (D-08a).

### The lift-planning method (LOLER Reg 8 + BS 7121 + the ISO 45001 6.1.2 residual loop)

Full method in `references/METHODOLOGY.md`. The **risk half** is the standard HIRA loop
(reused verbatim from the `risk-assessment` flagship — **no second risk engine**); the
**lift half** sequences the safe method and uses **no engine**. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Any named operatives, slingers, or operators
   that arrive **as incident-style evidence** (e.g. an operator named in a prior dropped-load
   near-miss, a medical-fitness note) are scrubbed to **role labels**. *(The lift plan later
   carries the **named appointed person / operator / slinger** the user deliberately supplies
   at Q5 for the competence record — those are duty-holder assignments, not leaked PII; see
   the de-id exception in `references/deid-checklist.md`. A worker's **medical-fitness / health
   detail never belongs in the circulated plan** and is always scrubbed.)*
2. **Lift categorisation (BS 7121)** — classify the lift basic / standard / complex against
   `KB-DATA-LIFT-CATEGORIES` (the **highest** triggered criterion sets the category); the
   category sets the planning depth — a **complex** lift (tandem / multi-crane, blind, over
   the public / occupied area, load near the SWL, poor / unknown ground, overhead-line /
   structure proximity) mandates an **appointed-person written plan + contingency / abort
   criteria + supervision**. Cite the code + the triggering criterion.
3. **Load & rigging confirmation** — record the **confirmed load weight including rigging**,
   the dimensions, the centre of gravity, and the lifting points (Q2). An unconfirmed weight
   is a `[GAP]` and a **stop** — never assumed.
4. **Equipment SWL / utilisation (READ, not computed)** — transcribe the **SWL at the working
   radius** and the **utilisation %** from the **manufacturer's rated-capacity chart** (Q3),
   present each value as `<parameter> = <value> (<source: chart model, year>)`, and **check**
   it against the `KB-DATA-LIFT-CATEGORIES` utilisation test. If utilisation exceeds the
   planned safe-utilisation margin → **flag re-selection of the equipment** (a bigger crane /
   shorter radius), do **not** proceed. **No value is calculated by the skill** — a chart
   value that the user has not supplied is a `[GAP]`, never invented.
5. **Ground & proximity hazards (the hierarchy-of-controls lever)** — for each Q4 hazard
   propose controls and **apply `KB-SNIP-HOC`**: rank Elimination → Substitution → Engineering
   → Administrative → PPE; then call `controls.rank_controls` + `controls.validate_treatment`.
   The lift-specific lever: an **overhead-line** hazard is treated by **eliminating the lift
   in that zone / re-routing / an engineered exclusion zone or goal-posts and a banksman** —
   **a PPE-only or "operatives to take care / wear PPE" overhead-line control is a defect** the
   Critic/QA pass must catch (`ppe_admin_only=True` with no higher-order control and no
   justification). Set the **exclusion zone / segregation** from the proximity tests
   (overhead-line clearance per GS6, the load-radius swing, the drop zone).
6. **Initial + residual risk scoring** — for each residual hazard call
   `risk_matrix.load_matrix(config)` then `risk_matrix.score(likelihood, severity, matrix)`
   (default 5×5); re-score **with the selected controls applied** and call
   `risk_matrix.residual_delta(initial, residual)` for the movement. A residual High / Critical
   risk flags that additional controls or a **hold-point (do-not-lift)** are required — not
   "accept and proceed". **Residual scoring reuses `risk_matrix`; there is no lifting
   calculator.**
7. **Sequenced lift method + roles + contingency / abort** — author the **ordered** safe lift
   method (rig → trial-lift / weigh → travel → slew → place → de-rig), the **roles** (the named
   appointed person who plans / supervises, the operator, the slinger / signaller — each with
   the competence basis from Q5), the **weather / wind limits** (the chart's in-service wind
   speed), and the **contingency & abort criteria** (loss of communication, exceedance of the
   wind limit, an unplanned obstruction — the named stop conditions). This is a narrative, **no
   engine**.
8. **SMART actions (named owners + dates)** — for every control that is an action, produce a
   SMART action (specific, measurable, **assignable**, relevant, **time-bound (ISO due
   date)**) and call `smart_actions.validate_register`. Any action missing an owner, a valid
   date, a measure, or a hazard link is **invalid** and must be fixed — no anonymous actions,
   no "ASAP".
9. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check loop: the lift is
   categorised; the **load weight + SWL-at-radius + appointed person are confirmed** (or the
   plan is refused); SWL / utilisation values are **transcribed-and-cited, never computed**;
   every proximity hazard is HoC-ranked with **no un-justified PPE-only overhead-line control**;
   residual risk is re-scored; the method is sequenced with named roles, weather limits, and
   abort criteria; LOLER Reg 8 / BS 7121 (and CDM 2015 / 29 CFR 1926 / the India state form via
   `hse-india`) cited; de-id applied; no conclusion on an unstated assumption.
10. **Assemble the branded report** — build `report.json` (see
    `assets/lift-plan.report.json`) and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **deterministic scoring steps (6 via
`risk_matrix`) are A7 script calls in every case — never a fan-out job** (there is no
"Risk-Scorer" subagent); the **lift categorisation, the SWL transcription, and the sequenced
method use no A7 engine** (and there is **no lifting calculator** — D-08a).

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

This is the **STANDARD moderate roster** (A6 "moderate = 2–3"): the **De-identifier is the
sequential first gate** (not a fan-out peer), the fan-out jobs are
**Load-&-Equipment-Analyst + Site-&-Method-Author + Regulatory-Checker**, and **Critic/QA is
mandatory**. **There is no Risk-Scorer subagent** — residual scoring is the deterministic A7
`risk_matrix` script at step 6 — and **there is no SWL-Calculator subagent**: SWL-at-radius /
utilisation are **read from the manufacturer's rated-capacity chart** (transcribed + checked
against `KB-DATA-LIFT-CATEGORIES`), never computed (D-08a). A **basic** routine lift runs
single-threaded. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all
  incident-derived PII / health detail (a named operator from a prior dropped-load near-miss,
  any **medical-fitness / health note**) to role labels before any analysis (every fan-out job
  below consumes scrubbed text). The **appointed person / operator / slinger the user supplies
  at Q5 for the competence record stay named** — they are duty-holder assignments, not leaked
  PII; a worker's **medical-fitness detail is always scrubbed and never circulated**.
- **Load-&-Equipment-Analyst** — categorise the lift per BS 7121 against
  `KB-DATA-LIFT-CATEGORIES`; confirm the **load weight incl. rigging** (Q2); **transcribe** the
  **SWL-at-radius + utilisation from the manufacturer's rated-capacity chart** (Q3) and **check**
  them against the utilisation test — flag re-selection if over margin. **Reads, never
  computes** a capacity; an unconfirmed weight / SWL is a `[GAP]` and a stop. SCOPE-OUT: site
  controls + the method (Site-&-Method-Author), law (Regulatory-Checker).
- **Site-&-Method-Author** — from the Q4 proximity hazards set the **exclusion zones /
  segregation** and the HoC-ranked controls (**overhead-line → eliminate / engineered exclusion,
  not PPE**), then author the **sequenced lift method**, the **roles**, the **weather / wind
  limits**, and the **contingency / abort criteria**. SCOPE-OUT: the SWL transcription
  (Load-&-Equipment-Analyst), the residual score (the A7 `risk_matrix` script), law
  (Regulatory-Checker).
- **Regulatory-Checker** — for the resolved jurisdiction return the lifting-law grounding: **UK**
  LOLER 1998 Reg 8 / Reg 9 + BS 7121 (+ CDM 2015 where the lift is construction works); **US**
  29 CFR 1926 Subpart CC; **India** the state crane-rules form via `KB-REG-IN-STATEFORMS` (state
  confirmed first; defers to `hse-india`; literal `[GAP]`, never a national form number).
  Conservative, flag `[GAP]`. SCOPE-OUT: the load / SWL (Load-&-Equipment-Analyst), the method
  (Site-&-Method-Author).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (an **Appointed Person / Lifting Operations Specialist** to BS
  7121) before any output: the lift is correctly categorised; the load weight + SWL-at-radius +
  appointed person are confirmed (not assumed); SWL / utilisation are transcribed-and-cited (not
  computed); the overhead-line / proximity controls lead with elimination / engineered
  exclusion; the method is sequenced with abort criteria. It **never emits "approved by a
  competent person"**.
- **Critic/QA** (MANDATORY) — the lift is categorised; **load weight + SWL-at-radius + appointed
  person confirmed** (or the plan refused); **SWL / utilisation transcribed-and-cited, never
  computed**; **no un-justified PPE-only overhead-line control**; residual re-scored via the A7
  engine; method sequenced with named roles + weather limits + abort criteria; LOLER Reg 8 / BS
  7121 cited; the named appointed person / operator / slinger are duty-holders (legitimate) while
  **zero incident-derived PII / medical-fitness detail** leaks. PASS/FAIL.

A **basic** routine repetitive lift runs single-threaded — no subagents — but the A7
`risk_matrix` residual call and the Critic/QA pass are still made.

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
