---
name: incident-investigation
description: 'Investigates an HSE incident — injury, illness, near-miss, property
  or environmental loss — and produces a defensible, de-identified investigation report:
  timeline, evidence log, root-cause analysis (5-Whys / ICAM / SCAT / Fishbone / Swiss-Cheese),
  root and contributing causes traced to evidence, a hierarchy-of-controls corrective-action
  plan with named owners and due dates, and the jurisdiction''s reporting/notification
  requirements. Use it to investigate an accident, conduct a root-cause analysis /
  RCA, write up an incident, build a CAPA from an event, or determine whether an incident
  is reportable (RIDDOR / OSHA 29 CFR 1904 / India state accident form). Decision-support
  only; a competent person must review the output.'
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: incident-management
  tier: 1
  audience:
  - M
  - C
  industry:
  - All
  jurisdiction:
  - All
  status: stable
  plugin: hse-core
  hse_reviewed_by: ''
  hse_reviewed_date: ''
---

# Incident Investigation

A consultant-grade HSE skill that turns an event — injury, illness, near-miss,
property or environmental loss — into a **defensible, de-identified investigation
report**: a timeline, a numbered evidence log, a root-cause analysis, root and
contributing causes **each traced to a numbered evidence item**, a
hierarchy-of-controls CAPA with named owners and ISO due dates, and the
jurisdiction's reporting/notification verdict. It is grounded in **ISO 45001 clause
10.2** (incident, nonconformity & corrective action). Two non-negotiables hold
throughout: **de-identify first** (no analysis or drafting ever touches raw
PII/health data), and **trace every conclusion to evidence** (no un-evidenced cause,
no anonymous action, no invented citation). Root-cause structure and systemic reach,
control ranking, and action traceability are **deterministic** (the A7 `rca`,
`controls`, `smart_actions` engines), never prose judgement.

## When to use this skill

Use this skill **after an incident, accident, or near-miss** — when a root-cause
analysis, a CAPA, or a reportability decision is needed for a concrete event at a
named site/asset. Trigger phrases: *investigate an incident, incident investigation,
root cause analysis / RCA, 5-Whys / ICAM / SCAT / Fishbone (Ishikawa) / Swiss-Cheese,
accident investigation, near-miss investigation, write up an incident, CAPA from an
incident, corrective action plan, is this reportable / reportability, RIDDOR, OSHA
recordable / 29 CFR 1904, India accident notice / state accident form*. **Not** for
live emergency response (a different skill), and **not** for routine incident-rate
dashboards (use `incident-rate-calculator`, B10 — this skill may surface only one
*contextual* rate). If the request is vague, the Workflow intake below forces the
specifics — and the de-identification of all personal/health detail — before any
analysis.

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

| Jurisdiction | Read (for the reporting/notification verdict) |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md + in-state-forms.md — **resolve the STATE first (mandatory)**, then read the accident-notice row for that state (e.g. Maharashtra → Form 24 within 24h via KB-REG-IN-STATEFORMS); never a national form number; append the OSH-Code transition note |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md (RIDDOR 2013 reportable events + timelines) |
| USA   | ../../knowledge-base/regulatory/us-osha.md (29 CFR 1904 recordkeeping + 1904.39 reporting timelines: 8h fatality / 24h in-patient-hospitalization/amputation/eye-loss) |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in **`KB-STD-ISO45001` clause 10.2** (incident,
nonconformity & corrective action) — the clause that structures the RCA + CAPA — and
applies `KB-SNIP-HOC` to every CAPA control (paired with the A7 `controls.rank_controls`
check). For an India site it resolves the state via `KB-REG-IN-STATEFORMS` (**mandatory
state detection** — confirm the state before citing any form; an un-seeded state →
`[GAP]` + "verify the state accident form with a competent person", never an invented
form). Every citation quotes the fragment's `source`+`year`; B5 **never invents** a
citation. The rule-9 manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

