<!-- CANDIDATE golden output for lab-biosafety-assessment (HC-05). Generated from eval case 1's
     scenario (diagnostic mycobacteriology lab, primary TB culture with aerosol-generating
     manipulation). It demonstrates the core lever: classify the agent's risk group FIRST, then
     select the BSL with engineering containment BEFORE PPE, and emit [GAP] rather than invent a
     classification. The submitted control -- "issue N95 respirators and gloves and work on the open
     bench" -- substitutes PPE for the biosafety cabinet + BSL-3 facility the risk group and procedure
     require; it is FLAGGED and PUSHED UP the hierarchy. A second unlisted environmental isolate is
     left as [GAP] (risk group not established), never invented. PHI is the highest tier: the
     specimen-source patient is referenced by role only with clinical/serostatus detail held
     separately, the worker is role-labelled with the serological-surveillance record held
     confidentially, and lab-incident data is aggregated with <5 categories suppressed. NOT
     owner-LOCKED -- the owner reviews + locks in P17. -->

# Laboratory Biosafety Risk Assessment — Primary Mycobacterial Culture, Diagnostic Mycobacteriology Laboratory

*Decision-support only. A competent person (a Biological Safety Officer) must review and sign off this
assessment. The specimen-source patient is referenced by role only, with any clinical / serostatus
detail held in a separate confidential record; the worker's identity and serological-surveillance /
occupational-health record are held confidentially and separately; the re-identification key is held
separately and is not part of this document.*

## 1. Laboratory, agent & procedure

De-identification ran first: the specimen-source patient's name, MRN, and clinical detail, and the
worker's name, contact, and serological-surveillance record were scrubbed; the patient and worker are
referenced by role only; no named individual or `<5` lab-incident cell appears below.

- **Laboratory:** diagnostic mycobacteriology laboratory, named site/room (lab- and agent-specific —
  not "a lab").
- **Agent / material:** *Mycobacterium tuberculosis* complex in primary clinical specimens and on
  primary culture — plus one **unlisted environmental mycobacterial isolate** of unestablished risk
  group (carried as a `[GAP]`, see §11).
- **Procedure:** specimen processing and **primary culture with aerosol-generating manipulation**
  (vortexing, centrifugation, sub-culture).
- **Proposed control (as received):** "issue N95 respirators and gloves and work on the open bench."
  This is assessed against the risk-group → BSL hierarchy below.

## 2. Risk-group determination (recorded FIRST — the primary input to the BSL)

The agent's risk group is classified **before** any containment is selected (`KB-SNIP-BIOSAFETY-RA`).
*M. tuberculosis* complex is **Risk Group 3 (RG3)** (WHO LBM 4th ed.; CDC/NIH BMBL 6th ed.) — a
serious-hazard agent transmissible by the **aerosol** route. The risk group is established from the
named agent, not guessed from the procedure or the available equipment. The unlisted environmental
isolate's risk group **cannot be established from the inputs** and is therefore a **`[GAP]`** routed to
a competent biosafety officer — it is **not** assigned a risk group or a BSL (§11).

## 3. Containment gate (the lever — engineering containment before PPE)

`controls.validate_treatment` was run **before** any control was accepted. The proposed "N95 + gloves
on the open bench" is a **PPE-led treatment with no biosafety cabinet and no BSL-3 facility** for an
RG3 aerosol-transmissible agent undergoing aerosol-generating manipulation — it is a **CONTROLS FLAG**
(`ppe_admin_only=True`) **pushed up the hierarchy**. PPE (respiratory protection) is the documented
residual barrier, never the primary containment.

| Proposed / existing control | Gate outcome |
|---|---|
| "N95 respirator + gloves, open-bench working" | **FLAG — PPE substituted for engineering containment.** Pushed up the hierarchy: all aerosol-generating manipulation of RG3 cultures is performed in a **Class II biosafety cabinet within a BSL-3 facility**; the N95/respirator is a residual barrier only, not the primary control. |

## 4. Procedure & aerosol-potential assessment

The procedure **modifies the required containment**: primary culture involves aerosol-generating steps
(vortexing, centrifugation in sealed safety cups, sub-culture). A BSL selected from the agent alone,
ignoring aerosolization, would be **flagged** — the aerosol-generating manipulation of an RG3 agent
fixes the practices, the primary containment (BSC class), and the facility at **BSL-3**.

## 5. Risk-group → biosafety-level determination matrix

| Risk group (agent) | Biosafety level | Primary containment (engineering) | Facility / practices | PPE (residual) |
|---|---|---|---|---|
| RG1 (no/low individual & community risk) | BSL-1 | Open bench; good microbiological practice | Sink, cleanable surfaces; no special facility | Gloves, lab coat |
| RG2 (moderate individual, limited community) | BSL-2 | Class I/II BSC for aerosol-generating steps | Lockable, restricted access; autoclave access | Gloves, lab coat, eye protection |
| RG3 (high individual, low community — *M. tuberculosis*) | **BSL-3** | **Class II BSC for ALL manipulations; sealed centrifuge safety cups** | Directional inward airflow, double-door entry, on-site autoclave, controlled access | Respiratory protection (fit-tested), gown, gloves |
| RG3 + high-aerosol/high-volume | BSL-3 enhanced | Class II BSC + additional respiratory protection / containment | BSL-3 with enhanced practices per local risk assessment | PAPR per local assessment |
| RG4 (high individual & community, no treatment) | BSL-4 | Class III BSC **or** positive-pressure suit | Dedicated maximum-containment facility | Positive-pressure suit |
| Unlisted / unknown agent | **`[GAP]`** | **Not assigned — route to a Biological Safety Officer** | Not assigned | Not assigned |

