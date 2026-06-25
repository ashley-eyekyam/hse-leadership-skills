# Leadership

`hse-leadership` is the leadership and safety-culture pack — the work an executive, EHS lead, or consultant does to set direction and shape culture rather than assess a single task. It covers the ISO 45001 clause-5.2 OH&S policy, a balanced leading/lagging KPI framework, safety-culture assessment against recognised maturity models, behaviour-based-safety program design, leadership safety / gemba walks, and the annual ESG occupational-health-&-safety disclosure (GRI 403 / SASB / ESRS S1).

```
/plugin install hse-leadership@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### bbs-program-designer
- **Produces:** Non-punitive BBS program design with ABC analysis, observable observation card, metrics, feedback loop, and system-fix actions.
- **For:** M, C, E · **Grounded in:** ABC/BBS method, BBS metrics catalogue, ISO 45001 clause 5.4, leadership clause map, hierarchy of controls. · **Packs:** hse-leadership.
- **Use when:** A named site, crew, or operation needs a behaviour-based safety program, observation card, peer-observation scheme, safety-conversation program, percent-safe metric, participation metric, or BBS feedback loop.
- **Don't use for:** A culture maturity assessment, leadership gemba walk, or full KPI framework; use [safety-culture-assessment](Leadership#safety-culture-assessment), [safety-walk-gemba](Leadership#safety-walk-gemba), or [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework) instead.
- **Have ready:** Named site/crew/operation, target tasks or behaviours, observable card-item wording, existing observation or incident data, observer pool, voluntary participation basis, metrics to track, jurisdiction/state where relevant, output audience, program owner, system-fix action owners, and review cycle.
- **Trigger:** "a user asks to design", "set up", "improve a behaviour-based safety / BBS / behavioural-safety / safe-behaviour-observation program".
- **You get:** ABC analysis, non-punitive observation-card design, observable behaviour list, percent-safe/participation/trend metrics with small-cell suppression, at-risk behaviour trends, hierarchy-ranked system fixes, feedback loop, and owned actions.
- **Pairs well with:** [safety-culture-assessment](Leadership#safety-culture-assessment) for culture diagnosis and [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework) for dashboarding BBS indicators.

### hse-annual-esg-report
- **Produces:** Pre-assurance annual ESG OH&S disclosure draft for GRI 403 / SASB / ESRS S1 with boundaries, denominators, suppression, and data-quality notes.
- **For:** M, C, E · **Grounded in:** GRI 403 / SASB / ESRS S1 crosswalk, ESG assurance method, ISAE 3000 / AA1000AS, ISO 45001, incident-rate benchmarks and incident_rates definitions. · **Packs:** hse-leadership.
- **Use when:** A named organisation and reporting period need an annual ESG, sustainability, GRI 403, ESRS S1, SASB, board-facing, or public OH&S performance disclosure.
- **Don't use for:** A final assurance opinion or legal sign-off; route assurance to a competent ESG/Sustainability Assurance Specialist. Use [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework) to design the underlying KPI set and [regulatory-returns](Operations#regulatory-returns) for statutory filings.
- **Have ready:** Artifact type, consolidation/reporting boundary, named organisation, exact reporting period, audience, workforce split, denominators and sources for each figure, claimed GRI/SASB/ESRS disclosures, assurance-level intent, double-materiality basis, comparatives/restatements, and report timeline.
- **Trigger:** "a user asks to build", "review an annual ESG / sustainability OH&S disclosure", "a GRI 403 health-and-safety report".
- **You get:** Disclosure crosswalk output, boundary and workforce-split statements, rate validation, data-quality table, assurance-level/materiality notes, de-id/aggregation notice, mandatory <5 small-cell and secondary suppression checks, [GAP] markers for missing disclosures, and pre-assurance disclaimer.
- **Pairs well with:** [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework) for defined metrics and [regulatory-returns](Operations#regulatory-returns) for recordkeeping source data.

### hse-policy-generator
- **Produces:** Context-fit, top-management-signed ISO 45001 clause 5.2 OH&S policy with the five mandatory commitments and communication/review note.
- **For:** M, C, E · **Grounded in:** ISO 45001 clause 5.2, ISO 14001/ISO 45003 policy variants, policy-commitments method, leadership clause map, hierarchy of controls, statutory written-policy duty branch. · **Packs:** hse-leadership.
- **Use when:** A named organisation needs to write, draft, generate, or review an OH&S, health-and-safety, environmental, psychosocial, or top-management policy commitment.
- **Don't use for:** Generic boilerplate that names no real risk, or for a signed final legal document; the policy must be owned by top management and reviewed by a competent person. Use [iso45001-gap-analysis](Operations#iso45001-gap-analysis) for broader clause readiness.
- **Have ready:** Policy standard selector, named organisation and scale, sector, actual significant risks, jurisdiction/state where relevant, worker-representation context, legal and other requirements, output audience, top-management signatory role/title, communication method, and review cycle.
- **Trigger:** "a user asks to write", "review an OH&S / health-and-safety policy", "a safety policy statement".
- **You get:** Clause-5.2 policy text, five mandatory commitments, context-fit risk references, hierarchy-of-controls commitment, statutory written-policy note where relevant, top-management signatory role, communication/review block, and boilerplate/gap checks.
- **Pairs well with:** [iso45001-gap-analysis](Operations#iso45001-gap-analysis) for certification readiness and [safety-walk-gemba](Leadership#safety-walk-gemba) for visible leadership commitment.

### leading-lagging-kpi-framework
- **Produces:** Balanced leading/lagging HSE KPI framework with fully defined indicators, targets, anti-gaming safeguards, and road-safety branch when in scope.
- **For:** M, E, C · **Grounded in:** ISO 45001 clause 9.1, KPI-design method, leading-indicators catalogue, leadership clause map, incident_rates definitions, ISO 39001 road-safety indicator branch. · **Packs:** hse-leadership.
- **Use when:** A named organisation, function, site, or fleet needs to design, normalise, rebalance, or define an HSE KPI framework or dashboard.
- **Don't use for:** Computing a given injury rate; use [incident-rate-calculator](Core#incident-rate-calculator). Use [process-safety-kpi](Process-Safety#process-safety-kpi) for API RP 754 tiers and domain SPI frameworks where those are the real scope.
- **Have ready:** KPI-design scope, named entity and reporting period, leading indicators, lagging indicators, formula/source/frequency/owner/target for each indicator, anti-gaming safeguards, culture maturity, benchmarks, output format, sector, monitoring standard/jurisdiction, and road-safety or India state details where relevant.
- **Trigger:** "Designs and normalises a balanced leading/lagging HSE KPI framework for a named organisation", "site against ISO 45001:2018 clause 9.1 — never a lagging-only set".
- **You get:** Balanced KPI table, per-indicator definitions, leading/lagging mix matched to maturity, target and anti-gaming checks, road-safety indicators when selected, RAG/dashboard-ready fields, benchmark/source gaps, and routes for rate calculators.
- **Pairs well with:** [hse-annual-esg-report](Leadership#hse-annual-esg-report) for publication metrics, [bbs-program-designer](Leadership#bbs-program-designer) for BBS indicators, and [safety-walk-gemba](Leadership#safety-walk-gemba) for commitment-closure leading indicators.

### safety-culture-assessment
- **Produces:** Safety-culture assessment or Schein diagnosis with model/lens mapping, triangulated evidence, confidentiality safeguards, and advancement roadmap.
- **For:** M, C · **Grounded in:** Bradley, Hudson/Hearts-and-Minds, Westrum, and Schein culture models; culture-maturity bands; leading-indicators catalogue; ISO 45001 clauses 5.1 and 5.4; hierarchy of controls. · **Packs:** hse-leadership.
- **Use when:** A named organisation, site, or business unit needs safety-culture or safety-climate assessment, culture survey design, maturity benchmarking, Bradley/Hudson/Westrum placement, Schein diagnosis, or advancement roadmap.
- **Don't use for:** A BBS observation program, a single leadership walk, or KPI framework; use [bbs-program-designer](Leadership#bbs-program-designer), [safety-walk-gemba](Leadership#safety-walk-gemba), or [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework). Do not produce a maturity rating from one weak evidence source.
- **Have ready:** Named population or sampling plan, model/lens choice, at least two data sources, confidentiality threshold, known context, comparison cohorts, jurisdiction/state where relevant, banding scale, output reader, assessor role, roadmap owners, and review cycle.
- **Trigger:** "a user asks to assess", "measure safety culture", "safety climate".
- **You get:** Confidentiality statement, model/lens rationale, source triangulation check, maturity band or Schein gap diagnosis, systemic drivers, small-cohort suppression, advancement controls, leading indicators, SMART roadmap, and sibling cross-reference.
- **Pairs well with:** [bbs-program-designer](Leadership#bbs-program-designer) to operationalise observation programs, [safety-walk-gemba](Leadership#safety-walk-gemba) for leadership walks, and [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework) to track advancement.

### safety-walk-gemba
- **Produces:** Leadership safety/gemba walk plan and/or record with open prompts, role-labelled concerns, tracked commitments, and closure leading indicator.
- **For:** M, E, F · **Grounded in:** ISO 45001 clauses 5.1 and 5.4, HSE HSG65 felt leadership, gemba prompt bank, leadership clause map, leading-indicators catalogue, hierarchy of controls. · **Packs:** hse-leadership.
- **Use when:** A leader, manager, or supervisor wants an engagement safety walk, gemba walk, felt-leadership round, leadership site visit, worker-engagement walk, safety conversation, or walk-and-talk for a named area/task/shift.
- **Don't use for:** A tick-box inspection/audit, BBS program, culture survey, or KPI framework; use [safety-audit](Core#safety-audit), [bbs-program-designer](Leadership#bbs-program-designer), [safety-culture-assessment](Leadership#safety-culture-assessment), or [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework).
- **Have ready:** Confirmation this is an engagement walk, named area/task/shift, walk purpose/prompt family, exposed group labels, jurisdiction/state where relevant, desired artifact, walk leader role, commitment owners, closure cadence, and next-walk date.
- **Trigger:** "a leader", "supervisor wants to run a felt-leadership safety walk", "a gemba walk".
- **You get:** Area-specific open prompt set, pre-walk plan, role-labelled concern capture, commitment register, SMART actions with owners/dates, closure cadence, commitment-count/closure-rate leading indicator, and tick-box/audit routing guard.
- **Pairs well with:** [safety-culture-assessment](Leadership#safety-culture-assessment) for culture evidence and [leading-lagging-kpi-framework](Leadership#leading-lagging-kpi-framework) for tracking commitment closure.
