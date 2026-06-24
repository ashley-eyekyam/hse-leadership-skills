---
name: sharps-needlestick-management
description: 'Produces a consultant-grade sharps-injury prevention package and
  exposure-control plan for a named healthcare service, driven by the
  engineering-control-first hierarchy. Use this skill whenever a user asks to
  prevent needlestick or sharps injuries, write or review a bloodborne-pathogen
  exposure control plan, build a sharps injury log, evaluate safer devices,
  set a no-recapping rule, or plan post-exposure follow-up for a clinic, ward,
  lab, dental practice, or ambulance. It forces the engineering-control-first
  hierarchy (eliminate unnecessary sharps -> safety-engineered devices ->
  no-recapping / safe-disposal -> PPE last), records the de-identified OSHA Sharps
  Injury Log, and builds a confidential source-testing / PEP pathway (source
  patient and worker by role only). It refuses a behaviour-led "be careful"
  treatment where a sharp could be eliminated or engineered out. Grounded in OSHA
  1910.1030 + the Needlestick Act and EU Directive 2010/32/EU.
  Decision-support only; a competent person must review.'
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

# Sharps & Needlestick Management

A consultant-grade, **engineering-control-first** sharps-injury prevention and bloodborne-pathogen
exposure-control package for a **named healthcare service or unit** — a ward, clinic, community/home
care service, dental practice, ambulance service, or clinical laboratory — never a generic "a
clinic". Its entire reason to exist is that **sharps safety leads with elimination and
safety-engineered devices, not behaviour rules**: every plan first records whether an unnecessary
sharp can be **eliminated or substituted** (needle-free connectors, alternative routes); only the
**residual** sharps are controlled by safety-engineered devices, then safe work practices
(no-recapping, point-of-use disposal), with **PPE and post-exposure prophylaxis as the documented
last lines**. A bare "staff to take care / wear gloves" is **refused** — a behaviour rule is an
administrative control, never the primary control where the sharp could be eliminated or engineered
out.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**the elimination/safety-engineered-device decision plus the full hierarchy of controls, with the
incident never identifying a person**. Bloodborne-pathogen exposure data is **special-category
health data (PHI)** — the **source patient's identity and serostatus** (HIV/HBV/HCV) and the
**injured worker's identity and PEP medical record** are scrubbed to role labels **before**
drafting (OSHA 1910.1030(f) confidentiality), the **Sharps Injury Log** in the circulated artifact
is **de-identified and aggregated** (never line-level), and a sharps-injury category with **fewer
than 5 individuals is suppressed** (small-cell back-calculation guarded). The skill **never** emits
a re-identification / exposure key file — the key is an instruction to the competent person, held
separately and access-controlled. Grounded in **OSHA 29 CFR 1910.1030** ((c) Exposure Control Plan,
(c)(1)(iv) annual safer-device evaluation, (d)(2) engineering & work-practice controls, (f)
confidential post-exposure follow-up, (h)(5) Sharps Injury Log), the **Needlestick Safety and
Prevention Act (PL 106-430, 2000)**, **EU Directive 2010/32/EU** + the **UK Sharps Regulations
2013** with COSHH, and **India Bio-Medical Waste Management Rules 2016** sharps segregation via
`hse-india`. Decision-support only; a competent person (occupational-health / infection-control
professional) must review the output.

## When to use this skill

