---
name: leading-lagging-kpi-framework
description: Designs and normalises a balanced leading/lagging HSE KPI framework for
  a named organisation, function, or site against ISO 45001:2018 clause 9.1 — never
  a lagging-only set. Each indicator is fully defined (formula, source, frequency,
  owner, target); a lagging-only request is flagged for balance and a gameable metric
  (raw incident count as a target) with no safeguard is flagged for defensibility.
  Carries a road-safety leading-indicator branch (ISO 39001:2012) when the scope is
  road/transport/fleet. It DESIGNS the indicator set — distinct from incident-rate-calculator
  (which computes given rates) and process-safety-kpi (API RP 754 tiers), which it
  references as exemplars, not replacements. Lagging rates are computed by the incident_rates
  engine to standard definitions, never invented. Decision-support only; a competent
  person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: performance
  tier: 2
  audience:
  - M
  - E
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-leadership
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Leading Lagging Kpi Framework

A consultant-grade HSE skill that **designs and normalises a balanced leading/lagging
KPI framework** for a named organisation, function, or site against **ISO 45001:2018
clause 9.1** (monitoring, measurement, analysis & performance evaluation). It forces the
single lever that separates a defensible measurement set from copy-paste paperwork:
**balance and specificity** — a **lagging-only** set (e.g. TRIR alone) is flagged as a
reactive-only picture, and **every indicator is fully defined** (formula · source ·
frequency · owner · target). A **gameable metric** — a raw incident count as a target,
which incentivises under-reporting — is flagged for defensibility unless paired with a
quality/assurance safeguard. It grounds in `KB-SNIP-KPI-DESIGN` (method) and the
single-source `KB-DATA-LEADING-INDICATORS` catalogue, maps to clause 9.1 via the shared
`KB-SNIP-LEADERSHIP-CLAUSE-MAP`, and computes any lagging **rate** through the
deterministic `incident_rates` engine (anchors TRIR 2.07 / LTIFR 6.00), never inventing a
figure. It carries a **road-safety EXTEND branch** (`KB-DATA-ROAD-SAFETY-INDICATORS`,
ISO 39001:2012) that activates when the scope is road / transport / fleet — one skill, the
single home of road-safety KPIs. This skill **designs** the indicator set: it is distinct
from `incident-rate-calculator` (which *computes* given rates), `process-safety-kpi` (API
RP 754 tiers) and `aviation-spi-spt-framework` (ICAO Annex 19), which it references as
domain **exemplars**, never replacing them. Decision-support only; a competent person must
review the output.

## When to use this skill

Use this skill when the user needs to **design, normalise, or rebalance a set of HSE
KPIs / safety performance indicators** for a named organisation, function, or site — for
example "build a balanced leading and lagging KPI dashboard for our manufacturing
division", "our scorecard is TRIR-only — design the leading indicators we're missing",
"define each of these metrics properly (formula, owner, target)", or "set up road-safety
KPIs for our fleet". Trigger phrases: *leading indicators, lagging indicators, KPI
framework, safety performance indicators, balanced scorecard, ISO 45001 clause 9.1
monitoring & measurement, anti-gaming metrics, road-safety / fleet KPIs (ISO 39001)*.

This skill **designs / normalises** the indicator set — it does **not** compute a given
injury rate (that is `incident-rate-calculator`), own the API RP 754 process-safety tiers
(`process-safety-kpi`) or the ICAO Annex 19 aviation SPIs (`aviation-spi-spt-framework`);
intake Q1 disambiguates against those calculators/exemplars and against the leadership
siblings `safety-culture-assessment`, `bbs-program-designer`, and `safety-walk-gemba`. If
the request is a **lagging-only** set, or a **gameable** metric with no safeguard, or an
indicator with no definition, the Workflow intake below forces balance, a safeguard, and a
full definition before any drafting.

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

This skill is **method-led**, not law-led: balanced KPI design is a management-system
method (ISO 45001 clause 9.1), so it **always** grounds in the KPI-design method + the
single-source indicator catalogue + the bundle clause map, and resolves the road-safety
branch only when the scope is road / transport / fleet.

