# De-identification Checklist — Safety Culture Assessment (REINFORCED)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **Culture-survey, focus-group and observation data is sensitive personnel data in a
> small population.** A cohort breakdown, a free-text comment, or a verbatim quote can
> re-identify a respondent inside a small team. The reinforced `<5` small-cohort
> suppression + secondary-suppression + no-identifying-quote rules below are **stricter
> than, and additional to,** the standard de-id block — and are enforced as a
> `de_identification` **hard-fail** in the eval suite (eval case 2).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
small-cohort reinforcement that the De-identifier subagent applies FIRST.

## 1. Treat ALL culture inputs as sensitive personnel data in a small population

Survey results and free-text comments, focus-group themes, leadership-walk / observation
notes, participation/turnover records, and any free-text disclosure are **sensitive
personnel data**. In a small site or team, a cohort label fine-grained enough to identify,
or a quoted comment, is itself an identifier. Handle every one of them under the strictest
tier from the first read — before any analysis.

## 2. DETECT & FLAG every identifier up front

List, before drafting: respondent names, contact details, home/site addresses, payroll or
employee IDs, exact dates, **fine-grained cohort labels** (a named team/shift/role small
enough to identify), **verbatim quotes** that reveal who spoke, and any disclosed personal
detail. If unsure whether something is identifying in a small population, treat it as
identifying.

## 3. PSEUDONYMIZE to role/group/cohort labels

Replace every individual with a stable **role/group/cohort label** ("Front-line
operators", "Site-leadership cohort"). **No individual is ever named as "the culture
problem"** — a finding is always attributed to a role/group and to the leadership system /
work design, never a person. Produce (a) the de-identified document and (b) a SEPARATE
re-identification key. **Never embed the key or any name↔label mapping in the document.**

## 4. SMALL-COHORT SUPPRESSION — the `<5` rule (HARD)

- **Suppress any cohort / sub-group breakdown with fewer than 5 respondents.** A maturity
  band or score for a group of 4 or fewer is **not** published — aggregate up to a group
  of ≥5 or report the parent group only. A 4-person department maturity comparison is
  suppressed.
- **Secondary suppression** — when one cohort cell is suppressed, suppress (or aggregate)
  a second cell so the suppressed value cannot be back-calculated from row/column totals.
- This applies to survey cohort breakdowns, focus-group counts, AND any records cells. A
  sub-5 cohort published unsuppressed is a `de_identification` **hard-fail**.

## 5. NO IDENTIFYING VERBATIM QUOTES

Free-text survey comments and focus-group remarks are **paraphrased and aggregated** —
never reproduced verbatim in a way that identifies the speaker in a small team. Honour the
per-cohort confidentiality threshold captured in intake Q3b (default ≥5 respondents to
publish a breakdown; paraphrase-only quotes by default).

## 6. WARN BEFORE WIDE DISTRIBUTION

Leadership summaries, board packs and any widely shared artifact default to fully
aggregated, role/group/cohort-level findings. Warn the user before any finer-grained
cohort breakdown, any verbatim quote, or any personal detail enters a widely shared copy.

## 7. MINIMIZE & LIMIT PURPOSE

Use only the data the assessment needs. Keep raw survey/focus-group/observation data out
of external services where you can. Where a genuine legal question arises (a consent
question, a suspected breach, a cross-border transfer), stop and defer to a competent
person.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, phone, email, address, gov/payroll
   ID, DOB-with-value).
3. No re-identification key / name↔label mapping embedded in the output.
4. **No cohort cell of fewer than 5 published** (the `<5` small-cohort rule), and no
   identifying verbatim quote.

Any single failing condition is a non-waivable `de_identification` hard-fail.
