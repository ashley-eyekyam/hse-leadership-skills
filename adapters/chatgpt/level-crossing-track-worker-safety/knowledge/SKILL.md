---
name: level-crossing-track-worker-safety
description: Build a level-crossing and track-worker safe-system-of-work artifact
  for a named crossing or work site. Use this skill to assess and control level-crossing
  risk and on-or-near-the-line track-work risk for a specific crossing, possession,
  or worksite. It leads level-crossing remediation with closure -> grade separation
  -> engineering, with sighting / signage / administrative LAST, and leads track-worker
  protection with separation (green-zone / line blockage / possession) -> safe systems
  of work -> warning -> lookout-only LAST. It RECORDS the user's All Level Crossing
  Risk Model (ALCRM) band rather than inventing or recomputing it (a missing band
  is [GAP]), grounds the work in KB-REG-LX-TRACKWORKER and KB-SNIP-LX-HIERARCHY, scores
  residual risk on a 5x5 matrix, assigns SMART actions with named role owners and
  dates, defers India content to hse-india, and de-identifies COSS / Sentinel / lookout
  role-holders to role labels. Decision-support only; a competent person must review
  the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: risk-assessment
  tier: 2
  audience:
  - M
  - C
  industry:
  - Gen
  jurisdiction:
  - UK
  status: stable
  plugin: hse-rail
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Level Crossing Track Worker Safety

The **hse-rail safe-system-of-work builder** — given a **named level crossing** or a **named on/near-the-line work site** (a possession, a worksite, a section of track), it produces a specific, defensible safe-system-of-work artifact whose **primary controls sit at the higher orders of two engineered hierarchies**, not at signage or a lookout.

**Level-crossing risk is led by the remedial hierarchy** — **closure → grade separation → engineering (barriers / obstacle detection / MSL / full-barrier) → sighting / signage / administrative LAST**. A crossing "controlled" with new signage while closure, grade separation, or engineering is reasonably practicable is exactly the indefensible paperwork this skill rejects (`KB-SNIP-LX-HIERARCHY`).

**Track-worker risk is led by the protection hierarchy** — **separation (green-zone working / line blockage / possession) → safe systems of work → warning (TOWS / other warning systems) → lookout-only LAST**. Lookout-only (red-zone) working is the *last resort*, never the lead control where separation is reasonably practicable; red-zone working is minimised.

**It RECORDS the user's ALCRM band — it never invents or recomputes it.** The All Level Crossing Risk Model (ALCRM, RSSB / Network Rail) bands crossings by individual + collective risk; the **band threshold values are the licensed model output** (`KB-DATA-ALCRM-BANDS`). This skill **records the user's supplied band** to prioritise remediation and leaves a missing band as `[GAP]` — it **never hard-codes ALCRM thresholds and never computes a band**. The remedial hierarchy still applies even when the band is `[GAP]`.

It grounds the two hierarchies, the COSS role and Sentinel competence framing in `KB-REG-LX-TRACKWORKER`, scores residual risk on the 5×5 matrix, assigns SMART corrective actions with named **role** owners and due dates, defers India statutory content to the `hse-india` engine (mandatory state detection; no national form invented), and **de-identifies COSS / Sentinel / lookout role-holders to role labels** in any distributed copy. Decision-support only; a competent person must review the output.

## When to use this skill

