# De-identification Checklist (A5) — STRICTEST variant for audiometric / STS health data (CONV-7)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. `noise-exposure-health-surveillance` is the **strictest de-id tier in
> the phase**: **audiometric thresholds, standard-threshold-shift (STS) results, and
> fitness-for-work notes are GDPR Art. 9 / India DPDP special-category health data**, so the
> standard block is reinforced below — the byte-identical `deid` block stays untouched; this
> checklist carries the stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos — **and every health detail**: **audiometric thresholds (dB HL
by frequency), standard-threshold-shift (STS) determinations, baseline/annual audiogram
comparisons, noise-induced-hearing-loss diagnoses, fitness-for-work / medical-removal notes**.
If unsure whether something is identifying, treat it as identifying.

## 2. Report by SEG/role, never by individual (special-category rule)
- Pseudonymize every individual to a **stable SEG/role label** ("Press-shop operator SEG",
  "Grinding-bay operator A"); keep the re-identification key **SEPARATE** — never in the document.
- **Audiometric and surveillance results are reported at the SEG/role level only.** A named
  worker's **audiogram / STS determination / NIHL diagnosis / fitness note is never circulated**
  — strip it to the SEG aggregate or remove it.

## 3. Aggregate small numbers — `<5` suppression on EVERY audiometric breakdown
- **Never publish an audiometric / health-outcome cell of fewer than 5 individuals** (e.g.
  "3 operators with a standard threshold shift", "2 referred for NIHL"). Aggregate up and apply
  **secondary suppression** so a suppressed `<5` cell can't be back-calculated from row/column
  totals.
- This applies to **any** breakdown by SEG, shift, area, frequency band, or outcome — not just
  the headline count. An unsuppressed `<5` audiometric cell surviving into the circulated output
  is a **`de_identification` hard-fail**.

## 4. Warn before wide distribution
Board reports, toolbox talks, and posters default to de-identified / SEG-aggregated; **warn the
user before any name or any audiometric / STS result enters a widely shared artifact.**

## 5. Minimize & limit purpose
Use only the personal/health data the assessment needs; keep raw audiometry out of external
services where you can. When in doubt, ask before including it.

---

**Hard-fail triggers (non-waivable):** a real name, a named audiometric / STS / fitness result,
an embedded re-identification key, or an unsuppressed `<5` audiometric / health-outcome cell in
the circulated output. The De-identifier subagent runs FIRST and every downstream job consumes
only its scrubbed, SEG-labelled output.
