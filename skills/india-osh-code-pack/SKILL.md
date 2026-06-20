---
name: india-osh-code-pack
description: 'Map an India establishment''s LEGACY statutory regime to its consolidated
  OSH Code 2020 equivalent — single registration, single consolidated annual return,
  the raised factory thresholds, the shifted Safety-Officer trigger — and flag what
  changes and that most states have NOT notified their OSH Rules. Use it for a forward-looking
  transition briefing: legacy-first answer + the consolidated direction + a per-state
  commencement caveat. State detection is MANDATORY; this is an opt-in transition
  mode that never tells a user to file an OSH form their state has not notified; any
  unnotified consolidated form is [GAP]-flagged, never invented; no hard-coded national
  form. Status beta — the law is actively transitioning. Decision-support only; a
  competent person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 3
  audience:
  - M
  - E
  - C
  industry:
  - All
  jurisdiction:
  - IN
  status: beta
  plugin: hse-india
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# India Osh Code Pack

The forward-looking **OSH Code 2020 transition** skill (`status: beta`). It maps an India establishment's **legacy statutory regime → its consolidated OSH-Code equivalent** (single registration; single consolidated annual return; the raised factory thresholds; the shifted Safety-Officer trigger), reading `KB-REG-IN-OSH-CODE`, and **flags what changes** and that **most states have not notified their OSH Rules** (the per-state notification status is read from `KB-REG-IN-OSH-CODE`, never hard-coded here; the savings clause keeps legacy filings valid). It runs in an explicit, opt-in **transition mode** and **never tells a user to file an OSH form their state has not notified** — any unnotified consolidated form is `[GAP]`-flagged, never invented. **State detection is MANDATORY** (CT-8); the legacy state form is always the primary, legacy-first answer (`KB-REG-IN-STATEFORMS`).

## When to use this skill

Use this skill for a **transition briefing**: "how will the OSH Code 2020 change what we file in [state], and is it live yet?". It returns the legacy-first answer + the consolidated direction of travel + a per-state commencement caveat. Because the law is **actively transitioning** (the KB fragment carries a 90-day staleness window, D-05c), it never overstates a consolidated form as live. It explains the transition; to find/assemble the legacy form itself, use `india-state-form-finder` / `factories-act-returns`.

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
| India (OSH transition) | ../../knowledge-base/regulatory/in-osh-code.md (KB-REG-IN-OSH-CODE — the consolidation map; status beta; 90d staleness, D-05c) |
| India (legacy form) | ../../knowledge-base/regulatory/in-state-forms.md (KB-REG-IN-STATEFORMS — **mandatory state detection**; the legacy-first primary answer) + in-factories-act.md |
| India (portal) | ../../knowledge-base/regulatory/in-portals.md (KB-REG-IN-PORTALS — Shram Suvidha / state portal; verify locally) |
| Any   | ../../knowledge-base/standards/iso-45001.md + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific law (confirm the **state** first) |

## Workflow

### Step 0 — Structured intake (run this first, one question at a time)

Open with a **structured multi-step intake** (`KB-SNIP-INTAKE`) — the full typed/branched
Q-table, coverage manifest, echo-back, and refuse-on-vague anchors live in
**`references/intake.md`**. Run ONE question at a time, branch on the answers, and **echo the
captured facts back before any mapping**. Never proceed on vague or missing inputs.

Must-ask dimensions: `ELI-JURIS` (**MANDATORY India→state detection — the state is a BLOCKING
gate, asked FIRST, infer-then-confirm; it drives whether the state has notified its OSH Rules;
unseeded/Unknown → direction-of-travel only, never a state-specific consolidated form**) ·
`ELI-INDUSTRY` (establishment type — each legacy regime maps differently) · `ELI-EXPOSURE`
(**worker headcount + power — drives the threshold-in/out conclusion: factory 10/20→20/40,
Safety-Officer 1000→500/250**) · `ELI-BASELINE` (what you file today — the *from* side of the
mapping) · `ELI-SCOPE` (the opt-in transition-mode toggle: legacy-only vs + mapping) ·
`ELI-SUBJECT` (legacy obligation) · `ELI-OUTPUT` (reader). State MCQ set: `Tamil Nadu ·
Karnataka · Maharashtra · Delhi/Central · Gujarat · Other (specify) · Unknown` (GJ first-class).

Once the **confirmed state + legacy obligation** are echoed back: give the **legacy-first**
answer (the legacy form from `KB-REG-IN-STATEFORMS`); then, in transition mode only, read
`KB-REG-IN-OSH-CODE` and map the legacy obligation → its consolidated OSH-Code equivalent,
**flagging what changes**. **Warn that the consolidated form/portal may not be live** in the
user's state — read the per-state notification status from `KB-REG-IN-OSH-CODE` (the volatile
fact lives only in the KB, never hard-coded here); for any state whose OSH Rules are not
notified, render the consolidated form `[GAP]`, never invented. **Never instruct the user to
file an OSH form their state has not notified.**

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

- **Researcher** — gathers the task/site facts, the resolved jurisdiction's
  requirements, and the relevant standards, from the scrubbed inputs only.
- **Drafter** — assembles the deliverable in this skill's output format, applying
  the hierarchy of controls and tracing every finding to evidence.
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety
  output: specificity, hierarchy of controls, defensibility, de-identification, and
  citation accuracy.
- **SME Review & Sign-off (MANDATORY, before any output)** — run the skill-specific
  OSH-Code transition persona + checklist in `references/sme-review.md` (legacy stays
  primary; never instruct filing an unnotified form). Decision-support only; it precedes
  — never replaces — the competent-person review.

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
