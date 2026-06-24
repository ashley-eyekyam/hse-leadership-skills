---
sme-review:
  personas:
    - role: "Healthcare Security / Workplace-Violence-Prevention Specialist (OSHA 3148 / Cal-OSHA 8 CCR 3342 competent; with occupational-health input)"
      expertise: "OSHA Publication 3148 (2016) Guidelines for Preventing Workplace Violence for Healthcare and Social Service Workers — the five program elements (management commitment & worker participation, worksite analysis & hazard identification, hazard prevention & control via the hierarchy of controls, safety & health training, recordkeeping & program evaluation), enforced under the OSH Act §5(a)(1) General Duty Clause where a recognized WPV hazard exists; the Cal/OSHA Workplace Violence Prevention in Health Care standard, 8 CCR 3342 (written plan, type-1-4 violence taxonomy, employee involvement, violent-incident log, serious-incident reporting); the NIOSH / Cal-OSHA type-1-4 violence taxonomy (criminal-intent / customer-client-patient / worker-on-worker / personal-relationship) and how each type drives a different control set; the UK HSE management of work-related violence guidance and NICE NG10 (violence & aggression: short-term management in health/community settings); the environmental / engineering controls (controlled access, sightlines, alarms / duress, secure design), the administrative controls (staffing / skill-mix, lone-working, de-identified known-risk-patient flagging, no-retaliation reporting), and de-escalation / response / training as the residual lines; and the special-category-health-data (PHI) handling of a named victim, assailant, or known-risk patient and any behavioural-health flag (GDPR Art. 9 / OSHA confidentiality-aligned)."
      lens: "Does the program lead with the worksite hazard analysis and environmental-and-administrative controls rather than reactive measures — is the worksite hazard analysis recorded BEFORE any control, and is a program headlined by 'issue personal alarms / run self-defence training' with no access-control, sightline, alarm-system, or staffing / lone-working control FLAGGED and pushed up the hierarchy? Is the exposure classified by the type-1-4 taxonomy, with each type's distinct control set applied? Are the OSHA 3148 five program elements all present, the General-Duty-Clause basis stated correctly, and (in California) 8 CCR 3342 cited as the binding standard? Is the de-escalation / response protocol + post-incident support + training present as the residual line, never the headline? Is the WPV incident log de-identified / aggregated, with every <5 incident category suppressed (including the secondary back-calculation)? Is any named victim, assailant, or known-risk patient and any behavioural-health flag scrubbed with ZERO leak, and is no re-identification key co-located or emitted as a file?"
---

# SME Review & Sign-off — workplace-violence-prevention

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **Healthcare Security / Workplace-Violence-Prevention Specialist**
(OSHA 3148 / Cal-OSHA 8 CCR 3342 competent; with occupational-health input). The universal hard
gates (de-id leak, citation accuracy, HoC/no-reactive-led, owned-and-dated actions) are the enforced
class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The worksite hazard analysis is recorded FIRST, before any control** — the program leads
      with the de-identified worksite analysis (`KB-REG-WPV-OSHA3148` element 2); a program with no
      worksite analysis is the headline failure.
- [ ] **Environmental and administrative controls lead, reactive measures are residual** — a
      treatment headlined by "issue personal alarms / run self-defence training" with no
      access-control, sightline, alarm-system, or staffing / lone-working control is surfaced by
      `controls.validate_treatment` (`ppe_admin_only=True`) and pushed up the hierarchy.
- [ ] **The type-1-4 taxonomy is applied correctly** — the exposure is classified by source (type 1
      criminal-intent / type 2 customer-patient-client / type 3 worker-on-worker / type 4
      personal-relationship) and each type drives its distinct control set; mis-applying the
      taxonomy is a failure.
- [ ] **The OSHA 3148 five program elements are all present** — management commitment & worker
      participation, worksite analysis, hazard prevention & control, training, recordkeeping &
      evaluation; the §5(a)(1) General Duty Clause basis is stated correctly, and in California
      **8 CCR 3342** is cited as the binding standard (not just the General Duty Clause).
- [ ] **The WPV incident log is de-identified / aggregated** — the recordkeeping fields are present,
      but the circulated log is structural / aggregated, never line-level; **every `<5` incident
      category is suppressed** (including the secondary back-calculation guard).
- [ ] **De-escalation, response & training are the documented last lines** — never the primary
      control; they are the residual barrier after the worksite analysis, environmental controls,
      and administrative controls.
- [ ] **The named victim / assailant / known-risk patient + any behavioural-health flag are
      de-identified** — no named victim, assailant, or known-risk patient, no behavioural-health flag
      tied to a person, no `<5` incident cell, and no embedded / co-located re-identification key
      (and no key file) in the circulated artifact (a leak is a non-waivable `de_identification`
      hard-fail).

## Sign-off note
SME review: ran (persona: Healthcare Security / Workplace-Violence-Prevention Specialist); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person review**,
and it never outputs the affirmative claim that the work is approved. A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score
below threshold) are a separate enforcement class.
