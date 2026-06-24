# De-identification Checklist — Leading/Lagging KPI Framework (REINFORCED)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> **cannot be waived**.
>
> **For this skill the reinforcement is the aggregate-metric rule.** A KPI framework
> reports **aggregate** performance indicators — never an individual's safety record. The
> single most important de-id failure mode here is a **per-person or small-cell breakdown**
> (e.g. a percent-safe or a recordable-injury count for a 3-person team) that
> re-identifies, plus a `<5` cell published without suppression. This is enforced as a
> `de_identification` **hard-fail** in the eval suite (the seeded-leak fixture
> `evals/files/deid-leak.md` proves the gate is live).

This checklist reinforces — it does not replace — the canonical A5 de-id discipline. The
byte-identical `hse:block:deid` block in `SKILL.md` is the contract; this file is the
KPI-specific reinforcement that the De-identifier subagent applies FIRST.

## 1. Metrics are aggregate — never an individual scorecard

Indicators are entity-level (organisation / function / site / fleet). Do not attribute a
metric to a named individual, and treat any breakdown small enough to identify one person
(a single-person team, a fine-grained role/shift label) as identifying from the first read.

## 2. DETECT & FLAG every identifier up front

List, before designing: any worker / owner names, employee or driver IDs, contact details,
exact dates carrying a person, a fine-grained role/shift label that identifies one person,
home/site addresses, and any government ID. If unsure whether something identifies an
individual in a small population, treat it as identifying.

## 3. PSEUDONYMIZE BY DEFAULT

Indicator **owners** and any named person become stable **role labels** ("Owner A",
"Safety Lead"). Produce (a) the de-identified framework and (b) a SEPARATE
re-identification key. **Never embed the key or any name↔label mapping in the output.**

## 4. AGGREGATE SMALL NUMBERS (`<5`) — the load-bearing rule here

Never publish an injury/illness category — or any per-person/per-team indicator
breakdown — with **fewer than 5 individuals**. Aggregate up and apply **secondary
suppression** so a suppressed cell cannot be back-calculated from the totals. A percent-safe
or recordable count for a 4-person crew is **suppressed**.

## 5. WARN BEFORE WIDE DISTRIBUTION

Board / exec dashboards default to de-identified, aggregated figures; warn the user before
any name, individual record, or `<5` cell enters a widely shared artifact.

## 6. MINIMIZE & LIMIT PURPOSE

Use only the data the framework needs — the aggregate metric, not the underlying personal
records. Keep sensitive raw data out of external services where you can.

## 7. Re-identification key handling

The re-identification key is held in a SEPARATE, access-controlled artifact and is **never
embedded** in the framework or its dashboard. (Mirrors the canonical A5 checklist §7.)
