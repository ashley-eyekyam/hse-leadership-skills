---
sme-review:
  personas:
    - role: "Flight-Data-Monitoring (FDM/FOQA) analyst"
      expertise: "exceedance/event-summary interpretation, trend vs one-off discrimination, threshold sensibility, the assistive boundary (structures supplied summaries, never analyses raw parameter data)"
      lens: "is every finding traced to a SUPPLIED summary item, are the trends real (not single-event noise), and has nothing been invented?"
    - role: "SME line pilot / fleet operational reviewer"
      expertise: "operational meaning of exceedances (unstable approach, high-energy, hard landing, GPWS/EGPWS), de-identification of crew, what an exceedance MEANS on the line"
      lens: "does the operational interpretation make line-sense, and is crew identity protected so this can never feed a punitive process?"
modes:
  exceedance-analysis:
    detected_by: "Q1 — What do you want produced? == Structure a period's exceedance summary (the FDM/FOQA analysis report, ICAO Annex 19 Pillar 3 Safety Assurance)"
    floor:
      - id: fdm-findings-trace-supplied
        description: "Every figure traces to a user-supplied summary item — the assistive boundary; an absent datum is a [GAP] routed to the competent FDM team, never a fabricated exceedance count or value"
        anchors: ['supplied', 'traces to', '\[GAP\]', 'as reported']
        min_matches: 1
      - id: fdm-structuring-not-raw
        description: "The output reads as structuring of supplied summaries, not autonomous analysis of raw flight data — flag any computed-from-raw result"
        anchors: ['supplied summ', 'exceedance summ', 'structur']
        min_matches: 1
      - id: fdm-trend-vs-oneoff
        description: "Trend vs one-off is discriminated — a single exceedance is not reported as a trend; an 'increasing' finding is backed by ≥2 periods of supplied data"
        anchors: ['trend', 'one.?off', 'across.{0,12}period', 'quarter']
        min_matches: 1
      - id: fdm-crew-deid-protected
        description: "Crew de-identification is protected — any crew named in a supplied summary is scrubbed to a role label before reasoning; FDM/FOQA identity protection (a leak is a de-id hard-fail)"
        anchors: ['de.identif', 'role label', 'crew.{0,18}protect', 'identity protect']
        min_matches: 1
      - id: fdm-findings-to-smart-actions
        description: "Each finding drives an HoC-ranked SMS action with a named role owner and a due date, not a crew-blame conclusion"
        anchors: ['owner', 'due', 'action', 'hierarchy of controls']
        min_matches: 2
      - id: fdm-findings-risk-ranked
        description: "Findings are risk-ranked/prioritised against hazard severity, not presented as a flat undifferentiated list"
        anchors: ['risk.rank', 'prioriti', 'severity', 'highest.risk']
        min_matches: 1
      - id: fdm-data-period-source
        description: "The data period(s) and the monitoring-programme source are identified so the analysis is tied to a dated, filed basis (record identity)"
        anchors: ['period', 'quarter', 'rolling', 'data source', 'FDM programme']
        min_matches: 1
---

# SME Review & Sign-off — aviation-fdm-foqa-analysis

This skill carries **two** SME lenses, both narrowing the **Aviation-SMS** archetype
(`KB-SNIP-ARCHETYPES`, the assistive-FDM check: "structured analysis of *user-supplied*
exceedance summaries, NOT autonomous analysis of raw flight data"). A 2nd lens is justified
because an FDM/FOQA finding needs both the **analytic read** (is the figure real, is the
trend real, is nothing invented) and the **operational read** (does the exceedance mean what
the output says on the line) — two distinct professions owning two distinct failure modes.
`status: assistive` is load-bearing here: an invented exceedance count/value is a FLAG, and
because FDM/FOQA data is intrinsically crew-and-sector-identifying, a **crew-identity leak is
a de-id hard-fail**, not a soft FLAG. The universal hard gates (de-id leak, citation accuracy,
HoC/no-PPE-only, owned-and-dated actions) are the enforced class and are not restated below.

## Domain checklist (the nuanced things only this expert catches)
- [ ] The assistive boundary holds — NO invented exceedance count or value; every figure traces to a user-supplied summary item; an absent datum is `[GAP]` routed to the competent FDM team, never fabricated.
- [ ] It reads as structuring of supplied summaries, not autonomous analysis of raw flight data — flag any output presenting a computed-from-raw result.
- [ ] Exceedance thresholds referenced are sensible — where the summary states a threshold (approach-speed / rate-of-descent gate), flag an implausible or mis-stated value for the event type (the analyst's catch).
- [ ] Trend vs one-off is discriminated — a single exceedance is not reported as a trend; a finding labelled "increasing" is backed by ≥2 periods of supplied data.
- [ ] Crew de-identification is protected — any crew named in a supplied summary is scrubbed to a role label *before* the content is reasoned about; FDM/FOQA data is doubly sensitive (it can identify a specific crew on a specific sector) and a leak is a de-id hard-fail. Role labels only; no re-identification.
- [ ] Findings reach systemic SMS actions — each finding drives an HoC-ranked SMS action with a named owner and date, not a crew-blame conclusion.
- [ ] Any DGCA CAR / FAA AC / EASA AMC reference is cited, never invented — India → `KB-REG-IN-DGCA` (exact CAR number `[GAP]` when unverified); FAA/EASA/Other → the user-supplied reference; an unconfirmable clause stays literal `[GAP]`, never a fabricated number.

## Omission lens

Run the shared omission protocol **`KB-SNIP-COMPLETENESS`**
(`../../../knowledge-base/prompt-snippets/completeness-lens.md`) as the second pass of this
skill's Step-4 SME review. The `modes:` map in this file's frontmatter declares the per-mode
must-include floor (the tripwire the pass reconciles against — never its search space).
Below are ONLY this skill's blind-spot hints.

Skill-specific blind spots (where this artifact class has actually gone hollow):
- **The repeat exceedance with no bridge** — an exceedance category that has broken its
  threshold gets an action dated a quarter out with no interim mitigation (a temporary
  procedure emphasis, a targeted briefing, an enhanced-monitoring flag) for the intervening
  period. The analysis looks complete while the trend runs on.
- **Prior-period silence** — the quarter's findings are structured without any comparison to
  the operator's prior-period exceedance history or occurrence record, so a genuinely rising
  trend is indistinguishable from normal variation.
- **Record identity & basis** — the analysis is not tied to a named data period, a stated
  monitoring programme, or the event-set definitions it counts against, so it cannot be filed
  as a dated safety-assurance record or reconciled against the next quarter.

## Sign-off note
SME review: ran (persona: FDM/FOQA analyst, with an SME line-pilot lens — Annex 19 Pillar 3
Safety Assurance; assistive); this is **decision-support only**. It **precedes — and never
replaces, never emits — the human competent-person (aviation-SME / FDM-team) sign-off**, and
it never outputs the affirmative claim "approved by a competent person". A FLAG it raises is
recorded, never merge-blocking; the deterministic hard blocks (de-id leak — acute for crew
data here — and invented citation) are a separate enforcement class.
