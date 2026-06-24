# Leadership

`hse-leadership` is the leadership and safety-culture pack — the work an executive, EHS lead, or consultant does to set direction and shape culture rather than assess a single task. It covers the ISO 45001 clause-5.2 OH&S policy, a balanced leading/lagging KPI framework, safety-culture assessment against recognised maturity models, behaviour-based-safety program design, leadership safety / gemba walks, and the annual ESG occupational-health-&-safety disclosure (GRI 403 / SASB / ESRS S1).

```
/plugin install hse-leadership@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### bbs-program-designer
- **Produces:** Designs a non-punitive behaviour-based-safety (BBS) program for a named site, crew, or operation — ABC (antecedent-behaviour-consequence) analysis, an observable observation-card design, defined metrics (percent-safe, participation, trend-by-category), and at-risk behaviours trended to systemic causes and routed to hierarchy-ranked system fixes.
- **For:** M, C, E · **Packs:** hse-leadership · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "set up"; "improve a behaviour-based safety / BBS / behavioural-safety / safe-behaviour-observation program"
- **Summary:** Designs a non-punitive behaviour-based-safety (BBS) program for a named site, crew, or operation — ABC (antecedent-behaviour-consequence) analysis, an observable observation-card design, defined metrics (percent-safe, participation, trend-by-category), and at-risk behaviours trended to systemic causes and routed to hierarchy-ranked system fixes. Use this skill whenever a user asks to design, set up, or improve a behaviour-based safety / BBS / behavioural-safety / safe-behaviour-observation program, an observation card, peer-observation or safety-conversation scheme, or to define BBS metrics and feedback loops. Observation cards are non-punitive by design — role-labelled or anonymous, voluntary, used for trending and learning, never individual discipline; observable site-specific behaviours only (never 'work safely'); at-risk behaviours route to system fixes via the controls engine (hierarchy of controls), never to 'retrain the worker'. Decision-support only; a competent person must review the output.

### hse-annual-esg-report
- **Produces:** Produces a consultant-grade, assurance-ready annual ESG occupational-health-&-safety disclosure for a named organisation and reporting period — a GRI 403 / SASB / ESRS S1 OH&S report with defined boundaries, denominators, and no back-calculable small cell.
- **For:** M, C, E · **Packs:** hse-leadership · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review an annual ESG / sustainability OH&S disclosure"; "a GRI 403 health-and-safety report"
- **Summary:** Produces a consultant-grade, assurance-ready annual ESG occupational-health-&-safety disclosure for a named organisation and reporting period — a GRI 403 / SASB / ESRS S1 OH&S report with defined boundaries, denominators, and no back-calculable small cell. Use this skill whenever a user asks to build or review an annual ESG / sustainability OH&S disclosure, a GRI 403 health-and-safety report, an ESRS S1 own-workforce safety section, a SASB workforce-health-and-safety metric set, or a board-facing annual safety-performance disclosure. It reuses the GRI 403 / SASB / ESRS S1 disclosure crosswalk, applies the ISAE 3000 / AA1000AS assurance method (level, boundary, data-quality, materiality), validates every lagging rate to a standard definition and denominator, and applies the strictest publication de-identification tier — mandatory <5 small-cell plus secondary suppression so no suppressed cell can be back-calculated from a total. Decision-support only; a competent person must review before publication.

### hse-policy-generator
- **Produces:** Produces a top-management-signed ISO 45001:2018 clause-5.2 OH&S policy for a named organisation, with all five mandatory clause-5.2 commitments, context-fit to the org's actual risks and scale (never boilerplate).
- **For:** M, C, E · **Packs:** hse-leadership · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "review an OH&S / health-and-safety policy"; "a safety policy statement"
- **Summary:** Produces a top-management-signed ISO 45001:2018 clause-5.2 OH&S policy for a named organisation, with all five mandatory clause-5.2 commitments, context-fit to the org's actual risks and scale (never boilerplate). Use this skill whenever a user asks to write, draft, generate, or review an OH&S / health-and-safety policy, a safety policy statement, an environmental (ISO 14001 5.2) or psychosocial (ISO 45003) policy, or a top-management policy commitment. It runs a structured intake, refuses a generic boilerplate policy that names no real risk, assembles the five mandatory commitments (objectives framework, legal+other requirements, eliminate hazards/reduce risk via the hierarchy of controls, continual improvement, worker consultation/participation), defers the India statutory written-policy duty to hse-india (state detection first, no national-form minting), and emits a documented, communicated, top-management-signed policy as a branded report. Decision-support only; a competent person must review the output.

### leading-lagging-kpi-framework
- **Produces:** Designs and normalises a balanced leading/lagging HSE KPI framework for a named organisation, function, or site against ISO 45001:2018 clause 9.1 — never a lagging-only set.
- **For:** M, E, C · **Packs:** hse-leadership · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Designs and normalises a balanced leading/lagging HSE KPI framework for a named organisation"; "site against ISO 45001:2018 clause 9.1 — never a lagging-only set"
- **Summary:** Designs and normalises a balanced leading/lagging HSE KPI framework for a named organisation, function, or site against ISO 45001:2018 clause 9.1 — never a lagging-only set. Each indicator is fully defined (formula, source, frequency, owner, target); a lagging-only request is flagged for balance and a gameable metric (raw incident count as a target) with no safeguard is flagged for defensibility. Carries a road-safety leading-indicator branch (ISO 39001:2012) when the scope is road/transport/fleet. It DESIGNS the indicator set — distinct from incident-rate-calculator (which computes given rates) and process-safety-kpi (API RP 754 tiers), which it references as exemplars, not replacements. Lagging rates are computed by the incident_rates engine to standard definitions, never invented. Decision-support only; a competent person must review the output.

### safety-culture-assessment
- **Produces:** Produces a consultant-grade safety-culture assessment for a named organisation, site, or business unit — designing a survey, mapping results to a maturity model (DuPont Bradley / Hudson Hearts-and-Minds / Westrum) or the Schein three-levels diagnostic lens, triangulating at least two data sources, and emitting a defensible advancement roadmap.
- **For:** M, C · **Packs:** hse-leadership · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "measure safety culture"; "safety climate"
- **Summary:** Produces a consultant-grade safety-culture assessment for a named organisation, site, or business unit — designing a survey, mapping results to a maturity model (DuPont Bradley / Hudson Hearts-and-Minds / Westrum) or the Schein three-levels diagnostic lens, triangulating at least two data sources, and emitting a defensible advancement roadmap. Use this skill whenever a user asks to assess, diagnose, benchmark, or measure safety culture or safety climate, run a culture-maturity assessment, design a culture survey, or place an organisation on a Bradley/Hudson/Westrum ladder or against Schein's three levels of culture. It refuses to produce a maturity rating from a single survey (requiring a model, a named population, and >=2 triangulated data sources), suppresses any sub-5 respondent cohort to protect confidentiality, drives a systemic advancement roadmap with named owners and dates, and emits a branded report. Decision-support only; a competent person must review the output.

### safety-walk-gemba
- **Produces:** Designs and runs a consultant-grade leadership safety walk / gemba walk (genchi-genbutsu "go and see") for a named area, task, or shift.
- **For:** M, E, F · **Packs:** hse-leadership · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "a leader"; "supervisor wants to run a felt-leadership safety walk"; "a gemba walk"
- **Summary:** Designs and runs a consultant-grade leadership safety walk / gemba walk (genchi-genbutsu "go and see") for a named area, task, or shift. Use this skill whenever a leader, manager, or supervisor wants to run a felt-leadership safety walk, a gemba walk, a leadership site visit, a safety conversation or engagement walk, or a worker-engagement / felt-leadership round — NOT a tick-box safety inspection or audit. It builds the walk from OPEN conversation prompts (engagement, never a closed yes/no checklist), captures worker concerns role-labelled to protect psychological safety, and converts every commitment made on the walk into an owned, dated smart_actions action tracked to closure — the count and closure-rate of which is itself a leading indicator. Grounded in ISO 45001:2018 clauses 5.1 (leadership and commitment) and 5.4 (consultation and participation of workers) and HSE HSG65 felt leadership. Decision-support only; a competent person must review the output.