Use this skill when the user needs a **sharps-injury prevention / exposure-control plan for a
concrete healthcare service** — for example "prevent needlestick injuries on the phlebotomy round",
"write a bloodborne-pathogen exposure control plan for the dental practice", "build a sharps injury
log for the ward", "evaluate safer IV cannulae", or "plan the post-exposure follow-up pathway". It
is **not** for a generic "how do I avoid needlesticks?" answer: the Workflow intake below forces the
named service and its real sharps inventory, the elimination/substitution decision, and the
safety-engineered-device process before any control plan, refuses a vague "a clinic" request, and
refuses a behaviour-led "staff to take care / wear gloves" treatment where the sharp could be
eliminated or a safety-engineered device fitted.

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
extension — the **source-patient serostatus** rule, the **injured-worker OH-record** rule, the
**`<5` small-cell suppression with secondary back-calculation guard**, and the
**re-identification-key-separation** instruction — lives in `references/deid-checklist.md` and the
**Workflow de-id step** below (it is NOT in the byte-identical block above).

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
| Sharps control spine (every run) | ../../knowledge-base/prompt-snippets/sharps-hierarchy.md (KB-SNIP-SHARPS-HIERARCHY) — the **eliminate → safety-engineered device → safe-procedure → PPE/PEP-residual** sharps control gate: a PPE-led / "be careful" treatment of a sharp that could be eliminated or engineered out is rejected; exposure reporting is small-cell-suppressed |
| Healthcare clause cross-walk (every run) | ../../knowledge-base/prompt-snippets/healthcare-clause-map.md (KB-SNIP-HEALTHCARE-CLAUSE-MAP) — the bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent |
| USA | ../../knowledge-base/regulatory/osha-bbp.md (KB-REG-OSHA-BBP) — OSHA 29 CFR 1910.1030 ((c) ECP / (c)(1)(iv) annual safer-device evaluation with frontline input / (d)(2) engineering & work-practice controls / (f) confidential post-exposure follow-up / (h)(5) Sharps Injury Log) + the Needlestick Safety and Prevention Act (cite the paragraph topics, never paste the rule) |
| EU / UK | ../../knowledge-base/regulatory/eu-sharps-2010-32.md (KB-REG-EU-SHARPS-2010-32) — EU Directive 2010/32/EU (eliminate unnecessary sharps, safer engineered devices, recapping ban, safe disposal, training, reporting + PEP) + the UK Sharps Regulations 2013 with COSHH (cite the member-state transposition for the binding duty) |
| India | ../../knowledge-base/regulatory/in-bmw2016.md (KB-REG-IN-BMW2016) — India Bio-Medical Waste Management Rules 2016 sharps segregation (yellow/blue/white-translucent stream); **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and leads every plan with the
**sharps engineering-first spine** `KB-SNIP-SHARPS-HIERARCHY` (eliminate the sharp → safety-engineered
device → safe work practices → PPE/PEP residual), aligns with the other hse-healthcare skills through
`KB-SNIP-HEALTHCARE-CLAUSE-MAP`, applies `KB-SNIP-HOC` to every control, and reuses the
`KB-SNIP-ARCHETYPES` subagent roster. The control selection is a **structured engineering-control-first
method** over the named device inventory + the cited OSHA/EU hierarchy — **not a calculation** (no new
engine). For a US site ground in `KB-REG-OSHA-BBP`; EU/UK in `KB-REG-EU-SHARPS-2010-32` (cite the
member-state transposition); for India, resolve the state via `hse-india` (**mandatory state
detection**) per the BMW Rules 2016, and emit a literal `[GAP]` where a state return is owed — never a
minted national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**De-identify FIRST (the highest-PHI step — before any drafting).** Run the `deid` block +
`references/deid-checklist.md` BEFORE the intake echo-back drives any analysis. Bloodborne-pathogen
exposure data is special-category health data: scrub the **source-patient identity and serostatus**
(HIV/HBV/HCV — never written into a circulated plan; the source-testing pathway references "the
source patient" by role only, with consent + a separate confidential record), the **injured
worker's identity, job, shift, and exposure/PEP medical record** (role-label "Worker A"; the medical
record is held confidentially, separate from the plan, per OSHA 1910.1030(f)), and any **patient
identifier** anywhere in the inputs. Apply **`<5` small-cell suppression** (with secondary
suppression) to every sharps-injury category, and produce a SEPARATE access-controlled
re-identification/exposure key — **never** co-located with the plan and **never** emitted as a key
file.

Run the sharps intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to plan for "a clinic": you need the named service + its real
sharps inventory + the elimination/substitution decision before any control plan. Refuse a
behaviour-led "staff to take care / wear gloves" treatment where the sharp could be eliminated or a
safety-engineered device fitted.**

1. **The named service & sharps inventory** (free-text — the specificity anchor) — "Name the exact
   unit / service (ward, phlebotomy round, dental surgery, ambulance, lab) **and the sharps actually
   used** (hollow-bore needles, lancets, scalpels, IV cannulae, suture needles). **Refuse 'a clinic'
   / 'the ward' — the plan is service-specific.**"
2. **Can any sharp be eliminated or substituted?** (mcq — asked FIRST among the controls) — yes →
   **remove unnecessary sharps / substitute needle-free connectors**: the plan leads with
   elimination · no → branch to engineering controls (Q3). **Eliminating the sharp is the primary
   control, not the safety device.**
