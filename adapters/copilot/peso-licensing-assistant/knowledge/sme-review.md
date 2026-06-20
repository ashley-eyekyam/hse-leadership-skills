---
sme-review:
  personas:
    - role: "Indian PESO licensing specialist (Petroleum Act / Explosives Act / Gas Cylinder & SMPV(U) Rules)"
      expertise: "Matching installation + capacity to the correct PESO instrument and form; MSIHC MAH on-site emergency plan; licence/authority routing."
      lens: "Is the licence type, form and authority correctly matched to this installation from the KB row — and is the MSIHC on-site emergency plan present whenever the installation is a MAH?"
    - role: "India HSE / labour-law compliance reviewer (state-form & legacy-first discipline)"
      expertise: "Mandatory state detection; legacy-first form citation; KB-REG-IN-STATEFORMS; OSH-Code transition framing."
      lens: "Is the site state resolved before any state-specific obligation is cited, and is every form taken from the KB row rather than a hard-coded national number — with any unverified form-id left as a literal [GAP]?"
---

# SME Review & Sign-off — peso-licensing-assistant

Two distinct disciplines own two failure modes on a PESO licensing artifact: matching
the **installation to the correct PESO instrument, form and authority** (the licensing
specialist) and the **state-form / legacy-first citation discipline** (the India
compliance reviewer). So this skill carries **two** SME lenses. Both specialize the
family's single **Process-Safety Engineer** archetype (`KB-SNIP-ARCHETYPES`) — the
PESO/MSIHC remit — and the second lens deliberately overlaps the India-Regulatory slot
(licensing ≠ statutory-form discipline); it must stay consistent with that slot, never
contradict it. The generic **HSE-SME-Reviewer** hook is the inherited fallback. The
universal hard gates (de-id leak, citation/clause accuracy, HoC, owned-and-dated actions)
are the enforced class and are not restated below.

**Form-id honesty is load-bearing here (GATE-06).** Every form must be resolved from the
matched KB row (`KB-REG-IN-PESO` / `KB-REG-IN-STATEFORMS`), never a nationally-hard-coded
number. Any PESO form whose id is **not** verified in the KB — including Form E, Form F,
or LS-1A — is left as a literal `[GAP]` routed to the authority/competent person; it is
**never invented**. The citation grader is row-blind to a fabricated form value, so this
discipline is the load-bearing statutory check, not a formatting nicety.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every form is resolved from `KB-REG-IN-PESO` / `KB-REG-IN-STATEFORMS`; no nationally-hard-coded form number appears, and any unverified form-id (e.g. Form E / Form F / LS-1A) is left as a literal `[GAP]` — never invented.
- [ ] Installation + capacity maps to the right PESO instrument (Petroleum Rules 2002 · Explosives Rules 2008 · Gas Cylinder Rules 2016 · SMPV(U) Rules 2016) → the right form and the right authority.
- [ ] Site state is resolved (asked, or inferred-from-address then confirmed) before any state-specific siting/consent obligation is cited — never silently assumed; an unconfirmed state means no state-specific form is cited yet.
- [ ] If the installation crosses MSIHC MAH thresholds, the on-site emergency plan is structured (reading `KB-REG-IN-MSIHC`); a MAH installation with no on-site plan is flagged.
- [ ] The OSH-Code transition note is appended (legacy-first framing); the transition itself is left to the hse-india skill — this skill only appends the note, never presents a consolidated national form as live.
- [ ] The named authority (PESO / Chief Controller of Explosives vs the state authority) matches the resolved instrument and state, and the artifact reads as structured licensing support, not autonomous regulatory determination (FLAG).

## Sign-off note
SME review: ran (personas: Indian PESO licensing specialist + India state-form compliance
reviewer); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class owned by the automated harness.
