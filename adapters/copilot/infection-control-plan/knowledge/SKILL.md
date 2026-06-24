---
name: infection-control-plan
description: 'Produces a consultant-grade, transmission-based infection prevention
  and control (IPC) plan for a named healthcare service or unit, driven by the
  engineering-and-administrative-controls-before-PPE hierarchy. Use this skill when a
  user asks to build or review an infection control plan, write an isolation /
  transmission-based precautions plan, select contact / droplet / airborne precautions
  for a ward or care home, decide device reprocessing by Spaulding classification, or
  plan de-identified outbreak / HAI surveillance. It forces Standard
  Precautions for every patient and the route-correct precautions,
  leads with engineering controls (ventilation, negative-pressure isolation rooms) and
  administrative controls (cohorting, screening) BEFORE PPE, applies the Spaulding
  reprocessing decision, and refuses a PPE-only plan (an airborne agent on a respirator
  alone, no isolation room). Grounded in the CDC isolation guideline + WHO IPC core
  components + Spaulding. Decision-support only; a competent person must review.'
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
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-healthcare
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Infection Control Plan

A consultant-grade, **engineering-and-administrative-controls-before-PPE** transmission-based
infection prevention and control (IPC) plan for a **named healthcare service or unit** — a ward,
clinic, community/home-care service, care home, dental practice, ambulance service, or clinical
laboratory — never a generic "a hospital". Its entire reason to exist is that **IPC leads with
ventilation, isolation, and administrative controls, not with PPE**: every plan applies **Standard
Precautions to every patient**, identifies the **transmission route(s)** of the agent(s) in scope,
and layers the correct **Transmission-Based precautions by route** — with **engineering controls**
(ventilation, negative-pressure / airborne-infection isolation rooms, single rooms, safer devices)
and **administrative controls** (cohorting, screening, signage, restricted entry) applied **before**
PPE, which is the **residual barrier, last**. A bare "give everyone an N95 / wear a mask" for an
airborne agent with **no isolation room or ventilation provision** is **refused** — a respirator is
the residual control, never the primary one where the route demands an engineering control.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**the route-correct precautions plus the full hierarchy of controls (engineering/administrative
before PPE), with no case or cluster ever identifying a patient**. Healthcare infection data is
**special-category health data (PHI)** — a **patient's infection / colonisation status** and any
**outbreak / cluster detail** are de-identified to role / aggregate level **before** drafting, the
surveillance in the circulated artifact is **de-identified and aggregated** (never line-level), and
a case category with **fewer than 5 individuals is suppressed** (small-cell back-calculation
guarded — a 3-case cluster on a named ward re-identifies patients). The skill follows the
**documented-procedure** PHI model: it emits **no re-identification key file** (the key is an
instruction to the competent person, held separately) and adds **no new report field** — the
de-identified banner is the existing report `meta.deid_notice` header. Grounded in the **CDC
Guideline for Isolation Precautions** (Standard + Transmission-Based: contact / droplet / airborne),
the **WHO Core Components of IPC Programmes**, and the **Spaulding classification** (critical →
sterilization / semi-critical → high-level disinfection / non-critical → low-level), with the **UK
Health and Social Care Act 2008 Hygiene Code**, the **OSHA bloodborne-pathogens** confidentiality
discipline, and **India Bio-Medical Waste Management Rules 2016** via `hse-india`. Decision-support
only; a competent person (infection-prevention & control professional) must review the output.

## When to use this skill

