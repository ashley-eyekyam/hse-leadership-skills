---
name: safety-audit
description: Conducts consultant-grade safety and compliance audits of a specific
  site, system, or process against a defined standard or checklist. Use this skill
  whenever a user asks to run a safety audit, an inspection, a compliance audit, a
  management-system audit, or a conformity assessment; to audit a site or process
  against ISO 45001, a regulation, or a custom checklist; to record clause-by-clause
  findings, nonconformities (major or minor), observations, or opportunities for improvement;
  to rate conformity; or to produce an audit report with corrective actions. Grounds
  the audit method in ISO 45001 clause 9.2 (internal audit), traces every finding
  to objective evidence, risk-rates each nonconformity, and drives corrective actions
  through the hierarchy of controls (no PPE-only treatments without justification)
  with named owners and due dates — emitting a branded audit report. Decision-support
  only; a competent person must review the output.
license: Apache-2.0
metadata:
  author: eyekyam
  version: '1.0'
  category: compliance
  tier: 1
  audience:
  - M
  - F
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

# Safety Audit (conformity assessment against a standard or checklist)

A consultant-grade HSE skill that audits a **specific** site, system, or process against a defined standard or checklist and produces a **clause-by-clause audit report**. It grounds the audit method in ISO 45001 clause 9.2 (internal audit), traces **every finding to objective evidence**, risk-rates each nonconformity, and drives corrective actions through the **full hierarchy of controls** — the single lever that separates a defensible audit from copy-paste paperwork. An audit finding with no evidence trail is, by definition, indefensible; this skill refuses to produce one.

## When to use this skill

Use this skill whenever a user asks to:

- Run a **safety audit, inspection, compliance audit, management-system audit, or conformity assessment** of a named site, system, or process.
- Audit something **against ISO 45001, a regulation (OSHA / Factories Act / HSWA), or a custom checklist**.
- Record **clause-by-clause findings** — conformity, nonconformity (major or minor), observation, or opportunity for improvement — each traced to evidence.
- **Rate conformity** for an audited scope, or produce an **audit report with corrective actions** (a CAPA register).

Do **not** use this skill to investigate an incident or run a root-cause analysis (that is `incident-investigation` / B5), to build a single-task JSA (`job-safety-analysis`), or to manage an existing CAPA register's lifecycle over time (`capa-manager` / B7 — this skill *produces* the register B7 then tracks). If the request is vague ("audit the site"), the Workflow intake below forces the specific scope and the audit criteria before any drafting.

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

