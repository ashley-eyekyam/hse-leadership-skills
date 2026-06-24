---
name: weather-dynamic-risk-assessment
description: 'Produce a consultant-grade point-of-work DYNAMIC weather risk assessment
  for a named renewables site/activity, led by NAMED NUMERIC thresholds -> a hold/stop/evacuate
  ACTION -> a MANDATORY re-assessment TRIGGER. Use this skill to set weather working
  limits for turbine/blade/tower or outdoor renewables work, decide when to hold,
  stop or evacuate for wind, lightning, ice, visibility or temperature, or replace
  a vague ''monitor the weather'' arrangement with defensible numeric triggers. Wind
  is measured at HUB HEIGHT, not base-of-tower (a base-of-tower reading is a control
  failure). It OWNS the weather thresholds wind-turbine-work-at-height-rescue (REN-01)
  only names: BS 7121-1 (2016) 7 m/s man-riding ceiling is the verified anchor, the
  hub-height cut-off ~=15 m/s is [ASSUMED A4] proposed-and-user-confirms, and every
  other threshold is user-confirmed or [GAP] -- never invented. De-identifies prior
  weather-incident context to role labels. Decision-support only; competent-person
  review required.'
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
  plugin: hse-renewables
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Weather Dynamic Risk Assessment

The **hse-renewables point-of-work DYNAMIC weather risk-assessment skill** — given a **named site / activity** and the **weather-sensitive task**, it produces a defensible weather RA that is **led by NAMED NUMERIC thresholds → a hold / stop / evacuate ACTION → a MANDATORY re-assessment TRIGGER** (`KB-SNIP-DYNAMIC-RA`, `KB-DATA-WEATHER-THRESHOLDS`). Wind is measured at **HUB HEIGHT, not base of tower** for turbine work — a base-of-tower reading understates the exposure and is treated as a **control failure**. It grounds the weather-as-a-work-at-height-governor relationship in `KB-REG-WAH2005` (weather governs whether work at height proceeds).

**The single failure mode this skill exists to kill is "monitor the wind and stop if it gets too windy".** A weather artifact with no numeric threshold, no defined action, or no re-assessment trigger is the indefensible paperwork this skill rejects. Every weather parameter (wind, lightning, ice, visibility, temperature) carries a **specific numeric trigger → a pre-decided action → a re-assessment event** — defined in advance, not decided on the day.

**Numeric thresholds are propose-and-user-confirms, never invented.** The **BS 7121-1 (2016 edition)** man-riding ceiling of **16 mph / 7 m/s** for a personnel-carrier lift is the one **verified public anchor**. The hub-height tower-top wind cut-off of **≈ 15 m/s** is an **`[ASSUMED A4]` industry baseline — not a single citable standard**; it is proposed and the user confirms it (stricter for less-experienced teams). Lightning stand-down follows **NFPA 780** practice / a lightning-warning service; manufacturer / CPA in-service crane wind limits, ice-accretion, visibility and temperature triggers are **user-confirmed or `[GAP]`**. No threshold is asserted as a fixed standard.

**This skill OWNS the weather thresholds REN-01 names (CONV-12, kept distinct).** `wind-turbine-work-at-height-rescue` (REN-01) **names** the hub-height wind hold / lightning stand-down and **defers their ownership here**; this skill owns `KB-DATA-WEATHER-THRESHOLDS` and the dynamic-RA method — cross-referenced, never merged.

## When to use this skill

Use this skill when the user needs a **point-of-work / dynamic weather risk assessment** or **weather working limits** for a **named renewables site and a weather-sensitive activity**. Trigger phrases: "set the wind / lightning / ice working limits for blade rope-access on WTG-09", "when do we hold, stop or evacuate for weather", "build a dynamic weather RA for the crane lift / tower-top work", "our method statement says 'monitor the wind' — make it defensible", "what wind speed stops man-riding lifts", "confirm the hub-height wind cut-off". If the request is vague ("keep an eye on the weather" / "stop if it's too windy"), the Workflow intake forces the named site, the weather-sensitive activity, the controlling equipment, and a numeric threshold for each parameter before any drafting. This skill owns the **weather thresholds + the dynamic-RA method**; the WAH plan + tested rescue is **`wind-turbine-work-at-height-rescue`** (REN-01) and lone working is **`lone-working-assessment`** (REN-02) — cross-referenced, never rebuilt (CONV-12).

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

