---
name: traffic-management-plan
description: Produces a construction traffic management plan for a named site — vehicle
  and pedestrian routing, segregation, loading/delivery and reversing controls, and
  the site-access and public-interface arrangements. Use this skill whenever a user
  asks to write or review a traffic management plan, a TMP, a site traffic plan, vehicle-pedestrian
  segregation, or construction logistics/access controls for a specific site. It separates
  people from vehicles by design (one-way systems, segregated routes, eliminating
  reversing), controls deliveries and the public interface, sets speed and signage
  rules, and applies the hierarchy of controls — emitting a branded report. Grounded
  in CDM 2015 Regulation 27 and Schedule 3. Decision-support only; a competent person
  must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 2
  audience:
  - M
  - C
  - F
  industry:
  - Con
  jurisdiction:
  - All
  status: stable
  plugin: hse-construction
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Traffic Management Plan (CDM 2015 Reg 27 + Schedule 3)

A consultant-grade HSE skill that produces a task/site-specific **construction traffic
management plan (TMP)** for a named site, grounded in **CDM 2015 Regulation 27** (organise
the site so pedestrians and vehicles can move safely) and **Schedule 3** (traffic routes —
**suitable, sufficient and separated**, with warning of approach). It plans the vehicle and
pedestrian routing, the **vehicle-pedestrian segregation by design**, the one-way / turning /
reversing controls, the loading & delivery management, the speed / signage rules, and the
public / live-highway interface for the named site. It forces the single lever that separates a
defensible TMP from copy-paste paperwork: a **named site with real access points and named
routes** plus the **segregation-by-design hierarchy** — never a vague plan whose only
pedestrian control is **"hi-vis and a banksman"**.

**Segregation-by-design is the core value.** A pedestrian control of **"hi-vis and a banksman"
with no physical or temporal segregation is flagged PPE/admin-led and pushed up the hierarchy**
(`KB-SNIP-TRAFFIC-SEGREGATION`): **eliminate the conflict / design out reversing → one-way &
turning arrangements → physical segregation (barriers, separated routes) → signage, speed
limits & lighting → a banksman / traffic marshal as the LAST resort**. Controls are ranked via
`KB-SNIP-HOC` and (where the residual conflict needs scoring) the deterministic `controls`
engine. A generic site, an unnamed access point, or **uncontrolled reversing with no Reg 27 /
Schedule 3 grounding** is a **refuse-to-plan** gate, not an assumption — the skill never invents
the site layout.

## When to use this skill

Use this skill when the user needs a **traffic management plan for a concrete, named
construction site** — for example "write a TMP for the Meadowbank Road site: two gated
accesses, HGV deliveries reversing into a loading bay, operatives crossing to the welfare
cabins", "review this site traffic plan whose only pedestrian control is a banksman in hi-vis",
or "plan vehicle-pedestrian segregation and the delivery / reversing controls for our city-centre
plot with a footway adjacent to the hoarding". Trigger phrases: *traffic management plan, TMP,
site traffic plan, vehicle-pedestrian segregation, one-way system, reversing controls, banksman /
traffic marshal, loading / delivery management, construction logistics, site access, public /
highway interface, CDM 2015 Reg 27, Schedule 3, HSG144*. The load-bearing inputs are the **named
site + its access points** and **at least the vehicle and pedestrian types** that interface; if
any is missing, the Workflow intake below **refuses to proceed** until they are elicited (it
never invents a layout, a route, or an access point).

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
| UK    | ../../knowledge-base/regulatory/cdm-2015.md (**CDM 2015 Reg 27** organise the site for safe vehicle/pedestrian movement + **Schedule 3** traffic routes — suitable, sufficient, separated, warning of approach — the **traffic-routes row**; pairs with **HSE HSG144** *The safe use of vehicles on construction sites*) |
| USA   | ../../knowledge-base/regulatory/osha-1926.md (**29 CFR 1926 Subpart O** motor vehicles, mechanised equipment & marine operations + **1926.601 / .602** — site traffic / equipment access) |
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state) — **mandatory state detection; defers to `hse-india`; the state site-traffic obligation is a literal `[GAP]`, never a minted national form number** |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Segregation-by-design (every run) | ../../knowledge-base/prompt-snippets/traffic-segregation.md (`KB-SNIP-TRAFFIC-SEGREGATION` — the segregation-**by-design** control hierarchy: eliminate the conflict / design out reversing → one-way & turning → physical segregation → signage / speed / lighting → banksman LAST; a "hi-vis + banksman only" pedestrian control is the prevented downgrade) |

