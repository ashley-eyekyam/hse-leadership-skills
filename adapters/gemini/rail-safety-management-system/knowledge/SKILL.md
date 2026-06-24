---
name: rail-safety-management-system
description: 'Build a ROGS goal-based rail Safety Management System (SMS) to the ROGS/ORR
  element set (policy, accountabilities, risk-control arrangements, CSM-RA change
  interface, competence/Sentinel, asset/ECM maintenance, emergency, monitoring/audit,
  continuous improvement) for a named transport operator or infrastructure manager.
  Use this skill to build or review a rail SMS or structure a ROGS safety-certificate
  / safety-authorisation submission. Grounds elements in KB-REG-ROGS and the change
  interface in KB-REG-CSM-RA, resolves the route first (mainline operator -> safety
  certificate; infrastructure manager -> safety authorisation; non-mainline -> Part
  3 verification), names the accountable duty-holder and safety-critical roles, ranks
  every mitigation through the hierarchy of controls, and de-identifies role-holder
  names / COSS / Sentinel numbers to role labels. The SMS is for-acceptance: it never
  claims it is ''accepted by ORR''. Decision-support only; a competent rail-SMS /
  ORR-aware person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: governance
  tier: 1
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

# Rail Safety Management System

The **hse-rail keystone** — given a named **transport operator** or **infrastructure manager**, it builds a **ROGS goal-based Safety Management System** to the full ROGS/ORR element set: safety policy · accountabilities · risk-control arrangements · the CSM-RA change interface · competence & Sentinel · asset/ECM maintenance · emergency arrangements · monitoring & audit · continuous improvement. Every element grounds in `KB-REG-ROGS` (the Railways and Other Guided Transport Systems (Safety) Regulations 2006); the change-management element grounds in `KB-REG-CSM-RA` (the CSM-RA significance test, the three risk-acceptance principles, and the independent AsBo). It **resolves the dutyholder route first** — a mainline **transport operator** needs a **safety certificate**, an **infrastructure manager** a **safety authorisation**, a **non-mainline** operation (tram / metro / heritage) a **ROGS Part 3 safety verification**. It names the **accountable duty-holder** and the **safety-critical role-holders**, forces operator/operation specificity (a generic "rail SMS" is exactly the indefensible copy-paste output this skill exists to prevent), and ranks every risk-control mitigation through the hierarchy of controls — never a vague, PPE-only treatment.

**For-acceptance, never accepted.** The SMS this skill builds is framed **for submission / for acceptance**. ORR is the **Safety Authority**; acceptance is *its* act. This skill **never states the SMS is "accepted by ORR"** — it would be fabricating the regulator's decision.

## When to use this skill

