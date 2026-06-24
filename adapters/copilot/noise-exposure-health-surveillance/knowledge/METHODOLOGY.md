# Methodology — Noise exposure assessment + hearing-conservation / audiometric surveillance

This is the domain method `noise-exposure-health-surveillance` applies. The SKILL.md Workflow is
the operational summary; this file is the full reference. Every conclusion is traced to a cited
source (action level / exposure limit with authority+year; method from ISO 1999 / 9612), every
control is ranked through the hierarchy of controls (hearing protection **LAST**), and every
action carries a named owner and a date — never a vague, hearing-protection-only treatment, and
**never a computed dB figure** (the skill transcribes measured values; no dosimetry is
calculated — D-08a).

## 0. De-identify first — special-category audiometric health data

**Audiometric thresholds, standard-threshold-shift (STS) determinations, NIHL diagnoses, and
fitness-for-work notes are GDPR Art. 9 / India DPDP special-category health data**. Before any
drafting (the `deid` block + `references/deid-checklist.md`): scrub names to stable SEG/role
labels, **report by SEG/role not by individual**, apply **`<5` small-cell suppression to every
audiometric breakdown**, and **never circulate an audiometry / STS result with a name**. The
re-identification key is held separately, never embedded. This is the **strictest de-id tier in
the phase** (CONV-7).

## 1. Define the area / similar-exposure group (SEG)

From the Q2 named area + roles, group workers with materially the same noise exposure (same
sources, same area, same controls) into SEGs — the SEG is the **unit of assessment and of
audiometric surveillance**. Refuse a generic area ("the factory") or SEG ("all staff"); each
SEG names the area/process and the roles. Flag `[GAP]` where the basis is uncertain — never
invent a SEG.

## 2. Characterise exposure & compare to a CITED action level / limit (transcribed, not computed)

For each SEG/area, **transcribe** the measured or estimated exposure (Q3) — the **8-hr TWA /
L_EX,8h dB(A)** (and peak / dB(C) if impulsive) — and compare it to the binding action level /
exposure limit resolved **with authority+year**:

- **USA** — OSHA 29 CFR **1910.95**: **85 dBA** action level (hearing-conservation program +
  audiometry) / **90 dBA** PEL, 8-hr TWA (KB-REG-OSHA1910-95).
- **UK / EU** — Control of Noise at Work Regs 2005 / Directive 2003/10/EC: lower action
  **80 dB(A)**, upper action **85 dB(A)**, limit **87 dB(A)** at-ear.

The skill **does NOT compute dosimetry** (D-08a): the measured/estimated value is the input; the
method facts are grounded in `KB-STD-ISO1999-9612` (ISO 9612 measurement, ISO 1999 NIHL
estimation). An exposure with **no cited threshold**, or a **fabricated dB figure**, is a defect
(specificity · regulatory_citation_accuracy). If Q1 is *none-yet*, **do not fabricate a
comparison** — recommend a measurement strategy first and stop.

> India lacks a single consolidated statutory noise-limit list cited here; for India sites
> resolve the **state** first, **defer to `hse-india`**, and emit a literal `[GAP]` — **never a
> minted national form-id** (CONV-8 three-tier).

## 3. Map exposure zones

From the per-SEG/area exposures, map the area into **exposure zones** (e.g. < 80 dB(A) /
80–85 / 85–90 / ≥ 90), each with its SEG(s), the cited threshold crossed, and the resulting
obligation (signage / mandatory-HPD zone / hearing-conservation enrolment). The zone map is the
spatial summary that drives signage and entry controls.

## 4. Rank noise-reduction controls up the hierarchy (hearing protection LAST)

Apply `KB-SNIP-HOC` + `KB-SNIP-NOISE-CONTROL-HIERARCHY` and call `controls.rank_controls` +
`controls.validate_treatment`: **eliminate/substitute the source → engineering enclosure/damping
→ distance/time admin → hearing protection LAST**. A plan whose **only** control for **≥ 85 dBA**
is "issue ear defenders" (no source/engineering assessment) is **PPE-led** and is a defect the
Critic/QA pass must catch. If `ppe_admin_only` is `True`, add a higher-order control **or** record
an explicit "higher-order controls not reasonably practicable because…" justification. Rate the
residual exposure with `risk_matrix.score`.

## 5. Set the action-level-linked audiometry surveillance schedule

Where exposure is **at/above the action level** (≥ 85 dBA OSHA; ≥ 85 dB(A) upper action UK),
**audiometric surveillance is required**: **baseline** audiogram on enrolment, **annual**
audiograms thereafter, with **standard-threshold-shift (STS)** comparison against baseline and
follow-up (retest / referral / control review) on a confirmed STS. **Below** the action level,
set a monitoring / re-assessment cadence — surveillance not yet triggered. The schedule is
**keyed to the cited action-level comparison**, not asserted. STS outcomes are reported by
SEG/role with **`<5` suppression**.

## 6. SMART actions (named owners + dates)

Every noise-reduction and surveillance action becomes a SMART action (named role owner + ISO due
date + measure + SEG link), validated by `smart_actions.validate_register`. No anonymous or
undated actions, no "ASAP".

## 7. Output / report assembly

Assemble one `report.json` (`hse-report-model/v1`) from
`assets/noise-exposure-health-surveillance.report.json` and run the canonical `report-output`
call. Section order: Area/SEG & exposure-zone map → Exposure-vs-action/limit comparison →
Noise-reduction plan (hierarchy-ranked, residual) → Hearing-conservation-program elements →
Audiometry surveillance schedule (baseline / annual / STS triggers) → Owned/dated actions →
Assumptions / `[GAP]` → Review & sign-off.

## 8. Evidence & defensibility

Every area/SEG named; every exposure compared to a cited action level / limit (authority+year)
and **transcribed not computed**; every control HoC-ranked above hearing protection; the
audiometry schedule action-level-linked; every action owned + dated; every citation traced to
the KB; zero special-category audiometric leak. The output is **decision-support**; a competent
person (occupational hygienist / audiometric technician / OH physician) must review it.
