---
name: noise-exposure-health-surveillance
description: 'Produces an occupational-noise exposure assessment and a hearing-conservation
  / audiometric-surveillance plan for a named area or similar-exposure group (SEG):
  compares measured or estimated noise to the cited action and limit values, maps
  exposure zones, ranks noise-reduction controls up the hierarchy (source → engineering
  → administrative → hearing protection LAST), and sets an audiometry schedule (baseline
  / annual / standard-threshold-shift triggers). Use this skill to assess noise exposure,
  build a hearing-conservation program, set up audiometric surveillance, compare a
  TWA / L_EX,8h to the 85/90 dBA (OSHA) or 80/85/87 dB(A) (UK) action and limit values,
  or plan noise reduction for an area or task. It transcribes measured levels (no
  dosimetry computed), cites each action level / limit with authority and year, refuses
  a schedule on a vague basis, and treats standard-threshold-shift audiometry as special-category
  health data reported by SEG/role. Decision-support only; a competent person must
  review it.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: occ-health
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - Mfg
  jurisdiction:
  - All
  status: stable
  plugin: hse-manufacturing
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Noise Exposure Health Surveillance

A consultant-grade **occupational-noise exposure assessment + hearing-conservation /
audiometric-surveillance plan** for a **named area or similar-exposure group (SEG)**. It
takes **measured or estimated** noise exposure (it **transcribes** the value — it does **not**
compute dosimetry), compares each to a **cited action level / exposure limit with authority +
year** (US OSHA 1910.95 85/90 dBA; UK Control of Noise at Work Regs 2005 80/85/87 dB(A)), maps
the area into **exposure zones**, ranks **noise-reduction controls up the hierarchy** (source →
engineering → administrative → **hearing protection LAST**), and sets an **audiometry
surveillance schedule** (baseline / annual / **standard-threshold-shift (STS) triggers**). It
forces the single lever that separates a defensible artifact from copy-paste paperwork:
exposure-basis specificity (no schedule on "it seems loud") plus the full hierarchy of controls
— never a vague, hearing-protection-only treatment. Audiometric / STS results are
**special-category health data**: reported by **SEG/role**, `<5` health-outcome cells
suppressed, never circulated with names. Decision-support only; a competent person
(occupational hygienist / audiometric technician / OH physician) must review the output.

## When to use this skill

Use this skill when the user needs a **noise exposure assessment or a hearing-conservation /
audiometric-surveillance plan** for a **concrete area, task, or asset** — for example "assess
the press-shop noise exposure and set up audiometry", "build a hearing-conservation program for
the grinding bay", "map the plant's noise exposure zones", or "set an audiometry schedule for
the operators above the action level". Trigger phrases: *noise exposure, occupational noise,
noise assessment, hearing-conservation program, audiometric / hearing surveillance, audiometry,
standard threshold shift / STS, action level, exposure (noise) zone, L_EX,8h / LEP,d / TWA,
ear defenders / hearing protection*. If the request is vague ("it seems loud"), the Workflow
intake below **refuses to set a surveillance schedule** until an **exposure basis** + a **named
area/SEG** + **≥ an estimated TWA** (or a documented `[GAP]` to measure) are captured — it
never invents a dB figure.

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
| USA | ../../knowledge-base/regulatory/osha-1910-95.md (KB-REG-OSHA1910-95) — **85 dBA** action level (hearing-conservation program + audiometry) / **90 dBA** PEL, 8-hr TWA |
| UK | ../../knowledge-base/regulatory/uk-hswa.md — Control of Noise at Work Regs 2005: lower action **80 dB(A)**, upper action **85 dB(A)**, limit **87 dB(A)** (at-ear) |
| EU | ../../knowledge-base/regulatory/eu-osh.md — Directive 2003/10/EC (same 80/85/87 dB(A) structure) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) — **defers to `hse-india`; mandatory state detection; emit literal `[GAP]`, never a national form-id** |
| Unknown | Ask before citing any specific law |
| Noise method (every run) | ../../knowledge-base/standards/iso1999-9612.md (KB-STD-ISO1999-9612) — ISO 9612 measurement method + ISO 1999 NIHL estimation; the skill **transcribes** the measured value, it does **not** compute dosimetry |
| Noise-control hierarchy (every control) | ../../knowledge-base/prompt-snippets/noise-control-hierarchy.md (KB-SNIP-NOISE-CONTROL-HIERARCHY) — source/substitution → engineering enclosure/damping → distance/time admin → hearing protection LAST; **HPD as the first/only control is flagged** |
| Manufacturing clause map | ../../knowledge-base/prompt-snippets/manufacturing-clause-map.md (KB-SNIP-MANUFACTURING-CLAUSE-MAP) — ISO 45001 §6.1.2 / §8.1.2 cross-walk for the regulatory-basis section |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and the `KB-SNIP-MANUFACTURING-CLAUSE-MAP`,
applies `KB-SNIP-HOC` + `KB-SNIP-NOISE-CONTROL-HIERARCHY` to every control (hearing protection
**LAST**), resolves the **action level / exposure limit** against the cited jurisdiction
threshold (OSHA 1910.95 `85/90 dBA` · Noise Regs 2005 `80/85/87 dB(A)`) with authority + year,
and grounds the measurement/estimation method in `KB-STD-ISO1999-9612` — **no dosimetry is
computed by the skill** (D-08a). For an India site, resolve the state via the India branch and
defer to `hse-india`; emit a literal `[GAP]` and **never a minted national form-id**. The
rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the six-question table, the
mandatory **India → state** branch, the **no-exposure-basis → measure-first** branch, the
echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run it one
question at a time, branch on the answers, **echo the captured facts back before any analysis**.
The load-bearing questions:

