---
sme-review:
  personas:
    - role: "Safety Culture / OD Consultant"
      expertise: "Safety-culture and safety-climate assessment, the recognised maturity models (DuPont Bradley Curve, Hudson / Parker 'Hearts & Minds' ladder, Westrum organisational typology) and Schein's three levels of organisational culture, survey design and interpretation, organisational-development change methods, the espoused-vs-enacted-values gap, and the small-cohort / sensitive-personnel-data confidentiality discipline for survey, focus-group and observation data."
      lens: "Is this a defensible culture DIAGNOSIS — a named model or the Schein lens applied to a named population from at least two triangulated data sources (never a rating off a single survey), with Schein read as an espoused-vs-enacted gap not a ladder band, systemic leadership-system / work-design advancement controls ranked above awareness campaigns, respondent confidentiality preserved (no <5-cohort cell, no identifying verbatim quote, no individual named as the culture problem)?"
modes:
  culture-assessment:
    detected_by: "Q1/Q2 — a culture-maturity assessment (not a BBS programme, gemba walk, or KPI set) + the model/lens (Bradley / Hudson / Westrum / Schein / Combined)"
    floor:
      - id: cul-triangulated-not-single-survey
        description: "Any maturity rating draws on a named model, a named population, and ≥2 triangulated data sources (survey · observation/walk · records) — a ladder placement built on one pulse survey is refused, not rated"
        anchors: ['triangulat', 'at least two', 'two.{0,6}source', 'single survey', '≥2']
        min_matches: 1
      - id: cul-schein-gap-not-band
        description: "A Schein output names the espoused-vs-enacted gaps (level-2 espoused values vs the assumptions enacted at levels 1 & 3); a Schein maturity rating/band is a FLAG (Schein is a diagnostic lens, not a 4th ladder)"
        anchors: ['espoused', 'enacted', 'Schein']
        min_matches: 2
      - id: cul-no-individual-blamed
        description: "Findings are attributed to roles/groups and to the leadership system / work design, never to a nameable person; a finding that frames a named person (or a 4-person cohort) as 'the problem' is a FLAG and a de-id concern"
        anchors: ['role', 'leadership system', 'work design', 'no individual']
        min_matches: 1
      - id: cul-small-cohort-confidential
        description: "No cohort/sub-group breakdown with <5 respondents is published; secondary suppression so a suppressed cell cannot be back-calculated; no identifying verbatim quote reproduced"
        anchors: ['cohort', 'fewer than 5', 'five respondent', 'suppress', '<5']
        min_matches: 1
      - id: cul-systemic-above-awareness
        description: "Advancement moves are systemic leadership-system / work-design changes (felt-leadership cadence, fixing the consequence system, genuine worker consultation), not a poster / awareness campaign or 'tell people to care more'"
        anchors: ['systemic', 'leadership.system', 'work design', 'felt.leadership', 'consultation']
        min_matches: 2
      - id: cul-advancement-leading-indicators
        description: "Each roadmap action is tied to a real leading indicator (KB-DATA-LEADING-INDICATORS) with a named role-label owner and a due date — an 'improve the culture' action with no measurable indicator is a FLAG"
        anchors: ['leading indicator', 'owner', 'due']
        min_matches: 2
      - id: cul-model-fidelity
        description: "Each banded result quotes its model source+year (KB-DATA-CULTURE-MATURITY) and the model is cited as method, not law; a bare band with no provenance, or a fabricated band, is a FLAG"
        anchors: ['Bradley', 'Hudson', 'Westrum', 'source', 'model']
        min_matches: 2
---

# SME Review & Sign-off — safety-culture-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`) into a **Safety Culture / OD Consultant**. The
universal hard gates (de-id leak, citation accuracy, HoC / no lower-order-only control
without justification, owned-and-dated actions) are the enforced class and are not
restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **No rating from a single survey** — any maturity *rating* (a Bradley stage, a
  Hudson rung, a Westrum type) draws on a named model, a **named population**, and **≥2
  triangulated data sources** (survey · observation/walk · records). A ladder placement
  built on one pulse survey is a FLAG (refuse, not rate).
- [ ] **Schein is a gap diagnosis, not a band** — a standalone Schein output names the
  **espoused-vs-enacted gaps** (level-2 espoused values vs the assumptions enacted in
  artifacts/behaviour at levels 1 & 3); a "Schein Level 4" or any Schein *maturity rating*
  is a FLAG (Schein is a diagnostic lens, not a 4th ladder).
- [ ] **No individual named as the culture problem** — findings are attributed to
  roles/groups and to the leadership system / work design, never to a nameable person; a
  finding that frames a named person (or a 4-person cohort) as "the problem" is a FLAG and
  a de-id concern.
- [ ] **Small-cohort confidentiality** — no cohort/sub-group breakdown with **<5
  respondents** is published; secondary suppression is applied so a suppressed cell cannot
  be back-calculated; no verbatim respondent quote that identifies the speaker in a small
  group is reproduced. A sub-5 cohort rendered identifiable is a FLAG (and a
  `de_identification` hard-fail).
- [ ] **Systemic advancement above awareness** — advancement moves are systemic
  leadership-system / work-design changes (felt-leadership cadence, fixing the consequence
  system, genuine worker consultation under ISO 45001 5.4, closing the espoused-vs-enacted
  gap); a roadmap whose primary move is a poster / awareness campaign or "tell people to
  care more" is a FLAG.
- [ ] **Advancement tracked to leading indicators** — each roadmap action is tied to a
  real leading indicator from `KB-DATA-LEADING-INDICATORS` with a named role-label owner
  and an ISO due date; an "improve the culture" action with no measurable leading
  indicator is a FLAG.
- [ ] **Model fidelity** — each banded result quotes its model `source`+`year`
  (`KB-DATA-CULTURE-MATURITY`) and the model is cited as **method, not law**; a bare band
  with no model provenance, or a fabricated band, is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The rating with no inputs** — a Bradley stage / Hudson rung is asserted without the survey
  response rate, the sample/cohort coverage, or the record data behind it shown, so the band
  cannot be checked and the next assessment cannot measure movement.
- **The roadmap with no bridge** — a serious cultural gap (e.g. a reporting-suppression signal)
  is identified with advancement actions dated quarters out and no interim leadership move for
  the intervening period, leaving the enacted risk live while the roadmap runs.
- **Method-vs-law honesty** — the assessment presents a proprietary maturity model as if it
  were a standard or a compliance verdict, rather than a cited diagnostic method the competent
  person interprets.

## Sign-off note
SME review: ran (persona: Safety Culture / OD Consultant); this is **decision-support
only**. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs an affirmative final-approval claim on the
competent-person's behalf. A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation, weighted score below threshold)
are a separate enforcement class.
