---
name: health-safety-file
description: Produces a CDM 2015 Health and Safety File for a named completed (or
  near-complete) construction project — the as-built residual-risk record handed to
  the client for future construction, maintenance, cleaning, refurbishment, and demolition.
  Use this skill whenever a user asks to compile, write, or review a health and safety
  file, an H&S file, a CDM completion file, or the residual-risk handover information
  for a structure. It captures the as-built information, the residual and unusual
  hazards a future worker could not reasonably anticipate, the location of services
  and hazardous materials, and the cleaning/maintenance safety arrangements — emitting
  a branded report. Grounded in CDM 2015 Regulation 12(5)–(9). Decision-support only;
  a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 2
  audience:
  - M
  - C
  industry:
  - Con
  jurisdiction:
  - All
  status: stable
  plugin: hse-construction
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Health & Safety File — CDM 2015 Reg 12(5)–(9)

A consultant-grade HSE skill that produces a task/site-specific **CDM 2015 Health & Safety
File** for a **named completed (or near-complete) structure** — the **as-built residual-risk
record** the principal designer prepares and maintains and the client retains for future
**construction, maintenance, cleaning, refurbishment, and demolition** (Reg 12(5)–(9)). It
captures the **as-built & services information**, the **residual and unusual hazards (with
locations)** a future worker **could not reasonably anticipate**, the **hazardous materials
left in situ**, and the **maintenance/cleaning/refurb/demolition safety arrangements**,
grounded in the **L153 Appendix-4 H&S-file content list** (`KB-SNIP-HS-FILE-CONTENT`).

Its signature lever is **residual-only discipline**: the file records **only what a future
worker could not reasonably anticipate** from the structure itself — a **full general-spec
dump is flagged**, not a file. Each located residual hazard's future-work control is framed
by the **hierarchy of controls** via the deterministic A7 `controls` engine, and any open
completion item becomes an owned/dated `smart_actions` item. The file is part of the **PCI →
CPP → H&S File** chain (Reg 4 → 12 → 12(5)) — it cross-references its siblings via the single
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **never assuming a sibling skill ran** (the CDM trilogy
stays loosely coupled). The H&S File is a structured residual-risk record, not calculation —
it uses no scoring/matrix engine.

## When to use this skill