Run the B5 question set below, one question at a time, MCQ where the answer space is
enumerable and free-text where it is open, branching on the answers (`KB-SNIP-INTAKE`).
**Never proceed on vague inputs**; record `[GAP]` for missing evidence and
`[ASSUMPTION]` for anything inferred. **Never invent evidence or causes.** Q5
("people involved") is **flagged for IMMEDIATE de-identification** — it is scrubbed in
Workflow step 2 before any analysis, and the intake echoes those facts back as role
labels.

| # | Question | Type | Options / branch |
|---|---|---|---|
| Q1 | **What happened?** (the core narrative — the sequence of events) | free-text | The investigation's seed; the factual account, not conclusions. |
| Q2 | **When and where?** (date, time, location/asset) | free-text | Flagged for de-id (exact date + precise location are quasi-identifiers). |
| Q3 | **Incident type / classification** | MCQ | injury · illness · near-miss · property damage · environmental release · dangerous occurrence — branches the reporting logic (step 7) + the rate context (Q10). |
| Q4 | **Severity / outcome** | MCQ | fatality · lost-time injury · medical-treatment · first-aid · no-injury near-miss · property-only · environmental-only — drives reportability urgency + the RCA-method suggestion. |
| Q5 | **People involved** | free-text | **Flagged for IMMEDIATE de-identification** — names, roles, witnesses captured here are pseudonymized in step 2 before any analysis; the intake echoes them back as role labels ("Worker A", witness "W-1"). |
| Q6 | **Immediate / obvious causes** (what visibly went wrong) | free-text | The *starting point* for RCA, never the endpoint — the skill drives past these to systemic factors. |
| Q7 | **Evidence available** | free-text | statements, photos, logs, readings, maintenance records, procedures → becomes the numbered evidence log; `[GAP]` recorded for anything missing. |
| Q8 | **RCA method preference** | MCQ | **Five A7-validated options, each with a one-line "when to pick":** **5-Whys** — quick single causal chain; minor events. **ICAM** — systems-based, organisational focus; serious/high-potential events. **SCAT** — Loss-Causation model linking to management-system control failures. **Fishbone (Ishikawa)** — categorise causes across Man/Machine/Method/Material/Measurement/Environment when factors span domains. **Swiss-Cheese (Reason)** — trace failed/absent defence layers to latent organisational influences; barrier/defence-in-depth events. *Branch:* ICAM → prompt for organisational-factor evidence; SCAT → management-system context; Fishbone → evidence across the non-Man branches; Swiss-Cheese → the failed barrier at each layer. |
| Q9 | **Jurisdiction** | MCQ | India · UK · USA · EU · Other/Unknown. **India → ask the STATE** (mandatory) → triggers `KB-REG-IN-STATEFORMS`; Unknown → the reporting step defers to "ask before citing." |
| Q10 | *(optional; branch on type=injury/illness)* **Period exposure hours + recordable counts** | free-text | Only if the user wants the contextual rate; otherwise **skipped** — `incident_rates` is omitted rather than fabricating a denominator. |

