---
sme-review:
  personas:
    - role: "HSE Leadership / Engagement Coach"
      expertise: "Felt-leadership / visible safety leadership (HSE HSG65), gemba / genchi-genbutsu engagement walks, ISO 45001:2018 clauses 5.1 (leadership and commitment) and 5.4 (consultation and participation of workers), psychological safety in frontline conversations, and converting leadership commitments into tracked leading-indicator actions."
      lens: "Is this an engagement walk built on OPEN, area-specific conversation prompts (never a closed yes/no tick-box checklist), with worker concerns captured role-labelled (no individual named, psychological safety preserved), and EVERY commitment converted to an owned, dated action tracked to closure whose closure-rate is reported as a leading indicator?"
---

# SME Review & Sign-off — safety-walk-gemba

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`) into an **HSE Leadership / Engagement Coach**. The
universal hard gates (de-id leak, citation accuracy, hierarchy of controls / no
lower-order-only control without justification, owned-and-dated actions) are the enforced
class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Open prompts, not a tick-box** — the walk is built from open, area-specific,
  non-interrogative questions that invite the worker's own account. A **closed yes/no
  checklist** (an inspection, not a gemba walk) is a FLAG (specificity · defensibility).
- [ ] **Concerns role-labelled** — every worker concern is attributed to a **role/group**,
  never to a nameable individual. A named-worker→concern attribution is a FLAG and a
  `de_identification` hard-fail (psychological safety).
- [ ] **Every commitment tracked** — each commitment made on the walk is converted to an
  **owned + dated** action tracked to closure. A commitment with **no owner / no due date /
  no closure tracking** is a FLAG (defensibility) — a walk that produces no tracked
  commitment fails the gate.
- [ ] **Closure-rate as a leading indicator** — the count and closure-rate of walk
  commitments is reported as a **leading indicator** (`KB-DATA-LEADING-INDICATORS`, source +
  year). Treating the walk as a one-off conversation with no forward measure is a FLAG.
- [ ] **Right tool** — this is an engagement walk, not an audit (`safety-audit`), a
  behaviour-observation programme (`bbs-program-designer`), a maturity survey
  (`safety-culture-assessment`), or a KPI framework (`leading-lagging-kpi-framework`). A
  walk that has drifted into one of those is a FLAG (steer to the right sibling).
- [ ] **Clause fidelity** — the walk is framed against ISO 45001:2018 **5.1 / 5.4**
  (`KB-SNIP-LEADERSHIP-CLAUSE-MAP`); a citation drift or a fabricated clause is a FLAG.

## Sign-off note
SME review: ran (persona: HSE Leadership / Engagement Coach); this is **decision-support
only**. It **precedes — and never replaces — the human competent-person sign-off**, and it
never asserts that the output has already been signed off. A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted
score below threshold) are a separate enforcement class.