First read the bundle cross-walk `../../knowledge-base/prompt-snippets/renewables-clause-map.md` (`KB-SNIP-RENEWABLES-CLAUSE-MAP`) — it routes the renewables standard → artifact → owning skill (**this skill owns the weather thresholds + the dynamic-RA method**; REN-01 `wind-turbine-work-at-height-rescue` only names the thresholds and owns the WAH plan + tested rescue; REN-02 `lone-working-assessment` owns the lone-working RA). This skill **OWNS** the weather data + method: read `../../knowledge-base/data-points/weather-thresholds.md` (`KB-DATA-WEATHER-THRESHOLDS`) for the anchors (BS 7121-1 2016 7 m/s man-riding `[VERIFIED]`; ≈15 m/s hub-height cut-off `[ASSUMED A4]`, proposed-and-user-confirms; NFPA 780 lightning practice; manufacturer/site values `[GAP]`) and `../../knowledge-base/prompt-snippets/dynamic-ra.md` (`KB-SNIP-DYNAMIC-RA`) for the **threshold → action → re-assessment-trigger** control spine and the **hub-height-not-base** measurement discipline. Apply `../../knowledge-base/prompt-snippets/hierarchy-of-controls.md` (`KB-SNIP-HOC`) to every control (eliminate the exposure to weather first — reschedule to a forecast low-weather window / do the work in shelter — before administrative stop-limits). Cross-reference the renewables hazard library `../../knowledge-base/hazard-library/renewables.md` for the weather / WAH / dropped-object hazard categories (single home; cross-referenced, never restated). Then resolve the jurisdiction:

| Jurisdiction / element | Read |
|---|---|
| UK (weather governs whether work at height proceeds — the WAH planning + avoid→prevent→mitigate hierarchy + the duty to not work at height in conditions that endanger) | ../../knowledge-base/regulatory/wah2005.md (`KB-REG-WAH2005` — Work at Height Regs 2005 SI 2005/735: reg 4 plan incl. weather, reg 6 avoid→prevent→mitigate, reg 7 collective-before-personal) |
| India (work at height / weather) | ../../knowledge-base/regulatory/in-renewables.md (`KB-REG-IN-RENEWABLES` — deferral pointer; **state detection is mandatory** (CONV-8); defer statutory content to the `hse-india` engine; **no national form number invented**) |
| Unknown | Ask the jurisdiction / regulatory regime before citing any specific regulation |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

The full typed/branched intake Q-table — the **named site / activity** (the
specificity anchor: a generic "the wind farm" is refused), the **weather-sensitive
task and the controlling equipment** (tower-top work / blade rope-access / crane or
man-riding lift / outdoor switching), the **weather parameters in play** (wind,
lightning, ice, visibility, temperature), the **numeric threshold for each parameter**
(the core-value gate: a "monitor / stop if too windy" answer with no number is
refused), the **measurement point** (the hub-height-not-base gate for turbine work),
the **action at each threshold** (hold / stop / evacuate) and the **re-assessment
trigger**, and the jurisdiction branch (UK → `KB-REG-WAH2005`; India →
`KB-REG-IN-RENEWABLES` + mandatory state detection) — lives in
**`references/intake.md`** (the `intake-coverage` manifest + echo-back +
refuse-on-vague anchors). Run it one question at a time, branch on the answers, and
**echo the confirmed site + activity + each parameter's threshold/action/trigger back
before any drafting**.

**The de-identification step runs FIRST** (above): any **prior weather-incident
context** (a named worker involved in a previous weather-related event) is scrubbed to
**role labels** before any analysis (`references/deid-checklist.md`). This is a **lower
de-id tier** — asset / installation / site-level data dominates — but a clean
role-labelled output is still mandatory.

