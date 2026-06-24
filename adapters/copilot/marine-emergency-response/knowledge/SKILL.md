---
name: marine-emergency-response
description: 'Produce a consultant-grade marine/offshore emergency-response (EER)
  plan for a named installation or vessel: muster + persons-on-board (POB) accounting,
  temporary-refuge integrity, the evacuation/escape/rescue hierarchy, TEMPSC/survival-craft,
  man-overboard (MOB) recovery, and helideck. Use this skill to build an offshore
  EER plan, a muster/station bill, a TEMPSC/lifeboat plan, an ERRV/standby-vessel
  or MOB/helideck response, or a temporary-refuge/PFEER plan for a platform, rig,
  FPSO, or support vessel. It builds scenario-keyed responses (muster -> temporary
  refuge -> evacuation -> escape -> rescue), leads with escalation prevention and
  TR integrity rather than ''muster and wait''/abandonment, checks TEMPSC capacity
  against POB (or records [GAP]), and de-identifies the station bill to role labels.
  It is the EER element the sibling offshore-safety-case (MAR-01) records -- cross-referenced,
  not rebuilt. Grounded in PFEER 1995 and SOLAS Chapter III. Decision-support only;
  review by a competent person required.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: emergency
  tier: 2
  audience:
  - M
  - C
  industry:
  - O&G
  jurisdiction:
  - All
  status: stable
  plugin: hse-marine-offshore
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Marine Emergency Response

The **hse-marine-offshore EER builder** — given a **named offshore installation or vessel** and its **persons-on-board (POB)**, it produces a defensible **evacuation, escape and rescue (EER) plan**: the muster + POB accounting, the temporary-refuge (TR) integrity basis, the EER hierarchy (evacuation → escape → rescue), the TEMPSC / survival-craft provision, the man-overboard (MOB) recovery, and the helideck arrangements. It grounds the duties in `KB-REG-PFEER` (muster, TR integrity, the EER chain, reg 17 recovery & ERRV) and the survival-craft / station-bill discipline in `KB-REG-SOLAS-LSA` (TEMPSC, capacity-vs-POB, the role-labelled station bill, OPITO competence), and assigns every person on the station bill an emergency duty by **role label, never by name** in the circulated copy.

**It leads with escalation prevention and temporary-refuge integrity — not "muster and wait".** The primary posture of every EER plan this skill builds is to **detect, control and prevent the emergency from escalating** so abandonment is the last resort, and to **hold the temporary refuge** for its required endurance while the response decision is made (`KB-SNIP-EER-MUSTER`). An EER plan reduced to "muster and abandon", with no escalation-prevention or TR-integrity basis, is the indefensible paperwork this skill rejects. **TEMPSC / survival-craft capacity is checked ≥ POB**; where POB is unsupplied the capacity sufficiency is recorded as a `[GAP]` — never silently assumed adequate.

**This EER plan is the EER element the safety case records — cross-referenced, never rebuilt.** The offshore safety case (the Schedule 6/7 demonstration) is built by the sibling skill **`offshore-safety-case`** (MAR-01). The EER / temporary-refuge plan this skill produces **is** the EER element that safety case records — the two are **cross-referenced and kept distinct, never merged** (`KB-SNIP-MARINE-CLAUSE-MAP`; CONV-12). This skill does not assemble the safety case; it produces the EER plan the safety case points to.

## When to use this skill

Use this skill when the user needs a **marine / offshore emergency-response (EER) plan** for a **named installation or vessel**. Trigger phrases: "build our offshore emergency-response plan", "draft the muster plan / station bill for the platform", "set out our EER strategy", "plan the TEMPSC / lifeboat abandonment", "what are our ERRV / standby-vessel and reg-17 recovery arrangements", "write the man-overboard (MOB) response", "the helideck emergency response", "our PFEER temporary-refuge plan". If the request is vague ("sort out our emergency plan"), the Workflow intake forces the named installation, the POB, and the scenario set before any drafting. This skill produces the **offshore EER plan**; the **offshore safety case** that records this EER element is **`offshore-safety-case`** (MAR-01), which this skill *cross-references* rather than rebuilds; **dropped-objects prevention** is **`dropped-objects-prevention`** (MAR-02).

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

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/marine-clause-map.md` (`KB-SNIP-MARINE-CLAUSE-MAP`) — it routes the marine standard → artifact → owning skill (this skill owns the PFEER muster/TR/EER plan and the SOLAS survival-craft/station-bill limb; **MAR-01 owns the safety case this EER plan supplies, never rebuilt here**; MAR-02 owns dropped objects). Always apply the EER control spine `../../knowledge-base/prompt-snippets/eer-muster.md` (`KB-SNIP-EER-MUSTER`) — escalation-prevention and TR integrity before abandonment — and `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (`KB-SNIP-HOC`) to every control. Then resolve the jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| UK (the offshore EER duty — muster / TR / EER / reg-17 recovery & ERRV) | ../../knowledge-base/regulatory/pfeer.md (`KB-REG-PFEER` — PFEER 1995 (SI 1995/743) + HSE L65: muster + POB accounting, temporary-refuge integrity, the EER chain, detection/firefighting, reg 17 recovery & rescue / ERRV) |
| All (survival craft + station bill — international) | ../../knowledge-base/regulatory/solas-lsa.md (`KB-REG-SOLAS-LSA` — SOLAS Chapter III + LSA Code: TEMPSC types & launch, survival-craft capacity-vs-POB, the role-labelled station bill, drills; OPITO BOSIET/HUET competence requirement, certificate detail `[GAP]`) |
| India (offshore) | ../../knowledge-base/regulatory/in-offshore.md (`KB-REG-IN-OFFSHORE` — OISD / PNG (Safety in Offshore Operations) Rules deferral pointer; **state detection for shore-base activity is mandatory** (CONV-8); defer statutory content to the `hse-india` engine; **no national form number invented**) |
| Unknown | Ask the installation's flag-state / regulatory regime before citing any specific regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the **named installation / vessel + type**
(fixed / floating production / MODU / FPSO / standby vessel) and the **POB** (the
specificity anchor: a generic "the platform" is refused, because the EER strategy
and the survival-craft capacity depend on POB and the installation layout), the
**emergency scenario set** (fire/explosion · loss of well control · gas release ·
helideck emergency · MOB · vessel collision · structural/stability · total loss
requiring abandonment — each keys its own response chain), the **muster + station-bill
+ POB accounting** method, the **EER hierarchy** (TEMPSC capacity vs POB · escape ·
rescue/recovery via ERRV + reg 17), the **temporary-refuge endurance + escalation
control** (the lead posture), the **drills + OPITO BOSIET/HUET competence + helideck**
arrangements, and the jurisdiction branch (UK → `KB-REG-PFEER` + `KB-REG-SOLAS-LSA`;
India → `KB-REG-IN-OFFSHORE` + mandatory state detection) — lives in
**`references/intake.md`** (the `intake-coverage` manifest + echo-back +
refuse-on-vague anchors). Run it one question at a time, branch on the answers, and
**echo the confirmed installation + POB + scenario set back before any drafting**.

