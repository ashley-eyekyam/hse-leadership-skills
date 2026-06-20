---
name: dgms-statutory-pack
description: Resolves the India Mines Act / DGMS statutory obligation for a mine —
  the 24-hour accident / dangerous-occurrence notice, the Form J accident register,
  the Form B employee register, the annual return (~20 January), and statutory Manager
  / officials appointment letters — for the mine's resolved region, and drafts the
  prescribed legacy form plus the OSH-Code transition note. Use it to determine which
  DGMS form a mine must file, draft a statutory mine notice / return / register entry,
  or check a statutory appointment. It cites only the five verified DGMS anchors as
  values; any unverified DGMS form id is recorded as [GAP], never invented. Decision-support
  only; a competent (DGMS-qualified) person must review the output.
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
  - Min
  jurisdiction:
  - IN
  status: stable
  plugin: hse-mining
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Dgms Statutory Pack

A consultant-grade compliance skill that resolves the **India Mines Act 1952 / DGMS** statutory obligation for a specific mine and drafts the prescribed **legacy** form — the **24-hour accident / dangerous-occurrence notice**, the **Form J** accident register, the **Form B** employee register, the **annual return (~20 January)**, and the **statutory Manager / officials appointment** letters — for the mine's **resolved region/zone**, with the OSH-Code transition note appended. It cites **only the five verified DGMS anchors** as values; any DGMS form id the KB does not verify is recorded as **`[GAP]`**, never invented. Folds the `dgms-returns-assistant` returns workflow. Grounds in `KB-REG-IN-MINES-ACT` / `KB-REG-IN-DGMS`; `smart_actions` tracks any follow-up. Decision-support only — a competent (DGMS-qualified) person reviews the output.

## When to use this skill

Use this skill when a mine must determine which DGMS form to file, draft a statutory mine notice / return / register entry, or check a statutory appointment — for a named mine in a resolved region. The obligation is the runtime gate (B6 pattern): the skill resolves the obligation, then drives to the prescribed form. Region/zone detection is **mandatory** before any form is cited. If the request is vague, the Workflow intake forces the mine context first. Any un-verified DGMS form id is recorded `[GAP]`, never fabricated.

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

| Jurisdiction | Read |
|---|---|
| India (mine) | ../../knowledge-base/regulatory/in-mines-act.md (KB-REG-IN-MINES-ACT) + regulatory/in-dgms.md (KB-REG-IN-DGMS — forms; [GAP] where unverified) |
| India (region) | ../../knowledge-base/regulatory/in-state-forms.md (KB-REG-IN-STATEFORMS — mandatory region/zone resolution) |
| Any | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — MS backbone) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific DGMS form |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open; one question at a time, branch on the answers, echo the captured facts before any drafting; refuse on a vague subject and never invent (`KB-SNIP-INTAKE`).

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched Q-table — obligation gate (Q1), the mandatory DGMS
region/zone resolution (Q4), the per-obligation follow-ups (Q5a–Q5d), the echo-back
and the refuse-on-vague anchors — lives in **`references/intake.md`**. Must-ask
dimensions: the **obligation** (the runtime gate) and the **DGMS region/zone** (a
mandatory gate that must be confirmed before any form is cited). Resolve the obligation
→ the `KB-REG-IN-MINES-ACT` duty row → the **form** from `KB-REG-IN-DGMS`; cite **only**
the five verified anchors (Form J, Form B, 24h notice, annual return ~20 Jan, statutory
Manager appointment) as values, and for **any other** DGMS form emit a literal
`(DGMS-prescribed — verify per mine) [GAP]`, **never a fabricated number**. Append the
OSH-Code transition note (legacy-first); `smart_actions` owner+dates any follow-up;
validate against `references/QUALITY_CHECKLIST.md`, then produce the output.

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

**Step 4 — SME review & sign-off (MANDATORY, before any output):** run the skill-specific
SME persona sign-off in **`references/sme-review.md`** (the DGMS statutory-compliance
specialist) — model QA, decision-support, FLAGs non-blocking; it precedes and never
replaces the human DGMS-qualified competent-person review.

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
