---
name: warehouse-racking-mhe-safety
description: 'Produces a consultant-grade warehouse racking + MHE/pedestrian-segregation
  safety artifact for a named warehouse, racking installation, and traffic layout
  — never a generic ''inspect carefully'' or ''wear hi-vis''. Use this skill to assess
  pallet racking, build a racking inspection regime, classify rack damage on the SEMA
  Red/Amber/Green bands, plan MHE/forklift and pedestrian segregation, or check a
  warehouse against BS EN 15635 / SEMA / OSHA 1910.178 / PUWER / HSE L117. It is design-
  and engineering-control-led: racking is controlled by SWL-rated configuration, column
  protection and the EN 15635 inspection regime (PRRS, weekly visual, >=12-monthly
  expert), and MHE/pedestrian conflict by ENGINEERED segregation (barriers, one-way
  systems, marked walkways) before hi-vis. It gets the SEMA RAG priority right (Green=monitor;
  Amber=repair in 4 weeks + escalate; Red=immediate off-load + isolate), refuses a
  vague ''a warehouse'', never assumes an SWL ([GAP]). Decision-support only; a competent
  person must review.'
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
  - Gen
  jurisdiction:
  - UK
  - US
  - IN
  status: stable
  plugin: hse-logistics-transport
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Warehouse Racking & MHE Safety

A consultant-grade, **design- and engineering-control-led** warehouse racking + MHE/pedestrian-
segregation safety assessment for a **named warehouse, racking installation, and traffic layout** —
never a generic "inspect carefully" or "wear hi-vis" statement. Its entire reason to exist is that
**racking and traffic risk are controlled by design and engineering first**: racking by the
**SWL-rated configuration**, **column/upright protection**, and the **BS EN 15635 inspection regime**
(a named **PRRS**, the **weekly visual** inspection and the **≥12-monthly expert** inspection); and
MHE/pedestrian conflict by **engineered segregation** (physical barriers, one-way systems, marked and
protected walkways and crossings) — **before** any reliance on hi-vis, signage, or "look out for
forklifts." A treatment that leads with "inspect carefully" / hi-vis, with no SWL design, no
inspection regime, and no engineered segregation, is **flagged and pushed up the hierarchy — never
accepted as the headline control** (`KB-SNIP-RACKING-MHE`). That is the failure mode this skill exists
to prevent.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**site/installation specificity plus the full hierarchy of controls**. It applies the **SEMA RAG
remedial priority** to every damage finding and gets the escalation right — **Green** = log + monitor;
**Amber** = repair/replace within 4 weeks **and auto-escalate to Red** if not actioned; **Red** =
**immediate off-load + isolate** the affected run (a Red finding down-rated to "monitor" is rejected).
It **refuses** to assess "a warehouse" or "looks fine" without a **named site + the racking
configuration + the traffic layout**, and **never assumes a site-specific SWL, tolerance, or
inspection interval** — an unsupplied value is a literal `[GAP]`, never an invented rating. Grounded in
**BS EN 15635:2008 / SEMA Code of Practice**, **OSHA 29 CFR 1910.178**, **PUWER 1998**, and **HSE ACOP
L117 / HSG136**. Decision-support only; a competent person must review the output.

## When to use this skill

