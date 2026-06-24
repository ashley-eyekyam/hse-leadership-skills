---
name: offshore-safety-case
description: 'Structures the Offshore Safety Case argument under the Offshore Installations
  (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 (SI 2015/398) —
  major-accident-hazard (MAH) identification, the Safety & Environmental Management
  System (SEMS), the corporate major-accident-prevention policy (CMAPP), the ALARP
  demonstration framing, and the safety-and-environmental-critical-element (SCE) verification
  scheme with performance standards — and records the duty-holder''s content into
  the safety-case argument. Assistive: it assembles and structures the claim -> argument
  -> evidence and never produces the safety case autonomously; QRA and consequence
  modelling are done externally, with [GAP] recorded for any unsupplied element, figure,
  or barrier-effectiveness claim, and it never emits accepted/approved/authorised
  language (acceptance is the competent authority''s act). Decision-support only;
  a competent person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: process-safety
  tier: 4
  audience:
  - M
  - C
  industry:
  - O&G
  jurisdiction:
  - UK
  - EU
  status: assistive
  plugin: hse-marine-offshore
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Offshore Safety Case

An **assistive** (Tier-4) skill that structures the **Offshore Safety Case** argument under the Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 (**SI 2015/398**, "SCR 2015") — major-accident-hazard (MAH) identification, the Safety & Environmental Management System (SEMS), the corporate major-accident-prevention policy (CMAPP), the ALARP-demonstration framing, and the safety-and-environmental-critical-element (SCE) verification scheme with performance standards — and records the duty-holder's content into a defensible **claim → argument → evidence** map. It HoC-ranks the risk-reduction measures with `controls` and tracks the gap-closure actions with `smart_actions`. It **never produces the safety case autonomously**: QRA and consequence modelling are external, any unsupplied element/figure/barrier-effectiveness claim is recorded as `[GAP]` (never invented), and it **never emits "accepted / approved / authorised" language** — acceptance is the competent authority's (HSE + OPRED) act, not this skill's.

## When to use this skill

Use this skill to structure or assemble an **Offshore Safety Case** for a **named installation** — e.g. "structure our offshore safety case", "set out the MAH identification and the SEMS sections", "frame the ALARP demonstration", "build the SCE register + verification scheme argument". It is for UK/EU offshore oil & gas duty-holders (fixed platforms, mobile rigs, FPSOs). It **structures the argument and records the duty-holder's content**; it never fabricates the installation's scenarios, ALARP numbers, QRA, or barrier-effectiveness claims — those are external inputs the skill organises. The EER (evacuation/escape/rescue) element it records is produced and maintained by the sibling `marine-emergency-response` (MAR-03) skill — this safety case **cross-references that plan, it does not rebuild it**. If the request is vague, the intake forces the specific named installation first. **SI 2015/398 is the current regime; SCR 2005 is named only as the superseded legacy reference.**

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

Resolve the safety-case element against `../../knowledge-base/regulatory/offshore-scr.md`
(`KB-REG-OFFSHORE-SCR` — the SI 2015/398 duty → safety-case-element + SEMS map) on every run,
and apply the marine/offshore clause idiom in
`../../knowledge-base/prompt-snippets/marine-clause-map.md` (`KB-SNIP-MARINE-CLAUSE-MAP`).
For India offshore work, **state detection is mandatory** before any shore-base statutory cite:
read `../../knowledge-base/regulatory/in-offshore.md` (`KB-REG-IN-OFFSHORE`) and defer to the
`hse-india` engine (CONV-8) — **no national form number is minted; unverified content stays `[GAP]`.**

| Jurisdiction | Read |
|---|---|
| UK (current regime) | ../../knowledge-base/regulatory/offshore-scr.md (KB-REG-OFFSHORE-SCR — SI 2015/398; SCR 2005 named only as the superseded legacy reference) |
| EU | ../../knowledge-base/regulatory/eu-osh.md (Offshore Safety Directive 2013/30/EU framing) |
| India | ../../knowledge-base/regulatory/in-offshore.md (KB-REG-IN-OFFSHORE — OISD + PNG offshore rules deferral; state detection mandatory → hse-india; no national form minted) |
| Unknown | Ask before citing any specific law |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(named installation · installation type · regime · MAH identification inputs · the
ALARP/QRA provenance · the SCE register + performance standards · the SEMS/CMAPP set ·
the EER element cross-reference · author/duty-holder · the verification & acceptance
status), the echo-back, and the refuse-on-vague anchors — lives in
**`references/intake.md`**. Run it before any assembly: confirm the **named installation**
first, elicit the inputs for each SI 2015/398 Schedule 6/7 safety-case element, and
**record `[GAP]`** for any element, figure, or barrier-effectiveness claim not supplied
(the skill records external numbers, it **never computes or invents** them). When the
inputs carry any prior-incident context or named personnel, run the **De-identifier
first** (CONV-7) — installation/asset data dominates, but a prior-incident name or a
named station-bill role-holder is pseudonymised to a role label before drafting.

Then: assemble the claim → argument → evidence map per the domain method → validate the
draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format
section below. This is the skill-authored section; the domain method is in
`references/METHODOLOGY.md`.

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

For a non-trivial task the triage gate may fan out to:

- **De-identifier** — runs FIRST (sequential dependency, CONV-7); scrubs any
  prior-incident name, named station-bill role-holder, contact or competence-certificate
  number into role labels before any assembly, and returns the re-identification key
  SEPARATELY (to the orchestrator, never to a sibling or into the document). Installation
  / asset data dominates this artifact (lower de-id tier), but a prior-incident name is
  special-category data.
- **Researcher** — gathers the named installation's safety-case inputs, the SI 2015/398
  duty → element map (`KB-REG-OFFSHORE-SCR`) and the relevant standards, from the scrubbed
  inputs only; records `[GAP]` for any unsupplied element/figure — never invents one.
- **Argument Assembler** — assembles the claim → argument → evidence map in this skill's
  output format, HoC-ranks the risk-reduction measures, and traces every claim to a named
  evidence reference; it **records** the duty-holder's QRA/consequence figures with their
  provenance and **never computes or invents** them, and **never asserts an SCE/barrier
  effective** without a cited performance-standard evidence reference.
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (offshore safety-case author / process-safety lead +
  QRA-provenance & SCE-verification reviewer) before ANY output: Schedule 6/7 element
  completeness, ALARP-as-demonstration, every quantitative figure externally sourced, no
  un-evidenced barrier claim, and **no "accepted / approved / authorised" language**.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety output:
  specificity, hierarchy of controls, defensibility, de-identification, and citation
  accuracy (SI 2015/398 current, SCR 2005 legacy only).

Simple single-subject tasks run single-threaded — no subagents.

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
