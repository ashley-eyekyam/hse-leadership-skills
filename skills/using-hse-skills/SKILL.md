---
name: using-hse-skills
description: Routes a user to the right HSE skill(s) when they are unsure which to
  use. Use this skill whenever the request is meta or ambiguous — 'not sure which
  assessment is needed', 'where to start with HSE for a site', 'what is needed for
  a new contractor job', 'an overview of the toolbox', or any multi-step HSE task
  spanning several deliverables. It elicits intent, requirement and success-criteria,
  then recommends one or an ordered chain of repo skills and hands the context over.
  It does NOT itself produce a risk assessment, toolbox talk, or any HSE artifact
  — a clear single-skill request (e.g. 'do a risk assessment for re-roofing') should
  go straight to that skill, not here.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: ms-admin
  tier: 1
  audience:
  - M
  - E
  - F
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Using HSE Skills — the catalog router (front door)

This is the catalog's **front door**, not an HSE deliverable. It elicits the user's intent,
requirement, and success-criteria, then reads the generated catalog index and recommends
**one skill or an ordered chain of skills** — each with a one-line rationale — and hands the
de-identified context over so the user enters the shared facts **once**. It produces **no**
risk assessment, toolbox talk, or any other HSE artifact itself: a clear single-skill request
goes straight to that skill; this router is for meta, ambiguous, or multi-step HSE intent.

## When to use this skill

