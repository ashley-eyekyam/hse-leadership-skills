# Aviation

The **hse-aviation** pack operationalises an ICAO Annex 19 Safety Management System for a named aircraft operator, airport, or approved maintenance/training organisation — building the four-pillar SMS manual and the artifacts that sit inside it (hazard register, change assessments, SPIs/SPTs, confidential reporting, just-culture policy, SRB minutes, and FDM/FOQA-informed analysis). Install it when you run or advise an aviation SMS — operator safety managers, accountable managers, airport/AMO safety teams, and aviation HSE consultants. Where the jurisdiction is India the pack aligns to the DGCA State Safety Programme.

Install: `/plugin install hse-aviation@hse-leadership-skills`

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### aviation-change-safety-assessment
- **Produces:** An SMS management-of-change safety assessment for a named operator/airport/AMO — new and changed hazards identified, each scored on the ICAO 5×5, mitigated through the hierarchy of controls, with a recorded approve/decline rationale.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 2 (Safety Risk Management / management of change), `KB-STD-ICAO-ANNEX19` + the ICAO 5×5 Risk Classification Scheme (`KB-DATA-AVI-RISK-MATRIX`) · **Packs:** hse-aviation
- **Use when:** You are assessing the safety of a specific change for a named operator/airport/AMO — a new route, a fleet/equipment change, a procedure change, or an organisational change.
- **Don't use for:** The standing hazard log (use [aviation-hazard-register](#aviation-hazard-register)) or the whole SMS manual (use [aviation-sms-builder](#aviation-sms-builder)).
- **Have ready:** The named operator, the change type and the specific change, its effective date / trial period, the certificating authority (CAA/SSP), and the new/changed hazards the change introduces.
- **Trigger:** "assess the safety of this change", "management of change for our SMS", "approve/decline this change with a safety rationale".
- **You get:** A branded DOCX + PDF assessment — change description, new/changed hazards, initial and residual 5×5 ratings, HoC-ranked mitigations with named owners and due dates, and the recorded approve/decline decision.
- **Pairs well with:** [aviation-hazard-register](#aviation-hazard-register) (feed the new hazards into the standing register) and [aviation-sms-builder](#aviation-sms-builder).

### aviation-confidential-reporting
- **Produces:** A confidential / voluntary safety reporting system design for a named operator/airport/AMO — the intake form, the de-identification and handling workflow, the feedback loop, and the reporter-protection assurances.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 4 (Safety Promotion / confidential reporting), `KB-STD-ICAO-ANNEX19` (India → DGCA, `KB-REG-IN-DGCA`) · **Packs:** hse-aviation
- **Use when:** You need to design or review a confidential/voluntary safety reporting scheme where reporter-identity protection is the point of the artifact.
- **Don't use for:** The just-culture policy behind the scheme (use [aviation-just-culture-policy](#aviation-just-culture-policy)) or the whole SMS (use [aviation-sms-builder](#aviation-sms-builder)).
- **Have ready:** The named operator, the scheme type (confidential / voluntary / anonymous), the protection basis / jurisdiction, the MOR interface, the named custodian and re-identification-key arrangement, and the feedback-loop SLA / retention.
- **Trigger:** "design our confidential reporting scheme", "how do we protect reporter identity", "set up our hazard reporting intake and feedback loop".
- **You get:** A branded DOCX + PDF design — intake form, de-identification + handling workflow, feedback loop, and reporter-protection assurances; no reporter is named and no re-identification key is embedded.
- **Pairs well with:** [aviation-just-culture-policy](#aviation-just-culture-policy) (the promise the scheme rests on) and [aviation-sms-builder](#aviation-sms-builder).

### aviation-fdm-foqa-analysis
- **Produces:** An FDM/FOQA-informed safety analysis structured from the exceedance and event summaries you supply — findings, trends, and SMS actions, each traced to a supplied summary item.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 3 (Safety Assurance); `status: assistive` · **Packs:** hse-aviation
- **Use when:** You already have FDM/FOQA exceedance / event summaries and need them structured into findings, trends, and SMS actions for a named operator.
- **Don't use for:** Raw-data analytics — it does NOT ingest or analyse raw flight-data parameters and never invents exceedance counts or values (an absent datum is recorded as `[GAP]` and routed to the competent FDM team).
- **Have ready:** The named operator and the FDM/FOQA exceedance / event summaries already produced by your FDM team.
- **Trigger:** "structure our FOQA exceedance summary into SMS findings", "frame these flight-data-monitoring events", "turn our FDM summary into actions".
- **You get:** A branded DOCX + PDF analysis — framed findings, trends, and SMS actions reaching systemic findings, each traced to its supplied summary item with named owners and dates.
- **Pairs well with:** [aviation-spi-spt-framework](#aviation-spi-spt-framework) (trends feed SPIs) and [aviation-srb-minutes](#aviation-srb-minutes) (findings reviewed at the board).

### aviation-hazard-register
- **Produces:** An SMS hazard register for a named operator/airport/AMO — each entry running hazard → consequence → existing controls → ICAO 5×5 risk classification → HoC-ranked mitigation with a named owner and date, every entry traced to evidence.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 2 (Safety Risk Management), `KB-STD-ICAO-ANNEX19` + the ICAO 5×5 Risk Classification Scheme (`KB-DATA-AVI-RISK-MATRIX`) · **Packs:** hse-aviation
- **Use when:** You need an SMS hazard register built or maintained, or aviation hazards risk-classified on the ICAO 5×5, for a named operator/airport/AMO.
- **Don't use for:** The whole-SMS manual (use [aviation-sms-builder](#aviation-sms-builder)) or a one-off change assessment (use [aviation-change-safety-assessment](#aviation-change-safety-assessment)).
- **Have ready:** The named operator and the specific hazard(s) — with consequences and existing controls — you want logged or risk-classified.
- **Trigger:** "build our hazard register", "risk-classify this aviation hazard", "rate this on the ICAO 5×5 matrix".
- **You get:** A branded DOCX + PDF register — hazard, consequence, existing controls, 5×5 classification, and HoC-ranked mitigation with named owner and date, every entry evidence-traced and scored by the shared risk-matrix engine so two assessors score it identically.
- **Pairs well with:** [aviation-sms-builder](#aviation-sms-builder) (the register the SMS frames) and [aviation-spi-spt-framework](#aviation-spi-spt-framework) (map SPIs to owning hazards).

### aviation-just-culture-policy
- **Produces:** A just-culture policy and its decision tree for a named operator/airport/AMO — the explicit culpability / substitution-test line distinguishing honest error and at-risk behaviour from reckless or negligent conduct.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 4 (Safety Promotion), `KB-STD-ICAO-ANNEX19` · **Packs:** hse-aviation
- **Use when:** You need a just-culture policy drafted or reviewed, including the culpability decision tree between acceptable and unacceptable behaviour.
- **Don't use for:** The confidential reporting system the policy underpins (use [aviation-confidential-reporting](#aviation-confidential-reporting)) or the whole SMS (use [aviation-sms-builder](#aviation-sms-builder)).
- **Have ready:** The named operator and the policy scope; de-identification runs first so no individual is named in any worked example.
- **Trigger:** "draft our just culture policy", "build the culpability decision tree", "where is the line between error and recklessness".
- **You get:** A branded DOCX + PDF policy with an explicit decision line a reviewer can apply — never a vague "we have a just culture" statement — and a culpability decision tree.
- **Pairs well with:** [aviation-confidential-reporting](#aviation-confidential-reporting) (the scheme that depends on the promise) and [aviation-sms-builder](#aviation-sms-builder).

### aviation-sms-builder
- **Produces:** A four-pillar ICAO Annex 19 Safety Management System manual for a named aircraft operator, airport, or approved maintenance/training organisation — Safety Policy & Objectives · Safety Risk Management · Safety Assurance · Safety Promotion.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 (all four pillars), `KB-STD-ICAO-ANNEX19` (India → DGCA State Safety Programme, `KB-REG-IN-DGCA`) · **Packs:** hse-aviation
- **Use when:** You need an SMS manual built or reviewed, an SMS aligned to a State Safety Programme (DGCA SSP / FAA / EASA), or an SMS-acceptance submission structured to the four Annex 19 pillars.
- **Don't use for:** The deeper artifacts the manual frames — the hazard register, the SPI/SPT detail, the just-culture policy, or the confidential-reporting design (each is its own skill below).
- **Have ready:** The named operator, the operation type, the jurisdiction, and the named Accountable Manager and Safety Manager.
- **Trigger:** "build our SMS manual", "ICAO Annex 19 safety management system", "align our SMS to the DGCA SSP".
- **You get:** A branded DOCX + PDF SMS manual — all four pillars, named Accountable Manager and Safety Manager, operator/operation-specific content (never a generic copy-paste manual), and every risk mitigation ranked through the hierarchy of controls.
- **Pairs well with:** [aviation-hazard-register](#aviation-hazard-register), [aviation-spi-spt-framework](#aviation-spi-spt-framework), [aviation-just-culture-policy](#aviation-just-culture-policy), and [aviation-confidential-reporting](#aviation-confidential-reporting) — the artifacts the SMS frames.

### aviation-spi-spt-framework
- **Produces:** A Safety Performance Indicator (SPI) and Safety Performance Target (SPT) framework for a named operator/airport/AMO — leading and lagging SPIs, each with an alert level and a target level, every SPI mapped to an owning hazard or safety objective.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 3 (Safety Assurance), `KB-STD-ICAO-ANNEX19` (India → DGCA ALoSP, `KB-REG-IN-DGCA`) · **Packs:** hse-aviation
- **Use when:** You need an SPI/SPT framework designed or reviewed, or SPIs aligned to a State Safety Programme's acceptable-level-of-safety-performance (ALoSP).
- **Don't use for:** The whole SMS (use [aviation-sms-builder](#aviation-sms-builder)), the hazard register (use [aviation-hazard-register](#aviation-hazard-register)), or the board review of the SPIs (use [aviation-srb-minutes](#aviation-srb-minutes)).
- **Have ready:** The named operator and the hazards / safety objectives the SPIs must track; trend context comes from the shared incident-rates engine and performance figures are never invented.
- **Trigger:** "design our SPIs", "set safety performance targets", "what alert and target levels should our SPIs have".
- **You get:** A branded DOCX + PDF framework — leading and lagging SPIs, each with an alert level and a target level, every SPI mapped to its owning hazard or objective so performance is monitored against defined thresholds.
- **Pairs well with:** [aviation-hazard-register](#aviation-hazard-register) (the hazards SPIs own), [aviation-sms-builder](#aviation-sms-builder), and [aviation-srb-minutes](#aviation-srb-minutes) (where the SPIs are reviewed).

### aviation-srb-minutes
- **Produces:** Safety Review Board / Safety Action Group minutes for a named operator — agenda, SPI/SPT review, hazard and risk decisions, actions with owner and due date, and a defensible decision log where every decision carries a rationale and an accountable person.
- **For:** M · E · C · **Grounded in:** ICAO Annex 19 Pillar 3 (Safety Assurance / management review), `KB-STD-ICAO-ANNEX19` · **Packs:** hse-aviation
- **Use when:** You need SRB / SAG minutes drafted or reviewed for a named operator.
- **Don't use for:** Designing the SPIs themselves (use [aviation-spi-spt-framework](#aviation-spi-spt-framework)) or the hazard register (use [aviation-hazard-register](#aviation-hazard-register)).
- **Have ready:** The named operator and the meeting agenda; attendees appear as role labels (chair = Accountable Manager) and de-identification runs first so no reporter named in a hazard item is identified.
- **Trigger:** "minute our Safety Review Board", "Safety Action Group minutes", "build the SRB decision log".
- **You get:** A branded DOCX + PDF minutes set — agenda, SPI/SPT review, hazard and risk decisions, an actions table with owner and due date, and a defensible decision log; ships an attendance / decision table with empty rows for the meeting to fill.
- **Pairs well with:** [aviation-spi-spt-framework](#aviation-spi-spt-framework) (the SPIs reviewed) and [aviation-hazard-register](#aviation-hazard-register).
