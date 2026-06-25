# Chemicals

The **hse-chemicals** pack covers chemical hazards and major-accident-hazard (MAH) work: exposure registers, dangerous-goods transport, GHS/CLP classification and SDS authoring, India MSIHC/MAH duties, reactive-chemistry and dust-explosion assessment, tank-farm and bunding controls, and toxic-release scenario framing. It is for HSE managers, process/chemical-safety leads, and external consultants on chemical-handling, petrochemical, and process sites. Install with `/plugin install hse-chemicals@hse-leadership-skills`.

The five shared PHA / barrier tools (bow-tie, HAZID, HAZOP, LOPA, What-If) belong primarily to the Process Safety pack and appear here as cross-reference stubs — their full cards live on the [Process Safety](Process-Safety) page.

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### chemical-exposure-register
- **Produces:** An OEL/WEL/PEL-linked chemical hazard and exposure register, organised by similar-exposure group (SEG), with each exposure banded on the risk matrix and a monitoring/health-surveillance schedule.
- **For:** M · C · **Grounded in:** ISO 45001 6.1.2, occupational exposure limits (EU REACH / UK EH40 WEL / US OSHA PEL / India), KB-DATA-OEL-LIMITS · **Packs:** hse-chemicals
- **Use when:** You need to build a chemical exposure register, link agents to OELs/WELs/PELs, band inhalation/dermal exposure risk by SEG, or plan an air-monitoring / health-surveillance schedule for a named site.
- **Don't use for:** Classifying a substance or writing its SDS (use `ghs-classification-sds-author`); transport classification (use `chemical-transport-safety`).
- **Have ready:** The SEGs (not "all workers"), the agents + CAS per SEG (not "various solvents"), exposure routes, carcinogen/sensitiser flags, any monitoring data, existing controls, surveillance status, and the jurisdiction (India → the state, mandatory).
- **Trigger:** "build a chemical exposure register", "link agents to occupational exposure limits", "assess inhalation exposure risk by SEG".
- **You get:** A branded DOCX + PDF register — agents linked to their cited limit (source + year), each exposure risk-banded, controls hierarchy-of-controls ranked, and the monitoring/surveillance schedule with named owners and dates; per-worker cells below 5 are suppressed.
- **Pairs well with:** `ghs-classification-sds-author` for the underlying SDS hazard data; `risk-assessment` for the task-level HIRA.

### chemical-transport-safety
- **Produces:** Loading/unloading and transport safety guidance plus a dangerous-goods classification cross-walk for road and sea — UN number / class / packing group, placarding, marking and segregation.
- **For:** M · C · **Grounded in:** ADR (EU road, KB-REG-EU-ADR), US DOT 49 CFR HMR (KB-REG-US-DOT-HMR), IMDG (sea, KB-STD-IMDG), cross-walked from GHS (KB-STD-GHS) · **Packs:** hse-chemicals
- **Use when:** You need to classify dangerous goods for transport, cross-walk a GHS class to a transport class, work out placarding/segregation, or write loading/unloading safety guidance for a named substance and chosen mode.
- **Don't use for:** Rail (RID) or air (IATA/ICAO-TI) — out of scope for v1.0 and flagged, not guessed; classifying the substance itself (use `ghs-classification-sds-author`).
- **Have ready:** The substance/CAS + UN number (resolved from your DG list, never assumed), physical state/flashpoint, quantity per package and total consignment, the transport mode + regime (road-India CMVR → the state, mandatory), packaging, and the GHS/§14 basis.
- **Trigger:** "classify dangerous goods for transport", "cross-walk a GHS class to a transport class", "write loading/unloading safety guidance".
- **You get:** A branded DOCX + PDF with the resolved UN / class / packing group, placarding and segregation, and hierarchy-of-controls ranked loading/unloading controls; unknown UN entries flagged `[GAP]`, rail/air flagged out of scope.
- **Pairs well with:** `ghs-classification-sds-author` (which hands the §14 transport cross-walk here).

