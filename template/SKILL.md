---
name: skill-name
description: >
  One- to three-sentence, third-person description of what this skill produces
  and when to reach for it. Replace this placeholder when instantiating the
  template; it drives discovery and reinforces the "When to use" section below.
license: Apache-2.0
metadata:
  author: eyekyam
  version: "1.0"
  category: risk-assessment
  tier: 1
  audience: [M, C, F]
  industry: [All]
  jurisdiction: [All]
  status: stable
  plugin: hse-core
  hse_reviewed_by: ""
  hse_reviewed_date: ""
---

# Skill Name

<!-- Replace the title and this overview when instantiating the template. -->
A consultant-grade HSE skill that produces a specific, defensible artifact for a
named task, site, or asset. State in one to three sentences what it produces and
the single lever it forces (specificity + the hierarchy of controls).

## When to use this skill

Use this skill when the user needs <the artifact> for a concrete task/site/asset.
List the trigger scenarios that reinforce the `description` so the host routes to
this skill rather than a generic answer. If the request is vague ("write me a risk
assessment"), the Workflow intake below forces the specifics before any drafting.

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
## Knowledge base

Read exactly ONE matching knowledge-base fragment per invocation. Resolve it from
the `(jurisdiction × industry × audience)` facets declared in this skill's
`metadata`; if the matching fragment is unknown or ambiguous, ASK the user one
clarifying question rather than guessing. Whatever the jurisdiction, ALWAYS apply
the hierarchy of controls (eliminate → substitute → engineer → administrate →
PPE) — never a PPE-only treatment.

<!-- PLACEHOLDER → A3 Phase 2: the jurisdiction resolution ROWS below are a
     byte-identical Phase-1 placeholder. A3 fills the `(law, state) → fragment`
     rows via `hse-skill-forge --sync`; this header + rubric are FINAL. -->

| Jurisdiction | Knowledge-base fragment to read |
| ------------ | ------------------------------- |
| (rows resolved by A3) | `../../knowledge-base/<facet>/<fragment>.md` |
<!-- hse:block:kb-selection:end -->

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is
enumerable, free-text where it is open. Ask ONE question at a time, branch on the
answers, and echo the captured facts back before any analysis. Never proceed on
vague or missing inputs; this intake is the operational core of *forcing
specificity*. (Intake is a Workflow convention, not a sixth block.)

Then: analyse / apply the domain method → validate the draft against
`references/QUALITY_CHECKLIST.md` → produce the output via the Output format
section below. This is the only fully skill-authored section; each skill writes
its own intake question set and domain checklist here.

<!-- hse:block:orchestration:start -->
## Agentic Execution

This block governs **runtime fan-out** (decomposing the work of a single
invocation). It is platform-neutral: it never names a host API, only the pattern.

**Step 0 — Triage gate.** First judge the work. Map complexity to a subagent
budget, with MAX=6 fixed: simple → 0 subagents (single-threaded); moderate → 2–3
subagents; complex → 4–6 subagents. Never exceed MAX=6.

**Fan-out contract (when the triage gate calls for subagents).** For each job:
spin up a subagent with **fresh context**; **paste in all the context it needs**
(it cannot see this conversation); state its **scope-in / scope-out** explicitly
and name the sibling jobs so work is not duplicated; require a **bounded, cited
output** (findings traced to evidence, within a stated effort budget); then
**synthesize** the returned outputs into one coherent artifact.

**If your host has no subagent capability, execute each job sequentially in this
same context — keep the scope discipline and the required Critic/QA pass.**

**Critic/QA pass is mandatory** for any regulatory/safety/legal output (every
skill in this pack): after synthesis, run a dedicated critic that checks
specificity, the hierarchy of controls, defensibility, de-identification, and
citation accuracy before the artifact is returned.
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

- Single-threaded by design — no subagents. (Replace with this skill's named
  fan-out jobs if the triage gate warrants them.)

<!-- hse:block:report-output:start -->
## Output format

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
## Attribution

<!-- PLACEHOLDER → A9 Phase 2: this one-liner is a byte-identical Phase-1
     placeholder; A9 finalizes the company-card surfacing via `--sync`. -->

Surfaced non-intrusively from `branding/company-card.yaml` after the output — a
single line crediting the producing organization without interrupting the work.
<!-- hse:block:attribution:end -->

## Reference material

On-demand pointers (read only when needed):

- `references/METHODOLOGY.md` — the domain method this skill applies.
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