Use this skill when the user needs a **warehouse racking + MHE/traffic safety assessment for a
concrete site, racking installation, and traffic layout** — for example "assess the pallet racking and
forklift routes in the Coventry DC", "build a racking inspection regime and PRRS appointment for the
chilled warehouse", "classify the damage on bays A12–A18 against the SEMA RAG bands", or "plan
MHE/pedestrian segregation for the goods-in marshalling area". It is **not** for a generic "how do I
keep a warehouse safe?" answer: the Workflow intake below forces the named site, the racking
configuration, and the traffic layout before any drafting, and refuses a vague "a warehouse" / "looks
fine" request.

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
| USA | ../../knowledge-base/regulatory/mhe-pit.md (KB-REG-MHE-PIT) — **OSHA 29 CFR 1910.178** powered industrial trucks: operator training/evaluation (1910.178(l)), pre-use inspection + defect removal-from-service, and **HSG136/ANSI MH16.1-style engineered pedestrian-vehicle segregation BEFORE "look out for forklifts"** |
| UK / EU | ../../knowledge-base/regulatory/mhe-pit.md (KB-REG-MHE-PIT) — **PUWER 1998 + HSE ACOP L117 + HSG136**: lift-truck suitability/maintenance/thorough examination + **engineered segregation by design** (barriers, one-way routes, marked/protected walkways), read with the EN 15635 racking standard |
| India | ../../knowledge-base/regulatory/in-mtw.md (KB-REG-IN-MTW) — **Motor Transport Workers Act 1961 + Factories-Act-as-warehouse + flagged OSH Code 2020 transition**; **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |
| Racking inspection regime + RAG (every run) | ../../knowledge-base/standards/en15635-sema.md (KB-STD-EN15635-SEMA) — **BS EN 15635:2008 + SEMA Code of Practice**: the **PRRS** appointment, the **weekly visual + ≥12-monthly expert** inspection cadence, the **SWL load-notice** duty, and the **SEMA Red/Amber/Green damage-action map** (Green=monitor / Amber=4-week repair+auto-escalate / **Red=immediate off-load+isolate**); the off-load nuance for Amber is confirmed by the SEMA-approved inspector. Site SWL/tolerance/interval = `[GAP]` |
| Racking/MHE control order (every run) | ../../knowledge-base/prompt-snippets/racking-mhe.md (KB-SNIP-RACKING-MHE) — the **SWL-design + inspection-regime + engineered-segregation-first control spine**: "inspect carefully" / hi-vis / "look out for forklifts" as a headline control is **rejected** and pushed up the hierarchy; a Red finding without an immediate off-load is rejected; an assumed SWL/tolerance/interval is rejected → `[GAP]` |
| Logistics clause cross-walk | ../../knowledge-base/prompt-snippets/logistics-clause-map.md (KB-SNIP-LOGISTICS-CLAUSE-MAP) — the bundle-shared standard→artifact→skill cross-walk (EN 15635/SEMA + OSHA 1910.178/PUWER → LOG-02); single source, never duplicated |

This skill always grounds racking in `KB-STD-EN15635-SEMA` (the inspection regime + SEMA RAG action
map) and MHE/traffic in `KB-REG-MHE-PIT` (operator competence + **engineered segregation by design**),
drives every control through the **SWL-design + inspection + engineered-segregation-first** spine in
`KB-SNIP-RACKING-MHE` (a hi-vis/"inspect carefully"-led treatment is a FLAG pushed up the hierarchy),
applies the `KB-SNIP-HOC` hierarchy to every recommendation, and locates itself in the bundle via
`KB-SNIP-LOGISTICS-CLAUSE-MAP`. For an India site, resolve the state via `hse-india` (**mandatory state
detection**, `KB-REG-IN-MTW`) and emit a literal `[GAP]` where a state form/return is owed — never a
minted national form number (CONV-8). A site-specific SWL, tolerance, or inspection interval is **never
assumed**; an unsupplied value is a literal `[GAP]`. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the racking + traffic walk one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "a warehouse" or "looks fine": you need the named site +
the racking configuration + the traffic layout before any drafting.** A missing SWL / tolerance /
inspection interval / bay configuration is a `[GAP]`, never an invented rating.

1. **The named warehouse / installation** (free-text — the specificity anchor) — "Name the exact site
   + the racking installation + what it stores (e.g. 'Coventry DC, 8 m APR pallet racking, chilled
   ambient, bays A1–A48'). **Refuse 'a warehouse' / 'the DC' — the assessment is site- and
   installation-specific.**"
2. **Racking configuration & SWL** (free-text — the integrity-of-advice gate) — "The rack type
   (APR / drive-in / cantilever / mobile), the bay/beam configuration, and the **displayed SWL load
   notices**. **A site-specific SWL, tolerance, or bay configuration is NEVER assumed — if not
   supplied, record a literal `[GAP]` and request the SWL load notice / rack-design drawing; never
   invent an SWL rating.**"
3. **Inspection regime & PRRS** (mcq+free-text) — "Is a **PRRS** (Person Responsible for Racking
   Safety) named? What is the inspection cadence (weekly visual / ≥12-monthly expert)?" — resolves the
   EN 15635 regime; an unappointed PRRS or an absent expert inspection is a high-priority finding.
4. **Damage findings & SEMA RAG band** (free-text) — "What rack damage is present, and its SEMA
   RAG classification (Green / Amber / Red)? **A Red-band damage finding triggers an IMMEDIATE
   off-load + isolate action — it is never down-rated to 'monitor'; Amber repairs within 4 weeks and
   auto-escalates to Red.** Any damage at an unstated tolerance is a `[GAP]`."
