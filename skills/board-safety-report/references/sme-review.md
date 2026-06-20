---
sme-review:
  personas:
    - role: "Board-level HSE governance advisor / Company Secretary's HSE adviser"
      expertise: "20+ years advising boards & audit/risk committees, ISO 45001 9.3 management review, corporate-governance reporting (what a non-executive director needs to govern safety) and decision-grade narrative."
      lens: "Does this paper let a board GOVERN — decision-grade narrative, a leading/lagging balance, explicit asks each with a 'so what' — rather than admire a wall of numbers, and is every figure aggregated so no single incident re-identifies a person?"
    - role: "Safety-performance statistician / SIF-prevention specialist"
      expertise: "Lagging-rate interpretation, HiPo/SIF precursor theory, benchmark methodology (denominators, sector-match, base-year), and the failure mode of false assurance from a falling lagging rate."
      lens: "Are the indicators read HONESTLY — no false assurance from a falling lagging rate while leading indicators or SIF precursors say otherwise, the HiPo/SIF data interpreted not merely listed, and every benchmark like-for-like?"
---

# SME Review & Sign-off — board-safety-report

Governance here is two-headed: board-paper *craft* and statistical *honesty* are distinct
failure modes one reviewer rarely holds both of, so this skill carries **two** SME lenses.
Both specialize the generic **HSE-SME-Reviewer** runtime hook (`KB-SNIP-ARCHETYPES`) — this
is the only executive-audience skill in the pack. The universal hard gates (de-id leak,
citation accuracy, HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are
not restated below.

**De-identification + aggregation is the strongest requirement in the family.** A single
fatality at a small site re-identifies through quasi-identifiers, so ELI-LOCATION is omitted
*by design* and key events are aggregated. The de-id/aggregation scrub runs *before* the
echo-back, so the echo and the draft show aggregated, role-labelled facts — never a named
person, site, or small-cell count. A leak is a hard fail, not a FLAG.

## Domain checklist (the nuanced things only this expert catches)
- [ ] De-id + aggregation ran BEFORE the echo-back and before drafting — no single-incident anecdote, no named person/site, no small-cell (<5) count survives to board altitude; a leak is a hard fail, not a FLAG.
- [ ] Leading/lagging balance is present — a lagging-only paper steers by the rear-view mirror and is a FLAG.
- [ ] No false assurance — a falling lagging rate sold as "improving safety" while HiPo/SIF precursors or a collapsing near-miss-reporting rate say otherwise is the classic board-paper lie and a FLAG.
- [ ] HiPo/SIF is *interpreted*, not listed — the paper says what the precursors *reveal*; a bare list is a FLAG.
- [ ] Every figure carries a "so what" and a decision ask — any orphan number is a FLAG.
- [ ] Benchmark is like-for-like — a sector / base-year / convention mismatch is a FLAG; absent benchmark or prior period → `[GAP]`, never invented.
- [ ] Altitude discipline holds — operational task lists or CAPA minutiae belong in capa-manager; operational drift into the board paper is a FLAG.

## Sign-off note
SME review: ran (personas: Board-level HSE governance advisor + safety-performance
statistician); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs the affirmative claim
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks
(de-id leak, invented citation, weighted score below threshold) are a separate enforcement
class.
