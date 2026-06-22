<!-- KB-SNIP-IPC-PRECAUTIONS -->
# IPC precautions — Standard + Transmission-Based precautions by route

**Fragment ID:** `KB-SNIP-IPC-PRECAUTIONS`
**This is prompt text, applied by the model — not a generator.** It is the
per-route precaution-selection logic for infection prevention and control in
`hse-healthcare`: apply **Standard Precautions to every patient**, then layer the
**Transmission-Based precautions for the route(s)** the agent uses — with
engineering and administrative controls applied before PPE.

> Source: CDC Guideline for Isolation Precautions (Standard + Transmission-Based) + the hierarchy of controls (`KB-SNIP-HOC`) — selection prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the precaution-selection order

1. **Standard Precautions (always).** Hand hygiene, PPE selected by anticipated
   exposure, respiratory hygiene/cough etiquette, safe injection practice, sharps
   safety, and environmental cleaning — for every patient regardless of diagnosis.
2. **Identify the transmission route(s).** Contact, droplet, airborne (or a
   combination) for the suspected/confirmed agent.
3. **Layer Transmission-Based precautions by route:**
   - **Contact** — single room / cohorting, gown + gloves, dedicated equipment.
   - **Droplet** — single room / spatial separation, surgical mask within range,
     respiratory etiquette.
   - **Airborne** — airborne-infection isolation room (negative pressure), fit-tested
     respirator, restricted entry.
4. **Apply the hierarchy of controls.** Engineering (ventilation, single rooms,
   negative pressure) and administrative controls (cohorting, screening, signage)
   come **before** relying on PPE; PPE is the residual barrier.

## The gate (reject these)
- A plan that jumps to PPE without the engineering/administrative controls the route
  requires (e.g. droplet/airborne with no room/ventilation control) → **reject**.
- An airborne agent managed without an AIIR/respirator where required → **reject**.
- Reporting a case cluster in a way that allows re-identification → **reject** (apply
  small-cell suppression).

## How the skill uses this fragment
`infection-control-plan` (HC-02) selects precautions by route here, grounded on the
WHO IPC core components and Spaulding reprocessing (`KB-STD-IPC-CDC-WHO`). No skill
restates the logic in its own body (anti-drift).
