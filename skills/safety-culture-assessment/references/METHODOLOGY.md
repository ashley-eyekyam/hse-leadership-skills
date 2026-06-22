# Methodology — Safety Culture Assessment (maturity models + the Schein lens)

The domain method the skill applies. It grounds in four recognised culture lenses (cited
as **method, not law**) and refuses to produce a maturity *rating* without a named model,
a named population, and **≥2 triangulated data sources**. Knowledge: `KB-SNIP-CULTURE-MODELS`
(descriptors + probes), `KB-DATA-CULTURE-MATURITY` (bands + the Schein gap rubric),
`KB-DATA-LEADING-INDICATORS` (advancement tracking), `KB-SNIP-LEADERSHIP-CLAUSE-MAP`
(ISO 45001 5.1 / 5.4).

## The four lenses

- **DuPont Bradley Curve** *(cited: DuPont Sustainable Solutions, Bradley Curve method)* —
  four progressive maturity stages defined by **where ownership of safety sits**:
  Reactive (instinct/compliance, delegated to the safety manager) → Dependent (supervision,
  rules & discipline) → Independent (personal commitment, self) → Interdependent (teams,
  others'-keeper). Probe: *"Who is seen to own safety here — the safety dept, supervisors,
  each worker, or the team?"*
- **Hudson / Parker "Hearts & Minds" ladder** *(cited: Patrick Hudson, Leiden Univ. /
  Shell)* — five rungs (built on Westrum): Pathological → Reactive → Calculative →
  Proactive → Generative, read through four behaviours per rung (leadership thinking,
  worker action, information flow, how incidents are treated).
- **Westrum organisational typology** *(cited: Ron Westrum, BMJ Qual Saf 2004)* — three
  types defined by **how information flows**: Pathological (information hidden, messengers
  shot) → Bureaucratic (information ignored, blame) → Generative (information sought,
  inquiry). Hudson's 5-rung ladder extends this 3-type typology — present them as related,
  not competing.
- **Schein three levels of culture** *(cited: Edgar H. Schein, Organizational Culture and
  Leadership)* — a **diagnostic-levels lens, NOT a maturity ladder** (D-05): Artifacts
  (visible structures/processes) · **Espoused** beliefs & values (stated strategies,
  "safety first" slogans, policy) · Basic underlying assumptions (the taken-for-granted
  beliefs that actually drive behaviour).

## The Schein test (D-05) — espoused-vs-enacted gap

Schein is **selectable** as the primary lens and **combinable** with any ladder as a
triangulation lens. The test compares the **espoused values** (level 2 — what the
organisation *says* it values: slogans, policy, "safety is our #1 priority") against the
**underlying assumption enacted** in artifacts and behaviour (levels 1 & 3 — what actually
wins when schedule and safety collide on a real job). A wide **espoused-vs-enacted gap**
(e.g. "safety first" espoused, but a production-pressure assumption enacted) is the key
diagnostic finding and **the advancement-roadmap input**. Standalone Schein output is a
**three-levels diagnosis of named gaps — NOT a maturity rating**. Do not assign a "Schein
Level 4" or fold Schein into a ladder band.

## Steps

1. **De-identify FIRST** — apply `references/deid-checklist.md`: suppress any cohort
   breakdown <5 (secondary suppression), scrub every individual to a role/group/cohort
   label, never reproduce an identifying verbatim quote. Everything downstream consumes
   only the scrubbed, aggregated text. No individual is named as "the culture problem".
2. **Confirm the refuse gate** — a named model/lens (intake Q2), a named population (Q1),
   and **≥2 triangulated data sources** (Q3). If only a single survey exists, **refuse to
   rate**: record `[GAP]`, ask for corroborating observation/records, and offer a Schein
   *diagnosis* of named gaps instead of a band. Never invent a rating.
3. **Map (rating) or diagnose (Schein)** — for a ladder model, band the triangulated
   evidence against `KB-DATA-CULTURE-MATURITY` (quote `source`+`year`) using
   `KB-SNIP-CULTURE-MODELS` descriptors/probes. For Schein, run the espoused-vs-enacted
   gap rubric above and name the gaps.
4. **Locate systemic drivers** — name **what in the leadership system / work design** holds
   the culture where it is (ownership of safety, Westrum information flow, how bad news is
   treated, worker consultation under ISO 45001 5.4). Attribute to roles/groups and
   systems; flag `[GAP]` where evidence is thin.
5. **Advancement controls (hierarchy lever)** — apply `KB-SNIP-HOC`, then
   `controls.rank_controls` + `controls.validate_treatment`. Systemic leadership-system /
   work-design changes (felt-leadership cadence, fixing the consequence system, genuine
   consultation, closing the espoused-vs-enacted gap) rank **above** awareness campaigns. A
   poster-campaign-only roadmap is a defect the Critic/QA + SME pass must catch.
6. **SMART roadmap** — each advancement move → a SMART action (named role-label owner +
   ISO due date + measure) via `smart_actions.validate_register`, tied to a **leading
   indicator** from `KB-DATA-LEADING-INDICATORS` so advancement is measured, not asserted.
7. **Validate** against `references/QUALITY_CHECKLIST.md`, then assemble the branded
   report (`assets/report.json`) with a confidentiality statement and the sibling
   cross-reference (`bbs-program-designer` · `safety-walk-gemba` ·
   `leading-lagging-kpi-framework`).
