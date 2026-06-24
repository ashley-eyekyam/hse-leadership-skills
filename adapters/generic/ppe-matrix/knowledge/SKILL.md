---
name: ppe-matrix
description: 'Produces a task×hazard→PPE selection matrix for a named area, line,
  or role set, driven by the controls-first gate: PPE is specified only for the residual
  hazard surviving the higher-order controls, never as the headline control. Use this
  skill whenever a user asks to build or review a PPE matrix, a PPE hazard assessment,
  a PPE selection table, or the OSHA 1910.132(d)(2) written hazard-assessment certification
  for a specific task, line, area, or role — not a site-wide sheet. It runs the hierarchy
  of controls before any PPE row (a hazard with no recorded higher-order control triggers
  a controls-first flag, not a PPE row), selects each PPE type against the named residual
  hazard with its cited conformity standard (EN / ANSI), reduces respiratory medical-clearance
  data to role labels, and emits a branded matrix report with the written hazard-assessment
  certification. Grounded in the OSHA PPE standard (29 CFR 1910.132) + the hierarchy
  of controls. Decision-support only; a competent person must review the output.'
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
  - Mfg
  jurisdiction:
  - All
  status: stable
  plugin: hse-manufacturing
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# PPE Matrix

A consultant-grade **task×hazard→PPE selection matrix** for a **named area, line, or role
set** — never a site-wide PPE sheet. Its entire reason to exist is the **controls-first
gate**: for each body-region hazard the higher-order controls (eliminate → substitute →
engineer → administrative) must be **applied or justified** before any PPE is specified, and
**PPE is selected only for the residual hazard that survives those controls**. A hazard with
**no recorded higher-order-control consideration triggers a "controls-first" flag, NOT a PPE
row** — PPE-first is the failure mode this skill exists to prevent. It forces the single lever
that separates a defensible artifact from copy-paste paperwork: **task specificity plus the
full hierarchy of controls** — never a vague, PPE-only headline treatment. Each PPE type is
selected against the **named residual hazard** and **cited to its conformity standard**
(EN / ANSI, with year — `KB-DATA-PPE-STANDARDS`); a protection level asserted without the
cited standard is a citation failure. The skill always emits the **OSHA 1910.132(d)(2) written
hazard-assessment certification** (workplace, certifier, date) — omitting it is a citation
failure. **Respiratory medical-clearance / fitness-for-respirator data is special-category
health data** (reduced to role labels; no named individual carried into the output). Grounded
in **OSHA 29 CFR 1910 Subpart I (1910.132)**, the **hierarchy of controls**, and the **PPE
conformity standards**. Decision-support only; a competent person must review the output.

## When to use this skill

