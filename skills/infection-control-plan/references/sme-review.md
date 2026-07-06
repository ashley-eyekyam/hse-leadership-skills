---
sme-review:
  personas:
    - role: "Infection Prevention & Control (IPC) Doctor / Nurse Consultant (CDC/WHO IPC competent)"
      expertise: "The CDC Guideline for Isolation Precautions — Standard Precautions (hand hygiene, PPE by anticipated exposure, respiratory hygiene, safe injection, environmental cleaning) and Transmission-Based precautions selected by route (contact: single room/cohort + gown & gloves + dedicated equipment; droplet: single room/spatial separation + surgical mask; airborne: airborne-infection isolation room (negative pressure) + fit-tested respirator + restricted entry); the WHO Core Components of IPC Programmes (programme & team, guidelines, education, surveillance, multimodal strategy, monitoring/audit & feedback, workload/staffing/bed-occupancy, built environment); the Spaulding classification for device reprocessing (critical → sterilization, semi-critical → high-level disinfection, non-critical → low-level disinfection); the hierarchy of controls applied to IPC (ventilation, negative-pressure isolation, single rooms and administrative controls before PPE); the UK Health and Social Care Act 2008 Code of Practice (the Hygiene Code) and India Bio-Medical Waste Management Rules 2016 segregation via hse-india; and the special-category-health-data (PHI) handling of a patient's infection / colonisation status and outbreak / cluster surveillance (GDPR Art. 9 / OSHA 1910.1030(f) confidentiality), including small-cell suppression so a small cluster on a named ward cannot re-identify a patient."
      lens: "Does the plan apply Standard Precautions to every patient and layer the correct Transmission-Based precautions by the identified route? Does it lead with engineering controls (ventilation, negative-pressure / airborne-infection isolation rooms, single rooms) and administrative controls (cohorting, screening, signage, restricted entry) BEFORE PPE — is an airborne agent managed by a respirator alone with no isolation room or ventilation provision FLAGGED and pushed up the hierarchy, with PPE recorded as the residual barrier? Is the Spaulding reprocessing decision correct — is a critical device sterilized (never merely high-level disinfected)? Is the WHO IPC programme structured against the core components? Is the surveillance de-identified / aggregated, with every <5 case / cluster category suppressed (including the secondary back-calculation, so a 3-case cluster on a named ward cannot re-identify a patient)? Is any patient's infection / colonisation status scrubbed with ZERO leak — never attributed to a named person — and is no re-identification key co-located or emitted as a file?"
modes:
  ipc-plan:
    detected_by: Q10 — Output artifact wanted + its reader (full IPC plan + programme structure / plan summary + surveillance structure / quick route-precautions answer — all render the single IPC plan at the reader's depth)
    floor:
    - id: icp-route-driven-precautions
      description: Precautions selected per transmission route — Standard plus contact / droplet / airborne (intake Q2, the routing anchor; CDC isolation guideline / KB-STD-IPC-CDC-WHO)
      anchors:
      - transmission.based|transmission route
      - contact
      - droplet|airborne
      min_matches: 1
    - id: icp-engineering-before-ppe
      description: Engineering / environmental controls (ventilation, negative-pressure / airborne-infection isolation room, single rooms) precede PPE on the airborne route (intake Q3; a respirator-only airborne plan is FLAGGED)
      anchors:
      - ventilation
      - negative.pressure|isolation room|AIIR
      - engineering
      min_matches: 1
    - id: icp-spaulding
      description: The Spaulding reprocessing decision per device class — critical to sterilization, semi-critical to high-level disinfection, non-critical to low-level (intake Q5; a high-level-disinfected critical device fails)
      anchors:
      - Spaulding
      - steril
      - high.level disinfection|semi.critical
      min_matches: 1
    - id: icp-admin-controls
      description: Administrative controls — cohorting, early screening / triage, isolation signage, a hand-hygiene programme + audit (intake Q4; these precede PPE)
      anchors:
      - cohort
      - hand.hygiene
      - screening|triage|signage
      min_matches: 1
    - id: icp-surveillance-deid
      description: De-identified / aggregated HAI / outbreak surveillance with case definitions and `<5` small-cell suppression against re-identification (intake Q6; PHI gate)
      anchors:
      - surveillance
      - de.identif|aggregat|suppress
      - case definition|outbreak|cluster
      min_matches: 1
    - id: icp-owner-review
      description: Named action owner(s) + a competent infection-prevention-and-control-professional verifier + a review cycle (annual IPC review / on-outbreak / on-guideline-change) (intake Q11/Q12)
      anchors:
      - owner
      - review
      - infection.prevention|IPC
      min_matches: 1
---

# SME Review & Sign-off — infection-control-plan

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into an **Infection Prevention & Control (IPC) Doctor / Nurse Consultant**
(CDC/WHO IPC competent). The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only-control, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Standard Precautions for every patient + the route-correct Transmission-Based precautions** —
      the route is identified and the correct contact / droplet / airborne precaution set is layered;
      a plan that jumps to PPE without the room / ventilation control the route requires is the
      headline failure, surfaced by `controls.validate_treatment` (`ppe_admin_only=True`).
- [ ] **Engineering and administrative controls are recorded BEFORE PPE** — an airborne agent managed
      by a respirator alone with no airborne-infection isolation room or ventilation provision is
      **flagged** and pushed up the hierarchy; PPE is the residual barrier, never the primary control.
- [ ] **The Spaulding reprocessing decision is correct** — a critical device (sterile tissue /
      bloodstream) is **sterilized**, never merely high-level disinfected; semi-critical → high-level
      disinfection; non-critical → low-level. A high-level-disinfected critical device fails.
- [ ] **The WHO IPC programme is structured against the core components** — programme/team,
      guidelines, education, surveillance, multimodal strategy, monitoring/feedback, workload/staffing,
      built environment.
- [ ] **The surveillance is de-identified / aggregated** — never line-level; **every `<5` case /
      cluster category is suppressed** (including the secondary back-calculation guard, so a 3-case
      cluster on a named ward cannot re-identify a patient).
- [ ] **A patient's infection / colonisation status + any outbreak detail are de-identified** — no
      infection status attributed to a named person, no named patient or staff member, no `<5` case
      cell, and no embedded / co-located re-identification key (and no key file) in the circulated
      artifact (a leak is a non-waivable `de_identification` hard-fail).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The airborne route managed by a respirator alone** — a plan can look complete yet never provision ventilation / negative-pressure (AIIR); confirm the engineering control precedes PPE on every airborne agent.
- **A Spaulding mis-application** — a critical (sterile-tissue- or bloodstream-contacting) device assigned high-level disinfection instead of sterilization silently downgrades reprocessing; check each device against critical / semi-critical / non-critical.
- **Surveillance published at re-identifying granularity** — an outbreak / cluster of `<5` on a named ward, or a patient's infection status attributed by name, must be aggregated and suppressed with a secondary back-calculation guard.

## Sign-off note
SME review: ran (persona: Infection Prevention & Control (IPC) Doctor / Nurse Consultant); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person review**,
and it never outputs the affirmative claim that the work is approved. A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score
below threshold) are a separate enforcement class.
