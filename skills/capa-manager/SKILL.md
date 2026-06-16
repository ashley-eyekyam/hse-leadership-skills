---
name: capa-manager
description: Manages the full lifecycle of corrective and preventive actions (CAPA)
  for an HSE finding, nonconformity, or incident cause — grounded in ISO 45001 clause
  10.2. Use this skill whenever a user asks to build, manage, or close out a CAPA,
  write a corrective action, add a preventive action, track a nonconformity, manage
  an audit finding, build a CAPA register or action tracker, or turn an incident's
  root cause into a managed action plan. Takes findings from an audit, incident, inspection,
  or near-miss (standalone, or ingested from an incident-investigation or safety-audit
  output), confirms the root cause, derives corrective and preventive actions ranked
  by the hierarchy of controls (no PPE- or admin-only treatments without justification),
  assigns named owners and due dates, schedules an effectiveness verification for
  each, and emits a branded CAPA register. Decision-support only; a competent person
  must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
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

# CAPA Manager (Corrective & Preventive Action)

A consultant-grade HSE skill that **manages the full lifecycle of a corrective &
preventive action set** for a finding, nonconformity, or incident cause — whether
captured standalone (an inspection, a near-miss, a management review) or **ingested
from a sibling skill's output** (a `safety-audit` finding set or an
`incident-investigation` root-cause + first CAPA). It is grounded in **ISO 45001
clause 10.2** (incident, nonconformity & corrective action): for each cause it derives
**both a corrective action** (fix this occurrence) **and ≥1 preventive action** (stop
recurrence), ranks every action by the **hierarchy of controls**, assigns a **named
owner + ISO due date + measurable effectiveness measure**, and **schedules an
effectiveness verification** for each — then emits a branded **CAPA register**. Two
non-negotiables hold throughout: **de-identify first** (no analysis or drafting ever
touches raw PII/health detail — an ingested output is re-checked, never assumed clean),
and **no vague controls** (no PPE/admin-only treatment without an explicit justification;
no anonymous owner; no untraced action). Register validation and control ranking are
**deterministic** (the A7 `smart_actions` and `controls` engines), never prose judgement.

It **manages** the CAPA lifecycle; it does **not** generate the upstream artifact —
the audit is `safety-audit`'s job, the investigation is `incident-investigation`'s.
The three skills **share one CAPA schema and one engine** (`smart_actions.py`): the
siblings *produce* the register, this skill *manages* it. v1.0 manages a register
**within a single invocation** (stateless-per-run) — a persistent, cross-session CAPA
store is a v2 consideration.

## When to use this skill

Use this skill **after an audit, incident, inspection, near-miss, or management
review** — when a corrective/preventive action set needs to be built, ranked, owned,
dated, cause-traced, and effectiveness-verified, or when an existing CAPA register
needs to be managed toward defensible closure. Trigger phrases: *build / manage / close
out a CAPA, corrective action, preventive action, nonconformity, CAPA register, action
tracker, close out a finding, manage an audit finding, root cause to action,
effectiveness verification, ISO 45001 10.2*. It **ingests** a supplied
`incident-investigation` or `safety-audit` output (lifting the finding + cause id + any
first CAPA without re-keying) or **captures** a standalone finding. **Not** for running
the audit (use `safety-audit`), conducting the full investigation/RCA narrative or the
reportability verdict (use `incident-investigation`), or incident-rate dashboards (use
`incident-rate-calculator`). If the request is vague, the Workflow intake below forces
the specific finding/cause before any drafting.

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

| Jurisdiction | Read (for the documented corrective-action / record-retention duty) |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state — **resolve the STATE first (mandatory)** for the documented corrective-action / return duty) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |

