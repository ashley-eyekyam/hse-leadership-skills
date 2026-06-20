---
name: chemical-transport-safety
description: Produce loading/unloading and transport safety guidance and a classification
  cross-walk for road and sea — ADR (EU road), United States DOT 49 CFR HMR (American
  road), and IMDG (sea) — including UN number / class / packing group, placarding,
  marking and segregation. Use it to classify dangerous goods for transport, cross-walk
  a GHS class to a transport class, work out placarding/segregation, or write loading/unloading
  safety guidance. Rail (RID) and air (IATA/ICAO-TI) are out of scope for v1.0 and
  flagged, not guessed; unknown UN entries are [GAP]-flagged; controls are hierarchy-of-controls
  ranked. Decision-support only; a competent person must review the output.
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
  - Chem
  - Process
  jurisdiction:
  - All
  status: stable
  plugin: hse-chemicals
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Chemical Transport Safety

A consultant-grade skill that produces loading/unloading and transport safety guidance and a classification cross-walk for road and sea — **ADR** (EU road, `KB-REG-EU-ADR`), **US DOT HMR** (US road, `KB-REG-US-DOT-HMR`) and **IMDG** (sea, `KB-STD-IMDG`) — including UN number / class / packing group, placarding, marking and segregation, cross-walked from the GHS class (`KB-STD-GHS`). Rail (RID) and air (IATA/ICAO-TI) are **out of scope** for v1.0 and flagged, not guessed; an unknown UN entry is `[GAP]`-flagged. Largely classification lookup + document assembly (single-thread); controls are HoC-ranked (`controls`).

## When to use this skill

Use this skill to classify dangerous goods for transport, cross-walk a GHS class to a transport class, work out placarding/segregation, or write loading/unloading safety guidance — for a named substance and a chosen mode. If the request is vague, the intake forces the substance, mode and packaging; rail/air are flagged out of scope rather than guessed.

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
| EU    | ../../knowledge-base/regulatory/transport-adr-dot.md (KB-REG-EU-ADR road) + standards/imdg.md (KB-STD-IMDG sea) |
| USA   | ../../knowledge-base/regulatory/transport-adr-dot.md (KB-REG-US-DOT-HMR road) + standards/imdg.md (sea) |
| Any   | ../../knowledge-base/standards/ghs.md (KB-STD-GHS — class cross-walk) + standards/imdg.md (KB-STD-IMDG) + prompt-snippets/hierarchy-of-controls.md |
| Unknown | Ask before citing any specific law |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

**Run the full structured intake in `references/intake.md`** — the typed/branched
Q-table, its intake-coverage manifest, the echo-back, and the refuse-on-vague anchors
live there. It elicits the substance/CAS + UN number (resolve the UN entry from the
user's DG list, never assumed; unknown → `[GAP]`), physical state/flashpoint, quantity
per package + total consignment, the transport mode + regime
(**road-India (CMVR) → resolve the state, mandatory** — `references/intake.md` Q6; rail
& air OUT OF SCOPE, flagged not guessed), packaging, the GHS/§14 basis
(neither → `[GAP]`, route to `ghs-classification-sds-author`), and route detail. Echo
substance + mode + packaging back before the cross-walk. The class / UN / packing group
is resolved from the regime table (`KB-REG-EU-ADR` / `KB-REG-US-DOT-HMR` / `KB-STD-IMDG`),
cross-walked from the GHS class; loading/unloading controls are HoC-ranked.

Then: analyse / apply the domain method → validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. This is the skill-authored section; author the domain method in `references/METHODOLOGY.md`.

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

- Single-threaded by design — no subagents. (Replace with this skill's named
  fan-out jobs if the triage gate warrants them.)
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the skill-specific
  persona, domain checklist, and boundary in `references/sme-review.md` (dangerous-goods
  transport SME / DGSA lens: UN entry resolved from the DG List not assumed; the
  GHS→transport cross-walk correct for the chosen mode; rail/air flagged out of scope
  not guessed). Decision-support only; precedes — never replaces — the human
  competent-person / DGSA review.

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
