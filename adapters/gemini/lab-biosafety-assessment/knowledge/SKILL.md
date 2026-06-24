---
name: lab-biosafety-assessment
description: 'Produces a consultant-grade laboratory biosafety risk assessment for a
  named lab and procedure, determining the agent risk group (RG1-RG4) and biosafety
  level (BSL-1-BSL-4) with engineering containment before PPE. Use this skill whenever
  a user asks to assess laboratory biosafety, classify a biological agent''s risk group,
  select a biosafety level or biosafety-cabinet class, or write or review a biosafety
  assessment for a clinical, research, or diagnostic lab handling an infectious agent,
  recombinant material, or human blood/OPIM. It classifies the risk
  group first, then selects the BSL with primary containment (cabinet class, airflow,
  decontamination) before PPE; a respirator-and-gloves plan with no containment is
  flagged, and an unknown risk group emits [GAP] rather than being invented.
  Specimen-source-patient and worker health data are scrubbed to role labels before
  drafting. Grounded in CDC/NIH BMBL 6th ed and WHO Laboratory Biosafety Manual.
  Decision-support only; a Biological Safety Officer must review.'
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

# Lab Biosafety Assessment

A consultant-grade **risk-group → biosafety-level** laboratory biosafety risk assessment for a
**named laboratory and procedure** — a clinical / diagnostic, research, teaching, or public-health
laboratory handling a specific biological agent, recombinant material, or human blood / other
potentially infectious material (OPIM) — never a generic "a lab". Its entire reason to exist is that
**containment is decided by classifying the agent's risk group FIRST, then matching it to the
biosafety level with engineering containment before PPE**: every assessment first establishes the
agent's **risk group (RG1–RG4)**, combines it with the **procedure** (aerosol-generating steps,
sharps, volumes, concentrations) and **staff competence**, and selects the **biosafety level
(BSL-1–BSL-4)** with its **primary containment** — biosafety-cabinet (BSC) class, directional
airflow, waste decontamination — **with PPE as the documented residual barrier**. A bare "wear a
respirator and gloves" treatment with no biosafety cabinet or BSL-appropriate facility is **refused**
— PPE substituted for engineering containment is a PPE-led control, never the primary one.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**the risk-group → BSL determination with engineering containment before PPE, never inventing a
classification it cannot establish**. Where the agent's risk group is **unknown or unlisted**, the
skill **emits a literal `[GAP]` and routes to a competent biosafety officer** — it **never invents a
risk group or a BSL** (an invented BSL is an indefensible containment decision). Laboratory
biosafety inputs are **special-category health data (PHI)** — the **specimen-source patient's
identity** and the **worker's serological-surveillance / occupational-health record** are scrubbed to
role labels **before** drafting, any lab-incident / exposure category with **fewer than 5
individuals is suppressed** (small-cell back-calculation guarded), and the skill **never** emits a
re-identification key file. Grounded in the **CDC/NIH Biosafety in Microbiological and Biomedical
Laboratories (BMBL, 6th ed., 2020)** biosafety levels BSL-1–4 + biosafety-cabinet classes, the
**WHO Laboratory Biosafety Manual (4th ed., 2020)** risk groups RG1–RG4 + risk-assessment approach,
the **NIH Guidelines** (recombinant / synthetic nucleic acids, IBC pointer), **UK COSHH 2002 + the
ACDP hazard groups**, **OSHA 29 CFR 1910.1030** where a procedure handles human blood / OPIM, and
**India Bio-Medical Waste Management Rules 2016** lab-waste segregation via `hse-india`.
Decision-support only; a competent person (a **Biological Safety Officer**) must review the output.

## When to use this skill

