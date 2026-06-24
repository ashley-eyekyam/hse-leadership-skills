---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-SCORING, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-EXPOSURE: "A clause-by-clause management-system conformance gap analysis is system-level (does the organisation meet each ISO 45001 clause); it has no exposed-population dimension. Personal-data exposure in audit interview notes is handled by the mandatory de-id step, not an intake question."
  branches:
    - {when: Q1, option: ISO 14001 (environmental), activates_kb_row: KB-STD-ISO14001, activates_output_section: clause-conformance-matrix, mandatory: false}
    - {when: Q1, option: ISO 45003 (psychosocial), activates_kb_row: KB-STD-ISO45003, activates_output_section: clause-conformance-matrix, mandatory: false}
    - {when: Q1, option: Combined, activates_kb_row: KB-STD-ISO14001, activates_output_section: clause-conformance-matrix, mandatory: false}
---

# Structured intake — iso45001-gap-analysis

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ
where the answer space is enumerable and free-text where it is open; branch on the
answers; **echo the captured facts back for confirmation before any analysis**. The
intake opens with the **standard selector (Q1)** — which fixes the clause set the walk
scores against — then captures the named scope, current state, per-clause-group evidence,
and target. **Refuse to score** until the **standard (Q1) + the named scope (Q2) + at least
one evidence source per major clause group (Q4)** are captured — ask again, or record
`[ASSUMPTION]` / `[GAP]`; never invent a conformance level.

Load-bearing branch: the **standard-selector branch** (Q1 = ISO 14001 / ISO 45003 / Combined
→ swap in that standard's clause set via the matching `KB-STD-*` row; the clause-walk method,
the maturity scale, and the prioritisation method are unchanged).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Standard to assess against** (branches the clause set) | MCQ | ISO 45001 (OH&S, default) / ISO 14001 (environmental) / ISO 45003 (psychosocial) / Combined | ELI-SCOPE | always |
| Q2 | **The named organisation / site + boundary** | free-text | "Which specific organisation or site is in scope, and what is the management-system boundary (whole org / one site / one division)?" — **the specificity anchor; refuse a generic 'are we ISO-ready?'** | ELI-SUBJECT | always |
| Q2a | Industry / sector | MCQ + free-text | Construction / Manufacturing / Oil & Gas / Chemicals / Mining / Healthcare / General-Other (+ detail) — selects sector context for the clause evidence | ELI-INDUSTRY | always |
| Q2b | Physical scope / sites covered | free-text | "Single site or multi-site? Name the site(s)/area(s) the analysis covers." | ELI-LOCATION | always |
| Q3 | **Current state** | MCQ | No system / Informal (undocumented) / Certified to another standard / Preparing for initial certification / Maintaining an existing certification | ELI-BASELINE | always |
| Q4 | **Evidence available, per major clause group** | MCQ multi-select + free-text | Tick the clause groups you can supply evidence for: Policy & leadership (cl. 5) · Planning / risk (cl. 6) · Support & competence (cl. 7) · Operation (cl. 8) · Performance evaluation (cl. 9) · Improvement (cl. 10) — **+ describe the evidence for each ticked group** (procedures, records, audit reports, minutes). **A clause group with no evidence is scored as a gap — never silently omitted.** | ELI-EVIDENCE | always |
| Q4a | Documented obligations / mandatory clauses to weight | free-text | "Any clauses your certification body or your organisation specifically commits to or has flagged (e.g. 5.2 policy, 9.2 internal audit)? (or 'standard set' → I assess all of 4–10)" | ELI-OBLIGATIONS | always |
| Q5 | **Target of this assessment** | MCQ | Initial certification readiness / Internal assurance / Surveillance-audit prep | ELI-OUTPUT | always |
| Q5a | Conformance scoring scale | MCQ | **5-level maturity scale (0 Absent → 4 Measured, default — `KB-DATA-ISO45001-MATURITY`)** / Supply our own scale | ELI-SCORING | always |
| Q6 | Operating jurisdiction (context only) | free-text | "Which country/countries does the management system operate in? Context only — ISO 45001/14001/45003 are jurisdiction-independent, so this does not change the clause scoring. For the legal clause (6.1.3) the legal register is a separate skill; any country-specific legal detail defers to that skill's engine. No national form number is minted here." | ELI-JURIS | always |
| Q7 | **Lead auditor + remediation owners** | free-text | "Who is the competent person running this gap analysis (role), and who will own the remediation actions? (named role/person — no 'TBD')" | ELI-COMPETENCY | always |
| Q7a | **Target certification / review date** | MCQ + free-text | Target cert/surveillance date / Next management-review date / Other (+date) — feeds the roadmap due-date horizon | ELI-TEMPORAL | always |

**Branch map:** `standard-selector` (Q1 = ISO 14001 / ISO 45003 / Combined → swap the
`KB-STD-*` clause set; non-mandatory). No India→state branch is wired — this is a
jurisdiction-independent standards gap analysis; Q6 is context-only.

## Echo-back

After Q7a, **echo a captured-facts summary** and confirm before any analysis:
"Gap analysis: ISO 45001 against AcmeCo Plant 2 (single site, manufacturing), current state
= preparing for initial certification, evidence held for clause groups 5/6/7/9 (none yet for
8/10), target = initial certification readiness, 5-level maturity scale, lead auditor = HSE
Manager, target cert date 2026-12-01 — correct?" Q4's evidence map drives which clauses can be
scored above level 1.

## Refuse-on-vague anchors

- **Q2 is the specificity anchor** — refuse a generic "are we ISO-ready?" with no named
  organisation/site; ask again or record `[GAP]`, never invent a scope.
- **Q4 is the evidence/gate anchor** — **do not score any conformance level until at least one
  evidence source per major clause group is captured.** Scoring a clause "conformant" on
  self-assertion alone (no records, no procedure) is a vacuous pass and is refused — a clause
  with no evidence is scored as a gap (level 0/1), and the analysis names the `[GAP]` where
  evidence is missing. Never rate the whole system "ready" off a single document.

## Domain evidence types (ELI-EVIDENCE)

OH&S policy + objectives (cl. 5) · risk-assessment / HIRA records + legal register (cl. 6) ·
competence matrix + training records + communication logs (cl. 7) · operational-control
procedures + permit-to-work + emergency plans + contractor controls (cl. 8) · monitoring data
+ internal-audit reports + management-review minutes (cl. 9) · incident-investigation +
corrective-action / nonconformity records (cl. 10). Each conformance level requires the
**evidence test** for that level in `KB-DATA-ISO45001-MATURITY`.
