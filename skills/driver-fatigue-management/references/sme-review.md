---
sme-review:
  personas:
    - role: "Road-transport safety & driver-fatigue / FRMS specialist (CMIOSH / transport-safety competent; FMCSA HOS + EU 561 + Fatigue Risk Management System practitioner)"
      expertise: "FMCSA Hours-of-Service of Drivers (49 CFR Part 395 — the 11 h driving limit, the 14 h on-duty window, the 30-min break after 8 cumulative driving hours, the 60 h/7-day and 70 h/8-day cycles, the 34 h restart, the sleeper-berth split, and the ELD mandate); EU Regulation (EC) 561/2006 drivers' hours (9 h daily driving extendable to 10 h twice a week, the 45-min break after 4.5 h continuous driving, 11 h daily rest reducible to 9 h, 56 h weekly and 90 h fortnightly driving) and the Reg (EU) 165/2014 tachograph; GB domestic drivers' hours; Fatigue Risk Management System (FRMS) design — roster and journey-plan redesign, built-in rest, and the circadian Window of Circadian Low (WOCL); the distinction between a regulatory compliance flag and an advisory fatigue index (a heuristic, never a regulatory threshold); and India Motor Transport Workers Act 1961 / state rules via hse-india."
      lens: "Are the hours-of-service compliance flags COMPUTED by the fatigue.py engine from the supplied duty log and traced to it — never narrated, never built on an invented driving hour or rest segment (a missing input is a [GAP])? Are the compliance flags presented as the AUTHORITATIVE finding and the fatigue index clearly flagged as an ADVISORY heuristic (never a regulatory threshold or a compliance verdict)? Is every multi-day cycle (60/70 h, 34 h restart) or cross-shift daily-rest claim that is absent from the single-shift log recorded as a [GAP] rather than asserted compliant? Is the fatigue treatment led by schedule/roster/journey-plan/built-in-rest (FRMS) redesign, with any 'stay alert' briefing or in-cab fatigue-detection gadget flagged up the hierarchy rather than taken as the headline control? Is the driver's name / CDL / DOT-medical / OSA / sleep-disorder detail de-identified to role level with ZERO leak and every <5 fatigue-event / sickness cell suppressed?"
modes:
  fatigue-assessment:
    detected_by: "Q1/Q8 — the named fleet/route/depot operation + the output artifact (full fatigue-risk-management report / HOS-compliance + FRMS summary / roster fix-list)"
    floor:
      - id: fat-hos-flags-computed
        description: "The FMCSA 49 CFR 395.3 / EU 561 per-rule PASS/FAIL flags come from the fatigue.py engine and trace to the supplied duty log — a narrated 'looks compliant' verdict or an invented driving hour / rest segment is the failure mode; a missing duty-log input is a [GAP]"
        anchors: ['compliance flag', 'PASS/FAIL', 'compliant', 'duty log', '\[GAP\]']
        min_matches: 2
      - id: fat-compliance-primary-index-advisory
        description: "The compliance flags are the AUTHORITATIVE finding; the fatigue index is rendered as a clearly-flagged ADVISORY heuristic (advisory: True + a note), never a regulatory threshold and never a compliance verdict"
        anchors: ['advisory', 'fatigue index', 'authoritative', 'compliance flag']
        min_matches: 2
      - id: fat-multiday-cycle-gap
        description: "The 60/70 h cycle, the 34 h restart, and the cross-shift daily-rest claim are NOT asserted compliant from a single-shift log — an absent cumulative / cross-shift figure is a literal [GAP]"
        anchors: ['60/70', 'restart', 'cross.shift', 'daily rest', '\[GAP\]']
        min_matches: 2
      - id: fat-roster-frms-leads
        description: "The treatment leads with schedule / roster / journey-plan / built-in-rest (FRMS) redesign; a 'stay alert' briefing, driver-alertness training, or an in-cab fatigue-detection gadget taken as the headline control is pushed up the hierarchy (KB-SNIP-FATIGUE-FRMS)"
        anchors: ['roster', 'FRMS', 'journey.plan', 'hierarchy', 'stay alert']
        min_matches: 2
      - id: fat-driver-oh-deidentified
        description: "No named driver, no CDL / DOT-medical / OSA / sleep-disorder detail, no <5 fatigue-event / sickness-absence cell, no embedded re-identification key in the circulated output (highest de-id tier; a leak is a non-waivable hard-fail)"
        anchors: ['de.identif', 'role label', 'CDL', 'DOT.medical', 'OSA', 'suppress']
        min_matches: 2
      - id: fat-citations-resolve
        description: "FMCSA 49 CFR Part 395 (part/section + the ELD record), EU Regulation (EC) 561/2006 + Reg (EU) 165/2014 tachograph, India via hse-india (state detection; [GAP], no national form) — a fabricated/mis-stated clause is a citation hard-fail"
        anchors: ['49 CFR', '561/2006', 'FMCSA', 'hse.india', 'tachograph']
        min_matches: 1