Use this skill when the user needs a **biosafety risk assessment for a concrete laboratory and
procedure** — for example "assess the biosafety of our diagnostic TB-culture work", "what biosafety
level do we need to handle this agent?", "select the biosafety-cabinet class for this aerosol-
generating procedure", "write a biosafety risk assessment for the research lab", or "review our
containment plan for handling human serum". It is **not** for a generic "how do labs stay safe?"
answer: the Workflow intake below forces the named lab + the specific agent + the procedure, runs the
**risk-group → BSL determination**, refuses a vague "a lab" request, refuses a behaviour/PPE-led
"wear a respirator and gloves" treatment where engineering containment (a BSC, the BSL facility) is
required, and **emits `[GAP]` rather than inventing a risk group for an unknown agent**.

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
extension — the **specimen-source-patient** confidentiality rule, the **worker
serological-surveillance OH-record** rule, the **`<5` small-cell suppression with secondary
back-calculation guard**, and the **re-identification-key-separation** instruction — lives in
`references/deid-checklist.md` and the **Workflow de-id step** below (it is NOT in the byte-identical
block above).

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
| Biosafety determination spine (every run) | ../../knowledge-base/standards/biosafety-bmbl-who.md (KB-STD-BIOSAFETY-BMBL-WHO) — the CDC/NIH **BMBL 6th ed** biosafety levels **BSL-1–4** + **biosafety-cabinet classes** and the **WHO LBM 4th ed** risk groups **RG1–RG4** + risk-assessment structure; the **risk-group → containment-level** decision (cite the levels / classes / groups, never paste the manual) |
| Biosafety RA gate (every run) | ../../knowledge-base/prompt-snippets/biosafety-ra.md (KB-SNIP-BIOSAFETY-RA) — the **classify the risk group (RG1–RG4; unknown → `[GAP]`, never invent) → assess the procedure → select the BSL → engineering/BSC containment before PPE** gate; a BSL selected from a guessed risk group, or a PPE-led plan without the required BSC/ventilation, is rejected; exposure reporting is small-cell-suppressed |
| Healthcare clause cross-walk (every run) | ../../knowledge-base/prompt-snippets/healthcare-clause-map.md (KB-SNIP-HEALTHCARE-CLAUSE-MAP) — the bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent |
| USA (procedures handling human blood / OPIM) | ../../knowledge-base/regulatory/osha-bbp.md (KB-REG-OSHA-BBP) — OSHA 29 CFR 1910.1030 ((c) ECP / (d)(2) engineering & work-practice controls / (f) confidential post-exposure follow-up + HBV vaccination) where a lab procedure handles human blood / OPIM (cite the paragraph topics, never paste the rule) |
| India | ../../knowledge-base/regulatory/in-bmw2016.md (KB-REG-IN-BMW2016) — India Bio-Medical Waste Management Rules 2016 lab-waste segregation; **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and the **biosafety determination spine**
`KB-STD-BIOSAFETY-BMBL-WHO`, runs the **risk-group → BSL containment gate** `KB-SNIP-BIOSAFETY-RA`
(classify the risk group → assess the procedure → select the BSL → engineering/BSC containment before
PPE), aligns with the other hse-healthcare skills through `KB-SNIP-HEALTHCARE-CLAUSE-MAP`, applies
`KB-SNIP-HOC` to every control, and reuses the `KB-SNIP-ARCHETYPES` subagent roster. The biosafety
assessment is a **structured determination** over the named agent + procedure + the cited
BMBL/WHO LBM classification — **not a calculation** (no new engine). Where a procedure handles human
blood / OPIM on a US site, also ground in `KB-REG-OSHA-BBP`; for India, resolve the state via
`hse-india` (**mandatory state detection**) per the BMW Rules 2016 lab-waste stream, and emit a
literal `[GAP]` where a state return is owed — never a minted national form number. **Where the
agent's risk group cannot be established, emit `[GAP]` and route to a competent biosafety officer —
never invent a risk group or BSL.** The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**De-identify FIRST (the highest-PHI step — before any drafting).** Run the `deid` block +
`references/deid-checklist.md` BEFORE the intake echo-back drives any analysis. Laboratory biosafety
inputs are special-category health data: scrub the **specimen-source patient's identity** (referenced
by role only; any clinical / serostatus detail held in a separate confidential record), the
**worker's identity, job, and serological-surveillance / occupational-health record** (role-label
"Worker A"; the OH record held confidentially, separate from the assessment), and any **patient
identifier** anywhere in the inputs. Apply **`<5` small-cell suppression** (with secondary
suppression) to every lab-incident / exposure category, and produce a SEPARATE access-controlled
re-identification key — **never** co-located with the assessment and **never** emitted as a key file.

Run the biosafety intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "a lab": you need the named laboratory + the specific
agent + the procedure before any containment decision. Refuse a behaviour/PPE-led "wear a respirator
and gloves" treatment where a biosafety cabinet or the BSL facility is required. Where the agent's
risk group cannot be established, emit `[GAP]` — never invent a risk group or BSL.**

1. **The named lab & the agent / material** (free-text — the specificity anchor) — "Name the exact
   laboratory (clinical / diagnostic, research, teaching, public-health) **and the specific
   biological agent or material** handled (the organism / sample type, recombinant material, human
   blood / OPIM). **Refuse 'a lab' — the assessment is lab- and agent-specific.**"
