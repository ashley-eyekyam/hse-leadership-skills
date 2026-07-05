---
sme-review:
  personas:
    - role: "LOPA / SIL functional-safety engineer (IEC 61511 / 61508, TÜV FSEng)"
      expertise: "Independent protection layer (IPL) independence testing; PFD bookkeeping; initiating-event frequency; residual-risk gap banding; the SIL link (allocated externally, never by the skill)."
      lens: "Are the claimed IPLs genuinely independent and credit-worthy, is the residual-gap conclusion arithmetically honest, and has the skill stopped short of computing a PFD or allocating a SIL itself?"
modes:
  worksheet:
    detected_by: "Q10 — What output, audience, distribution? (Worksheet / Full report — both emit the single-scenario IEC 61511 LOPA worksheet, the skill's single artifact class)"
    floor:
      - id: single-scenario-one-ie
        description: "Exactly one consequence scenario with one initiating event and its engineer-supplied frequency (per year) — never a conflated multi-scenario sheet (intake Q2/Q3 specificity anchor)"
        anchors: ['initiating event', 'per year|/yr|frequency']
        min_matches: 2
      - id: ipl-independence-test-recorded
        description: "Each candidate IPL carries a recorded independence-test result — independent of the initiating event AND of every other IPL; shared-controller double-counting excluded (intake Q4; KB-STD-IEC-61511 independence discipline)"
        anchors: ['independen', 'IPL|independent protection layer']
        min_matches: 2
      - id: pfd-engineer-supplied-provenance
        description: "Every PFD is engineer-supplied with its provenance recorded (company LOPA table / vendor data / site history); an unsupplied PFD is a literal [GAP], never computed (the non-computation core)"
        anchors: ['PFD', 'engineer.supplied|supplied by|company LOPA table|vendor']
        min_matches: 2
      - id: tolerable-target-basis
        description: "The tolerable target frequency / SIL target is stated with its engineer-supplied basis (corporate risk criteria / standard) — the criterion the gap is measured against (intake Q6)"
        anchors: ['tolerable', 'target frequency|risk criteri']
        min_matches: 1
      - id: residual-gap-banded
        description: "The residual-risk gap is banded on the named matrix — the worksheet's ONLY arithmetic (intake Q8, risk_matrix output)"
        anchors: ['residual', 'gap']
        min_matches: 2
      - id: value-owner-role
        description: "The competent engineer/team owning the supplied values is named as a role (the assistive-evidence / defensibility anchor, intake Q7)"
        anchors: ['values owned by|owned by the|owning engineer', 'ownership of values|engineer.verified']
        min_matches: 1
      - id: sil-link-external
        description: "The SIL link is recorded as externally allocated (or [GAP] where no allocation exists) — the skill never allocates a SIL"
        anchors: ['SIL', 'allocat']
        min_matches: 2
      - id: iec61511-grounding
        description: "The method is grounded in IEC 61511 (cited from KB-STD-IEC-61511)"
        anchors: ['IEC 61511', 'KB-STD-IEC-61511']
        min_matches: 1
---

# SME Review & Sign-off — lopa-worksheet

This skill carries **one** specialized SME lens: a LOPA / SIL functional-safety engineer.
It narrows the family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`)
to the single-scenario IEC 61511 LOPA; the generic **HSE-SME-Reviewer** hook is the
inherited fallback. The universal hard gates (de-id leak, citation accuracy, HoC / no
PPE-or-admin-only without justification, owned-and-dated actions) are the enforced class
and are not restated below.

**The non-computation discipline is load-bearing here.** Every PFD, credit and SIL target
is engineer-supplied and so labelled, with its provenance (company LOPA table / vendor data
/ site history) recorded as the assistive evidence — the *owning engineer/team* is the
defensibility anchor. The skill **never computes a PFD or allocates a SIL**; an unsupplied
value is `[GAP]`, never a fabricated number. The only arithmetic is banding the residual
*gap*.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Each IPL carries a recorded independence-test result — independent of the initiating event AND of every other IPL; the same device/system is not double-counted.
- [ ] Each claimed IPL meets the LOPA criteria (specific, independent, dependable, auditable); a BPCS loop and its alarm are not both credited where they share the controller.
- [ ] Every PFD and the SIL target are engineer-supplied and so labelled; no PFD is computed and no SIL is allocated by the skill; an unsupplied value reads `[GAP]`, never invented.
- [ ] Residual-gap banding is the *only* arithmetic; the tolerable-vs-not conclusion follows from the engineer-supplied PFDs, not a skill-multiplied frequency.
- [ ] The tolerability target / SIL claim is tied to a stated risk-tolerance basis (corporate matrix / standard), not asserted.
- [ ] Exactly one consequence scenario with one initiating event — not a conflated multi-cause worksheet — and the values are owned by a named competent engineer/team (FLAG: reads as structured engineer-supplied analysis, not autonomous AI judgement).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **IPLs credited without the independence test on paper** — the layer list looks complete
  and each carries a PFD, but no row records the independence verdict; the double-count
  (BPCS loop + its own alarm) hides exactly there.
- **PFDs that float free of provenance** — numbers present, sources absent; an auditor
  cannot tell a company-table value from an invented one, which defeats the worksheet's
  entire defensibility.
- **A conclusion with no criterion** — the sheet declares the scenario tolerable/not
  without ever stating the tolerable target frequency or whose criterion it is.
- **Enabling conditions and conditional modifiers silently skipped** — occupancy,
  ignition probability, time-at-risk factors neither applied nor declared out-of-scope,
  quietly flattering the residual gap.

## Sign-off note
SME review: ran (persona: LOPA / SIL functional-safety engineer, IEC 61511); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
