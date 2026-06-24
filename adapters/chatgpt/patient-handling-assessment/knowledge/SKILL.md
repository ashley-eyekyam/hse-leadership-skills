---
name: patient-handling-assessment
description: 'Produces a consultant-grade moving-and-handling-of-people (patient
  handling) risk assessment for a named care task — a TILE/SPHM assessment with a
  mobility-and-equipment matrix and a move-toward-zero-manual-lift control plan. Use
  this skill whenever a user asks to assess patient handling, manual handling of
  people, moving and handling, or a hoist / transfer / repositioning / bariatric
  handling risk assessment on a ward, in a care home, in community care, or in an
  ambulance. It avoids hazardous manual handling first (substitute a hoist for a lift),
  assesses the residual with the MHOR Schedule 1 TILE filter
  (Task, Individual, Load, Environment), ranks controls up the hierarchy (eliminate the
  manual lift -> mechanical aids -> safe systems -> technique/PPE last), and refuses a
  manual lift where a mechanical aid is available. The patient is de-identified to
  mobility / dependency / weight band. Grounded in ANA SPHM (2021), NIOSH, ISO/TR 12296,
  and UK MHOR 1992. Decision-support only; a competent person must review.'
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
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-healthcare
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Patient Handling (Moving & Handling of People) Assessment

A consultant-grade, **move-toward-zero-manual-lift** moving-and-handling-of-people risk assessment
for a **named care task** — a bed-to-chair transfer, a reposition, a lateral transfer, a falls
recovery, a bariatric move, an ambulance loading — on a ward, in a care home, in community/home
care, or in an ambulance, never a generic "moving patients". Its entire reason to exist is that
**patient handling leads by avoiding the manual lift, not by lifting more carefully**: every
assessment first records whether the hazardous manual handling can be **avoided** (a ceiling or
mobile hoist, a slide sheet, a transfer board substituted for a manual lift — the MHOR reg 4 avoid
duty / the SPHM move-toward-zero principle); only the **residual, unavoidable** handling is assessed
with the **TILE** filter (Task, Individual, Load, Environment) and controlled by mechanical aids,
then safe systems of work, with **technique and PPE (a back belt) as the documented last lines, never
the control**. A bare "use correct technique / wear a back belt" is **refused** — technique is an
administrative measure, and a back belt is PPE; neither is the primary control where the manual lift
could be avoided with a mechanical aid.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**the avoid-the-manual-lift decision plus the full hierarchy of controls, with the patient and the
worker never identified**. Patient mobility / dependency data and a worker's musculoskeletal /
back-condition record are **special-category health data (PHI)** — the **patient** is assessed and
recorded by **de-identified mobility / dependency level and weight band only** (never a name,
MRN/hospital number, ward/bay, diagnosis, or care-plan detail in the circulated assessment), the
worker's capability under TILE **Individual** is assessed **without** writing the worker's name or any
fitness / back-condition record into the circulated copy (role-label; the medical-fitness detail held
confidentially, separate), and any handling-injury category aggregated across the unit with **fewer
than 5 individuals is suppressed** (small-cell back-calculation guarded). The skill **never** emits a
re-identification key file — the key is an instruction to the competent person, held separately and
access-controlled. Grounded in **ANA Safe Patient Handling and Mobility (SPHM): Interprofessional
National Standards, 2nd ed. (2021)** (the move-toward-zero culture + the 8 standards), **NIOSH
safe-lifting guidance** (the recommended manual-lift limit; minimize manual patient lifting),
**ISO/TR 12296:2012** (ergonomics — manual handling of people in healthcare), and the **UK Manual
Handling Operations Regulations 1992 (MHOR)** reg 4 (avoid → assess (Schedule 1 **TILE**) → reduce),
with **India** factory/occupational ergonomics via `hse-india`. Decision-support only; a competent
person (moving-and-handling / ergonomics specialist) must review the output.

## When to use this skill

Use this skill when the user needs a **moving-and-handling-of-people risk assessment for a concrete
care task** — for example "assess the bed-to-chair transfer on the rehab ward", "do a moving and
handling assessment for repositioning in the care home", "a hoist-transfer risk assessment for
community care", or "a bariatric lateral-transfer plan". It is **not** for a generic "how do I move
patients safely?" answer: the Workflow intake below forces the named care task and setting, the
**avoid-the-manual-lift decision (asked first)**, the four-element TILE assessment, and the
mobility-and-equipment matrix before any control plan, refuses a vague "moving patients" request, and
refuses a "use good technique / wear a back belt" treatment where the manual lift could be avoided
with a mechanical aid.

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

