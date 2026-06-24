# Methodology — Construction Phase Plan (CDM 2015 Reg 12)

The method this skill applies to produce a **risk-proportionate Construction Phase Plan
(CPP)** from a **named project's real significant activities**, grounded in `KB-REG-CDM2015`
(Reg 12 + HSE L153) / `KB-REG-OSHA1926` (US) and the proportionate content skeleton
`KB-SNIP-CPP-STRUCTURE`. Risk scoring, control ranking, and residual re-scoring are
**deterministic** A7 engine calls (`risk_matrix`, `controls`, `smart_actions`).

## 0. De-identify the inputs (always first)
Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Any operative
**named in a prior incident / near-miss** in the inputs is scrubbed to a **role label**;
distributed copies use role labels. The **duty-holders the user supplies for the CPP record**
(principal contractor, CDM construction manager, site manager) **stay named** — a legitimate
contractual record, not leaked PII (the §2 exception).

## 1. The GATE — refuse a generic "a building site"
No CPP is produced until **a named project (Q1)**, **≥1 significant activity (Q4)**, and **the
contractor configuration (Q2)** are captured. A generic request is refused; never invent a
project, an activity, or a duty-holder (record `[GAP]`).

## 2. Build the proportionate CPP (`KB-SNIP-CPP-STRUCTURE`)
A CPP is **proportionate to the project's risk** — a small single-contractor refurb's plan is
short; a multi-contractor new-build's is fuller. Build, scaled to the named project:
1. **Project description & programme** — the named project, scope, duration, key dates.
2. **Management & arrangements** — duty-holders & responsibilities (Reg 12/13), induction,
   consultation, supervision, **emergency arrangements**, **welfare**.
3. **Site rules** — the site-specific rules everyone on site must follow.
4. **Significant risks & controls by activity** — see step 3 (the core lever).
5. **Notification status (F10)** — see step 4.
6. **Review schedule** — the CPP is reviewed/updated through the project (Reg 12(3)–(4)).

## 3. Significant risks & controls by activity (the hierarchy-of-controls lever)
For each significant activity from Q4 (the Schedule 3 set: work at height · excavation/ground
works · demolition · lifting operations · confined spaces · work near water/services · hot
works):
1. Score the activity's risk via `risk_matrix.load_matrix(config)` + `risk_matrix.score(...)`
   (default 5×5; the band is the engine's).
2. Propose controls and **apply `KB-SNIP-HOC`** — rank Elimination → Substitution →
   Engineering → Administrative → PPE; call `controls.rank_controls` +
   `controls.validate_treatment`.
3. **Work at height: collective protection LEADS.** Edge protection, MEWPs, nets, or
   eliminating the at-height task rank above personal fall-arrest. If `ppe_admin_only` is
   `True` (e.g. "operatives to wear harnesses" with no collective protection), the Workflow
   **must** add a higher-order collective control **or** record an explicit justification — a
   **PPE-led work-at-height control as the headline is a defect the Critic/QA pass catches**.
   This is doubly load-bearing in construction, where "harnesses + a briefing" is the classic
   under-control.
4. **Re-score residual** via `risk_matrix.score` + `risk_matrix.residual_delta`; a residual
   High/Critical flags a hold-point or further controls.

## 4. Notification status (F10 / Reg 12)
State the F10 / Reg 12 notification position from Q3: a **notifiable** project (>30 working
days with >20 workers simultaneously, or >500 person-days) **must state the F10 / Reg 12
duty** — a notifiable project whose CPP omits it is a **regulatory-citation defect**. A **sole
contractor still owns the CPP under Reg 12(2)** — the duty is never excused.

## 5. CDM-chain cross-reference + assumptions / `[GAP]` (loose coupling, D-06)
- Emit the **one-line cross-reference** to the **PCI (Reg 4)** the CPP consumes and the **H&S
  File (Reg 12(5))** it feeds, with their place in the **Reg 4 → 12 → 12(5)** chain — sourced
  from `KB-SNIP-CONSTRUCTION-CLAUSE-MAP`, **without assuming a sibling skill ran**.
- **PCI is an OPTIONAL input** (Q5). If supplied, pull it in. If absent, **flag the Reg 4 gap
  as `[GAP]`** and list the **assumptions** the plan proceeds on — never invent the missing
  input.

## 6. SMART actions (named owners + dates)
For every control that is an action, produce a SMART action (specific, measurable, assignable,
relevant, time-bound — ISO due date). Call `smart_actions.validate_register`; any action
missing an owner, a valid date, a measure, or a hazard link is invalid (no anonymous actions,
no "ASAP").

## 7. Jurisdiction grounding
- **UK** — `KB-REG-CDM2015` (Reg 12(1)–(4), Schedule 3, HSE L153).
- **US** — `KB-REG-OSHA1926` (29 CFR 1926 Subpart C).
- **India** — defers to `hse-india` / `bocw-compliance`, **mandatory state detection**; emit a
  literal `[GAP]` where a BOCW state form/return is owed — **never a minted national form
  number**.

## 8. Validate + assemble
Validate against `references/QUALITY_CHECKLIST.md`, run the **mandatory SME Review &
Sign-off** (`references/sme-review.md`), then assemble the branded CPP report
(`assets/construction-phase-plan.report.json`) via the SKILL.md Output format section. The SME
review is decision-support that **precedes — never replaces** — the human competent-person
review; it never claims competent-person approval on this statutory-adjacent plan.