---

# SME Review & Sign-off — driver-fatigue-management

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **road-transport safety & driver-fatigue / FRMS specialist** (FMCSA
HOS + EU 561 + FRMS competent). The universal hard gates (de-id leak, citation accuracy,
HoC/no-alertness-led, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The HOS compliance flags are COMPUTED, never narrated** — the FMCSA 49 CFR 395.3 / EU 561
      per-rule PASS/FAIL flags come from the `fatigue.py` engine (`fmcsa_compliance` /
      `eu561_compliance`) and trace to the supplied duty log; a narrated "looks compliant" verdict,
      or an invented driving hour / rest segment, is the failure mode this skill exists to prevent.
      A missing duty-log input is a `[GAP]`.
- [ ] **Compliance-flags-primary / advisory-index-secondary is kept distinct** — the compliance
      flags are presented as the **authoritative** finding; the fatigue index is rendered as a
      **clearly-flagged advisory** heuristic (it carries `advisory: True` + a note), **never** a
      regulatory threshold and never a compliance verdict. An index used as the pass/fail call is a
      failure.
- [ ] **Multi-day cycle & cross-shift rest are `[GAP]`, not asserted** — the 60/70 h cycle, the 34 h
      restart, and the cross-shift daily-rest claim are **NOT** asserted compliant from a single-shift
      log; an absent cumulative / cross-shift figure is a literal `[GAP]` (the engine's single-shift
      default is "no breach detectable", not "compliance proven").
- [ ] **Roster/FRMS redesign leads; alertness is flagged up the hierarchy** — the treatment leads
      with schedule / roster / journey-plan / built-in-rest (FRMS) redesign; a "stay alert" briefing,
      driver-alertness training, or an in-cab fatigue-detection gadget taken as the **headline**
      control is the headline failure, surfaced by `controls.validate_treatment`
      (`ppe_admin_only=True`) and pushed up the hierarchy (`KB-SNIP-FATIGUE-FRMS`).
- [ ] **The driver's occupational-health data is de-identified (HIGHEST tier)** — no named driver,
      no CDL / DOT-medical / OSA / sleep-disorder detail, no `<5` fatigue-event / sickness-absence
      cell, no embedded re-identification key in the circulated output (a leak is a non-waivable
      `de_identification` hard-fail).
- [ ] **Citations resolve** — FMCSA **49 CFR Part 395** (the part/section numbers + the ELD record),
      EU **Regulation (EC) 561/2006** + the **Reg (EU) 165/2014** tachograph, India via `hse-india`
      (state detection; `[GAP]`, no national form number). A fabricated or mis-stated clause is a
      regulatory_citation_accuracy hard-fail.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The breach with no bridge** — a per-rule HOS breach or an elevated fatigue index is
  flagged with a roster redesign dated a cycle out, but no interim measure (a journey
  re-plan, a swapped shift, a rest stop) for the drivers running the exposed roster in the
  meantime.
- **The emergency / fitness-to-drive leg** — the assessment computes hours but never states
  the fitness-to-drive self-declaration process, the report-fatigue-without-penalty route, or
  what a driver does when too tired to continue mid-shift; the human backstop to the roster
  maths is missing.
- **The quantitative basis absent** — a control (maximum shift length, minimum rest) is
  asserted without the rule threshold, the current roster figure, or the ELD/tachograph source
  it is measured against, so the finding cannot be reproduced or audited.

## Sign-off note
SME review: ran (persona: road-transport safety & driver-fatigue / FRMS specialist); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person
review**, and it never outputs the affirmative claim that the work is approved. A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented citation,
weighted score below threshold) are a separate enforcement class.
