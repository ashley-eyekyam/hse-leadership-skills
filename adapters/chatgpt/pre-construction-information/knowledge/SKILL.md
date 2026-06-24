---
name: pre-construction-information
description: Produces a Pre-Construction Information (PCI) pack for a named construction
  project under CDM 2015 — the pre-tender hazard and information set the client must
  provide to every designer and contractor. Use this skill whenever a user asks to
  compile, write, or review pre-construction information, a PCI pack, CDM pre-tender
  information, or the client's health-and-safety information for a project. It assembles
  the project, site, and existing-structure hazard information (asbestos, buried services,
  ground conditions, adjacent occupancies, existing H&S file content), states what
  is known versus a documented information gap, and emits a branded report that feeds
  the construction phase plan. Grounded in CDM 2015 Regulation 4. Decision-support
  only; a competent person must review the output.
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

# Pre-Construction Information (PCI) — CDM 2015 Reg 4

A consultant-grade HSE skill that produces a task/site-specific **Pre-Construction
Information (PCI) pack** for a **named construction project** under **CDM 2015 Regulation
4** — the pre-tender hazard and information set the client must provide, *as soon as
practicable*, to everyone appointed or being considered (Reg 4(4)). It assembles the
**existing-structure hazard information** (asbestos / hazardous materials, buried and
overhead services, ground conditions, structural form, the existing health & safety
file), the **site & surroundings**, and the **significant hazards a designer/contractor
must be told of**, grounded in the **L153 Appendix-1 PCI content checklist**
(`KB-SNIP-PCI-CHECKLIST`).

Its signature lever is **gap discipline**: every missing existing-structure source — a
missing asbestos survey, no ground investigation, no as-built drawings — is recorded as a
`[GAP]` with a **named owner + due date** and turned into an owned/dated `smart_actions`
item, **never silently omitted**. A PCI that drops a missing survey instead of flagging it
is a defensibility failure. The pack **feeds the Construction Phase Plan** — it cross-walks
the **PCI → CPP → H&S File** chain (Reg 4 → 12 → 12(5)) via the single
`KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **never assuming a sibling skill ran** (the CDM trilogy
stays loosely coupled). The information-gap closure actions use the deterministic A7
`smart_actions` engine; PCI is information assembly + gap documentation, not calculation.

## When to use this skill

Use this skill when the user needs to **compile, write, or review Pre-Construction
Information, a PCI pack, CDM pre-tender information, or the client's health-and-safety
information** for a **named construction project** — for example "compile the PCI for the
Tower B brownfield refurbishment", "what existing-structure hazard information must I give
the designers for this demolition", or "review this PCI pack before it goes to tender".
Trigger phrases: *pre-construction information, PCI, PCI pack, CDM pre-tender information,
client's H&S information, existing-structure hazard information, information gaps register,
Reg 4, L153 Appendix 1*. The load-bearing inputs are the **named project + client** and the
**existing-structure information status (present or `[GAP]`)**; if either is vague, the
Workflow intake below **refuses to proceed** until they are elicited. PCI is information for
*before* construction starts — a request for the Construction Phase Plan (CON-01) or the
Health & Safety File (CON-03) is routed to its CDM-chain sibling (Q1 disambiguates).

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
| UK    | ../../knowledge-base/regulatory/cdm-2015.md (**CDM 2015 Reg 4** — the client's PCI duty, provided *as soon as practicable* to everyone appointed/considered (Reg 4(4)); Reg 4(5)/(6) no construction start without arrangements/CPP; the **L153 Appendix-1 PCI content checklist**) |
| USA   | ../../knowledge-base/regulatory/osha-1926.md (29 CFR 1926 — site-condition disclosure equivalents) |
| India | ../../knowledge-base/regulatory/in-state-forms.md (BOCW pre-work site information — **defers to `hse-india` / `bocw-compliance`, mandatory state detection; emit a literal `[GAP]`, never a minted national form number**) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill grounds every run in `KB-STD-ISO45001` (6.1.2) and applies `KB-SNIP-HOC` to
every control. It assembles the PCI content heads from `KB-SNIP-PCI-CHECKLIST` (the L153
Appendix-1 checklist: project & client brief · existing structure · services · ground ·
surroundings · significant hazards · information-gaps register) and grounds the client's
**Reg 4 duty + timing** on `KB-REG-CDM2015` — **omitting the Reg 4 duty/timing is a
regulatory_citation_accuracy hard-fail**. For an **India** site it resolves the state via
`KB-REG-IN-STATEFORMS` (**mandatory state detection**) and **defers the India leg to the
`hse-india` `bocw-compliance` skill** — legacy-first, **never a minted national form
number**; an un-seeded state → `[GAP]`. The one-line **PCI → CPP → H&S File** (Reg 4 → 12 →
12(5)) cross-reference is sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP` **without assuming
the CPP or H&S File skill ran** (loose coupling). The rule-9 manifest is
`references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(Q1 **project & client** · Q2 **existing-structure information sources** · Q3 site &
surroundings · Q4 known significant hazards · Q5 project stage · Q6 jurisdiction), the
**UK → CDM 2015 Reg 4** path and the **mandatory India → state branch** (defers to
`hse-india` / `bocw-compliance`, state detection mandatory, literal `[GAP]`, never a minted
national form number), the echo-back, and the refuse-on-vague anchors — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo the
captured facts back before any analysis**, and **refuse to proceed** on a generic project
(Q1) or with the existing-structure information status unknown — **the GATE: no PCI until a
named project + client AND the existing-structure information status (present or `[GAP]`)
are captured**. **Q1 also disambiguates the CDM document** — this skill owns the PCI; a
request for the Construction Phase Plan (CON-01) or the Health & Safety File (CON-03) is
routed to its CDM-chain sibling. Full method in `references/METHODOLOGY.md`.

### The PCI compilation method (gap discipline is the lever)

Full method in `references/METHODOLOGY.md`, grounded in `KB-SNIP-PCI-CHECKLIST`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Survey/occupier inputs routinely carry a
   **named occupier with a health detail** (e.g. an asbestos survey naming a resident's
   condition) — scrub these to role labels; a leak there is an **auto-fail**. Set a
   **restricted-distribution flag** where the PCI carries sensitive site detail.
2. **Inventory the existing-structure information sources** (Q2) — for each PCI content head
   in `KB-SNIP-PCI-CHECKLIST` (existing structure · services · ground · surroundings ·
   significant hazards), record **what is known versus what is a documented gap**.
3. **Capture the existing-structure hazard information** — asbestos / ACMs and hazardous
   materials, buried & overhead services, ground conditions / contamination, structural
   form & stability, the existing H&S file content; each cited to its stated source, with
   `[ASSUMPTION]` / `[GAP]` flagged where uncertain — **never invent a survey result**.
4. **Document the surroundings** — adjacent occupancies, boundaries, access/egress, the
   public interface, neighbouring activities (Q3).
5. **Build the information-gaps register (the gap-discipline lever)** — **every missing
   source is recorded as a `[GAP]`, never silently omitted**: a missing asbestos survey, no
   ground investigation, no as-built/services drawings each becomes an explicit register row
   stating the gap and the assumption carried in its place.
6. **Turn every gap into an owned/dated action** — for each `[GAP]` produce a SMART action
   via `smart_actions.validate_register`: specific, **assignable (named owner / role)**,
   **time-bound (ISO due date)**, linked to the gap. Any action missing an owner, a valid
   date, or a gap link is **invalid** and must be fixed — no anonymous gaps, no "ASAP". An
   information gap that blocks construction (e.g. an outstanding asbestos survey) is flagged
   as a **hold-point** before the relevant works start.
7. **Cross-reference the CDM document chain** — add the one-line **PCI → CPP → H&S File**
   (Reg 4 → 12 → 12(5)) cross-reference sourced from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`,
   **without assuming the CPP or H&S File skill ran** (loose coupling). State the **client's
   Reg 4 duty and timing** (as soon as practicable; before appointments/start) — omitting it
   is a citation hard-fail.
