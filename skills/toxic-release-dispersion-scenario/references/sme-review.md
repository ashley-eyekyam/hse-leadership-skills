---
sme-review:
  personas:
    - role: "Consequence-modelling / dispersion specialist (process-safety engineer)"
      expertise: "source-term derivation, release modes (catastrophic/continuous/instantaneous), neutral vs dense-gas dispersion, weather/stability (Pasquill class), toxic endpoints (ERPG/AEGL/IDLH), the bowtie/LOPA/QRA consequence interface"
      lens: "is this honest SCENARIO FRAMING for the modelling team — or has a quantitative result been smuggled in"
modes:
  scenario-framing:
    detected_by: "Q1 — Framing target (bowtie, LOPA, QRA input, or emergency-plan/siting study — the scenario brief for a modeller)"
    floor:
      - id: trd-source-term-captured-not-computed
        description: "The source term is CAPTURED from the user (substance, inventory-at-risk, release mode, hole size/duration), NOT computed — a release rate derived from first principles without user input is a FLAG"
        anchors: ['source term', 'captured.{0,6}not computed|NOT computed']
        min_matches: 1
      - id: trd-no-invented-dispersion
        description: "No invented dispersion distance or concentration — any un-modelled distance/concentration is a literal [GAP] routed to PHAST/ALOHA + a competent person; an invented quantitative result presented as modelled is hard-gate-adjacent"
        anchors: ['un.modelled', 'PHAST|ALOHA']
        min_matches: 1
      - id: trd-weather-explicit-assumption
        description: "Weather / atmospheric stability is held as an explicit [ASSUMPTION] — an implied stability class or wind speed asserted as fact is a FLAG"
        anchors: ['\[ASSUMPTION\]', 'held.{0,20}assumption']
        min_matches: 1
      - id: trd-receptors-endpoint-named
        description: "Receptors (on-site/public/environment) and the toxic endpoint (ERPG/AEGL/IDLH) are named for the modeller — silently assuming 'no public receptor' is a FLAG"
        anchors: ['AEGL|ERPG|IDLH', 'receptor']
        min_matches: 1
      - id: trd-consequence-band-qualitative
        description: "The consequence band is qualitative only (the risk_matrix consequence-axis band), explicitly NOT a modelled severity — a band dressed up as a modelled outcome is a FLAG"
        anchors: ['qualitative', 'not a modelled|NOT a modelled']
        min_matches: 1
      - id: trd-downstream-owners-named
        description: "Downstream owners are named — the consequence side is handed to bowtie-builder / lopa-worksheet by name (SCOPE-OUT); a scenario that closes out the study itself is a FLAG (KB-STD-CCPS-BOWTIE / KB-STD-IEC-61511)"
        anchors: ['bowtie.builder', 'lopa.worksheet']
        min_matches: 1
---

# SME Review & Sign-off — toxic-release-dispersion-scenario

This is the family's deliberately most omit-heavy skill — assistive-only, it captures the
source term and hands off; it never models. One lens suffices: a consequence-modelling /
dispersion specialist whose single job is to confirm the output is honest scenario framing for
the modelling team and that no quantitative result has been smuggled in. The persona **narrows**
the Chemical-Process-Safety sector slot that extends the generic **HSE-SME-Reviewer** hook
(`KB-SNIP-ARCHETYPES`). The universal hard gates (de-id leak, citation accuracy, HoC/no-PPE-
only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] Source term captured, **not computed** — substance, inventory-at-risk, release mode, hole size/duration recorded from the user; a release **rate** derived from first principles without user input is a FLAG.
- [ ] No invented dispersion distance or concentration — any un-modelled distance/concentration is `[GAP]`, routed to PHAST/ALOHA + a competent person. An invented quantitative result presented as if modelled is **hard-gate-adjacent** (escalate).
- [ ] Weather / atmospheric stability held as an explicit assumption — an implied stability class or wind speed is flagged `[ASSUMPTION]`, never asserted as fact.
- [ ] Receptors and the toxic endpoint named, not optimistic — on-site/public/environment receptors listed and the endpoint basis (ERPG/AEGL/IDLH) named for the modeller; silently assuming "no public receptor" is a FLAG.
- [ ] Consequence band qualitative only — the `risk_matrix` output is the consequence-axis band, explicitly *not* a modelled severity; a band dressed up as a modelled outcome is a FLAG.
- [ ] Downstream owners named — the consequence side handed to `bowtie-builder` and `lopa-worksheet` by name (SCOPE-OUT); a scenario that closes out the study itself is a FLAG.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The smuggled quantitative result (canary S7 scope honesty)** — the load-bearing failure of
  this assistive skill: a distance/concentration presented as if modelled instead of a [GAP]
  handed to PHAST/ALOHA; the output must stay scenario framing, never a modelled outcome.
- **The basis asserted by silence (canary S5)** — the source term, weather/stability, and toxic
  endpoint stated with no explicit [ASSUMPTION]/[GAP] flags, so an optimistic implicit value rides
  into the study unchallenged.
- **The optimistic receptor set (assistive completeness)** — the public / environmental receptor
  silently dropped so only on-site workers are framed, understating the consequence side.
- **The study that closes itself out (canary S7 leg interaction)** — no hand-off to
  bowtie-builder / lopa-worksheet, so the consequence-side barriers are never developed by the
  owning study.

## Sign-off note
SME review: ran (persona: Consequence-modelling / dispersion specialist); this is **decision-
support only** — scenario framing for a competent-person study, NOT a modelled result. It
**precedes — and never replaces, never emits — the human competent-person sign-off**, and it
never outputs "approved by a competent person". A FLAG it raises is recorded, never merge-
blocking; the deterministic hard blocks (de-id leak, invented citation, weighted score below
threshold) are a separate enforcement class.
