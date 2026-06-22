---
name: workplace-violence-prevention
description: 'Produces a consultant-grade workplace-violence-prevention (WPV)
  program for a named healthcare service — the worksite hazard analysis, the
  type-1-4 violence taxonomy, environmental and administrative controls, and the
  confidential incident log. Use this skill whenever a user asks to prevent
  workplace violence or aggression in healthcare, build a WPV program or plan,
  assess violence risk in an ED / mental-health / care setting, design
  de-escalation or security controls, or set up violence incident reporting. It
  leads with environmental and administrative design (controlled access,
  sightlines, alarms / duress, staffing, lone-working) before reactive measures,
  classifies violence by source (type 1 criminal -> type 4 personal), and records
  a de-identified worksite analysis with small-cell suppression. It refuses a
  program headlined by "personal alarms / self-defence training" alone. Grounded
  in OSHA 3148 + §5(a)(1) and Cal/OSHA 8 CCR 3342. Decision-support only; review
  by a competent person.'
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

# Workplace-Violence Prevention

A consultant-grade, **environmental-and-administrative-control-first** workplace-violence (WPV)
prevention program for a **named healthcare service or unit** — an emergency department, a
mental-health unit, a reception / triage area, a community or lone home-visit service, an ambulance
service, or a residential care setting — never a generic "a hospital". Its entire reason to exist is
that **WPV is controlled by designing out the exposure, not by reactive measures**: every program
first records the **worksite hazard analysis** (records review, incident log, walkthrough, staff
input) and then leads with **environmental / engineering controls** (controlled access, sightlines,
alarm / duress systems, secure design) and **administrative controls** (staffing / skill-mix,
lone-working procedures, known-risk-patient flagging, no-retaliation reporting), with
**de-escalation, response training, and personal alarms as the documented residual lines**. A bare
"issue personal alarms and run self-defence training" is **refused** as the headline — a reactive
measure is the last line, never the primary control where the exposure could be designed out.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**the worksite hazard analysis plus the environmental-and-administrative-before-reactive hierarchy
of controls, with the incident never identifying a person**. Workplace-violence incident data is
**special-category health data (PHI)** — a **named victim, assailant, or known-risk patient** and
any **behavioural-health flag** are scrubbed to role labels **before** drafting, the **worksite
analysis and incident log** in the circulated artifact are **de-identified and aggregated** (never
line-level), and an incident category with **fewer than 5 individuals is suppressed** (small-cell
back-calculation guarded — a 2-incident category on a named ward de-anonymizes the people involved).
The skill **never** emits a re-identification key file — the key is an instruction to the competent
person, held separately and access-controlled. Grounded in **OSHA Publication 3148 (2016)**
*Guidelines for Preventing Workplace Violence for Healthcare and Social Service Workers* (the five
program elements — management commitment & worker participation, worksite analysis, hazard
prevention & control, training, recordkeeping & evaluation), enforced under the **OSH Act §5(a)(1)
General Duty Clause** where a recognized WPV hazard exists, the enforceable **Cal/OSHA Workplace
Violence Prevention in Health Care standard, 8 CCR 3342** (written plan, type-1-4 taxonomy, employee
involvement, violent-incident log), the **UK HSE management of work-related violence** guidance with
**NICE NG10**, and India occupational-safety provisions via `hse-india`. Decision-support only; a
competent person (healthcare security / WPV / occupational-health professional) must review the
output.

## When to use this skill

