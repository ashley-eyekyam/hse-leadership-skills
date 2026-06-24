# De-identification Checklist — HSE Annual ESG Report (STRICTEST TIER — external publication)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **This is the strictest de-identification tier in the bundle.** The output is an
> **externally-published** annual ESG disclosure (board pack, sustainability report,
> annual-report section, public-facing). Any injury/illness figure — especially a
> **fatality or an ill-health case by site or demographic** — could identify the affected
> person once published. The `<5` small-cell suppression **and** the secondary-suppression
> rule below are **stricter than, and additional to,** the standard de-id block, and they
> are enforced as a `de_identification` **hard-fail** in the eval suite (the de-id PAIR).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
external-publication reinforcement the De-identifier subagent applies FIRST.

## 1. Treat ALL published OH&S figures as publication-sensitive

Injury counts and rates, ill-health figures, fatalities, sickness-absence, and any
breakdown by site / function / demographic are **published to an external, permanent
audience**. Handle every one of them under the strictest tier from the first read — before
any analysis — on the assumption the reader will try to recover the underlying individuals.

## 2. DETECT & FLAG every identifier and every small cell up front

List, before drafting: any residual personal identifier (name, contact, exact date or
location of an event, injured-party role detail), AND **every injury/illness cell with
fewer than 5 individuals**, AND any breakdown (by site, function, shift, demographic) fine-
grained enough that a small group is identifiable. If unsure whether a cell is recoverable,
treat it as recoverable.

## 3. AGGREGATE ALL — publish at the boundary, not the individual

Every injury/illness figure is published **aggregated** to the reporting boundary, by role
label or category only. **No individual incident is narrated** with a date, location, or
injury detail; no individual is named or made identifiable. Produce (a) the published,
aggregated disclosure and (b) — only if a re-identification mapping exists at all — a
SEPARATE access-controlled key. **Never embed any key or name↔label mapping in the
document.**

## 4. SMALL-CELL SUPPRESSION — the `<5` rule (HARD)

- **Suppress any injury/illness category with fewer than 5 individuals.** A fatality cell,
  an ill-health cell, or any site/demographic breakdown of 4 or fewer is **not** published —
  aggregate up to a group of ≥5 or report the parent category only.
- This applies to fatalities, recordable injuries, ill-health, and any sub-group breakdown.
  A sub-5 cell published unsuppressed is a `de_identification` **hard-fail**.

## 5. SECONDARY SUPPRESSION — defeat back-calculation (HARD, the strictest-tier rule)

Primary suppression alone is **insufficient** at this tier: a single suppressed cell is
**back-calculable** when the published total and the remaining cells let a reader subtract
to recover it.

- When one cell is suppressed, **suppress (or aggregate) a second cell** so the suppressed
  value cannot be recovered from the row/column total or the other cells.
- **Define denominators and reporting boundaries** so totals cannot be reverse-engineered to
  a small cell.
- A published table where the suppressed cell = total − (the other published cells) is a
  `de_identification` **hard-fail** — the leak fixture is built to fail on primary-
  suppression-only, and the clean version passes only because secondary suppression is
  applied.

## 6. WARN BEFORE PUBLICATION

The disclosure is, by definition, widely distributed and permanent. Before any figure is
published, confirm the aggregation + `<5` + secondary suppression has been applied and warn
the user that, once published, a small cell cannot be retracted.

## 7. MINIMIZE & LIMIT PURPOSE

Publish only the figures the disclosure requires. Keep raw incident/health records out of
external services. Where a genuine legal question arises (a consent question, a suspected
breach, a cross-border transfer), stop and defer to a competent person.

## Observable pass conditions (what the grader checks)

1. Identifiers and small cells listed before the draft (the de-id pass ran first).
2. No residual direct identifier in the output (name, contact, exact event date+location).
3. No re-identification key / name↔label mapping embedded in the output.
4. **No injury/illness cell of fewer than 5 published** (the `<5` small-cell rule).
5. **No suppressed cell is back-calculable** from a published total + the remaining cells
   (secondary suppression applied).

Any single failing condition is a non-waivable `de_identification` hard-fail.
