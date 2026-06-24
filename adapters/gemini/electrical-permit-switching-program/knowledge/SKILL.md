---
name: electrical-permit-switching-program
description: 'Produces a consultant-grade HV/LV switching program (a switching
  schedule + safety-document plan) for named electrical apparatus, driven by the
  de-energize-first hierarchy and the isolation → prove-dead → earthing →
  sanction-to-test discipline. Use this skill whenever a user asks to build a
  switching program or switching schedule, plan an isolation, write a
  permit-to-work or sanction-to-test, take HV/LV equipment to a safe working
  condition and back, or sequence the points of isolation, prove-dead, and
  protective earthing. It refuses to author a program for "the substation" without
  the named apparatus, voltage, and points of isolation/earthing; it records the
  ordered switching sequence with per-step authorisation, gates work behind
  prove-dead AND protective earthing where required (un-proven or un-earthed work is
  flagged), and keeps the sanction-to-test distinct from a work permit. Grounded in
  NFPA 70E Article 120, OSHA 1910.269/.333/.147, and EAWR 1989. Decision-support
  only; a competent person must review.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: process-safety
  tier: 2
  audience:
  - M
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-utilities-power
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Electrical Permit & Switching Program

A consultant-grade, **de-energize-first** switching program for **named electrical apparatus** — a
feeder, busbar section, transformer, ring main unit, or HV/LV switchboard — never a generic "the
substation". Its entire reason to exist is that **safe electrical work leads with isolation and
proof, not with PPE**: every program records the **ordered switching sequence** that takes the
apparatus from energized to a **proven safe working condition** — **isolate → prove dead → earth →
sanction the work via a safety document → restore** — establishing an **electrically safe work
condition** per NFPA 70E **Article 120** before any work begins. **Work authorised on apparatus
that was isolated but not proven dead, or that omits protective earthing where the procedure
requires it, is flagged and pushed up the hierarchy — never accepted as the program.** That is the
failure mode this skill exists to prevent.

It forces the single lever that separates a defensible artifact from copy-paste paperwork: the
**ordered isolation/prove-dead/earthing sequence with per-step authorisation, plus the full
hierarchy of controls**. It **refuses** to author a program for "the substation" without the
**named apparatus + the operating voltage + the points of isolation/earthing**, and it keeps the
**sanction-to-test** (controlled re-energization for testing) **distinct from a permit-to-work**
(work on dead equipment) — conflating the two is a document-discipline failure. Grounded in **NFPA
70E Article 120** (establishing + verifying an electrically safe work condition) read with **Annex
K** and **120.5** (the process for establishing an ESWC), **OSHA 29 CFR 1910.269** (T&D —
lockout/tagout 269(d), protective grounding 269(n)) + **1910.333** (selection and use of work
practices) + **1910.147** (the LOTO standard), and **EAWR 1989 regs 12–13** (means of cutting off
supply / isolation + working dead) read with **HSG85** (electricity at work — safe working
practices). Decision-support only; a competent person (authorised/senior authorised person) must
review the output.

## When to use this skill

