---
sme-review:
  personas:
    - role: "India BOCW / construction-labour-welfare compliance specialist"
      expertise: "Building & Other Construction Workers (RE&CS) Act 1996 + Welfare Cess Act 1996 + state BOCW Rules + the state Construction Workers Welfare Boards"
      lens: "is the RIGHT state Welfare Board's registration/cess/return correctly attributed to the right duty-holder, and is the 1% cess base correctly framed?"
modes:
  compliance-review:
    detected_by: "Q1 = India + Q2 = Construction (BOCW) → the state BOCW compliance gap-list / return for the confirmed state Welfare Board"
    floor:
      - id: state-resolved-before-board-cited
        description: "The state is resolved and confirmed before any Welfare-Board return/portal is cited — BOCW is run by state Welfare Boards; an unconfirmed state is a FLAG"
        anchors: ['karnataka', 'welfare board']
        min_matches: 2
      - id: form-xxv-cess-verified-anchors
        description: "Form XXV (annual return, ~15 Feb) and the 1% welfare cess are cited as the verified anchors"
        anchors: ['form xxv', 'cess']
        min_matches: 2
      - id: cess-base-cost-of-construction
        description: "The 1% welfare cess is framed against the COST OF CONSTRUCTION (not wages/headcount); a mis-attributed cess base is a FLAG"
        anchors: ['cost of construction', 'cess']
        min_matches: 2
      - id: state-values-gap-never-invented
        description: "State-specific values the KB does not verify (Safety-Officer headcount threshold, accident-notice form/timing) are literal [GAP], never inferred or fabricated"
        anchors: ['\[gap', 'not verified|not confirmed|do not substitute|verify']
        min_matches: 2
      - id: duty-holder-attribution
        description: "Registration, cess, return and accident-notice duties land on the correct duty-holder (principal employer vs contractor / establishment), not generically 'the site'"
        anchors: ['principal employer', 'contractor']
        min_matches: 2
      - id: safety-officer-threshold-state-not-national
        description: "The Safety-Officer / Safety-Committee appointment trigger is read from the resolved state's rule (or [GAP]), never a single hard-coded national headcount"
        anchors: ['safety officer', 'threshold']
        min_matches: 2
      - id: corrective-controls-smart-owned
        description: "Each compliance gap carries a corrective control as a SMART action with a role-label owner and a due date (HoC-ranked where a physical control is needed)"
        anchors: ['action|corrective|smart', 'due|by 19 july|by 4 august|15 february']
        min_matches: 2
      - id: osh-code-savings-legacy-primary
        description: "The OSH-Code transition is noted as direction-of-travel with the savings clause + per-state commencement caveat; legacy BOCW filings stay primary"
        anchors: ['osh code', 'savings clause|legacy']
        min_matches: 2
---

# SME Review & Sign-off — bocw-compliance

This is an **always-India** skill — `ELI-JURIS` is the spine and India→state detection is
load-bearing. BOCW is administered by the **state Construction Workers Welfare Boards**, so
the operative return + portal are state-Board-specific: the state must be resolved and
confirmed BEFORE any Welfare-Board return or portal is cited. One lens suffices — a single
specialist covers the statutory + welfare-board surface; the legal interpretation here is
duty-attribution (principal employer vs contractor), not contested construction. The persona
**narrows** the `India-Regulatory` SME-persona archetype (`KB-SNIP-ARCHETYPES`) to the BOCW
Act 1996 + state Welfare-Board layer. The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] **State resolved BEFORE any Welfare-Board return/portal is cited** — citing Form XXV timing or a Board portal without a *confirmed* state (or inferring from address without echo-back) is FLAGged. State detection is the mandatory, blocking, infer-then-confirm gate (`KB-REG-IN-STATEFORMS`, topic `state-detection`); an unseeded/unknown state → literal `[GAP]` + route to the state Welfare Board, never a fabricated national value.
- [ ] **`≥10`-worker registration trigger + cess base correctly applied** — establishment registration keyed to the ≥10-worker threshold; the **1% welfare cess** stated against *cost of construction* (not wages/headcount). A mis-attributed cess base is FLAGged.
- [ ] **Form XXV annual return cited as the verified anchor; everything else honestly `[GAP]`** — safety-officer headcount threshold, accident-notice form/timing, and cess due date are state-specific and must be `[GAP]` where the KB does not verify them, never inferred. **[GAP — verify the Form XXV due date and the state Safety-Officer/Committee headcount triggers against the live state BOCW Rules; do not assert.]**
- [ ] **Duty correctly attributed to the principal employer vs the contractor/establishment** — registration, cess, return, and accident-notice duties land on the correct duty-holder (principal employer / employer of record), not generically "the site". A mis-attributed duty-holder is FLAGged.
- [ ] **Safety-Officer / Safety-Committee thresholds tied to the resolved state, not a national default** — the appointment trigger is read from the KB row for the resolved state; a single hard-coded national headcount is FLAGged. **[GAP — verify per-state Safety-Officer headcount trigger.]**
- [ ] **OSH-Code transition noted as direction-of-travel, not overstated** — BOCW-subsumed-under-OSH-Code-2020 is flagged with the savings clause + per-state commencement caveat; presenting a consolidated BOCW-replacement form as *live* is FLAGged.
- [ ] **HoC + owner/date on every corrective control** — each gap's corrective control HoC-ranks engineering/admin before PPE and carries a role-label owner + date.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The gap with no bridge (S2)** — an acknowledged compliance gap (unregistered establishment,
  unpaid cess, absent Safety Officer) with a far due date and no interim measure for the exposure
  period leaves the principal employer exposed now. Each gap carries its corrective action AND the
  interim control until it closes.
- **The regime named, its duty set unswept (S6)** — citing "the BOCW Act" while omitting the
  duties it pairs with the return: beneficiary registration (s.12), welfare amenities (Chapter IV),
  statutory registers, contractor-compliance verification, and accident notification. Sweep the
  BOCW duty set, not just the annual return.
- **The state value asserted as national (S5)** — the Safety-Officer headcount threshold, the
  accident-notice form, and cess due dates are state-specific; a single national number presented
  without its source is a recalled guess. Source the state value or [GAP] it.
- **Derivative liability through contractors** — the principal employer's exposure for a
  contractor's default (cess arrears, unregistered workers) is a standard Board enforcement posture;
  a gap-list that assesses only the principal employer and never the on-site contractors is hollow.

## Sign-off note
SME review: ran (persona: India BOCW / construction-labour-welfare compliance specialist);
this is **decision-support only**. It **precedes — and never replaces, never emits — the
human competent-person sign-off**, and it never outputs "approved by a competent person". A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