This skill always grounds in `KB-STD-ISO45001` (6.1.2 hazard ID + 8.1.2 hierarchy of controls)
and applies `KB-SNIP-HOC` to every control. The traffic-specific grounding is the
**segregation-by-design hierarchy** in `KB-SNIP-TRAFFIC-SEGREGATION` (read it every run) plus, for
a **UK** site, **CDM 2015 Reg 27 + Schedule 3** via `KB-REG-CDM2015` (the **traffic-routes row** —
routes *suitable, sufficient and separated*, with warning of approach) and **HSE HSG144**; the
bundle clause cross-walk `KB-SNIP-CONSTRUCTION-CLAUSE-MAP` carries the **Reg 27 + Schedule 3 →
Traffic Management Plan** row that places this skill in the hse-construction document chain. For a
**US** site it cites **29 CFR 1926 Subpart O** (+ 1926.601 / .602) via `KB-REG-OSHA1926`. For an
**India** site it resolves the state via `KB-REG-IN-STATEFORMS` (**mandatory state detection** —
defers to `hse-india`; confirm the state before citing any obligation; emit a literal `[GAP]`,
**never a national form number**) with the Factories Act framing in `KB-REG-IN-FACTORIES`. The
rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table (Q1 site &
layout free-text [**named site + access points + constraints** — refuse a generic site] · Q2
traffic types multi-select [HGV deliveries · plant / MEWP · forklift / telehandler · light
vehicles · pedestrians / operatives · public / highway] · Q3 known conflict points free-text
[gates, loading bays, crossings, blind corners, shared routes] · Q4 delivery & reversing profile
MCQ [scheduled banked / ad-hoc / continuous — **reversing present → push toward elimination via
one-way / turning areas, banksman as the LAST resort**] · Q5 public & highway interface MCQ [none
/ footway adjacent / live highway] · Q6 jurisdiction), the **mandatory India → state branch** (Q6
= India → Q6a + `KB-REG-IN-STATEFORMS`, defers to `hse-india`, literal `[GAP]`, never a national
form number), the echo-back, and the refuse-on-vague anchors — lives in **`references/intake.md`**.
Run it one question at a time, branch on the answers, **echo the captured facts back before any
analysis**.

**The GATE (refuse-on-vague):** **no traffic management plan is produced** until **a named site
with its access points (Q1)** and **at least the vehicle and pedestrian types that interface (Q2)**
are captured. The skill **refuses to plan on a generic site, an unnamed access point, or "the site
roads"** — ask again, or record `[ASSUMPTION]` / `[GAP]`; **never invent a layout, a route, an
access point, or a conflict point.** **Uncontrolled reversing with no Reg 27 / Schedule 3 grounding
is a citation + specificity failure** — name the routes, do not produce a generic plan.

### The traffic-management method (CDM 2015 Reg 27 + Schedule 3 + the segregation-by-design hierarchy)

