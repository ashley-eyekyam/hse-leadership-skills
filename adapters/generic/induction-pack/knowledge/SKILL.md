---
name: induction-pack
description: Produces a site-specific health-and-safety induction pack for a named
  site, project, or contractor cohort, with a competence-verification record and refresher-tracking
  schedule. Use this skill whenever a user asks to build a site induction, new-starter
  or contractor induction, orientation pack, or onboarding safety briefing for a specific
  location. It grounds the induction in the site's real hazards, emergency arrangements,
  and rules over the mandatory induction baseline (KB-SNIP-INDUCTION-BASELINE); produces
  a delivery pack plus a signed competence-verification record proving each inductee
  understood the content; and schedules refreshers by role-risk — emitted as a branded
  report. A generic induction with no named site or site-specific hazards is refused.
  Decision-support only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: training
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-operations
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Induction Pack

A consultant-grade HSE skill that produces a **site-specific health-and-safety induction pack**
for a **named site, project, or contractor cohort** — grounded in the site's real hazards,
emergency arrangements, and rules over the mandatory induction baseline
(`KB-SNIP-INDUCTION-BASELINE`), framed by **ISO 45001:2018 clauses 7.2 (competence) & 7.3
(awareness)**. It layers the **named site's** specifics onto the baseline (emergency · welfare ·
rules · site-specific hazards · reporting), produces a **competence-verification record** (per
inductee, role-labelled in any widely distributed copy, the verification level set on
`KB-DATA-COMPETENCE-LEVELS`) proving each inductee understood the content, and schedules
**refreshers by role-risk** as dated SMART actions. It forces the single lever that separates a
defensible artifact from copy-paste paperwork: **every induction topic tied to a named site
arrangement, the real site hazards ranked up the full hierarchy of controls, and a verification
record always present** — never a generic, template-only induction, never a PPE-only treatment.
**A generic induction with no named site or site-specific hazards is refused.**

## When to use this skill

