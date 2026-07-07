---
sme-review:
  personas:
    - role: "GWO-competent wind-turbine work-at-height & rescue technician / trainer"
      expertise: "Wind-turbine WAH operations (nacelle/hub/blade/tower-internal), GWO Working at Heights / First Aid / Advanced Rescue Training, suspension-trauma physiology, two-person climb-team discipline, anchor/fall-protection systems, and tested team-owned rescue methods."
      lens: "would a wind-O&M competent person and the WAH Regs 2005 stand behind this — work at height genuinely avoided where practicable, collective fall-prevention before personal, a TESTED team-owned rescue that recovers a suspended worker in minutes (never 'call 999'), two-person-minimum manning, GWO competence cited not numbered, weather thresholds named but owned by REN-03, zero climber-name / GWO-cert leak"
modes:
  assessment:
    detected_by: "Q = the requested deliverable (a wind-turbine work-at-height / rescue plan for the named turbine) — single-output skill; this mode is always active"
    floor:
      - id: avoid-then-prevent-leads
        description: "Work at height is genuinely tested for avoidance (reg 6) then collective fall-prevention before personal (reg 7)"
        anchors: ['avoid|reg 6', 'collective|reg 7|prevent']
        min_matches: 2
      - id: tested-team-rescue-mandatory
        description: "A suspended-worker rescue plan is present and is a tested, team-owned rescue that recovers in minutes — not 'call 999'"
        anchors: ['rescue', 'tested|two.person|team']
        min_matches: 2
      - id: two-person-minimum-manning
        description: "The climb is a two-person-minimum team with ground support able to initiate the rescue"
        anchors: ['two.person|two person|2.person|minimum', 'team|ground support|manning']
        min_matches: 1
      - id: gwo-competence-cited
        description: "The GWO competence requirement (current WAH / First Aid / ART, 2-yr refresh) is cited, not reproduced"
        anchors: ['gwo|competence', 'cited|refresh|current|wah']
        min_matches: 2
      - id: weather-thresholds-named
        description: "Any hold/stop threshold (hub-height wind cut-off ~15 m/s, lightning) is named here and owned by the weather sibling"
        anchors: ['weather|hub.height|15 m/s|lightning', 'threshold|hold|stop|cut']
        min_matches: 2
      - id: residual-smart-owned
        description: "Residual risk is scored and SMART actions carry role-label owners and dates; unresolved values are [GAP]"
        anchors: ['residual|smart|action', 'owner|date|\[gap']
        min_matches: 2
---

# SME Review & Sign-off — wind-turbine-work-at-height-rescue

The reviewer adopts the **GWO-competent wind WAH & rescue** persona and reads the draft against
the nuanced things only a wind-O&M competent person catches — not just the universal hard gates.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Avoid-then-prevent leads (reg 6/7).** Work at height is genuinely tested for avoidance (ground-level work / lowering the component / man-rider / platform) before any at-height method; where unavoidable, **collective fall-prevention (guardrails / working platform) is selected before personal fall-arrest** — no fall-arrest/PPE-only treatment where avoidance or collective prevention is reasonably practicable.
- [ ] **The rescue plan is mandatory, tested and team-owned.** A suspended-worker rescue is present and is a **tested, two-person-minimum, team-owned capability that recovers the casualty within minutes** (suspension trauma) — **"call 999 / wait for emergency services" is NEVER recorded as the rescue plan** (only as a supplement). An untested capability or an unstated recovery time is flagged `[GAP]`, never left open.
- [ ] **Two-person-minimum manning.** The climb is a two-person-minimum team with ground support able to initiate the rescue; a solo climb is rejected (REN-02 routes lone WAH here).
- [ ] **GWO competence cited, not reproduced.** The GWO competence **requirement** (current WAH / First Aid / ART, 2-yr refresh) is cited; **no licensed module curriculum or certificate number is reproduced** — certificate detail is `[GAP]`, climber identities de-identified to role labels.
- [ ] **Weather thresholds named, not owned.** Any hold/stop threshold (hub-height wind cut-off ≈ 15 m/s, lightning stand-down) is **named and deferred to REN-03 `weather-dynamic-risk-assessment`** — the ≈15 m/s anchor is flagged `[ASSUMED]` / proposed-and-confirmed, never embedded as a hard citation.
- [ ] **Specificity + defensibility.** Every control is specific to the named turbine / site / WAH activity; every conclusion traces to a cited source + year (`KB-REG-WAH2005`, `KB-STD-GWO-WAH-RESCUE`); each action carries a named role owner + a due date; residual risk is re-scored on the 5×5 after the reg-6 controls + tested rescue.
- [ ] **De-identification.** Zero climber name / GWO certificate number / personal contact leak into the circulated copy; the re-identification key is held separately, never embedded.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The rescue plan that is 'call the emergency services' (S1)** — a suspended-worker rescue that
  relies on external responders arriving in time is not a rescue; suspension trauma is a
  minutes-scale emergency. The rescue is tested, team-owned, and recovers in minutes.
- **Avoidance untested** — jumping to fall-arrest without first testing avoidance (ground-level
  work, lifting the task down) and collective before personal protection skips reg 6/7.
- **The lone climb** — a single-climber arrangement with no two-person minimum and no ground
  support able to initiate the rescue removes the rescue capability entirely.
- **GWO reproduced, weather un-owned (S6)** — the GWO competence is cited (not reproduced) and the
  weather hold/stop thresholds are named here but owned by the weather sibling, not silently
  dropped or re-authored.
- **The climb with no isolation (19-08 audit)** — turbine energy isolation / lockout and a
  permit-to-work are absent, and the post-rescue legs (lightning stand-down, anti-suspension-trauma
  handling) are missing; a rescue plan that stops at 'recover in minutes' without the isolation and
  medical legs is incomplete.

## Sign-off note
SME review: ran (persona: GWO-competent wind-turbine work-at-height & rescue technician / trainer);
this is decision-support; competent-person review still required. A FLAG it raises is recorded,
never merge-blocking — it precedes and never replaces the human competent-person review.
