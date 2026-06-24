<!-- KB-SNIP-LEGAL-REGISTER-METHOD -->
# Legal-register method — applicability → evidence → review cadence

**Fragment ID:** `KB-SNIP-LEGAL-REGISTER-METHOD`
**This is prompt text, applied by the model — not a generator.** It is the method the
`legal-compliance-register` (#20) skill follows to build a defensible multi-jurisdiction
register. The applicability menu is `KB-DATA-OBLIGATION-FAMILIES`; **India defers to
`hse-india`** with mandatory state detection and no minted national form numbers.

> Source: ISO 45001:2018 cl. 6.1.3 (legal & other requirements) / 9.1.2 (evaluation of compliance) · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

1. **Determine applicability per named activity** (refuse a generic scope). Use
   `KB-DATA-OBLIGATION-FAMILIES` to seed candidate obligations by jurisdiction × activity,
   then **confirm** each against the named activity — a register that lists an inapplicable
   regulation (e.g. a construction reg for an office) is flagged (#20 eval case 1). Every
   obligation carries an **applicability rationale**.
2. **Map evidence of compliance.** Each obligation → the evidence that demonstrates
   compliance → a gap (if any) → a named **owner** → a **review date**. No empty evidence
   cell passes silently.
3. **Evaluate compliance** (cl. 9.1.2) — summarise compliant / gap / unknown.
4. **India branch — defer to `hse-india`.** Run **state detection first**
   (`KB-REG-IN-STATEFORMS`), then resolve the India obligation/form via the `hse-india`
   skills (`india-state-form-finder` / `factories-act-returns`). **Never hard-code a national
   form number** — an India scenario that does so is a `regulatory_citation_accuracy`
   hard-fail (#20 eval case 2); leave an unresolved id `[GAP]`.
5. **Set the update cadence** — obligations are volatile; state when the register is
   re-reviewed and on what trigger (new activity, legal change).

## Output expectation

A grouped register (obligation / applicability / evidence / gap / owner / review-date per
jurisdiction), a compliance-evaluation summary, and the India deferral note (state-detection
result). Feeds `specificity`, `defensibility`, `regulatory_citation_accuracy`.