Use this skill when the user needs an **induction pack for a concrete, named site, project, or
contractor cohort** — for example "build a site induction for the Tilbury distribution
warehouse", "I need a contractor induction for the crews mobilising to Bravo oil terminal",
"write a new-starter orientation pack for our Pune plant", or "set up the visitor safety
briefing and sign-off for our chemicals site". Trigger phrases: *site induction, new-starter /
contractor / visitor induction, orientation pack, onboarding safety briefing, induction
verification / sign-off record, refresher schedule*. It produces a **delivery pack + a signed
competence-verification record + a refresher schedule** — distinct from `sop-writer` (a
procedure) and `toolbox-talk` (a single pre-task briefing). For the **contractor** cohort it
pulls site-rules + permit-to-work awareness and follows contractor prequalification
(`contractor-prequalification`, #16). If the request is vague ("write me an induction"), the
Workflow intake below **refuses to produce a pack** until the named site + at least the
emergency arrangements + at least one site-specific hazard are captured — a generic induction
is explicitly refused.

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

**Jurisdiction selector (Q5) → read the matching legal-induction-baseline fragment:**

| Jurisdiction | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (Factories Act 1948 s.111A worker right to information; + in-state-forms.md for the user's state — defers to `hse-india`, no national form number minted) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (MHSWR 1999 reg. 10 information for employees + reg. 13 capabilities & training) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (OSH Act s.5(a)(1) General Duty Clause + standard-specific training/orientation duties) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

Always — for every run — also read the shared induction baseline + competence + method snippets
and apply them over the named site's specifics:

- `../../knowledge-base/prompt-snippets/induction-baseline.md` (**KB-SNIP-INDUCTION-BASELINE**) —
  the **mandatory induction-topic baseline** (emergency · welfare · site rules · site-specific
  hazards · incident/concern reporting) the named site's specifics are layered onto; a generic
  induction with no named site/hazards is refused; every induction produces a
  competence-verification record.
- `../../knowledge-base/data-points/competence-levels.md` (**KB-DATA-COMPETENCE-LEVELS**) — the
  shared **4-level competence scale** (aware / trained / competent / expert) with the evidence
  test per level; sets the **verification level** each inductee/role must reach. Quote its
  `source`+`year`.
- `../../knowledge-base/prompt-snippets/ops-clause-map.md` (**KB-SNIP-OPS-CLAUSE-MAP**) — the
  bundle clause cross-walk (induction = ISO 45001 7.3 awareness); routes a user who asks for the
  wrong artifact for a clause to the owning sibling (e.g. competence-matrix → `training-needs-analysis`).
- `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (**KB-SNIP-HOC**) — applied to
  every site-specific hazard's control in the induction (never a PPE-only line) and to the
  refresher schedule's remediation.

This skill always grounds in `KB-STD-ISO45001` (cl. 7.2/7.3) + `KB-SNIP-INDUCTION-BASELINE` +
`KB-DATA-COMPETENCE-LEVELS`, and reads ONE jurisdiction fragment for the legal-induction baseline
(Q5). The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(Q1 **audience** · Q2 **named site** · Q3 **site-specific hazards & arrangements available** ·
Q4 delivery mode · Q5 jurisdiction · Q6 **verification method** · roles/owners · refresher
cadence), the **contractor-cohort branch** (Q1 = contractors → pull site-rules + PTW awareness,
follow `contractor-prequalification` #16), and the **refuse-on-vague anchors** — lives in
**`references/intake.md`**. Run it one question at a time, branch on the answers, **echo the
captured facts back before any drafting**, and **refuse to produce a pack** until the **named
site (Q2) + at least the emergency arrangements + at least one site-specific hazard (Q3)** are
captured — record `[ASSUMPTION]` / `[GAP]`, never emit a generic induction. **A generic
induction with no named site or site-specific hazards is explicitly refused.**

### The site-specific induction-design method (ISO 45001 7.2/7.3)

Full method in `references/METHODOLOGY.md`; the topic baseline is `KB-SNIP-INDUCTION-BASELINE`
and the verification scale is `KB-DATA-COMPETENCE-LEVELS`. Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + De-identifier-first
   orchestration rule). Inductee names belong **only** on the legitimate signed
   competence-verification record; any **widely distributed** copy of the pack uses **role
   labels**, and **no inductee health/medical detail** enters the pack. The de-id block warns
   before any name enters a shared artifact.
2. **Resolve the audience + the named site** — from Q1/Q2; refuse a generic site. The contractor
   cohort (Q1) branches to pull **site-rules + permit-to-work awareness** and follows
   prequalification (`contractor-prequalification`).
3. **Lay the mandatory baseline** — apply `KB-SNIP-INDUCTION-BASELINE`: every induction covers
   **emergency arrangements · welfare & first aid · site rules · site-specific hazards &
   controls · incident/concern reporting**. The baseline is the floor, never the whole pack.
4. **Layer the named site's specifics (the core lever)** — for every baseline topic, tie it to
   **this site's** real arrangement (the named muster point, the actual traffic plan, the real
   permit systems) and each **site-specific hazard to its control ranked via `KB-SNIP-HOC`**
   (Elimination → Substitution → Engineering → Administrative → PPE) — never a generic line,
   never PPE-only without justification. A topic with no named site arrangement is a `[GAP]`.
5. **Build the competence-verification record** — per inductee (role-labelled in any shared
   copy), set the **verification level** required for the role on `KB-DATA-COMPETENCE-LEVELS`
   (aware / trained / competent / expert) and the verification method from Q6 (quiz / supervised
   sign-off / competence demonstration). **An induction with no verification record fails the
   quality gate.**
6. **Schedule refreshers by role-risk** — turn the refresher cadence into **SMART actions** via
   `smart_actions.validate_register` — each with a **named owner + ISO due date** (higher-risk
   roles refresh more often). No anonymous actions, no "ASAP".
7. **Validate against `references/QUALITY_CHECKLIST.md`** — no generic-only content; every topic
   tied to a named site arrangement; the verification record present; de-id applied; every legal
   citation traced to the KB.
8. **Assemble the branded report** — build `report.json` (see
   `assets/induction-pack-report.template.json`) and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The induction is **content assembly, not a
calculation** — `smart_actions` (step 6, the refresher schedule) is the only A7 script call.

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

This is the **single-thread-by-default roster**: a short induction-assembly artifact passes the
Step-0 triage as low-complexity and runs **single-threaded** — no subagents — but the de-id
scrub, the `KB-SNIP-INDUCTION-BASELINE` baseline, the `KB-DATA-COMPETENCE-LEVELS` verification
level, and the SME + Critic/QA passes are still made. It fans out to **2** only for a **large
multi-audience pack** (e.g. permanent + contractor + visitor variants of one site), never
exceeding MAX=6. Archetypes: `KB-SNIP-ARCHETYPES`.

- **Single-threaded by design** — for a single-audience induction the orchestrator does it
  itself: de-identify first, lay the baseline, layer the named site's specifics, build the
  verification record and refresher schedule.
- **De-identifier** (fan-out only) — runs **FIRST** (sequential gate, not a fan-out peer); scrub
  every inductee name, contact, and any health/medical detail to role labels before any
  assembly. Inductee names survive **only** on the legitimate signed verification record; every
  widely distributed copy is role-labelled. The Content-Assembler consumes scrubbed text only.
- **Content-Assembler** (fan-out only) — assemble the per-audience induction pack: the
  `KB-SNIP-INDUCTION-BASELINE` baseline layered with **this named site's** real hazards
  (controls ranked via `KB-SNIP-HOC`), the competence-verification record (level on
  `KB-DATA-COMPETENCE-LEVELS`), and the refresher schedule (`smart_actions`). SCOPE-OUT: de-id
  (the De-identifier owns it), SME sign-off (the SME Reviewer owns it).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (**Site HSE Manager**) before any output: no generic-only
  content, every topic tied to a named site arrangement, the verification record present, no
  inductee health detail or names in a widely distributed copy.
- **Critic/QA** (MANDATORY) — adversarial final pass: no generic-only induction, every
  site-specific hazard's control ranked (no PPE/admin-only without justification), the
  competence-verification record present, every legal-induction citation traced to the KB, zero
  PII/health leak (no inductee name/medical detail in a shared copy, no re-id key in the
  output). PASS/FAIL.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME persona
  sign-off per `references/sme-review.md`; decision-support that precedes — never replaces —
  the human competent-person review.

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
