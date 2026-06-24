---
name: toolbox-talk
description: Produces a short, ready-to-deliver toolbox talk (a pre-task safety briefing
  / tailgate / pre-start / take-5 / safety moment) plus a sign-off / attendance sheet
  for a specific crew, task, and site. It runs a quick structured intake, grounds
  the talk in the named task's real hazards and the hierarchy of controls, references
  a recent relevant incident or near-miss (de-identified, or a clearly-labelled typical
  example — never a fabricated local event), and gives the supervisor discussion prompts
  and key takeaways the crew can act on today. Use it for daily / shift safety briefings,
  tailgate talks, pre-job briefs, and topic safety moments — not for full risk assessments
  or incident investigations. Decision-support only; a competent person must review
  the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: training
  tier: 1
  audience:
  - F
  - M
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  bundled_in:
  - hse-construction
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Toolbox Talk

A fast, frontline toolbox-talk generator: it turns a short structured intake into a
**ready-to-deliver talk script plus a signable attendance / sign-off sheet** in one
short pass (the `<2-min` value). The one thing to internalise is **speed and
specificity together** — produce the talk in a single quick interaction, but make
every line about *this* task, *this* crew, *this* site: never generic safety patter.
A talk that says "the task" instead of "re-roofing Bay 3 with the cherry-picker out
of service" has failed its only job. Controls are hierarchy-of-controls-aware (no
PPE-only without justification); any referenced incident is de-identified or a
clearly-labelled typical example — never a fabricated local event. The deliverable
is a short, printable, plain-language talk + the sign-off sheet that makes the
briefing auditable.

## When to use this skill

Use this skill for a quick crew briefing before a specific task: a **daily / shift
safety briefing**, a **tailgate / pre-start / pre-job brief**, a **take-5 / safety
moment** on a named topic, or any short pre-task briefing on a non-routine job.
Trigger phrases: *toolbox talk, pre-task safety briefing, tailgate, pre-start,
pre-job brief, take-5, safety moment, daily / shift safety briefing, sign-off /
attendance sheet*. If the request is vague ("write me a toolbox talk"), the Workflow
intake below **refuses to proceed** until the specific task/site/crew is elicited.

**When NOT to use this skill** (steering to the right flagship keeps B3 lean): for a
full hazard assessment use `risk-assessment` (HIRA); for a step-by-step job safety
analysis use `job-safety-analysis`; to investigate an event that already happened use
`incident-investigation`. B3 briefs a crew before a task — it does not assess, file,
or investigate.

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

<!-- B3 jurisdiction rows are intentionally LEAN (Decision 5): a toolbox talk briefs a
     crew, it does not file a statutory form, so the default is the ISO 45001 standards
     backbone (7.4 communication / 5.4 consultation) and the per-jurisdiction reads are
     CONDITIONAL — only consulted if the talk must name a local rule. -->

| Jurisdiction / scope | Read |
|---|---|
| Not jurisdiction-specific (default) | ../../knowledge-base/standards/iso-45001.md (clause 7.4 communication / 5.4 consultation & participation — the management-system basis for a toolbox talk) |
| India | + ../../knowledge-base/regulatory/in-factories-act.md — only if a statutory point is raised; resolve the state first (mandatory state detection) |
| UK    | + ../../knowledge-base/regulatory/uk-hswa.md — only if a statutory point is raised |
| USA   | + ../../knowledge-base/regulatory/us-osha.md — only if a statutory point is raised |
| EU    | + ../../knowledge-base/regulatory/eu-osh.md — only if a statutory point is raised |

This skill always grounds in `KB-STD-ISO45001` clause **7.4 (communication)** + **5.4
(consultation & participation)** as the basis for the talk, applies `KB-SNIP-HOC` to any
control it states, and instantiates the `KB-SNIP-INTAKE` pattern in its lean intake. The
topic-specific hazard facts come from the relevant `data-points/` fragment selected by
intake Q1; an "Other" topic with no matching fragment degrades to general hazard framing
(recorded `[GAP]`, never invented). The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Lean structured intake (run first, one question at a time)

