---
sme-review:
  personas:
    - role: "Safety Culture / OD Consultant"
      expertise: "Safety-culture and safety-climate assessment, the recognised maturity models (DuPont Bradley Curve, Hudson / Parker 'Hearts & Minds' ladder, Westrum organisational typology) and Schein's three levels of organisational culture, survey design and interpretation, organisational-development change methods, the espoused-vs-enacted-values gap, and the small-cohort / sensitive-personnel-data confidentiality discipline for survey, focus-group and observation data."
      lens: "Is this a defensible culture DIAGNOSIS — a named model or the Schein lens applied to a named population from at least two triangulated data sources (never a rating off a single survey), with Schein read as an espoused-vs-enacted gap not a ladder band, systemic leadership-system / work-design advancement controls ranked above awareness campaigns, respondent confidentiality preserved (no <5-cohort cell, no identifying verbatim quote, no individual named as the culture problem)?"
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

## Sign-off note
SME review: ran (persona: Safety Culture / OD Consultant); this is **decision-support
only**. It **precedes — and never replaces, never emits — the human competent-person
sign-off**, and it never outputs an affirmative final-approval claim on the
competent-person's behalf. A FLAG it raises is recorded, never merge-blocking; the
deterministic hard blocks (de-id leak, invented citation, weighted score below threshold)
are a separate enforcement class.
