---
name: hse-policy-generator
description: Produces a top-management-signed ISO 45001:2018 clause-5.2 OH&S policy
  for a named organisation, with all five mandatory clause-5.2 commitments, context-fit
  to the org's actual risks and scale (never boilerplate). Use this skill whenever
  a user asks to write, draft, generate, or review an OH&S / health-and-safety policy,
  a safety policy statement, an environmental (ISO 14001 5.2) or psychosocial (ISO
  45003) policy, or a top-management policy commitment. It runs a structured intake,
  refuses a generic boilerplate policy that names no real risk, assembles the five
  mandatory commitments (objectives framework, legal+other requirements, eliminate
  hazards/reduce risk via the hierarchy of controls, continual improvement, worker
  consultation/participation), defers the India statutory written-policy duty to hse-india
  (state detection first, no national-form minting), and emits a documented, communicated,
  top-management-signed policy as a branded report. Decision-support only; a competent
  person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: governance
  tier: 2
  audience:
  - M
  - C
  - E
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-leadership
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# HSE Policy Generator

A consultant-grade HSE skill that produces a **top-management-signed ISO 45001:2018
clause-5.2 OH&S policy** for a **named organisation**, grounded in **ISO 45001:2018
clause 5.2** (the OH&S-policy requirement) and its variants (**ISO 14001:2015 clause 5.2**
environmental, **ISO 45003:2021** psychosocial). It assembles the **five mandatory
clause-5.2 commitments** (objectives framework · legal + other requirements · eliminate
hazards & reduce risk via the hierarchy of controls · continual improvement · worker
consultation & participation), context-fits **every** commitment to the named org's
**actual risks and scale**, and produces a **documented, communicated, top-management-signed**
policy as a branded report. It forces the single lever that separates a defensible
artifact from copy-paste paperwork: **a generic boilerplate policy that names no real
risk is refused** (the clause-5.2 "appropriate to the purpose, size and context"
anti-boilerplate test), the hazard-elimination commitment is ranked up the full
**hierarchy of controls** (`KB-SNIP-HOC`) — never a PPE-only statement — and a policy
**missing any one of the five mandatory commitments is a `regulatory_citation_accuracy`
HARD-FAIL**. The India statutory written-policy duty **defers to `hse-india`** (CONV-8 —
state detection first, no national-form minting). Decision-support only; a competent
person must review the output, and the signed policy never reads as a final legal document.

## When to use this skill

Use this skill when the user needs to **write, draft, generate, or review an OH&S /
health-and-safety policy** for a **concrete, named organisation** — for example "draft an
ISO 45001 OH&S policy for AcmeCo's two warehouses and a chemical store", "write our
top-management safety policy statement", "review our health-and-safety policy against
clause 5.2", or "produce an environmental (ISO 14001 5.2) / psychosocial (ISO 45003)
policy". Trigger phrases: *OH&S policy, health and safety policy, safety policy statement,
policy commitment, top-management policy, ISO 45001 5.2 policy, environmental policy,
psychosocial policy*. This skill **owns ISO 45001 clause 5.2** in the leadership bundle
(see `KB-SNIP-LEADERSHIP-CLAUSE-MAP`); for clause 5.1 felt-leadership use
`safety-walk-gemba`, for clause 5.4 worker participation use `bbs-program-designer`, and
for clause 9.1 performance evaluation use `leading-lagging-kpi-framework`. If the request
is **vague boilerplate** ("just give me a generic safety policy"), the Workflow intake
below **refuses to draft** until the named organisation, its scale, and its **actual
significant risks** are captured — a template naming no real risk fails the specificity
gate.

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

<!-- The selector ROWS below live BELOW the :end marker: per-skill, presence-only
     (rule-2 presence check, never byte-diffed). This skill is driven by the STANDARD
     SELECTOR (Q1) — ISO 45001/14001/45003 5.2 are jurisdiction-independent management-
     system standards — plus a jurisdiction branch for the statutory written-policy duty.
     rule-9 checks every path/ID resolves against the KB registries. -->

**Always read — the clause-5.2 commitment set + the bundle clause cross-walk:**

- `../../knowledge-base/prompt-snippets/policy-commitments.md` (**KB-SNIP-POLICY-COMMITMENTS**) —
  the **five mandatory clause-5.2 commitments** + the clause-5.2 "appropriate to purpose,
  size and context" characteristics + the variant selector + the anti-boilerplate context-fit
  test. The policy is assembled FROM this fragment; a policy missing any of the five
  commitments fails the citation-accuracy gate. Quote its `source`+`year`.
