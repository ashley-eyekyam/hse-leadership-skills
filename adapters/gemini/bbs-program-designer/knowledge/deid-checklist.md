# De-identification Checklist — BBS Program Designer (REINFORCED)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **For this skill the reinforcement is the non-punitive-card rule.** A behaviour-based
> safety program lives or dies on being non-punitive: an observation card that records a
> **nameable individual for discipline** re-identifies and punishes the observed worker.
> That is the single most important de-id failure mode here and is enforced as a
> `de_identification` **hard-fail** in the eval suite (the seeded-leak fixture
> `evals/files/deid-leak.md` proves the gate is live).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
BBS-specific reinforcement that the De-identifier subagent applies FIRST.

## 1. Treat all observation/participation data as identifying in a small crew

Observation cards, participation logs, and any free-text observer note can identify the
**observed worker** — especially in a small crew where "the night-shift forklift driver"
is one person. Handle every input under the strictest tier from the first read, before
any analysis.

## 2. DETECT & FLAG every identifier up front

List, before drafting: worker/observer names, employee IDs, contact details, exact
dates+times of an observation, a fine-grained role/shift label that identifies one
person, and any photo. If unsure whether something identifies an individual in a small
population, treat it as identifying.

## 3. PSEUDONYMIZE to role/group labels — and NEVER a discipline card

Replace every individual with a stable **role/group label** ("a picker", "the loading
crew"). **No card ever records a nameable individual for discipline** — observation data
is **role-labelled or anonymous**, **voluntary**, and used for **trending and learning,
never individual sanction**. A card naming an individual for discipline is a
`de_identification` **hard-fail**, non-waivable. Produce (a) the de-identified output and
(b) a SEPARATE re-identification key if one is unavoidable; **never embed the key or any
name↔label mapping in the document**.

## 4. SMALL-CELL SUPPRESSION — the `<5` rule (HARD)

- **Suppress any team/crew breakdown with fewer than 5 individuals.** A percent-safe or
  participation figure for a group of 4 or fewer is **not** published — aggregate up to a
  group of ≥5 or report the parent group only.
- **Secondary suppression** — when one cell is suppressed, suppress (or aggregate) a
  second cell so the suppressed value cannot be back-calculated from row/column totals.
- This applies to percent-safe by sub-team, participation by crew, AND any at-risk
  category broken down by a small group. A sub-5 cell published unsuppressed is a
  `de_identification` **hard-fail**.

## 5. TREND BY CATEGORY, NEVER BY PERSON

Metrics and trends are reported **by behaviour category** (manual handling, line-of-fire,
…), never **by person**. A "percent-safe leaderboard" naming or ranking individuals is a
de-id and a non-punitive-design failure.

## 6. WARN BEFORE WIDE DISTRIBUTION

Roll-up summaries, posters and any widely shared artifact default to fully aggregated,
category-level findings. Warn the user before any finer-grained breakdown enters a widely
shared copy.

## 7. Re-identification key handling

If a re-identification key is genuinely needed (e.g. to follow up a serious unsafe act
through the proper process, NOT the BBS program), hold it as a SEPARATE,
access-controlled artifact. It is **never embedded** in the de-identified document and
never shared with a sibling subagent.

## Observable pass conditions (what the grader checks)

1. Identifiers listed before the draft (the de-id pass ran first).
2. **No card records a nameable individual for discipline** (the non-punitive rule).
3. No residual direct identifier in the output (name, phone, email, address, employee ID).
4. No re-identification key / name↔label mapping embedded in the output.
5. **No team breakdown of fewer than 5 published** (the `<5` small-cell rule).

Any single failing condition is a non-waivable `de_identification` hard-fail.
