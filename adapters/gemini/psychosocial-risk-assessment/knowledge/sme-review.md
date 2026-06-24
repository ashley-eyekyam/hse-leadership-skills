---
sme-review:
  personas:
    - role: "Occupational Health / Psychosocial Specialist"
      expertise: "ISO 45003:2021 psychosocial risk management, the UK HSE Management Standards (demands/control/support/relationships/role/change), validated indicator-tool interpretation, work-design (organisational) controls, and the special-category-data / small-cell confidentiality discipline for survey, focus-group and sickness-absence data."
      lens: "Is this hazard assessed AT SOURCE — work design, not the individual — rated from at least two data sources (never a single anecdote), with organisational work-design controls ranked above individual resilience training, respondent confidentiality preserved (no <5-respondent cell, no individual named as the risk)?"
---

# SME Review & Sign-off — psychosocial-risk-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`) into an **Occupational Health / Psychosocial
Specialist**. The universal hard gates (de-id leak, citation accuracy, HoC / no
lower-order-only control without justification, owned-and-dated actions) are the
enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Assessed at source, not the worker** — the hazard is a feature of the **work
  design** (workload, decision latitude, support, conflict, role clarity, change
  management), not a deficiency of the individual. An assessment that frames the
  worker as the problem ("staff lack resilience") is a FLAG.
- [ ] **No individual named as the risk** — a finding attributed to a nameable person
  ("X is the stress risk") is a FLAG and a de-id concern; findings are role/group-level.
- [ ] **Multi-source triangulation** — each rated domain draws on **≥2 data sources**;
  a rating built on a single survey item, or a single anecdote, is a FLAG (refuse, not
  rate).
- [ ] **Small-cell confidentiality** — no domain/team breakdown with **<5 respondents**
  is published; secondary suppression is applied so a suppressed cell cannot be
  back-calculated. A sub-5 group rendered identifiable is a FLAG (and a `de_identification`
  hard-fail).
- [ ] **Work-design controls above individual resilience** — organisational controls
  (achievable workloads, manager-support systems, anti-bullying enforcement, role
  clarity, early change-consultation) come first; "resilience training" / EAP referral
  as the **sole** or primary control is a FLAG.
- [ ] **Domain completeness** — each selected HSE Management Standards domain (demands ·
  control · support · relationships · role · change) is addressed or explicitly marked
  out-of-scope; a silently dropped domain is a FLAG.
- [ ] **Benchmark fidelity** — each banded result quotes its indicator-tool `source`+`year`
  (`KB-DATA-PSYCHOSOCIAL-INDICATORS`); a bare number with no benchmark provenance is a FLAG.

## Sign-off note
SME review: ran (persona: Occupational Health / Psychosocial Specialist); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
