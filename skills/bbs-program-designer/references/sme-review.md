---
sme-review:
  personas:
    - role: "Behavioural Safety Consultant"
      expertise: "Behaviour-based safety program design — ABC (antecedent-behaviour-consequence) analysis, observable-behaviour definition, non-punitive peer-observation card design, percent-safe / participation / trend-by-category metrics with small-cell confidentiality, and routing trended at-risk behaviours to hierarchy-ranked system fixes (never discipline or 'retrain the worker'). Grounded in ISO 45001 clause 5.4 worker participation."
      lens: "Is this BBS program NON-PUNITIVE by design — observation cards role-labelled or anonymous, voluntary, used for trending and learning (never individual sanction) — with OBSERVABLE site-specific behaviours (never 'work safely'), defined metrics with the <5 small-cell guardrail, and at-risk behaviours trended to SYSTEMIC causes and routed to hierarchy-ranked system fixes rather than to the worker?"
modes:
  bbs-program:
    detected_by: "Q1/Q7 — confirmed BBS observation program (not a culture assessment, gemba walk, or KPI set) + the output artifact (full BBS program design / roll-out summary / card + metrics pack)"
    floor:
      - id: bbs-non-punitive-by-design
        description: "Observation cards are role-labelled or anonymous, voluntary, and the data is used for trending and learning — never individual sanction; a card that records a nameable individual for discipline is a FLAG and a de-id hard-fail"
        anchors: ['non.punitive', 'voluntary', 'role.label', 'anonymous']
        min_matches: 2
      - id: bbs-observable-behaviours
        description: "Every card item is an observable, site-specific behaviour tied to a named task/area — a vague, non-observable item ('work safely', 'be careful') is refused, never published"
        anchors: ['observable', 'card item', 'behaviou?r', 'site.specific']
        min_matches: 2
      - id: bbs-atrisk-to-system-fix
        description: "A trended at-risk category is routed to a hierarchy-ranked SYSTEM fix (eliminate/substitute/engineer/administrate before PPE), not 'retrain the worker' or discipline"
        anchors: ['system fix', 'hierarchy of control', 'systemic', 'at.risk']
        min_matches: 2
      - id: bbs-abc-discipline
        description: "Each behaviour has its antecedent and consequence mapped, and the system is designed so the SAFE behaviour carries the soon/certain/positive consequence — not a slogan or a poster"
        anchors: ['antecedent', 'consequence', '\bABC\b']
        min_matches: 2
      - id: bbs-metrics-small-cell
        description: "Percent-safe / participation / trend-by-category are defined (KB-DATA-BBS-METRICS), trended by behaviour category not by person, and no team breakdown of fewer than 5 is published (secondary suppression)"
        anchors: ['percent.safe', 'participation', 'small.cell', 'suppress', 'fewer than 5', '<5']
        min_matches: 2
      - id: bbs-feedback-loop-systemic
        description: "The observer→observed feedback is two-way and immediate, and the program closes the loop to systemic improvement — a program that only tallies cards and produces no systemic fix is a FLAG"
        anchors: ['feedback', 'close.{0,8}loop', 'two.way', 'systemic']
        min_matches: 1
      - id: bbs-owner-review-cycle
        description: "A named role owner for the program AND the system-fix action owners are stated, with a review cycle (intake Q8/Q9) — no 'TBD'"
        anchors: ['owner', 'review']
        min_matches: 2
---

# SME Review & Sign-off — bbs-program-designer

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`) into a **Behavioural Safety Consultant**. The
universal hard gates (de-id leak, citation accuracy, HoC / no lower-order-only control
without justification, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Non-punitive by design** — observation cards are **role-labelled or anonymous**,
  **voluntary**, and the data is used for **trending and learning, never individual
  sanction**. A card that records a nameable individual for discipline is a FLAG **and a
  `de_identification` hard-fail**.
- [ ] **Observable, site-specific behaviours** — every card item is something that can be
  **observed and counted**, tied to a named task/area. A vague, non-observable item
  ("work safely", "be careful") is a FLAG (refuse, do not publish).
- [ ] **At-risk behaviours route to SYSTEM fixes** — a trended at-risk category is routed
  to a **hierarchy-ranked system fix** (eliminate / substitute / engineer / administrate
  before PPE) via the `controls` engine. "Retrain the worker", "be more careful", or
  discipline as the response to a trended at-risk category is a FLAG and a
  `hierarchy_of_controls` defect.
- [ ] **ABC discipline** — each behaviour has its real **antecedent** and **consequence**
  mapped, and the system is designed so the **safe** behaviour carries the
  soon/certain/positive consequence — not a slogan or a poster.
- [ ] **Defined metrics + small-cell confidentiality** — percent-safe / participation /
  trend-by-category are defined per `KB-DATA-BBS-METRICS`, trended **by behaviour
  category, never by person**, and **no team breakdown of fewer than 5 is published**
  (secondary suppression applied). A percent-safe for a 4-person crew rendered
  identifiable is a FLAG (and a `de_identification` hard-fail).
- [ ] **Closed feedback loop to systemic learning** — the observer→observed feedback is
  two-way and immediate, and the program closes the loop to systemic improvement; a
  program that only tallies cards and produces no systemic fix is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The trended category with no owned system fix** — an at-risk behaviour category is
  trended and reported, but the systemic corrective action is dated far out (or absent) with
  no interim measure and no named owner, so the program surfaces the problem and never closes
  it.
- **The consent and data-governance leg** — the program collects observation data on people
  but never states the voluntary-participation consent basis, the retention period, or who
  may see raw cards, so the non-punitive promise has no governance behind it.
- **Observer competence and calibration** — the card is designed but the observer-training
  content, the calibration between observers, and the minimum trained-pool size are unstated,
  so percent-safe is not comparable across teams.

## Sign-off note
SME review: ran (persona: Behavioural Safety Consultant); this is **decision-support
only**. It **precedes — and never replaces — the human competent-person sign-off**, and
it never outputs the affirmative claim that the artifact has been signed off. A FLAG it
raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