After the last applicable question (and **after** the step-2 de-id scrub), **echo the
captured, de-identified facts back** ("Here is what I have: a lost-time injury to
Worker A on [date], at [location], witnessed by W-1; evidence E-1…E-4; method ICAM;
jurisdiction India/Maharashtra — confirm before I analyse?") and proceed only on
confirmation.

### The investigation method (de-id-first → evidence → cause → control → report)

Full method in `references/METHODOLOGY.md`. The sequence is strict: **evidence before
cause, cause before control**. Steps:

1. **Structured intake** (Step 0 above) — gather facts; never proceed on vague inputs.
2. **De-identify FIRST (the `deid` block above — a sequential dependency).** Before
   anything else, run the De-identifier over **all** intake inputs: detect and list
   every identifier; pseudonymize to stable role labels ("Worker A", witness "W-1");
   aggregate any injury/illness cell `<5`; emit the re-identification key as a
   **separate** artifact returned to the user — **never** in the report or any subagent
   prompt. **Every subsequent step consumes only the scrubbed, role-labelled text.** (On
   a single-thread host the orchestration fallback runs this inline, first.)
3. **Establish the timeline & gather evidence.** Reconstruct the factual sequence from
   the scrubbed inputs into a numbered, time-ordered event list; build the **evidence
   log** with each item numbered `E-1, E-2, …` and typed (statement / photo-ref / log /
   reading / document). Flag `[GAP]` where a needed fact is absent. **No causes yet —
   facts only.**
4. **Root-cause analysis (A7 `rca` — the user-chosen method, one of five).** Take the
   method chosen at Q8 (**5-Whys / ICAM / SCAT / Fishbone / Swiss-Cheese** — all
   A7-validated). Run `rca.scaffold(method, problem)` to get the method's required
   slots; fill them **from the evidence log** (each causal claim cites an `E-n`); then
   run `rca.validate(method, analysis)` and resolve every issue it raises.
   **`reaches_systemic` is enforced for ALL FIVE methods — it is not optional:** a
   5-Whys terminating at individual error fails; an ICAM with no Organisational Factor
   fails; a SCAT missing Basic-Causes / Lack-of-Control fails; a **Fishbone with only
   the "Man" branch populated fails** (all-individual-blame); a **Swiss-Cheese with no
   organisational-influence layer fails** (no latent/systemic reach). The skill must
   reach a systemic/organisational factor whatever the method.
5. **Identify root + contributing causes — traced to evidence (defensibility).** Emit
   causes as `{id: "RC-n", statement, tier: root|contributing|immediate, evidence_ref:
   "E-n"}`. Every cause **must** carry an `evidence_ref` into the step-3 evidence log; a
   cause with no evidence is dropped or re-tagged `[ASSUMPTION]` and **cannot be a root
   cause.** This is the defensibility lever made mechanical.
6. **CAPA — hierarchy-of-controls-driven, owners + dates (A7 `controls` +
   `smart_actions`).** For each root/contributing cause, draft corrective/preventive
   actions ranked by the hierarchy of controls (apply `KB-SNIP-HOC`): prefer
   Elimination/Substitution/Engineering; any PPE/admin-only action must be explicitly
   justified or escalated. Emit `{action, owner, due (ISO-8601), measure, links_to_cause:
   "RC-n", hoc_tier}`. Run `controls.rank_controls` on the action set (it flags
   PPE/admin-only-without-justification) and `smart_actions.validate_register` (assert
   every action has a named owner, a valid ISO due date, a measure, and a
   `links_to_cause` — `all_traced_to_cause` must be true). **No anonymous actions, no
   "ASAP", no untraced action.**
7. **Jurisdiction reporting/notification check (a first-class step).** Resolve the
   jurisdiction (Q9); **India → resolve the STATE first** (ask, or infer-then-confirm —
   mandatory) and look up the accident-notice row in `KB-REG-IN-STATEFORMS`. Return a
   reportability **verdict + the exact rule/clause + the deadline + the prescribed
   form** (India state form + the OSH-Code transition note / UK RIDDOR / US OSHA 29 CFR
   1904.39). **Surface the verdict even when NOT reportable** ("assessed against
   [authority] — not reportable because [criterion]"). An un-seeded India state →
   `[GAP]` + "verify with a competent person"; **never invent a national form number**;
   Unknown jurisdiction → ask before citing.
8. **Validate against `references/QUALITY_CHECKLIST.md`.** Self-check before drafting:
   de-id clean (no residual identifier, no `<5` cell, no key in output); every cause
   has an `evidence_ref`; `rca.validate` passed (`reaches_systemic` true); every CAPA
   has owner + ISO date + measure + `links_to_cause`; at least one
   Engineering-or-higher control or a justified absence; a reporting verdict cited to
   the matched KB row. Fix anything that fails before the report.
9. **Produce the branded report (A4).** Assemble the `assets/` block tree (see
   `assets/investigation-report.template.json`) into `report.json` and run the
   canonical `report-output` call below. The engine auto-stamps the cover,
   classification banner, and the limitations & de-identification notice.

**Contextual incident rate (optional, off by default).** Only if Q10 captured period
hours **and** recordable counts, call `incident_rates.compute_all(counts, hours_worked,
period)` to surface a single *contextual* TRIR/LTIFR `metrics` KPI ("this LTI moves the
site LTIFR to X"). It is **never** the investigation's conclusion, and **never**
fabricated — `incident_rates` raises on zero/negative hours, so it is called inside a
guard and **omitted** when the inputs are absent. Rate *dashboards* belong to B10.

The orchestration block (below) governs the agentic execution: for a non-trivial
incident the triage gate fans out steps 3–7 across the 4-agent roster **after** the
De-identifier; for a trivial single-witness near-miss it stays single-threaded but
still runs the de-id scrub first and the mandatory Critic/QA pass. The **De-identifier
is never one of the parallel jobs** — it is the sequential gate before fan-out.

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

### Step 4 — Critic / QA (MANDATORY — this is regulatory/safety output)
Spawn ONE Critic: give it the draft + the inputs + the output contract. It finds errors,
unsupported claims, missed regulatory triggers, lower-order-only controls, and any
de-identification leak. Fix everything it raises before delivery.

> Single-threaded fallback: if your host has no subagent capability, execute each job
> sequentially in THIS context — run the de-identification scrub first, keep the scope
> discipline, and still perform the required Critic/QA pass before delivery.
<!-- hse:block:orchestration:end -->

### Subagent roster for THIS skill
- **De-identifier** — runs FIRST (sequential dependency); scrub all PII/health detail —
  injured-party, witnesses, diagnoses, exact dates/locations, small injury cells — into role
  labels before any analysis. Returns the re-identification key SEPARATELY (to the orchestrator,
  not to any sibling). Everything below consumes only its scrubbed output.
- **A · Evidence & Timeline Reconstructor** — assemble the numbered, time-ordered event
  sequence and the numbered evidence log (E-1…) from the scrubbed inputs; flag [GAP].
  SCOPE-OUT: does not assign causes (B owns it) or decide reportability (C owns it).
- **B · Root-Cause Analyst** — apply the chosen method (5-Whys / ICAM / SCAT / Fishbone /
  Swiss-Cheese) via rca.py; every causal claim cites an evidence item (E-n); reach a
  systemic/organisational factor (rca.validate `reaches_systemic` true for whichever method).
  SCOPE-OUT: reportability (C owns it) and control selection (D owns it).
- **C · Regulatory Reportability Checker** — for the resolved jurisdiction (India → resolved
  STATE first), return verdict + clause/section + deadline + form (India state accident form
  via KB-REG-IN-STATEFORMS / UK RIDDOR / US OSHA 29 CFR 1904). Conservative — flag [GAP] and
  "ask a competent person" when unsure. SCOPE-OUT: does not draft the report or invent a form number.
- **D · Corrective-Action Drafter** — hierarchy-of-controls-tagged CAPAs, each tracing to a
  named cause (RC-n) with a named owner + ISO due date + measure; prefer higher-order controls,
  justify any PPE/admin-only. SCOPE-OUT: does not score causes (B) or check law (C).
- **Critic/QA** (MANDATORY) — adversarial read-only review: every cause evidence-backed, RCA
  reaches a systemic factor, reportability cited conservatively to the matched KB row, every
  CAPA traces to a cause with owner+date, no PPE/admin-only without justification, and ZERO
  PII/health leak (no residual identifier, no <5 cell, no re-id key in the output).

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
- `references/deid-checklist.md` — the full de-identification checklist (A5).
- `references/QUALITY_CHECKLIST.md` — the pre-output validation gate.
- `references/_skill-kb.md` — the knowledge-base fragments this skill resolves.