Use this skill when the user needs a **workplace-violence-prevention program for a concrete
healthcare service** — for example "prevent violence in the emergency department", "build a WPV
program for the mental-health unit", "assess aggression risk for the community lone-working team",
"design reception / triage security controls", or "set up confidential violence incident reporting".
It is **not** for a generic "how do I stop workplace violence?" answer: the Workflow intake below
forces the named service and where / when violence occurs, the violence type(s), and the worksite
hazard analysis before any control plan, refuses a vague "a hospital" request, and refuses a
reactive-led "issue personal alarms / run self-defence training" treatment where the exposure could
be designed out by environmental or administrative controls.

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
extension — the **named-victim / assailant / known-risk-patient** rule, the **behavioural-health-flag**
rule, the **`<5` small-cell suppression with secondary back-calculation guard**, and the
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
| WPV control spine (every run) | ../../knowledge-base/prompt-snippets/wpv-controls.md (KB-SNIP-WPV-CONTROLS) — the **worksite analysis → environmental/engineering → administrative → training/response-residual** WPV control gate: a program led by "de-escalation training / panic buttons" alone, with no environmental or administrative controls, is rejected as reactive-led; incident reporting is small-cell-suppressed |
| Healthcare clause cross-walk (every run) | ../../knowledge-base/prompt-snippets/healthcare-clause-map.md (KB-SNIP-HEALTHCARE-CLAUSE-MAP) — the bundle-shared ISO 45001 6.1.2 + clinical PPE-last cross-walk that keeps the five hse-healthcare skills consistent |
| USA + California | ../../knowledge-base/regulatory/wpv-osha-3148.md (KB-REG-WPV-OSHA3148) — OSHA Publication 3148 (2016) five-element WPV program map (management commitment & worker participation · worksite analysis · hazard prevention & control · training · recordkeeping & evaluation) enforced under the OSH Act §5(a)(1) General Duty Clause where a recognized WPV hazard exists, plus the type-1-4 violence taxonomy and the Cal/OSHA 8 CCR 3342 written-plan / violent-incident-log standard for California healthcare employers (cite the program-element topics + the General Duty Clause, never paste the guideline; cite 8 CCR 3342 as the binding standard in California) |
| EU / UK | ../../knowledge-base/standards/iso-45003.md (KB-STD-ISO45003) — ISO 45003 psychosocial-risk grounding for the aggression/violence aftermath; combine with the UK HSE management of work-related-violence guidance and NICE NG10 (violence & aggression: short-term management in health/community settings) for the binding UK leg (cite the guidance, never paste it) |
| India | India occupational-safety provisions — **defers to `hse-india`, mandatory state detection** (state forms / rules resolved via `KB-REG-IN-STATEFORMS`); emit `[GAP]`, never a national form number |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2, with the `KB-STD-ISO45003` psychosocial link
for the aggression / violence aftermath) and leads every program with the **WPV
environmental-and-administrative-first spine** `KB-SNIP-WPV-CONTROLS` (worksite analysis →
environmental / engineering → administrative → training / response residual), classifying hazards by
the type-1-4 taxonomy and grounding the five program elements in `KB-REG-WPV-OSHA3148`, aligns with
the other hse-healthcare skills through `KB-SNIP-HEALTHCARE-CLAUSE-MAP`, applies `KB-SNIP-HOC` to
every control, and reuses the `KB-SNIP-ARCHETYPES` subagent roster. The control selection is a
**structured environmental-and-administrative-control-first method** over the named service's worksite
analysis + the cited OSHA 3148 / §5(a)(1) / Cal-OSHA framework — **not a calculation** (no new
engine). For a US site ground in `KB-REG-WPV-OSHA3148` (cite §5(a)(1); cite 8 CCR 3342 as the binding
standard in California); for the UK lean on the HSE work-related-violence guidance + NICE NG10; for
India, resolve the state via `hse-india` (**mandatory state detection**) and emit a literal `[GAP]`
where a state return is owed — never a minted national form number. The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**De-identify FIRST (the highest-PHI step — before any drafting).** Run the `deid` block +
`references/deid-checklist.md` BEFORE the intake echo-back drives any analysis. Workplace-violence
incident data is special-category health data: scrub any **named victim, assailant, or known-risk
patient** and any **behavioural-health flag** (role labels only — "Worker A", "the patient"; a
behavioural-health flag is held in a separate confidential clinical record, never written into a
circulated program), and any **patient identifier** anywhere in the inputs. Apply **`<5` small-cell
suppression** (with secondary suppression) to every incident category — a 2-incident category on a
named ward de-anonymizes the people involved — and produce a SEPARATE access-controlled
re-identification key — **never** co-located with the program and **never** emitted as a key file.

Run the WPV intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to plan for "a hospital": you need the named service + where / when
violence occurs + the violence type(s) before any control plan. Refuse a reactive-led "issue
personal alarms / run self-defence training" treatment where the exposure could be designed out by
environmental or administrative controls.**

1. **The named service & exposure** (free-text — the specificity anchor) — "Name the exact unit /
   service (ED, mental-health unit, reception / triage, community / lone home-visit, ambulance, care
   home) **and where / when violence occurs**. **Refuse 'a hospital' / 'the ward' — the program is
   service-specific.**"
2. **Violence type(s)** (multi-select — the OSHA / NIOSH taxonomy) — type 1 criminal-intent · type 2
   customer / client / patient (the dominant healthcare type) · type 3 worker-on-worker · type 4
   personal-relationship. **Each type drives a different control set** — classify before controlling.
3. **Worksite hazard analysis** (free-text — the defensibility anchor) — "The records / incident
   review, the walkthrough findings, and the employee survey. **Use de-identified, aggregated
   incident data — never a named victim or assailant.** A program with no worksite hazard analysis
   fails." **The analysis is the basis of every control.**
