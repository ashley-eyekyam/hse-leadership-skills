---
sme-review:
  personas:
    - role: "Occupational hygienist"
      expertise: "SEG design, inhalation AND dermal exposure assessment, OEL/WEL/PEL selection (STEL vs 8-h TWA, skin notation, sensitiser/carcinogen flags), air-monitoring strategy + health-surveillance triggers, measured-vs-modelled-vs-[GAP] confidence call"
      lens: "is each agent tied to the correct applicable limit (source+year) for the right averaging period; is the SEG genuinely homogeneous; are dermal/sensitiser routes not lost behind an inhalation-only TWA"
modes:
  exposure-register:
    detected_by: "Q1 — Scope (build a new / extend an exposure register, or plan a monitoring/surveillance schedule)"
    floor:
      - id: cer-agent-oel-cited-source-year
        description: "Each agent is banded against the correct applicable OEL with source + year; where no statutory limit exists (India) the most-protective referenced value is cited and flagged non-statutory — an invented OEL is escalated (KB-DATA-OEL-LIMITS)"
        anchors: ['\bOEL\b', 'non.statutory']
        min_matches: 1
      - id: cer-averaging-period-route
        description: "The right averaging period/limit type is used (8-h TWA vs STEL vs ceiling; skin 'Sk' notation honoured) and dermal/sensitiser/carcinogen routes are not lost behind an inhalation-only TWA"
        anchors: ['STEL', 'dermal', 'skin.{0,6}sk']
        min_matches: 1
      - id: cer-seg-homogeneity
        description: "SEG homogeneity is defensible — workers in a SEG genuinely share agents/tasks/controls; a SEG mixing unlike exposures is a FLAG"
        anchors: ['\bSEG\b', 'homogene']
        min_matches: 1
      - id: cer-band-confidence-measured-modelled-gap
        description: "Band confidence reflects measured vs modelled vs [GAP] — a 'low risk' band on no monitoring data is a FLAG and a [GAP] triggers a monitoring action"
        anchors: ['precautionary|modelled', 'confidence']
        min_matches: 1
      - id: cer-controls-hoc-ranked
        description: "Controls are HoC-ranked — LEV/containment/substitution before RPE; an exposure 'controlled' by RPE alone is hard-gate-adjacent (HoC) unless justified-or-escalated (KB-SNIP-HOC)"
        anchors: ['hierarchy of controls', 'substitution']
        min_matches: 1
      - id: cer-deid-small-cell-suppression
        description: "De-id holds at SEG/role level with small-cell suppression — results tied to SEG/role labels never names; per-worker cells <5 suppressed (a leak is a de-id hard-fail)"
        anchors: ['small.cell|<\s?5', 'suppress']
        min_matches: 1
      - id: cer-india-osh-transition
        description: "For India the state is resolved, no national OEL/form is asserted (referenced values flagged non-statutory), and the OSH-Code transition is noted (KB-REG-IN-FACTORIES)"
        anchors: ['OSH.Code', 'Factories Act']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The band with no inputs — a level asserted by silence (canary S5)** — a risk band stated
  without the measured/modelled basis, the averaging period, or the cited OEL; a 'low' band on
  absent monitoring data with no confidence flag is the hollow.
- **The surveillance loop never closed (canary S3)** — a carcinogen/sensitiser/Repr agent with no
  health-surveillance element, no baseline, and no symptom/biological-monitoring linkage; prior
  outcomes neither reviewed (de-identified) nor confirmed absent.
- **The regime named, its element set unswept (canary S6)** — Factories Act / OSH-Code cited while
  the §41C surveillance / §41F exposure-limit / register-and-form element set is not actually
  swept for the state.
- **The dermal/skin route lost behind an inhalation TWA (assistive completeness)** — a skin-notation
  or dermally-absorbed agent banded only on an 8-h inhalation TWA, with no dermal control or
  biological-monitoring leg.

## Sign-off note
SME review: ran (persona: Occupational hygienist); this is **decision-support only**. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
