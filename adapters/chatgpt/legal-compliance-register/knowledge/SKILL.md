---
name: legal-compliance-register
description: Produces a multi-jurisdiction HSE legal and other-requirements compliance
  register for a named organisation or site. Use this skill whenever a user asks to
  build a legal register, compliance obligations register, applicable-legislation
  list, or to evaluate compliance against ISO 45001 clause 6.1.3. It identifies applicable
  legal and other requirements for the user's jurisdiction(s) and activities, maps
  each obligation to its applicability and the evidence of compliance, flags gaps
  with owners and review dates, and emits a branded register. For India, it defers
  to the hse-india engine for state-specific obligations and never hard-codes national
  form numbers; state detection is mandatory. Decision-support only; a competent person
  must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 2
  audience:
  - M
  - C
  - E
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-operations
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Legal Compliance Register

A consultant-grade HSE skill that produces a **multi-jurisdiction legal &
other-requirements compliance register** for a named organisation or site, grounded
in **ISO 45001 clause 6.1.3** (determination of legal and other requirements) and
**clause 9.1.2** (evaluation of compliance). It forces the single lever that separates
a defensible register from a copy-paste list: **applicability is confirmed against the
named activities, not just asserted** — every obligation row carries an applicability
rationale, a compliance-evidence cell, a named owner, and a review date. For **India**
it **defers to the `hse-india` engine** after **mandatory state detection** and never
mints a national form number (unverified → `[GAP]`). Method: `KB-SNIP-LEGAL-REGISTER-METHOD`.

## When to use this skill

Use this skill when the user needs a **legal register / compliance-obligations register
/ applicable-legislation list**, or to **evaluate compliance against ISO 45001 clause
6.1.3 / 9.1.2**, for a named organisation or site across one or more jurisdictions
(UK · US · EU · India · other). Trigger phrases: *legal register, compliance register,
applicable legislation, legal and other requirements, obligation register, compliance
evaluation, due-diligence register, M&A HSE legal review*. Each obligation is mapped
**obligation → applicability → compliance-evidence → gap/owner/review-date**, grouped
by jurisdiction. If the request is vague ("build me a legal register"), the Workflow
intake below **refuses to list any obligation** until the jurisdiction(s) and the
activity profile are captured; for **India**, mandatory **state detection runs before
any India obligation is cited** and the India leg defers to `hse-india`.

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
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (KB-REG-UK-HSWA — HSWA 1974 + MHSWR 1999 obligation set) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (KB-REG-US-OSHA — OSH Act + applicable 29 CFR 1910/1926) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md (KB-REG-EU-OSH — Framework Directive 89/391/EEC; cite member-state transposition for binding forms) |
| India | **DEFER to `hse-india`** — confirm the STATE first (../../knowledge-base/regulatory/in-state-forms.md, KB-REG-IN-STATEFORMS), then route via the three-tier India leg; never mint a national form number → `[GAP]` until resolved |
| Unknown | Ask before listing any obligation for that jurisdiction |

This skill always grounds in `KB-STD-ISO45001` (**6.1.3** legal & other requirements +
**9.1.2** evaluation of compliance) and applies `KB-SNIP-LEGAL-REGISTER-METHOD` (the
applicability → evidence → review-cadence method) over `KB-DATA-OBLIGATION-FAMILIES`
(the activity → obligation-family lookup per jurisdiction). The bundle clause cross-walk
is `KB-SNIP-OPS-CLAUSE-MAP` (6.1.3/9.1.2 → this skill). `KB-SNIP-HOC` ranks any control
raised against a gap. For an **India** leg it resolves the state via `KB-REG-IN-STATEFORMS`
and defers the state-specific obligation/return detail to the `hse-india` engine
(`india-state-form-finder` / `factories-act-returns`) — **mandatory state detection;
confirm the state before citing any form; never a national form number**; the legacy
form is the primary answer with the `KB-REG-IN-OSH-CODE` transition flagged. The rule-9
manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(jurisdiction(s) Q1 multi-select · the **mandatory India → state branch** Q1a · named
org/site + activities Q2 the **specificity anchor** · activity/hazard profile Q3 ·
register purpose Q4 · existing register Q5 · obligation owners Q6 · review cadence Q7),
the echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**. Run
it one question at a time, branch on the answers, **echo the captured facts back before
any analysis**, and **refuse to list any obligation** until the jurisdiction(s) **and**
the activity profile are captured (Q2/Q3 are the specificity anchors). **For India, the
mandatory state-detection branch (Q1 = India → Q1a + `KB-REG-IN-STATEFORMS`) runs before
any India obligation is cited** — record `[ASSUMPTION]` / `[GAP]`, never invent a state
form number.

