# Methodology — lab-biosafety-assessment (risk-group → BSL, engineering-containment-first, PHI-protected)

The domain method `lab-biosafety-assessment` applies. Its spine is **classify the agent's risk group
first, then match it to the biosafety level with engineering containment before PPE**
(`KB-SNIP-BIOSAFETY-RA` + `KB-STD-BIOSAFETY-BMBL-WHO` + `KB-SNIP-HOC`): determine the **risk group
(RG1–RG4)**, combine it with the **procedure** and **competence**, select the **biosafety level
(BSL-1–BSL-4)**, then the **primary containment** (biosafety-cabinet class, directional airflow, waste
decontamination), with **PPE as the documented residual barrier**. A treatment that **substitutes
gloves/respirator for a biosafety cabinet or the BSL-appropriate facility** is a **FLAG pushed up the
hierarchy, never the headline control**. There is **no calculation** — the biosafety assessment is a
structured determination over the named agent + procedure + the cited BMBL / WHO LBM classification.
**Where the agent's risk group cannot be established, emit `[GAP]` and route to a competent biosafety
officer — never invent a risk group or BSL.**

## 0. De-identify first (the highest-PHI step — specimen-source patient + worker)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Laboratory biosafety
inputs are **special-category health data (PHI)**. Scrub the **specimen-source / index patient's
identity** (never circulated; referenced by role only, any clinical / serostatus detail held in a
separate confidential record), the **worker's identity, job, and serological-surveillance /
occupational-health record** (role-label "Worker A"; the OH record held confidentially + separately
per OSHA 1910.1030(f) / GDPR Art. 9), and any **patient identifier**. Apply `<5` small-cell
suppression (with secondary suppression) to every lab-incident / exposure category. **The skill emits
NO re-identification key file** — the key is an instruction to the competent person (held separately,
access-controlled). The De-identifier subagent runs FIRST; everything downstream consumes only its
scrubbed output.

## 1. Scope the named lab & the agent / material (Q1)

- **Named lab & agent / material (Q1)** — the exact laboratory (clinical-diagnostic, research,
  teaching, public-health) **and the specific biological agent or material** (the organism / sample
  type, recombinant material, human blood / OPIM). **Refuse "a lab"** (the specificity anchor). A
  missing lab or agent is a `[GAP]`, never invented.

## 2. Determine the agent's risk group — the FIRST determination step (the spine)

This question is asked **first among the determination** because the risk group is the **primary
input to the BSL**, not the cabinet or the PPE:

- **Q2 = RG1–RG4** → the established risk group drives the biosafety-level decision (combined with the
  procedure, Q3).
- **Q2 = Unknown / unlisted agent** → **emit a literal `[GAP]` and route to a competent biosafety
  officer**. The skill **never invents a risk group or assigns a BSL from a guessed risk group** — an
  invented classification is an indefensible containment decision (`KB-SNIP-BIOSAFETY-RA` rejects a
  BSL selected from a guessed risk group).

## 3. Assess the procedure & aerosol potential (Q3)

Assess the steps performed: **aerosol-generating activities** (centrifugation, sonication, vortexing,
pipetting), sharps, volumes, and concentrations. **The procedure modifies the required containment —
a BSL selected from the agent alone, ignoring aerosolization, is FLAGGED.** The aerosol potential
drives the biosafety-cabinet selection in Step 5.

## 4. Select the biosafety level (BSL-1–BSL-4) (the determination)

Map the established **risk group + the procedure** to the **biosafety level** — the containment
practices, facilities, and safety equipment per BMBL (`KB-STD-BIOSAFETY-BMBL-WHO`). Record the
risk-group → BSL determination explicitly (the agent's risk group, the procedure, and the resulting
BSL), so the containment decision is traceable. Where the inputs do not support a determination, the
result is a `[GAP]`, never an invented BSL.

## 5. Primary containment — engineering first (Q4) — BSC class before PPE

Select the **primary containment (engineering controls first)**: the **biosafety-cabinet class**
(I / II A–B / III — matched to the aerosol potential and the agent), **directional airflow /
ventilation**, **waste decontamination** (autoclave), and the BSL facility features. **A containment
plan that relies on PPE without the biosafety cabinet / ventilation the level requires is REJECTED
(PPE-led)** — PPE (gloves, gowns, respiratory protection) is the **residual barrier matched to the
BSL**, never the headline control.

## 6. Biosecurity, immunisation / surveillance, and the confidential exposure-response pathway (Q5)

Author the **biosecurity / access-control** measures (restricted access, inventory / accountability
for the agents that warrant it), the **immunisation / serological-surveillance offer** (held
confidentially), and the **confidential exposure-response pathway**: immediate first aid →
**confidential** incident report → occupational-health follow-up. **No specimen-source patient or
worker is named in the circulated assessment**; the serological-surveillance / OH record is held
confidentially and separately.

## 7. Rank the controls (the hierarchy gate) + the residual + SMART actions + report

Run the `controls` engine. The control narrative **always leads with engineering containment** (the
biosafety cabinet + ventilation + decontamination for the determined BSL) → administrative (the
biosafety procedures, training, surveillance) → **PPE LAST**. A treatment that **substitutes
gloves/respirator for a biosafety cabinet or the BSL facility** (`controls.validate_treatment`
returning `ppe_admin_only=True`) is a **FLAG pushed up the hierarchy, never the headline control**.
Frame the qualitative residual biosafety risk via `risk_matrix`. Every containment / training /
surveillance / decontamination action becomes a SMART action (named role owner + ISO due date +
measure), validated by `smart_actions.validate_register`. Validate the draft against
`references/QUALITY_CHECKLIST.md`, then assemble `assets/lab-biosafety-assessment.report.json` and run
the canonical `report-output` call.

## Jurisdiction

The **CDC/NIH BMBL 6th ed (2020)** biosafety levels + the **WHO Laboratory Biosafety Manual 4th ed
(2020)** risk groups (`KB-STD-BIOSAFETY-BMBL-WHO`) ground the determination everywhere; the
**NIH Guidelines** (IBC) apply to recombinant / synthetic nucleic-acid work. For US procedures
handling **human blood / OPIM**, also ground in **OSHA 29 CFR 1910.1030** (`KB-REG-OSHA-BBP` — (c) ECP
/ (d)(2) engineering & work-practice controls / (f) confidential follow-up + HBV vaccination); for the
**EU/UK**, **COSHH 2002** with the **ACDP hazard groups** is the binding duty. For India, resolve the
state via `hse-india` (**mandatory state detection**) per the **Bio-Medical Waste Management Rules
2016** lab-waste segregation, and emit a literal `[GAP]` where a state return is owed — **never a
minted national form number**.
