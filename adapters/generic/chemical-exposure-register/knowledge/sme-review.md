---
sme-review:
  personas:
    - role: "Occupational hygienist"
      expertise: "SEG design, inhalation AND dermal exposure assessment, OEL/WEL/PEL selection (STEL vs 8-h TWA, skin notation, sensitiser/carcinogen flags), air-monitoring strategy + health-surveillance triggers, measured-vs-modelled-vs-[GAP] confidence call"
      lens: "is each agent tied to the correct applicable limit (source+year) for the right averaging period; is the SEG genuinely homogeneous; are dermal/sensitiser routes not lost behind an inhalation-only TWA"
---

# SME Review & Sign-off — chemical-exposure-register

One lens suffices here: an occupational hygienist who owns SEG design, limit selection and the
measured-vs-modelled confidence call. The persona **narrows** the Chemical-Process-Safety
sector slot that extends the generic **HSE-SME-Reviewer** hook (`KB-SNIP-ARCHETYPES`). The
universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions)
are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each agent → the correct applicable OEL/WEL/PEL, **with source + year**; an invented OEL is **hard-gate-adjacent** (escalate). Where no statutory limit exists (e.g. India), cite the most-protective referenced value and flag non-statutory (presenting it as statutory is a FLAG).
- [ ] Right averaging period / limit type — 8-h TWA vs STEL vs ceiling; skin/"Sk" notation honoured; banding a peak task against an 8-h TWA only is a FLAG.
- [ ] Dermal and sensitiser/carcinogen routes not omitted — banding inhalation only while the agent carries a skin/respiratory-sensitiser/carcinogen hazard is a FLAG.
- [ ] SEG homogeneity defensible — workers in a SEG genuinely share agents/tasks/controls; a SEG mixing unlike exposures is a FLAG.
- [ ] Band confidence reflects measured vs modelled vs `[GAP]` — a "low risk" band on no monitoring data is a FLAG; `[GAP]` must trigger a monitoring action.
- [ ] Controls HoC-ranked — LEV/containment/substitution before RPE; an exposure "controlled" by RPE alone is **hard-gate-adjacent** (HoC) unless justified-or-escalated.
- [ ] De-id holds at SEG/role level + small-cell suppression — results tied to SEG/role labels never names; per-worker surveillance cells <5 suppressed (a leak is a de-id **hard fail**).

## Sign-off note
SME review: ran (persona: Occupational hygienist); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