Use this skill when the user needs a **task-level PPE selection matrix** for a concrete area,
line, role set, or task — for example "build a PPE matrix for the line-3 fettling cell",
"do the PPE hazard assessment and certification for the welding bay", "what PPE for the
acid-decant task and to which standard", or "produce the 1910.132(d)(2) written certification
for the despatch dock". Trigger phrases: *PPE matrix, PPE selection table, PPE hazard
assessment, PPE certification, 1910.132(d)(2) written certification, what PPE for <task>,
PPE by body region*. If the request is vague ("make a PPE matrix") or site-wide, the Workflow
intake below **refuses to emit any PPE row** until the **named scope (Q1)**, the **body-region
hazards (Q2)**, and — for each hazard — the **higher-order controls considered (Q3, the
controls-first gate)** are captured; a hazard with no higher-order control recorded is a
**controls-first flag, never an invented PPE row**. For the full risk assessment behind the
hazards, use `risk-assessment`; this skill is the PPE-selection layer that sits downstream of it.

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
| USA | ../../knowledge-base/regulatory/osha-1910-i.md (KB-REG-OSHA1910-I) — OSHA 29 CFR 1910 Subpart I: 1910.132(d)(1) PPE hazard assessment + **1910.132(d)(2) written certification** + the body-region sections (.133 eye/face · .135 head · .136 foot · .138 hand) |
| UK / EU | ../../knowledge-base/regulatory/uk-hswa.md — PPE at Work Regs 1992 (amended 2022, extends to limb (b) workers) + the EN conformity standards |
| India | ../../knowledge-base/regulatory/in-factories-act.md — Factories Act 1948 PPE provisions; **defers to `hse-india`, mandatory state detection (+ in-state-forms.md for the user's state); emit `[GAP]`, never a national form number** |
| EU | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| The controls-first gate (every run) | ../../knowledge-base/prompt-snippets/ppe-matrix-logic.md (KB-SNIP-PPE-MATRIX-LOGIC) — the **residual-hazard-only PPE-selection logic + controls-first gate** (the spine), applied with ../../knowledge-base/prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) and verified by the `controls` engine |
| PPE conformity standards (every PPE row) | ../../knowledge-base/data-points/ppe-standards.md (KB-DATA-PPE-STANDARDS — **REUSE, never re-authored**) — the EN/ANSI conformity standard per PPE category; **cite the standard + year**, never assert protection without it |
| Operational PPE duty (every run) | ../../knowledge-base/regulatory/osha-1910-o.md (KB-REG-OSHA1910-O) — the machinery/operational-control cross-reference where PPE sits as the residual control |
| Manufacturing clause cross-walk | ../../knowledge-base/prompt-snippets/manufacturing-clause-map.md (KB-SNIP-MANUFACTURING-CLAUSE-MAP) — the ISO-45001 §6.1.2 / §8.1.2 manufacturing clause cross-walk |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) + the manufacturing clause cross-walk
`KB-SNIP-MANUFACTURING-CLAUSE-MAP`, runs the **controls-first gate** (`KB-SNIP-PPE-MATRIX-LOGIC`
+ `KB-SNIP-HOC`, verified by the `controls` engine) before any PPE row, selects each residual-only
PPE type against its **cited EN/ANSI conformity standard + year** (`KB-DATA-PPE-STANDARDS`, reused
not re-authored), grounds the PPE duty + the **mandatory written certification** on
`KB-REG-OSHA1910-I` (1910.132(d)(2)), and **does not author `KB-DATA-PPE-STANDARDS`** (it is
reused, not minted) **or the manufacturing HazCom fragment** (P17-deferred). For an India site, resolve the state via
`hse-india` (mandatory state detection) and emit a literal `[GAP]` where a state form/return is
owed — never a minted national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table, the
**per-hazard controls-first-gate branch** (Q3 — higher-order controls considered, the spine),
the **mandatory India→state branch**, the echo-back, and the refuse-on-vague anchors — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo the
captured facts back before any analysis**:

- **Q1 — named scope** (free-text): the exact area / line / role set + the tasks performed.
  **Refuse a generic or site-wide PPE sheet ("PPE for the whole plant") — the matrix is
  task-specific; this is the specificity anchor.**
- **Q2 — hazards by body region** (multi-select, per OSHA Subpart I): eye/face · head · hearing
  · respiratory · hand/arm · foot/leg · body/torso — selected per task in scope.
- **Q3 — higher-order controls considered** (free-text **per hazard**, **the controls-first
  gate, MANDATORY**): for each Q2 hazard, what elimination / substitution / engineering /
  administrative controls are in place or justified. **PPE is selected only for the residual
  hazard surviving those controls. A hazard with NO higher-order control recorded triggers a
  "controls-first" FLAG — NOT a PPE row.** Never invent a PPE row to fill the gate.
- **Q4 — task duration & conditions** (MCQ): occasional / regular / continuous shift-long +
  environment (heat, confined space, IDLH) — sets respiratory-fit / clearance needs.
- **Q5 — existing PPE & gaps** (free-text): what PPE is issued today and where it does not
  match the residual hazard or carries no cited conformity standard.
- **Q6 — jurisdiction** (MCQ): US OSHA 1910.132 + ANSI default · UK/EU PPE at Work Regs 1992
  + EN · **India Factories Act PPE via `hse-india` — mandatory state detection, emit `[GAP]`,
  never a national form number**.

**The controls-first gate is a deterministic check, not a narration.** Per hazard, the Workflow
calls `controls.rank_controls(...)` / `controls.validate_treatment(...)` via the
`scripts/hse_components` symlink: a treatment whose only entries are PPE/administrative returns
`ppe_admin_only=True`, and a hazard with no higher-order control recorded is flagged
(controls-first) — the PPE row is **withheld**, not invented. Respiratory medical-clearance /
fitness data is reduced to role labels before any drafting.

### The ppe-matrix method (scope → body-region hazards → controls-first gate → residual-only PPE + cited standard → written certification)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs FIRST (special-category respiratory medical-clearance / fitness
   data).** Before any drafting (the `deid` block above + `references/deid-checklist.md` + the
   De-identifier-runs-first orchestration rule): scrub names to role labels, reduce any
   respiratory medical-clearance / fitness-for-respirator note to the role level, apply `<5`
   small-cell suppression to any health breakdown, and **never circulate a named clearance
   note**. Everything downstream consumes the scrubbed text.
2. **Capture the named scope and the body-region hazards (Q1 → Q2).** Refuse a generic or
   site-wide sheet; the matrix is task-specific.