5. **MHE & pedestrian traffic layout** (mcq+free-text) — "The MHE inventory (forklift / reach /
   VNA / PPT) and the **traffic layout**: are vehicles and pedestrians **engineered apart** by
   barriers, one-way systems, and marked/protected walkways and crossings? **A treatment that treats
   MHE/pedestrian conflict with hi-vis / signage / 'look out for forklifts' alone — with no engineered
   segregation — is a FLAG pushed up the hierarchy, never the headline control.**"
6. **Jurisdiction** (mcq) — UK / USA / EU / India / Other / Unknown. **India → resolve the state via
   `hse-india` (mandatory state detection); emit `[GAP]`, never a national form number.**
7. **Action owner(s) + verifier** (free-text) — "Who owns the SWL-correction / inspection-regime /
   segregation / `[GAP]`-closure actions, and who is the competent person reviewing the assessment
   (named role — no 'TBD')?"
8. **Review cycle / next review** (mcq+free-text) — on-damage-report / on-reconfiguration / quarterly
   (or sooner for high-traffic / 24-7 sites) / other (+date).

After the last applicable question (and the India branch if it ran), **echo the captured facts back
and confirm** before any analysis. Never proceed on a vague or missing input — a missing input is a
`[GAP]`, never an invented SWL or guard.

Then: rank every racking/MHE control through the **SWL-design + inspection-regime + engineered-
segregation-first** order (`KB-SNIP-RACKING-MHE`, the `controls` engine — a hi-vis/"inspect carefully"-
led mechanical-zone control is a FLAG pushed up the hierarchy), apply the **SEMA RAG remedial action**
to every damage finding (Red = immediate off-load + isolate), re-score the residual via `risk_matrix`,
assign owned/dated `[GAP]`-closure actions via `smart_actions` → validate the draft against
`references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain
method is in `references/METHODOLOGY.md`.

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

For a multi-bay racking + traffic survey the triage gate fans out to (the **De-identifier runs
FIRST — sequential dependency**; everything below consumes only its scrubbed output). This is a
**lower de-id tier** skill — asset/installation/site data dominates — but any **prior struck-by /
collapse-injury context** is special-category health data and is de-identified before analysis:

- **De-identifier** — runs FIRST. This skill's inputs are mostly asset/installation data (bay configs,
  SWL ratings, damage findings) — but scrub any **named worker from a prior struck-by / rack-collapse
  incident** (the injured party, the injury, the body part, the medical outcome, exact date/location)
  to **role labels** before any analysis; suppress any `<5` injury cell; return the re-identification
  key SEPARATELY to the orchestrator, never to a sibling.
- **Racking-Inspection-Analyst** — resolve the **PRRS** appointment and the **EN 15635 inspection
  regime** (weekly visual + ≥12-monthly expert), record the displayed **SWL** load notices, and
  classify every damage finding on the **SEMA RAG band** — applying the matching action (Green=monitor
  / Amber=4-week repair+auto-escalate / **Red=immediate off-load+isolate**). A site-specific SWL,
  tolerance, or interval that is unstated is a `[GAP]`, never assumed. SCOPE-OUT: does not select the
  MHE/traffic controls (the Traffic-Segregation-Engineer owns it) or check the law (the SME persona).
- **Traffic-Segregation-Engineer** — drive `KB-REG-MHE-PIT` + `KB-SNIP-RACKING-MHE`: pedestrian-vehicle
  separation is achieved **by engineered design first** (physical barriers, segregated/one-way routes,
  marked and protected walkways and crossings) **before** hi-vis or signage; run the **`controls`
  engine** — an MHE/pedestrian control left as hi-vis/"look out for forklifts" only (`ppe_admin_only`)
  is a **FLAG pushed up the hierarchy, never the headline control**. Re-score the residual via
  `risk_matrix`. SCOPE-OUT: does not de-identify (De-identifier) or rank the racking damage (the
  Racking-Inspection-Analyst).
- **Critic/QA** (MANDATORY) — adversarial final pass: every racking control is SWL-design /
  inspection-regime led and every MHE/pedestrian control is engineered-segregation led (no
  hi-vis/"inspect carefully" headline control accepted), every SEMA Red finding carries an immediate
  off-load action, no SWL/tolerance/interval assumed (every unsupplied value is a `[GAP]`), every
  citation resolves (EN 15635 / SEMA / 1910.178 / PUWER / L117), and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME persona sign-off per
  `references/sme-review.md` (the **SEMA-approved racking inspector** — to confirm the A5 Amber
  off-load nuance); decision-support that precedes — never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the A7 `controls` /
`risk_matrix` / `smart_actions` calls and the per-bay SEMA RAG classification + engineered-segregation
selection inline, then the mandatory Critic/QA + SME pass — same scope discipline, no subagents.

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
