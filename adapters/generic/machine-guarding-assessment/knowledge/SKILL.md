---
name: machine-guarding-assessment
description: 'Produces a consultant-grade machine-guarding assessment for a named
  machine or line — guard-by-hazard-zone per ISO 12100/14120 and OSHA 1910 Subpart
  O (1910.212/.219). Use this skill whenever a user asks to assess machine guarding,
  review a guarding survey, select guards or protective devices for a danger zone,
  check guarding against PUWER or Subpart O, or build a hazard-zone register — not
  a generic ''guard all moving parts''. It is engineering-control-led: each danger
  zone walks the selection order (fixed, interlocked, presence-sensing, two-hand,
  trip) against the access-frequency rule, and a mechanical-zone control left as PPE-only
  or admin-only (''keep hands clear / wear gloves'') is flagged and pushed up the
  hierarchy. It refuses ''a machine'' or ''looks guarded'' without a named machine
  plus motion/hazard type plus safeguarding status, cross-references the existing
  lockout/tagout map for maintenance, and emits a branded hazard-zone register. Decision-support
  only; a competent person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - Mfg
  jurisdiction:
  - All
  status: stable
  plugin: hse-manufacturing
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Machine Guarding Assessment

A consultant-grade, **guard-by-hazard-zone** machine-guarding assessment for a **named machine,
line, or cell** — never a generic "guard all moving parts" statement. Its entire reason to exist
is that **mechanical-zone safeguarding is engineering-control-led**: for every danger zone the
guard/device is selected in order — **fixed → interlocked → presence-sensing → two-hand/hold-to-run
→ trip** — against the **access-frequency rule**, inside the **ISO 12100 three-step method**
(inherent safe design → safeguarding → information for use). A mechanical-zone control left as
**PPE-only or admin-only** ("operators trained to keep hands clear / wear gloves" with no fixed or
interlocked guard) is **flagged and pushed up the hierarchy — never accepted as the headline
control**. That is the failure mode this skill exists to prevent.

It forces the single lever that separates a defensible artifact from copy-paste paperwork:
**per-zone specificity plus the full hierarchy of controls**. It **refuses** to assess "a machine"
or "looks guarded" without a **named machine + the motion/hazard type + the existing-safeguarding
status**. The **maintenance interaction mode** cross-references the existing `KB-REG-LOTO`
energy-isolation map (lockout/tagout). Grounded in **OSHA 29 CFR 1910 Subpart O** (1910.212 /
1910.219), **ISO 12100 / ISO 14120**, and **PUWER 1998 Regs 11–12**. Decision-support only; a
competent person must review the output.

## When to use this skill

Use this skill when the user needs a **machine-guarding assessment for a concrete machine, line,
or cell** — for example "assess the guarding on the PL-3 power press", "review the guarding survey
for the assembly cell against Subpart O", "select guards for the in-running nip point on the
calender", or "build a hazard-zone register for the CNC mill". It is **not** for a generic
"how do I guard machines?" answer: the Workflow intake below forces the named machine, the motion
and danger zones, and the existing-safeguarding status before any drafting, and refuses a vague
"a machine" / "looks guarded" request.

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

| Jurisdiction / scope | Read |
|---|---|
| USA | ../../knowledge-base/regulatory/osha-1910-o.md (KB-REG-OSHA1910-O) — OSHA 29 CFR 1910 Subpart O: **1910.212** general requirements (point of operation, in-running nip points, rotating parts, flying chips/sparks; guards affixed and secure) + **1910.219** mechanical power-transmission apparatus (shafts, belts, gears, couplings) |
| UK / EU | ../../knowledge-base/regulatory/uk-hswa.md — **PUWER 1998 Regs 11–12** (dangerous parts of machinery + protection against specified hazards), read with the ISO 12100 + ISO 14120 guard standards |
| EU | ../../knowledge-base/regulatory/eu-osh.md |
| India | ../../knowledge-base/regulatory/in-factories-act.md — **Factories Act 1948 §21 (fencing of machinery)** + the hazardous-process provisions; **defers to `hse-india`, mandatory state detection (+ in-state-forms.md for the user's state); emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |
| Guard/device selection (every danger zone) | ../../knowledge-base/prompt-snippets/guard-selection.md (KB-SNIP-GUARD-SELECTION) — the **engineering-control-led selection order** (fixed → interlocked → presence-sensing → two-hand/hold-to-run → trip) governed by the **access-frequency rule**; "operators to be careful / wear gloves" as a headline control is rejected (`KB-SNIP-HOC`) |
| Machine-safety method (every run) | ../../knowledge-base/standards/iso12100-14120.md (KB-STD-ISO12100-14120) — the **ISO 12100 three-step method** (inherent safe design → safeguarding → information for use) + the ISO 14120 guard taxonomy; the method the guard/device selection sits inside |
| Maintenance interaction (Q5 = maintenance) | ../../knowledge-base/regulatory/loto.md (KB-REG-LOTO — **REUSE, existing fragment**) — the **energy-source → isolation-step → verify-zero-energy** map for servicing/maintenance (29 CFR 1910.147 / UK EAWR); the maintenance interaction mode cross-references this for lockout/tagout |
| Manufacturing clause cross-walk | ../../knowledge-base/prompt-snippets/manufacturing-clause-map.md (KB-SNIP-MANUFACTURING-CLAUSE-MAP) — the ISO-45001 §6.1.2 / §8.1.2 + ISO 12100 three-step manufacturing clause cross-walk |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) + the manufacturing clause cross-walk
`KB-SNIP-MANUFACTURING-CLAUSE-MAP`, drives **guard/device selection per danger zone** through
`KB-SNIP-GUARD-SELECTION` against the **access-frequency rule** inside the **ISO 12100 three-step
method** (`KB-STD-ISO12100-14120`), grounds the US duty on `KB-REG-OSHA1910-O` (1910.212 / 1910.219),
and — when the maintenance interaction mode is selected (Q5) — cross-references the **existing**
`KB-REG-LOTO` fragment for energy isolation (the LOTO duty is the existing regulatory fragment; no
separate LOTO-isolation snippet is minted). For an India site, resolve the state via `hse-india` (**mandatory
state detection**) and emit a literal `[GAP]` where a state form/return is owed — never a minted
national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the hazard-zone walk one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "a machine" or "looks guarded": you need the named
machine + its motion/hazard type + the existing-safeguarding status before any drafting.**

