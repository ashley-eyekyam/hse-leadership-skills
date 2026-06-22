---
name: construction-phase-plan
description: Produces a consultant-grade, risk-proportionate CDM 2015 Construction
  Phase Plan (CPP) for a named construction project. Use this skill whenever a user
  asks to build, write, or review a Construction Phase Plan, a CPP, a CDM 2015 Regulation
  12 plan, or the principal contractor's pre-start plan. Forces project specificity
  (refuses 'a building site' — needs the named project, at least one significant activity,
  and the contractor configuration), sets out management & arrangements, site rules,
  and significant risks & controls by activity ranked by the hierarchy of controls
  (work at height leads with collective protection, never PPE), states the F10 / Reg
  12 notification duty for a notifiable project, and cross-references the wider CDM
  document chain (Pre-Construction Information and the Health & Safety File). Grounded
  in CDM 2015 Reg 12 + HSE L153 in the UK, or 29 CFR 1926 Subpart C in the USA; India
  BOCW defers to hse-india with state detection. Decision-support only; a competent
  person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - Con
  jurisdiction:
  - All
  status: stable
  plugin: hse-construction
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Construction Phase Plan (CDM 2015 Reg 12)

A consultant-grade HSE skill that produces a **risk-proportionate Construction Phase Plan
(CPP)** under **CDM 2015 Regulation 12(1)–(2)** for a **named construction project**. It
forces the single lever that separates a defensible plan from boilerplate paperwork: a CPP
built from the project's **real significant activities** with controls ranked by the full
**hierarchy of controls** — for **work at height, collective protection leads** (edge
protection, MEWP, nets), never PPE (a harness) as the headline control. It **refuses a
generic "a building site"** (it needs a named project + ≥1 significant activity + the
contractor configuration), states the **F10 / Reg 12 notification duty** for a notifiable
project, and cross-references the wider **CDM document chain** — the Pre-Construction
Information (Reg 4) it consumes and the Health & Safety File (Reg 12(5)) it feeds — **without
assuming a sibling skill ran**. Risk scoring, control ranking, and residual re-scoring are
**deterministic** (the A7 `risk_matrix` / `controls` engines).

## When to use this skill