Use this skill when the user needs to **compile, write, or review a Health & Safety File, an
H&S file, a CDM completion file, or the residual-risk handover information** for a **named
structure** — for example "compile the CDM Health & Safety File for the Tower B fit-out at
handover", "what residual hazards must the maintenance team be told about for this atrium
roof", or "review this H&S file before it goes to the client". Trigger phrases: *health and
safety file, H&S file, CDM completion file, residual-risk handover, as-built residual
hazards, Reg 12(5), L153 Appendix 4, could-not-reasonably-anticipate*. The load-bearing
inputs are the **named structure + use** and **at least one residual/unusual hazard (or a
stated "none beyond the obvious" justification)**; if either is vague, the Workflow intake
below **refuses to proceed** until they are elicited. The H&S File is the *handover* record
at completion — a request for the Pre-Construction Information (CON-02) or the Construction
Phase Plan (CON-01) is routed to its CDM-chain sibling (Q1 disambiguates which CDM document).

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
| UK    | ../../knowledge-base/regulatory/cdm-2015.md (**CDM 2015 Reg 12(5)** — the principal designer prepares & maintains the H&S file; Reg 12(6)–(9) review, update, **handover to the client at completion**, client retention/availability; the **L153 Appendix-4 H&S-file content list**) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (29 CFR 1926 — as-built / record-retention equivalents) |
| India | ../../knowledge-base/regulatory/in-state-forms.md (BOCW completion records — **defers to `hse-india` / `bocw-compliance`, mandatory state detection; emit a literal `[GAP]`, never a minted national form number**) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill grounds every run in `KB-STD-ISO45001` (6.1.2; 7.5 documented information) and
applies `KB-SNIP-HOC` to every future-work control. It builds the file content heads from
`KB-SNIP-HS-FILE-CONTENT` (the **L153 Appendix-4** content list + the
**"could-not-reasonably-anticipate"** residual-hazard test) and grounds the **Reg 12(5)
principal-designer duty** + the **handover duty (Reg 12(6)–(9))** on `KB-REG-CDM2015` —
**attributing preparation to the wrong duty-holder, or omitting the handover duty, is a
`regulatory_citation_accuracy` hard-fail**. For an **India** site it resolves the state via
`KB-REG-IN-STATEFORMS` (**mandatory state detection**) and **defers the India leg to the
`hse-india` `bocw-compliance` skill** — legacy-first, **never a minted national form
number**; an un-seeded state → `[GAP]`. The one-line **PCI → CPP → H&S File** (Reg 4 → 12 →
12(5)) cross-reference is sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP` **without assuming
the PCI or CPP skill ran** (loose coupling). The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(Q1 **named structure & use** · Q2 **file purpose** — completion handover / updating an
existing file / single-package addition · Q3 **residual & unusual hazards present** · Q4
**as-built information available** — each missing item a `[GAP]` · Q5 **future-work scope**
— maintenance / + refurb / + demolition · Q6 **jurisdiction**), the **UK → CDM 2015 Reg
12(5)** path and the **mandatory India → state branch** (defers to `hse-india` /
`bocw-compliance`, state detection mandatory, literal `[GAP]`, never a minted national form
number), the echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**.
Run it one question at a time, branch on the answers, **echo the captured facts back before
any analysis**, and **refuse to proceed** on a generic structure (Q1).

**The GATE (refuse-on-vague):** no file is produced until **a named structure (Q1)** AND
**at least one residual/unusual hazard (Q3) — or a stated "none beyond the obvious"
justification** — are captured. The file is about **what a future worker could NOT reasonably
anticipate**, not a general-spec dump. **Q2 update mode APPENDS, never overwrites** prior
residual-risk content. **Q1 also disambiguates the CDM document** — this skill owns the H&S
File (the *handover* record at completion); a request for the PCI (CON-02) or the CPP
(CON-01) is routed to its CDM-chain sibling. Full method in `references/METHODOLOGY.md`.

### The H&S-File method (residual-only discipline is the lever)

Full method in `references/METHODOLOGY.md`, grounded in `KB-SNIP-HS-FILE-CONTENT`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). **Commissioning, survey, or as-built records
   routinely name an individual** (a commissioning engineer with an incident/health note, a
   surveyor, an occupier) — scrub these to role labels; a leak there is an **auto-fail**.
   **No worker health detail belongs in the file at all.** Flag **restricted-distribution**
   where the file carries security-sensitive structural/services detail. *(Duty-holders the
   user deliberately names for the record — the principal designer, the client, owners of
   open completion items — stay named; those are duty-holder assignments, not leaked PII.)*
2. **Capture the as-built & services information** — what was built and its use; key as-built
   drawings; the **location of services and isolation points** — each cited to its source,
   `[GAP]` where a record is missing (Q4); never invent an as-built detail.
3. **Identify the residual & unusual hazards — apply the "could-not-reasonably-anticipate"
   test (THE LEVER)** — for each system, include an item **only if a competent future worker
   could not reasonably anticipate it** from the structure itself (fragile roof glazing,
   no permanent edge protection at high-level plant, presumed-asbestos lagging, restricted
   confined-plant egress, buried services on an unusual route). **Each residual hazard is
   LOCATED** (where in the structure). **A routine/anticipatable hazard or a full general-spec
   dump is REJECTED** — that is a specificity/defensibility failure, not a file.
4. **Record the hazardous materials in situ** — asbestos register, coatings, insulation, and
   other materials left in place, **with their locations**; `[GAP]` where a survey is
   outstanding (presumed-present-pending-survey), flagged as a hold-point before disturbance.
5. **Frame each residual hazard's future-work control by the hierarchy** — for the
   maintenance/cleaning/refurb/demolition arrangements, propose controls and **apply
   `KB-SNIP-HOC`** via `controls.rank_controls` + `controls.validate_treatment`: prefer a
   higher-order future-work control (specify permanent edge protection / an anchor system at
   next refurbishment) over a PPE-/admin-only treatment ("wear a harness"); a lower-order-only
   arrangement with no justification is a **defect the Critic/QA pass must catch**.
6. **Build the maintenance/cleaning/refurb/demolition safety arrangements** — for the
   future-work scope captured at Q5, author the safety information a future worker needs for
   each foreseeable activity; demolition arrangements still rank controls via `KB-SNIP-HOC`.
7. **Record the information gaps & revision control** — every unknown is a documented `[GAP]`
   (never silently omitted); any open completion item becomes an owned/dated `smart_actions`
   item via `smart_actions.validate_register` (named owner / role + ISO due date + link).
   The file carries **revision/version control**; **an update (Q2) APPENDS — it never
   overwrites prior residual-risk content**.
8. **Cross-reference the CDM document chain** — add the one-line **PCI → CPP → H&S File**
   (Reg 4 → 12 → 12(5)) cross-reference sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`,
   **without assuming the PCI or CPP skill ran** (loose coupling). State the **principal
   designer's Reg 12(5) preparation duty AND the handover duty (Reg 12(6)–(9))** — attributing
   preparation to the wrong duty-holder, or omitting the handover duty, is a citation hard-fail.