1. **The named machine** (free-text — the specificity anchor) — "Name the exact machine / line /
   cell + manufacturer/model + what it does (e.g. 'PL-3 250-ton power press, blanking line').
   **Refuse 'a machine' / 'the factory' — the assessment is machine-specific.**"
2. **Machine type & motion** (mcq, multi-select) — power press / rotating shaft or spindle /
   conveyor or in-running rolls / robot or automated cell / mixer or auger / saw or blade /
   other (+ detail) — the hazardous motion drives the danger zones.
3. **Danger zones** (mcq, multi-select; per 1910.212(a) / ISO 12100) — point of operation /
   in-running nip point / rotating parts / power-transmission (shaft/belt/gear) / flying
   chips or sparks / crush or trap point.
4. **Existing safeguarding & condition** (free-text) — "What guards/devices are fitted today,
   and their condition? **A defeated, missing, or overridden guard is flagged immediately as a
   high-priority finding.**"
5. **Interaction modes** (mcq, multi-select) — normal operation / setting / cleaning /
   **maintenance** — **selecting MAINTENANCE triggers the lockout/tagout cross-reference to
   `KB-REG-LOTO`** (energy isolation: identify sources → isolate → verify zero energy).
6. **Jurisdiction** (mcq) — USA / UK / EU / India / Other / Unknown. **India → resolve the state
   via `hse-india` (mandatory state detection); emit `[GAP]`, never a national form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented guard.

Then: run the guard/device selection per danger zone (`KB-SNIP-GUARD-SELECTION`, the `controls`
engine — a PPE/admin-only mechanical-zone control is a FLAG pushed up the hierarchy) → re-score
the residual → validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output
via the Output format section below. The domain method is in `references/METHODOLOGY.md`.

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

For a multi-zone guarding survey the triage gate fans out to (the **De-identifier runs
FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier (esp. a **named
  operator from a prior amputation / crush incident**) to role labels before any analysis;
  return the re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **Hazard-Zone-Analyst** — enumerate the **danger zones** per machine (point of operation,
  in-running nip points, rotating parts, flying chips/sparks per 1910.212(a) / ISO 12100),
  record the motion type and the existing-safeguarding status per zone, and flag a defeated /
  missing / overridden guard immediately as a high-priority finding. SCOPE-OUT: does not
  select the guard (the Guard-Selection-Engineer owns it) or rank the residual.
- **Guard-Selection-Engineer** — for each zone, drive `KB-SNIP-GUARD-SELECTION` (fixed →
  interlocked → presence-sensing → two-hand/hold-to-run → trip) against the **access-frequency
  rule**, cite the ISO 14120 basis, and run the **`controls` engine** — a mechanical-zone
  control left PPE-only / admin-only (`ppe_admin_only=True`) is a **FLAG pushed up the
  hierarchy, never the headline control**. Re-score the residual via `risk_matrix`. SCOPE-OUT:
  does not de-identify (De-identifier) or check the law (the SME persona).
- **Interaction-Mode-Author** (optional — when a setting/cleaning/**maintenance** mode is in
  scope) — author the per-mode controls; for the **maintenance** mode cross-reference
  `KB-REG-LOTO` for energy isolation (identify sources → isolate → verify zero energy).
- **Critic/QA** (MANDATORY) — adversarial final pass: every danger zone has an
  engineering-led guard or a recorded FLAG, no PPE/admin-only mechanical-zone control accepted,
  every citation resolves (1910.212/.219 / ISO 14120), the maintenance LOTO cross-ref is
  present, and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the A7 `controls` /
`risk_matrix` / `smart_actions` calls and the per-zone guard selection inline, then the
mandatory Critic/QA + SME pass — same scope discipline, no subagents.

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