3. **Safety-engineered devices in use** (free-text) — which devices have an integrated
   sharps-protection mechanism, which do not, and the **frontline-worker selection process**. **A
   non-engineered device still in use without a recorded justification is FLAGGED** — OSHA mandates a
   documented **annual safer-device evaluation with non-managerial frontline-worker input**.
4. **Work practices & disposal** (multi-select) — no-recapping rule · point-of-use sharps containers
   (fill line, location) · safe-disposal route · single-handed/scoop technique. **A plan permitting
   recapping by hand fails.**
5. **Exposure response** (free-text) — the post-exposure pathway: immediate first aid →
   **confidential** incident report → **source-patient testing with consent and confidentiality** →
   PEP timing for HBV/HCV/HIV → follow-up → the Sharps Injury Log entry. **Refuse to draft a pathway
   that names a source patient or worker in the circulated plan.**
6. **Jurisdiction** (mcq) — USA (OSHA 1910.1030) / EU (Directive 2010/32/EU + transposition) / UK
   (Sharps Regs 2013 / COSHH) / India / Other / Unknown. **India → resolve the state via `hse-india`
   (mandatory state detection); BMW Rules 2016 sharps segregation; emit `[GAP]`, never a national
   form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented device or count.

Then: record the **elimination/substitution decision first** (`KB-SNIP-SHARPS-HIERARCHY`); rank the
residual controls up the hierarchy via the `controls` engine (eliminate → safety-engineered devices
& containers → no-recapping/safe-disposal work practices → **PPE last** — a behaviour-led / PPE-led
treatment where the sharp could be eliminated is a FLAG pushed up the hierarchy); record the
**documented safer-device consideration with frontline-worker involvement**; build the **confidential
post-exposure (PEP) pathway** (first-aid → report → consented source-testing → PEP → follow-up) and
the **de-identified/aggregated Sharps Injury Log structure**; frame the residual sharps-exposure risk
via `risk_matrix`; make every action a SMART action via `smart_actions` → validate the draft against
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

For a multi-area sharps program the triage gate fans out (moderate 2–3; the **De-identifier runs
FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier — esp. the **source
  patient's identity and serostatus** (HIV/HBV/HCV) and a **named injured worker's PEP medical
  record** — to role labels before any analysis; apply `<5` small-cell suppression (with secondary
  suppression) to every sharps-injury category; return the re-identification / exposure key
  SEPARATELY to the orchestrator, never to a sibling, and never as a key file.
- **Controls-&-Device-Analyst** — runs the **elimination → safety-engineered-device → work-practice**
  hierarchy via the `controls` engine: lead with eliminating unnecessary sharps; specify the
  safety-engineered devices + the **documented safer-device consideration with frontline-worker
  involvement**; define no-recapping + point-of-use disposal. A treatment that **leads with "be
  careful / wear gloves" where the sharp could be eliminated or engineered out** is a **FLAG pushed
  up the hierarchy, never the headline control**. SCOPE-OUT: does not author the PEP pathway / log
  (the Exposure-Response-&-Log-Author) or de-identify (the De-identifier).
- **Exposure-Response-&-Log-Author** — author the **confidential post-exposure (PEP) pathway**
  (first-aid → confidential report → **consented** source-patient testing → PEP timing for
  HBV/HCV/HIV → follow-up), the **de-identified/aggregated Sharps Injury Log structure** (never
  line-level identified), and the HBV-vaccination status. **No source patient or worker is named in
  the circulated artifact.** SCOPE-OUT: does not select the controls (the Controls-&-Device-Analyst)
  or de-identify (the De-identifier).
- **Critic/QA** (MANDATORY) — adversarial final pass: the elimination/substitution decision is
  recorded BEFORE any device or PPE, every non-engineered device carries a justification, the
  no-recapping rule is present, the annual safer-device consideration + frontline involvement is
  recorded, the Sharps Injury Log is de-identified/aggregated, the PEP pathway preserves
  source-patient and worker confidentiality, **no `<5` injury cell is published**, and ZERO
  de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the
elimination/substitution decision, the A7 `controls` / `risk_matrix` / `smart_actions` calls inline,
the confidential PEP pathway + the de-identified Sharps Injury Log, then the mandatory Critic/QA +
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