Then walk the **offshore EER method** (`references/METHODOLOGY.md`): installation /
POB scoping → the scenario set → muster + station-bill + POB accounting →
**temporary-refuge endurance + escalation control as the lead** (escalation
prevention + maintain-TR via `controls.py` and `KB-SNIP-EER-MUSTER`, **never
"muster and wait" / abandonment-as-headline**) → the EER hierarchy (controlled
**evacuation** with **TEMPSC capacity ≥ POB or a recorded `[GAP]`** → **escape**
secondary means → **rescue & recovery** ERRV / reg-17 / MOB / fast-rescue craft) →
helideck arrangements → the drill schedule + OPITO competence — recording `[GAP]`
for any unsupplied basis (TR endurance, survival-craft capacity, ERRV arrangement)
and closing each `[GAP]` with a SMART action (`smart_actions`) carrying a named role
owner and a due date. **The station bill is role-labelled, never named, in the
circulated copy.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the EER hierarchy + the capacity-vs-POB sufficiency check + the cross-reference to MAR-01's safety case) is in `references/METHODOLOGY.md`.

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

Moderate fan-out for a full-installation EER plan (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub the **station bill** — every named person
  assigned an emergency duty — into **role labels** for the distributed copy, and
  scrub any prior MOB / fatality / abandonment-incident detail referenced for
  context. POB is carried as a **count**, never a named manifest. Returns the
  re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **Scenario-&-Muster-Planner** — assemble the scenario set, the muster stations,
  the station-bill duty assignment (role-labelled), the POB accounting / headcount
  method, and the temporary-refuge endurance basis; flag an unassigned person or an
  unaccounted POB method as a `[GAP]`. SCOPE-OUT: does not author the evacuation /
  rescue hierarchy (the EER-Strategy-Author owns it).
- **EER-Strategy-Author** — author the EER hierarchy with **escalation prevention +
  TR integrity as the lead** (via `controls.py` + `KB-SNIP-EER-MUSTER`), then the
  controlled evacuation (**TEMPSC capacity ≥ POB, or a recorded `[GAP]`** — never
  assumed adequate), escape (secondary means), and rescue & recovery (ERRV / reg-17 /
  MOB / fast-rescue craft), plus the helideck arrangements. SCOPE-OUT: **does not
  rebuild the safety case** — the EER plan it produces is the element MAR-01
  `offshore-safety-case` records (CONV-12); it cross-references, never assembles, the
  safety case.
- **Drill-&-Competence-Author** — the drill schedule (muster / lifeboat / MOB /
  helideck), the OPITO BOSIET/HUET competence baseline (certificate detail `[GAP]`),
  and the owned/dated `[GAP]`-closure actions (`smart_actions`). SCOPE-OUT: does not
  set the EER strategy (the EER-Strategy-Author owns it).
- **Critic/QA** (MANDATORY) — the offshore-EER persona (`references/sme-review.md` /
  `KB-SNIP-ARCHETYPES`): every person has a station-bill duty; POB accounting is
  defined; escalation prevention + TR integrity lead the response (never
  "muster and wait" / abandonment-as-headline); **TEMPSC capacity ≥ POB or a recorded
  `[GAP]`**; rescue & recovery (ERRV / reg 17) present, never assumed; no PPE/admin-only
  control unjustified; and ZERO station-bill name leak into the circulated copy. Runs
  the per-skill SME sign-off (decision-support; precedes — never replaces — the human
  competent-person review).

Simple single-scenario responses (e.g. a standby-vessel MOB recovery) run single-threaded — no subagents.

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