### ghs-classification-sds-author
- **Produces:** A GHS / EU CLP classification (with REACH SDS and registration duties) and a full 16-section Safety Data Sheet — hazard class + category, pictograms, signal word, H/P statements, and §8 exposure controls.
- **For:** M · C · **Grounded in:** GHS (KB-STD-GHS), EU CLP / REACH (KB-REG-EU-CLP / KB-REG-EU-REACH), US HazCom 29 CFR 1910.1200 (KB-REG-US-OSHA) · **Packs:** hse-chemicals
- **Use when:** You need to classify a named substance/mixture, author or revise an SDS, check CLP labelling, or resolve REACH SDS/registration duties for a concrete substance with stated composition and hazard data.
- **Don't use for:** Transport classification — the §14 cross-walk is handed to `chemical-transport-safety`; building an exposure register (use `chemical-exposure-register`). It is never an authoritative regulatory SDS.
- **Have ready:** Substance/mixture identity + CAS (mixtures → component composition, not "proprietary blend"), intended use, per-endpoint hazard data, jurisdiction (India → the state, mandatory), and REACH tonnage band.
- **Trigger:** "classify a chemical to GHS/CLP", "write an SDS", "work out REACH SDS / registration duties".
- **You get:** A branded DOCX + PDF SDS with the hazard class + category, pictograms, signal word, H/P statements, and a §8 controls table ranked engineering-before-PPE; absent hazard data is flagged `[GAP]` and routed to a competent person, never invented.
- **Pairs well with:** `chemical-transport-safety` for §14 transport; `chemical-exposure-register` to drive the exposure banding from the SDS data.

### india-msihc-mah-pack
- **Produces:** A Major Accident Hazard (MAH) installation-status determination under India's MSIHC Rules 1989, plus an on-site emergency plan outline and a safety-report outline, with PESO licensing pointers.
- **For:** M · C · **Grounded in:** India MSIHC Rules 1989 Schedule thresholds (KB-REG-IN-MSIHC), state forms (KB-REG-IN-STATEFORMS), PESO (KB-REG-IN-PESO) · **Packs:** hse-chemicals
- **Use when:** You need to determine MAH status under MSIHC, build an on-site emergency plan outline, outline a safety report, or resolve India chemical storage/handling statutory duties for a named India site with a hazardous-chemical inventory.
- **Don't use for:** Non-India MAH/process-safety reports (use `comah-safety-report-assistant` for COMAH/Seveso); generic chemical classification (use `ghs-classification-sds-author`).
- **Have ready:** The site + inventory + maximum quantities (not "various chemicals"), the Indian state (mandatory — confirmed before any form is cited), licences held, MAH/notification status, off-site receptors, the on-site plan status, occupier, and deadlines.
- **Trigger:** "determine MAH status under MSIHC", "build an MSIHC on-site emergency plan", "outline an India chemical safety report".
- **You get:** A branded DOCX + PDF with the MAH verdict against the Schedule thresholds, the resolved state form (never a hard-coded national form), the emergency-plan and safety-report outlines with owners and dates, and the OSH-Code transition note; unresolved thresholds/forms flagged `[GAP]`.
- **Pairs well with:** `peso-licensing-assistant` and `tank-farm-bunding-controls` for the storage-licensing and containment detail.

### reactive-dust-explosion-assessment
- **Produces:** A DSEAR-/NFPA-/ATEX-aligned basis of safety with hazardous-area zoning for reactive-chemistry, combustible-dust, and explosive-atmosphere risk.
- **For:** M · C · **Grounded in:** NFPA 652/660 DHA (KB-STD-NFPA-652/660), DSEAR / ATEX (KB-STD-DSEAR / KB-STD-ATEX), IEC 61882 for the reactive nodes · **Packs:** hse-chemicals
- **Use when:** You need to run a Dust Hazard Analysis (DHA), assess reactive chemistry/incompatibility, classify a hazardous area into ATEX zones, or set a basis of safety for a flammable atmosphere for a named process/material and area.
- **Don't use for:** Running the reactive/deflagration workshop itself — that study is handed to `hazop-facilitator`; this skill frames the nodes, it does not run the workshop.
- **Have ready:** The named process + material (not "some powder"), the hazard scope (DSEAR vs NFPA 652·660 vs ATEX), the dust-generating equipment, per-parameter characterisation data (Kst/Pmax/MIE/MIT) with lab source + year, existing safeguards, and the zoning target + adjacent connected vessels.
- **Trigger:** "run a dust hazard analysis", "classify a hazardous area into ATEX zones", "set the basis of safety for a flammable atmosphere".
- **You get:** A branded DOCX + PDF basis of safety with the DHA elements, the justified ATEX zone + EPL, consequence banded on the risk matrix, and hierarchy-of-controls ranked controls (inherently-safer/eliminate/substitute before engineering, engineering before admin/PPE); missing dust parameters flagged `[GAP]`, never invented.
- **Pairs well with:** `hazop-facilitator` (which runs the reactive/deflagration node study); `tank-farm-bunding-controls` for connected bulk storage.