- `../../knowledge-base/prompt-snippets/leadership-clause-map.md` (**KB-SNIP-LEADERSHIP-CLAUSE-MAP**) —
  the bundle ISO 45001 leadership clause cross-walk (5.1 / 5.2 / 5.4 / 9.1 → owning skill);
  route a user who asks for the wrong artifact for a clause to the owning sibling.
- `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (**KB-SNIP-HOC**) — the
  hazard-elimination/risk-reduction commitment (commitment 3) is phrased through the full
  hierarchy of controls, never a PPE-only or admin-only statement.

**Standard selector (Q1) → read the matching management-system standards fragment:**

| Standard selected (Q1) | Read (the clause-5.2 requirement to build the policy against) |
|---|---|
| ISO 45001 (default — OH&S) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001 — clause 5.2 OH&S policy) |
| ISO 14001 (environmental) | ../../knowledge-base/standards/iso-14001.md (KB-STD-ISO14001 — clause 5.2 environmental policy) |
| ISO 45003 (psychosocial) | ../../knowledge-base/standards/iso-45003.md (KB-STD-ISO45003 — psychosocial policy commitment) |
| Combined | read each selected standards fragment and assemble each policy variant in turn |

**Statutory written-policy duty branch (jurisdiction) — never the body of the policy:**

| Jurisdiction | Read / route |
|---|---|
| UK | ../../knowledge-base/regulatory/uk-hswa.md — HSWA 1974 s.2(3): written policy required at 5+ employees |
| India | **defer to `hse-india`** (CONV-8) — resolve the STATE first; ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) for the routing pointer **only**; **mint NO national-form number** (`[GAP]` when unverified); never hard-blocks |
| USA | ../../knowledge-base/regulatory/us-osha.md — no single federal written-policy mandate; note state-plan variation |
| EU | ../../knowledge-base/regulatory/eu-osh.md — Framework Directive 89/391/EEC policy duty |
| Unknown | Ask before citing any specific statutory written-policy duty |

This skill always grounds the policy in `KB-SNIP-POLICY-COMMITMENTS` (the five clause-5.2
commitments) and references `KB-SNIP-LEADERSHIP-CLAUSE-MAP`; ISO 14001 / ISO 45003 substitute
their own clause-5.2 variant via the Q1 selector. The statutory written-policy duty is a
jurisdiction **branch** (it determines *whether the law compels a written policy*), separate
from the policy content; India **defers to `hse-india`** and **never mints a national form
number**. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table, and
the refuse-on-vague anchors — lives in **`references/intake.md`**. Run it one question at a
time, branch on the answers, **echo the captured facts back before drafting**, and **refuse
to draft** until the policy is anchored to a real organisation and its real risks. Capture:

1. **Standard selector (Q1)** — ISO 45001 (OH&S, default) · ISO 14001 (environmental) ·
   ISO 45003 (psychosocial) · combined → selects the clause-5.2 variant in
   `KB-SNIP-POLICY-COMMITMENTS`.
2. **Named organisation + scale** — the org's legal name, headcount band, number/type of
   sites. (Drives the statutory written-policy branch and the "appropriate to size" test.)
3. **Sector + the org's actual significant risks** — free-text: the **real** hazards this
   organisation carries (e.g. forklift traffic, working at height, hazardous substances,
   driving, psychosocial load). **This is the anti-boilerplate anchor** — every commitment
   is context-fit to these named risks.
4. **Jurisdiction** — for the statutory written-policy duty branch (UK HSWA s.2(3) / India →
   **defer to `hse-india`**, state first, no national-form mint / US / EU). This sits beside
   the policy, never inside it.
5. **Top-management signatory** — the role/title that will sign (clause 5.2 requires
   demonstrated top-management commitment); captured as a **role/title**, never personal data.
6. **Communication + review cadence** — how the policy is documented, communicated, and the
   review cycle.

**Refuse-on-vague GATE:** a request for a "generic safety policy" that names **no real
risk, sector, or scale** is **refused** — the skill elicits the org's actual significant
risks first. A boilerplate policy reciting the five commitments but naming no concrete
hazard fails the specificity gate (record `[GAP]`, never invent a risk).

### The clause-5.2 policy-generation method (ISO 45001 5.2; ISO 14001/45003 via Q1)

Full method in `references/METHODOLOGY.md`; the commitment set is `KB-SNIP-POLICY-COMMITMENTS`.

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). Policy PII surface is **low** (the org and
   signatories are named by role/title, not personal data) — but any personal identifier in
   the supplied context is scrubbed to a role label first.
2. **Resolve the standard + select the variant** — from Q1, read the matching standards
   fragment (`KB-STD-ISO45001` default; `KB-STD-ISO14001` / `KB-STD-ISO45003` via the
   selector) and the matching `KB-SNIP-POLICY-COMMITMENTS` variant.
3. **Assemble the five mandatory clause-5.2 commitments** — the policy **must** include
   commitments to: (1) a **framework for setting OH&S objectives**; (2) **fulfilling legal
   and other requirements**; (3) **eliminating hazards and reducing OH&S risks** (ranked via
   `KB-SNIP-HOC` — never PPE-/admin-only); (4) **continual improvement** of the OH&S
   management system; (5) **consultation and participation of workers** (and their
   representatives where they exist). **A policy missing any one of these five is a
   `regulatory_citation_accuracy` HARD-FAIL** — never silently dropped.
4. **Context-fit every commitment (the anti-boilerplate test)** — tie each commitment to a
   concrete obligation or risk the **named org actually carries** (from Q3). The policy must
   be **appropriate to the org's purpose, size and context** and the specific nature of its
   OH&S risks. A commitment reciting the standard but naming no real hazard is **boilerplate**
   and is flagged — re-anchor it to a named risk.
5. **Apply the clause-5.2 characteristics** — the policy is **documented information**,
   **communicated** within the organisation, **available to interested parties**, and
   **signed by top management** (the captured signatory role) — clause 5.2 requires
   demonstrated top-management commitment.
6. **Resolve the statutory written-policy branch (beside the policy)** — for the resolved
   jurisdiction, note whether the law compels a written policy (UK HSWA s.2(3) at 5+
   employees, etc.). For **India**, **defer to `hse-india`** (CONV-8): resolve the **state
   first**, route via the `hse-india` engine; **mint NO national-form number** (`[GAP]` when
   unverified). This never hard-blocks the policy.
7. **Validate against `references/QUALITY_CHECKLIST.md`** — all five commitments present;
   every commitment context-fit to a named org risk (no boilerplate); the hazard-elimination
   commitment ranked up the hierarchy of controls; signed by top management; the standard
   citation traced to the KB (no invented clause); India deferral with no minted form; de-id
   applied; and the output framed as decision-support — never reading as a final legal
   document.
8. **Assemble the branded report** — build `report.json` (see `assets/report.json`) and run
   the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. **Policy generation is a structured composition
over the clause-5.2 commitment set, not a calculation — there is no scoring engine.**

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

This is the **moderate roster** (A6 "moderate = 2–3"): a single policy assembles from one
commitment set, so the triage gate fans out only when the inputs warrant it (e.g. a
multi-standard combined policy, or a jurisdiction branch that needs the `hse-india` cross-call).
The **De-identifier is the sequential first gate**; the **Commitment-Assembler** drafts the
five commitments context-fit to the org's risks; the **Statutory-Branch Resolver** handles the
written-policy-duty branch (the India `hse-india` cross-call); **SME Reviewer** and **Critic/QA**
are mandatory. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub any personal
  identifier in the supplied context to a role/title label before drafting (policy PII surface
  is low — the org and signatories are named by role/title, never personal data). Everything
  below consumes scrubbed text only.
- **Commitment-Assembler** — assemble the **five mandatory clause-5.2 commitments** from
  `KB-SNIP-POLICY-COMMITMENTS`, **context-fit each to the named org's real risks** (Q3), phrase
  the hazard-elimination commitment via `KB-SNIP-HOC`, and apply the clause-5.2 characteristics
  (documented · communicated · top-management-signed). SCOPE-OUT: the statutory written-policy
  branch (the Statutory-Branch Resolver owns it), the de-id scrub (the De-identifier owns it).
- **Statutory-Branch Resolver** — for the resolved jurisdiction, determine whether the law
  compels a written policy (UK HSWA s.2(3), etc.); for **India**, **defer to `hse-india`**
  (CONV-8 — resolve the STATE first, route via the `hse-india` engine, **mint NO national-form
  number**, `[GAP]` when unverified). SCOPE-OUT: the policy content (the Commitment-Assembler
  owns it); never minting a form number.
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (Senior HSE Manager / Director) before any output: all five
  commitments present, every commitment context-fit (not boilerplate), the hazard-elimination
  commitment ranked up the hierarchy of controls, signed by top management, India deferral with
  no minted form, and the signed policy never reading as a final legal document.
- **Critic/QA** (MANDATORY) — all five clause-5.2 commitments present (a missing commitment is a
  `regulatory_citation_accuracy` hard-fail), every commitment context-fit to a named org risk
  (no boilerplate), no PPE-/admin-only hazard-elimination commitment, the standard citation
  traces to the KB (no invented clause), no minted India national form, zero PII leak. PASS/FAIL.

For a single-standard policy for one named organisation the skill runs **single-threaded** —
no fan-out — but the de-id scrub, the five-commitment assembly, the context-fit test, and the
SME + Critic/QA passes are still made. The roster never exceeds MAX=6.

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
