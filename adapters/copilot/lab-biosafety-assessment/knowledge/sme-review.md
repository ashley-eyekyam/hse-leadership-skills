---
sme-review:
  personas:
    - role: "Biological Safety Officer (BSO) / Biosafety Professional (CDC/NIH BMBL + WHO Laboratory Biosafety Manual competent; Registered Biosafety Professional (RBP) where available)"
      expertise: "The CDC/NIH Biosafety in Microbiological and Biomedical Laboratories (BMBL, 6th ed.) biosafety levels BSL-1 to BSL-4 (containment practices, facilities, safety equipment per level) and the biosafety-cabinet classes (I / II A-B / III); the WHO Laboratory Biosafety Manual (4th ed.) risk-group classification RG1-RG4 and the agent + procedure + competence risk-assessment approach; the NIH Guidelines for recombinant or synthetic nucleic-acid molecules and Institutional Biosafety Committee (IBC) oversight; UK COSHH 2002 with the ACDP (Advisory Committee on Dangerous Pathogens) hazard groups; OSHA 29 CFR 1910.1030 where a laboratory procedure handles human blood / OPIM; India Bio-Medical Waste Management Rules 2016 lab-waste segregation via hse-india; primary-containment selection (biosafety-cabinet class against the aerosol potential, directional airflow, waste decontamination); laboratory biosecurity / access-control and agent accountability; immunisation and serological surveillance of laboratory workers; and the special-category-health-data (PHI) handling of the specimen-source patient's identity and the worker's serological-surveillance / occupational-health record (GDPR Art. 9 / OSHA 1910.1030(f) confidentiality)."
      lens: "Is the agent's risk group (RG1-RG4) determined FIRST, and where the agent's risk group is unknown or unlisted is a literal [GAP] emitted and routed to a competent biosafety officer rather than a risk group or BSL being INVENTED? Does the selected biosafety level match the established risk group AND the procedure -- is a BSL assigned from the agent alone, ignoring aerosolization, FLAGGED? Is the primary containment (biosafety-cabinet class against the aerosol potential, directional airflow, waste decontamination) selected BEFORE PPE -- is a 'wear a respirator and gloves' treatment with no biosafety cabinet or BSL-appropriate facility FLAGGED and pushed up the hierarchy, with PPE as the residual barrier matched to the BSL? Are the biosecurity / access-control measures present where the agent warrants them, and the immunisation / serological-surveillance offer and the confidential exposure-response pathway authored? Is the specimen-source patient referenced by role only with any clinical detail held separately, the worker's serological-surveillance / OH record held confidentially per 1910.1030(f) / GDPR Art. 9, every <5 lab-incident category suppressed (including the secondary back-calculation), and is the specimen-source-patient identity and the worker's identity scrubbed with ZERO leak and no re-identification key co-located or emitted as a file?"
---

# SME Review & Sign-off — lab-biosafety-assessment

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into a **Biological Safety Officer (BSO) / Biosafety Professional** (BMBL /
WHO LBM competent; RBP where available). The universal hard gates (de-id leak, citation accuracy,
HoC / no-PPE-led, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **The agent's risk group is determined FIRST, and an unknown agent is a `[GAP]`, never
      invented** — the risk group (RG1–RG4) is the primary input to the BSL
      (`KB-SNIP-BIOSAFETY-RA`); where the agent's risk group is unknown or unlisted, a literal
      `[GAP]` is emitted and routed to a competent biosafety officer. An invented risk group or a BSL
      assigned from a guessed risk group is the headline failure.
- [ ] **The selected BSL matches the established risk group AND the procedure** — a BSL assigned from
      the agent alone, ignoring aerosolization, is flagged; the determination (risk group → procedure
      → BSL) is recorded traceably and the citations resolve to BMBL / WHO LBM.
- [ ] **Primary containment (engineering) precedes PPE** — the biosafety-cabinet class is matched to
      the aerosol potential and the agent; directional airflow / ventilation and waste
      decontamination are specified. A "wear a respirator and gloves" treatment of work that requires
      a biosafety cabinet or the BSL facility is surfaced by `controls.validate_treatment`
      (`ppe_admin_only=True`) and pushed up the hierarchy; PPE is the residual barrier matched to the
      BSL.
- [ ] **Biosecurity, surveillance, and the exposure pathway are present and confidential** — the
      biosecurity / access-control measures (where the agent warrants them), the immunisation /
      serological-surveillance offer (held confidentially), and the confidential exposure-response
      pathway (first aid → confidential report → occupational-health follow-up) are authored; the
      worker's serological-surveillance / OH record is held confidentially and **separately** from
      the assessment.
- [ ] **The specimen-source patient + the worker are de-identified** — no specimen-source-patient
      identity, no named worker, no serological-surveillance / serostatus result tied to a person, no
      `<5` lab-incident cell, and no embedded / co-located re-identification key (and no key file) in
      the circulated artifact (a leak is a non-waivable `de_identification` hard-fail).

## Sign-off note
SME review: ran (persona: Biological Safety Officer (BSO) / Biosafety Professional); this is
**decision-support only**. It **precedes — and never replaces — the human competent-person review**,
and it never outputs the affirmative claim that the work is approved. A FLAG it raises is recorded,
never merge-blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score
below threshold) are a separate enforcement class.