### tank-farm-bunding-controls
- **Produces:** An assessment of bulk-storage / tank-farm / bunding controls — secondary containment sizing basis, segregation of incompatible substances, overfill protection, drainage and firewater containment.
- **For:** M · C · **Grounded in:** ISO 45001 6.1.2, DSEAR flammable-atmosphere area control (KB-STD-DSEAR), India PESO storage licensing (KB-REG-IN-PESO) · **Packs:** hse-chemicals
- **Use when:** You need to assess a tank farm, size a bund, plan secondary containment, or review overfill/segregation controls for bulk chemical storage with named substances, volumes and a storage configuration.
- **Don't use for:** Substance classification or SDS work (use `ghs-classification-sds-author`); the dust/reactive basis of safety (use `reactive-dust-explosion-assessment`).
- **Have ready:** Each stored substance + tank volume (not "bulk solvents"; flag the largest tank), tanks-per-bund + incompatible pairs, DG class/flashpoint, the storage configuration, existing containment, receptor proximity (watercourse/drain/boundary), the containment-sizing rule, and the jurisdiction (India → the state, mandatory).
- **Trigger:** "assess a tank farm", "size a bund / plan secondary containment", "review overfill and segregation controls".
- **You get:** A branded DOCX + PDF stating the containment basis (resolved from the rule, never an assumed %), consequence banded on the risk matrix, segregation respecting incompatibilities, hierarchy-of-controls ranked controls, and remediation actions with named owners and dates.
- **Pairs well with:** `india-msihc-mah-pack` and `peso-licensing-assistant` for the India storage-licensing pointers; `reactive-dust-explosion-assessment` for flammable-atmosphere zoning.

### toxic-release-dispersion-scenario
- **Produces:** A structured toxic-release / dispersion scenario — source term, release mode, receptors, and a qualitative consequence band — as input for a competent-person bowtie / LOPA / QRA study.
- **For:** M · C · **Grounded in:** CCPS bow-tie (KB-STD-CCPS-BOWTIE), IEC 61511 LOPA (KB-STD-IEC-61511), DSEAR (KB-STD-DSEAR) · **Packs:** hse-chemicals
- **Use when:** You need to structure a release scenario, prepare dispersion input for a study, or frame the consequence side of a bowtie/LOPA for a named substance + inventory + release scenario. It is assistive: it frames input for a competent-person study.
- **Don't use for:** Quantitative dispersion modelling — it does NOT run PHAST/ALOHA or invent distances/concentrations; running the barrier study itself (use `bowtie-builder` / `lopa-worksheet`).
- **Have ready:** The released substance + CAS + inventory at risk (not "a toxic gas"), physical state + storage P/T, the release scenario, whether a release rate is supplied or `[GAP]` for the modeller, the toxicity benchmark, the release/receptor geometry + weather, the receptors, and the target study.
- **Trigger:** "structure a toxic-release scenario", "prepare dispersion input for a study", "frame the consequence side of a bowtie".
- **You get:** A branded DOCX + PDF framing the source term, release mode, receptors and a qualitative consequence band, with every un-modelled value recorded as `[GAP]` and the consequence side explicitly handed to `bowtie-builder` / `lopa-worksheet`; never an autonomous quantitative result.
- **Pairs well with:** `bowtie-builder` and `lopa-worksheet` (which develop the consequence side); `reactive-dust-explosion-assessment` for flammable-atmosphere scenarios.

---

### bowtie-builder -> see [Process Safety](Process-Safety#bowtie-builder)
Structures major-accident barrier analysis for chemical hazards where bow-tie thinking is needed. Full card on the Process Safety page.

### hazid-facilitator -> see [Process Safety](Process-Safety#hazid-facilitator)
Facilitates structured hazard identification for chemical processes before deeper PHA methods are selected. Full card on the Process Safety page.

### hazop-facilitator -> see [Process Safety](Process-Safety#hazop-facilitator)
Facilitates guideword-based HAZOP review for chemical and process nodes. Full card on the Process Safety page.

### lopa-worksheet -> see [Process Safety](Process-Safety#lopa-worksheet)
Structures LOPA/SIL gap worksheets for chemical major-accident scenarios. Full card on the Process Safety page.

### whatif-facilitator -> see [Process Safety](Process-Safety#whatif-facilitator)
Structures What-If workshops for chemical operations where a lighter PHA method fits. Full card on the Process Safety page.
