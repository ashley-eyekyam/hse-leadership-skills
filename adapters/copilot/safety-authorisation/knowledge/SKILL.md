---
name: safety-authorisation
description: Assemble a ROGS safety-authorisation (or safety-certificate) application
  pack for submission to the Office of Rail and Road (ORR), drawing on an existing
  rail Safety Management System rather than rebuilding it. Use this skill to structure
  and gap-check a ROGS application for a named infrastructure manager or transport
  operator. It resolves the dutyholder route first (infrastructure manager -> safety
  authorisation; mainline transport operator -> safety certificate; non-mainline ->
  Part-3 verification), references the SMS from the sibling skill rail-safety-management-system
  (RAIL-01) as an input, grounds the pack in KB-REG-ROGS and KB-REG-CSM-RA, names
  the accountable duty-holder and safety-critical roles, ranks mitigations through
  the hierarchy of controls, records [GAP] for unsupplied elements, and de-identifies
  role-holder names / Sentinel numbers to role labels. The pack is for-submission
  and never claims it is 'authorised by ORR'. Decision-support only; a competent person
  must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: governance
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

# Safety Authorisation

The **hse-rail application assembler** — given a named **infrastructure manager** (or **transport operator**) and its existing **rail Safety Management System**, it assembles a **ROGS application pack for submission to ORR**: the safety-authorisation / safety-certificate application that the dutyholder files with the **Office of Rail and Road (ORR)**. It **resolves the dutyholder route first** — an **infrastructure manager** files a **safety authorisation**, a mainline **transport operator** a **safety certificate**, a **non-mainline** operation (tram / metro / heritage) a **ROGS Part 3 safety verification**. It grounds the application duties in `KB-REG-ROGS` and the change-management evidence in `KB-REG-CSM-RA` (the significance test, the three risk-acceptance principles, the independent AsBo), names the **accountable duty-holder** and the **safety-critical role-holders**, ranks every risk-control mitigation through the hierarchy of controls (never a vague, PPE-only treatment), and records `[GAP]` for any application element the inputs do not supply.

**It references the SMS — it never rebuilds it.** The full ROGS/ORR Safety Management System is built by the sibling skill **`rail-safety-management-system`** (RAIL-01). This skill takes that SMS as an **input** and assembles the *application pack that submits it* — it must **never re-author or regenerate the SMS element set** (`KB-SNIP-RAIL-CLAUSE-MAP`; CONV-12). If the SMS does not yet exist, it points the user to RAIL-01 and records the SMS as a `[GAP]` input rather than building one.

**For-submission, never authorised.** The pack this skill builds is framed **for submission**. ORR is the **Safety Authority**; granting the safety authorisation / certificate is *its* act. This skill **never states the application is "authorised / accepted / approved / granted by ORR"** — it would be fabricating the regulator's decision.

## When to use this skill

