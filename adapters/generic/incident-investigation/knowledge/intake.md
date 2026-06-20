---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-LOCATION, ELI-EXPOSURE,
           ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY, ELI-TEMPORAL]
  omits:
    ELI-INDUSTRY: "Inferable from Q1/Q2; not load-bearing for the RCA method or the reportability verdict."
    ELI-BASELINE: "An investigation analyses failed/absent barriers as an RCA output (Q6/Q7), not a pre-existing controls baseline."
  branches:
    - {when: Q8, activates_output_section: rca-method-subprompt, mandatory: false}  # ICAM→organisational-factor evidence; SCAT→management-system context; Fishbone→non-Man branches; Swiss-Cheese→failed barrier per layer
    - {when: Q9, option: India, activates_questions: [Q9a], activates_kb_row: KB-REG-IN-STATEFORMS, activates_output_section: state-accident-notice, mandatory: true}
    - {when: Q3, option: injury, activates_questions: [Q10], mandatory: false}
    - {when: Q3, option: illness, activates_questions: [Q10], mandatory: false}
---

# Structured intake — incident-investigation

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. Never
proceed on vague inputs; record `[GAP]` for missing evidence and `[ASSUMPTION]` for
anything inferred — **never invent evidence or causes**.

**De-id sequencing is load-bearing.** Q5 (people involved) is **flagged for IMMEDIATE
de-identification** — it is scrubbed in Workflow step 2 *before* any analysis, so the
echo-back shows **role labels only** ("Worker A", witness "W-1"), never raw names. Q2
(when & where) carries exact-date / precise-location quasi-identifiers and is scrubbed
the same way. The scrub runs *before* the echo-back.

Two load-bearing branches: the **four RCA-method sub-prompts** (Q8 = ICAM → organisational-
factor evidence; SCAT → management-system context; Fishbone → the non-"Man" branches;
Swiss-Cheese → the failed barrier at each layer) and the **mandatory India→state branch**
(Q9 = India → Q9a + `KB-REG-IN-STATEFORMS` + the state-accident-notice section; confirm the
state before citing any form — never a national form number). The optional contextual-rate
branch (Q10) is asked only when Q3 ∈ {injury, illness}.

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **What happened?** (the core narrative — the sequence of events) | free-text | The investigation's seed; the factual account, not conclusions. | ELI-SUBJECT | always |
| Q2 | **When and where?** (date, time, location/asset) | free-text | Flagged for de-id (exact date + precise location are quasi-identifiers). | ELI-LOCATION / ELI-TEMPORAL | always |
| Q3 | **Incident type / classification** | MCQ | injury / illness / near-miss / property damage / environmental release / dangerous occurrence — branches the reporting logic + the rate context (Q10). | ELI-SCOPE | always |
| Q4 | **Severity / outcome** | MCQ | fatality / lost-time injury / medical-treatment / first-aid / no-injury near-miss / property-only / environmental-only — drives reportability urgency + the RCA-method suggestion. | ELI-SCOPE | always |
| Q5 | **People involved** | free-text | **Flagged for IMMEDIATE de-identification** — names, roles, witnesses captured here are pseudonymized in step 2 before any analysis; the intake echoes them back as role labels ("Worker A", witness "W-1"). | ELI-EXPOSURE | always |
| Q6 | **Immediate / obvious causes** (what visibly went wrong) | free-text | The *starting point* for RCA, never the endpoint — the skill drives past these to systemic factors. | ELI-SUBJECT | always |
| Q7 | **Evidence available** | free-text | statements, photos, logs, readings, maintenance records, procedures → becomes the numbered evidence log; `[GAP]` recorded for anything missing. | ELI-EVIDENCE | always |
| Q7b | **Permits / procedures in force at the time** | free-text | "Any PTW, isolation, or procedure that was supposed to be in force for this task at the time? (informs causation, not blame)" — optional. | ELI-OBLIGATIONS | always |
| Q8 | **RCA method preference** | MCQ | **Five A7-validated options, each with a one-line "when to pick":** **5-Whys** — quick single causal chain; minor events. **ICAM** — systems-based, organisational focus; serious/high-potential events. **SCAT** — Loss-Causation model linking to management-system control failures. **Fishbone (Ishikawa)** — categorise causes across Man/Machine/Method/Material/Measurement/Environment when factors span domains. **Swiss-Cheese (Reason)** — trace failed/absent defence layers to latent organisational influences; barrier/defence-in-depth events. *Branch:* ICAM → prompt for organisational-factor evidence; SCAT → management-system context; Fishbone → evidence across the non-Man branches; Swiss-Cheese → the failed barrier at each layer. | ELI-SCORING | always |
| Q9 | **Jurisdiction** | MCQ | India / UK / USA / EU / Other-or-Unknown. **India → ask the STATE** (Q9a, mandatory) → triggers `KB-REG-IN-STATEFORMS`; Unknown → the reporting step defers to "ask before citing." | ELI-JURIS | always |
| Q9a | *(India only)* **Which state?** | MCQ | Tamil Nadu / Karnataka / Maharashtra / Delhi-Central / Gujarat / Other — **mandatory state detection; confirm the state before citing any accident form** (never a national form number; an un-seeded state → `[GAP]`). | ELI-JURIS | Q9 == India |
| Q9b | **Investigation team / investigator** | free-text | "Who is conducting this investigation (role/competence)? Who will own the corrective actions? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q10 | *(optional; branch on type = injury/illness)* **Period exposure hours + recordable counts** | free-text | Only if the user wants the contextual rate; otherwise **skipped** — `incident_rates` is omitted rather than fabricating a denominator. | ELI-SCORING | Q3 == injury / illness |

**Branch map:** four RCA-method sub-prompts (`rca-icam` / `rca-scat` / `rca-fishbone` /
`rca-swisscheese` — each activating its method-specific evidence section, non-mandatory);
`india-state` (Q9 = India → Q9a + `KB-REG-IN-STATEFORMS` + state-accident-notice;
**mandatory**); `rate-context` (Q3 ∈ {injury, illness} → Q10; non-mandatory). A severe
outcome (Q4 ∈ {fatality, LTI, dangerous occurrence} or Q3 = environmental release) opens
the reportability clock at the reporting step.

## Echo-back

After the last applicable question — and **after** the step-2 de-id scrub — **echo the
captured, de-identified facts back** and proceed only on confirmation. The template shows
**role labels only** (the scrub has already run):
"A lost-time injury to Worker A on [date], at [location], witnessed by W-1; evidence
E-1…E-4; method ICAM; jurisdiction India/Maharashtra; reportable on the state accident
form within the statutory window — confirm before I analyse?"

## Refuse-on-vague anchors

- Never proceed on vague inputs: record `[GAP]` for missing evidence and `[ASSUMPTION]`
  for anything inferred; **never invent evidence or causes**.
- **De-id sequencing is the load-bearing anchor** — the Q5 scrub runs *before* echo-back,
  so the echoed facts are de-identified role labels, never raw names. No name, exact date,
  precise location, or `<5` injury cell ever reaches the analysis or the echo.

## Domain evidence types (ELI-EVIDENCE)

Witness statements · photos · plant/process logs and readings · maintenance records · the
procedure/PTW that should have applied · CCTV/access logs · prior incidents on the same
equipment/task · for the optional rate context: period hours + recordable counts.
