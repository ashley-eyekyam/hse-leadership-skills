# Methodology — infection-control-plan (engineering/administrative-controls-before-PPE, PHI-protected)

The domain method `infection-control-plan` applies. Its spine is **Standard Precautions for every
patient, then the route-correct Transmission-Based precautions, with engineering and administrative
controls before PPE** (`KB-STD-IPC-CDC-WHO` + `KB-SNIP-IPC-PRECAUTIONS` + `KB-SNIP-HOC`): identify the
transmission route(s), apply engineering controls (ventilation, negative-pressure / airborne-infection
isolation rooms, single rooms, safer devices), then administrative controls (cohorting, screening,
signage, restricted entry), with **PPE as the residual barrier last**. An IPC treatment that **leads
with PPE — an airborne agent managed by a respirator alone with no isolation room or ventilation** — is
a **FLAG pushed up the hierarchy, never the headline control**. There is **no calculation** —
transmission-based IPC is a structured route-driven precaution-selection method over the named unit +
agents + the cited CDC/WHO/Spaulding frameworks.

## 0. De-identify first (the highest-PHI step — patient infection status + outbreak detail)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Healthcare infection data
is **special-category health data (PHI)**. Scrub any **patient's infection / colonisation status**
(never attributed to a named person in a circulated plan — the patient is referenced by role / cohort
only, and any status that must be recorded is held in a separate confidential clinical record), any
**outbreak / cluster detail** (reported de-identified and aggregated), and any patient/staff
identifier. Apply `<5` small-cell suppression (with secondary suppression) to every case / cluster
category — **a 3-case cluster on a named ward re-identifies patients** (the small-cell
back-calculation). **The skill emits NO re-identification key file** (documented-procedure model — the
key is an instruction to the competent person, held separately, access-controlled), and adds **no new
report field** (the de-identified banner is the existing report `meta.deid_notice` header). The
De-identifier subagent runs FIRST; everything downstream consumes only its scrubbed output.

## 1. Scope the named service & unit (Q1)

- **Named service & unit (Q1)** — the exact unit/service (ward, clinic, care home, dental surgery,
  ambulance, lab). **Refuse "a hospital" / "the ward"** (the specificity anchor). A missing service is
  a `[GAP]`, never invented.

## 2. Identify the agent(s) and transmission route(s) (Q2) — the routing anchor

The route drives the precautions. Apply **Standard Precautions to every patient**, then identify the
**transmission route(s)** — contact, droplet, airborne, or a combination — for the suspected/confirmed
agent(s). An unknown route is a `[GAP]`, resolved before precautions are selected.

## 3. Engineering controls first, then administrative — before PPE (the hierarchy gate, the spine)

Asked and applied **before** PPE because engineering and administrative controls are the primary
controls, not the respirator:

- **Engineering controls (Q3)** — ventilation, **negative-pressure / airborne-infection isolation
  room (AIIR)** for the airborne route, single rooms for contact/droplet, safer devices. **An airborne
  agent with no AIIR or ventilation provision controlled by a respirator alone is FLAGGED** and pushed
  up the hierarchy.
- **Administrative controls (Q4)** — cohorting, early screening / triage, isolation signage, restricted
  entry, the hand-hygiene programme + audit. These precede PPE.
- **PPE last** — route-appropriate residual PPE (gown+gloves for contact; surgical mask for droplet;
  fit-tested respirator for airborne) is the residual barrier, never the headline control.

## 4. Layer the Transmission-Based precautions by route (Q2 → precautions)

Layer the per-route precaution set (`KB-SNIP-IPC-PRECAUTIONS`): **contact** — single room / cohorting,
gown+gloves, dedicated equipment; **droplet** — single room / spatial separation, surgical mask within
range, respiratory etiquette; **airborne** — AIIR (negative pressure), fit-tested respirator, restricted
entry. A plan that jumps to PPE without the room/ventilation control the route requires is rejected.

## 5. Spaulding reprocessing decision (Q5)

Record the **Spaulding classification** per device class (`KB-STD-IPC-CDC-WHO`): **critical** (contacts
sterile tissue / the bloodstream) → **sterilization**; **semi-critical** (contacts mucous membranes /
non-intact skin) → **high-level disinfection** (sterilization where feasible); **non-critical**
(contacts intact skin) → **low-level disinfection**. **High-level disinfection of a critical device is
a Spaulding mis-application and fails.**

## 6. WHO IPC programme structure + de-identified surveillance

Structure the **WHO IPC programme** against the core components (programme + team, guidelines,
education/training, surveillance, multimodal strategy, monitoring/audit + feedback, workload/staffing/
bed-occupancy, built environment). Build the **de-identified / aggregated surveillance** (HAI /
outbreak / cluster) — never line-level — and apply `<5` small-cell suppression with the secondary
back-calculation guard to every category (by ward, organism, unit, or period). **No outbreak is
reported on a named ward in a way that re-identifies a patient.**

## 7. Rank the controls + the residual + SMART actions + report

Run the `controls` engine. The control narrative **always leads with engineering controls**
(ventilation, AIIR / negative pressure, single rooms) → **administrative** (cohorting, screening,
signage, hand-hygiene audit) → **PPE last**. A treatment that **leads with PPE — a respirator-alone
airborne plan with no isolation room or ventilation** (`controls.validate_treatment` returning
`ppe_admin_only=True`) is a **FLAG pushed up the hierarchy, never the headline control**. Frame the
qualitative residual transmission risk via `risk_matrix`. Every engineering / cohorting / reprocessing
/ surveillance action becomes a SMART action (named role owner + ISO due date + measure), validated by
`smart_actions.validate_register`. Validate the draft against `references/QUALITY_CHECKLIST.md`, then
assemble `assets/infection-control-plan.report.json` and run the canonical `report-output` call.

## Jurisdiction

The default frameworks are the **CDC Guideline for Isolation Precautions** (Standard +
Transmission-Based), the **WHO Core Components of IPC Programmes**, and the **Spaulding classification**
(`KB-STD-IPC-CDC-WHO`). UK grounds in the **Health and Social Care Act 2008 Code of Practice** (the
Hygiene Code); US exposure / health-data confidentiality grounds in the **OSHA bloodborne-pathogens**
standard ((f) confidential follow-up) via `KB-REG-OSHA-BBP`. For India, resolve the state via
`hse-india` (**mandatory state detection**) per the **Bio-Medical Waste Management Rules 2016**
segregation, and emit a literal `[GAP]` where a state return is owed — **never a minted national form
number**.