### The register method (ISO 45001 6.1.3 + 9.1.2 — `KB-SNIP-LEGAL-REGISTER-METHOD`)

Full method in `references/METHODOLOGY.md`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Named compliance owners and any
   enforcement detail are role-labelled in the shared register; everything downstream
   consumes the scrubbed text.
2. **Applicability determination (per named activity — confirm, do not just list)** —
   for each jurisdiction and each activity/hazard from the intake, look up the
   obligation family in `KB-DATA-OBLIGATION-FAMILIES`, then **confirm the obligation is
   APPLICABLE to the named activity** — an obligation pulled for an activity the org
   does not perform (e.g. a construction reg for an office) is **flagged as inapplicable
   and excluded**, not listed. This applicability rigour is the core-value lever; a
   vacuous "thorough" register that lists inapplicable law is a defect the Critic/QA
   pass must catch.
3. **Obligation extraction + citation** — for the applicable obligations, cite the
   source instrument from the resolved jurisdiction's KB fragment (UK `KB-REG-UK-HSWA` ·
   US `KB-REG-US-OSHA` · EU `KB-REG-EU-OSH`, citing member-state transposition for
   binding forms). **India is NOT cited here — it routes through step 4.** Never invent
   a citation; an uncertain obligation is `[GAP]`.
4. **India leg — DEFER to `hse-india` (three-tier graceful degradation; state detection
   FIRST)** — run mandatory state detection (Q1a / `KB-REG-IN-STATEFORMS`), then produce
   the India obligations by deferring to the `hse-india` engine:
   - **Tier 1 (subagents available):** spawn the **India-Obligation-Mapper** subagent,
     which runs the relevant `hse-india` skill — `india-state-form-finder` (resolve the
     state form/return/portal) and/or `factories-act-returns` (the return obligations) —
     for the resolved state.
   - **Tier 2 (no subagents):** the main thread reads the `hse-india` KB INLINE
     (`KB-REG-IN-FACTORIES` + `KB-REG-IN-STATEFORMS`, flagging the `KB-REG-IN-OSH-CODE`
     transition) and integrates the India rows itself.
   - **Tier 3 (`hse-india` not installed):** fall back to **routing prose + a KB pointer
     + `[GAP]`** — name the skill to run (`india-state-form-finder` / `factories-act-returns`)
     and mark the state-specific form `[GAP]`.
   At **every tier**: the legacy state form is the primary answer, the OSH-Code direction
   is flagged, **no national form number is ever minted** (unverified → `[GAP]`), and the
   India leg **never hard-blocks** the rest of the register.
5. **Evidence mapping + gap/owner/review-date (9.1.2)** — for each applicable obligation,
   map the **compliance evidence** the org holds (permit, certificate, test record,
   procedure) → mark **Compliant / Gap / [GAP-evidence]**; every row carries a **named
   (role-label) owner** and a **review date**. A gap raises a control via `KB-SNIP-HOC`
   (eliminate the non-compliant activity / engineer the control before an administrative
   reminder) + a SMART action — call `smart_actions.validate_register`; any action
   missing an owner, a valid date, a measure, or an obligation link is invalid.
