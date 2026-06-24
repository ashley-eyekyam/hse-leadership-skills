# Pre-output Quality Checklist — ergonomics-assessment

The self-check loop the Workflow runs before assembling the report. Every box must pass; a
failing box is a defect the Critic/QA + SME passes must fix before delivery.

## Specificity (named task)
- [ ] Each scored item names the **actual task/role and the workstation** (from Q2) — not
      "general handling" or "the line"; the intake refused to proceed on a generic task.
- [ ] The named site/area (Q8) and affected role/SEG (Q5) appear in the output.
- [ ] No conclusion rests on an unstated assumption — explicit `[GAP]` only.

## Score traceability (the citation core)
- [ ] Every RULA/REBA/NIOSH score is the `ergonomics` engine's output (RULA grand score +
      action level / REBA final score / NIOSH RWL + Lifting Index), tool-named — **not narrated
      prose and not a copied KB band table**.
- [ ] **Every score shows its input parameters** — a Lifting Index without its lift geometry,
      or a posture score without its joint angles, is a defect (regulatory_citation_accuracy).
- [ ] **A missing required parameter is a `[GAP]`** — no posture angle or load weight is
      invented to complete a score.
- [ ] The engine `[metrics, table]` pair from `to_report_blocks` is in the report's "Computed
      score & action band" section; the action band is cited to the method (NIOSH / RULA / REBA
      / ISO 11228).

## Hierarchy of controls (the core value)
- [ ] `KB-SNIP-HOC` + `KB-SNIP-ERGO-CONTROLS` applied to **every** control; `controls.rank_controls`
      ranked them Elimination → Engineering/redesign → Administrative → PPE/training.
- [ ] **Controls redesign the task before they train the worker** — a high RULA/REBA/LI whose
      only control is manual-handling training (no task/workstation redesign or mechanical aid)
      is flagged training-led and pushed up the hierarchy, or an explicit "not reasonably
      practicable because…" justification is recorded. Training is not a control for a
      biomechanical overload.

## Surveillance / symptom linkage
- [ ] Reported symptoms (Q5) and exposure pattern (Q4) drive a surveillance / re-assessment
      cadence; every surveillance action has a named role owner + an ISO date.

## Citations
- [ ] ISO 45001 6.1.2 cited (and `KB-SNIP-MANUFACTURING-CLAUSE-MAP`); the method cited to source
      (NIOSH equation / RULA / REBA / ISO 11228). For India the **resolved state** is handled via
      `hse-india` — a state return owed is a `[GAP]`, **never a national form number**.

## De-identification (non-waivable — special-category MSD/fitness data)
- [ ] The De-identifier ran FIRST; identifiers listed before drafting.
- [ ] Output uses **role/SEG labels only** — no residual name, no named back-injury/fitness note,
      **no `<5` symptom/health-outcome cell published**, no re-identification key embedded.

## Report
- [ ] A valid `report.json` (`hse-report-model/v1`) assembled from the cloned template; the
      `report-output` call produces docx + pdf (or warns-and-degrades).
