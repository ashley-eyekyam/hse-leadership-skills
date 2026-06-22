---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-EXPOSURE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-TEMPORAL]
  omits:
    ELI-JURIS: "The publication FRAMEWORK (GRI 403 / SASB / ESRS S1), not a legal jurisdiction, governs an annual ESG disclosure — captured under ELI-OBLIGATIONS (disclosures in scope) and ELI-SCOPE (reporting boundary). Any statutory return defers to hse-india / hse-process (no national-form minting here), so no India->state branch is needed."
    ELI-INDUSTRY: "Sector selects the SASB industry standard and is captured within ELI-OBLIGATIONS (which framework/standard set applies); it does not change the OH&S disclosure method, so it is not a separate intake gate."
    ELI-LOCATION: "An organisation-and-period disclosure aggregates across all sites; per-site physical conditions are not assessed (and a per-site small cell is suppressed, not surfaced). Site is captured only as a de-id risk (ELI-EXPOSURE), not as a hazard-environment dimension."
    ELI-BASELINE: "This skill DISCLOSES period performance, it does not assess controls against a current-state baseline; no initial-vs-residual scoring applies."
    ELI-SCORING: "No risk-matrix rating is produced; the figures are lagging RATES computed deterministically by incident_rates to standard definitions, captured under ELI-EVIDENCE (denominator + definition), not a scoring scheme."
    ELI-COMPETENCY: "The competent-person / assurance-specialist review is a fixed output boundary (orchestration Step 4 + references/sme-review.md), not a per-run intake variable; named owners on improvement commitments are de-identified to roles."
  branches:
    - when: Q3
      option: own-workforce + non-employee
      activates_questions: [Q3a]
---

# Structured intake — hse-annual-esg-report

Run one question at a time; MCQ where the answer space is enumerable, free-text where it
is open; branch on the answers; **echo the captured facts back before any analysis**;
**refuse on a vague subject** (record `[ASSUMPTION]`/`[GAP]`, never invent). Canonical
runtime pattern: `KB-SNIP-INTAKE`. This is the **strictest-publication** intake: no figure
is accepted without its **denominator + reporting boundary**, and no "GRI 403" claim is
accepted without its required disclosures.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q0 | What ESG OH&S artifact, and what reporting boundary (consolidation basis)? | MCQ | full annual OH&S disclosure / a single framework section (GRI 403, ESRS S1, SASB) / a board-facing safety-performance disclosure — and operational-control / financial-control / equity-share boundary | ELI-SCOPE | always |
| Q1 | The named organisation and reporting period (the specificity anchor) | free-text | name the reporting entity + the exact period (e.g. "Acme Plc, FY2025, 1 Jan–31 Dec 2025"); refuse "our ESG section" with no named org + period | ELI-SUBJECT | always |
| Q2 | Output artifact wanted + its reader | MCQ | published annual-report section / standalone sustainability-report disclosure / board pack — reader: board / assurance provider / public | ELI-OUTPUT | always |
| Q3 | Workforce coverage to disclose (ESRS S1 mandates the split) | MCQ | own-workforce only / non-employee (contractors) only / own-workforce + non-employee | ELI-EXPOSURE | always |
| Q3a | For the own-workforce + non-employee split, confirm each population's headcount/hours basis | free-text | state hours worked + recordable counts per population so each rate has its own denominator | ELI-EXPOSURE | when Q3 = own-workforce + non-employee |
| Q4 | The figures + their denominators and sources (the refuse-on-vague gate) | free-text | for each rate (TRIR / LTIFR / DART / fatalities / ill-health): definition + denominator (hours worked) + source + period + completeness; **refuse any rate with no denominator/definition** | ELI-EVIDENCE | always |
| Q5 | Disclosures in scope + assurance-level intent + materiality basis | free-text | which GRI 403 / SASB / ESRS S1 disclosures are claimed; limited vs reasonable assurance intent; the double-materiality basis. **A "GRI 403" claim missing a required 403 disclosure is flagged [GAP] / citation hard-fail** | ELI-OBLIGATIONS | always |
| Q6 | Reporting period + comparatives + report timeline | MCQ | FY period only / + prior-period comparatives / + restatement note — and the report/assurance deadline | ELI-TEMPORAL | always |

## Echo-back
Before any analysis, echo the captured facts back and ask the user to confirm, e.g.:
"Producing: the **{Q0 artifact}** for **{Q1 org, period}** on a **{Q0 boundary}** basis,
covering **{Q3 workforce split}**, disclosing **{Q5 disclosures}** at **{Q5 assurance
level}** intent — each figure denominator-defined per Q4, comparatives per Q6. Confirm
before I begin?" Never proceed until the user confirms.

## Refuse-on-vague anchors
- **Q1 is the specificity anchor**: refuse a vague subject ("write our ESG safety
  section") — require the named organisation + the exact reporting period.
- **Q3/Q4 denominator gate**: refuse any disclosed rate with **no denominator/definition**
  and any figure with **no stated reporting boundary** — neither is assurable; never invent
  a rate or a basis.
- **Q5 framework-fidelity gate**: a **"GRI 403" claim missing a required 403 disclosure**
  is recorded `[GAP]` and is a `regulatory_citation_accuracy` hard-fail — never paper over a
  missing disclosure.
- Never proceed on a vague or missing input; record `[GAP]`/`[ASSUMPTION]`, never invent.