Use this skill when the user needs an **infection control / isolation plan for a concrete healthcare
service** — for example "build an IPC plan for the respiratory ward", "write the transmission-based
precautions for a suspected TB admission", "select contact / droplet / airborne precautions for the
care home", "structure our IPC programme against the WHO core components", "decide how to reprocess
the endoscopes by Spaulding", or "set up de-identified HAI surveillance". It is **not** for a generic
"how do I stop infections?" answer: the Workflow intake below forces the named service, the agent(s)
and their transmission route(s), and the engineering/administrative controls **before** PPE, refuses
a vague "a hospital" request, and refuses a PPE-only treatment (an airborne agent managed by a
respirator alone with no isolation room or ventilation provision).

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
extension — the **patient infection/colonisation-status** rule, the **outbreak / cluster
confidentiality** rule, the **`<5` small-cell suppression with secondary back-calculation guard**
(a 3-case cluster on a named ward re-identifies patients), and the
**re-identification-key-separation** instruction (documented-procedure model — no key file, no new
report field; the banner is the existing `meta.deid_notice` header) — lives in
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
| IPC framework spine (every run) | ../../knowledge-base/standards/ipc-cdc-who.md (KB-STD-IPC-CDC-WHO) — the **CDC isolation precautions + WHO IPC core components + Spaulding** topic→artifact structure map: Standard + Transmission-Based precautions (contact/droplet/airborne), the WHO programme core components, and the critical/semi-critical/non-critical reprocessing decision (cite the topics, never paste the guideline) |
| Per-route precaution selection (every run) | ../../knowledge-base/prompt-snippets/ipc-precautions.md (KB-SNIP-IPC-PRECAUTIONS) — the **Standard-always → identify route → layer Transmission-Based precautions → engineering/administrative before PPE** gate: a plan that jumps to PPE without the room/ventilation control the route requires, or an airborne agent with no AIIR/respirator, is rejected; cluster reporting is small-cell-suppressed |
| Healthcare clause cross-walk (every run) | ../../knowledge-base/prompt-snippets/healthcare-clause-map.md (KB-SNIP-HEALTHCARE-CLAUSE-MAP) — the bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent |
| USA / bloodborne-exposure confidentiality | ../../knowledge-base/regulatory/osha-bbp.md (KB-REG-OSHA-BBP) — OSHA 29 CFR 1910.1030 confidentiality discipline for exposure / health data ((f) confidential post-exposure follow-up) reused for IPC PHI handling (cite the paragraph topics, never paste the rule) |
| India | ../../knowledge-base/regulatory/in-bmw2016.md (KB-REG-IN-BMW2016) — India Bio-Medical Waste Management Rules 2016 segregation (yellow/red/blue/white-translucent stream); **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 / 8.1.2) and the **IPC framework spine**
`KB-STD-IPC-CDC-WHO` (CDC isolation precautions + WHO core components + Spaulding), selects precautions
by route through `KB-SNIP-IPC-PRECAUTIONS` (**Standard always → engineering/administrative controls
before PPE**), aligns with the other hse-healthcare skills through `KB-SNIP-HEALTHCARE-CLAUSE-MAP`,
applies `KB-SNIP-HOC` to every control, and reuses the `KB-SNIP-ARCHETYPES` subagent roster. The
precaution selection is a **structured route-driven method** over the named unit + agents + the cited
CDC/WHO/Spaulding frameworks — **not a calculation** (no new engine). For US exposure / health-data
confidentiality ground in `KB-REG-OSHA-BBP`; for India, resolve the state via `hse-india`
(**mandatory state detection**) per the BMW Rules 2016, and emit a literal `[GAP]` where a state
return is owed — never a minted national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**De-identify FIRST (the highest-PHI step — before any drafting).** Run the `deid` block +
`references/deid-checklist.md` BEFORE the intake echo-back drives any analysis. Healthcare infection
data is special-category health data: scrub any **patient's infection / colonisation status** (never
attributed to a named person in a circulated plan), any **outbreak / cluster detail** (reported
de-identified and aggregated), and any patient/staff identifier anywhere in the inputs. Apply **`<5`
small-cell suppression** (with secondary suppression) to every case / cluster category — a 3-case
cluster on a named ward re-identifies patients (the small-cell back-calculation). Follow the
**documented-procedure PHI model**: the re-identification key is an **instruction** to the competent
person (held separately, access-controlled) — the skill emits **no key file** and adds **no new
report field** (the de-identified banner is the existing report `meta.deid_notice` header).

Run the IPC intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to plan for "a hospital": you need the named service + the agent(s)
and their transmission route(s) before any precaution plan. Refuse a PPE-only treatment — an airborne
agent managed by a respirator alone with no airborne-infection isolation room or ventilation
provision is rejected and pushed up the hierarchy.**

1. **The named service & unit** (free-text — the specificity anchor) — "Name the exact unit / service
   (ward, clinic, care home, dental surgery, ambulance, lab). **Refuse 'a hospital' / 'the ward' —
   the plan is service-specific.**"
2. **The agent(s) and their transmission route(s)** (mcq+free-text — the routing anchor) — contact /
   droplet / airborne / a combination (and the suspected/confirmed agent). **The route drives the
   precautions; an unknown route is a `[GAP]`, resolved before precautions are selected.**
3. **Engineering controls available** (free-text — asked BEFORE PPE) — ventilation, single rooms,
   negative-pressure / airborne-infection isolation room (AIIR), safer devices. **An airborne agent
   with no AIIR or ventilation provision controlled by a respirator alone is FLAGGED and pushed up the
   hierarchy.**
