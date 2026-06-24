<!-- KB-DATA-RECORDABILITY-TESTS -->
# Recordability & reportability tests — OSHA 1904 / RIDDOR 2013 (each cited)

**Fragment ID:** `KB-DATA-RECORDABILITY-TESTS`
**What this is:** the **decision-logic reference** the `regulatory-returns` (#27) skill
applies to determine whether an incident is *recordable* (US OSHA) or *reportable* (UK
RIDDOR / EU equivalents), which form applies, and the deadline. Each test and deadline
carries a named **authority + year**.
**What this is NOT:** legal advice, a complete rule text, or a source of India national form
numbers. The binding rule is read from the cited regulation at use time. **The India row
POINTS INTO `hse-india`** (`factories-act-returns` / `india-accident-notice` /
`india-state-form-finder`) after mandatory state detection — **no national India form number
is ever minted here**; an unverified form id is left literal `[GAP]`.

> Source: US OSHA 29 CFR 1904 (Forms 300/300A/301; 1904.41 electronic) · UK RIDDOR 2013 (reg. 4/7/8/9, Sch. 1/2) · EU member-state transposition · India → hse-india · Year: 2026 · Reviewed: 2026-06-22 · Volatile: true (recordkeeping rules & thresholds revised; resolve binding test/deadline at use time).

---

## US — OSHA 29 CFR 1904 recordability

| Test | Recordable if … | Form & deadline |
|---|---|---|
| Work-relatedness + new case + beyond first aid | Death, days away, restricted work/transfer, medical treatment beyond first aid, loss of consciousness, or a significant diagnosed injury/illness. | Log on **Form 300** within **7 calendar days**; **Form 301** incident report within 7 days; **Form 300A** annual summary posted **Feb 1 – Apr 30**. "OSHA 29 CFR 1904.7/1904.29, 2024" |
| First-aid-only | NOT recordable (the 1904.7(b)(5) first-aid list). | No entry — but evidence the test was applied. "OSHA 1904.7(b)(5)" |
| Electronic submission applicability | By establishment size/NAICS (1904.41). | Electronic **300A** (and 300/301 for covered establishments) by the annual deadline. "OSHA 1904.41, 2024" |

## UK — RIDDOR 2013 reportability

| Test | Reportable if … | Deadline |
|---|---|---|
| Specified injury | A reg. 4 / Sch. 1 specified injury (e.g. fracture (not fingers/thumbs/toes), amputation, loss of sight). | Report **without delay**; written report within **10 days**. "RIDDOR 2013 reg.4/Sch.1" |
| Over-7-day incapacitation | Incapacitated for routine work > 7 consecutive days. | Within **15 days** of the accident. "RIDDOR 2013 reg.4(2)" |
| Dangerous occurrence | A reg. 7 / Sch. 2 listed dangerous occurrence. | Without delay; written within 10 days. "RIDDOR 2013 reg.7/Sch.2" |
| Occupational disease | A reg. 8/9 reportable disease on diagnosis. | Without delay on receiving the diagnosis. "RIDDOR 2013 reg.8/9" |

## EU / India

| Jurisdiction | Resolution |
|---|---|
| EU member state | Resolve the binding return from the **member-state transposition** of the Framework Directive; cite the national instrument + year. |
| **India** | **→ `hse-india`** — run state detection first, then resolve the state accident-notice/return via `india-accident-notice` / `factories-act-returns` / `india-state-form-finder`. **No national form number is asserted here**; leave `[GAP]` until `hse-india` resolves it. |

**Discipline:** never assert a "reportable yes/no" without the incident facts the test needs;
never assert a deadline without the jurisdiction (#27 eval case 1). The statutory submission
contains injured-person identity by law, but every internal/working copy is de-identified,
with `<5` small-cell suppression on any aggregated summary (e.g. 300A by department).

## How the skill uses this fragment

- **#27 regulatory-returns** reads jurisdiction + incident facts → applies the cited test →
  identifies the form + deadline → prepares a de-identified return with the evidence trail
  (`KB-SNIP-RETURNS-METHOD` drives the method). An India scenario that hard-codes a national
  form number instead of deferring to `hse-india` is a `regulatory_citation_accuracy`
  hard-fail (#27 eval case 2).
