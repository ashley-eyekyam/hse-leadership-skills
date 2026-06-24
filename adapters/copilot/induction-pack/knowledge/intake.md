---
intake-coverage:
  covers: [ELI-SCOPE, ELI-SUBJECT, ELI-OUTPUT, ELI-JURIS, ELI-INDUSTRY, ELI-LOCATION,
           ELI-EXPOSURE, ELI-BASELINE, ELI-EVIDENCE, ELI-OBLIGATIONS, ELI-COMPETENCY,
           ELI-TEMPORAL]
  omits:
    ELI-SCORING: "An induction pack is content assembly, not a risk-scored analysis — there is no risk-matrix / likelihood×severity rating dimension. Site-specific hazards are surfaced and their controls ranked via the hierarchy of controls (KB-SNIP-HOC); the verification scale is the competence scale (KB-DATA-COMPETENCE-LEVELS), captured under ELI-COMPETENCY, not a scoring matrix."
  branches:
    - {when: Q1, option: Contractors, activates_kb_row: KB-SNIP-INDUCTION-BASELINE, activates_output_section: site-rules-and-ptw-awareness, mandatory: false}
    - {when: Q5, option: India, activates_questions: [Q5b], activates_kb_row: KB-REG-IN-FACTORIES, activates_output_section: induction-content-baseline, mandatory: true}
---

# Structured intake — induction-pack

Run the question set below following `KB-SNIP-INTAKE` — **one question at a time**, MCQ where the
answer space is enumerable and free-text where it is open; branch on the answers; **echo the
captured facts back for confirmation before any drafting**. The intake captures the audience, the
**named site** (the specificity anchor), the site-specific hazards & arrangements available, the
delivery mode, the jurisdiction (for the legal-induction baseline), and the verification method.
**Refuse to produce a pack** until the **named site (Q2) + at least the emergency arrangements +
at least one site-specific hazard (Q3)** are captured — ask again, or record `[ASSUMPTION]` /
`[GAP]`; **never emit a generic induction**.

Load-bearing branches: the **contractor-cohort branch** (Q1 = contractors → pull site-rules +
permit-to-work awareness; induction follows `contractor-prequalification` #16) and the
**India→state branch** (Q5 = India → resolve the state via `hse-india`; no national form number
minted).

| # | Question | Type | Options / prompt | Dim | Asked-when |
|---|---|---|---|---|---|
| Q1 | **Audience** (branches the cohort) | MCQ | Permanent new starters / Contractors / Visitors / Agency or temporary | ELI-SCOPE | always |
| Q1a | **Who is exposed / being inducted** (the cohort + roles) | free-text | "Which roles/cohort is this induction for, and roughly how many? (named roles, not 'everyone' — the verification level is set per role)" | ELI-EXPOSURE | always |
| Q2 | **The named site / project / asset** | free-text | "Which specific site, project, or asset is this induction for? — **the specificity anchor; refuse a generic 'write me an induction'**" | ELI-SUBJECT | always |
| Q2a | Industry / sector | MCQ + free-text | Construction / Manufacturing / Warehouse & logistics / Oil & Gas / Chemicals / Healthcare / General-Other (+ detail) — selects the sector hazard context | ELI-INDUSTRY | always |
| Q2b | Physical location / environment | free-text | "Describe the physical site — areas covered, access/egress, any confined spaces / height / traffic / ATEX zones the inductee will encounter." | ELI-LOCATION | always |
| Q3 | **Site-specific hazards & arrangements available** | MCQ multi-select + free-text | Tick what you can supply, **and describe each for THIS site**: Site rules · Emergency & muster arrangements · First-aid & welfare · Traffic management · Permit systems (PTW) · Known site hazards — **the baseline is laid for all five topics; a topic with no named site arrangement is a `[GAP]`, never boilerplate.** | ELI-BASELINE | always |
| Q3a | Evidence / source for the site hazards | free-text | "Where do the site-specific hazards come from — the site risk assessment / HIRA, the permit register, incident history? (source + date)" | ELI-EVIDENCE | always |
| Q4 | **Delivery mode** | MCQ | Face-to-face / E-learning / Blended | ELI-OUTPUT | always |
| Q5 | **Jurisdiction** (legal-induction baseline) | MCQ | UK / USA / India / EU / Other — sets the legal-induction duty baseline | ELI-JURIS | always |
| Q5b | **India → state** (mandatory when Q5 = India) | free-text | "Which Indian state is the site in? — mandatory state detection; the induction baseline defers to `hse-india` for the state detail. No national form number is minted here." | ELI-JURIS | when Q5 = India |
| Q5a | Legal / standard obligations to satisfy | free-text | "Any specific induction duty your organisation or contract commits to (e.g. ISO 45001 7.2 and 7.3, a client site-induction standard, a CDM requirement)? (or 'standard set' → the legal-induction baseline for the jurisdiction)" | ELI-OBLIGATIONS | always |
| Q6 | **Verification method** | MCQ | Questions / quiz · Supervised sign-off · Competence demonstration — sets how understanding is proven on the verification record | ELI-COMPETENCY | always |
| Q6a | **Induction owner + verification level per role** | free-text | "Who owns delivering and signing off this induction (role), and what competence level must each role reach (aware / trained / competent / expert on KB-DATA-COMPETENCE-LEVELS)? (named role — no 'TBD')" | ELI-COMPETENCY | always |
| Q7 | **Refresher cadence** | MCQ + free-text | Annual / 2-yearly / On change of site rules or process / After an incident / Other (+interval) — higher-risk roles refresh more often | ELI-TEMPORAL | always |

**Branch map:** `contractor-cohort` (Q1 = Contractors → add site-rules + PTW awareness, follow
`contractor-prequalification`); `India→state` (Q5 = India → resolve the state via `hse-india`,
no national form number minted; mandatory state detection).

## Echo-back

After Q7, **echo a captured-facts summary** and confirm before any drafting:
"Induction pack: permanent new starters (warehouse operatives, ~12) for the **Tilbury
distribution warehouse** (warehouse & logistics; MHP areas + FLT traffic + a mezzanine edge),
delivery = blended, jurisdiction = UK (MHSWR reg. 10/13), verification = supervised sign-off,
each operative to reach 'trained' on the competence scale, induction owner = Warehouse HSE Lead,
refreshers annual — correct?" Q3's hazards/arrangements drive what gets layered onto the baseline;
no pack is produced until the named site + emergency arrangements + ≥1 site-specific hazard are
captured.

## Refuse-on-vague anchors

- **Q2 is the specificity anchor** — refuse a generic "write me an induction" with no named site;
  ask again or record `[GAP]`, never invent a site. **A generic induction is explicitly refused.**
- **Q3 is the content/gate anchor** — **do not produce a pack until the named site + at least the
  emergency arrangements + at least one site-specific hazard are captured.** An induction that is
  not grounded in *this* site's real hazards and arrangements is generic boilerplate and is
  refused; a baseline topic with no named site arrangement is named as a `[GAP]`, never filled
  with boilerplate.
- **Verification is non-negotiable** — every induction produces a competence-verification record;
  an "induction" that is only delivery content with no proof-of-understanding record fails the
  quality gate.

## Domain evidence types (ELI-EVIDENCE)

Site risk assessment / HIRA (the site-specific hazards) · permit-to-work register (the PTW
systems) · emergency-response plan (muster points, evacuation routes) · site rules / contractor
handbook · incident & near-miss history (real events to ground the hazard awareness) · the
competence/training matrix (the required verification level per role). Each site-specific hazard
cites its evidence source + date; the verification level is the `KB-DATA-COMPETENCE-LEVELS`
scale's, not a prose guess.