Full method in `references/METHODOLOGY.md`. The skill **reads** the segregation hierarchy and
**ranks** controls; it uses **no risk-scoring engine for the plan body** (the optional `controls`
engine ranks/validates a residual conflict's treatment). Steps:

1. **De-identify the inputs** — before any drafting (the `deid` block above + the
   De-identifier-runs-first orchestration rule). This is the **lowest-PII** skill in the pack
   (site / route-level), but any **named driver / operative / banksman** that arrives in the
   inputs (e.g. a named driver in a prior reversing near-miss, a fitness-for-duty note) is
   scrubbed to a **role label** before any analysis. The TMP is a **site/route-level document** —
   it carries **no named individual** in the circulated plan; see `references/deid-checklist.md`.
2. **Map the site & routes (the specificity anchor)** — from Q1/Q3 lay out the **named** vehicle
   routes, the **named** pedestrian routes, the access points, the loading / delivery bays, and
   the conflict points (gates, crossings, blind corners, shared routes). An unnamed route or a
   generic "site roads" is a `[GAP]` and a **stop** — never invented.
3. **Identify every vehicle-pedestrian conflict point** — for each Q2 / Q3 interface name **what**
   conflicts (reversing HGV vs operative crossing, forklift vs pedestrian on a shared route, the
   public footway vs the site access) and **where**. Routes must be **suitable, sufficient and
   separated** (Schedule 3).
4. **Apply the segregation-by-design hierarchy (the core-value lever)** — for **every** conflict
   point apply `KB-SNIP-TRAFFIC-SEGREGATION` **in order**: **(1) eliminate the conflict / design
   out reversing** (drive-through / one-way systems, remove pedestrians from the vehicle area,
   reduce movements) → **(2) one-way & turning arrangements** (turning circles, dedicated
   loading / unloading bays so vehicles do not reverse into the work area) → **(3) physical
   segregation** (barriers, segregated pedestrian routes, edge protection, gated crossings,
   separate vehicle / people access) → **(4) signage, speed limits & lighting** (warning of
   approach per Schedule 3) → **(5) a banksman / traffic marshal — the LAST resort**, only where a
   higher-order control cannot eliminate the residual reversing / manoeuvring risk. A pedestrian
   control whose only treatment is **"hi-vis and a banksman" with no physical or temporal
   segregation is flagged PPE/admin-led and pushed up the hierarchy** (`controls.validate_treatment`
   → `ppe_admin_only=True` with no higher-order control and no justification is a **defect** the
   Critic/QA pass must catch). Rank every residual control via `KB-SNIP-HOC`.
5. **Reversing elimination (Q4)** — where reversing is present, the plan **leads with eliminating
   it**: a one-way system, a turning circle, or a drive-through loading bay so vehicles do not
   reverse into the work area. A banksman is only the residual control **after** the higher-order
   options are designed in — never the headline.
6. **Loading / delivery management** — schedule deliveries (banked / booked-in delivery windows to
   reduce queueing and ad-hoc reversing), set the loading / unloading bays, the holding area, and
   the routing to and from them.
7. **Speed limits & signage (Schedule 3 warning of approach)** — set the site speed limit, the
   signage at conflict points, the lighting at crossings, and the wheel-wash / road-cleanliness
   provision where the highway interface needs it.
8. **Public / highway interface (Q5)** — for a footway-adjacent or live-highway interface, set the
   pedestrian protection (hoarding, covered way, protected footway), the highway-signing duty
   (where applicable), and the public segregation; the **public is never controlled by a banksman
   alone**.
9. **Enforcement, monitoring & review** — set who enforces the plan on site, the monitoring (route
   inspections, near-miss capture), and the **review schedule** (a re-plan trigger on any change of
   phase, access, traffic type, or delivery profile) — each as a **SMART action with a named owner
   (role) + a review date**.
10. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check loop: the site + access
    points + traffic types are named (or the plan is refused); every conflict point is treated by
    the **segregation-by-design hierarchy** with **no un-justified "hi-vis + banksman only"
    control**; reversing leads with elimination; routes are suitable / sufficient / separated;
    Reg 27 + Schedule 3 (and HSG144 / 29 CFR 1926 Subpart O / the India state obligation via
    `hse-india`) cited; de-id applied (no named individual in the circulated plan); no conclusion on
    an unstated assumption.
11. **Assemble the branded report** — build `report.json` (see
    `assets/traffic-management-plan.report.json`) and run the canonical `report-output` call below.

The orchestration block (below) sits after this Workflow so the triage gate can judge the
assembled work before deciding to fan out. The **segregation hierarchy is read prompt-text**
(`KB-SNIP-TRAFFIC-SEGREGATION`); the optional `controls.rank_controls` / `controls.validate_treatment`
calls flag a **"hi-vis + banksman only"** treatment — **there is no traffic-flow or risk-scoring
calculator** in this skill.

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

This is the **STANDARD moderate roster** (A6 "moderate = 2–3"): the **De-identifier is the
sequential first gate** (not a fan-out peer, even at this skill's low PII), the fan-out jobs are
**Routing-&-Segregation-Analyst + Delivery-&-Interface-Author + Regulatory-Checker**, and
**Critic/QA is mandatory**. **There is no traffic-flow / risk-scoring calculator** — the
segregation hierarchy is read prompt-text (`KB-SNIP-TRAFFIC-SEGREGATION`) and the optional
`controls` engine only ranks / validates a residual conflict's treatment. A **small single-access
site** runs single-threaded. Archetypes: `KB-SNIP-ARCHETYPES`.

- **De-identifier** — runs **FIRST** (sequential gate, not a fan-out peer); scrub any
  **named driver / operative / banksman** and any **fitness-for-duty / health detail** that
  arrives in the inputs (e.g. a named driver in a prior reversing near-miss) to role labels before
  any analysis — every fan-out job below consumes only the scrubbed text. The TMP is a
  **site / route-level document and carries no named individual** in the circulated plan; any
  incident is recorded at role level ("a prior reversing near-miss at the south gate") without the
  individual's identity, date, or medical outcome. A worker's **fitness / health detail is always
  scrubbed and never circulated**.
- **Routing-&-Segregation-Analyst** — from Q1 / Q3 lay out the **named** vehicle and pedestrian
  routes, the access points, and the **vehicle-pedestrian conflict points**; for each conflict
  apply the **segregation-by-design hierarchy** (`KB-SNIP-TRAFFIC-SEGREGATION`) — **eliminate /
  design out reversing → one-way & turning → physical segregation → signage / speed / lighting →
  banksman LAST** — and **flag any "hi-vis + banksman only" pedestrian control** as PPE/admin-led
  for push-up (`controls.validate_treatment`). Routes must be **suitable, sufficient and
  separated** (Schedule 3). SCOPE-OUT: deliveries + the public / highway interface
  (Delivery-&-Interface-Author), the law (Regulatory-Checker).
- **Delivery-&-Interface-Author** — author the **loading / delivery management** (booked-in delivery
  windows, loading bays, holding area, routing — **eliminate ad-hoc reversing**), the **speed
  limits & signage** (Schedule 3 warning of approach, lighting at conflict points), and the
  **public / live-highway interface** (hoarding / covered way / protected footway, the highway-
  signing duty — the **public is never controlled by a banksman alone**). SCOPE-OUT: the route /
  segregation layout (Routing-&-Segregation-Analyst), the law (Regulatory-Checker).
- **Regulatory-Checker** — for the resolved jurisdiction return the traffic-law grounding: **UK**
  **CDM 2015 Reg 27 + Schedule 3** (traffic routes suitable / sufficient / separated, warning of
  approach) via `KB-REG-CDM2015` + **HSE HSG144**; **US** **29 CFR 1926 Subpart O** (+ 1926.601 /
  .602) via `KB-REG-OSHA1926`; **India** the state site-traffic obligation via `KB-REG-IN-STATEFORMS`
  (state confirmed first; defers to `hse-india`; literal `[GAP]`, never a national form number).
  Conservative, flag `[GAP]`. SCOPE-OUT: the routes / deliveries (the two Authors above).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in
  **`references/sme-review.md`** (a **Construction Logistics / Temporary Works (Traffic)
  Coordinator**) before any output: the site + access points + traffic types are named (not a
  generic site); **every conflict point leads with segregation-by-design and reversing leads with
  elimination** (a "hi-vis + banksman only" control is the prevented downgrade); routes are
  suitable / sufficient / separated; Reg 27 + Schedule 3 cited. It **never emits "approved by a
  competent person"**.
- **Critic/QA** (MANDATORY) — the site + access points + traffic types are named (or the plan is
  refused); **every conflict point is treated by the segregation-by-design hierarchy with no
  un-justified "hi-vis + banksman only" control**; reversing leads with elimination; routes are
  suitable / sufficient / separated; deliveries / signage / the public interface are set; Reg 27 +
  Schedule 3 (HSG144 / 29 CFR 1926 Subpart O / the India state obligation) cited; every action
  carries a named owner (role) + a review date; **zero named individual** leaks into the circulated
  site/route-level plan. PASS/FAIL.

A **small single-access** site with one delivery profile runs single-threaded — no subagents — but
the De-identifier gate, the segregation-hierarchy pass, and the Critic/QA pass are still made.

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
