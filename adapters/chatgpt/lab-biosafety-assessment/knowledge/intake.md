---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-OBLIGATIONS, ELI-EVIDENCE, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-BASELINE: "A biosafety assessment determines the containment afresh from the named agent + procedure; there is no prior-baseline measurement to diff against (unlike a noise or exposure survey), so a dedicated baseline question is not asked — the agent's risk group (Q2) and the procedure / containment state (Q3/Q4) are the assessment's starting facts."
    ELI-SCORING: "Biosafety containment is a structured risk-group -> BSL determination, not a calculated score; the residual biosafety risk is framed qualitatively via risk_matrix after controls, so a scoring-scale question is not asked of the user."
  branches:
    - {when: Q2, option: "Unknown", activates_questions: [], activates_kb_row: KB-SNIP-BIOSAFETY-RA, mandatory: true}
    - {when: Q6, option: India, activates_questions: [Q6a], activates_kb_row: KB-REG-IN-BMW2016, mandatory: true}
---

# Structured intake — lab-biosafety-assessment

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where the
answer space is enumerable and free-text where it is open; branch on the answers; **echo the captured
facts back for confirmation before any analysis**. The intake opens with the **named lab & agent /
material (Q1 — the specificity anchor)**, then — **first among the determination** — the **agent's
risk group (Q2)** (RG1–RG4; **Unknown → `[GAP]`, never invent**), the **procedure & aerosol potential
(Q3)**, the **primary containment & facility (Q4)**, the **staff competence & exposure response
(Q5)**, and the **jurisdiction (Q6)**. **Refuse to assess "a lab": you need the named laboratory + the
specific agent (Q1) and the agent's risk group (Q2) before any containment decision. Refuse a
behaviour/PPE-led "wear a respirator and gloves" treatment where a biosafety cabinet or the BSL
facility is required.** The biosafety determination is a structured risk-group → BSL method — never a
calculation — and a missing input is a `[GAP]`, never an invented agent, risk group, or BSL.

**De-identify FIRST** — laboratory biosafety inputs are special-category health data (PHI). Before
the echo-back drives any analysis, scrub the specimen-source patient's identity, the worker's
identity + serological-surveillance / OH record, and apply `<5` small-cell suppression to every
lab-incident / exposure category (`references/deid-checklist.md`).

Two load-bearing branches: the **unknown-risk-group branch** (Q2 = Unknown → emit `[GAP]` and route
to a competent biosafety officer; **never invent the risk group or BSL**; mandatory) and the
**mandatory India→state branch** (Q6 = India → Q6a + `hse-india`; BMW Rules 2016 lab-waste
segregation; confirm the state before citing any rule — never a national form number, emit `[GAP]`
where a state return is owed).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **The named lab & agent / material** (clinical-diagnostic / research / teaching / public-health lab + the specific agent or material) | free-text | "Name the exact laboratory + the specific biological agent or material handled (the organism / sample type, recombinant material, human blood / OPIM). **Refuse 'a lab' — the assessment is lab- and agent-specific; this is the specificity anchor.**" | ELI-SUBJECT | always |
| Q2 | **The agent's risk group (RG1–RG4)** (asked FIRST among the determination — the risk group is the primary input to the BSL) | mcq | RG1 / RG2 / RG3 / RG4 / Unknown / **Unknown → `[GAP]` — never invent a risk group or BSL** | ELI-SCOPE | always |
| Q3 | **The procedure & aerosol potential** | free-text | "The steps performed, **aerosol-generating activities** (centrifugation, sonication, vortexing, pipetting), sharps, volumes, concentrations. **A BSL selected from the agent alone, ignoring aerosolization, is FLAGGED** — the procedure modifies the required containment." | ELI-OBLIGATIONS | always |
| Q4 | **Primary containment & facility** | mcq+free-text | biosafety-cabinet **class** (I / II A–B / III) · directional airflow / ventilation · waste decontamination (autoclave) · the BSL facility features — **a plan relying on PPE without the BSC / ventilation the level requires fails (PPE-led)** | ELI-EXPOSURE | always |
| Q5 | **Staff competence & exposure response** | free-text | "Staff training / competence, the immunisation / serological-surveillance offer (held confidentially), and the exposure pathway: first aid → **confidential** incident report → occupational-health follow-up. **Refuse to draft a pathway that names a specimen-source patient or worker in the circulated assessment.**" | ELI-EVIDENCE | always |
| Q6 | **Jurisdiction** | mcq | USA (OSHA 1910.1030 where human blood/OPIM) / EU-UK (COSHH 2002 + ACDP) / India / Other / Unknown | ELI-JURIS | always |
| Q6a | *(India only)* Which state? | mcq | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Other — **mandatory state detection; BMW Rules 2016 lab-waste segregation; defer to `hse-india`, confirm the state before citing any rule; emit `[GAP]`, never a national form number** | ELI-JURIS | Q6 == India |
| Q7 | Industry / lab setting | mcq+free-text | Clinical-diagnostic / Research / Teaching / Public-health-reference / Industrial-QC / General-Other (+ detail) | ELI-INDUSTRY | always |
| Q8 | Location / site / area | free-text | "Which specific site / building / room is the laboratory in?" | ELI-LOCATION | always |
| Q9 | Output artifact wanted + its reader | mcq | full biosafety risk assessment + containment plan (consultant) / risk-group + BSL determination summary (manager) / quick containment / cabinet-class answer (frontline) | ELI-OUTPUT | always |
| Q10 | **Action owner(s) + verifier** | free-text | "Who owns the containment / training / surveillance / decontamination actions and who is the competent person (a Biological Safety Officer) verifying the assessment (named role — no 'TBD')?" | ELI-COMPETENCY | always |
| Q11 | **Review cycle / next review** | mcq+free-text | annual / on-agent-change / on-procedure-change / on-incident / other (+date) | ELI-TEMPORAL | always |

