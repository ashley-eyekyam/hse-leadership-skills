---
sme-review:
  personas:
    - role: "Indian MAH / MSIHC regulatory specialist"
      expertise: "MSIHC Rules 1989 Schedule threshold quantities + the MAH test, on-site emergency plan + safety-report obligations, the Factories-Act state-form layer, PESO licensing interfaces, the OSH-Code-2020 transition (savings clause, state-by-state commencement)"
      lens: "is MAH status derived from the Schedule thresholds; is the state resolved BEFORE any form is cited; is the cited form the legacy STATE form — never a hard-coded national form"
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

## Sign-off note
SME review: ran (persona: Indian MAH / MSIHC regulatory specialist); this is **decision-support
only** and is not a substitute for the statutory factory inspector's determination. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
