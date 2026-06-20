---
name: hse-skill-forge
description: 'Scaffold a new, contract-conformant HSE Leadership skill at build time:
  this build-time authoring tool runs an author-interview, then emits a born-conformant
  skills/<name>/ with the five inline blocks byte-matching template/blocks/*, the
  folder skeleton, vocab-validated metadata, the seeded runtime intake step, and an
  A8-shaped evals skeleton. It is for skill authors and maintainers extending the
  pack, not an HSE-advice skill — it produces no risk assessment, talk, or investigation.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: ms-admin
  tier: 1
  audience:
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-systems
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# hse-skill-forge — the build-time scaffolder

A **build-time authoring tool** for the people who EXTEND this skill pack — skill
authors and maintainers, not HSE end users. It runs a short author-interview about
the skill you want to build, then emits a **born-conformant** `skills/<name>/` that
`lint_skills.py` passes with zero hand-edits: the five inline blocks copied
byte-for-byte from `template/blocks/*`, the folder skeleton, vocab-validated
metadata, the §2.7 runtime-intake STEP seeded into the new skill's Workflow, the
A7 component shim and A9 branding link where declared, and an A8-shaped `evals/`
skeleton (including the de-id fixture pair). It produces **no** HSE artifact — no
risk assessment, no toolbox talk, no investigation; it produces the *next skill*.

The forge dogfoods the very contract it scaffolds: this SKILL.md is itself a
conformant six-block skill (it is how the pack proves the contract is satisfiable
in practice — A10 AC#8).

## When to use this skill

Use this skill at **build time** when you are adding a new skill to the HSE
Leadership pack or regenerating an existing skill's contract surface — for example:

- "Scaffold a new `permit-to-work` skill" / "add a `behaviour-based-safety` skill".
- "Re-sync this skill's inline blocks against the canonical `template/blocks/*`"
  (the `--sync` anti-drift verb).
- "Give me a contract-clean skeleton I can drop a domain body into."

Do **not** reach for this skill to produce an HSE deliverable for a real task or
site — that is what the `hse-core` advice skills (risk-assessment, toolbox-talk,
incident-investigation, …) are for. This skill lives in the `hse-systems` bundle,
deliberately outside the advice grouping, so it is never mistaken for one.

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

<!-- The forge handles no real-task PII (it scaffolds skills, not HSE artifacts);
     the de-id block is inherited byte-for-byte because the contract is invariant —
     every skill in the pack, the forge included, carries it. If an author ever
     pastes a real incident sample as an example while building a skill, the block
     above governs: scrub it BEFORE it lands in any seeded eval fixture. -->

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

<!-- The forge has no jurisdiction-specific advice surface of its own — it grounds
     in the AUTHORING references (subagent archetypes + the runtime-intake pattern),
     listed in references/_skill-kb.md. The table below is the presence-only rule-2
     subsection (never byte-diffed); it documents the rows the forge SEEDS into every
     scaffolded skill so the author refines them for the jurisdictions that skill serves. -->

| Jurisdiction | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

## Workflow

The forge's Workflow is an **author-interview**: a build-time Q&A that asks WHAT
skill to build, not what HSE problem to solve.

> **The two intakes are categorically distinct — never conflate them (A10 D4, "the
> single most important error to avoid").** The author-interview below is the
> *forge's own* Workflow; it asks the author about the skill they want to create.
> It is NOT the §2.7 runtime intake. The runtime intake is a *seeded STEP* — a
> `<!-- TODO -->` scaffold (`templates/intake-todo.md`) that the forge plants into
> the NEW skill's Workflow for the author to fill with that skill's domain
> questions later. The forge never invents the new skill's domain question VALUES;
> it only seeds the intake STEP. See `references/mandatory-blocks.md` for the full
> contrast.

### Step 1 — Author-interview (one question at a time)

Ask these ten questions, MCQ where the answer space is enumerable, free-text where
it is open; branch on the answers; echo the captured facts back before scaffolding:

1. **Skill name** — lowercase `[a-z0-9-]`, ≤64 chars, MCP-safe (free-text).
2. **One-line domain** — what artifact does it produce? (free-text → `description`).
3. **Category** — MCQ from the A2 §4.1 `category` vocab (risk-assessment, training,
   incident-management, compliance, ms-admin, …).
4. **Audience** — MCQ, one or more of M / E / F / C.
5. **Industry** — MCQ from the `industry` vocab (All, Con, Chem, Min, Avi, …).
6. **Jurisdictions** — which the skill serves (All / UK / US / IN / EU).
7. **Single-thread vs roster** — MCQ: single-thread · moderate fan-out · the
   flagship-b5 four-agent roster (`references/orchestration-patterns.md`).
8. **A7 components** — MCQ: which deterministic engines it calls (risk_matrix,
   controls, rca, smart_actions, incident_rates) — or none (no `scripts/`).
9. **Trigger keywords** — the discovery phrases (reinforce `description`).
10. **Tier + status** — MCQ from the `tier` (1–4) and `status` (stable/beta/assistive) vocab.

### Step 2 — Serialize → scaffold → validate → handoff

- Serialize the answers to an `answers.json` (the `metadata{}` block + `roster` /
  `a7_components` / `kb_ids` flags — see `references/mandatory-blocks.md`).
- Run `scripts/scaffold.py --name <name> --answers <answers.json>` (add
  `--from-skill-creator <draft.md>` to wrap a `skill-creator` domain draft, or
  `--standalone` to use the `templates/*` fallback skeletons).
- The scaffolder self-validates: it refuses exit 0 unless its output lints clean.
- Run `scripts/validate_repo_skill.py <skill>` (the `lint_skills.py` re-export) to
  confirm; `--sync` re-pulls any drifted canonical block from `template/blocks/*`.
- Hand off `assets/forge-handoff.template.json` listing the seeded TODOs the author
  must fill (the domain body, the intake question VALUES, the eval expectations).

This Workflow performs no HSE analysis and circulates no personal data; the
deterministic blocks above are inherited because the contract is invariant.

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

- Single-threaded by design — no subagents. The forge's author-interview +
  scaffold + self-lint runs in one context. (NOTE: this is the forge's own
  *runtime* roster — distinct from the BUILD-TIME `§3.7` campaign fan-out, where
  one subagent authors each skill in parallel; the forge SEEDS rosters into other
  skills via `references/orchestration-patterns.md`, it does not run a fan-out itself.)

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

<!-- The forge's "output" is a scaffolded skill directory + the
     assets/forge-handoff.template.json hand-off, NOT a rendered DOCX/PDF report. The
     report-output block is inherited byte-for-byte because the contract is invariant
     (every skill carries it); the forge simply does not exercise the render path. -->

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

- `references/mandatory-blocks.md` — the human-readable six-block contract; what
  each block is, its marker, and that its text is canonical in `template/blocks/*`.
- `references/orchestration-patterns.md` — the roster-authoring menu (single-thread
  · moderate · flagship-b5), pointing at `KB-SNIP-ARCHETYPES`.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
- `references/METHODOLOGY.md` — the scaffold→validate→handoff method.
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