1. **Q1 — Exposure-data basis** (MCQ): *measured dosimetry / area survey (ISO 9612)* ·
   *estimated from equipment / similar tasks* · *none yet*. On **none yet → recommend a
   measurement strategy FIRST and set NO surveillance plan** until an exposure basis exists.
2. **Q2 — Named area + similar-exposure group (SEG) / roles** (free-text): the specificity
   anchor — **refuse a generic area ("the factory") or SEG ("all staff")**.
3. **Q3 — Exposure levels** (free-text): the **8-hr TWA / L_EX,8h dB(A) per SEG** (and peak /
   C-weighted if impulsive). **≥ 85 dBA triggers a hearing-conservation program; at/above the
   limit mandates noise reduction.** Transcribe the value — never compute or invent one.
4. **Q4 — Noise sources** (multi-select): the equipment / processes driving the exposure.
5. **Q5 — Existing controls** (multi-select): **hearing-protection-only is flagged — it does
   not satisfy the hierarchy** (source/engineering must be assessed first).
6. **Q6 — Jurisdiction** (MCQ): USA / UK / EU / **India** / Other / Unknown — sets the cited
   action level / limit. **India → mandatory state branch (Q6a); defer to `hse-india`; emit a
   literal `[GAP]`, never a national form-id.**

**Refuse-on-vague GATE (the specificity core):** do **not** set an audiometry / surveillance
schedule until an **exposure basis (Q1)** + a **named area/SEG (Q2)** + **≥ an estimated TWA
(Q3)** are captured (or a documented `[GAP]` to measure). On "it seems loud" with no number,
recommend a **measurement strategy first** — never fabricate a dB figure.

### The noise-assessment + hearing-conservation method

Full method in `references/METHODOLOGY.md`: de-identify first (audiometric/STS is
special-category health data) → exposure-vs-action/limit comparison (cited, transcribed) →
exposure-zone map → noise-reduction plan (hierarchy-ranked, residual) → hearing-conservation
elements → OEL/action-level-linked audiometry schedule (baseline / annual / STS triggers) →
owned + dated SMART actions → validate against `references/QUALITY_CHECKLIST.md` → assemble the
branded report (`assets/noise-exposure-health-surveillance.report.json`) and run the canonical
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

This is a **moderate fan-out**: the **De-identifier is the sequential first gate**
(audiometric / standard-threshold-shift results are special-category health data), then an
**Exposure-Zone-Analyst** and a **Surveillance-&-Program-Planner** run in parallel, and
**Critic/QA is mandatory**. The action-level/limit comparison is **transcribed + cited**, never
computed — there is no dosimetry calculator. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer). Scrub every
  identifier to a stable SEG/role label, and treat **audiometric thresholds / standard-threshold-
  shift (STS) / fitness-for-work notes as special-category health data**: report by SEG/role,
  apply **`<5` small-cell suppression to every audiometric breakdown**, and strip every named
  audiometry / STS result. Returns the re-identification key **SEPARATELY** (never to a sibling).
  Every job below consumes only its scrubbed, SEG-labelled output.
- **Exposure-Zone-Analyst** — from the scrubbed Q1–Q4 inputs, transcribe each SEG/area's noise
  exposure and compare it to the **cited action level / exposure limit** (OSHA 1910.95 85/90 dBA
  · Noise Regs 2005 80/85/87 dB(A)) with **authority + year** from the resolved jurisdiction;
  map the area into **exposure zones**; name the surveillance trigger (≥ action level →
  audiometry). **SCOPE-OUT:** control selection + the schedule (the Planner) — and **never
  compute dosimetry** (transcribe the measured value, flag `[GAP]` if absent).
- **Surveillance-&-Program-Planner** — rank **noise-reduction controls up the hierarchy** via
  `controls` + `KB-SNIP-HOC` + `KB-SNIP-NOISE-CONTROL-HIERARCHY` (source/engineering before
  **hearing protection**; **HPD-only ≥ 85 dBA is flagged**), then set the **action-level-linked
  audiometry schedule** (baseline / annual / STS triggers); every action **SMART** (named role
  owner + ISO date) via `smart_actions`. **SCOPE-OUT:** exposure characterisation (the Analyst).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Occupational Hygienist / Audiometric Technician / OH
  Physician) before any output: every exposure compared to a **cited** action level / limit,
  controls above hearing protection, the audiometry schedule action-level-linked, and **ZERO
  special-category-health leak** (no named STS result, no `<5` audiometric cell).
- **Critic/QA** (MANDATORY) — adversarial final pass: every area/SEG named, every exposure
  action-level-compared (cited, transcribed), no hearing-protection-only treatment without
  justification, every action owned + dated + SEG-linked, every citation traces to the KB, and
  **zero special-category health leak**. PASS/FAIL.

A single-area single-SEG check (e.g. one SEG's noise exposure) runs single-threaded — no
subagents — but the De-identifier-first scrub, the `controls`/`smart_actions` calls, and the
Critic/QA + SME passes are still made.

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