**Branch map:** `unknown-risk-group` (Q2 = Unknown → emit `[GAP]`, route to a competent biosafety
officer; **mandatory** — never invent the risk group / BSL); `india-state` (Q6 = India → Q6a +
`hse-india`; **mandatory**).

## Echo-back

After the last applicable question (Q11, and Q6a if its branch ran), **echo a captured-facts
summary** and confirm before any analysis:
"Building a biosafety risk assessment for: the diagnostic mycobacteriology lab, Block-C Room 12,
Maharashtra; agent — *M. tuberculosis* (risk group RG3); procedure — primary culture with
aerosol-generating manipulation; primary containment — Class II A2 biosafety cabinet + directional
airflow + autoclave; BSL-3 facility; serological-surveillance offered and held confidentially; full
assessment; review annually — correct?" The biosafety determination is a structured risk-group → BSL
method, never a calculation; the specimen-source patient and the worker are referenced by role only.

## Refuse-on-vague anchors

- **Q1 is the specificity anchor** — refuse "a lab"; ask again or record `[GAP]`, never invent the
  laboratory or its agent.
- **Risk-group first, never invented** — an **unknown / unlisted agent risk group is a `[GAP]`**
  routed to a competent biosafety officer; the skill **never invents a risk group or a BSL** (an
  invented BSL is an indefensible containment decision).
- **Engineering containment first, PPE last** — a behaviour/PPE-led treatment ("wear a respirator
  and gloves") with no biosafety cabinet or BSL-appropriate facility is **refused and pushed up the
  hierarchy**; PPE substituted for engineering containment is never the primary control. A BSL
  selected from the agent alone, ignoring aerosolization, is flagged.
- **PHI gate** — the skill **never** writes a specimen-source-patient identity, a worker's name, a
  surveillance / serostatus result, or a sub-five lab-incident count into the circulated artifact;
  the re-identification key is held separately, never co-located and never emitted as a key file.
  **Never proceed on a vague input.**

## Domain evidence types (ELI-EVIDENCE)

The agent's risk-group determination (Q2 — `[GAP]` where unknown) · the procedure / aerosol-potential
assessment (Q3) · the selected biosafety level + the primary containment (Q4 — biosafety-cabinet
class, ventilation, decontamination) · the staff competence + the immunisation / serological-
surveillance offer + the confidential exposure-response pathway (Q5) · the biosecurity / access-
control measures · the de-identified / aggregated lab-incident / exposure summary · a prior
lab-acquired-infection / exposure referenced for context (de-identified to role level — the
specimen-source patient and the worker's surveillance record are highest-sensitivity PHI).