6. **Compliance-evaluation summary (9.1.2)** — summarise applicable obligations,
   compliant vs gap counts, and the overdue-for-review set; flag every gap with its
   owner and target date. Group the register **by jurisdiction**, with the **India
   deferral note** (state-detection result + the `hse-india` routing) as its own section.
7. **Validate against `references/QUALITY_CHECKLIST.md`** — every obligation has an
   applicability rationale + an evidence cell + an owner + a review date; no inapplicable
   regulation listed; India rows defer to `hse-india` with no minted form number; no
   invented citation; de-id applied (owners role-labelled).
8. **Assemble the branded report** — build `report.json` (see
   `assets/legal-compliance-register-report.template.json`) and run the canonical
   `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge
the assembled work before deciding to fan out (typically by jurisdiction).

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

This is the **moderate roster** (A6 "moderate = 2–4"), fanned out **by jurisdiction**:
the De-identifier is the **sequential first gate**, then one **Obligation-Mapper per
jurisdiction** (the India mapper defers to `hse-india`), a **Register-Synthesizer**, and
a **mandatory Critic/QA**. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub named
  compliance owners + any enforcement/disciplinary detail to role labels before any
  analysis (every mapper below consumes scrubbed text). Returns the re-identification
  key SEPARATELY to the orchestrator, never into the register.
- **UK Obligation-Mapper** — for the UK activities, confirm applicability per activity
  against `KB-REG-UK-HSWA`, extract obligation → source instrument → evidence prompt;
  flag inapplicable regs as excluded and `[GAP]` where uncertain. SCOPE-OUT: other
  jurisdictions, India (India-Obligation-Mapper owns it), synthesis (Register-Synthesizer).
- **US Obligation-Mapper** — same against `KB-REG-US-OSHA` (OSH Act + the applicable
  29 CFR 1910/1926 standards for the named activities). SCOPE-OUT: as above.
- **EU Obligation-Mapper** — same against `KB-REG-EU-OSH` (Framework Directive 89/391/EEC;
  cite member-state transposition for binding forms). SCOPE-OUT: as above.
- **India-Obligation-Mapper (via `hse-india`)** — runs the D-04 three-tier deferral with
  **state detection FIRST** (`KB-REG-IN-STATEFORMS`): **Tier 1** runs the `hse-india`
  skills `india-state-form-finder` / `factories-act-returns` for the resolved state;
  **Tier 2** reads the `hse-india` KB inline (`KB-REG-IN-FACTORIES` + `KB-REG-IN-STATEFORMS`,
  flagging `KB-REG-IN-OSH-CODE`); **Tier 3** emits routing prose + a KB pointer + `[GAP]`.
  **NEVER mints a national form number; never hard-blocks.** SCOPE-OUT: UK/US/EU mappers,
  synthesis.
- **Register-Synthesizer** — assemble the per-jurisdiction obligation rows into the
  grouped register (obligation/applicability/evidence/gap/owner/review-date), the
  compliance-evaluation summary (9.1.2), and the India deferral note; raise a
  `KB-SNIP-HOC`-ranked SMART action for each gap. SCOPE-OUT: the per-jurisdiction
  applicability calls (the mappers own them).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Regulatory Compliance Counsel / HSE Legal Specialist):
  applicability rationale real, no inapplicable reg listed, India deferred not minted,
  every obligation owned + evidenced + review-dated.
- **Critic/QA** (MANDATORY) — every obligation has an applicability rationale + evidence
  cell + owner + review date; no inapplicable regulation; India rows defer to `hse-india`
  with **no minted form number** ([GAP] where unresolved); no invented citation; zero
  PII leaked. PASS/FAIL.

Single-jurisdiction registers run single-threaded — no subagents — but the
applicability-confirmation, the India three-tier deferral, and the Critic/QA pass are
still made.

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
