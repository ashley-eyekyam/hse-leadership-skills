# De-identification Checklist (A5) — REINFORCED for special-category MSD/fitness data

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE drafting
> any output. A de-identification leak is an eval **`de_identification` hard-fail** (A8) and
> **cannot be waived**. `ergonomics-assessment` handles **reported MSD symptoms and
> medical-fitness notes — GDPR Art. 9 / India DPDP special-category health data**, so the
> standard block is reinforced below — the byte-identical `deid` block stays untouched; this
> checklist carries the stricter handling.

## 1. Detect & flag every identifier (list them up front)
Names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations,
job title / crew / shift, photos or posture video showing faces — **and every health detail**:
reported MSD symptoms (back pain, RSI, shoulder/wrist complaints), fitness-for-work notes,
diagnoses, prior injury context, restricted-duties records. If unsure whether something is
identifying, treat it as identifying.

## 2. Report by role/SEG, never by individual (special-category rule)
- Pseudonymize every individual to a **stable role/SEG label** ("Line-2 packer SEG",
  "Operator A"); keep the re-identification key **SEPARATE** — never in the document.
- **Reported symptoms and fitness detail are reported at the role/SEG level only.** A named
  worker's back-injury note, medical-fitness assessment, or restricted-duties record is
  **never** circulated — strip it to the SEG aggregate or remove it.

## 3. Aggregate small numbers — `<5` suppression on EVERY symptom/outcome breakdown
- **Never publish a symptom/health-outcome cell of fewer than 5 individuals** (e.g. "2 packers
  with reported lower-back pain", "3 RSI cases"). Aggregate up and apply secondary suppression
  so a suppressed `<5` cell can't be back-calculated from row/column totals.
- This applies to **any** breakdown by role/SEG, shift, line, or symptom — not just the
  headline count. A `<5` cell surviving into the circulated output is a `de_identification`
  hard-fail.

## 4. Warn before wide distribution
Board reports, toolbox talks, and posters default to de-identified / SEG-aggregated; **warn
the user before any name or any reported-symptom / fitness note enters a widely shared artifact.**

## 5. Minimize & limit purpose
Use only the personal/health data the assessment needs — the ergonomics scoring needs the task
parameters (geometry / joint angles), not a named worker's medical history; keep raw symptom
data out of external services where you can. When in doubt, ask before including it.

---

**Hard-fail triggers (non-waivable):** a real name, a named medical-fitness / back-injury note,
an embedded re-identification key, or an unsuppressed `<5` symptom/health-outcome cell in the
circulated output. The De-identifier subagent runs FIRST and every downstream job consumes only
its scrubbed, role/SEG-labelled output.