This skill always grounds in **`KB-STD-ISO45001` clause 10.2** (incident,
nonconformity & corrective action — the CAPA-lifecycle core: react → evaluate the need
to eliminate the cause so it does not recur → implement corrective + preventive action
→ review effectiveness → retain documented evidence) and **clause 8.1.2** (hierarchy of
controls), and applies `KB-SNIP-HOC` to **every** corrective and preventive action
(paired with the A7 `controls.rank_controls` check). For an India site it resolves the
state via `KB-REG-IN-STATEFORMS` (**mandatory state detection** — confirm the state
before citing any documented-information duty; an un-seeded state → `[GAP]` + "verify
with a competent person", never an invented national form number). Every citation quotes
the fragment's `source`+`year`; this skill **never invents** a citation. The rule-9
manifest is `references/_skill-kb.md`.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (run this first, one question at a time)

Run the question set below one question at a time, MCQ where the answer space is
enumerable and free-text where it is open, branching on the answers (`KB-SNIP-INTAKE`).
**Never proceed on a vague finding**; record `[GAP]` for missing facts and
`[ASSUMPTION]` for anything inferred — **never invent a cause or an action**. The intake
opens with the **source gate (Q0)**; when a sibling `incident-investigation`/`safety-audit`
output is supplied it runs the **INGEST branch (Q0a)** — lifting the finding + cause
id(s) + any first CAPA + the de-identified facts instead of re-eliciting them.

| # | Question | Type | Options / branch |
|---|---|---|---|
| Q0 | **Source of the finding/cause this CAPA addresses** | MCQ | **Audit · Incident · Inspection · Near-miss · Other** — *Incident* → offer the INGEST branch (an `incident-investigation` output?); *Audit* → offer the INGEST branch (a `safety-audit` finding set?); all others → the capture path. |
| Q0a | *(if a sibling output exists)* **Supply it to ingest?** | MCQ + free-text/file | **Yes — paste/point to it · No, capture manually.** *Yes* → the **INGEST branch**: lift the finding + cause id(s) + any first CAPA + de-identified facts; skip Q2/Q3 re-elicitation; proceed to confirm + complete. |
| Q1 | **Jurisdiction** | MCQ | India · UK · USA · EU · Other/Unknown. **India → Q1a (state)** → the §kb-selection row + the documented corrective-action duty. |
| Q1a | *(India only)* **Which state?** | MCQ | Tamil Nadu · Karnataka · Maharashtra · Delhi/Central · Other — resolves `KB-REG-IN-STATEFORMS`; **mandatory state detection** — confirm before citing. |
| Q2 | **The finding / nonconformity / incident cause** (the anchor) | free-text | "State the exact finding, nonconformity, or incident cause this CAPA addresses, and against which requirement/clause (e.g. 'Audit NC-07: emergency lighting in Bay 3 not tested — ISO 45001 8.2 / local fire rule')." The **specificity anchor** — refuse to proceed on "general non-compliance". |
| Q3 | **Root cause (if known)** | free-text | "Is the root cause established? If yes, state it (or the ingested cause id RC-n). If no, I'll run a brief 5-Whys to establish one." If absent → step 3 light `rca`; if a cause id is ingested → reuse. |
| Q4 | **Proposed actions, if any** | free-text | "Any corrective or preventive actions already proposed? (I'll rank them by the hierarchy of controls and fill the gaps.)" Seeds step 4; flags any PPE/admin-only proposal for higher-order escalation. |
| Q5 | **Owners** | free-text | "Who owns each action? (named role/person — no 'TBD'.)" → `smart_actions` owner field; refuse anonymous owners. |
| Q6 | **Due dates** | free-text | "Target completion date for each action (ISO date — no 'ASAP'.)" → `smart_actions` `due`; validated ISO-8601. |
| Q7 | **Verification / effectiveness-check method** | MCQ + free-text | Re-audit · Re-inspection · Metric/KPI trend · Observation/walkdown · Document/record check · Other (+ free-text) → the `verification.method` (the lifecycle step this skill owns). |
| Q8 | **CAPA scope** | MCQ | Single action (close-out) · Multi-action register (a finding set / audit) — single = single-threaded triage; register = fan-out. |

After the last applicable question the Workflow **echoes a captured-facts summary**
("Managing CAPA for Audit NC-07 (emergency lighting, Bay 3, Maharashtra) → cause RC-1
(no PM schedule for life-safety systems); 1 corrective + 1 preventive action, owners
and dates as given, verification by re-inspection in 30 days — correct?") and proceeds
only on confirmation. On the **INGEST branch** the echo confirms what was lifted from
the sibling output before this skill completes/manages it.

### The CAPA lifecycle method (ISO 45001 10.2 — stateless-per-run)

Full method in `references/METHODOLOGY.md`. The whole lifecycle runs **within one
invocation** — ingest/capture → structure → validate → schedule → emit — with **no
persistent cross-session store** (that is v2). Steps:

1. **Structured intake** (Step 0 above) — capture facts, or **ingest** a sibling
   output; never proceed on a vague finding.
2. **De-identify FIRST (the `deid` block above — a sequential dependency).** Run the
   De-identifier over **all** inputs: detect and list every identifier; pseudonymize to
   stable role labels ("Worker A"); aggregate any injury/illness cell `<5`; emit the
   re-identification key **separately**, never in the report or any subagent prompt.
   **Every step below consumes only the scrubbed, role-labelled text.** *An ingested
   sibling output is already de-identified — the De-identifier **re-checks** it and flags
   any residual identifier rather than assuming it is clean.*
3. **Capture the finding/nonconformity/incident-cause the CAPA addresses.** Anchor the
   CAPA to the **specific** finding from intake (or the ingested one): what
   nonconformity/finding/cause occurred, where, against which requirement/clause. Flag
   `[GAP]` where the finding is vague — **never invent**. The Workflow refuses to manage
   a CAPA against "general non-compliance".
4. **Confirm/establish the root cause (optional `rca` link).** If a cause is supplied —
   an ingested `RC-n` id, or stated at intake — **confirm and reuse it** (do **not**
   re-investigate; that is `incident-investigation`). If a standalone finding has **no**
   cause, run a **light `rca.scaffold("5-whys", finding)` then `rca.validate("5-whys",
   analysis)`** (`reaches_systemic` enforced) **only** to *establish* a minimal cause so
   each action can trace to it. Emit/reuse causes as `{id: "RC-n", statement,
   evidence_ref}`. A CAPA whose actions trace to no cause is invalid.
5. **Derive corrective + preventive actions, HoC-tagged + cause-traced.** For each
   cause produce **both** a **corrective** action (`capa_type: corrective` — fix this
   occurrence) **and ≥1 preventive** action (`capa_type: preventive` — stop recurrence).
   Apply `KB-SNIP-HOC`, then call `controls.rank_controls(controls)` +
   `controls.validate_treatment(controls)` over the **full corrective + preventive set**
   (Elimination → Substitution → Engineering → Administrative → PPE; the **preventive**
   action especially favours higher-order controls). If `ppe_admin_only` is `True`, the
   Workflow **must** either add a higher-order control or record an explicit
   justification ("higher-order controls not reasonably practicable because…") — a
   **PPE/admin-only corrective or preventive treatment with no justification is a defect
   the Critic/QA pass must catch**. This is the hard enforcement of the core value, not
   a mention. Each action carries `links_to_cause: "RC-n"` and `hoc_tier`.
6. **Assign owner + due date + effectiveness measure, then validate the register (the
   core engine).** Every action gets a **named owner**, an **ISO-8601 due date**, and a
   **measurable effectiveness measure**. Call `smart_actions.validate_register(actions)`:
   any action missing an owner, a valid ISO date, a measure, or a `links_to_cause` is
   **invalid** and must be fixed — no anonymous actions, no "ASAP", no untraced action;
   `all_traced_to_cause` must be true. **The register is validated by the engine, not by
   prose.**
7. **Schedule the verification / effectiveness-check (the lifecycle step this skill
   owns).** For every action set a **`verification` `{method, due, status}`**: *how*
   effectiveness will be confirmed (re-audit, re-inspection, metric trend, observation,
   document check), *by when*, and the current `status`. Set each CAPA's `status`
   (`open` / `in-progress` / `verified-effective` / `verified-ineffective` / `closed`);
   **a CAPA cannot be `verified-effective` without a recorded check** (floor =
   method + due + status). Use `smart_actions.days_until_due(verification.due, today)` to
   flag any verification past-due in the register view. The Workflow **refuses to close a
   CAPA `verified-effective` without a recorded effectiveness check**.
8. **Validate against `references/QUALITY_CHECKLIST.md`** — the self-check before
   output: every action HoC-ranked; no un-justified PPE/admin-only treatment; every
   action owned + dated + measured + traced to a cause; **every CAPA has a scheduled
   effectiveness check**; the corrective/preventive split present per cause; every
   citation traced to the KB (ISO 45001 10.2 always); de-id applied; no conclusion on an
   unstated assumption.
9. **Assemble the branded CAPA report (A4).** Build `report.json` (see
   `assets/capa-report.template.json`) and run the canonical `report-output` call. The
   engine auto-stamps the cover, classification banner, and the limitations &
   de-identification notice.

**The CAPA action schema (reused verbatim from the sibling producers; extended
additively).** Each action is the exact `{action, owner, due, measure, links_to_cause,
hoc_tier}` shape an `incident-investigation`/`safety-audit` register emits — the first
**six fields are validated by `smart_actions.validate_register`** — extended with three
**lifecycle metadata fields this skill owns and the engine ignores**: `capa_type`
(`corrective` | `preventive`), `verification` `{method, due, status, verified_by,
verified_date}`, and `status`. These additions are **never** moved into
`smart_actions.REQUIRED_FIELDS` — doing so would fork the A7 engine and break the
round-trip. So a register round-trips between the producers and this manager **with zero
A7 change** (see `references/METHODOLOGY.md` for the ingest field-mapping).

The orchestration block (below) governs the agentic execution: for a multi-finding CAPA
register the triage gate fans out the 2 LLM jobs (Researcher/Cause-Analyst → steps 3–4;
Drafter → steps 5–7 assembling the register); for a single-action close-out it stays
single-threaded. The **deterministic steps (6 register validation via `smart_actions`;
5 control ranking via `controls`) are A7 script calls in every case — never a fan-out
job**.

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

<!-- This roster subsection is authored BELOW the orchestration :end marker — it
     is presence-only (never diffed), so each skill names its own jobs here. -->

The moderate roster (A6 "moderate = 2–3"): the **De-identifier is the sequential first
gate, not a fan-out peer**; the **2 fan-out jobs** are Researcher/Cause-Analyst +
Drafter; **Critic/QA is mandatory**. **There is no CAPA-Scorer subagent** — register
validation + control ranking are deterministic A7 calls at Workflow steps 5/6
(`controls`, `smart_actions`), not LLM fan-out work.

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all
  PII/health detail to role labels before any analysis (every fan-out job below consumes
  scrubbed text; an ingested sibling output is **re-checked**, not assumed clean).
  Returns the re-identification key SEPARATELY (to the orchestrator, never to a sibling).
- **Researcher / Cause-Analyst** — confirm or establish the root cause the CAPA traces
  to (reuse an ingested `RC-n` id if present; else a light 5-Whys via `rca.py` reaching
  a systemic factor) and gather the evidence the corrective-vs-preventive split hangs
  off; cited summary, flag `[GAP]`. SCOPE-OUT: drafting the register (Drafter); running a
  full investigation/timeline/reportability (that is `incident-investigation`). (Register
  validation + control ranking are NOT a subagent — they are the A7
  `smart_actions`/`controls` scripts.)
- **Drafter** — write the CAPA register/plan to the output template using role
  placeholders: per cause, a corrective + ≥1 preventive action, each tagged its
  `KB-SNIP-HOC` tier, each with owner + ISO due + measure + `links_to_cause` + a
  scheduled verification. SCOPE-OUT: confirming the cause (Cause-Analyst); validating the
  register (the A7 `smart_actions` script).
- **Critic/QA** (MANDATORY) — every action HoC-ranked, no PPE/admin-only corrective or
  preventive treatment without justification, every action owned + dated + measured +
  traced to a cause, **every CAPA has a scheduled effectiveness check**, every citation
  traces to the KB (ISO 45001 10.2), zero PII leaked. PASS/FAIL.

A **Regulatory-Checker** may be added as a third fan-out job for a jurisdiction-heavy
CAPA (the documented-information / corrective-action duty) and still stay in A6's
"moderate = 2–3" band. Single-subject close-outs run single-threaded — no subagents (the
de-id scrub still runs first and the Critic/QA pass is still performed).

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
