---
sme-review:
  personas:
    - role: "Industrial toxicologist / GHS-CLP classification SME"
      expertise: "GHS hazard-class structure + EU CLP (incl. Annex VI harmonised entries), bridging principles, cut-off/concentration limits, the 16-section SDS contract"
      lens: "is every assigned class logically forced by the STATED data — and is every absent datum honestly [GAP], never back-filled"
    - role: "Regulatory-affairs / SDS-format specialist"
      expertise: "jurisdictional SDS format + duties — EU REACH (e)SDS + exposure scenarios §15, UK COSHH, US HazCom 29 CFR 1910.1200"
      lens: "does the SDS section set + label match the RESOLVED jurisdiction, not a blurred generic"
---

# SME Review & Sign-off — ghs-classification-sds-author

This skill carries the chemicals family's **only** justified 2nd lens (D-06; max 2):
classification competence and jurisdictional SDS-format competence are two distinct
expertises — an industrial toxicologist who forces every hazard class from the stated data,
and a regulatory-affairs specialist who matches the SDS section-set and label to the resolved
jurisdiction. Both **narrow** the Chemical-Process-Safety sector slot that extends the generic
**HSE-SME-Reviewer** hook (`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak,
citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are
not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Every applicable hazard class assessed — physical *and* health *and* environmental classes considered; a class silently skipped (not `[GAP]`-marked) is a FLAG.
- [ ] Class ⇄ category ⇄ H-statement ⇄ pictogram ⇄ signal word mutually consistent — e.g. "Danger" with only Category-2 hazards, or a pictogram absent for an assigned class, is a FLAG. A class/category/H-statement invented on absent data is **hard-gate-adjacent** (escalate).
- [ ] Mixture classification method stated — calculation/summation vs bridging vs test data, with the cut-off / concentration limits actually applied; an undocumented method is a FLAG.
- [ ] EU CLP Annex VI harmonised entry checked where one exists — a self-classification contradicting a harmonised entry is a FLAG.
- [ ] §8 exposure controls HoC-ranked — engineering/LEV/containment ahead of RPE/PPE; a PPE/RPE-first §8 is **hard-gate-adjacent** (HoC) unless justified-or-escalated. Any OEL/WEL/PEL in §8 carries source + year (SEG depth deferred to `chemical-exposure-register`).
- [ ] §14 transport **not authored here** — the transport class/UN/packing-group cross-walk is handed to `chemical-transport-safety`; a transport classification invented in-skill is a FLAG.
- [ ] Output framed as a decision-support draft, **never** an authoritative regulatory SDS — a draft presented as the final compliant SDS is a FLAG.

## Sign-off note
SME review: ran (personas: Industrial toxicologist / GHS-CLP classification SME + Regulatory-
affairs / SDS-format specialist); this is **decision-support only**. It **precedes — and never
replaces, never emits — the human competent-person sign-off**, and it never outputs "approved
by a competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic
hard blocks (de-id leak, invented citation, weighted score below threshold) are a separate
enforcement class.
