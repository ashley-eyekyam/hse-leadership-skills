<!-- KB-SNIP-RETURNS-METHOD -->
# Regulatory-returns method — determine → form → deadline → prepare

**Fragment ID:** `KB-SNIP-RETURNS-METHOD`
**This is prompt text, applied by the model — not a generator.** It is the method the
`regulatory-returns` (#27) skill follows to determine recordability/reportability and prepare
the return. The cited decision logic is `KB-DATA-RECORDABILITY-TESTS`; **India defers to
`hse-india`** with mandatory state detection and no minted national form numbers.

> Source: US OSHA 29 CFR 1904 (300/300A/301) · UK RIDDOR 2013 · EU member-state transposition · India → hse-india · Year: 2026 · Reviewed: 2026-06-22 · Volatile: false.

---

## Instruction

1. **Capture the facts the test needs first.** Never give a "reportable yes/no" until the
   incident facts the jurisdiction's test requires are captured; never assert a deadline
   without the jurisdiction (#27 eval case 1).
2. **Apply the cited test** (`KB-DATA-RECORDABILITY-TESTS`):
   - **US OSHA** — work-relatedness + new case + beyond first aid → recordable; cite the
     1904 rule applied.
   - **UK RIDDOR** — specified injury / over-7-day / dangerous occurrence / reportable
     disease → reportable; cite the reg.
   - **EU** — resolve the binding return from the member-state transposition.
3. **Identify the form + deadline** from the test result (e.g. OSHA 300/300A/301 with the
   posting window; RIDDOR 10-day / 15-day rule).
4. **Prepare a de-identified working return + evidence trail.** The statutory submission
   contains injured-person identity **by law** (named, controlled); every internal/working
   copy is **de-identified**, with `<5` small-cell suppression on any aggregated summary
   (e.g. 300A by department) — a seeded identity in an internal copy is a `de_identification`
   hard-fail (#27 eval case 3). Never embed the re-identification key in the return.
5. **India branch — defer to `hse-india`.** Run **state detection first**, then route to
   `factories-act-returns` / `india-accident-notice` / `india-state-form-finder`. **Never
   hard-code a national form number** — doing so is a `regulatory_citation_accuracy` hard-fail
   (#27 eval case 2); leave an unresolved id `[GAP]`.

## Output expectation

A recordability/reportability determination (test cited), the correct form + deadline, a
de-identified prepared return + evidence trail, and the India deferral note where applicable.
Feeds `regulatory_citation_accuracy`, `specificity`, `de_identification`.
