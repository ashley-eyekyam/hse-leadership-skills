---
sme-review:
  personas:
    - role: "Occupational-Health Physician / Infection-Prevention & Control (IPC) Nurse Specialist (sharps / bloodborne-pathogen-exposure competent)"
      expertise: "OSHA 29 CFR 1910.1030 — (c) the written Exposure Control Plan + (c)(1)(iv) the annual review and documented safer-device evaluation with non-managerial frontline-worker input, (d)(2) engineering & work-practice controls (engineered sharps-injury protections), (d)(3) PPE as the residual control, (f) the confidential hepatitis-B vaccination offer + the confidential post-exposure evaluation and follow-up, and (h)(5) the Sharps Injury Log; the Needlestick Safety and Prevention Act (PL 106-430); EU Council Directive 2010/32/EU (eliminate unnecessary sharps, safer engineered devices, recapping ban, safe disposal, training, reporting + PEP) and the UK Health and Safety (Sharp Instruments in Healthcare) Regulations 2013 with COSHH + RIDDOR for reportable exposures; India Bio-Medical Waste Management Rules 2016 sharps segregation via hse-india; the clinical post-exposure prophylaxis pathways for HBV/HCV/HIV (source-patient testing with consent, PEP timing); and the special-category-health-data (PHI) handling of source-patient serostatus and the injured worker's exposure/PEP record (GDPR Art. 9 / OSHA 1910.1030(f) confidentiality)."
      lens: "Does the plan lead with elimination and safety-engineered devices rather than a behaviour rule — is the elimination/substitution decision recorded BEFORE any device or PPE, and is a 'staff to take care / wear gloves' treatment of a sharp that could be eliminated or engineered out FLAGGED and pushed up the hierarchy? Does every non-engineered device carry a recorded justification, and is the documented annual safer-device consideration with frontline-worker involvement present? Is the no-recapping rule present and recapping refused? Is the post-exposure pathway confidential — source-patient testing by role only with consent, PEP timing for HBV/HCV/HIV, the worker's medical record held separately per 1910.1030(f)? Is the Sharps Injury Log de-identified / aggregated, with every <5 sharps-injury category suppressed (including the secondary back-calculation)? Is the source-patient serostatus and the injured worker's identity scrubbed with ZERO leak, and is no re-identification / exposure key co-located or emitted as a file?"
modes:
  sharps-exposure-control:
    detected_by: Q9 — Output artifact wanted + its reader (full sharps prevention & exposure-control package / control summary + log structure / quick safer-device answer — all render the single sharps package at the reader's depth)
    floor:
    - id: snm-elimination-first
      description: Elimination/substitution of the sharp stated as the primary control before any safety-engineered device (intake Q2, the first-among-controls decision; KB-SNIP-SHARPS-HIERARCHY)
      anchors:
      - eliminat
      - substitut
      - needle.free
      min_matches: 1
    - id: snm-safety-engineered-devices
      description: Safety-engineered (sharps-protection) devices with the documented annual safer-device consideration and non-managerial frontline-worker involvement (intake Q3; OSHA 29 CFR 1910.1030 / KB-REG-OSHA-BBP)
      anchors:
      - safety.engineered
      - safer.device
      - frontline
      min_matches: 1
    - id: snm-no-recapping-disposal
      description: The no-recapping rule + point-of-use sharps containers + a safe-disposal route as the work-practice controls (intake Q4; a plan permitting recapping by hand fails)
      anchors:
      - recapping
      - sharps container
      - point.of.use|safe.disposal
      min_matches: 1
    - id: snm-pep-pathway
      description: A confidential post-exposure pathway — first aid, confidential report, consented source-patient testing, PEP timing for HBV/HCV/HIV, follow-up (intake Q5; OSHA 1910.1030(f))
      anchors:
      - post.exposure|PEP
      - HBV|HCV|HIV
      - source.patient|consent
      min_matches: 1
    - id: snm-sharps-injury-log
      description: A de-identified / aggregated Sharps Injury Log structure with `<5` small-cell suppression, plus HBV-vaccination status (intake Q5; OSHA 1910.1030(h)(5))
      anchors:
      - Sharps Injury Log
      - de.identif|aggregat|suppress
      - vaccinat
      min_matches: 1
    - id: snm-owner-review
      description: Named action owner(s) + a competent occupational-health / infection-control verifier + a review cycle (annual safer-device review / on-device-change / on-incident) (intake Q10/Q11)
      anchors:
      - owner
      - review
      - occupational.health|infection.control|IPC
      min_matches: 1
---

# SME Review & Sign-off — sharps-needlestick-management

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into an **Occupational-Health Physician / Infection-Prevention & Control
(IPC) Nurse Specialist** (sharps / bloodborne-pathogen-exposure competent). The universal hard gates
(de-id leak, citation accuracy, HoC/no-behaviour-led, owned-and-dated actions) are the enforced class
and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The elimination/substitution decision is recorded FIRST, before any device or PPE** — the
      plan leads with eliminating unnecessary sharps (`KB-SNIP-SHARPS-HIERARCHY`); a "staff to take
      care / wear gloves" treatment of a sharp that could be eliminated or engineered out is the
      headline failure, surfaced by `controls.validate_treatment` (`ppe_admin_only=True`) and pushed
      up the hierarchy. A plan permitting recapping by hand fails.
- [ ] **Every non-engineered device is justified, never assumed** — a non-engineered device left in
      use without a recorded justification is **flagged**, and the **documented annual safer-device
      evaluation with non-managerial frontline-worker input** (OSHA (c)(1)(iv) / Needlestick Act) is
      present.
- [ ] **The post-exposure pathway is confidential and clinically correct** — source-patient testing
      is by role only, **with consent**; PEP timing for HBV/HCV/HIV is present; the HBV-vaccination
      offer + follow-up (1910.1030(f)) is recorded; the injured worker's exposure / PEP medical
      record is held confidentially and **separately** from the plan.
- [ ] **The Sharps Injury Log is de-identified / aggregated** — the OSHA (h)(5) fields are present,
      but the circulated log is structural / aggregated, never line-level; **every `<5` sharps-injury
      category is suppressed** (including the secondary back-calculation guard).
- [ ] **PPE and PEP are the documented last lines** — never the primary control; PPE is the residual
      barrier after elimination, safety-engineered devices, and safe work practices.
- [ ] **The source-patient serostatus + the injured worker are de-identified** — no source-patient
      identity or serostatus, no named injured worker, no `<5` injury cell, and no embedded /
      co-located re-identification / exposure key (and no key file) in the circulated artifact (a
      leak is a non-waivable `de_identification` hard-fail).

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The confidential post-exposure (PEP) pathway collapsed to "report it"** — a polished plan can list safety-engineered devices yet omit consented source-patient testing, PEP timing for HBV/HCV/HIV, and the OSHA 1910.1030(f) confidential follow-up. Check the PEP pathway exists and preserves source-patient and worker confidentiality.
- **The documented annual safer-device evaluation with non-managerial frontline-worker input** — often absent; a device list without the recorded frontline involvement, and without a justification for any non-engineered device still in use, silently drops the OSHA mandate.
- **The Sharps Injury Log rendered line-level, or a `<5` injury category published** — the log must be structural / aggregated with small-cell suppression; a three-injury cell on a named unit re-identifies workers.

## Sign-off note
SME review: ran (persona: Occupational-Health Physician / Infection-Prevention & Control (IPC) Nurse
Specialist); this is **decision-support only**. It **precedes — and never replaces — the human
competent-person review**, and it never outputs the affirmative claim that the work is approved. A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
