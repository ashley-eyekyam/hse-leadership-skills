---
sme-review:
  personas:
    - role: "Dangerous-goods (DG) transport SME / Dangerous Goods Safety Adviser"
      expertise: "UN model regulations + the modal regimes in scope — ADR (EU road), US DOT 49 CFR HMR (§172.101 HMT), IMDG (sea); UN number / PSN / class / packing group, placarding & marking, segregation of incompatible classes"
      lens: "is the UN entry resolved from the Dangerous Goods List (never assumed); is the GHS→transport cross-walk correct for the chosen mode; are rail/air flagged out of scope rather than guessed"
---

# SME Review & Sign-off — chemical-transport-safety

One lens suffices: a dangerous-goods transport SME / DGSA who resolves the UN entry from the
Dangerous Goods List and cross-walks GHS to the chosen modal regime. The persona **narrows**
the Chemical-Process-Safety sector slot that extends the generic **HSE-SME-Reviewer** hook
(`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-
only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] UN number / proper shipping name resolved from the Dangerous Goods List, not assumed — an assumed/invented UN entry or class is **hard-gate-adjacent** (escalate); an unknown entry is `[GAP]`-flagged.
- [ ] Class + packing group cross-walk matches the **chosen mode** — correct for ADR vs DOT-HMR vs IMDG (the same substance can differ by regime); a mode-mismatched classification is a FLAG.
- [ ] Segregation respects class incompatibilities — the mode's segregation table/rules applied to incompatible classes loaded together; a missing segregation check is a FLAG.
- [ ] Placarding & marking match the resolved class/UN/PG — placards, UN marks, and (IMDG) the marine-pollutant mark consistent with the classification; an inconsistent placard set is a FLAG.
- [ ] Rail (RID) and air (IATA/ICAO-TI) flagged out of scope for v1.0 — **not answered**; an output that classifies for rail/air is a FLAG.
- [ ] India road branch: the state is resolved BEFORE any CMVR/state transport rule is cited — a transport rule cited without a confirmed state, or a national-form fallback, is a FLAG; an unverified India transport row stays `[GAP]`.
- [ ] Loading/unloading controls HoC-ranked — engineering/handling controls ahead of admin/PPE; a PPE-only loading control is **hard-gate-adjacent** (HoC) unless justified-or-escalated.

## Sign-off note
SME review: ran (persona: Dangerous-goods transport SME / DGSA); this is **decision-support
only** and is not a shipping declaration. It **precedes — and never replaces, never emits — the
human competent-person / DGSA sign-off**, and it never outputs "approved by a competent
person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks
(de-id leak, invented citation, weighted score below threshold) are a separate enforcement
class.
