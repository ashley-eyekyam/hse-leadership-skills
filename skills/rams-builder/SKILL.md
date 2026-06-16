---
name: rams-builder
description: Creates consultant-grade, construction-ready RAMS — a combined Risk Assessment
  and Method Statement for a specific construction activity on a specific site. Use
  this skill whenever a user asks to build, write, or review a RAMS, a method statement,
  or a safe system of work for construction works, or to produce a CDM RAMS, a contractor
  RAMS, or a method statement tied to a risk assessment. Assesses the activity's hazards
  on a risk matrix, enforces the hierarchy of controls (no PPE-only treatments without
  justification), builds a sequenced safe system of work with plant, competencies,
  and permits, cross-references every method step to the risk assessment, names the
  competent persons, sets out emergency and rescue arrangements, and produces a briefing/sign-off
  record — grounded in ISO 45001 clause 6.1.2 and the applicable construction law
  (UK CDM 2015 Regulation 13, or India BOCW with the user's state form), emitting
  a branded report. Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 1
  audience:
  - M
  - C
  industry:
  - Con
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# RAMS — Risk Assessment & Method Statement (construction)

A consultant-grade HSE skill that produces a task/site-specific **RAMS** — a combined
**Risk Assessment + Method Statement** for a specific construction activity on a
specific site. The **RA half** runs the standard HIRA loop grounded in **ISO 45001
clause 6.1.2** (the same loop the `risk-assessment` flagship uses, reused verbatim);
the **MS half** is the **sequenced safe system of work** — the ordered steps, the
plant, the competencies, the permits, the rescue arrangements. A **bidirectional
RA↔MS cross-reference** ties every method step to the RA rows that treat its hazards
and flags any RA hazard no step addresses. It forces the single lever that separates
a defensible RAMS from copy-paste paperwork: a **real sequence on a real site** plus
the full **hierarchy of controls** — never a vague, PPE-only method. Grounded in the
applicable construction law (**UK CDM 2015** Reg 13/15 + the Construction Phase Plan,
or **India BOCW** with the user's resolved state form), with **named competent
persons** and a **briefing/sign-off record**. Scoring, residual re-scoring, and
control ranking are **deterministic** (the A7 `risk_matrix`/`controls` engines); the
MS half uses no engine.

## When to use this skill

Use this skill when the user needs a **RAMS, a method statement, or a safe system of
work** for a **concrete construction activity on a named site** — for example "build
a RAMS to erect a mobile tower and replace south-elevation cladding on levels 2–4",
"write a method statement for excavating a 1.8 m service trench across the access
road", or "review this contractor RAMS". Trigger phrases: *RAMS, method statement,
safe system of work, risk assessment, construction, CDM, CDM 2015, contractor RAMS,
method ↔ RA cross-reference, hierarchy of controls, permit-to-work, BOCW*. The two
load-bearing inputs are the **construction activity** and the **sequence of works**;
if either is vague, the Workflow intake below **refuses to proceed** until they are
elicited.

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
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (CDM 2015 — Reg 13 PC duties, Reg 15 contractor duties, Construction Phase Plan linkage) |
| India | ../../knowledge-base/regulatory/in-state-forms.md (BOCW rows + the user's state) — **mandatory state detection before citing any form** |
| USA   | ../../knowledge-base/regulatory/us-osha.md (29 CFR 1926 construction — site-specific safety plan) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 HIRA + 8.1.2 hierarchy of
controls) and applies `KB-SNIP-HOC` to every control. For a **UK** site it cites
**CDM 2015** (Reg 13 principal-contractor duties, Reg 15 contractor duties, and the
Construction Phase Plan linkage) via `KB-REG-UK-HSWA`. For an **India** site it
resolves the state via `KB-REG-IN-STATEFORMS` (**mandatory state detection** — confirm
the state before citing any form; the **BOCW** Form XXV annual return is the
legacy-first answer, with the OSH-Code transition note appended; **never a national
form number**; an unseeded state → `[GAP]`). The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

Run the question set below, **one question at a time**, MCQ where the answer space is
enumerable and free-text where it is open; branch on the answers; **echo the captured
facts back for confirmation before any analysis**. The **two specificity anchors** are
**Q2 (the construction activity)** and **Q-S (the sequence of works)** — the Workflow
**refuses to proceed** on a vague activity or an unsequenced method; ask again, or
record `[ASSUMPTION]` / `[GAP]`; never invent. Full method in
`references/METHODOLOGY.md`.

| # | Question | Type | Options / prompt |
|---|---|---|---|
| Q1 | Jurisdiction | MCQ | UK · India · USA · EU · Other/Unknown — UK → CDM 2015 (Reg 13) duty path; India → Q1a + BOCW |
| Q1a | *(India only)* Which state? | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Other — **mandatory state detection; confirm before citing any form** |
| **Q2** | **The construction activity / works being assessed** | **free-text** | "Describe the exact works and the structure/element (e.g. 'erect a mobile tower to replace cladding panels on the south elevation, levels 2–4')." — **specificity anchor #1; refuse a vague answer** |
| Q3 | Site & environment | free-text | "Which specific site/area? What's around it — occupied building, public footpath, live traffic, other trades, overhead/buried services, ground conditions, weather exposure?" |
| **Q-S** | **Sequence of works (the ordered steps, start to finish)** | **free-text** | "List the work steps in order, set-up to clear-down (e.g. 'mobilise & set exclusion zone → inspect & erect tower → transfer materials → remove old panels → fit new panels → inspect → dismantle → clear site')." — **specificity anchor #2; refuse an unsequenced answer** |
| Q-P | Plant & equipment | MCQ multi-select + free-text | Access (scaffold/tower/MEWP/ladder) · Lifting (crane/telehandler/hoist) · Excavation (excavator/breaker) · Power tools · Welding/hot-work kit · Other (+ detail) |
| Q-C | Personnel & competencies / cards | free-text | "Who does each step, and what competency/cards do they hold (CSCS, CPCS, IPAF, PASMA, appointed-person for lifts)? **Name the competent persons for the sign-off record.**" — **never invent a card the user did not state** (record `[GAP]`) |
| Q-W | Permits-to-work required | MCQ multi-select | None · Hot work · Excavation/ground disturbance · Confined space · Working at height/suspended access · Lifting operations · Electrical isolation · Other |
| Q4 | Existing controls already in place | free-text | "What site-wide or activity controls already exist (site induction, traffic-management plan, edge protection, the Construction Phase Plan)?" |
| Q5 | Org risk-matrix size | MCQ | 3×3 · 4×4 · **5×5 (default)** · Supply our matrix |
| Q6 | **CDM / contractor role** *(asked for UK; offered elsewhere)* | MCQ | Principal contractor · Contractor / sub-contractor · Principal designer · Client · Not applicable — tunes the CDM 2015 duty cited (Reg 13 PC / Reg 15 contractor) + the CPP linkage; for India maps to the BOCW principal-employer/contractor duty |

After the last applicable question, **echo a captured-facts summary** ("RAMS for:
erecting a mobile tower to replace south-elevation cladding (levels 2–4), occupied
building with a public footpath alongside, 8-step sequence set-up→clear-down, tower +
MEWP, PASMA + IPAF operatives, working-at-height permit, UK / principal contractor,
5×5 matrix — correct?") and only then proceed. Likelihood/severity bands are applied
**per-hazard** at scoring time (step 3) on the org's matrix.

### The RA + Method-Statement method

Full method in `references/METHODOLOGY.md`. The **RA half** is the standard HIRA loop
(reused verbatim from the `risk-assessment` flagship — **no second risk engine**); the
**MS half** is the sequenced safe system of work and uses **no engine**. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Any named operatives, supervisors, or
   sub-contractor personnel in the inputs are scrubbed to **role labels** ("Site
   Supervisor", "Operative A"); everything downstream consumes the scrubbed text.
   *(The RAMS output later carries **named competent persons** — the role+name
   assignments the user **deliberately supplies** for the sign-off record at Q-C; those
   are duty-holder assignments, not PII leaked from incident-style inputs. See the
   de-id exception note below.)*
2. **Hazard identification (RA half)** — for each step elicited in Q-S, identify the
   specific, observable hazards (working at height, excavation collapse, lifting
   operations, hot work, plant/pedestrian interface, electrical, manual handling,
   COSHH/dust), grounded in `KB-STD-ISO45001` 6.1.2; each names **what** is hazardous
   and **who/what is exposed** (own operatives, other trades, the public adjacent to
   the site). Assign each hazard an **RA-id** (RA-01…) for the cross-reference. Flag
   `[GAP]` where a step's hazards are uncertain — never invent.
3. **Initial risk scoring (RA half)** — for each hazard call
   `risk_matrix.load_matrix(config)` then `risk_matrix.score(likelihood, severity,
   matrix)` (Q5 config; default 5×5). The score + band are the engine's,
   deterministically.
4. **Control selection (the hierarchy-of-controls lever)** — for each hazard propose
   controls and **apply `KB-SNIP-HOC`**: rank Elimination → Substitution → Engineering
   → Administrative → PPE; then call `controls.rank_controls` + `controls.validate_treatment`.
   If `ppe_admin_only` is `True`, the Workflow **must** either add a higher-order
   control (edge protection / a MEWP instead of "wear a harness"; an exclusion zone
   instead of "be careful") **or** record an explicit justification — a lower-order-only
   treatment with no justification is a **defect the Critic/QA pass must catch**. This
   is doubly load-bearing in construction, where "PPE + a safe-working briefing" is the
   classic under-control.
5. **Residual re-scoring (RA half)** — re-score each hazard *with the selected controls
   applied* via `risk_matrix.score`, then `risk_matrix.residual_delta(initial,
   residual)` for the movement. A residual High/Critical risk flags that additional
   controls or a hold-point (do-not-start) are required.
6. **Build the Method Statement (the sequenced safe system of work)** — for the
   sequence in Q-S produce, **in order**, for each step: the **work-step description**,
   the **plant/equipment** at that step (Q-P), the **competencies/cards required**
   (Q-C — never invent a certification the user did not supply), the **permits-to-work**
   that gate it (Q-W — hot-work, excavation, confined-space, lifting), and the
   **step-specific controls** from step 4. The MS is a safe-system-of-work **narrative**,
   not a hazard table — it tells the crew *how* to do the job safely, in sequence
   (**no A7 engine**).
7. **RA↔MS cross-reference (the load-bearing coupling)** — tie each method step's
   residual hazards to the RA rows that treat them (an RA-refs column: "Step 3 (excavate)
   → RA-04 collapse, RA-07 buried services"). This is **bidirectional**: the Workflow
   **refuses to ship a method step whose hazards are not in the RA**, **and flags any RA
   hazard that no method step addresses**. This is the difference between a real RAMS and
   stapled paperwork.
8. **Emergency & rescue arrangements** — author the **activity-specific** emergency/
   rescue provisions: a rescue plan for at-height / excavation / confined-space /
   suspended-access work, first-aid provision, emergency contacts/RV point, and the
   spill/fire/services-strike response as relevant to the sequence. Generic "call 999"
   is insufficient where a rescue plan is required.
9. **SMART actions (named owners + dates)** — for every control that is an action (not
   already in place), produce a SMART action: specific, measurable, **assignable (named
   owner / role)**, relevant, **time-bound (ISO due date)**. Call
   `smart_actions.validate_register`; any action missing an owner, a valid date, a
   measure, or a hazard link is **invalid** and must be fixed — no anonymous actions, no
   "ASAP".
10. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check loop: every
    hazard scored; every control HoC-ranked; no un-justified lower-order-only treatment;
    **every method step cross-referenced to the RA and every RA hazard addressed by a
    step** (step 7); named competent persons present where a step needs one; emergency/
    rescue arrangements activity-specific; every action owned + dated + hazard-linked;
    every citation traced to the KB (ISO 45001 6.1.2/8.1.2 always; **CDM 2015 Reg 13/15**
    for UK; **BOCW** + the resolved state form for India); de-id applied; **the briefing
    table ships with empty signature rows**; no conclusion on an unstated assumption.
11. **Assemble the branded RAMS report** — build `report.json` (see
    `assets/rams-report.template.json`) and run the canonical `report-output` call below.

**De-id ↔ named-competent-persons exception (important — do not weaken the de-id gate).**
The de-id block scrubs personal data that arrives *as input evidence* (e.g. an operative
named in a prior near-miss) to role labels — a leak there is an **auto-fail**. The
**sign-off / briefing record** carries the names the user **deliberately supplies as the
duty-holders / competent persons** for this RAMS at Q-C — these are the contractually
required named persons, **not** leaked PII, and they **stay named**. The
briefing-acknowledgement table ships as **empty signature rows** for the crew to
complete on site (it never pre-populates operative names). The distinction the Critic/QA
+ de-id grader enforce is: "names the user assigned as duty-holders for this document"
(legitimate output) vs "names that leaked from the evidence" (scrub to roles).

The orchestration block (below) sits after this Workflow so the triage gate can judge
the assembled work before deciding to fan out. The **deterministic scoring/ranking steps
(3, 4, 5 via `risk_matrix`/`controls`) are A7 script calls in every case — never a
fan-out job** (there is no "Risk-Scorer" subagent); the **MS half (step 6) and the
RA↔MS cross-reference (step 7) use no A7 engine**.

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

### Step 4 — Critic / QA (MANDATORY — this is regulatory/safety output)
Spawn ONE Critic: give it the draft + the inputs + the output contract. It finds errors,
unsupported claims, missed regulatory triggers, lower-order-only controls, and any
de-identification leak. Fix everything it raises before delivery.

> Single-threaded fallback: if your host has no subagent capability, execute each job
> sequentially in THIS context — run the de-identification scrub first, keep the scope
> discipline, and still perform the required Critic/QA pass before delivery.
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

This is the **STANDARD moderate roster** (A6 "moderate = 2–3"): the De-identifier is
the **sequential first gate** (not a fan-out peer), the **3 fan-out jobs** are
Researcher + Regulatory-Checker + Drafter, and **Critic/QA is mandatory**. **There is
no Risk-Scorer subagent** — scoring, residual re-scoring, and control ranking are
deterministic A7 script calls at Workflow steps 3/4/5 (`risk_matrix`, `controls`); the
**MS half and the RA↔MS cross-reference use no engine**. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all PII
  (operative/supervisor/sub-contractor names, personal data) to role labels before any
  analysis (every fan-out job below consumes scrubbed text). The **named competent
  persons the user supplies at Q-C for the sign-off record stay named** (the §3.8
  exception) — they are duty-holder assignments, not leaked PII.
- **Researcher** — gather evidence for the activity's hazards, plant/equipment, and
  competency requirements from primary sources (manufacturer/HSE guidance for the named
  plant; the CSCS/CPCS/IPAF/PASMA scheme requirements the user states); cited summary,
  flag `[GAP]`. SCOPE-OUT: law (Regulatory-Checker), drafting (Drafter). (Scoring is NOT
  a subagent — it is the A7 `risk_matrix` script.)
- **Regulatory-Checker** — for the resolved jurisdiction, return the applicable
  construction duty + clause: **UK** CDM 2015 Reg 13/15 + the Construction Phase Plan
  linkage (via `KB-REG-UK-HSWA`); **India** BOCW + the resolved **state** form via
  `KB-REG-IN-STATEFORMS` (state confirmed first; never a national form number) + the
  OSH-Code transition note; plus any permit/notification trigger. Conservative, flag
  `[GAP]`. SCOPE-OUT: drafting the RAMS, gathering hazard/plant evidence (Researcher).
- **Drafter** — write the RA register + control plan + the **sequenced** method statement
  + the **RA↔MS cross-reference** + the emergency/rescue arrangements + the sign-off /
  briefing record to the output template using role placeholders (and the user-named
  competent persons for the sign-off record; **empty signature rows** for the crew); each
  control tagged its `KB-SNIP-HOC` tier (consumes the De-identifier's scrubbed text + the
  A7 `risk_matrix`/`controls` scores + the Regulatory-Checker's verdict). SCOPE-OUT:
  gathering evidence (Researcher), checking law (Regulatory-Checker).
- **Critic/QA** (MANDATORY) — every hazard scored (via the A7 engine), every control
  HoC-ranked, no PPE/admin-only treatment without justification, **every method step
  cross-referenced to the RA and every RA hazard addressed by a step**, named competent
  persons present, emergency/rescue arrangements activity-specific, every action owned +
  dated + hazard-linked, every citation traces to the KB, **the briefing table ships
  with empty signature rows**, zero input-derived PII leaked. PASS/FAIL.

Researcher + Regulatory-Checker may merge to land at 2 fan-out jobs and stay in-band.
Single-step trivial works run single-threaded — no subagents — but the A7
scoring/ranking calls and the Critic/QA pass are still made.

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
