# Methodology — live-working-risk-assessment (de-energize-first, statutory-justification-driven)

The domain method `live-working-risk-assessment` applies. Its spine is **de-energization first**
(`KB-SNIP-DEENERGIZE-FIRST` + `KB-SNIP-HOC`): the default is to establish an **electrically safe
work condition** (NFPA 70E **Article 120** / EAWR dead-working) and **only if dead working is
genuinely not reasonable** is live work permitted — and then **only** when the **three-part
statutory live-working test** (`KB-SNIP-LIVE-WORK-JUSTIFICATION`) holds. **A live-working plan
justified by convenience, cost, or schedule, or whose only control is arc-rated PPE with no recorded
de-energization evaluation, is never the assessment — it is a FLAG pushed up the hierarchy.** The
live-working decision is **cited statutory-test logic plus a cross-reference to the arc-flash
incident energy computed by `arc-flash-assessment` (#1)** — this skill performs **no** new
computation; the controls hierarchy and the SMART register are deterministic.

## 0. De-identify first (a prior contact / electrocution / arc-flash burn incident)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. A live-working assessment
may cite a prior **contact, electrocution, or arc-flash burn incident** as context; a named injured
worker from that incident is **special-category health data** (GDPR Art. 9 / India DPDP). Reduce the
worker to a role label, record the incident at role level, apply `<5` small-cell suppression to any
injury breakdown, and **never circulate a named incident**. The De-identifier subagent runs FIRST;
everything downstream consumes only its scrubbed output.

## 1. Scope the named task & live conductors (Q1)

- **Named task & live conductors (Q1)** — the exact task + the live conductors/apparatus + the
  operating voltage. **Refuse "work near the live parts" / "a panel"** (the specificity anchor). A
  missing task or conductor id is a `[GAP]`, never invented.

## 2. The de-energization evaluation — the de-energize-first gate (the spine)

This evaluation is recorded **first**, because de-energization is the **primary control**, not an
afterthought (Q2 — the gate the whole skill turns on):

- **The task CAN be done dead (Q2 = yes)** → the assessment **recommends de-energization + an ESWC**
  (NFPA 70E Article 120); **live work is not assessed further** — the default. Arc-rated PPE is not
  the headline.
- **The task cannot / only partly be done dead (Q2 = no/partly)** → branch to the **statutory
  live-working justification (Q3)**.

## 3. The three-part statutory live-working gate (KB-SNIP-LIVE-WORK-JUSTIFICATION) — the spine

Where live work is proposed, the **three-part test must ALL hold**, each recorded:

1. **It is unreasonable in the circumstances to work dead** — de-energizing introduces a *greater*
   hazard or is genuinely infeasible. A *desire* to keep equipment running is **not** "unreasonable
   to work dead".
2. **It is reasonable in the circumstances to work live** — the task can be done safely live given
   the system, the work, and the competence available.
3. **Suitable precautions are taken** — competent persons, approach-boundary control, insulated
   tools/PPE selected against the **calculated** incident energy (cross-referenced from #1, never
   invented), and an **energized-electrical-work permit** authorizing the task.

**The gate (reject these):** a live-work treatment justified by convenience / cost / "it's quicker"
→ **reject**; live work with no energized-electrical-work permit → **reject**; PPE selected against a
narrated/estimated incident energy rather than the engine output → **reject**; any of the three
tests not recorded → treat as **not justified**; default to dead working or emit `[GAP]`. This is
the EAWR reg 14 / OSHA 1910.333(a)(2) / NFPA 70E 130.2 gate.

## 4. Approach boundaries + arc-flash cross-reference (Q4)

- Define the **limited and restricted approach boundaries** (shock — NFPA 70E **130.4** / OSHA
  **1910.269** minimum approach distances) for the working position.
- **Cross-reference** the **arc-flash incident energy (cal/cm²) + the PPE category** at the working
  position from `arc-flash-assessment` (#1) — computed once by its `arcflash.py` engine. **This skill
  never re-derives the cal/cm² figure.** A missing arc-flash study is a `[GAP]`, never an invented
  incident-energy value. Where the incident energy at the working position exceeds **40 cal/cm²**,
  flag the work as **prohibited**.
- Author the precautions hierarchy: insulation / barriers / insulated tools → qualified persons &
  accompaniment → **arc-rated PPE LAST**, as the documented residual-hazard precaution.

## 5. Rank the controls (the hierarchy gate) + the residual

Run the `controls` engine. The narrative **always leads with de-energization** → engineer / insulate
/ barrier → approach control & qualified persons → the energized-work-permit control → **PPE LAST**.
A plan whose **only control is arc-rated PPE with no de-energization evaluation**, or whose
**justification is convenience** (`controls.validate_treatment` returning `ppe_admin_only=True` / a
lower-order-only headline) is a **FLAG pushed up the hierarchy, never the assessment**. Frame the
qualitative residual via `risk_matrix`.

## 6. Assemble the energized-work permit (Annex J) + SMART actions + report

Where live work is authorised, assemble the **energized-electrical-work permit** carrying the NFPA
70E **Annex J** content: the justification, the precautions, the approach boundaries, the PPE
(against the cross-referenced incident energy), and the **authorising signature**. Every
precaution / permit / competence action becomes a SMART action (named role owner + ISO due date +
measure), validated by `smart_actions.validate_register`. Validate the draft against
`references/QUALITY_CHECKLIST.md`, then assemble
`assets/live-working-risk-assessment.report.json` and run the canonical `report-output` call.

## Jurisdiction

US NFPA 70E (2024) **110.5/130.2** (energized-work justification + permit) / **130.4** (approach
boundaries) / **Annex J** (the permit) / **Article 120** (the ESWC default), read with **OSHA 29 CFR
1910.333(a)(2)** (de-energize-first + the additional-hazard/infeasibility justification) +
**1910.269** (T&D minimum approach distances), is the default duty; UK/EU is **EAWR 1989 reg 14**
(the three-part live-working test) + **HSG85** + **HSR25**. For India, resolve the state via
`hse-india` (**mandatory state detection**) per the CEA / state electricity rules + line-clearance
permit practice, and emit a literal `[GAP]` where a state return is owed — **never a minted national
form number**.
