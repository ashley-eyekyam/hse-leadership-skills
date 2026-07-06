---
sme-review:
  personas:
    - role: "Indian MAH / MSIHC regulatory specialist"
      expertise: "MSIHC Rules 1989 Schedule threshold quantities + the MAH test, on-site emergency plan + safety-report obligations, the Factories-Act state-form layer, PESO licensing interfaces, the OSH-Code-2020 transition (savings clause, state-by-state commencement)"
      lens: "is MAH status derived from the Schedule thresholds; is the state resolved BEFORE any form is cited; is the cited form the legacy STATE form — never a hard-coded national form"
modes:
  msihc-pack:
    detected_by: "Q1 — Scope (MAH-status verdict, on-site emergency plan, safety-report outline, or the full MSIHC pack)"
    floor:
      - id: msihc-mah-verdict-schedule
        description: "MAH status is derived by comparing the inventory to the MSIHC Schedule threshold quantities; an invented threshold is escalated and an unresolved one is a literal [GAP] (KB-REG-IN-MSIHC)"
        anchors: ['MAH.status verdict|MAH tier|MAH status', 'MSIHC Schedule', 'threshold']
        min_matches: 1
      - id: msihc-state-first-no-national-form
        description: "The state is resolved and confirmed BEFORE any statutory form is cited, and only the legacy STATE form is cited — never a hard-coded national form; an unseeded state -> literal [GAP] (KB-REG-IN-STATEFORMS)"
        anchors: ['state.first', 'no national form']
        min_matches: 1
      - id: msihc-off-site-district-authority
        description: "Where off-site receptors are present, the off-site emergency plan is pointed to the District authority (KB-REG-IN-MSIHC)"
        anchors: ['off.site emergency plan', 'district authority']
        min_matches: 1
      - id: msihc-onsite-plan-safety-report
        description: "The on-site emergency plan outline and the safety-report outline are MSIHC-complete for an MAH installation — a thin outline missing required MSIHC elements is a FLAG"
        anchors: ['on.site emergency plan', 'safety report']
        min_matches: 1
      - id: msihc-major-accident-controls-hoc
        description: "Major-accident scenarios and their controls are HoC-ranked (most effective first — prevention before mitigation, PPE/drills never the basis of safety) (KB-SNIP-HOC)"
        anchors: ['hierarchy of controls', 'most effective first']
        min_matches: 1
      - id: msihc-gap-register-nothing-invented
        description: "An open [GAP] register carries every unresolved threshold/form as a literal [GAP] with a verification path — nothing invented, no national-form fallback"
        anchors: ['gap.{0,3}register', 'nothing invented|never invented']
        min_matches: 1
      - id: msihc-osh-code-transition
        description: "The OSH-Code transition is noted as direction-of-travel (savings clause + state-commencement caveat, legacy-first), never presenting a consolidated form as live"
        anchors: ['OSH.Code', 'legacy.first']
        min_matches: 1
---

# SME Review & Sign-off — india-msihc-mah-pack

This is an **always-India** skill — `ELI-JURIS` is the spine and India→state detection is
load-bearing. One lens suffices: an Indian MAH / MSIHC regulatory specialist who derives MAH
status from the Schedule thresholds, **resolves and confirms the state BEFORE citing any
statutory form**, and never hard-codes a national form. The persona **narrows** the Chemical-
Process-Safety sector slot crossed with the India-Regulatory hook's state-first / legacy-first
discipline (`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] MAH status derived from the MSIHC Schedule threshold quantities — inventory compared to thresholds for the verdict; an invented threshold is **hard-gate-adjacent** (escalate); `[GAP]` + competent-person is the honest path.
- [ ] **State resolved and confirmed BEFORE any statutory form is cited** — ask-or-infer-from-address then confirm; a form cited without a confirmed state, or inferred from an address without confirmation, is a FLAG (the load-bearing India check).
- [ ] **No hard-coded national form — legacy state form only** — the form resolves from `KB-REG-IN-STATEFORMS`; a fabricated/national form id is **hard-gate-adjacent** (the citation grader is row-blind to a fabricated form value). An unseeded ("Other") state → literal `[GAP]`, never an invented form, never a silent national-form fallback.
- [ ] On-site emergency plan + safety-report outlines are MSIHC-complete for an MAH installation — a thin outline missing required MSIHC elements is a FLAG.
- [ ] PESO pointers referenced, not re-authored — petroleum/explosives/SMPV licensing cites `KB-REG-IN-PESO` (hse-process-owned) by ID; re-stating or contradicting PESO duties is a FLAG.
- [ ] OSH-Code transition noted as direction-of-travel, not overstated — flagged with the savings clause + state-commencement caveat (legacy-first); presenting a consolidated form as live is a FLAG.
- [ ] De-id holds under DPDP — worker/establishment identity, Aadhaar/government IDs, home addresses, small (<5) cells suppressed (a leak is a de-id **hard fail**).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The pack with no emergency leg (canary S1)** — an MAH verdict with no on-site emergency plan
  (assembly, mutual-aid, notification chain) and, where off-site receptors exist, no District-
  authority off-site plan pointer.
- **The regime named, its element set unswept (canary S6)** — MSIHC cited while the Schedule
  threshold test, the on-site-plan / safety-report element set, and the PESO/state-form interfaces
  are not actually swept; the invented-national-form failure is the sharp edge here.
- **The major-accident basis asserted by silence (canary S5)** — a scenario (chlorine toxic
  release, LPG BLEVE) with no consequence framing, no receptor distance, and PPE/drills offered as
  the basis of safety rather than prevention-first engineering.
- **Record identity & statutory basis absent (canary S8)** — the state confirmed, the occupier
  role recorded, and every unresolved threshold/form carried as a dated [GAP] with a verification
  path, never a fabricated number.

## Sign-off note
SME review: ran (persona: Indian MAH / MSIHC regulatory specialist); this is **decision-support
only** and is not a substitute for the statutory factory inspector's determination. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
