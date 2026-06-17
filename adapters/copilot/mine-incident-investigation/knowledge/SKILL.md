---
name: mine-incident-investigation
description: Sector-tuned incident investigation for a mining event (a DGMS-reportable
  accident or dangerous occurrence) — de-id-first 4-fan-out, ICAM-led root-cause analysis
  reaching organisational factors, a DGMS reportability verdict (24-hour notice +
  Form J entry), and a hierarchy-of-controls CAPA plan with named owners and due dates.
  Use it to investigate a mine accident, run an RCA on a mining incident, or determine
  DGMS reportability. Decision-support only; a competent (DGMS-qualified) person must
  review the output. Statutory form ids beyond the verified DGMS anchors are recorded
  as [GAP], never invented.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: incident-management
  tier: 2
  audience:
  - M
  - C
  industry:
  - Min
  jurisdiction:
  - IN
  - All
  status: stable
  plugin: hse-mining
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Mine Incident Investigation

A consultant-grade incident-management skill — sector-tuned **incident investigation** for a mining event (a **DGMS-reportable** accident or dangerous occurrence). It **extends the B5 flagship pattern verbatim**: a **de-id-first** 4-subagent fan-out (De-identifier -> Evidence/Timeline + Root-Cause Analyst + Regulatory-Reportability Checker + Corrective-Action Drafter -> mandatory Critic/QA), **ICAM-led** RCA reaching organisational factors, cause->evidence + CAPA->cause traceability, and a hierarchy-of-controls CAPA (`controls` / `smart_actions`). It overlays the **DGMS reportability path** — the **24-hour accident notice + Form J** register entry (`KB-REG-IN-DGMS`), region-resolved (`KB-REG-IN-STATEFORMS`). Statutory form ids beyond the verified DGMS anchors are recorded **`[GAP]`**, never invented. `incident_rates` is context only. Decision-support only — a competent (DGMS-qualified) person reviews the output.

## When to use this skill

Use this skill to investigate a **mine accident**, run an **RCA** on a mining incident, build a CAPA from a mining event, or determine **DGMS reportability** — for a specific mining incident. It is the core B5 investigation with a mining intake, **ICAM as the default RCA method**, and a DGMS 24h-notice + Form-J reportability path. De-identification runs FIRST. If the request is vague, the Workflow intake forces the incident facts first; any un-verified DGMS form id is recorded `[GAP]`, never fabricated.

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
| India (mine) | ../../knowledge-base/regulatory/in-dgms.md (KB-REG-IN-DGMS — 24h notice + Form J; [GAP] elsewhere) + regulatory/in-mines-act.md (KB-REG-IN-MINES-ACT) |
| India (region) | ../../knowledge-base/regulatory/in-state-forms.md (KB-REG-IN-STATEFORMS — mandatory region/zone resolution before any form) |
| Any | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — 10.2 incident) + prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |
| Unknown | Ask before citing any specific DGMS form |

## Workflow

Open with a **structured multi-step intake** (`KB-SNIP-INTAKE`) — one question at a time, branch, echo the captured facts before any analysis. **De-identification runs FIRST** (the orchestration block below) — injured/deceased-miner identity, witness detail, exact pit/shaft locations and small (<5) fatality/injury cells are scrubbed to role labels and suppressed before any analysis.

1. **Mine + region** — commodity, opencast/underground, and the **DGMS region/zone** (**mandatory** — ask or infer-from-location-then-confirm; region precedes any form citation).
2. **Event** — free-text: the de-identified incident facts (what/when/where/sequence).
3. **RCA method** — MCQ, **ICAM default** (5-Whys / ICAM / SCAT / Fishbone / Swiss-Cheese); every causal claim cites an evidence item and the RCA **reaches a systemic/organisational factor** (not 'miner error').

Then (B5 pattern + DGMS overlay): reconstruct the timeline + evidence log; run the RCA (`rca`, reaches_systemic); **resolve DGMS reportability** — the **24-hour accident notice + Form J** register entry for a DGMS-reportable accident/dangerous occurrence (`KB-REG-IN-DGMS`), region-resolved; cite **only** the verified DGMS anchors as values, any other form id `[GAP]`, never invented; draft the **HoC-tagged CAPA** (`controls` / `smart_actions`), each tracing to a named cause with owner + due date. `incident_rates` is context only. Validate against `references/QUALITY_CHECKLIST.md`, then produce the output via the Output format section. A competent (DGMS-qualified) person reviews it.

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
- **De-identifier** — runs FIRST (sequential dependency); scrub all PII/health detail —
  injured-party, witnesses, diagnoses, exact dates/locations, small injury cells — into role
  labels before any analysis. Returns the re-identification key SEPARATELY (to the orchestrator,
  not to any sibling). Everything below consumes only its scrubbed output.
- **A · Evidence & Timeline Reconstructor** — assemble the numbered, time-ordered event
  sequence and the numbered evidence log (E-1…) from the scrubbed inputs; flag [GAP].
  SCOPE-OUT: does not assign causes (B owns it) or decide reportability (C owns it).
- **B · Root-Cause Analyst** — apply the chosen method (5-Whys / ICAM / SCAT / Fishbone /
  Swiss-Cheese) via rca.py; every causal claim cites an evidence item (E-n); reach a
  systemic/organisational factor (rca.validate `reaches_systemic` true for whichever method).
  SCOPE-OUT: reportability (C owns it) and control selection (D owns it).
- **C · Regulatory Reportability Checker** — for the resolved jurisdiction (India → resolved
  STATE first), return verdict + clause/section + deadline + form (India state accident form
  via KB-REG-IN-STATEFORMS / UK RIDDOR / US OSHA 29 CFR 1904). Conservative — flag [GAP] and
  "ask a competent person" when unsure. SCOPE-OUT: does not draft the report or invent a form number.
- **D · Corrective-Action Drafter** — hierarchy-of-controls-tagged CAPAs, each tracing to a
  named cause (RC-n) with a named owner + ISO due date + measure; prefer higher-order controls,
  justify any PPE/admin-only. SCOPE-OUT: does not score causes (B) or check law (C).
- **Critic/QA** (MANDATORY) — adversarial read-only review: every cause evidence-backed, RCA
  reaches a systemic factor, reportability cited conservatively to the matched KB row, every
  CAPA traces to a cause with owner+date, no PPE/admin-only without justification, and ZERO
  PII/health leak (no residual identifier, no <5 cell, no re-id key in the output).

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
