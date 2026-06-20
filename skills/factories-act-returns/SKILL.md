---
name: factories-act-returns
description: Assemble an India Factories Act state statutory return or register for
  a DETECTED state — the annual / half-yearly return + statutory registers (TN Form
  22 / KA Form 20 / MH Form 27 / DL Form 21; GJ [GAP] until verified) — legacy-first,
  with the OSH-Code transition note appended. Use it to produce the filled state return
  for a named establishment in a given state, with the prescribed form id, citing
  rule, due date and filing portal. State detection is MANDATORY; an unseeded state
  yields [GAP] and a refusal to invent a national form number; form values absent
  from the KB are [GAP]-flagged, never fabricated. Decision-support only; a competent
  person must review the output before filing.
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
  - All
  jurisdiction:
  - IN
  status: stable
  plugin: hse-india
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Factories Act Returns

A consultant-grade, India-facing skill that assembles a **Factories Act state statutory return / register** for a **detected state** — the annual / half-yearly return + statutory registers — legacy-first, with the OSH-Code transition note appended. It resolves the prescribed form from `KB-REG-IN-STATEFORMS`: **TN Form 22 / KA Form 20 / MH Form 27 / DL Form 21**, and **GJ `[GAP]`** (the Gujarat annual-return form value is a literal `[GAP]` until verified — the citation grader is row-blind, so a fabricated value would pass the automated gate; D-02/CT-1). **State detection is MANDATORY** (CT-8): an unseeded state yields `[GAP]` and a **refusal to invent a national form number** (KB-02). The OSH-Code direction of change is noted (legacy-first).

## When to use this skill

Use this skill to produce the **filled state Factories-Act return** (annual / half-yearly) or a statutory register for a named establishment in a given state — with the prescribed form id, citing rule, due date, and filing portal. Use it when a manager or consultant says "assemble our [state] Factories Act annual return". If the state is missing, the intake forces it FIRST — a wrong state is a wrong statutory form. It assembles the return; to merely *find* which form applies, use `india-state-form-finder`; for the accident notice specifically, use `india-accident-notice`.

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

| Jurisdiction | Read |
|---|---|
| India (state form) | ../../knowledge-base/regulatory/in-state-forms.md (KB-REG-IN-STATEFORMS — the (law,state,obligation) engine; **mandatory state detection**) + in-factories-act.md (KB-REG-IN-FACTORIES — statutory framing) |
| India (OSH transition) | ../../knowledge-base/regulatory/in-osh-code.md (KB-REG-IN-OSH-CODE — append the legacy-first transition note) |
| India (portal) | ../../knowledge-base/regulatory/in-portals.md (KB-REG-IN-PORTALS — state factory-department portal; verify locally) |
| Any   | ../../knowledge-base/standards/iso-45001.md + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific law (confirm the **state** first) |

## Workflow

### Step 0 — Structured intake (run this first, one question at a time)

Open with a **structured multi-step intake** (`KB-SNIP-INTAKE`) — the full typed/branched
Q-table, coverage manifest, echo-back, and refuse-on-vague anchors live in
**`references/intake.md`**. Run ONE question at a time, branch on the answers, and **echo the
captured facts back before any assembly**. Never proceed on vague or missing inputs.

Must-ask dimensions: `ELI-JURIS` (**MANDATORY India→state detection — the state is a BLOCKING
gate, asked FIRST, infer-then-confirm; unseeded → `[GAP]`, refuse a national form**) ·
`ELI-EVIDENCE` (the return fields elicited **field-group by field-group** — accident tally by
class, leave-with-wages, OSH appointments — never one blob) · `ELI-EXPOSURE` (avg/max workers +
man-days — drive thresholds and the return body) · `ELI-COMPETENCY` (the **occupier / factory
manager** who signs — a load-bearing named role) · `ELI-BASELINE` (first filing vs correction) ·
`ELI-INDUSTRY` (hazardous-process?) · `ELI-TEMPORAL` (return year / half) · `ELI-SCOPE` /
`ELI-SUBJECT` / `ELI-OUTPUT`. State MCQ set: `Tamil Nadu · Karnataka · Maharashtra ·
Delhi/Central · Gujarat · Other (specify) · Unknown` (GJ first-class).

Once the **confirmed state + obligation + establishment** are echoed back: read the matched
`KB-REG-IN-STATEFORMS` row and assemble the return under its prescribed `form` / `rule` / `due`
(TN Form 22 / KA Form 20 / DL Form 21; **GJ = `[GAP]`**). **`[GAP]` — MH annual-return form-id:**
`KB-REG-IN-STATEFORMS` seeds MH only for accident-notice, with no seeded MH annual-return row,
so the MH annual-return form is carried forward as a literal `[GAP]` (verify against the live
Maharashtra Factory Rules 1963 / seed the row — see `references/intake.md`); do **not** assert a
number. Append the row's `osh_transition` note and a pointer to `india-osh-code-pack`, and
surface the `KB-REG-IN-PORTALS` (state factory-department) pointer. Every field absent from the
source is a literal `[GAP]`, never fabricated.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method is in `references/METHODOLOGY.md`.

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

### Step 4 — Critic / QA (MANDATORY — this is regulatory/safety output)
Spawn ONE Critic: give it the draft + the inputs + the output contract. It finds errors,
unsupported claims, missed regulatory triggers, lower-order-only controls, and any
de-identification leak. Fix everything it raises before delivery.

> Single-threaded fallback: if your host has no subagent capability, execute each job
> sequentially in THIS context — run the de-identification scrub first, keep the scope
> discipline, and still perform the required Critic/QA pass before delivery.
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

For a non-trivial task the triage gate may fan out to:

- **Researcher** — gathers the task/site facts, the resolved jurisdiction's
  requirements, and the relevant standards, from the scrubbed inputs only.
- **Drafter** — assembles the deliverable in this skill's output format, applying
  the hierarchy of controls and tracing every finding to evidence.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety
  output: specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.
- **SME Review & Sign-off (MANDATORY, before any output)** — run the skill-specific
  Indian factory / occupational-safety compliance persona + checklist in
  `references/sme-review.md` (correct STATE form for the occupier; every unverified field —
  incl. the MH annual-return form-id — honestly `[GAP]`). Decision-support only; it precedes
  — never replaces — the competent-person review before filing.

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
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
