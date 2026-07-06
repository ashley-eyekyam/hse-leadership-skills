---
sme-review:
  personas:
    - role: "OSHA/RIDDOR recordability & safety-statistics SME"
      expertise: "OSHA 29 CFR 1904 recordability & DART classification, RIDDOR reportability, exposure-hour denominators, the 200,000 / 1,000,000 base conventions, and benchmark methodology."
      lens: "Is each count classified to the right recordability rule, the denominator real and period-actual, the base correct per rate — and is every figure presented as the engine returned it, never re-computed in prose and never a fabricated zero?"
modes:
  rate-calculation:
    detected_by: "Q1 — Which rate(s) (TRIR / DART / LTIFR / All three); the computation floor applies to each selected rate. Q2b fixes the recordability standard before counting."
    floor:
      - id: named-scope-period
        description: "Every rate carries a named scope and exact reporting period — a context-less number is not defensible (intake Q2 specificity anchor)"
        anchors: ['period', 'inputs']
        min_matches: 2
      - id: denominator-real-not-annualized
        description: "The denominator is real, period-actual, and NOT annualized; a missing/zero hours figure is refused, never defaulted (intake Q4 hours-gate)"
        anchors: ['denominator', 'not annualized']
        min_matches: 2
      - id: correct-base-per-rate
        description: "Correct base per rate — TRIR/DART use 200,000; LTIFR uses 1,000,000; a base swap silently changes the number by 5x (intake Q5; the engine constant)"
        anchors: ['200,000', '1,000,000']
        min_matches: 2
      - id: formula-and-inputs-shown
        description: "Each rate shows its formula and the actual inputs, and the value is the engine's returned figure — never re-divided in prose"
        anchors: ['formula:', 'inputs:']
        min_matches: 2
      - id: severity-rate-deferred-gap
        description: "The severity rate stays a literal [GAP] — there is no validated engine for it in v1.0; it is never computed in-prompt (D-03 severity-deferred)"
        anchors: ['severity rate', 'not computed', '\[GAP\]']
        min_matches: 2
      - id: benchmark-sourced-or-gap
        description: "A benchmark is used only with its publishing body + year; a bare comparator is [GAP], never treated as comparable (intake Q6; KB-DATA-TRIR-BENCHMARKS)"
        anchors: ['benchmark', 'publishing body', '\[GAP\]']
        min_matches: 2
      - id: data-quality-caveats
        description: "Data-quality caveats and a competent-person disposition accompany the figures — the reader is told what the numbers can and cannot bear before acting"
        anchors: ['data.quality caveat', 'competent person', 'disposition']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints. Quantitative-basis omission (canary S5) is the
native failure mode of a rate artifact and is anchored in the floor above.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A rate with no exposure basis shown** — the number without its denominator, base
  convention, or the formula that produced it; the reader cannot audit or reproduce it.
- **Recordability taken on trust** — counts accepted without checking each against the
  stated standard (a first-aid case counted recordable, a restricted-duty case dropped from
  DART); the classification that precedes the arithmetic is the real work.
- **The annualization trap** — a partial-period hours figure quietly annualized, or a
  default substituted for missing hours, inflating or deflating every rate.
- **Small-number silence** — a single case over a small exposure base producing a dramatic
  rate reported as a trend, with no small-number/volatility caveat.
- **Benchmark mismatch** — a sector / base-year / NAICS-mismatched comparator used as if
  like-for-like, or a bare number with no source.

## Sign-off note
SME review: ran (persona: OSHA/RIDDOR recordability & safety-statistics SME); this is
**decision-support only**. It **precedes — and never replaces, never emits — the human
competent-person sign-off**, and it never outputs the affirmative claim "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard
blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
