---
sme-review:
  personas:
    - role: "Board-level HSE governance advisor / Company Secretary's HSE adviser"
      expertise: "20+ years advising boards & audit/risk committees, ISO 45001 9.3 management review, corporate-governance reporting (what a non-executive director needs to govern safety) and decision-grade narrative."
      lens: "Does this paper let a board GOVERN — decision-grade narrative, a leading/lagging balance, explicit asks each with a 'so what' — rather than admire a wall of numbers, and is every figure aggregated so no single incident re-identifies a person?"
    - role: "Safety-performance statistician / SIF-prevention specialist"
      expertise: "Lagging-rate interpretation, HiPo/SIF precursor theory, benchmark methodology (denominators, sector-match, base-year), and the failure mode of false assurance from a falling lagging rate."
      lens: "Are the indicators read HONESTLY — no false assurance from a falling lagging rate while leading indicators or SIF precursors say otherwise, the HiPo/SIF data interpreted not merely listed, and every benchmark like-for-like?"
modes:
  board-paper:
    detected_by: "Q2 — Audience body (Board of directors / Executive committee / Senior leadership team); this skill emits one board-audience safety paper and Q2 only tunes its altitude, so the floor applies to every run."
    floor:
      - id: leading-lagging-balance
        description: "Both leading AND lagging indicators are present with readings — a lagging-only paper steers by the rear-view mirror (intake Q3 leading indicators; ISO 45001 cl. 9.1)"
        anchors: ['lagging indicators', 'leading indicators']
        min_matches: 2
      - id: no-false-assurance
        description: "A falling lagging rate is never sold as 'improving safety' while HiPo/SIF precursors or a collapsing near-miss-reporting rate say otherwise (the classic board-paper lie)"
        anchors: ['false assurance', 'assurance from the falling rates']
        min_matches: 1
      - id: hipo-sif-interpreted
        description: "High-potential (HiPo) / SIF-precursor exposure is INTERPRETED, not merely listed — the paper says what the precursors reveal (intake Q5; the D-01 HiPo/SIF lens)"
        anchors: ['HiPo', 'high.potential', 'SIF']
        min_matches: 1
      - id: figure-so-what-and-ask
        description: "Every headline figure carries a 'so what' and, where a decision is needed, an explicit governance ask (ISO 45001 cl. 9.3 management-review outputs) — no orphan numbers"
        anchors: ['so what', 'decisions requested', 'management.review']
        min_matches: 1
      - id: benchmark-like-for-like
        description: "Benchmarks are like-for-like and carry source + year; an absent benchmark or prior period is [GAP], never invented (intake Q8; KB-DATA-TRIR-BENCHMARKS)"
        anchors: ['benchmark', '\[GAP\]']
        min_matches: 2
      - id: deid-aggregated-to-board-altitude
        description: "De-identification AND aggregation ran before board altitude — no single-incident anecdote, named person/site, or small-cell (<5) count survives (the family's strongest requirement; a leak is a hard fail, not a FLAG)"
        anchors: ['aggregat', 'de.identif']
        min_matches: 2
      - id: material-risks-carried-forward
        description: "Material risks carried into the next period are stated with the decisions requested of the board — the forward governance ledger, not just a rear-view of outcomes"
        anchors: ['material risk', 'decisions requested']
        min_matches: 1
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

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **A wall of favourable numbers with no decision** — rates and charts, no explicit ask,
  no accountable executive, no "so what". A board cannot GOVERN a paper that only reports;
  every headline needs its governance consequence.
- **The open assurance gap with no bridge** (canary S2) — a material open item (audit
  closure short of target, a late-closing HiPo CAPA, a carried-forward high risk)
  acknowledged but with no interim measure, owner, or date for the gap period. Silence over
  the gap reads as false assurance.
- **Numbers presented without their basis** (canary S5) — a rate, a trend %, or a benchmark
  stated without its denominator, base convention, source, or vintage. A board figure with
  no defensibility basis is an un-auditable claim; where the basis is absent it must be
  `[GAP]`, never smoothed over.
- **Leading/lagging read in isolation** — a falling lagging rate not reconciled against the
  leading and HiPo/SIF signals, so severity-potential (what *nearly* happened) is invisible
  behind outcome frequency (what *did* happen).
- **Altitude leakage** — operational CAPA minutiae or task lists dragged into a governance
  paper (that belongs in capa-manager), or conversely a strategic ask left with no owner.

## Sign-off note
SME review: ran (personas: Board-level HSE governance advisor + safety-performance
statistician); this is **decision-support only**. It **precedes — and never replaces, never
emits — the human competent-person sign-off**, and it never outputs the affirmative claim
"approved by a competent person". A FLAG it raises is recorded, never merge-blocking; the deterministic hard blocks
(de-id leak, invented citation, weighted score below threshold) are a separate enforcement
class.