Use this skill when the user needs a **switching program for concrete electrical apparatus** —
for example "build the switching program to take the 11 kV feeder F2 to RMU-3 dead for cable
work", "write the isolation and prove-dead sequence for the transformer TX-1 secondary",
"sequence the points of isolation and earthing for busbar section B at the main switchboard", or
"prepare a sanction-to-test for commissioning the new protection relay". It is **not** for a
generic "how do I isolate equipment?" answer: the Workflow intake below forces the named
apparatus, the operating voltage, and the points of isolation/earthing before any drafting,
refuses a vague "the substation" request, and refuses a program that would authorise work without
prove-dead and (where required) protective earthing.

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
| Switching / isolation discipline (every run) | ../../knowledge-base/prompt-snippets/switching-sequence.md (KB-SNIP-SWITCHING-SEQUENCE) — the **ordered isolation → prove-dead → earthing → sanction-to-test → restore** sequence; carries the full isolation / point-of-isolation / lock-off / prove-test-prove / protective-earthing / permit-to-work / sanction-to-test vocabulary, so this skill needs **no** separate electrical-isolation fragment; working un-proven or un-earthed where required is **rejected** |
| Electrical control spine (every run) | ../../knowledge-base/prompt-snippets/deenergize-first.md (KB-SNIP-DEENERGIZE-FIRST) — the **de-energize-first / ESWC** spine: establish an electrically safe work condition (NFPA 70E Article 120) BEFORE any reliance on PPE; a PPE-led or convenience-led treatment is rejected |
| Electrical safe-working duty (every run) | ../../knowledge-base/standards/nfpa-70e.md (KB-STD-NFPA70E) — the copyright-safe NFPA 70E **Article 120** (establishing + verifying an electrically safe work condition) + Annex K + 120.5 clause→artifact structure map (cite the clause/article numbers only — never the table cells) |
| Utilities clause cross-walk | ../../knowledge-base/prompt-snippets/utilities-clause-map.md (KB-SNIP-UTILITIES-CLAUSE-MAP) — the bundle-shared NFPA 70E Article 120 + 130.4 + 130.5 cross-walk that keeps the three hse-utilities-power skills consistent on de-energize-first |
| USA | ../../knowledge-base/regulatory/osha-1910-269.md (KB-REG-OSHA1910-269) — US duty: OSHA 29 CFR **1910.269** (T&D — **269(d)** lockout/tagout, **269(n)** protective grounding, 269(m) de-energizing lines and equipment) read with **1910.333** (selection and use of work practices) + **1910.147** (the LOTO standard) |
| UK / EU | ../../knowledge-base/regulatory/uk-eawr.md (KB-REG-UK-EAWR) — **EAWR 1989 regs 12–13** (means of cutting off supply + isolation / working on or near dead conductors) read with **HSG85** (electricity at work — safe working practices) |
| India | ../../knowledge-base/regulatory/in-electrical.md (KB-REG-IN-ELECTRICAL) — India CEA / state electricity rules + line-clearance / permit practice; **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and leads every program with the
**de-energize-first spine** `KB-SNIP-DEENERGIZE-FIRST` (establish an ESWC per NFPA 70E Article 120
before any work), drives the **ordered switching sequence** — isolate → prove dead → earth →
sanction → restore — through `KB-SNIP-SWITCHING-SEQUENCE` (which carries the isolation / prove-dead
/ earthing / sanction-to-test vocabulary, so no separate isolation fragment is referenced), grounds
the Article 120 ESWC duty on `KB-STD-NFPA70E`, and aligns with the other hse-utilities-power skills
through `KB-SNIP-UTILITIES-CLAUSE-MAP`. The US duty is `KB-REG-OSHA1910-269` (269(d)/(n)) + 1910.333
+ 1910.147; the UK leg is `KB-REG-UK-EAWR` (regs 12–13 + HSG85). **Work authorised without
prove-dead, or omitting protective earthing where the procedure requires it, is rejected by the
`controls` gate, never accepted as the program.** For an India site, resolve the state via
`hse-india` (**mandatory state detection**) and emit a literal `[GAP]` where a state return is owed
— never a minted national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the switching intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to author a program for "the substation": you need the named
apparatus + the operating voltage + the points of isolation/earthing before any drafting. Refuse a
program that would authorise work without prove-dead and (where required) protective earthing.**

1. **The named apparatus** (free-text — the specificity anchor) — "Name the exact apparatus +
   type (feeder / busbar section / transformer / ring main unit / switchboard) + operating voltage
   + function (e.g. '11 kV feeder F2 to RMU-3, ring main'). **Refuse 'the substation' / 'the
   switchroom' — the program is apparatus-specific.**"
2. **Operating voltage & system** (mcq) — LV (≤1 kV) / HV 11 kV / HV 33 kV / HV other / mixed.
   **The voltage drives the approach distances, the earthing requirement, and the authorisation
   level (authorised vs senior authorised person).**
3. **Points of isolation & earthing** (free-text — the program backbone) — "List every point of
   supply / isolation for this apparatus and where protective earthing will be applied. **A program
   that cannot enumerate its points of isolation is refused; working un-earthed where the procedure
   requires earthing is a flagged failure.**"
