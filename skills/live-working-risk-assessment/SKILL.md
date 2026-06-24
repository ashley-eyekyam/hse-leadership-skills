---
name: live-working-risk-assessment
description: 'Produces a consultant-grade live-working (energized-work) risk
  assessment and statutory justification for a named task on or near energized
  conductors, driven by the de-energize-first default and the EAWR reg-14 / OSHA
  1910.333(a)(2) three-part live-working test. Use this skill when a user asks to
  assess live or energized electrical work, justify working live, build an
  energized electrical work permit, or set the approach boundaries near live
  conductors. It applies the de-energize-first default (an ESWC, NFPA
  70E Article 120 first), forces the statutory test (unreasonable to be dead +
  reasonable to work live + suitable precautions), states the approach distances
  (NFPA 70E 130.4), keeps arc-rated PPE last, and cross-references the arc-flash
  incident energy from arc-flash-assessment without recomputing it. It refuses a
  convenience justification and emits a branded NFPA 70E Annex J energized-work
  permit. Grounded in NFPA 70E, OSHA 1910.333, EAWR 1989 reg 14. Decision-support
  only; a competent person must review.'
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
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-utilities-power
  bundled_in:
  - hse-renewables
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Live-Working Risk Assessment

A consultant-grade, **de-energize-first** live-working (energized-work) risk assessment for a
**named task on or near energized conductors** — a specific live LV/HV apparatus, a defined work
activity, and an operating voltage — never a generic "work near the live parts". Its entire reason
to exist is that **safe electrical work leads with de-energization and a statutory justification,
not with PPE**: the default is to establish an **electrically safe work condition** (NFPA 70E
**Article 120** / EAWR dead-working) and **only if dead working is genuinely not reasonable** is
live work permitted — and then **only** when the **three-part statutory test** holds (it is
*unreasonable to work dead* + *reasonable to work live* + *suitable precautions are taken*). **A
live-working plan justified by convenience, cost, or schedule ("production cannot stop / it's
quicker"), or one whose only control is "arc-rated PPE" with no de-energization evaluation, is
flagged and pushed up the hierarchy — never accepted as the assessment.** That is the failure mode
this skill exists to prevent.

It forces the single lever that separates a defensible artifact from copy-paste paperwork: the
**recorded de-energization decision + the statutory live-working justification + the defined
approach boundaries, inside the full hierarchy of controls**. It **refuses** to assess "work near
the live parts" without the **named task + the live conductors/apparatus + the operating voltage**,
records the justification verbatim as the spine of the artifact, defines the **limited and
restricted approach boundaries** (shock — NFPA 70E 130.4), and **cross-references the arc-flash
incident energy + PPE category computed by `arc-flash-assessment`** at the working position (it
**never re-derives** the cal/cm² figure — that computation is owned by the arc-flash engine).
Grounded in **NFPA 70E (2024)** 110.5/130.2 (energized-work justification + permit), **130.4**
(shock risk assessment + approach boundaries), **130.2(B) / Annex J** (the energized electrical work
permit), and **Article 120** (the de-energize-first ESWC default), read with **OSHA 29 CFR
1910.333(a)(2)** (the de-energize-first rule + the additional-hazard/infeasibility justification) +
**1910.269** (T&D minimum approach distances), and **EAWR 1989 reg 14** (the three-part live-working
test) + **HSG85** + **HSR25**. Decision-support only; a competent person must review the output and a
competent authority must sanction any live work.

## When to use this skill

Use this skill when the user needs a **live-working risk assessment for a concrete energized task** —
for example "assess and justify live thermographic survey on the energized LV switchboard SB-2",
"build the energized electrical work permit for protection-relay testing on the 11 kV panel",
"set the limited and restricted approach boundaries for work near the live busbar at MCC-4", or
"evaluate whether the proposed live work on feeder F1 can be done dead instead". It is **not** for a
generic "how do I work on live equipment safely?" answer: the Workflow intake below forces the named
task, the live conductors, and the voltage before any drafting, refuses a vague "near the live
parts" request, refuses a live-working justification of convenience, and never reduces the
assessment to "wear the flash suit" — the de-energization decision + the statutory justification
come first, arc-rated PPE is the residual last line.

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
| Live-work justification (every live-work path) | ../../knowledge-base/prompt-snippets/live-work-justification.md (KB-SNIP-LIVE-WORK-JUSTIFICATION) — the **three-part live-working gate** (it is *unreasonable to work dead* + *reasonable to work live* + *suitable precautions are taken*) per **EAWR reg 14** / **OSHA 1910.333(a)(2)** / **NFPA 70E 130.2**; **convenience / cost / "it's quicker" is NOT a justification** — a live-work plan justified by convenience, or with no energized-work permit, is rejected |
| Electrical control spine (every run) | ../../knowledge-base/prompt-snippets/deenergize-first.md (KB-SNIP-DEENERGIZE-FIRST) — the **de-energize-first / ESWC** spine: establish an electrically safe work condition (NFPA 70E Article 120) BEFORE any reliance on arc-rated PPE or approach controls; a PPE-led or convenience-led treatment is rejected |
| Electrical safe-working duty (every run) | ../../knowledge-base/standards/nfpa-70e.md (KB-STD-NFPA70E) — the copyright-safe NFPA 70E **110.5/130.2** (energized-work justification + permit), **130.4** (shock risk assessment + the limited/restricted approach boundaries), **Annex J** (the energized electrical work permit) + **Article 120** clause→artifact structure map (cite the clause/article numbers only — never the table cells) |
| Utilities clause cross-walk | ../../knowledge-base/prompt-snippets/utilities-clause-map.md (KB-SNIP-UTILITIES-CLAUSE-MAP) — the bundle-shared NFPA 70E Article 120 + 130.4 + 130.5 cross-walk that keeps the three hse-utilities-power skills consistent on de-energize-first |
| USA | ../../knowledge-base/regulatory/osha-1910-269.md (KB-REG-OSHA1910-269) — US duty: OSHA 29 CFR **1910.333(a)(2)** (de-energize-first / the additional-hazard-or-infeasible energized-work justification) read with **1910.269** (T&D — **minimum approach distances**, de-energizing, protective grounding) + **1910.147** (the LOTO standard) |
| UK / EU | ../../knowledge-base/regulatory/uk-eawr.md (KB-REG-UK-EAWR) — **EAWR 1989 reg 14** (the three-part live-working test — no work on or near a live conductor unless it is unreasonable to be dead, reasonable to work live, and suitable precautions are taken) read with **HSG85** + **HSR25** (electricity at work — safe working practices, dead-working default, live-working precautions and approach control) |
| India | ../../knowledge-base/regulatory/in-electrical.md (KB-REG-IN-ELECTRICAL) — India CEA / state electricity rules + line-clearance / permit practice; **defers to `hse-india`, mandatory state detection; emit `[GAP]`, never a national form number** |
| Unknown | Ask before citing any specific law |

This skill always grounds in `KB-STD-ISO45001` (6.1.2) and leads every assessment with the
**de-energize-first spine** `KB-SNIP-DEENERGIZE-FIRST` (establish an ESWC per NFPA 70E Article 120
before any live work is even considered), then — **only** if dead working is genuinely not
reasonable — applies the **three-part statutory live-working gate** `KB-SNIP-LIVE-WORK-JUSTIFICATION`
(unreasonable to be dead + reasonable to work live + suitable precautions; **convenience is never a
justification**), grounds the Article 120 / 130.2 / 130.4 duty on `KB-STD-NFPA70E`, and aligns with
the other hse-utilities-power skills through `KB-SNIP-UTILITIES-CLAUSE-MAP`. The US duty is
`KB-REG-OSHA1910-269` (1910.333(a)(2) + 1910.269 approach distances); the UK leg is `KB-REG-UK-EAWR`
(reg 14 + HSG85 + HSR25). **The arc-flash incident energy + PPE category at the working position are
cross-referenced from `arc-flash-assessment` (computed once by its `arcflash.py` engine) — this
skill never re-derives the cal/cm² figure.** A live-work plan justified by convenience, or whose only
control is arc-rated PPE with no recorded de-energization evaluation, is rejected by the `controls`
gate, never accepted as the assessment. For an India site, resolve the state via `hse-india`
(**mandatory state detection**) and emit a literal `[GAP]` where a state return is owed — never a
minted national form number. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

Run the live-working intake one question at a time (full coverage contract + branch map in
`references/intake.md`). **Refuse to assess "work near the live parts": you need the named task +
the live conductors/apparatus + the operating voltage before any drafting. The assessment does not
proceed past the de-energization question (Q2) unless de-energization has been genuinely evaluated;
if live work is proposed, a statutory justification (Q3) is mandatory — and a justification of mere
convenience is REFUSED.**

1. **The named task & live conductors** (free-text — the specificity anchor) — "Name the exact task +
   the live conductors/apparatus + the operating voltage (e.g. 'thermographic survey on the energized
   LV switchboard SB-2, 400 V'). **Refuse 'work near the live parts' / 'a panel' — the assessment is
   task- and conductor-specific.**"
2. **Can the task be done dead?** (mcq — the gate the whole skill turns on; asked **first among the
   controls** because de-energization is the primary control) — **yes → the assessment recommends
   de-energization + an ESWC (Article 120); live work is NOT assessed further** (the default) /
   **no or partly → branch to Q3 the live-working justification.**
3. **Live-working justification** *(only if Q2 ≠ yes — the spine of the artifact)* (free-text) —
   "Justify against the **statutory three-part test**: **EAWR reg 14** — (a) it is *unreasonable to
   be dead* + (b) it is *reasonable to work live* + (c) *suitable precautions* are taken — **or** OSHA
   **1910.333(a)(2)** ('additional/increased hazard or infeasible'). **A bare 'production cannot stop
   / it's quicker' is REFUSED** — economic convenience alone does not justify live work. Record the
   justification verbatim."
4. **Approach distances & precautions** (free-text) — "The working distance vs the **limited and
   restricted approach boundaries** (NFPA 70E 130.4 / 1910.269 approach distances); insulation /
   barriers / insulated tools; the qualified-person & accompaniment requirement; and the **arc-flash
   incident energy + PPE category at the working position — cross-referenced from
   `arc-flash-assessment` (#1)**, never recomputed here. Arc-rated PPE is recorded as the **last**
   precaution, after the higher orders."
5. **Energized-work permit** (mcq) — live work authorised → **an energized-work permit is generated
   (NFPA 70E Annex J content)** carrying the justification, the precautions, the approach boundaries,
   the PPE, and the authorising signature.
6. **Jurisdiction** (mcq) — USA / UK / EU / India / Other / Unknown. **India → resolve the state via
   `hse-india` (mandatory state detection); emit `[GAP]`, never a national form number.**

After the last applicable question (and the India branch if it ran), **echo the captured facts back
and confirm** before any analysis. Never proceed on a vague or missing input — a missing input is a
`[GAP]`, never an invented approach boundary, justification, or arc-flash figure.

Then: record the **de-energization evaluation first** (`KB-SNIP-DEENERGIZE-FIRST`); if live work is
proposed, run the **three-part statutory live-working gate** (`KB-SNIP-LIVE-WORK-JUSTIFICATION` — a
convenience justification is REFUSED); define the **limited/restricted approach boundaries** and
**cross-reference the arc-flash incident energy + PPE category from `arc-flash-assessment`** (no
second computation); run the `controls` hierarchy gate (de-energize → engineer/insulate/barrier →
approach control & qualified persons → arc-rated PPE LAST — a plan whose only control is arc-rated
PPE, or whose justification is convenience, is a FLAG pushed up the hierarchy) → frame the
qualitative residual via `risk_matrix` → make every action a SMART action via `smart_actions` →
assemble the **energized-work permit (Annex J content)** → validate the draft against
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

For a live-working risk assessment the triage gate fans out to (moderate fan-out 2–3; the
**De-identifier runs FIRST — sequential dependency**; everything below consumes only its scrubbed
output):

- **De-identifier** — runs FIRST. Scrub every personal/health identifier (esp. a **named worker from
  a prior contact / electrocution / arc-flash burn incident**) to role labels before any analysis;
  return the re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **De-energization-&-Justification-Analyst** — runs **before** any approach/permit work so the
  assessment is de-energize-led: record the **de-energization evaluation** (`KB-SNIP-DEENERGIZE-FIRST`
  — the ESWC default per Article 120). Where live work is proposed, apply the **three-part statutory
  live-working gate** (`KB-SNIP-LIVE-WORK-JUSTIFICATION` — EAWR reg 14 / OSHA 1910.333(a)(2): it is
  unreasonable to be dead + reasonable to work live + suitable precautions). **A bare convenience
  reason ("production cannot stop / it's quicker") is REJECTED.** SCOPE-OUT: does not set the approach
  boundaries or author the permit (the Approach-&-Permit-Author owns it) or de-identify (the
  De-identifier).
- **Approach-&-Permit-Author** — define the **limited and restricted approach boundaries** (NFPA 70E
  130.4 / 1910.269 approach distances), the precautions hierarchy (insulation / barriers / insulated
  tools / qualified persons), **cross-reference the arc-flash incident energy + PPE category at the
  working position from `arc-flash-assessment` (#1) — never recomputed here**, and assemble the
  **energized-work permit (NFPA 70E Annex J content)** with the justification, the approach
  boundaries, the PPE, and the authorising signature. Run the **`controls` engine** — a plan whose
  only control is arc-rated PPE, or whose justification is convenience (`ppe_admin_only=True` /
  lower-order-only) is a **FLAG pushed up the hierarchy, never the assessment**; re-frame the residual
  via `risk_matrix`. SCOPE-OUT: does not de-identify or re-derive the arc-flash figure.
- **Critic/QA** (MANDATORY) — adversarial final pass: the de-energization decision is recorded BEFORE
  any live-work justification, the statutory three-part test is met (never "for convenience"), the
  approach boundaries are defined, the arc-flash incident energy is **cross-referenced from #1 (not
  invented)**, the energized-work permit carries the justification + precautions + authorising
  signature, arc-rated PPE is the documented LAST line (never the headline), the EAWR reg 14 / OSHA
  1910.333 / NFPA 70E 130.2/130.4/Annex J citations are accurate, every action is owned and dated,
  and ZERO de-identification leak.
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off per `references/sme-review.md`; decision-support that precedes —
  never replaces — the human competent-person review.

**Single-threaded fallback:** run the **De-identifier scrub first**, then the de-energization
evaluation, the three-part live-working gate (`KB-SNIP-LIVE-WORK-JUSTIFICATION`), the approach
boundaries + the arc-flash cross-reference to #1, the A7 `controls` / `risk_matrix` / `smart_actions`
calls inline, then the mandatory Critic/QA + SME pass — same scope discipline, no subagents.

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
