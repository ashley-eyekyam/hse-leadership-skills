---
sme-review:
  personas:
    - role: "Dangerous-goods (DG) transport SME / Dangerous Goods Safety Adviser"
      expertise: "UN model regulations + the modal regimes in scope — ADR (EU road), US DOT 49 CFR HMR (§172.101 HMT), IMDG (sea); UN number / PSN / class / packing group, placarding & marking, segregation of incompatible classes"
      lens: "is the UN entry resolved from the Dangerous Goods List (never assumed); is the GHS→transport cross-walk correct for the chosen mode; are rail/air flagged out of scope rather than guessed"
modes:
  consignment-classification:
    detected_by: "Q1 — Scope (classify for transport, loading/unloading guidance, or a transport-document/placard check for the consignment)"
    floor:
      - id: cts-un-entry-resolved
        description: "The UN number / proper shipping name is resolved from the Dangerous Goods List, not assumed; an unknown entry is [GAP]-flagged and an invented UN/class is escalated (KB-STD-GHS)"
        anchors: ['UN ?1791|UN number', 'dangerous goods list', 'proper shipping name']
        min_matches: 1
      - id: cts-class-pg-crosswalk-mode
        description: "The class + packing group cross-walk matches the CHOSEN mode (ADR vs DOT-HMR vs IMDG) — a mode-mismatched classification is a FLAG (KB-REG-EU-ADR)"
        anchors: ['PG ?III|packing group', 'ADR', 'cross.?walk']
        min_matches: 1
      - id: cts-segregation-incompatibility
        description: "Segregation respects class incompatibilities — the mode's segregation table/rules are applied; a missing segregation check is a FLAG"
        anchors: ['segregation', 'incompatib', 'mixed loading']
        min_matches: 1
      - id: cts-placarding-marking
        description: "Placarding & marking match the resolved class/UN/PG (placards, UN marks, and the IMDG marine-pollutant mark) — an inconsistent placard set is a FLAG"
        anchors: ['placard', 'marine pollutant']
        min_matches: 1
      - id: cts-rail-air-out-of-scope
        description: "Rail (RID) and air (IATA/ICAO-TI) are flagged out of scope for v1.0 — an output that classifies for rail/air is a FLAG"
        anchors: ['out of scope', 'RID', 'IATA']
        min_matches: 1
      - id: cts-loading-hoc-ranked
        description: "Loading/unloading controls are HoC-ranked — engineering/handling controls ahead of admin/PPE; a PPE-only loading control is hard-gate-adjacent (HoC) unless justified-or-escalated (KB-SNIP-HOC)"
        anchors: ['hierarchy', 'loading . unloading|loading/unloading']
        min_matches: 1
      - id: cts-transport-doc-route-controls
        description: "The transport document is set and route-specific controls (ADR tunnel restriction code, multimodal handover/segregation) are resolved or [GAP]'d — never guessed"
        anchors: ['transport document', 'tunnel', 'multimodal']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The classification with no emergency leg (canary S1)** — a class/UN assigned but no emergency
  action information (EAC/Hazchem or the ADR written instructions), spill/leak response, or
  first-response for a corrosive/toxic-gas evolution on the route.
- **The regime named, its element set unswept (canary S6)** — ADR/IMDG cited while the mode's full
  element set (segregation table, tunnel code, packaging UN-spec, documentation, placard set) is
  not actually swept for the consignment.
- **The two legs that never meet (canary S7)** — a multimodal consignment where the road leg and
  the sea/port handover are classified independently, with the segregation/marking carry-over at
  the boundary never reconciled.
- **The quantitative basis absent (canary S5)** — flashpoint, quantity thresholds (LQ/placard
  limits), and the tunnel category recorded or `[GAP]`'d, never a bare 'transport it safely'.

## Sign-off note
SME review: ran (persona: Dangerous-goods transport SME / DGSA); this is **decision-support
only** and is not a shipping declaration. It **precedes — and never replaces, never emits — the
human competent-person / DGSA sign-off**, and it never outputs "approved by a competent
person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks
(de-id leak, invented citation, weighted score below threshold) are a separate enforcement
class.