Then walk the **dynamic-RA method** (`references/METHODOLOGY.md`): site / activity /
equipment scoping → for **each weather parameter**, build the control as a
**THRESHOLD → ACTION → RE-ASSESSMENT TRIGGER** (`KB-SNIP-DYNAMIC-RA`): a **specific
numeric threshold** (the BS 7121-1 2016 7 m/s man-riding figure cited verbatim where a
personnel-carrier lift is used; the ≈15 m/s hub-height tower-top cut-off proposed and
user-confirmed `[ASSUMED A4]`; lightning per NFPA 780 practice; ice / visibility /
temperature / manufacturer-CPA crane limits user-confirmed or `[GAP]`) → a **pre-decided
action** (hold / stop / evacuate) → a **mandatory re-assessment trigger** (forecast
change, threshold approached, interval). Apply the **measurement discipline**: wind is
read at **hub height, not base of tower** — flag a base-of-tower reading used for a
tower-top decision as a **control failure**. Apply `controls.py` + `KB-SNIP-HOC` so the
control leads with **eliminating the weather exposure** (reschedule to a forecast
low-weather window / shelter the work) before the administrative stop-limit. Re-score
residual risk on the `risk_matrix` 5×5 after the thresholds + actions, record `[GAP]`
for any unsupplied numeric basis (manufacturer/site limits, lightning detection radius),
and close each `[GAP]` with a SMART action (`smart_actions`) carrying a **named role
owner + an ISO due date**. **Numeric thresholds are user-confirmed / `[GAP]`, never
invented as a fixed standard.**

Then: validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. The domain method (the threshold → action → re-assessment-trigger spine + the hub-height measurement discipline + the propose-and-confirm anchor rules) is in `references/METHODOLOGY.md`.

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

Moderate fan-out for a full dynamic weather RA (the De-identifier runs FIRST as a sequential dependency):

- **De-identifier** — runs FIRST; scrub any **prior weather-incident context** (a named
  worker / crew involved in a previous weather-related event) and any personal contact
  into **role labels** ("Site Lead (role)", "Rope-Access Supervisor (role)"). This is a
  **lower de-id tier** (asset/site data dominates) but role-labelling is still mandatory.
  Returns the re-identification key SEPARATELY to the orchestrator, never to a sibling.
- **Threshold-&-Action-Author** — for each weather parameter author the
  **THRESHOLD → ACTION → RE-ASSESSMENT TRIGGER** control (`KB-SNIP-DYNAMIC-RA`,
  `KB-DATA-WEATHER-THRESHOLDS`): a **specific numeric threshold** (BS 7121-1 2016 7 m/s
  man-riding cited verbatim; ≈15 m/s hub-height cut-off proposed-and-user-confirmed
  `[ASSUMED A4]`; lightning per NFPA 780; ice/visibility/temperature/crane limits
  user-confirmed or `[GAP]`), a **pre-decided action** (hold/stop/evacuate), and a
  **re-assessment trigger** — measured at **hub height, not base of tower**; flag a
  base-of-tower reading as a control failure. **Reject any "monitor the weather / stop
  if too windy" control with no number.** SCOPE-OUT: does not own the WAH plan / rescue
  (REN-01 owns it) or invent a threshold as a fixed standard.
- **Residual-&-Actions-Author** — apply `controls.py` + `KB-SNIP-HOC` (eliminate the
  weather exposure — reschedule / shelter — before the administrative stop-limit), score
  residual risk (`risk_matrix` 5×5) after the thresholds + actions, and write the
  owned/dated `[GAP]`-closure actions (`smart_actions`) for every unsupplied numeric
  basis (manufacturer/site limits, lightning detection radius). SCOPE-OUT: does not set
  the per-parameter thresholds (the Threshold-&-Action-Author owns them).
- **Critic/QA** (MANDATORY) — the renewables-field / dynamic-RA persona
  (`references/sme-review.md` / `KB-SNIP-ARCHETYPES`): every weather parameter carries a
  **numeric threshold → an action → a re-assessment trigger** (no "monitor the weather"
  control survives); wind is measured at **hub height, not base of tower**; the BS 7121-1
  2016 man-riding figure is cited correctly and the ≈15 m/s anchor is flagged `[ASSUMED]`
  / proposed-and-confirmed (never asserted as a fixed standard); every other numeric
  threshold is user-confirmed or `[GAP]`; and ZERO prior-incident PII leak into the
  circulated copy. Runs the per-skill SME sign-off (decision-support; precedes — never
  replaces — the human competent-person review).

Simple single-parameter limits run single-threaded — no subagents.

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