Use this skill when the user needs a **level-crossing risk-and-remediation assessment** or a **track-worker (on or near the line) safe-system-of-work** for a named crossing or work site. Trigger phrases: "assess the risk at our [named] level crossing", "what controls for this crossing", "build the safe system of work for this possession / track renewal", "plan protection for the gang working on this section", "we have an ALCRM band for this crossing — what next", "track-worker safety for [named] worksite". If the request is vague ("sort out level-crossing safety"), the Workflow intake forces a named crossing/work site, the activity, and the protection arrangement before any drafting. This skill **owns level crossings + track-worker safety**; the rail Safety Management System is built by **`rail-safety-management-system`** (RAIL-01) and the ROGS application pack by **`safety-authorisation`** (RAIL-02) — they are referenced, not rebuilt here (CONV-12).

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

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/rail-clause-map.md` (`KB-SNIP-RAIL-CLAUSE-MAP`) — it routes the rail bundle's ISO-clause→skill map and the sibling-skill boundaries (**RAIL-03 owns level crossings + track-worker safety**; RAIL-01 owns the SMS; RAIL-02 owns the ROGS application — referenced, never rebuilt). Then apply the two control hierarchies via `../../knowledge-base/prompt-snippets/lx-hierarchy.md` (`KB-SNIP-LX-HIERARCHY`) and resolve the jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| GB / UK (the two hierarchies + COSS / Sentinel framing) | ../../knowledge-base/regulatory/lx-trackworker.md (`KB-REG-LX-TRACKWORKER` — level-crossing remedial hierarchy closure→grade-separation→engineering→signage-last; track-worker hierarchy separation→SSOW→warning→lookout-last; cite NR/L2/OHS/019 + ORR LX guidance + LXRMTK by reference, never reproduce; issue/date is `[ASSUMED A3]` → `[GAP]`/SME-confirmed) + prompt-snippets/lx-hierarchy.md (`KB-SNIP-LX-HIERARCHY`) + prompt-snippets/hierarchy-of-controls.md (`KB-SNIP-HOC`) |
| GB / UK (the ALCRM risk band — RECORD, never recompute) | ../../knowledge-base/data-points/alcrm-bands.md (`KB-DATA-ALCRM-BANDS` — record the user's individual/collective band to prioritise the crossing; band threshold VALUES are the licensed RSSB/NR model output → **never embed, never compute**; a missing band is `[GAP]`) |
| GB / UK (a significant change to a crossing/asset) | ../../knowledge-base/regulatory/csm-ra.md (`KB-REG-CSM-RA` — the significance test + the three risk-acceptance principles + independent AsBo, where altering a crossing is a significant change; change specifics are `[GAP]` until supplied) |
| India (rail) | ../../knowledge-base/regulatory/in-rail.md (`KB-REG-IN-RAIL` — cite the Railways Act 1989 / Commissioner of Railway Safety as framing; **state detection is mandatory**; defer state-specific non-railway-depot statutory content to the `hse-india` engine; **no national form number invented** → `[GAP]`) |
| Unknown | Ask the infrastructure manager / Safety Authority and the jurisdiction before citing any route or regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table lives in **`references/intake.md`** (the
`intake-coverage` manifest + echo-back + refuse-on-vague anchors). Run it one question
at a time, branch on the answers, and **echo the confirmed scope (which task type, the
named crossing/work site, the protection arrangement) back before any analysis**. The
intake captures, at minimum:

1. **Which task?** (MCQ) — (a) level-crossing risk & remediation, (b) track-worker
   (on/near the line) safe system of work, or (c) both. Branch the rest on this answer.
2. **The named crossing / work site** (free-text) — the specific crossing (with its
   type: e.g. user-worked, automatic half-barrier, manually-controlled, footpath) or the
   named possession / worksite / section of track. **Refuse on a generic, unnamed site.**
3. **The activity & the line status** (free-text + MCQ) — what work, and whether trains
   are running during it (the question that drives separation vs warning vs lookout).
4. **The ALCRM band** (free-text, optional) — *if the user has an ALCRM
   individual/collective band from their licensed model output, RECORD it.* If they do
   not, the band is **`[GAP]`** — **never invent or compute one**; the remedial hierarchy
   still applies.
5. **The existing / proposed controls** (free-text) — so the method can test whether the
   lead control is signage-only (crossing) or lookout-only (track work) where a higher
   order is reasonably practicable.
6. **Jurisdiction** (MCQ) — GB → `KB-REG-LX-TRACKWORKER`; India → `KB-REG-IN-RAIL` +
   **mandatory state detection** (defer to `hse-india`, no national form invented).
7. **De-identification & distribution** (MCQ) — whether the output circulates, so
   COSS / Sentinel / lookout role-holders are role-labelled before distribution.

Then walk the **two-hierarchy method** (`references/METHODOLOGY.md`): record the ALCRM
band (or `[GAP]`) → rank every **crossing** control through closure → grade separation →
engineering → signage-last and **reject a signage-led treatment** where a higher order is
reasonably practicable → rank every **track-work** control through separation (green-zone
/ line blockage / possession) → SSOW → warning → lookout-last and **reject a
lookout-only-led system** where separation is reasonably practicable (`controls.py` +
`KB-SNIP-LX-HIERARCHY`) → score residual risk on the 5×5 matrix (`risk_matrix.py`) →
close every `[GAP]` with a SMART action (`smart_actions`) carrying a named **role** owner
and a due date.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output
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

Moderate fan-out (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub any named **COSS / Controller of Site Safety**,
  **lookout**, **PICOP / engineering supervisor**, gang members, and any **Sentinel
  number** into role labels before any analysis. Suppress any sub-5 incident cell on a
  named crossing/corridor (a `<5` cell de-anonymizes the involved person). Returns the
  re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **Crossing-Remediation-Analyst** — for a crossing task, record the user's ALCRM band
  (or `[GAP]` — **never invent/compute**) and rank remediation through closure → grade
  separation → engineering → signage-last (`KB-REG-LX-TRACKWORKER` / `KB-SNIP-LX-HIERARCHY`);
  reject a signage-led treatment where a higher order is reasonably practicable.
  SCOPE-OUT: does not build the rail SMS (RAIL-01) or the ROGS application (RAIL-02).
- **Track-Worker-SSOW-Analyst** — for a track-work task, rank protection through
  separation (green-zone / line blockage / possession) → SSOW → warning → lookout-last;
  reject a lookout-only-led system where separation is reasonably practicable; minimise
  red-zone working. SCOPE-OUT: does not assert an ALCRM band.
- **Drafter** — assemble the safe-system-of-work / crossing-remediation artifact in the
  output format, naming **role** owners (never persons), HoC-ranking every control via
  `controls.py`, scoring residual risk 5×5, and recording `[GAP]` for unsupplied inputs
  (the ALCRM band, the NR/L2/OHS/019 issue/date, site specifics) — never invented.
- **Critic/QA** (MANDATORY) — the level-crossing / track-safety SME persona
  (`references/sme-review.md` / `KB-SNIP-ARCHETYPES`): crossing led by closure/grade-sep
  (not signage), track work led by separation (not lookout-only), the ALCRM band
  **recorded not invented**, no PPE/admin-only mitigation unjustified, citations accurate
  (NR/L2/OHS/019 cited by reference, not reproduced), and ZERO COSS/Sentinel/lookout
  leak. Runs the per-skill SME sign-off checklist (decision-support; precedes — never
  replaces — the human competent-person review).

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