The matrix is the core artifact: the established risk group plus the aerosol-generating procedure maps
to **BSL-3** for this work; an unestablished risk group is a `[GAP]`, never an invented BSL.

## 6. Hierarchy-ranked containment controls (engineering first → administrative → PPE last)

| Control | Tier | Owner (role) |
|---|---|---|
| All aerosol-generating manipulation performed in a **Class II biosafety cabinet**; centrifugation in **sealed safety cups** opened inside the BSC | Engineering (primary containment) | Biological Safety Officer |
| **BSL-3 facility**: directional inward airflow, double-door/anteroom entry, sealed surfaces, on-site validated autoclave for waste decontamination | Engineering (secondary containment) | Estates / Facilities Lead |
| Validated BSC (annual certification), airflow monitoring, autoclave validation, access control to the BSL-3 suite | Administrative | Laboratory Manager |
| Documented work practices, competency-based training, supervised entry, exposure-response protocol, immunisation / serological-surveillance offer | Administrative | Laboratory Manager |
| Fit-tested respiratory protection (N95/FFP3 or PAPR), gown, gloves as the **residual** barrier behind the BSC | PPE (last line) | Occupational Health |

## 7. Biosecurity, access control & exposure response

- **Biosecurity / access control:** the BSL-3 suite is access-controlled to trained, authorised staff;
  the agent inventory is logged; entry/exit is recorded.
- **Immunisation / surveillance (held confidentially):** BCG status / baseline and periodic
  occupational-health surveillance is **offered** and the record is held confidentially by Occupational
  Health, separate from this assessment.
- **Exposure-response pathway:** first aid → **confidential** incident report → occupational-health
  follow-up (risk assessment for post-exposure management). No specimen-source patient or worker is
  named in the circulated assessment.

## 8. Lab-incident & exposure context (de-identified / aggregated)

Laboratory exposures / incidents this period are reported by area, not by individual: the total is
aggregated to `≥ 5`, with categories of fewer than five suppressed and secondary suppression applied so
a suppressed cell cannot be back-calculated from totals. Individual worker surveillance results and any
serostatus are held confidentially and are never circulated.

## 9. Residual risk

After engineering containment (Class II BSC for all manipulations, sealed centrifuge cups), the BSL-3
facility, validated decontamination, competency training, and the surveillance / exposure protocol —
with respiratory protection as the last line — the residual biosafety risk is framed via `risk_matrix`
as **Low–Medium**, contingent on annual BSC certification and access-control discipline.

## 10. Duty-holders & verification (owned + dated actions)

| Action | Priority | Owner (role) | Due |
|---|---|---|---|
| Cease open-bench manipulation; route all aerosol-generating TB-culture work to the Class II BSC in the BSL-3 suite | P1 | Biological Safety Officer | 2026-07-10 |
| Verify BSC annual certification + directional-airflow monitoring + autoclave validation for the BSL-3 suite | P1 | Estates / Facilities Lead | 2026-07-31 |
| Confirm competency-based BSL-3 training + fit-testing for all assigned staff; document supervised entry | P2 | Laboratory Manager | 2026-08-31 |
| Establish the unlisted-isolate `[GAP]` referral to the BSO before any work on that agent proceeds | P1 | Biological Safety Officer | 2026-07-15 |
| Confirm the confidential immunisation / serological-surveillance offer + exposure-response pathway | P2 | Occupational Health | 2026-09-15 |

## 11. Assumptions, gaps & sign-off

- The **unlisted environmental mycobacterial isolate** has **no established risk group** from the
  inputs — recorded as a `[GAP]` routed to the Biological Safety Officer; **no risk group or BSL is
  invented** (an invented BSL is an indefensible containment decision).
- Lab-incident counts taken from the de-identified laboratory record; categories of fewer than five are
  suppressed — a missing figure is a `[GAP]`, never invented.
- India site (if applicable): state Bio-Medical Waste Rules 2016 lab-waste segregation / return owed —
  `[GAP]` (resolve the state via `hse-india`; no national form number minted).
- **Regulatory / standards basis:** CDC/NIH *Biosafety in Microbiological and Biomedical Laboratories*
  (BMBL, 6th ed., 2020) BSL-1–4 + biosafety-cabinet classes; WHO *Laboratory Biosafety Manual*
  (4th ed., 2020) risk groups RG1–RG4 + risk-assessment approach; NIH Guidelines (recombinant /
  synthetic nucleic acids — IBC pointer, where applicable); UK COSHH 2002 + ACDP hazard groups;
  OSHA 29 CFR 1910.1030 where a procedure handles human blood / OPIM; ISO 45001 §6.1.2.
- Review trigger: annual / on-change-of-agent / on-change-of-procedure / on-incident — whichever is
  first.
- Decision-support only — a competent person (a Biological Safety Officer) must review before use.