Use this skill when the user is **unsure which HSE skill they need**, or when their goal
spans **several deliverables** — "not sure which assessment I need", "where do I start with
HSE for this site", "what do I need for a new contractor job", "give me an overview of the
toolbox", or a single task that clearly needs a chain (e.g. re-roofing → risk assessment,
JSA, permit, toolbox talk). The Workflow intake forces the shared facts before any
recommendation. A request that already names its own artifact ("write a toolbox talk for
tonight's shift") should go straight to that skill — this router does **not** hijack it.

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
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

## Workflow

**Step 0 — Structured intake (run `references/intake.md`).** Open with the multi-step
intake — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE
question at a time, branch on the answers (the **mandatory India→state** branch included),
and **echo the captured facts back before any recommendation**. Never proceed on vague or
missing inputs — Q-SUBJECT is the specificity anchor (`KB-SNIP-INTAKE`). The router elicits
only the **shared, carry-over facts** (the 3 universal facets + jurisdiction/industry/
exposure); the deep per-artifact facets are deferred to the chosen skill (no double-intake).
(Intake is a Workflow convention, not a sixth block.)

**Step 1 — Read the index.** Read `references/skill-index.yaml` — the committed,
generated catalog index (one row per routable skill: full `description`, `bundles`,
`category`, `triggers`). Do NOT hand-list skills from memory; the index is the single
non-drifting roster.

**Step 2 — Match intent → an ordered chain (with a WHY per skill).** Reason over each row's
`description` + `triggers` + `category` + `bundles` against the elicited intent and
success-criteria. Assemble an **ordered set** (not a single forced pick — a multi-deliverable
goal becomes a chain), and write a **one-line `WHY`** per recommended skill tying it to the
elicited intent / success-criteria (ROUTE-03). If the request clearly names a single artifact,
recommend that one skill and point straight at it — do not over-elicit (D-06).

**Step 3 — De-identify the captured facts FIRST.** Before writing any handoff block, run the
De-identifier (orchestration block, above) over the captured facts: pseudonymize to stable
role labels (`[SITE-1]`, `[ROLE: site manager]`, `[CONTRACTOR]`) per `references/deid-checklist.md`.
The run-sheet/handoff blocks are the de-id surface — a leak here is a non-waivable HARD-fail.

**Step 4a — Confirm-or-refine gate (the accuracy lever).** Before any handover, present ONE
choice on the echoed context + draft chain: **accept** it as-is / **edit** the context /
**re-scope**. On an **edit**, fold the change into the captured facts (no new question — reuse
Step-0's facts), **re-run Step 2's match** so the chain refines, and show a one-line iteration
trail (e.g. "refined to add `permit-to-work` because the edit named confined-space entry").
Loop until the user accepts. This adds no elicitation facet — it re-drives the match on the
facts already captured.

**Step 4b — Emit + PERSIST + PRESENT the run sheet (the durable Steps-2+ plan).** (**MANDATORY
— produce this IN FULL before Step 4c. Do NOT mention Step 1, invoke any skill, or proceed to
4c until this step is complete.**) De-id has already run (Step 3). Compose the **complete
standalone plan**: ONE de-identified **Context Capsule** (the Step-0 facts + the agreed
`SEQUENCE MAP`), the ordered **chain table**, a **Step-1 record** (what Step 1 is / that it
runs in place), then for each later step (Step 2, 3, …) TWO blocks:

(A) A lean **continuation prompt** with the markers **`WHY`** (one-line rationale) / **`RUN`**
(`/skill-name` or "use the X skill") / **`REFERENCE`** (points back to the Context Capsule
above — do NOT repeat the shared context) / **`ATTACH`** (the **specific named section or
table** to copy from the prior skill's output, e.g. "copy the 'Control Measures Table' and the
'Residual Risk Rating' summary from the risk-assessment output" — already de-identified by
that skill; name the exact heading) / **`DELTA`** (only this step's new detail) /
**`DEPENDENCY`** (Independent / Dependent — run after Step N) / **`FEEDS →`** the next step.

(B) A **`PASTE-BLOCK`** — a pre-merged, fully copy-pasteable block titled clearly
"📋 **Copy this entire block and paste it at the top of your Step N chat**". It inlines, in
order: the full Context Capsule text (verbatim from above), the ATTACH instruction (naming the
specific section to copy from the prior skill's output), and the DELTA for this step. This is
the ONE thing the user pastes to start that fresh chat — no assembly required.

Add a short opt-in **"expand to standalone"** note for a user who cannot carry the capsule.
Persist with ONE portable rule: on a host with file-write, **write the run sheet to a durable
de-identified `.md` file** with a role-label filename slug (e.g.
`hse-run-sheet-<subject-slug>.md` — never a real name/site) and **surface the path**; on a
chat-only host, present the SAME run sheet as ONE clearly-delimited, copy-pasteable fenced
markdown **save-block** ("save this as your Steps-2+ run sheet"). Tell the user this saved file
is their durable Steps-2+ plan — it survives Step 1 flooding the chat. The persisted file and
every continuation prompt are the de-id surface — role labels only (`[SITE-1]`,
`[ROLE: site manager]`, `[CONTRACTOR]`), no re-id key; a leak here is a non-waivable HARD-fail.

**Step 4c — Clearance gate (Step 1 fires only on "go").** Present the saved run sheet and ask
ONE go/no-go: *"Here is your saved run sheet — review it. Say 'go' (or 'proceed' / 'run step 1')
to start Step 1 here, or 'edit' to change the context/chain first."* Step 1 is invoked **only on
explicit clearance**. An **edit** loops back to **Step 4a** (re-drive the Step-2 match and
**re-persist**). This gate applies on **EVERY host — the Skill-tool host included** — so Step 1
**never auto-fires**.

**Step 4d — Run Step 1 IN PLACE (asymmetric), now GATED on clearance.** ONLY after clearance:
Step 1 is **not** a copy-paste-to-fresh-chat block. On a Skill-tool host, invoke Step 1's skill
seeded with the confirmed facts in THIS same chat. Off-platform (no Skill tool), print a
complete, copy-pasteable Step-1 block to paste **here** (ROUTE-04 portability). Steps 2+ are the
fresh-chat set; Step 1 is run where the user already is.

**Step 5 — Teach the user how to run it (educative).** Explain, don't just list: **Step 1 runs
here** because the first skill does the heavy lifting and fills this chat; **Steps 2+ go to a
fresh chat each** because a fresh chat stays fast and focused; **your run sheet already contains
everything you need for each later step** — find the step, copy the `📋 PASTE-BLOCK`, and paste
it at the top of a fresh chat; and the de-id reassurance — **the OUTPUT you attach is already
de-identified by the skill that produced it**, so attach the skill's emitted output (not raw
notes), specifically the named section the PASTE-BLOCK points to, and the chain stays clean.
Add: **the saved run sheet is your durable Steps-2+ plan — keep it open in a separate tab**; we
held off Step 1 until you'd saved it, because Step 1 fills this chat. Each target skill's own
§2.7 "echo back facts" intake then confirms the pasted capsule and asks only the deferred
facets — **edit no other skill**. The full method (capsule composition, the A/B continuation
format, the PASTE-BLOCK rule, the attached-output rule, the iteration-trail convention, and the
persist-then-clear rule) lives in `references/METHODOLOGY.md`.

**On request only:** also render the run sheet as a branded "HSE Skills Roadmap" document via
the shared report engine (Output format below) — composed from the existing report-model block
types; never forced when the user just wants to chain straight in.

Validate the recommendation against `references/QUALITY_CHECKLIST.md` before presenting. The
router cites only existing KB ids (`KB-SNIP-INTAKE`, `KB-SNIP-HOC`, `KB-STD-ISO45001`) and
mints none; the routing method detail lives in `references/METHODOLOGY.md`.

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
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

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
