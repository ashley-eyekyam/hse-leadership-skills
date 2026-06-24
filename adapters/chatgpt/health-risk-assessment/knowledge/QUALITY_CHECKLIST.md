# Pre-output Quality Checklist — health-risk-assessment

The self-check loop the Workflow runs before assembling the report. Every box must pass; a
failing box is a defect the Critic/QA + SME passes must fix before delivery.

## Specificity (SEGs)
- [ ] Each SEG names the **actual task/role and the agent** (from Q2) — not "all staff" or
      "the workforce"; the intake refused to proceed on a generic SEG.
- [ ] The named site/area (Q8) and exposed population (Q9) appear in the output.
- [ ] No conclusion rests on an unstated assumption — explicit `[ASSUMPTION]` / `[GAP]` only.

## Exposure-vs-OEL comparison (the citation core)
- [ ] **Every** exposure is compared to a **cited OEL/WEL/PEL** resolved from
      `KB-DATA-OEL-LIMITS` / `KB-DATA-EXPOSURE-LIMITS` with **authority + year** — never a
      bare number, never a fabricated limit, never a parallel OEL table.
- [ ] Where there is no exposure data (Q3 = none-yet), a **monitoring strategy is recommended
      first** — no fabricated comparison.

## Ergonomics (deterministic)
- [ ] Every ergonomic score is the `ergonomics` engine's output (RULA grand score + action
      level / REBA final score / NIOSH RWL + Lifting Index), tool-named — **not narrated prose**.
- [ ] The engine `[metrics, table]` pair from `to_report_blocks` is in the report's
      "Ergonomic scores" section.

## Hierarchy of controls (the core value)
- [ ] `KB-SNIP-HOC` applied to **every** control; `controls.rank_controls` ranked them
      Elimination → Substitution → Engineering → Administrative → PPE.
- [ ] **No PPE-only and no surveillance-only treatment** — substitution/engineering precede
      PPE and precede surveillance; `ppe_admin_only` cleared or an explicit "not reasonably
      practicable because…" justification recorded. Surveillance is monitoring, not a control.

## Health-surveillance schedule
- [ ] The surveillance cadence is **OEL-linked** — triggered by the exposure-vs-action-level/
      OEL comparison (audiometry / lung-function / HAV), not asserted.
- [ ] Every surveillance action has a named role owner + an ISO date.

## Citations
- [ ] ISO 45001 6.1.2 cited (and `KB-SNIP-OPS-CLAUSE-MAP`); the jurisdiction surveillance
      regime cited (COSHH / Control of Noise / Control of Vibration / OSHA 1910.95). For India
      the **resolved state form** is cited via `KB-REG-IN-STATEFORMS` — never a national form.

## De-identification (non-waivable — special-category health data)
- [ ] The De-identifier ran FIRST; identifiers listed before drafting.
- [ ] Output uses **SEG/role labels only** — no residual name, no named audiometry/biological-
      monitoring result, **no `<5` health-outcome cell published**, no re-identification key
      embedded.

## Report
- [ ] A valid `report.json` (`hse-report-model/v1`) assembled from the cloned template; the
      `report-output` call produces docx + pdf (or warns-and-degrades).