2. **The agent's risk group (RG1–RG4)** (mcq — asked FIRST among the determination) — RG1 / RG2 /
   RG3 / RG4 / **Unknown**. **`Unknown` → emit `[GAP]` and route to a competent biosafety officer —
   never assume or invent a risk group.** The risk group is the primary input to the BSL, not the
   cabinet or the PPE.
3. **The procedure & aerosol potential** (free-text) — the steps performed, **aerosol-generating
   activities** (centrifugation, sonication, vortexing, pipetting), sharps, volumes, and
   concentrations. **A BSL selected from the agent alone, ignoring aerosolization, is FLAGGED** —
   the procedure modifies the required containment.
4. **Primary containment & facility** (multi-select) — biosafety-cabinet **class** (I / II A–B /
   III) · directional airflow / ventilation · waste decontamination (autoclave) · the BSL facility
   features. **A plan that relies on PPE without the BSC / ventilation the level requires fails
   (PPE-led).**
5. **Staff competence & exposure response** (free-text) — staff training / competence, the
   immunisation / serological-surveillance offer (held confidentially), and the exposure pathway
   (first aid → confidential report → occupational-health follow-up). **Refuse to draft a pathway
   that names a specimen-source patient or worker in the circulated assessment.**
6. **Jurisdiction** (mcq) — USA (OSHA 1910.1030 where human blood/OPIM) / EU-UK (COSHH 2002 + ACDP
   hazard groups) / India / Other / Unknown. **India → resolve the state via `hse-india` (mandatory
   state detection); BMW Rules 2016 lab-waste segregation; emit `[GAP]`, never a national form
   number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented agent, risk group, or BSL.

Then: record the **risk-group determination first** (`KB-SNIP-BIOSAFETY-RA`; an unknown risk group
is a `[GAP]`, never invented); assess the procedure / aerosol potential; **select the biosafety
level (BSL-1–BSL-4)** and the **primary containment (engineering first)** via the `controls` engine
(biosafety-cabinet class + ventilation + decontamination → administrative procedures → **PPE last**
— a treatment substituting gloves/respirator for a biosafety cabinet or the BSL facility is a FLAG
pushed up the hierarchy); record the **biosecurity / access-control** measures; frame the residual
biosafety risk via `risk_matrix`; make every action a SMART action via `smart_actions` → validate
the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format
section below. The domain method is in `references/METHODOLOGY.md`.

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

For a multi-area biosafety assessment the triage gate fans out (moderate 2–3; the **De-identifier
runs FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier — esp. the
  **specimen-source patient's identity** and a **named worker's serological-surveillance / OH
  record** — to role labels before any analysis; apply `<5` small-cell suppression (with secondary
  suppression) to every lab-incident / exposure category; return the re-identification key SEPARATELY
  to the orchestrator, never to a sibling, and never as a key file.
- **Risk-Group-&-Containment-Analyst** — runs the **risk-group → BSL determination** gate
  (`KB-SNIP-BIOSAFETY-RA`): classify the agent's risk group (RG1–RG4; **unknown → `[GAP]`, never
  invent**); assess the procedure / aerosol potential; select the **biosafety level** and the
  **primary containment (engineering first — BSC class, ventilation, decontamination)** via the
  `controls` engine. A treatment that **substitutes gloves/respirator for a biosafety cabinet or the
  BSL facility**, or **assigns a BSL from a guessed risk group**, is a **FLAG pushed up the
  hierarchy / a `[GAP]`, never the headline control**. SCOPE-OUT: does not author the biosecurity /
  exposure-response section (the Biosecurity-&-Response-Author) or de-identify (the De-identifier).
- **Biosecurity-&-Response-Author** — author the **biosecurity / access-control** measures, the
  **immunisation / serological-surveillance** offer (held confidentially), and the **confidential
  exposure-response pathway** (first aid → confidential report → occupational-health follow-up).
  **No specimen-source patient or worker is named in the circulated artifact.** SCOPE-OUT: does not
  determine the risk group / BSL (the Risk-Group-&-Containment-Analyst) or de-identify (the
  De-identifier).
- **Critic/QA** (MANDATORY) — adversarial final pass: the risk-group determination is recorded
  BEFORE the BSL, an unknown risk group is a `[GAP]` (never invented), the BSL matches the risk
  group + procedure, engineering containment (BSC class + ventilation) precedes PPE, no PPE-led
  treatment is the headline control, the biosecurity / access-control measures are present, no `<5`
  lab-incident cell is published, and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the risk-group → BSL
determination, the A7 `controls` / `risk_matrix` / `smart_actions` calls inline, the biosecurity /
confidential exposure-response section, then the mandatory Critic/QA + SME pass — same scope
discipline, no subagents.

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
