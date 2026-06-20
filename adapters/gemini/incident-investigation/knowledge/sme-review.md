---
sme-review:
  personas:
    - role: "ICAM/TapRooT-trained lead incident investigator"
      expertise: "Serious-incident & SIF investigation, the 5 RCA methods (5-Whys/ICAM/SCAT/Fishbone/Swiss-Cheese), human-factors & latent-organisational-failure analysis, evidence discipline and chain-of-custody."
      lens: "Does the RCA reach a SYSTEMIC/organisational factor (not stop at 'worker error'), is every cause traced to a numbered evidence item, and were all personal identifiers scrubbed to role labels before any echo-back or draft?"
    - role: "HSE regulatory-reportability specialist"
      expertise: "RIDDOR 2013, OSHA 29 CFR 1904 recordkeeping + 1904.39 fatality/in-patient/amputation timelines, India state accident-notice forms and the OSH-Code 2020 transition; conservative notifiability judgement."
      lens: "Is the reportability verdict correct, conservative, and cited to the right rule/form/deadline — surfaced even when the conclusion is NOT reportable — with the India state resolved before any form is named?"
---

# SME Review & Sign-off — incident-investigation

Two distinct professions own two distinct failure modes here, so this skill carries
**two** SME lenses: causal-analysis *depth* (lead investigator) and regulatory
*reportability* (compliance/legal). Both specialize the generic **HSE-SME-Reviewer**
runtime hook (`KB-SNIP-ARCHETYPES`); the first lens also narrows the mining-pack Mine
Manager archetype's "RCA reaches organisational factors" check. The universal hard
gates (de-id leak, citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the
enforced class and are deliberately not restated below.

**De-identification is a non-waivable HARD gate for this skill.** The Q5 people-involved
scrub runs *before* echo-back and before any drafting, so every echo and every draft
shows stable role labels ("Worker A", "W-1") and never a raw name. A de-id leak is a
hard fail, not a FLAG.

## Domain checklist (the nuanced things only this expert catches)
- [ ] De-id pass ran BEFORE the echo-back and before drafting — the echo and the draft carry role labels only ("Worker A", "W-1"), never raw names, addresses, or small-cell (<5) identifiers; a leak is a hard fail, not a FLAG.
- [ ] RCA reaches the system — method-specific test: a 5-Whys terminal why is not "careless/forgot"; ICAM has ≥1 Organisational Factor; SCAT has Basic Causes *and* Lack-of-Control; Fishbone has ≥1 non-"Man" branch; Swiss-Cheese names a latent organisational layer. A "valid but shallow" RCA is a FLAG.
- [ ] Every cause carries an evidence_ref, root causes especially — any un-evidenced cause promoted to "root" is a FLAG; evidence comes before cause, cause before control.
- [ ] Reportability is surfaced even when negative — a silent non-report is a FLAG; a missed notification trigger (e.g. an amputation under OSHA 1904.39's 24h clock) is the most serious FLAG.
- [ ] India: the state is resolved before any form is cited — a form named without a confirmed state, or inferred from an address, is wrong-form risk; an un-seeded state resolves to `[GAP]`, never a fabricated national form.
- [ ] Immediate vs contributing vs root causes are not conflated, and an optional single-event contextual rate (if Q3∈{injury,illness}) uses real hours+counts only and is framed as context — never a fabricated denominator and never used as a conclusion.

## Sign-off note
SME review: ran (personas: ICAM-trained lead investigator + HSE regulatory-reportability
specialist); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs "approved by a
competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a
separate enforcement class.