4. **Work activity & document type** (mcq) — work on dead equipment (**permit-to-work**) /
   controlled re-energization for testing (**sanction-to-test**) / both. **The sanction-to-test is
   kept DISTINCT from a permit-to-work — conflating the two is a document-discipline failure.**
5. **De-energization decision** (mcq — asked among the controls) — work the apparatus **dead**
   (de-energize + establish an ESWC per Article 120; the default) / **live work** (**branch to Q5a
   justification**). **De-energization + isolation is the primary control, not an afterthought.**
6. **Jurisdiction** (mcq) — USA / UK / EU / India / Other / Unknown. **India → resolve the state
   via `hse-india` (mandatory state detection); emit `[GAP]`, never a national form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts
back and confirm** before any analysis. Never proceed on a vague or missing input — a missing
input is a `[GAP]`, never an invented isolation point or earthing claim.

Then: record the **de-energization decision first** (`KB-SNIP-DEENERGIZE-FIRST`); build the
**ordered switching sequence** — isolate → prove dead → earth → sanction the work via the correct
safety document → restore — per `KB-SNIP-SWITCHING-SEQUENCE`, with **per-step authorisation**; run
the `controls` hierarchy gate (de-energize + isolate → prove dead → earth → safety document → PPE
last — a program that authorises work un-proven/un-earthed, or that conflates sanction-to-test with
a work permit, is a FLAG pushed up the hierarchy) → frame the qualitative residual via
`risk_matrix` → make every action a SMART action via `smart_actions` → validate the draft against
`references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The
domain method is in `references/METHODOLOGY.md`.

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

For a multi-apparatus switching program the triage gate fans out to (the **De-identifier runs
FIRST — sequential dependency**; everything below consumes only its scrubbed output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier (esp. a **named operator
  from a prior switching / electrocution / arc-flash incident**) to role labels before any
  analysis; return the re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **De-energization-&-Isolation-Analyst** — runs **before** the sequence is sanctioned so the
  program is de-energize-led: record the **Article 120 ESWC decision** (`KB-SNIP-DEENERGIZE-FIRST`)
  and enumerate every **point of isolation** for the named apparatus; where live work is proposed,
  capture the justification (OSHA 1910.333 / EAWR — a bare convenience reason is REJECTED).
  SCOPE-OUT: does not build the ordered switching steps (the Switching-Sequence-Author owns it) or
  de-identify (the De-identifier).
- **Switching-Sequence-Author** — build the **ordered switching sequence** per
  `KB-SNIP-SWITCHING-SEQUENCE`: isolate → **prove dead** (prove-test-prove) → **earth** (protective
  earthing/grounding where required) → issue the correct **safety document** (permit-to-work for
  dead work; **sanction-to-test** kept DISTINCT for controlled re-energization) → restore, with
  **per-step authorisation** (authorised vs senior authorised person by voltage). SCOPE-OUT: does
  not rank the residual controls (the Controls-&-Document-Author) or check the law (the SME persona).
- **Controls-&-Document-Author** — rank the controls up the hierarchy (de-energize + isolate →
  prove dead → earth → safety-document control → PPE last) via the **`controls` engine** — a
  program that authorises work **un-proven or un-earthed where earthing is required**
  (`ppe_admin_only=True` / lower-order-only) is a **FLAG pushed up the hierarchy, never the
  program**; keep the **sanction-to-test distinct from a permit-to-work**; re-frame the residual via
  `risk_matrix`. SCOPE-OUT: does not de-identify or build the raw sequence steps.
- **Critic/QA** (MANDATORY) — adversarial final pass: the de-energization/isolation decision is
  recorded BEFORE work, every work step is gated behind **prove-dead AND protective earthing** where
  the procedure requires it, the **sanction-to-test is not conflated with a permit-to-work**, the
  Article 120 ESWC sequence + the 1910.269 / EAWR grounding are cited correctly, every action is
  owned and dated, and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the de-energization /
isolation decision, the ordered switching sequence (`KB-SNIP-SWITCHING-SEQUENCE`), the A7
`controls` / `risk_matrix` / `smart_actions` calls inline, then the mandatory Critic/QA + SME pass —
same scope discipline, no subagents.

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