B3 runs the **leanest defensible intake in the pack** (Decision 2) — ~6–7 questions,
MCQ-heavy, with only **two** free-text prompts. The full typed, branched intake — the
`intake-coverage` manifest, the 7-row question table (topic/hazard · trade/crew · **site &
specific task today [the specificity anchor]** · duration · **recent incident [never
fabricated]** · reading level/language · light-touch jurisdiction), the light-touch
**India→state branch** (Q7 = India, mandatory only if a statutory point is raised), the
**never-invent-a-local-incident** discipline (Q5 blank → a clearly-labelled *typical*
example), the echo-back, and the refuse-on-vague anchors — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo the
captured facts back** before assembling, and **never invent** a fact (the cut is *quantity of
questions*, never *specificity* — every surviving question is load-bearing).

### The talk-assembly method (single-threaded — no fan-out)

The whole pass is one short interaction (the `<2-min` value). The sub-parts are
tightly dependent, so the orchestration block's Step-0 triage gate keeps B3
single-threaded; the de-id scrub (above) still runs **first**, and the mandatory
Critic/QA pass still runs **inline**. Full method in `references/METHODOLOGY.md`.
Assemble in this fixed 7-element structure:

1. **De-identify the inputs first** — the `deid` block above scrubs any user-supplied
   incident or named person to role labels *before* it reaches step 5. Never draft the
   talk over raw PII.
2. **Hook** — one or two sentences that make *this* hazard real for *this* crew today,
   on this named task (not generic patter).
3. **The specific hazard(s)** — the concrete, observable hazards of the named task/site
   (grounded in the topic's `data-points/` hazard facts) — the leading edge, the
   unavailable MEWP — not generic categories.
4. **Key controls (hierarchy-of-controls-aware)** — apply `KB-SNIP-HOC`: name
   higher-order controls first (eliminate → substitute → engineer → administrate →
   PPE); if only PPE/admin controls are available, **say why higher-order controls are
   not reasonably practicable** rather than defaulting to "wear your PPE". Each control
   names the specific hazard it addresses. (B3 wires **no** `controls.py` — the
   prompt-side `KB-SNIP-HOC` discipline is sufficient for the ~2 controls a talk names.)
5. **A recent relevant incident / near-miss** — the **de-identified** user-supplied
   event (role labels, no name, no <5 cell), **OR**, when none was supplied, a
   **clearly-labelled typical / illustrative example** ("a near-miss of this type
   reported elsewhere") — **never a fabricated 'last week on this site' local event**
   (Decision 6) — with the one lesson it teaches.
6. **Crew discussion prompts** — 2–3 open questions that get the crew talking ("what
   could go wrong on *our* task today?"), not a lecture.
7. **Key takeaways + sign-off** — 3–5 short actionable points the crew can act on this
   shift, then the **attendance / sign-off sheet** (Name/Role · Signature · Date) — the
   auditable record that the briefing happened.

Then **validate against `references/QUALITY_CHECKLIST.md`** (the 5-point talk-quality
self-check) and **produce the output** via the Output format section below.

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
     is presence-only (never diffed). B3 is the CANONICAL single-thread exemplar:
     the roster is exactly one line. B10 (incident-rate-calculator) and any future
     ~2-min skill copy this line verbatim. -->

- Single-threaded by design — no subagents.
- **SME Reviewer** (MANDATORY pre-output gate, run inline) — the skill-specific SME sign-off
  in **`references/sme-review.md`** (frontline safety supervisor / crew lead): is the talk
  about THIS task/crew/site today, deliverable in the target time, with real controls and a
  real (or clearly-labelled typical) incident — not generic patter? FLAG-only; does not block.

The Step-0 triage gate keeps B3 single-threaded (all three single-thread conditions
hold: it is a short/frontline ~2-min artifact, its parts are tightly dependent, and the
input fits one context window), so the orchestration block self-deactivates at runtime
and the skill assembles the talk directly. The inline **de-identification scrub still
runs first**, the inline **SME Reviewer pass** (`references/sme-review.md`) runs before
output, and the **mandatory Critic/QA pass still runs** (a single adversarial
self-check that the talk is specific, HoC-ranked, evidence-based, and PII-free before
delivery). On a host with no subagent capability nothing changes — B3 was already
single-threaded, the cleanest demonstration that the block degrades to nothing while
preserving the de-id + Critic discipline.

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
