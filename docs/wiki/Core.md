# Core

`hse-core` is the everyday HSE toolbox — the ten skills that cover the artifacts a safety manager, supervisor, or consultant produces most weeks: risk assessments, JSAs, toolbox talks, audits, SOPs, RAMS, incident investigations, CAPAs, incident-rate maths, and the board paper. It is the pack to install first; every other sector pack composes on top of it. Install it with:

```
/plugin install hse-core@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

### board-safety-report
**Produces:** An executive, board-level HSE narrative report — leading & lagging indicators turned into "what changed, why it matters, what leadership must decide".
**For:** E · **Grounded in:** ISO 45001 clauses 9.1 (monitoring & performance evaluation) and 9.3 (management review) · **Packs:** hse-core
**Use when:** You are preparing a board or executive-committee safety paper, a quarterly or annual HSE performance report, a leadership/board performance review, or a management-review safety input.
**Don't use for:** Computing or dashboarding the rates themselves — use [incident-rate-calculator](#incident-rate-calculator); investigating a single event — use [incident-investigation](#incident-investigation). This skill builds the narrative *around* the numbers, not the calculation or the investigation.
**Have ready:** The reporting period and the audience body; your leading & lagging safety data (and the hours worked if you want rates computed); the period's key events and any HiPo/SIF precursors; strategic priorities; the prior-period figures and a benchmark (with its source + year); jurisdiction (India → state).
**Trigger:** "write a board safety report", "executive safety summary", "quarterly safety performance review".
**You get:** A branded PDF + Word board narrative — an executive story of what changed and what to decide, an interpreted HiPo/SIF lens, leading/lagging indicator tables as supporting evidence, trend and benchmark readings (source + year), and explicit decision asks — every incident detail de-identified and aggregated so no single event or person is identifiable.
**Pairs well with:** [incident-rate-calculator](#incident-rate-calculator) (feed it a computed rate) and [incident-investigation](#incident-investigation) (summarise its de-identified outputs at board altitude).

### capa-manager
**Produces:** A managed, validated CAPA register — corrective + preventive actions for a finding, nonconformity, or incident cause, each owned, dated, cause-traced, and scheduled for effectiveness verification.
**For:** M, C · **Grounded in:** ISO 45001 clause 10.2 (incident, nonconformity & corrective action) · **Packs:** hse-core
**Use when:** After an audit, incident, inspection, near-miss, or management review — a corrective/preventive action set needs to be built, ranked, owned, dated, cause-traced and effectiveness-verified, or an existing register needs to be managed toward defensible closure.
**Don't use for:** Running the audit — use [safety-audit](#safety-audit); conducting the full investigation/RCA or the reportability verdict — use [incident-investigation](#incident-investigation); incident-rate dashboards — use [incident-rate-calculator](#incident-rate-calculator). It *manages* the register; the siblings *produce* it.
**Have ready:** The source (standalone, or an ingestible `safety-audit` / `incident-investigation` output); the specific finding/nonconformity and its root cause; proposed actions; a named owner and an ISO due date for each; the effectiveness-verification method; jurisdiction (India → state).
**Trigger:** "build a CAPA", "close out a corrective action", "manage an audit finding".
**You get:** A branded PDF + Word CAPA register — each action tagged corrective or preventive, ranked by the hierarchy of controls (no un-justified PPE/admin-only treatment), traced to its cause (`RC-n`), carrying a named owner + ISO due date + measurable effectiveness measure, with an effectiveness verification scheduled — validated deterministically by the `smart_actions` engine.
**Pairs well with:** [safety-audit](#safety-audit) and [incident-investigation](#incident-investigation) (it ingests their finding/cause sets via one shared CAPA schema).

### incident-investigation
**Produces:** A defensible, de-identified incident investigation report — timeline, evidence log, root-cause analysis, evidence-traced causes, a hierarchy-of-controls CAPA, and the jurisdiction's reportability verdict.
**For:** M, C · **Grounded in:** ISO 45001 clause 10.2; reportability against RIDDOR / OSHA 29 CFR 1904 / India state accident forms · **Packs:** hse-core
**Use when:** After an incident, accident, or near-miss — when a root-cause analysis, a CAPA, or a reportability decision is needed for a concrete event at a named site or asset.
**Don't use for:** Live emergency response (a different skill); routine incident-rate dashboards — use [incident-rate-calculator](#incident-rate-calculator) (this skill surfaces only one *contextual* rate).
**Have ready:** The incident narrative and when/where it happened; the incident type and severity; the people involved (de-identified immediately); immediate causes; the evidence held and any permits in force; your preferred RCA method (5-Whys / ICAM / SCAT / Fishbone / Swiss-Cheese); jurisdiction (India → state); the investigation team.
**Trigger:** "investigate this incident", "run a root cause analysis", "is this reportable?".
**You get:** A branded PDF + Word investigation report — a numbered timeline and evidence log (`E-1…`), an RCA in your chosen method (with systemic reach enforced), root + contributing causes each traced to an evidence item, a HoC-ranked CAPA with named owners + ISO dates, and the reportability/notification verdict — every personal and health identifier scrubbed to role labels, the re-identification key returned separately.
**Pairs well with:** [capa-manager](#capa-manager) (hands off the validated CAPA) and [incident-rate-calculator](#incident-rate-calculator) (for the contextual rate).

### incident-rate-calculator
**Produces:** OSHA-standard lagging incident rates — TRIR, DART, and LTIFR — computed by the shared tested engine and presented verbatim, with each figure's formula, inputs, base, and optional benchmark.
**For:** M, E · **Grounded in:** OSHA recordkeeping conventions (TRIR/DART per 200,000 hours; LTIFR per 1,000,000 hours) · **Packs:** hse-core
**Use when:** You need an OSHA-standard lagging rate for a named site and period — TRIR, DART, LTIFR, a recordable or lost-time frequency rate, or a benchmark comparison against an industry figure.
**Don't use for:** Writing the board narrative around the figures — use [board-safety-report](#board-safety-report); investigating the event behind a count — use [incident-investigation](#incident-investigation); assessing a hazard — use [risk-assessment](#risk-assessment). Severity rate is out of scope (marked a deferred `[GAP]`).
**Have ready:** Which rate(s) you need; the site/scope and period; the recordability standard (India → state); the recordable / DART / lost-time counts; the **mandatory** total hours worked (no rate without it); the base convention; an optional benchmark with its source + year.
**Trigger:** "calculate our TRIR", "what's our LTIFR", "benchmark our recordable rate".
**You get:** A branded PDF + Word rate report — each rate exactly as the engine returned it (the model never does the arithmetic) alongside its formula, inputs, base and period label, plus the optional benchmark delta — so a reviewer can re-run the same inputs and reproduce the number; a zero/missing denominator surfaces an honest error, never a fake `0.0`.
**Pairs well with:** [board-safety-report](#board-safety-report) (consumes a computed rate as context for the executive narrative).

### job-safety-analysis
**Produces:** A task- and site-specific step-by-step Job Safety Analysis (JSA / JHA) — hazards, risk score, controls and residual risk assessed *per step*, consolidated into SMART actions.
**For:** M, F, C · **Grounded in:** ISO 45001 clause 6.1.2 applied per step, with the hierarchy of controls (8.1.2) at step granularity · **Packs:** hse-core
**Use when:** You need a step-by-step safety analysis of a concrete physical job — "break this welding job into steps and assess the hazards of each step", "build a JHA for working at height on the north roof".
**Don't use for:** A whole-activity risk assessment (one row per *hazard*, not per *step*) — use [risk-assessment](#risk-assessment); investigating an event that already happened — use [incident-investigation](#incident-investigation).
**Have ready:** Jurisdiction and industry; the job anchor; the **ordered step sequence** (the spine — a JSA with no steps is not a JSA); tools/materials and any SDS held; who performs each step and their competencies; the environment, permits-to-work and location; the likelihood/severity matrix; the review trigger.
**Trigger:** "build a JSA", "job hazard analysis", "step-by-step safe-work analysis".
**You get:** A branded PDF + Word JSA — the job decomposed into its ordered steps, and for each step the specific hazards, an initial risk score, HoC-ranked controls (no un-justified PPE-only step), and a re-scored residual risk — all consolidated into SMART actions with named owners and ISO due dates; scoring and ranking are deterministic via the `risk_matrix`/`controls` engines.
**Pairs well with:** [risk-assessment](#risk-assessment) (the whole-activity counterpart) and [sop-writer](#sop-writer) (turn the JSA into a procedure).

### rams-builder
**Produces:** A construction-ready RAMS — a combined Risk Assessment + Method Statement for a specific construction activity on a specific site, with a bidirectional RA↔MS cross-reference.
**For:** M, C · **Grounded in:** ISO 45001 clause 6.1.2 + the applicable construction law (UK CDM 2015 Reg 13/15, or India BOCW with the user's state form) · **Packs:** hse-core
**Use when:** You need a RAMS, a method statement, or a safe system of work for a concrete construction activity on a named site — "build a RAMS to erect a mobile tower and replace cladding on levels 2–4", "write a method statement for excavating a 1.8 m service trench".
**Don't use for:** A non-construction whole-activity assessment — use [risk-assessment](#risk-assessment); a single physical task's step analysis without the method-statement half — use [job-safety-analysis](#job-safety-analysis).
**Have ready:** Jurisdiction and CDM role; the construction-activity anchor; the site & environment; the **ordered sequence of works**; plant & equipment; personnel & competency cards; permits-to-work and existing controls / CPP; any CPP/RAMS/SDS to ingest; the matrix and the works window/RAMS validity.
**Trigger:** "build a RAMS", "write a method statement", "safe system of work for construction".
**You get:** A branded PDF + Word RAMS — the RA half (HIRA loop scored on the risk matrix, controls ranked by the hierarchy, residual re-scored) plus the MS half (the sequenced safe system of work: ordered steps, plant, competencies, permits, rescue arrangements), every method step cross-referenced to the RA rows that treat its hazards, named competent persons, and a briefing/sign-off record.
**Pairs well with:** [risk-assessment](#risk-assessment) (the RA half reuses its HIRA loop) and [permit-to-work](Process-Safety#permit-to-work) (for the permits the method demands).

### risk-assessment
**Produces:** A consultant-grade, task- and site-specific Hazard Identification & Risk Assessment (HIRA / HIRARC), with an optional ISO 14001 environmental-aspects branch.
**For:** M, C, F · **Grounded in:** ISO 45001 clause 6.1.2 (and ISO 14001 clause 6.1.2 for environmental scope) · **Packs:** hse-core
**Use when:** You need a risk assessment for a concrete task, site, or asset — "assess the risk of confined-space entry to clean Tank T-402", "build a HIRA for working at height", or an environmental aspects/impacts assessment via the scope gate.
**Don't use for:** A step-by-step single-job analysis — use [job-safety-analysis](#job-safety-analysis); a construction method statement — use [rams-builder](#rams-builder); investigating an event that occurred — use [incident-investigation](#incident-investigation).
**Have ready:** The scope gate (safety / environmental / both); jurisdiction; the task-steps anchor (the specificity anchor); location and exposure; existing controls and evidence held; task-level obligations; the likelihood/severity matrix; assessment type, assessor and owners; the review cycle.
**Trigger:** "assess this risk", "build a HIRA", "score this hazard on our 5×5 matrix".
**You get:** A branded PDF + Word risk register — one row per hazard (and optional aspect→impact pairs), an initial likelihood × severity score and band, HoC-ranked controls (no un-justified PPE-only treatment), a re-scored residual risk, and SMART actions with named owners and ISO due dates — all scored deterministically via the `risk_matrix`/`controls` engines.
**Pairs well with:** [job-safety-analysis](#job-safety-analysis), [sop-writer](#sop-writer), and [rams-builder](#rams-builder) (all reuse or ingest the HIRA output).

### safety-audit
**Produces:** A clause-by-clause safety/compliance audit report — findings classified and evidence-traced, nonconformities risk-rated, with a corrective-action CAPA register.
**For:** M, F, C · **Grounded in:** ISO 45001 clause 9.2 (internal audit); audits against ISO 45001, a regulatory regime (OSHA / Factories Act / HSWA), or a custom checklist · **Packs:** hse-core
**Use when:** You need to run a safety audit, inspection, compliance audit, management-system audit, or conformity assessment of a named site, system, or process — recording clause-by-clause findings and rating conformity.
**Don't use for:** Investigating an incident or running an RCA — use [incident-investigation](#incident-investigation); a single-task JSA — use [job-safety-analysis](#job-safety-analysis); managing an existing CAPA register's lifecycle over time — use [capa-manager](#capa-manager) (this skill *produces* the register).
**Have ready:** Jurisdiction; the scope/boundary anchor; the criteria gate (ISO 45001 / a regulatory regime / a custom checklist); the audit type; the evidence available; industry; the nonconformity-rating matrix; the audit team / lead auditor; the audit date and CAPA cycle; physical location.
**Trigger:** "run a safety audit", "compliance audit against ISO 45001", "audit this site to a checklist".
**You get:** A branded PDF + Word audit report — one finding per criterion classified on the 4-class ISO scheme (conformity / major / minor / observation / OFI), each traced to objective evidence, every nonconformity risk-rated on the matrix, an overall conformity rating, and a B5-schema CAPA register (HoC-ranked, owned, dated, finding-linked) ready for `capa-manager` to track.
**Pairs well with:** [capa-manager](#capa-manager) (ingests the validated CAPA register and tracks it to closure).

### sop-writer
**Produces:** A clear, task-specific, version-controlled Standard Operating Procedure / Safe Work Procedure — written to the reader's literacy level with the hierarchy of controls embedded into the steps.
**For:** M, C · **Grounded in:** ISO 45001 clause 8.1 (operational control) · **Packs:** hse-core
**Use when:** You need an SOP or safe work procedure for a concrete task, operation, or asset — "write an SOP for the manual print-head changeover on Press 4", "turn this JSA into a step-by-step work instruction".
**Don't use for:** Scoring risk (this skill authors a procedure, it does not run a matrix — use [risk-assessment](#risk-assessment) or [job-safety-analysis](#job-safety-analysis) first); a sequenced construction method statement — use [rams-builder](#rams-builder).
**Have ready:** Jurisdiction and industry; the task/operation anchor; an existing RA or JSA to ingest (or the hazards + controls to elicit inline); location; standards/limits; the **ordered procedure steps**; roles & competencies; the target literacy register/language; the review cycle and output type.
**Trigger:** "write an SOP", "draft a safe work procedure", "turn this JSA into a work instruction".
**You get:** A branded PDF + Word, revision-controlled, approval-ready procedure — real ordered task-specific steps (one action per step) with the controls / PPE / checks / hold-points embedded *inline* into each risk-bearing step (never a flat PPE list at the end), the higher-order controls the procedure operates within surfaced, responsibilities and competencies named by role, and emergency provisions — cross-referencing the ingested RA/JSA by id rather than re-scoring it.
**Pairs well with:** [risk-assessment](#risk-assessment) and [job-safety-analysis](#job-safety-analysis) (it ingests their hazards + rated controls as its source).

### toolbox-talk
**Produces:** A short, ready-to-deliver toolbox talk (pre-task briefing / tailgate / pre-start / take-5 / safety moment) plus a sign-off / attendance sheet, for a specific crew, task, and site.
**For:** F, M · **Grounded in:** the named task's real hazards and the hierarchy of controls (ISO 45001-aligned) · **Packs:** hse-core
**Use when:** You need a quick crew briefing before a specific task — a daily/shift safety briefing, a tailgate / pre-start / pre-job brief, or a take-5 / safety moment on a named topic.
**Don't use for:** A full hazard assessment — use [risk-assessment](#risk-assessment); a step-by-step job analysis — use [job-safety-analysis](#job-safety-analysis); investigating an event that already happened — use [incident-investigation](#incident-investigation). It briefs a crew before a task; it does not assess, file, or investigate.
**Have ready:** The topic/hazard; the trade/crew; the site & the specific task today (the specificity anchor); the duration; a recent relevant incident (never fabricated — left blank yields a clearly-labelled typical example); the reading level/language; light-touch jurisdiction.
**Trigger:** "write a toolbox talk", "tailgate / pre-start brief", "safety moment on [topic]".
**You get:** A branded, printable PDF + Word talk in a fixed 7-element structure — a hook, the specific hazard(s) of this task/site, hierarchy-of-controls-aware key controls, a de-identified (or clearly-labelled typical) incident with its one lesson, 2–3 crew discussion prompts, and 3–5 key takeaways — plus a signable attendance / sign-off sheet (Name/Role · Signature · Date) that makes the briefing auditable.
**Pairs well with:** [risk-assessment](#risk-assessment) and [job-safety-analysis](#job-safety-analysis) (brief the crew on the hazards those skills identified).
