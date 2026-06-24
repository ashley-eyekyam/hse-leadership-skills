---
sme-review:
  personas:
    - role: "Occupational Hygienist / Audiometric Technician / OH Physician"
      expertise: "Occupational-noise exposure assessment (ISO 9612 measurement, ISO 1999 NIHL estimation), action-level / exposure-limit comparison (OSHA 1910.95 85/90 dBA; UK Control of Noise at Work Regs 2005 80/85/87 dB(A)), exposure-zone mapping, engineering noise control vs hearing protection, hearing-conservation-program design, audiometric surveillance regimes (baseline / annual / standard-threshold-shift triggers), and special-category audiometric-health-data confidentiality."
      lens: "Is each area/SEG named and specific, is every exposure compared to a CITED action level / limit (authority+year) and TRANSCRIBED not computed, are noise-reduction controls driven up the hierarchy ABOVE hearing protection, is the audiometry schedule action-level-linked — and is there ZERO special-category audiometric-health leak (no named STS result, no <5 audiometric cell)?"
---

# SME Review & Sign-off — noise-exposure-health-surveillance

This skill carries **one** SME lens, specializing the generic **HSE-SME-Reviewer** runtime hook
(`KB-SNIP-ARCHETYPES`) into an **Occupational Hygienist / Audiometric Technician / OH
Physician**. The universal hard gates (de-id leak, citation accuracy, HoC / no-hearing-
protection-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **Areas / SEGs are specific** — each names the area/process and the roles exposed; a generic area ("the factory") or SEG ("all staff") is a FLAG.
- [ ] **Every exposure is compared to a CITED action level / limit** — measured/estimated dB(A) vs the binding action value / PEL with authority+year (OSHA 1910.95 85/90 dBA; Noise Regs 2005 80/85/87 dB(A)); an exposure with no cited threshold, or a fabricated dB figure, is a FLAG. No data → a measurement strategy is recommended, not a fabricated comparison.
- [ ] **Exposure is TRANSCRIBED, not computed** — the skill does not run a dosimetry calculation; a narrated "calculated 89 dBA" with no measured/estimated source value is a FLAG.
- [ ] **Controls beat the noise, above hearing protection** — source/engineering precede HPD; a plan whose only control for ≥ 85 dBA is "issue ear defenders" (no source/engineering assessment) is a FLAG. Hearing protection is the LAST resort, not the first/only control.
- [ ] **The audiometry schedule is action-level-linked** — baseline + annual audiometry is triggered by the exposure-vs-action-level comparison (≥ 85 dBA), with STS-determination follow-up; a surveillance schedule with no action-level linkage is a FLAG.
- [ ] **Special-category audiometric data is protected** — audiometry / STS results reported by SEG/role, `<5` audiometric cells suppressed, never circulated with names; a named STS result or a `<5` audiometric cell is a FLAG (and a de_identification hard-fail).
- [ ] **India defers correctly** — for an India site the state is resolved and the skill defers to `hse-india`, emitting a literal `[GAP]` and never a minted national form-id; a fabricated India form number is a FLAG.

## Sign-off note
SME review: ran (persona: Occupational Hygienist / Audiometric Technician / OH Physician); this
is **decision-support only**. It **precedes — and never replaces — the human competent-person
sign-off**, and it never outputs the affirmative claim "approved by a competent person". A FLAG
it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak, invented
citation, weighted score below threshold) are a separate enforcement class.
