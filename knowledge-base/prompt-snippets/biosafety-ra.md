<!-- KB-SNIP-BIOSAFETY-RA -->
# Biosafety risk assessment — risk group → biosafety level containment gate

**Fragment ID:** `KB-SNIP-BIOSAFETY-RA`
**This is prompt text, applied by the model — not a generator.** It is the
biosafety risk-assessment gate for `hse-healthcare`: determine the agent's **risk
group (RG1–RG4)**, combine it with the procedure and competence, and select the
**biosafety level (BSL-1–BSL-4)** and primary containment (BSC class) — applying
engineering and procedural controls before PPE. Where the agent's risk group is
unknown, **do not invent it** — emit `[GAP]` and route to a competent biosafety
officer.

> Source: WHO Laboratory Biosafety Manual risk assessment + CDC/NIH BMBL biosafety levels + the hierarchy of controls (`KB-SNIP-HOC`) — assessment gate prompt · Year: 2026 · Reviewed: 2026-06-23 · Volatile: false.

---

## Instruction — the risk-group → BSL containment order

1. **Classify the agent's risk group.** RG1 (unlikely to cause disease) → RG4
   (severe disease, high transmissibility, no effective treatment). If the agent's
   risk group is not established, emit `[GAP]` — never assume.
2. **Assess the procedure.** Aerosol-generating steps, sharps, volumes,
   concentrations, and the competence of staff modify the required containment.
3. **Select the biosafety level.** Map risk group + procedure to BSL-1–BSL-4
   containment practices, facilities, and safety equipment.
4. **Select primary containment (engineering first).** Biosafety cabinet by class
   (I / II / III), ventilation/directional airflow, and waste decontamination —
   before relying on PPE.
5. **PPE (residual).** Gloves, gowns, respiratory protection as the residual barrier
   matched to the BSL — never as the headline control.

## The gate (reject these)
- A BSL selected from a guessed risk group rather than an established one →
  **reject**; emit `[GAP]`.
- A containment plan that relies on PPE without the BSC/ventilation the level
  requires → **reject** (PPE-led).
- Reporting an exposure in a way that allows re-identification of staff → **reject**
  (apply small-cell suppression).

## How the skill uses this fragment
`lab-biosafety-assessment` (HC-05) runs this gate, grounded on the BMBL/WHO
structure (`KB-STD-BIOSAFETY-BMBL-WHO`) and the bloodborne-pathogen duties
(`KB-REG-OSHA-BBP`). No skill restates the gate in its own body (anti-drift).