4. **Administrative controls** (multi-select) — cohorting · early screening / triage · isolation
   signage · restricted entry · hand-hygiene programme + audit. **These precede PPE.**
5. **Device reprocessing (Spaulding)** (free-text) — which devices contact sterile tissue/bloodstream
   (critical → **sterilization**), mucous membranes / non-intact skin (semi-critical → **high-level
   disinfection**), or intact skin (non-critical → low-level). **High-level disinfection of a critical
   device is a Spaulding mis-application and fails.**
6. **Surveillance** (free-text) — HAI / outbreak / cluster monitoring. **Reported de-identified and
   aggregated; every `<5` case category suppressed (with secondary back-calc guard). Refuse to report
   an outbreak on a named ward in a way that re-identifies a patient.**
7. **Jurisdiction** (mcq) — USA / UK / EU / India / Other / Unknown. **India → resolve the state via
   `hse-india` (mandatory state detection); BMW Rules 2016 segregation; emit `[GAP]`, never a national
   form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented agent, route, or count.

Then: apply **Standard Precautions to every patient**, identify the **transmission route(s)**, and
layer the **Transmission-Based precautions by route** (`KB-SNIP-IPC-PRECAUTIONS`); rank the controls
up the hierarchy via the `controls` engine (**engineering — ventilation/AIIR/single rooms — →
administrative — cohorting/screening/signage — → PPE last**; a PPE-only / respirator-alone treatment
where the route demands an engineering control is a FLAG pushed up the hierarchy); record the
**Spaulding reprocessing decision** per device class; structure the **WHO IPC programme** (core
components); build the **de-identified / aggregated surveillance** with `<5` small-cell suppression;
frame the residual transmission risk via `risk_matrix`; make every action a SMART action via
`smart_actions` → validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output
via the Output format section below. The domain method is in `references/METHODOLOGY.md`.

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

For a multi-route IPC plan the triage gate fans out (moderate 2–3; the **De-identifier runs FIRST —
sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every patient/staff identifier — esp. any **patient's
  infection / colonisation status** and any **outbreak / cluster detail** — to role / aggregate level
  before any analysis; apply `<5` small-cell suppression (with secondary suppression) to every case /
  cluster category (a 3-case cluster on a named ward re-identifies patients); the re-identification
  key is an instruction returned SEPARATELY to the orchestrator, never to a sibling, and never as a
  key file.
- **Precautions-&-Controls-Analyst** — applies **Standard Precautions to every patient**, identifies
  the **transmission route(s)**, and layers the **Transmission-Based precautions by route** via the
  `controls` engine: lead with **engineering controls** (ventilation, AIIR / negative pressure, single
  rooms) and **administrative controls** (cohorting, screening, signage), with **PPE as the residual
  barrier last**. A treatment that **leads with PPE — an airborne agent managed by a respirator alone
  with no isolation room or ventilation** — is a **FLAG pushed up the hierarchy, never the headline
  control**. SCOPE-OUT: does not author the surveillance / programme structure (the
  Surveillance-&-Programme-Author) or de-identify (the De-identifier).
- **Surveillance-&-Programme-Author** — structures the **WHO IPC programme** (core components) and the
  **de-identified / aggregated surveillance** (HAI / outbreak / cluster — never line-level, every `<5`
  category suppressed with the secondary back-calc guard), and records the **Spaulding reprocessing
  decision** per device class. **No outbreak is reported on a named ward in a way that re-identifies a
  patient.** SCOPE-OUT: does not select the precautions/controls (the Precautions-&-Controls-Analyst)
  or de-identify (the De-identifier).
- **Critic/QA** (MANDATORY) — adversarial final pass: Standard Precautions are applied to every
  patient, the route is identified and the correct Transmission-Based precautions layered, the
  **engineering and administrative controls are recorded BEFORE PPE** (a respirator-alone airborne plan
  is flagged), the Spaulding reprocessing decision is correct (no high-level disinfection of a critical
  device), the surveillance is de-identified / aggregated, **no `<5` case cell is published** (with the
  secondary back-calc guard), and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then Standard + the route-correct
Transmission-Based precautions, the A7 `controls` / `risk_matrix` / `smart_actions` calls inline, the
Spaulding decision + the WHO programme structure + the de-identified surveillance, then the mandatory
Critic/QA + SME pass — same scope discipline, no subagents.

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
