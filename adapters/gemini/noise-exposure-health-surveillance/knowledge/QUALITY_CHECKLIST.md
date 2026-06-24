# Pre-output Quality Checklist — noise-exposure-health-surveillance

The self-check loop the Workflow runs before assembling the report. Every box must pass; a
failing box is a defect the Critic/QA + SME passes must fix before delivery.

## Specificity (areas / SEGs)
- [ ] Each SEG names the **actual area/process and the roles** (from Q2) — not "the factory" or
      "all staff"; the intake refused to proceed on a generic area/SEG.
- [ ] The named site/area (Q8) and the noise sources (Q4) appear in the output.
- [ ] No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` / `[GAP]` only.

## Exposure-vs-action/limit comparison (the citation core)
- [ ] **Every** exposure is compared to a **cited action level / exposure limit** with
      **authority + year** (OSHA 1910.95 85/90 dBA; Noise Regs 2005 80/85/87 dB(A)) — never a
      bare number, never a fabricated dB figure, never a fabricated threshold.
- [ ] The exposure value is **transcribed** (measured / estimated), **not computed** — no
      dosimetry calculation; no narrated dB with no source value.
- [ ] Where there is no exposure data (Q1 = none-yet), a **measurement strategy is recommended
      first** — no fabricated comparison, no surveillance plan set.

## Exposure-zone map
- [ ] The area is mapped into **exposure zones** keyed to the cited thresholds, each with its
      SEG(s) and the resulting obligation (signage / mandatory-HPD zone / hearing-conservation).

## Hierarchy of controls (the core value)
- [ ] `KB-SNIP-HOC` + `KB-SNIP-NOISE-CONTROL-HIERARCHY` applied to **every** control;
      `controls.rank_controls` ranked them source/substitution → engineering → administrative →
      **hearing protection LAST**.
- [ ] **No hearing-protection-only treatment for ≥ 85 dBA** — source/engineering precede HPD;
      "issue ear defenders" as the only control is **flagged PPE-led**; `ppe_admin_only` cleared
      or an explicit "not reasonably practicable because…" justification recorded.

## Audiometry surveillance schedule
- [ ] The audiometry cadence is **action-level-linked** — **baseline + annual** audiometry
      triggered by the exposure-vs-action-level comparison (≥ 85 dBA), with **STS** comparison +
      follow-up — not asserted.
- [ ] Every surveillance action has a named role owner + an ISO date.

## Citations
- [ ] ISO 45001 6.1.2 cited (and `KB-SNIP-MANUFACTURING-CLAUSE-MAP`); the jurisdiction noise
      regime cited with authority+year (OSHA 1910.95 / Control of Noise at Work Regs 2005). For
      **India** the state is resolved, the skill **defers to `hse-india`**, and a literal `[GAP]`
      is emitted — **never a minted national form-id**.

## De-identification (non-waivable — special-category audiometric health data)
- [ ] The De-identifier ran FIRST; identifiers listed before drafting.
- [ ] Output uses **SEG/role labels only** — no residual name, no named audiometry / STS result,
      **no `<5` audiometric cell published**, no re-identification key embedded.

## Report
- [ ] A valid `report.json` (`hse-report-model/v1`) assembled from
      `assets/noise-exposure-health-surveillance.report.json`; the `report-output` call produces
      docx + pdf (or warns-and-degrades).