| Jurisdiction / criteria | Read |
|---|---|
| India | ../../knowledge-base/regulatory/in-factories-act.md (+ in-state-forms.md for the user's state — **mandatory state detection** before citing any form) |
| UK    | ../../knowledge-base/regulatory/uk-hswa.md |
| USA   | ../../knowledge-base/regulatory/us-osha.md |
| EU    | ../../knowledge-base/regulatory/eu-osh.md |
| Unknown | Ask before citing any specific law |
| Audit method (always) | ../../knowledge-base/standards/iso-45001.md (KB-STD-ISO45001, clause 9.2 — internal audit: the method backbone, scope→criteria→evidence→findings→reporting) |
| Criteria = ISO 45001 (Q-Crit) | ../../knowledge-base/standards/iso-45001.md (the audited clauses — e.g. 6.1.2, 7.2, 8.1, 9.1 — become the criteria set the audit walks; distinct from 9.2, the method) |
| Criteria = custom checklist (Q-Crit) | Use the user-supplied checklist items as the criteria set; cite **no** external clause beyond what the user names (a private checklist has no KB fragment) |

**Method vs criteria (the distinction this skill turns on):** ISO 45001 **9.2** is always the *method* (how the audit is planned and conducted). The *criteria* — what is audited **against** — are chosen at intake (Q-Crit): ISO 45001 itself, a regulatory regime, or a custom checklist. The same 9.2 loop audits a site against any of them.

## Workflow

Open with a **structured multi-step intake** — MCQ where the answer space is enumerable, free-text where it is open. Ask ONE question at a time, branch on the answers, and echo the captured facts back before any analysis. Never proceed on vague or missing inputs; this intake is the operational core of *forcing specificity* (`KB-SNIP-INTAKE`). (Intake is a Workflow convention, not a sixth block.)

### Step 0 — Structured intake (one at a time; branch; echo back; never proceed on vague)

The full typed, branched intake — the `intake-coverage` manifest, the question table
(jurisdiction · the **scope/boundary anchor Q-Scope** · the **criteria gate Q-Crit** ·
audit type · evidence available · industry · nonconformity-rating matrix · the **audit
team / lead auditor Q-Team** · the **audit date + CAPA cycle Q-When** · physical location),
the **mandatory India→state branch** (Q-Juris = India → Q-Juris-a), the **criteria-gate
branches** (Q-Crit = ISO 45001 → `KB-STD-ISO45001`; A regulatory regime → the jurisdiction
fragment; A custom checklist → no external clause), the echo-back, and the refuse-on-vague
anchors — lives in **`references/intake.md`**. Run it one question at a time, branch on
the answers, **echo the captured facts back before any analysis**, and **refuse to
proceed** on a vague scope ("general site audit") or an undeclared criteria set (Q-Scope
and Q-Crit are load-bearing — record `[GAP]`, never invent a clause). An audit with no
defined boundary is unauditable; one with no criteria set cannot classify a finding.

### The audit method (ISO 45001 9.2 internal-audit loop)

Full method — finding-classification rules, sampling guidance, evidence-sufficiency tests — in `references/METHODOLOGY.md`. The steps:

1. **De-identify the inputs FIRST** (the `deid` block + the De-identifier-runs-first rule). Audit evidence routinely carries worker names, signatures, training/injury records — scrub all of it to role labels before any assessment; everything downstream (every finding, every quoted evidence item) consumes the scrubbed text. A personal identifier surviving into a finding's evidence trail is a de-id auto-fail.
2. **Establish the scope & criteria set.** Fix the boundary (Q-Scope) and resolve Q-Crit into a concrete, walkable clause/checklist list: ISO 45001 → the relevant clauses from `KB-STD-ISO45001`; a regulatory regime → the duties from the matched jurisdiction fragment; a custom checklist → the user's items. State the audit type (Q-Type) and methodology (interview / document review / observation / sampling). Record `[GAP]` where the criteria set is incomplete — **never invent a clause**.
3. **Gather & assess objective evidence per criterion.** For each clause/checklist item, assess the available evidence **against that specific criterion**: what it shows, whether it is sufficient, what is missing. Each assessment names the specific evidence item (document id, observation, interview-role, record) it rests on. Flag `[GAP]` where evidence is absent — an unassessed criterion is "insufficient evidence," **never silently passed**.
4. **Record one finding per criterion, each classified + traced to evidence (the defensibility core).** Classify with the 4-class ISO scheme:
   - **Conformity** — evidence demonstrates the requirement is met.
   - **Nonconformity — Major** — a systemic failure or total absence of a required arrangement.
   - **Nonconformity — Minor** — an isolated lapse against an otherwise-conforming arrangement.
   - **Observation** — conforming now, but a risk of drift / an early warning.
   - **Opportunity for improvement** — conforming, but a better practice is available.
   Every finding names the **clause/checklist item, the objective evidence, and the classification**. **Risk-rate EVERY nonconformity by default** via `risk_matrix.load_matrix(config)` then `risk_matrix.score(likelihood, severity, matrix)` (config from Q-NCrate, default 5×5) so remediation can be prioritised — the band is the engine's, not prose. Conformities/observations need no score.
5. **Rate overall conformity.** Count by classification; derive a conformity rating for the scope (conformity % of assessed criteria, count of major/minor nonconformities, highest residual nonconformity risk band) — computed from the per-finding ratings, not asserted in prose.
6. **Corrective actions (HoC, owners + dates) + emit the CAPA register.** For **every nonconformity** (and any observation the auditor elects to action), apply `KB-SNIP-HOC` (Elimination → Substitution → Engineering → Administrative → PPE), then call `controls.rank_controls(controls)` + `controls.validate_treatment(controls)`. If `ppe_admin_only` is `True`, **add a higher-order control or record an explicit justification** — an un-justified lower-order-only treatment is a defect the Critic/QA pass catches. Each action is SMART (named owner + ISO due date + measure) linked to its **finding id**; assemble the CAPA register and call `smart_actions.validate_register(actions)`. The register uses the **B5 schema verbatim** — `{action, owner, due, measure, links_to_cause, hoc_tier}`, where `links_to_cause` is the **finding id**. Any action missing an owner, a valid date, a measure, or a finding link is **invalid** and must be fixed (no anonymous actions, no "ASAP"). *This validated register is the handoff artifact `capa-manager` (B7) ingests — B6 creates and validates it; B7 tracks and closes it.*
7. **Validate against `references/QUALITY_CHECKLIST.md`** — every criterion assessed (or `[GAP]`-flagged); every finding classified + evidence-traced + (if a nonconformity) risk-rated; every corrective action HoC-ranked, owned, dated, finding-linked; no un-justified lower-order-only treatment; every cited criterion traces to the KB (9.2 method always; the audited clauses / jurisdiction fragment for the criteria); de-id applied.
8. **Assemble the branded audit report** — build `report.json` (see `assets/audit-report.template.json`) and run the canonical `report-output` call.

The **orchestration block below** sits after this Workflow so the triage gate judges the assembled work before fanning out. The deterministic rating/ranking steps (4 risk-rating via `risk_matrix`; 6 ranking via `controls`, register validation via `smart_actions`) are **A7 script calls in every case — never a fan-out job** (there is no "Conformity-Scorer" subagent: deterministic work runs in the script).

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

The standard **moderate roster** (A6 "moderate = 2–3"). The De-identifier is the **sequential first gate, not a fan-out peer**; the 3 fan-out jobs are Evidence-Assessor + Regulatory-Checker + Drafter; Critic/QA is mandatory. **There is no Conformity-Scorer** — nonconformity risk-rating, control ranking, and CAPA-register validation are deterministic A7 script calls at steps 4/6 (the project's core value: deterministic work runs in the script).

- **De-identifier** — runs FIRST (sequential gate, not a fan-out peer); scrub all PII/health detail in the audit evidence (names, signatures, training/injury records) to role labels before any assessment. Every fan-out job below consumes only its scrubbed output.
- **Evidence-Assessor** — for each criterion in the resolved criteria set, assess the scrubbed objective evidence against that specific clause/checklist item: what it shows, sufficiency, what is missing; cite the specific evidence item per assessment; flag `[GAP]` where evidence is absent. SCOPE-OUT: law/criteria wording (Regulatory-Checker owns it), drafting the report (Drafter owns it). (Conformity rating is NOT a subagent — it is the A7 `risk_matrix`/`controls` scripts.)
- **Regulatory-Checker** — for the resolved jurisdiction + criteria, return the applicable duty + clause/section + (India → resolved STATE first) the state form via `KB-REG-IN-STATEFORMS`, and confirm each cited clause exists; conservative — flag `[GAP]` when unsure. SCOPE-OUT: assessing evidence (Evidence-Assessor), drafting (Drafter), inventing a form number.
- **Drafter** — write the clause-by-clause findings + nonconformity log + conformity summary + corrective-action plan + CAPA register to the output template using role placeholders; each finding tagged its classification + evidence trail, each control tagged its `KB-SNIP-HOC` tier (consumes the De-identifier's scrubbed text + the Evidence-Assessor's per-criterion assessments + the A7 `risk_matrix`/`controls` ratings + the Regulatory-Checker's verdict). SCOPE-OUT: assessing evidence (Evidence-Assessor), checking law (Regulatory-Checker).
- **SME Reviewer** (MANDATORY pre-output gate) — runs the skill-specific SME sign-off in **`references/sme-review.md`** (lead auditor, ISO 19011 / ISO 45001 9.2) before any output: every finding traced to OBJECTIVE evidence against a named criterion, classified correctly (major vs minor NC vs observation vs OFI), every nonconformity risk-rated, and the emitted CAPA register handoff-clean for the B6→B7 seam.
- **Critic/QA** (MANDATORY) — every criterion assessed or `[GAP]`-flagged, every finding classified + traced to objective evidence, every nonconformity risk-rated (via the A7 engine), every corrective action HoC-ranked + owned + dated + finding-linked, no PPE/admin-only treatment without justification, every cited clause traces to the KB, zero PII/health leak. PASS/FAIL.

Single-thread fallback (the block's canonical line): on a host with no subagent capability, the same jobs run sequentially in one context — De-identifier scrub first, the A7 rating/ranking/validation calls still made deterministically, scope discipline kept, the Critic/QA pass still performed. (This skill is *not* single-threaded-by-design; it ships the roster above.)

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
