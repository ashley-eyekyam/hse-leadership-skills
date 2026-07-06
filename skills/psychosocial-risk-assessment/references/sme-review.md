---
sme-review:
  personas:
    - role: "Occupational Health / Psychosocial Specialist"
      expertise: "ISO 45003:2021 psychosocial risk management, the UK HSE Management Standards (demands/control/support/relationships/role/change), validated indicator-tool interpretation, work-design (organisational) controls, and the special-category-data / small-cell confidentiality discipline for survey, focus-group and sickness-absence data."
      lens: "Is this hazard assessed AT SOURCE — work design, not the individual — rated from at least two data sources (never a single anecdote), with organisational work-design controls ranked above individual resilience training, respondent confidentiality preserved (no <5-respondent cell, no individual named as the risk)?"
modes:
  assessment:
    detected_by: "Q = the requested deliverable (a psychosocial risk assessment for the named team/organisation) — single-output skill; this mode is always active"
    floor:
      - id: assessed-at-source-work-design
        description: "The hazard is assessed at source as a feature of work design, not attributed to the individual worker"
        anchors: ['at source|work design', 'not the individual|not the worker|work.design']
        min_matches: 2
      - id: multi-source-triangulation
        description: "Each rated domain draws on >=2 data sources (never a single anecdote) — a rating from one source is a FLAG"
        anchors: ['triangulat|two source|two data source|data source', 'data source|method|indicator']
        min_matches: 2
      - id: small-cell-confidentiality
        description: "No domain/team breakdown with <5 respondents; small cells are suppressed/aggregated to preserve respondent confidentiality"
        anchors: ['<5|fewer than 5|small.cell|respondent', 'suppress|confidential|aggregat']
        min_matches: 2
      - id: work-design-controls-above-resilience
        description: "Organisational work-design controls are ranked ABOVE individual resilience training in the hierarchy — a resilience-first treatment is a FLAG"
        anchors: ['work.design|organisational', 'resilience|hierarchy|above']
        min_matches: 2
      - id: domain-completeness
        description: "Each selected HSE Management Standards domain (demands · control · support · relationships · role · change) is assessed, none silently dropped"
        anchors: ['demands|control|support|relationships|change', 'domain']
        min_matches: 2
      - id: benchmark-fidelity
        description: "Each banded result quotes its indicator-tool source + year — a band with no benchmark provenance is a FLAG"
        anchors: ['source', 'year|benchmark|indicator']
        min_matches: 2
      - id: no-individual-named-confidential
        description: "No finding is attributed to a nameable individual; confidentiality of respondents/special-category data is preserved"
        anchors: ['confidential', 'individual|role label|special.category']
        min_matches: 2
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The hazard relocated to the worker (root failure)** — a psychosocial finding framed as an
  individual's "resilience" or "stress management" deficit rather than a feature of work design
  (workload, control, role clarity) misdiagnoses the hazard and treats the wrong target.
- **The single-anecdote rating (S5)** — a domain banded from one survey question or one manager's
  view; without >=2 triangulated sources the rating is an opinion, not an assessment.
- **The confidentiality breach through small cells** — a team/domain breakdown with fewer than
  five respondents can re-identify individuals even without names; suppress or aggregate.
- **Resilience-training-as-treatment** — offering "resilience workshops" as the primary control
  while the organisational driver (understaffing, unclear roles) is untouched inverts the
  hierarchy of controls.

## Sign-off note
SME review: ran (persona: Occupational Health / Psychosocial Specialist); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
