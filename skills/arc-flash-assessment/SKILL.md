---
name: arc-flash-assessment
description: 'Produces a consultant-grade arc-flash risk assessment for named
  electrical equipment, driven by the de-energize-first hierarchy. Use this skill
  whenever a user asks to perform an arc-flash assessment or hazard analysis, run an
  incident-energy study, calculate the arc-flash boundary, determine the PPE
  category, or produce arc-flash labels for electrical equipment. It computes
  incident energy and the boundary with the IEEE 1584-2018 method (the cal/cm² value
  is COMPUTED, never narrated), records whether the task can be
  done de-energized first (an electrically safe work condition per NFPA 70E Article
  120), justifies any energized work against OSHA 1910.333(a)(2) or EAWR reg 14
  (convenience is refused), ranks controls up the hierarchy (de-energize first,
  arc-rated PPE last), and emits a branded report with NFPA 70E 130.5(H) label
  content. It refuses a PPE-led treatment with no de-energization decision. Grounded
  in NFPA 70E (2024) and IEEE 1584-2018. Decision-support only; a competent person
  must review.'
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
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-utilities-power
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Arc-Flash Assessment

A consultant-grade, **de-energize-first** arc-flash risk assessment for **named electrical
equipment** — a panel, switchgear, MCC, transformer secondary, or distribution board — never a
generic "a panel". Its entire reason to exist is that **electrical safety leads with
de-energization**: every assessment first records whether the task can be done **de-energized**
(establishing an **electrically safe work condition** per NFPA 70E **Article 120**); only if dead
working is genuinely not reasonable is energized work **justified explicitly** (OSHA
**1910.333(a)(2)** infeasibility/added-hazard test, or EAWR **reg 14**). A bare "production can't
stop / it's quicker" is **refused** — economic convenience alone never justifies energized work.
**Arc-rated PPE is the documented last line, never the headline control.**

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**the de-energization decision plus the full hierarchy of controls, with a number that is
COMPUTED not narrated**. The incident energy (cal/cm²), the arc-flash boundary (the distance to
**1.2 cal/cm²**), and the **NFPA 70E PPE category** are produced by the **deterministic IEEE
1584-2018 engine** (`scripts/hse_components/arcflash.py`, consumed via `scripts/_shim.py`) — the
skill **never** asserts a cal/cm² value, a boundary, or a category from assumption, and **never
invents a fault current or a clearing time** (a missing required input is a `[GAP]`, never a
fabricated parameter). Grounded in **NFPA 70E (2024) 130.5** (arc-flash risk assessment),
**130.5(G)** (incident-energy method), **130.5(H)** (label content), **130.4** (shock risk
assessment + approach boundaries), **130.7(C)(15)** (the PPE-category table alternative), and
**IEEE 1584-2018** (208 V – 15 kV). Decision-support only; a competent person (qualified
electrical engineer) must review the output.

## When to use this skill

Use this skill when the user needs an **arc-flash assessment for concrete electrical equipment** —
for example "perform an arc-flash assessment on main switchboard MSB-1", "calculate the incident
energy and arc-flash boundary for the 13.8 kV switchgear", "determine the PPE category for the MCC
feeders", or "produce NFPA 70E arc-flash labels for the distribution board". It is **not** for a
generic "how do I do arc flash?" answer: the Workflow intake below forces the named equipment, the
de-energization decision, and the IEEE 1584 required inputs before any computation, refuses a vague
"a panel" request, and refuses a PPE-led "issue a CAT 2 suit" with no recorded de-energization
decision.

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
| Electrical control spine (every run) | ../../knowledge-base/prompt-snippets/deenergize-first.md (KB-SNIP-DEENERGIZE-FIRST) — the **de-energize-first / ESWC / energized-work-justification** spine: establish an electrically safe work condition (NFPA 70E Article 120) BEFORE any reliance on arc-rated PPE; a PPE-led or convenience-led treatment is rejected |
| Arc-flash / electrical duty (every run) | ../../knowledge-base/standards/nfpa-70e.md (KB-STD-NFPA70E) — the copyright-safe NFPA 70E (130.4 / 130.5 / 130.5(G) / 130.5(H) / 130.7(C)(15) / Article 120) + IEEE 1584-2018 clause→artifact + PPE-category structure map (cite the clause/table numbers + the 1.2/4/8/25/40 cal/cm² breakpoint structure only — never the table cells) |
| Utilities clause cross-walk | ../../knowledge-base/prompt-snippets/utilities-clause-map.md (KB-SNIP-UTILITIES-CLAUSE-MAP) — the bundle-shared NFPA 70E Article 120 + 130.4 + 130.5 cross-walk that keeps the three hse-utilities-power skills consistent on de-energize-first |
| USA | ../../knowledge-base/standards/nfpa-70e.md (KB-STD-NFPA70E) — US duty: NFPA 70E (2024) read with **OSHA 29 CFR 1910.333** (de-energize-first / energized-work justification) + **1910.269** (utility T&D approach distances) |
| UK / EU | ../../knowledge-base/standards/nfpa-70e.md (KB-STD-NFPA70E) — read with **UK EAWR 1989 reg 14** (the dead-working default + live-working test) + **HSG85** for the UK leg |
| India | ../../knowledge-base/regulatory/in-electrical.md (KB-REG-IN-ELECTRICAL) — India CEA / state electricity rules; **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and leads every assessment with the
**de-energize-first spine** `KB-SNIP-DEENERGIZE-FIRST` (establish an ESWC per NFPA 70E Article 120
before any PPE reliance), grounds the arc-flash duty + the IEEE 1584-2018 method on
`KB-STD-NFPA70E` (130.5 / 130.5(G) / 130.5(H) / 130.7(C)(15)), and aligns with the other
hse-utilities-power skills through `KB-SNIP-UTILITIES-CLAUSE-MAP`. The **incident energy,
arc-flash boundary, and PPE category are COMPUTED by the deterministic `arcflash.py` engine** (the
IEEE 1584-2018 method), never narrated — `KB-STD-NFPA70E` is the cited structural reference, never
a substitute for the computation. For an India site, resolve the state via `hse-india` (**mandatory
state detection**) and emit a literal `[GAP]` where a state return is owed — never a minted
national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the arc-flash intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "a panel": you need the named equipment + the
de-energization decision + the IEEE 1584 required inputs before any computation. Refuse a PPE-led
"issue a CAT 2 suit" with no recorded de-energization decision.**

