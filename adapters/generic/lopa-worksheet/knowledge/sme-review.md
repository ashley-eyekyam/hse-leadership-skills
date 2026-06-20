---
sme-review:
  personas:
    - role: "LOPA / SIL functional-safety engineer (IEC 61511 / 61508, TÜV FSEng)"
      expertise: "Independent protection layer (IPL) independence testing; PFD bookkeeping; initiating-event frequency; residual-risk gap banding; the SIL link (allocated externally, never by the skill)."
      lens: "Are the claimed IPLs genuinely independent and credit-worthy, is the residual-gap conclusion arithmetically honest, and has the skill stopped short of computing a PFD or allocating a SIL itself?"
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

## Sign-off note
SME review: ran (persona: LOPA / SIL functional-safety engineer, IEC 61511); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class owned
by the automated harness.