3. **Run the controls-first gate, per hazard (Q3 — the spine).** Apply `KB-SNIP-PPE-MATRIX-LOGIC`
   + `KB-SNIP-HOC` and call `controls.rank_controls` / `controls.validate_treatment`. For each
   body-region hazard, confirm the higher-order controls (eliminate / substitute / engineer /
   administrative) are applied or justified. **PPE is specified only for the residual hazard
   that survives them.** A hazard with no higher-order control recorded is a **controls-first
   flag — emit the flag, NOT a PPE row.**
4. **Select the residual-only PPE + cite the conformity standard.** For each residual hazard,
   select the PPE type and **cite the EN/ANSI conformity standard + year** from
   `KB-DATA-PPE-STANDARDS` (e.g. "EN 166 / ANSI Z87.1, [year]"). **Never assert protection
   without the cited standard** — that is a citation hard-fail.
5. **Emit the written hazard-assessment certification (1910.132(d)(2) — mandatory).** Produce
   the certification block: the workplace assessed, the certifier (role), and the date.
   **Omitting it is a citation hard-fail.** A missing input (no task, no hazard) is a `[GAP]`;
   PPE is never the headline control.
6. **SMART actions (named owners + dates).** Every PPE-gap / controls-first action becomes a
   SMART action (named role owner + ISO due date + measure), validated by
   `smart_actions.validate_register`.
7. **Validate against `references/QUALITY_CHECKLIST.md`** then **assemble the branded report**
   (`assets/ppe-matrix.report.json`) and run the canonical `report-output` call below.

The **controls-first gate (step 3, via `controls`) is an A7 script call in every case** — never
a fan-out job that narrates a PPE row past the gate.

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

This is a **staged fan-out** with a strict order: the **De-identifier is the sequential first
gate** (special-category respiratory medical-clearance / fitness data), then the
**Hazard-Assessment-Analyst** runs **the controls-first gate** (deterministic `controls` call),
and only the **PPE-Selection-Author** turns surviving residual hazards into cited PPE rows —
**Critic/QA + SME Review are mandatory**. The controls-first gate is a **deterministic A7 script
call** (`controls.rank_controls` / `controls.validate_treatment`), never LLM fan-out work.
Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer). Scrub every identifier
  to a stable role label, and treat **respiratory medical-clearance / fitness-for-respirator
  notes as special-category health data**: reduce them to the role level, apply `<5`
  suppression to any health breakdown, and strip every named clearance/fitness note. Returns
  the re-identification key SEPARATELY (never to a sibling). Every job below consumes only its
  scrubbed, role-labelled output.
- **Hazard-Assessment-Analyst (the controls-first gate)** — for each task in scope, identify
  the **body-region hazards** (per OSHA Subpart I), then run **the controls-first gate**: call
  `controls.rank_controls` / `controls.validate_treatment` with `KB-SNIP-PPE-MATRIX-LOGIC` +
  `KB-SNIP-HOC` and confirm the higher-order controls (eliminate / substitute / engineer /
  administrative) are applied or justified per hazard. **A hazard with no higher-order control
  recorded is returned as a "controls-first" FLAG, NOT a PPE row** — it never invents one.
  SCOPE-OUT: PPE selection (the PPE-Selection-Author owns it).
- **PPE-Selection-Author** — for each **residual** hazard that survived the gate, select the
  PPE type and **cite the EN/ANSI conformity standard + year** (`KB-DATA-PPE-STANDARDS`); never
  assert protection without the cited standard. Assemble the task×hazard→PPE matrix grid and the
  **1910.132(d)(2) written certification block** (workplace, certifier, date — mandatory).
  SCOPE-OUT: the controls-first gate (the Analyst owns it) — it must NOT add a PPE row for a
  flagged hazard.
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Certified Safety Professional / PPE-program lead) before any
  output: every PPE row passed the controls-first gate, every protection level cited to its
  EN/ANSI standard + year, the written certification present, and ZERO special-category
  respiratory-clearance leak.
- **Critic/QA** (MANDATORY) — adversarial final pass: every PPE row traces to a residual hazard
  that survived the controls-first gate (no PPE-first), every flagged hazard shows the
  controls-first flag not a PPE row, every protection level cites its EN/ANSI standard + year,
  the 1910.132(d)(2) certification is present, every action owned + dated, and zero
  respiratory-clearance / fitness leak. PASS/FAIL.

A single-task single-hazard check runs single-threaded — no subagents — but the **De-identifier
runs first**, the **controls-first gate is still a deterministic `controls` call**, and the
Critic/QA + SME passes are still run.

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