8. **Validate against `references/QUALITY_CHECKLIST.md`** — every missing information source
   recorded as a `[GAP]` (not omitted); asbestos status explicit; buried/overhead services
   addressed; the client's Reg 4 duty cited; every gap owned + dated; de-id applied; no
   conclusion on an unstated assumption.
9. **Assemble the branded PCI report** — build `report.json` (see
   `assets/pre-construction-information.report.json`) and run the canonical `report-output`
   call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **`smart_actions` gap-closure call (step 6)
is an A7 script call in every case — never a fan-out job**; PCI uses no scoring/matrix
engine (it is information assembly, not calculation).

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

This is a **moderate fan-out** roster (A6 "moderate = 2–3") for a complex brownfield PCI:
the **De-identifier is the sequential first gate** (not a fan-out peer), then two fan-out
jobs — **Existing-Structure-Hazard-Compiler** and **Surroundings-&-Gap-Author** — with a
**mandatory Critic/QA** and the **CDM Principal Designer / Client Adviser SME** pre-output
gate. A **simple greenfield PCI runs single-threaded** — no subagents — but the
`smart_actions` gap-closure call and the Critic/QA pass are still made. Archetypes:
`KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all PII /
  health detail to role labels before any analysis — **a named occupier with a health
  detail from a survey** (e.g. an asbestos survey naming a resident's condition), survey
  authors, exact dates/locations — everything downstream consumes scrubbed text; a leak is
  an **auto-fail**. Set the **restricted-distribution flag** where the PCI carries sensitive
  site detail. *(Duty-holders the user deliberately names for the record stay named.)*
- **Existing-Structure-Hazard-Compiler** — compile the existing-structure hazard
  information from the scrubbed inputs per `KB-SNIP-PCI-CHECKLIST`: **asbestos / hazardous
  materials, buried & overhead services, ground conditions / contamination, structural form
  & stability, the existing H&S file content** — each cited to its stated source, flag
  `[GAP]` where a source is missing (never invent a survey result). SCOPE-OUT: surroundings
  and the gaps register (Surroundings-&-Gap-Author); the law (the Drafter cites Reg 4).
- **Surroundings-&-Gap-Author** — author the **site & surroundings** (adjacent occupancies,
  public interface, access, services) AND build the **information-gaps register**: **every
  missing source becomes a `[GAP]` with a named owner + ISO due date via `smart_actions`,
  never silently omitted**; flag any gap that is a construction hold-point. SCOPE-OUT:
  compiling the existing-structure hazard detail (Existing-Structure-Hazard-Compiler).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (the **CDM Principal Designer / Client Adviser** persona)
  before any output: is the existing-structure hazard information complete and source-cited,
  is **every missing source a documented `[GAP]`** (not omitted), is the client's Reg 4 duty
  & timing stated, and is the India state resolved before any form?
- **Critic/QA** (MANDATORY) — every missing information source recorded as a `[GAP]` (not
  silently omitted), asbestos status explicit, buried/overhead services addressed, every gap
  owned + ISO-dated + gap-linked, the Reg 4 client duty cited, the PCI → CPP → H&S File
  cross-reference present without assuming a sibling ran, every citation traces to the KB,
  zero input-derived PII leaked. PASS/FAIL.

Simple single-subject (greenfield) PCIs run single-threaded — no subagents — but the
`smart_actions` gap-closure call and the Critic/QA pass are still made.

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