Use this skill when the user needs a **Construction Phase Plan, a CPP, a CDM 2015 Regulation
12 plan, or the principal contractor's pre-start health & safety plan** for a **named
construction project** — for example "draw up the CPP for the Tower B fit-out: demolition of
the level-3 partitions, then steel-frame erection and cladding to levels 3–5, principal
contractor, notifiable", or "review this contractor's construction phase plan". Trigger
phrases: *construction phase plan, CPP, CDM 2015, Regulation 12, principal contractor's plan,
pre-start H&S plan, F10 notification, significant risks by activity, work at height,
notifiable project*. The load-bearing inputs are the **named project**, **≥1 significant
activity**, and the **contractor configuration**; if any is vague, the Workflow intake below
**refuses to proceed** until they are elicited. This skill owns the **CPP**; a request for
the Pre-Construction Information or the Health & Safety File is routed to its CDM-chain
sibling.

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
| UK    | ../../knowledge-base/regulatory/cdm-2015.md (KB-REG-CDM2015) — **CDM 2015 Reg 12(1)–(2)** (the principal/sole contractor's duty to draw up the Construction Phase Plan **before** the construction phase begins) + **Reg 12(3)–(4)** (review/update) + **Schedule 3** significant-risk activities, read with HSE **L153** ACOP; a **notifiable** project's plan must state the **F10 / Reg 12** duty |
| USA   | ../../knowledge-base/regulatory/osha-1926.md (KB-REG-OSHA1926) — **OSHA 29 CFR 1926 Subpart C** (accident-prevention responsibilities / site-specific safety programme) as the US-jurisdiction CPP-equivalent grounding |
| India | ../../knowledge-base/regulatory/in-factories-act.md — **defers to `hse-india` / `bocw-compliance`, mandatory state detection** (+ in-state-forms.md for the user's state); emit a literal `[GAP]` where a BOCW state form/return is owed — **never a minted national form number** |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (Directive 92/57/EEC temporary/mobile construction sites — the CPP analogue) |
| Unknown | Ask before citing any specific law |
| CPP content skeleton (every run) | ../../knowledge-base/prompt-snippets/cpp-structure.md (KB-SNIP-CPP-STRUCTURE) — the **proportionate** Reg 12(1)–(2) content skeleton (project description & programme · management & arrangements · site rules · **significant risks & controls by activity, hierarchy-ranked** · notification status · review schedule); work at height **leads with collective protection**, never PPE as the headline |
| CDM document chain (every run) | ../../knowledge-base/prompt-snippets/construction-clause-map.md (KB-SNIP-CONSTRUCTION-CLAUSE-MAP) — the **Reg 4 → 12 → 12(5)** duty → artifact → skill cross-walk (PCI / CPP / H&S File); the source for the **one-line cross-reference** to the Pre-Construction Information it consumes and the Health & Safety File it feeds — **no runtime assumption that a sibling skill ran** |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 hazard ID + 8.1.2 hierarchy of
controls) and applies `KB-SNIP-HOC` to every control — **work at height leads with
collective protection (edge protection, MEWP, nets); an "operatives to wear harnesses"
control with no collective protection is flagged PPE-led and pushed up the hierarchy**.
It builds the CPP from the **proportionate** `KB-SNIP-CPP-STRUCTURE` skeleton against the
*named* project's real significant activities (it **refuses a generic "a building site"**),
grounds the duties on `KB-REG-CDM2015` (Reg 12 + L153; a notifiable project must state the
**F10** position; a **sole contractor still owns the CPP under Reg 12(2)**) or
`KB-REG-OSHA1926` for the US. The **Pre-Construction Information (PCI, Reg 4)** is an
**optional input** — pulled in if supplied, otherwise the Reg 4 gap is flagged `[GAP]` and
the plan proceeds on stated assumptions; the output carries a **one-line cross-reference**
to the PCI and the **Health & Safety File (Reg 12(5))** and their place in the
**Reg 4 → 12 → 12(5)** chain, sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP` — **the CDM
trilogy stays loosely coupled; this skill never assumes CON-02 (PCI) or CON-03 (H&S File)
ran**. For an **India** site, resolve the state via `hse-india` (**mandatory state
detection**) and emit a literal `[GAP]` where a BOCW state form/return is owed — never a
minted national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table,
the **mandatory India → state branch**, and the refuse-on-vague anchors — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo
the captured facts back before any analysis**, and **refuse to proceed** until the **GATE**
is satisfied: a **named project** (Q1) **+ ≥1 significant activity** (Q4) **+ the contractor
configuration** (Q2). The load-bearing questions:

- **Q1 — The named project (free-text).** "Which project — name it, its scope, and its
  programme/duration?" This also **disambiguates which CDM document the user needs** (this
  skill owns the **Construction Phase Plan**; a request for the Pre-Construction Information
  or the Health & Safety File is routed to its sibling via the CDM chain). **Refuse "a
  building site"** — force the named project. *(specificity anchor)*
- **Q2 — Contractor configuration (MCQ).** Principal contractor (multi-contractor) /
  **sole contractor** / sub-contractor / not yet appointed. **A sole contractor still owns
  the CPP under Reg 12(2)** — this never excuses the duty.
- **Q3 — Notifiability (MCQ).** ≤30 working days **with** >20 workers simultaneously, **or**
  >500 person-days → **notifiable: the plan must state the F10 / Reg 12 notification duty**;
  otherwise non-notifiable (the CPP is still required).
- **Q4 — Significant / high-risk activities (multi-select, Schedule 3).** Work at height ·
  excavation / ground works · demolition · lifting operations · confined spaces · work near
  water / services · hot works · other. **≥1 required for the GATE** — these drive the
  "significant risks & controls by activity" section.
- **Q5 — Pre-Construction Information available? (MCQ).** Yes (paste / reference it — it is
  **pulled in** to inform the plan) / **No (→ the Reg 4 gap is flagged `[GAP]` and the plan
  proceeds on stated assumptions)**. **PCI is an OPTIONAL input — the CPP never assumes a
  sibling produced it** (D-06 loose coupling).
- **Q6 — Jurisdiction (MCQ).** UK → CDM 2015 (Reg 12 + L153) / USA → 29 CFR 1926 Subpart C /
  **India → mandatory state detection, defers to `hse-india` / `bocw-compliance`, literal
  `[GAP]` (never a minted national form number)** / EU / Unknown (ask before citing).

After the GATE is satisfied, the output carries a **one-line cross-reference** to the PCI
(Reg 4) it consumes and the **Health & Safety File (Reg 12(5))** it feeds, and their place in
the **Reg 4 → 12 → 12(5)** chain — sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **without
assuming a sibling skill ran**.

### The CPP method

Full method in `references/METHODOLOGY.md`; the proportionate content skeleton is
`KB-SNIP-CPP-STRUCTURE`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Any operative named in a prior incident /
   near-miss in the inputs is scrubbed to a **role label**; everything downstream consumes
   the scrubbed text. *(The CPP later carries the **duty-holders the user deliberately
   supplies** — the principal contractor, the CDM construction manager — as a legitimate
   record; those are duty-holder assignments, not PII leaked from incident-style inputs.)*
2. **Build the proportionate CPP** — scaled to the project's risk (a small single-contractor
   refurb's plan is short; a multi-contractor new-build's is fuller), per
   `KB-SNIP-CPP-STRUCTURE`: project description & programme · management & arrangements
   (duty-holders, induction, supervision, emergency, welfare) · site rules · **significant
   risks & controls by activity** · notification status (F10) · review schedule.
3. **Significant risks & controls by activity (the hierarchy-of-controls lever)** — for each
   significant activity from Q4, score the risk via `risk_matrix`, then propose controls and
   **apply `KB-SNIP-HOC`** via `controls.rank_controls` + `controls.validate_treatment`.
   **For work at height, collective protection (edge protection, MEWP, nets, elimination of
   the at-height task) LEADS** — if `ppe_admin_only` is `True` (e.g. "operatives to wear
   harnesses" with no collective protection), the Workflow **must** add a higher-order
   collective control **or** record an explicit justification; a PPE-led WAH control as the
   headline is a **defect the Critic/QA pass must catch**. Re-score residual.
4. **Notification status** — state the F10 / Reg 12 position from Q3; a **notifiable project
   that omits the F10 / Reg 12 duty is a citation defect**. A sole contractor still owns the
   CPP (Reg 12(2)).
5. **CDM-chain cross-reference + assumptions / `[GAP]`** — emit the one-line PCI → CPP → H&S
   File cross-reference (from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`); where the PCI was absent
   (Q5 = No) record the Reg 4 gap as `[GAP]` and list the assumptions the plan proceeds on —
   never invent the missing input.