Use this skill when the user needs a **rail SMS** built or reviewed for a named operator / infrastructure manager, or a **ROGS safety-certificate / safety-authorisation submission** structured to the ROGS/ORR element set. Trigger phrases: "build our rail SMS", "ROGS safety management system", "structure our safety-authorisation submission", "draft our rail safety policy and accountabilities", "align our metro/tram operation to ROGS". If the request is vague ("improve our rail safety"), the Workflow intake forces the named operator, the operation type, and the dutyholder route first. It builds the SMS; the application pack that submits it is the sibling skill **`safety-authorisation`** (RAIL-02), which *references* this SMS rather than rebuilding it (`KB-SNIP-RAIL-CLAUSE-MAP`); level-crossing / track-worker safety is **`level-crossing-track-worker-safety`** (RAIL-03).

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

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/rail-clause-map.md` (`KB-SNIP-RAIL-CLAUSE-MAP`) — it routes the SMS element set, the route test, and the sibling-skill boundaries (RAIL-02 references this SMS; RAIL-03 owns level crossings). Then resolve the dutyholder route + jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| GB / UK (the SMS framework + the route) | ../../knowledge-base/regulatory/uk-rogs.md (`KB-REG-ROGS` — the SMS duties + the safety-certificate / safety-authorisation / Part-3-verification route map) + prompt-snippets/hierarchy-of-controls.md (`KB-SNIP-HOC`) |
| GB / UK (the change-management element) | ../../knowledge-base/regulatory/csm-ra.md (`KB-REG-CSM-RA` — the significance test, the three risk-acceptance principles, the independent AsBo; the live change details are `[GAP]` until supplied) |
| India (rail) | ../../knowledge-base/regulatory/in-rail.md (`KB-REG-IN-RAIL` — cite the Railways Act 1989 / Commissioner of Railway Safety as the framing; **state detection is mandatory**; defer state-specific non-railway-depot statutory content to the `hse-india` engine; **no national form number invented**) |
| Unknown | Ask the operator's Safety Authority / dutyholder type before citing any route or regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the **dutyholder type** (the route-determining
question: mainline transport operator → certificate, infrastructure manager →
authorisation, non-mainline → Part-3 verification), the **named operator + operation
scope**, the **accountable duty-holder + safety-critical role-holders**, the
**build / review / submission** mode, the jurisdiction branch (GB → `KB-REG-ROGS`;
India → `KB-REG-IN-RAIL` + mandatory state detection), and the audience/distribution
gate — lives in **`references/intake.md`** (the `intake-coverage` manifest + echo-back +
refuse-on-vague anchors). Run it one question at a time, branch on the answers, and
**echo the confirmed operator + dutyholder route + accountable duty-holder back before
any drafting**.

Then walk the **ROGS/ORR SMS element set** in order (`KB-REG-ROGS`), recording `[GAP]` for any element the inputs do not supply (never invented):

1. **Safety policy & objectives** — the dutyholder's safety policy and measurable objectives.
2. **Accountabilities & responsibilities** — name the **accountable duty-holder** and the **safety-critical role-holders** (de-identified to role labels; the *role* is filled, never left as a generic heading).
3. **Risk-control arrangements** — the operation's significant risks and their controls; **every mitigation ranked through the hierarchy of controls** via `controls.py` (no PPE/admin-only treatment without an explicit "higher-order not reasonably practicable" justification — the SFAIRP test), residual risk re-scored on the `risk_matrix` 5×5.
4. **CSM-RA change interface** (`KB-REG-CSM-RA`) — the significance test, the three risk-acceptance principles (codes of practice / reference systems / explicit risk estimation), and the **independent AsBo** for significant changes.
5. **Competence & Sentinel** — competence management and fitness-for-duty for safety-critical work (Sentinel where it applies).
6. **Asset & ECM maintenance** — asset/infrastructure condition and Entity in Charge of Maintenance arrangements.
7. **Emergency arrangements** — emergency preparedness and response coordination.
8. **Monitoring, audit & review** — the assurance and audit regime.
9. **Continuous improvement** — how the SMS learns and improves.

Throughout, **resolve the route once and hold it** (certificate / authorisation / Part-3 verification) and keep the framing **for-acceptance** — never write that the SMS is "accepted by ORR". Close any `[GAP]` with a SMART action (`smart_actions`) carrying a named role owner and a due date.

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the element-by-element build + the route logic) is in `references/METHODOLOGY.md`.

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
- **Researcher (element-coverage)** — from the scrubbed inputs, gather the
  operator/operation facts and check the ROGS/ORR SMS element set (`KB-REG-ROGS`) for
  coverage; flag any element with no input as `[GAP]`.
- **Regulatory-Checker (route + CSM-RA)** — resolve the dutyholder route
  (`KB-REG-ROGS`: mainline operator → certificate, infrastructure manager →
  authorisation, non-mainline → Part-3 verification) and confirm the change-management
  element aligns to the CSM-RA significance test + risk-acceptance + AsBo
  (`KB-REG-CSM-RA`); keep the framing **for-acceptance**, **never "accepted by ORR"**;
  India → `KB-REG-IN-RAIL` after state detection, no national form invented. SCOPE-OUT:
  does not draft.
- **Drafter** — assemble the ROGS/ORR SMS element set in the output format, naming the
  accountable duty-holder + safety-critical roles, HoC-ranking every risk-control
  mitigation, tracing every claim to an input. SCOPE-OUT: does not resolve the route or
  the CSM-RA alignment (the Regulatory-Checker owns it).
- **Critic/QA** (MANDATORY) — the rail-SMS persona (`references/sme-review.md` /
  `KB-SNIP-ARCHETYPES`): every element complete, the accountable duty-holder named, the
  route correct, the SMS framed for-acceptance (never "accepted by ORR"), no PPE/admin-only
  mitigation unjustified, and ZERO role-holder / Sentinel-number leak. Runs the per-skill
  SME sign-off checklist (decision-support; precedes — never replaces — the human
  competent-person review).

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