| Read on every run | File |
|---|---|
| The balanced leading/lagging KPI design method — balance, per-indicator definition (formula·source·frequency·owner·target), anti-gaming guardrails, target-setting by maturity | ../../knowledge-base/prompt-snippets/kpi-design.md (KB-SNIP-KPI-DESIGN) |
| The single-source leading/lagging indicator catalogue (each cited) — the balanced set is built from this, never a private list | ../../knowledge-base/data-points/leading-indicators.md (KB-DATA-LEADING-INDICATORS) |
| The bundle-shared ISO 45001 leadership clause cross-walk (9.1 performance evaluation → this skill is primary) | ../../knowledge-base/prompt-snippets/leadership-clause-map.md (KB-SNIP-LEADERSHIP-CLAUSE-MAP) |
| Applied wherever a leading indicator implies a control action — a measure ranks above admin/PPE, never a PPE-only treatment | ../../knowledge-base/prompt-snippets/hierarchy-of-controls.md (KB-SNIP-HOC) |

| Scope branch | Read |
|---|---|
| Road / transport / fleet scope (the LEAD-06 road-safety EXTEND branch, D-01) — the ISO 39001:2012 road-safety indicator set; this skill is its single home | ../../knowledge-base/data-points/road-safety-indicators.md (KB-DATA-ROAD-SAFETY-INDICATORS) |
| Any other scope | No road-safety branch — design the balanced set from KB-DATA-LEADING-INDICATORS only |

For management-system structure, ground in `../../knowledge-base/standards/iso-45001.md`
(KB-STD-ISO45001 — clause 9.1 is the regulatory anchor). For any **lagging rate**, the
figure is **computed** by `scripts/hse_components/incident_rates` to standard definitions
(anchors TRIR 2.07 / LTIFR 6.00) — never invented in-prompt; an occupational-rate
*computation* request routes to `incident-rate-calculator`. For any benchmark/target
figure, resolve the ID in the relevant `_registry.yaml`, read ONLY the named file, and
quote its `source`+`year`. The rule-9 manifest is `references/_skill-kb.md`.

| Jurisdiction (the performance-monitoring duty, where a law is cited) | Read |
|---|---|
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state — **mandatory state detection**, defers to `hse-india`) |
| Unknown | Ask before citing any specific law — the balanced KPI method (ISO 45001 9.1) still applies |

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(scope/level · named org-function-site + period · the **leading** indicators tracked ·
the **lagging** outcomes · per-indicator **definition** (formula·source·frequency·owner·
target) · **targets** and the anti-gaming **safeguard** for any countable target · culture
maturity for the leading/lagging mix · benchmark · output), the **road-safety branch**
(road/transport/fleet scope → the ISO 39001:2012 indicator set from
`KB-DATA-ROAD-SAFETY-INDICATORS`), the **balance gate** (a lagging-only set is refused),
the **anti-gaming gate** (a gameable metric with no safeguard is refused), the echo-back,
and the refuse-on-vague anchors — lives in **`references/intake.md`**. A **rate** is never
reported without its work-hours denominator (it is computed by `incident_rates`, never
invented); an occupational-rate *computation* request routes to `incident-rate-calculator`;
Q1 disambiguates against `process-safety-kpi` / `aviation-spi-spt-framework` and the
leadership siblings.

Then: design / normalise the balanced indicator set per the method → validate the draft against `references/QUALITY_CHECKLIST.md` → produce the output via the Output format section below. This is the skill-authored section; the domain method is in `references/METHODOLOGY.md`.

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

For a non-trivial task the triage gate may fan out to:

- **Indicator Designer** — from the scrubbed inputs, builds the **balanced** set from
  `KB-DATA-LEADING-INDICATORS` (+ the road-safety branch where the scope is
  road/transport/fleet), defines every indicator (formula·source·frequency·owner·target),
  and matches the leading/lagging mix to culture maturity. SCOPE-OUT: does not *compute*
  lagging rates (the `incident_rates` engine does) and does not own the API RP 754 / ICAO
  tiers (`process-safety-kpi` / `aviation-spi-spt-framework` own those).
- **Anti-gaming Reviewer** — stress-tests every countable target for a perverse incentive
  (raw incident count → under-reporting), pairs each with a quality/assurance safeguard,
  and flags any lagging-only imbalance (clause 9.1 reactive-only picture).
- **Critic/QA** (MANDATORY) — adversarial final pass for this regulatory/safety output:
  specificity (every indicator defined), balance (not lagging-only), defensibility (no
  gameable metric without a safeguard), de-identification (aggregate metrics, <5
  small-cell suppression), and citation accuracy (clause 9.1 + indicator definitions +
  ISO 39001 on the road-safety branch).
- **SME Review & Sign-off** (MANDATORY, before ANY output) — run the per-skill SME
  persona sign-off (HSE Performance / Assurance Manager) per `references/sme-review.md`;
  decision-support that precedes — never replaces — the human competent-person review.

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