6. **SMART actions (named owners + dates)** — for every control that is an action, produce a
   SMART action via `smart_actions.validate_register`; any action missing an owner, a valid
   ISO date, a measure, or a hazard link is invalid.
7. **Validate against `references/QUALITY_CHECKLIST.md`**, then assemble the branded CPP
   report (`assets/construction-phase-plan.report.json`) via the Output format section below.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. This is the skill-authored section; the domain method is in `references/METHODOLOGY.md`.

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

This is a **moderate fan-out** roster. The **De-identifier is the sequential first gate**
(not a fan-out peer); the fan-out jobs build the CPP by activity and by arrangement; the
**A7 scoring/ranking calls (`risk_matrix`, `controls`, `smart_actions`) are deterministic
script calls — there is no "Risk-Scorer" subagent**; **Critic/QA and the SME Review are
mandatory**. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all PII
  (any operative named in a prior incident / near-miss in the inputs) to role labels before
  any analysis — every fan-out job below consumes scrubbed text. The **duty-holders the user
  supplies for the CPP record (principal contractor, CDM construction manager) stay named** —
  they are duty-holder assignments, not leaked PII.
- **Activity-Risk-Analyst** — for each significant activity from Q4, build the
  **significant-risks-&-controls-by-activity** rows: score the risk (A7 `risk_matrix`), rank
  controls by `KB-SNIP-HOC` (A7 `controls`), re-score residual. **For work at height,
  collective protection LEADS** — flag any PPE-led WAH control (harnesses with no collective
  protection) and push it up the hierarchy. SCOPE-OUT: the management/arrangements/site-rules
  narrative (Arrangements-&-Rules-Author), the duty-holder map (Duty-holder-Mapper).
- **Arrangements-&-Rules-Author** — author the **management & arrangements**, **site rules**,
  **welfare**, **emergency arrangements**, and the **notification status (F10 / Reg 12)** and
  **review schedule** sections from `KB-SNIP-CPP-STRUCTURE`, scaled to the project's risk;
  emit the **one-line CDM-chain cross-reference** (PCI → CPP → H&S File, Reg 4 → 12 → 12(5))
  from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP` and the **assumptions / `[GAP]`** where the PCI was
  absent. SCOPE-OUT: the per-activity risk rows (Activity-Risk-Analyst), the law citation
  (resolved inline from `KB-REG-CDM2015` / `KB-REG-OSHA1926` / `hse-india` for India).
- **Duty-holder-Mapper** *(optional)* — when the project is multi-contractor, map the
  duty-holders and their CDM responsibilities (Reg 12/13) to the management section using the
  **user-supplied** names (no invented appointments; `[GAP]` where unstated). Merges into the
  Arrangements-&-Rules-Author for a small single-contractor refurb.
- **Critic/QA** (MANDATORY) — adversarial final pass: the project is named (no generic "a
  building site"), every significant activity has a hierarchy-ranked control with a named
  owner, **no PPE-led work-at-height control without justification (collective above
  personal)**, the **F10 / Reg 12 notification duty is stated for a notifiable project**, the
  CDM-chain cross-reference is present without assuming a sibling ran, every action is owned +
  dated + hazard-linked, every citation traces to the KB, and **zero input-derived PII
  leaked**. PASS/FAIL.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME persona
  sign-off per `references/sme-review.md` (the Principal Contractor / CDM Construction Manager
  lens); decision-support that precedes — never replaces — the human competent-person review.
  **It never emits "approved by a competent person"** (the CPP is statutory-adjacent).

**Single-threaded fallback** — for a small single-contractor refurbishment the triage gate
stays single-threaded (no subagents), but the **De-identifier still runs FIRST**, the **A7
`risk_matrix` / `controls` / `smart_actions` calls are still made**, and the **Critic/QA +
SME Review passes are still performed** in this context before any output.

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