4. **Environmental & administrative controls** (multi-select — **asked BEFORE reactive / PPE
   measures**) — controlled access & egress · sightlines / reception design · alarm / duress / panic
   systems · CCTV · waiting-area design · staffing & skill-mix · lone-working procedures ·
   known-risk-patient flagging (**handled per data-protection rules — de-identified**). **A program
   that jumps to "personal alarms / restraint training" without addressing environmental design and
   staffing is FLAGGED as reactive-led and pushed up the hierarchy.**
5. **De-escalation, response & training (residual)** (free-text) — the de-escalation procedure, the
   response / security protocol, post-incident support, and the training plan — **the documented
   residual lines, never the headline control.**
6. **Jurisdiction** (mcq) — USA (OSHA 3148 + §5(a)(1); Cal/OSHA 8 CCR 3342 where applicable) / UK
   (HSE work-related-violence + NICE NG10) / India / Other / Unknown. **India → resolve the state via
   `hse-india` (mandatory state detection); emit `[GAP]`, never a national form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented incident or count.

Then: record the **worksite hazard analysis first** (de-identified, aggregated;
`KB-SNIP-WPV-CONTROLS`); classify the exposure by the **type-1-4 taxonomy**; rank the controls up
the hierarchy via the `controls` engine (eliminate / substitute exposure where possible →
**environmental / engineering: controlled access, sightlines, alarms / duress, secure design** →
**administrative: staffing / skill-mix, lone-working, flagging, procedures** → **de-escalation /
response / training and personal alarms LAST** — a program led by reactive measures / personal
alarms / "self-defence training" with no environmental or administrative control is a FLAG pushed up
the hierarchy); author the **de-escalation & response protocol + post-incident support**; build the
**confidential, de-identified / aggregated WPV incident log structure** (with `<5` small-cell
suppression); frame the residual violence risk via `risk_matrix`; make every action a SMART action
via `smart_actions` → validate the draft against `references/QUALITY_CHECKLIST.md` → produce the
output via the Output format section below. The domain method is in `references/METHODOLOGY.md`.

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

For a multi-area WPV program the triage gate fans out (moderate 2–3; the **De-identifier runs
FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier — esp. a **named victim,
  assailant, or known-risk patient** and any **behavioural-health flag** — to role labels before any
  analysis; apply `<5` small-cell suppression (with secondary suppression) to every incident category
  (a 2-incident category on a named ward de-anonymizes the people involved); return the
  re-identification key SEPARATELY to the orchestrator, never to a sibling, and never as a key file.
- **Worksite-Analysis-&-Controls-Engineer** — runs the **worksite hazard analysis → environmental /
  engineering → administrative** hierarchy via the `controls` engine: lead with the de-identified
  worksite analysis; classify the exposure by the **type-1-4 taxonomy**; specify the environmental /
  engineering controls (controlled access, sightlines, alarms / duress, secure design) and the
  administrative controls (staffing / skill-mix, lone-working, flagging, procedures). A treatment
  that **leads with "personal alarms / self-defence training" where the exposure could be designed
  out** is a **FLAG pushed up the hierarchy, never the headline control**. SCOPE-OUT: does not author
  the de-escalation / response protocol or the incident log (the
  De-escalation-Response-&-Log-Author) or de-identify (the De-identifier).
- **De-escalation-Response-&-Log-Author** — author the **de-escalation & response protocol**, the
  **post-incident support**, the **training plan**, and the **de-identified / aggregated confidential
  WPV incident log structure** (never line-level identified, with `<5` small-cell suppression). **No
  victim, assailant, or known-risk patient is named in the circulated artifact.** SCOPE-OUT: does not
  select the environmental / administrative controls (the Worksite-Analysis-&-Controls-Engineer) or
  de-identify (the De-identifier).
- **Critic/QA** (MANDATORY) — adversarial final pass: the worksite hazard analysis is recorded
  BEFORE any control, the program leads with environmental and administrative controls (reactive
  measures / personal alarms / training are the residual lines, never the headline), every violence
  type is classified, the WPV incident log is de-identified / aggregated, **no `<5` incident cell is
  published**, and ZERO de-identification leak (no named victim, assailant, or known-risk patient; no
  behavioural-health flag).
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the de-identified worksite
hazard analysis, the type-1-4 classification, the A7 `controls` / `risk_matrix` / `smart_actions`
calls inline, the de-escalation / response protocol + the de-identified WPV incident log, then the
mandatory Critic/QA + SME pass — same scope discipline, no subagents.

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