1. **The named equipment** (free-text — the specificity anchor) — "Name the exact equipment +
   type (switchgear / MCC / panelboard / transformer secondary / distribution board) +
   manufacturer + function (e.g. 'main switchboard MSB-1, 400 V, building incomer'). **Refuse 'a
   panel' / 'the switchroom' — the assessment is equipment-specific.**"
2. **Can the task be done de-energized?** (mcq — asked FIRST among the controls) — yes →
   **de-energize & establish an ESWC (NFPA 70E Article 120)**: the assessment scopes safe
   isolation + verification, not energized PPE as the headline · no → must justify (branch to Q3).
   **De-energization is the primary control, not an afterthought.**
3. **Energized-work justification** *(only if Q2 = no)* (free-text) — against OSHA **1910.333(a)(2)**
   ("additional/increased hazard or infeasible") **or** EAWR **reg 14** ("unreasonable to be
   dead"). **A bare 'it's quicker / production needs it' is REFUSED** — economic convenience alone
   does not justify energized work. Record the justification verbatim and route to an
   energized-work permit (NFPA 70E Annex J).
4. **Electrical parameters** (free-text — IEEE 1584 method inputs) — nominal system voltage,
   available bolted fault / short-circuit current, upstream protective-device clearing time,
   electrode configuration (VCB / VCBB / HCB / VOA / HOA), enclosure & gap dimensions, working
   distance. **Refuse to compute on a missing required parameter → record a `[GAP]` and request a
   power-system / short-circuit study; never invent a fault current or a clearing time.**
5. **PPE-selection method** (mcq) — incident-energy analysis (130.5(G), via the engine) /
   arc-flash PPE category table (130.7(C)(15)). **The two methods are not mixed on the same
   equipment.**
6. **Jurisdiction** (mcq) — USA / UK / EU / India / Other / Unknown. **India → resolve the state
   via `hse-india` (mandatory state detection); emit `[GAP]`, never a national form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented parameter.

Then: record the **de-energization decision first** (`KB-SNIP-DEENERGIZE-FIRST`); if energized
work is justified, record the verbatim justification + permit trigger; compute the **incident
energy → arc-flash boundary → PPE category** via the **`arcflash.py` engine** (`incident_energy()`
→ `to_report_blocks()`, consumed through `scripts/_shim.py` — never narrated); run the `controls`
hierarchy gate (de-energize → engineer → approach control → arc-rated PPE last — a PPE-led
treatment is a FLAG pushed up the hierarchy) → frame the qualitative residual via `risk_matrix` →
make every action a SMART action via `smart_actions` → validate the draft against
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

For a multi-equipment arc-flash study the triage gate fans out to (the **De-identifier runs
FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier (esp. a **named worker
  from a prior arc-flash burn / electrocution incident**) to role labels before any analysis;
  return the re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **De-energization-&-Justification-Analyst** — runs **before** the energy analysis so the
  assessment is de-energize-led: record the **Article 120 ESWC decision** (`KB-SNIP-DEENERGIZE-FIRST`);
  if the task cannot be done dead, capture the **energized-work justification** against OSHA
  1910.333(a)(2) / EAWR reg 14 (a bare convenience/economic reason is REJECTED) and route to an
  energized-work permit. SCOPE-OUT: does not compute incident energy (the Incident-Energy-Engineer
  owns it) or de-identify (the De-identifier).
- **Incident-Energy-Engineer** — per equipment, capture the IEEE 1584 parameters and run the
  **`arcflash.py` engine** (`incident_energy()` → `to_report_blocks()`, via `scripts/_shim.py`) to
  COMPUTE the incident energy (cal/cm²), the arc-flash boundary, and the PPE category. **A missing
  required parameter is a `[GAP]` (request a short-circuit study) — never an invented fault
  current.** SCOPE-OUT: does not select the controls or write the label (the Controls-&-Label-Author).
- **Controls-&-Label-Author** — rank the controls up the hierarchy (de-energize → engineer →
  approach control → **arc-rated PPE last**) via the **`controls` engine** — an arc-flash treatment
  that **leads with arc-rated PPE when the task could be de-energized** (`ppe_admin_only=True`) is a
  **FLAG pushed up the hierarchy, never the headline control**; author the **NFPA 70E 130.5(H)
  label content**; re-frame the residual via `risk_matrix`. SCOPE-OUT: does not de-identify or
  check the law (the SME persona).
- **Critic/QA** (MANDATORY) — adversarial final pass: the de-energization decision is recorded
  BEFORE any PPE, energized work is justified (never on convenience), every incident-energy value
  traces to its IEEE 1584 inputs (no invented fault current → `[GAP]`), arc-rated PPE is the
  documented last line, `>40 cal/cm²` flags energized work as prohibited, the 130.5(H) label
  content + the 1.2 cal/cm² boundary threshold are correct, and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the de-energization
decision, the `arcflash.py` computation, the A7 `controls` / `risk_matrix` / `smart_actions` calls
inline, then the mandatory Critic/QA + SME pass — same scope discipline, no subagents.

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
