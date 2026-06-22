# De-identification Checklist — Psychosocial Risk Assessment (REINFORCED, D-06)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **This skill is one of the three highest-de-id-sensitivity skills.** Psychosocial
> survey responses, focus-group transcripts and sickness-absence data are
> **special-category health data** (GDPR Art. 9 / India DPDP / OSHA-aligned). The
> reinforced `<5` small-cell suppression + secondary-suppression rules below are
> **stricter than, and additional to,** the standard de-id block — and they are
> enforced as a `de_identification` **hard-fail** in the eval suite (eval case 2).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline.
The byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is
the special-category reinforcement that the De-identifier subagent applies FIRST.

## 1. Treat ALL psychosocial inputs as special-category health data

Survey results, focus-group themes, sickness-absence/turnover records, grievance and
incident data, and any free-text disclosure (e.g. a respondent mentioning a diagnosis
or medication) are **special-category health data**. Handle every one of them under
the strictest tier from the first read — before any analysis.

## 2. DETECT & FLAG every identifier up front

List, before drafting: respondent names, contact details, home/site addresses, payroll
or employee IDs, exact dates, sub-team / shift / role labels fine-grained enough to
identify, and **any disclosed health detail** (diagnosis, medication, GP/OH visits,
absence reason). If unsure whether something is identifying in a small population,
treat it as identifying.

## 3. PSEUDONYMIZE to role/group labels

Replace every individual with a stable **role/group label** ("Night-shift advisers",
"Team-lead role"). **No individual is ever named as "the risk"** — a psychosocial
finding is always attributed to the **work design** for a role/group, never a person.
Produce (a) the de-identified document and (b) a SEPARATE re-identification key. **Never
embed the key or any name↔label mapping in the document.**

## 4. SMALL-CELL SUPPRESSION — the `<5` rule (HARD)

- **Suppress any domain/team/sub-group breakdown with fewer than 5 respondents.** A
  result for a group of 4 or fewer is **not** published — aggregate up to a group of
  ≥5 or report the parent group only.
- **Secondary suppression** — when one cell is suppressed, suppress (or aggregate) a
  second cell so the suppressed value cannot be back-calculated from row/column totals.
- This applies to survey breakdowns, focus-group counts, AND sickness-absence/illness
  cells. A sub-5 cell published unsuppressed is a `de_identification` **hard-fail**.

## 5. CONFIDENTIALITY THRESHOLD by source

Honour the per-source confidentiality threshold captured in intake Q3b (default ≥5
respondents to publish a breakdown). Verbatim focus-group quotes are **paraphrased and
aggregated** — never reproduced in a way that identifies the speaker in a small team.

## 6. WARN BEFORE WIDE DISTRIBUTION

Management summaries, board packs and any widely shared artifact default to fully
aggregated, role/group-level findings. Warn the user before any finer-grained breakdown
or any health detail enters a widely shared copy.

## 7. MINIMIZE & LIMIT PURPOSE

Use only the data the assessment needs. Keep raw survey/focus-group/absence data out of
external services where you can. Where a genuine legal question arises (a consent
question, a suspected breach, a cross-border transfer), stop and defer to a competent
person.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, phone, email, address, gov/payroll
   ID, DOB-with-value).
3. No re-identification key / name↔label mapping embedded in the output.
4. **No domain/team/illness cell of fewer than 5 published** (the `<5` small-cell rule).

Any single failing condition is a non-waivable `de_identification` hard-fail.
