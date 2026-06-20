---
sme-review:
  personas:
    - role: "India BOCW / construction-labour-welfare compliance specialist"
      expertise: "Building & Other Construction Workers (RE&CS) Act 1996 + Welfare Cess Act 1996 + state BOCW Rules + the state Construction Workers Welfare Boards"
      lens: "is the RIGHT state Welfare Board's registration/cess/return correctly attributed to the right duty-holder, and is the 1% cess base correctly framed?"
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

## Sign-off note
SME review: ran (persona: India BOCW / construction-labour-welfare compliance specialist);
this is **decision-support only**. It **precedes — and never replaces, never emits — the
human competent-person sign-off**, and it never outputs "approved by a competent person". A
FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks (de-id leak,
invented citation, weighted score below threshold) are a separate enforcement class.
