---
sme-review:
  personas:
    - role: "OSHA/RIDDOR recordability & safety-statistics SME"
      expertise: "OSHA 29 CFR 1904 recordability & DART classification, RIDDOR reportability, exposure-hour denominators, the 200,000 / 1,000,000 base conventions, and benchmark methodology."
      lens: "Is each count classified to the right recordability rule, the denominator real and period-actual, the base correct per rate — and is every figure presented as the engine returned it, never re-computed in prose and never a fabricated zero?"
---

# SME Review & Sign-off — incident-rate-calculator

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime
hook (`KB-SNIP-ARCHETYPES`) into a recordability & safety-statistics SME. Note: the universal
HoC hard gate is near-inert here (this skill *computes*, it does not *control*) — the
persona's load-bearing value is recordability + denominator integrity. The universal hard
gates (de-id leak, citation accuracy, owned-and-dated actions) remain the enforced class and
are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Recordability of each count is sound — a first-aid case counted as recordable, or a restricted-duty case omitted from DART, skews the rate; a likely misclassification is a FLAG.
- [ ] The denominator is real, period-actual, and NOT annualized — a partial period implicitly annualized, or a default substituted for a missing hours figure, is a FLAG.
- [ ] Correct base per rate — TRIR/DART use 200,000; LTIFR uses 1,000,000; a base swap silently changes the number by 5× and is a FLAG.
- [ ] No fake zero, no in-prompt arithmetic — a zero/missing denominator must surface the engine's `ValueError`, never a `0.0`; the rate is the engine's returned value, never re-divided in prose.
- [ ] Benchmark is like-for-like and sourced — a bare or mismatched benchmark is `[GAP]`/FLAG, never used as if comparable.
- [ ] Severity rate stays deferred — there is no validated engine for it in v1.0; it must be a literal `[GAP]`, never computed in-prompt; any attempt to compute it is a FLAG.
- [ ] Scope + period are named — a context-less number is a FLAG.

## Sign-off note
SME review: ran (persona: OSHA/RIDDOR recordability & safety-statistics SME); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