Use this skill when the user needs a **ROGS safety-authorisation or safety-certificate application pack** structured and assembled for submission to ORR for a named dutyholder. Trigger phrases: "assemble our safety-authorisation application", "structure our ORR safety-certificate submission", "put together our ROGS application pack", "gap-check our safety authorisation before we submit", "what do we file with ORR as an infrastructure manager". If the request is vague ("sort out our ORR submission"), the Workflow intake forces the named dutyholder, the dutyholder route, and whether the SMS already exists, before any drafting. This skill **assembles the application**; the underlying SMS is built by **`rail-safety-management-system`** (RAIL-01), which this skill *references* rather than rebuilds; level-crossing / track-worker safety is **`level-crossing-track-worker-safety`** (RAIL-03).

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

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/rail-clause-map.md` (`KB-SNIP-RAIL-CLAUSE-MAP`) — it routes the application route test and the sibling-skill boundaries (**RAIL-02 references RAIL-01's SMS, never rebuilds it**; RAIL-03 owns level crossings). This skill mints **no unique new KB** — it reuses the rail bundle's existing fragments. Then resolve the dutyholder route + jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| GB / UK (the application route + the SMS duties it references) | ../../knowledge-base/regulatory/uk-rogs.md (`KB-REG-ROGS` — the safety-certificate / safety-authorisation / Part-3-verification route map + the SMS duties the application packages) + prompt-snippets/hierarchy-of-controls.md (`KB-SNIP-HOC`) |
| GB / UK (the change-management evidence in the pack) | ../../knowledge-base/regulatory/csm-ra.md (`KB-REG-CSM-RA` — the significance test, the three risk-acceptance principles, the independent AsBo; live change details are `[GAP]` until supplied) |
| India (rail) | ../../knowledge-base/regulatory/in-rail.md (`KB-REG-IN-RAIL` — cite the Railways Act 1989 / Commissioner of Railway Safety as the framing; **state detection is mandatory**; defer state-specific non-railway-depot statutory content to the `hse-india` engine; **no national form number invented**) |
| Unknown | Ask the operator's Safety Authority / dutyholder type before citing any route or regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the **dutyholder type** (the route-determining
question: infrastructure manager → **safety authorisation**; mainline transport operator →
**safety certificate**; non-mainline → **Part-3 verification**), the **named dutyholder +
operation scope**, **whether the rail SMS already exists** (the input this skill references,
built by RAIL-01 — if absent, route to RAIL-01 and record `[GAP]`), the **accountable
duty-holder + safety-critical role-holders**, any **significant change** (the CSM-RA evidence
limb), the jurisdiction branch (GB → `KB-REG-ROGS`; India → `KB-REG-IN-RAIL` + mandatory
state detection), and the submission-status / audience gate — lives in **`references/intake.md`**
(the `intake-coverage` manifest + echo-back + refuse-on-vague anchors). Run it one question
at a time, branch on the answers, and **echo the confirmed dutyholder + route + the SMS-input
status back before any assembly**.

Then walk the **ROGS application-pack assembly** (`references/METHODOLOGY.md`): confirm the
route → confirm the referenced SMS as an input (never rebuild it) → assemble the application
elements (applicant identity & route declaration, the SMS reference + scope, the
risk-control summary with every mitigation HoC-ranked via `controls.py`, the CSM-RA
change-evidence where there is a significant change, competence/Sentinel & ECM assurance,
the declaration), recording `[GAP]` for any element the inputs do not supply (never invented)
and closing each `[GAP]` with a SMART action (`smart_actions`) carrying a named role owner
and a due date. **Hold the for-submission framing throughout — never write that the
application is "authorised / accepted by ORR".**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the route logic + the references-not-rebuilds-SMS discipline + the application element set) is in `references/METHODOLOGY.md`.

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

- **De-identifier** — runs FIRST; scrub any named individuals (the accountable
  duty-holder, safety-critical role-holders, COSS, and any Sentinel number) into role
  labels before any analysis. Returns the re-identification key SEPARATELY to the
  orchestrator, never to a sibling.
- **Regulatory-Checker (route + CSM-RA)** — resolve the dutyholder route
  (`KB-REG-ROGS`: infrastructure manager → authorisation, mainline transport operator →
  certificate, non-mainline → Part-3 verification) and confirm the change-evidence limb
  aligns to the CSM-RA significance test + risk-acceptance + AsBo (`KB-REG-CSM-RA`); keep
  the framing **for-submission**, **never "authorised by ORR"**; India → `KB-REG-IN-RAIL`
  after state detection, no national form invented. SCOPE-OUT: does not draft.
- **SMS-Reference-Recorder** — records the **existing rail SMS as an INPUT** to the
  application, citing where each application claim draws on it. SCOPE-OUT: **must NOT
  rebuild or regenerate the SMS element set** — that is `rail-safety-management-system`
  (RAIL-01)'s artifact (CONV-12); if the SMS does not exist, record it as a `[GAP]` and
  route the user to RAIL-01.
- **Drafter** — assemble the ROGS application elements in the output format, naming the
  accountable duty-holder + safety-critical roles, HoC-ranking every risk-control summary
  mitigation, tracing every claim to a supplied input or the referenced SMS, recording
  `[GAP]` for unsupplied elements. SCOPE-OUT: does not resolve the route (the
  Regulatory-Checker owns it) and does not rebuild the SMS (the SMS-Reference-Recorder
  owns the input).
- **Critic/QA** (MANDATORY) — the rail-ORR-submission persona (`references/sme-review.md` /
  `KB-SNIP-ARCHETYPES`): the route correct, the SMS **referenced not rebuilt**, the pack
  framed for-submission (never "authorised by ORR"), no PPE/admin-only mitigation
  unjustified, and ZERO role-holder / Sentinel-number leak. Runs the per-skill SME sign-off
  checklist (decision-support; precedes — never replaces — the human competent-person
  review).

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
