# De-identification Checklist (A5) — REINFORCED for special-category respiratory-clearance / fitness data

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. `ppe-matrix` handles **respiratory medical-clearance and
> fitness-for-respirator notes — GDPR Art. 9 / India DPDP special-category health data**, so the
> standard block is reinforced below — the byte-identical `deid` block stays untouched; this
> checklist carries the stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail**: respiratory medical-clearance
results, fitness-for-respirator / fit-test records, spirometry, medical-questionnaire outcomes,
restricted-duties notes, and any diagnosis. If unsure whether something is identifying, treat it
as identifying.

## 2. Report by role, never by individual (special-category rule)
- Pseudonymize every individual to a **stable role label** ("Line-3 fettler", "Operator A");
  keep the re-identification key **SEPARATE** — never in the document.
- **Respiratory medical-clearance and fitness detail are reduced to the role level only.** A
  named worker's respiratory-clearance note, fit-test result, or restricted-duties record is
  **never** circulated in the PPE matrix — record the requirement ("respirator fit-test +
  medical clearance required for this role") without the individual's result.

## 3. Aggregate small numbers — `<5` suppression on EVERY health-outcome breakdown
- **Never publish a health-outcome cell of fewer than 5 individuals** (e.g. "2 workers failed
  respirator clearance"). Aggregate up and apply secondary suppression so a suppressed `<5` cell
  can't be back-calculated from row/column totals.
- This applies to **any** breakdown by role, shift, or line — not just the headline count. A
  `<5` cell surviving into the circulated output is a `de_identification` hard-fail.

## 4. Warn before wide distribution
Board reports, toolbox talks, and posted PPE matrices default to de-identified / role-aggregated;
**warn the user before any name or any respiratory-clearance / fitness note enters a widely
shared artifact.**

## 5. Minimize & limit purpose
Use only the personal/health data the PPE matrix needs — the matrix needs the **task hazard and
the role-level fit/clearance requirement**, not a named worker's medical-clearance history; keep
raw clearance data out of external services where you can. When in doubt, ask before including it.

---

**Hard-fail triggers (non-waivable):** a real name, a named respiratory medical-clearance /
fitness note, an embedded re-identification key, or an unsuppressed `<5` health-outcome cell in
the circulated output. The De-identifier subagent runs FIRST and every downstream job consumes
only its scrubbed, role-labelled output.