This skill is one of the catalog's **highest-PHI** artifacts. The reinforced healthcare PHI
extension — the **patient-assessed-by-de-identified-mobility/dependency/weight-band** rule, the
**worker back-condition / OH-record** rule, the **`<5` small-cell suppression with secondary
back-calculation guard** for handling-injury data, and the **re-identification-key-separation**
instruction — lives in `references/deid-checklist.md` and the **Workflow de-id step** below (it is NOT
in the byte-identical block above).

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
| Patient-handling spine (every run) | ../../knowledge-base/prompt-snippets/tile-people.md (KB-SNIP-TILE-PEOPLE) — the **avoid → assess by TILE → reduce** patient-handling gate: a control plan that defaults to a manual lift ("two staff lift") where a mechanical aid is available is rejected (move-toward-zero not applied); a TILE assessment missing any of the four elements is rejected; handling-injury reporting is small-cell-suppressed |
| Patient-handling standard (every run) | ../../knowledge-base/standards/sphm.md (KB-STD-SPHM) — the **ANA SPHM 8-standard** move-toward-zero programme structure + ISO/TR 12296 method + NIOSH safe-lift; mechanical aids and environment design precede manual technique; residual risk on `risk_matrix` 5×5, **NOT a NIOSH-equation engine** (that lives in manufacturing's `ergonomics`) |
| Healthcare clause cross-walk (every run) | ../../knowledge-base/prompt-snippets/healthcare-clause-map.md (KB-SNIP-HEALTHCARE-CLAUSE-MAP) — the bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent |
| UK | ../../knowledge-base/regulatory/uk-mhor.md (KB-REG-UK-MHOR) — UK Manual Handling Operations Regulations 1992: reg 4(1)(a) **avoid** → reg 4(1)(b)(i) **assess** (suitable & sufficient) → reg 4(1)(b)(ii) **reduce**, with the Schedule 1 **TILE** factors and reg 4(2) review (cite the regulation numbers + TILE, never paste the wording) |
| India | India factory/occupational-ergonomics provisions via `hse-india` — **mandatory state detection**; emit `[GAP]`, never a national form number |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and leads every assessment with the
**avoid-the-manual-lift spine** `KB-SNIP-TILE-PEOPLE` (avoid the manual lift → assess the residual by
TILE → reduce with mechanical aids first, manual lifting last resort), grounds the programme structure
in `KB-STD-SPHM` (the ANA SPHM 8 standards + ISO/TR 12296 + NIOSH), aligns with the other
hse-healthcare skills through `KB-SNIP-HEALTHCARE-CLAUSE-MAP`, applies `KB-SNIP-HOC` to every control,
and reuses the `KB-SNIP-ARCHETYPES` subagent roster. The TILE assessment and the mobility-and-equipment
matrix are a **structured assessment frame** over the named care task + the cited SPHM/MHOR standards —
**not a calculation**; the residual moving-and-handling risk reuses the standard `risk_matrix` 5×5
(the standard path applies here, unlike arc flash) — there is **no new engine** (the NIOSH lifting
equation is the manufacturing pack's `ergonomics`, NOT this skill). For a UK site ground in
`KB-REG-UK-MHOR`; for India, resolve the state via `hse-india` (**mandatory state detection**) and
emit a literal `[GAP]` where a state return is owed — never a minted national form number. The rule-9
manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**De-identify FIRST (the highest-PHI step — before any drafting).** Run the `deid` block +
`references/deid-checklist.md` BEFORE the intake echo-back drives any analysis. Patient mobility data
and a worker's musculoskeletal record are special-category health data: assess and record the
**patient by de-identified mobility / dependency level and weight band only** (never a name,
MRN/hospital number, ward/bay, diagnosis, or care-plan detail — "a bariatric, fully-dependent patient
on Ward 4 bay 2" is identifying; scrub the ward/bay and any clinical detail), assess the **worker's
capability** under TILE Individual **without** writing the worker's name or any fitness /
back-condition record into the circulated copy (role-label "Worker A"; the medical-fitness detail held
confidentially, separate). Apply **`<5` small-cell suppression** (with secondary suppression) to every
handling-injury category aggregated across the unit, and produce a SEPARATE access-controlled
re-identification key — **never** co-located with the assessment and **never** emitted as a key file.

Run the patient-handling intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "moving patients": you need the named care task + setting
+ the avoid-the-manual-lift decision before any control plan. Refuse a "use good technique / wear a
back belt" treatment where the manual lift could be avoided with a mechanical aid.**

1. **The named care task & setting** (free-text — the specificity anchor) — "Name the exact handling
   task (bed-to-chair transfer, repositioning, lateral transfer, falls recovery, bariatric move,
   ambulance loading) **and the setting** (ward / care home / community / ambulance). **Refuse
   'moving patients' / 'the ward' — the assessment is task-specific.**"
2. **Can the manual lift be avoided?** (mcq — asked FIRST among the controls) — yes → **substitute a
   ceiling/mobile hoist, slide sheet, or transfer board**: the assessment leads with the mechanical
   aid (move-toward-zero, the SPHM/NIOSH principle) · no/partly → branch to a TILE assessment of the
   residual (Q3). **Avoiding the manual lift is the primary control, not the technique.**
3. **TILE assessment of the residual handling** (free-text — refuse to score without all four) —
   **Task** (frequency, posture, distance, twisting) · **Individual** (the worker's capability,
   training, limitation; number of handlers — **never the worker's medical record** in the circulated
   copy) · **Load** (the patient's weight band, dependency, cooperation, attachments — lines, drains;
   bariatric; falling risk — the **patient assessed by mobility/dependency, de-identified**) ·
   **Environment** (space, floor, bed/chair height, ceiling-track availability, obstructions). **A
   TILE assessment missing any of the four elements is not suitable and sufficient — refused.**
4. **Mobility-and-equipment matrix** (free-text — the core artifact) — the patient's mobility /
   dependency level → the matched equipment and the number of handlers. **A "two-person manual lift"
   recommended where a hoist or slide aid is reasonably available is FLAGGED** and pushed up the
   hierarchy.
5. **Bariatric / special** (mcq) — bariatric → equipment safe-working-load (SWL), environmental
   loading, extended planning · falls → post-fall handling plan · routine → standard.
6. **Jurisdiction** (mcq) — UK (MHOR 1992 + TILE) / USA (OSHA ergonomics / SPHM + NIOSH) /
   International (ISO/TR 12296) / India / Other / Unknown. **India → resolve the state via `hse-india`
   (mandatory state detection); factory/occupational ergonomics; emit `[GAP]`, never a national form
   number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented task, weight band, or count.

Then: record the **avoid-the-manual-lift decision first** (`KB-SNIP-TILE-PEOPLE`); assess the
residual handling by the four-element **TILE** filter; build the **mobility-and-equipment matrix**
(dependency level → equipment + handler count); rank the residual controls up the hierarchy via the
`controls` engine (eliminate the manual lift → mechanical aids (hoist, slide sheet, transfer board) &
environment design → administrative safe systems of work / training → **technique & PPE (back belt)
last** — a manual-lift recommendation where a mechanical aid is reasonably available, or a "good
technique / back belt" headline, is a FLAG pushed up the hierarchy); add the **bariatric / falls
plan** where the branch ran; frame the residual moving-and-handling risk via `risk_matrix` (the
standard 5×5); make every action a SMART action via `smart_actions` → validate the draft against
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

For a multi-area patient-handling assessment the triage gate fans out (moderate 2–3; the
**De-identifier runs FIRST — sequential dependency**; everything below consumes only its scrubbed
output):

- **De-identifier** — runs FIRST. Reduce the **patient to a de-identified mobility / dependency level
  and weight band** (never a name, MRN/hospital number, ward/bay, diagnosis, or care-plan detail) and
  **role-label the worker** (the worker's name and any fitness / back-condition record held
  confidentially, separate) before any analysis; apply `<5` small-cell suppression (with secondary
  suppression) to every handling-injury category aggregated across the unit; return the
  re-identification key SEPARATELY to the orchestrator, never to a sibling, and never as a key file.
- **TILE-&-Lift-Avoidance-Analyst** — records the **avoid-the-manual-lift decision FIRST** (can a
  hoist / slide sheet / transfer board remove the manual lift — move-toward-zero, the SPHM/NIOSH
  principle), then assesses the unavoidable residual by the four-element **TILE** filter (Task,
  Individual, Load, Environment). A control plan that defaults to a **manual lift where a mechanical
  aid is reasonably available**, or a TILE assessment **missing any of the four elements**, is a
  **FLAG / not-suitable-and-sufficient**, never accepted. SCOPE-OUT: does not build the
  mobility-and-equipment matrix or rank the controls (the Equipment-Matrix-&-Controls-Author) or
  de-identify (the De-identifier).
- **Equipment-Matrix-&-Controls-Author** — builds the **mobility-and-equipment matrix** (dependency
  level → matched equipment + handler count) and runs the **eliminate-the-manual-lift → mechanical
  aids → safe systems of work → technique/PPE last** hierarchy via the `controls` engine; adds the
  **bariatric / falls plan** (equipment SWL, environmental loading, post-fall handling) where it
  applies. A treatment that **leads with "use good technique / wear a back belt" where the manual lift
  could be avoided** is a **FLAG pushed up the hierarchy, never the headline control**. SCOPE-OUT:
  does not make the avoid / TILE assessment (the TILE-&-Lift-Avoidance-Analyst) or de-identify (the
  De-identifier).
- **Critic/QA** (MANDATORY) — adversarial final pass: the avoid-the-manual-lift decision is recorded
  BEFORE any equipment or technique, the four TILE elements are all assessed, the mobility-and-equipment
  matrix is present, no manual lift is recommended where a mechanical aid is reasonably available, no
  treatment is reduced to "good technique / back belt", the bariatric SWL + environmental loading is
  addressed where it applies, no `<5` handling-injury cell is published, the patient is recorded by
  de-identified mobility/dependency/weight band, and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the avoid-the-manual-lift
decision, the four-element TILE assessment, the mobility-and-equipment matrix, the A7 `controls` /
`risk_matrix` / `smart_actions` calls inline, the bariatric/falls plan, then the mandatory Critic/QA +
SME pass — same scope discipline, no subagents.

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
- `references/deid-checklist.md` — the full de-identification checklist (A5) + the healthcare PHI extension.
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