9. **Validate against `references/QUALITY_CHECKLIST.md`** — only residual/unusual hazards a
   future worker could not anticipate (no general-spec dump); every hazard located; hazardous
   materials in situ listed; future-work controls HoC-ranked; the Reg 12(5) duty + handover
   cited; an update appends; de-id applied; no conclusion on an unstated assumption.
10. **Assemble the branded H&S-File report** — build `report.json` (see
    `assets/health-safety-file.report.json`) and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **`controls` HoC-ranking and `smart_actions`
gap-closure calls (steps 5/7) are A7 script calls in every case — never a fan-out job**; the
H&S File uses **no scoring/matrix engine** (it is a residual-risk record, not calculation).

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

This is a **moderate fan-out** roster (A6 "moderate = 2–3") for a large structure: the
**De-identifier is the sequential first gate** (not a fan-out peer), then two fan-out jobs —
**Residual-Hazard-Compiler** and **Maintenance-&-Handover-Author** — with a **mandatory
Critic/QA** and the **CDM Principal Designer** SME pre-output gate. A **small package file
runs single-threaded** — no subagents — but the `controls` HoC-ranking, the `smart_actions`
gap-closure call, and the Critic/QA pass are still made. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all PII /
  health detail to role labels before any analysis — **a commissioning or survey record
  naming an individual with an incident/health note**, surveyors, occupiers, exact
  dates/locations — everything downstream consumes scrubbed text; a leak is an **auto-fail**.
  **No worker health detail belongs in the file at all.** Set the **restricted-distribution
  flag** where the file carries security-sensitive structural/services detail. *(Duty-holders
  the user deliberately names for the record — principal designer, client, open-item owners —
  stay named.)*
- **Residual-Hazard-Compiler** — apply the **"could-not-reasonably-anticipate" test per
  system** from the scrubbed inputs: include a hazard **only if** a competent future worker
  could not reasonably anticipate it from the structure; **LOCATE each one**; record the
  **hazardous materials left in situ** (asbestos register / coatings / insulation) with
  locations. **REJECT a routine/anticipatable hazard or a full general-spec dump** (that is
  the residual-only-discipline FLAG). SCOPE-OUT: the future-work arrangements & handover
  (Maintenance-&-Handover-Author); the law (the SME / Drafter cites Reg 12(5)).
- **Maintenance-&-Handover-Author** — author the **maintenance/cleaning/refurb/demolition
  safety arrangements** for the future-work scope (Q5), framing **each residual hazard's
  future-work control by the hierarchy** via `controls` (a higher-order future-work control
  before PPE/admin-only); build the **information-gaps register** (every unknown a `[GAP]`
  with an owner + ISO date via `smart_actions`) and the **revision/version control** (an
  update APPENDS, never overwrites). SCOPE-OUT: compiling the residual-hazard set
  (Residual-Hazard-Compiler).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (the **CDM Principal Designer** persona) before any output:
  is the file **residual-only** (could-not-anticipate, located — not a spec dump), are
  hazardous materials in situ recorded, are future-work controls HoC-ranked, and is the **Reg
  12(5) preparation duty + the handover duty** correctly attributed (never the wrong
  duty-holder), with the India state resolved before any form?
- **Critic/QA** (MANDATORY) — only residual/unusual hazards a future worker could not
  anticipate (no general-spec dump), every hazard located, hazardous materials in situ listed,
  every future-work control HoC-ranked with no unjustified PPE/admin-only, the Reg 12(5)
  duty + handover cited, an update appends (never overwrites), every gap owned + ISO-dated, the
  PCI → CPP → H&S File cross-reference present without assuming a sibling ran, every citation
  traces to the KB, zero input-derived PII leaked. PASS/FAIL.

A small single-package-addition file runs single-threaded — no subagents — but the `controls`
HoC-ranking, the `smart_actions` gap-closure call, and the Critic/QA pass are still made.

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
