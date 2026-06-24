# Offshore Safety Case assembly — `offshore-safety-case`

**Assistive:** structures the safety-case argument and records the duty-holder's content; **never produces the safety case autonomously**, never computes/invents QRA, never asserts a barrier/SCE effective without performance-standard evidence, and never emits "accepted/approved/authorised" language (acceptance is the competent authority's — HSE + OPRED — act).

## Regime (current vs legacy)
- **Current:** the Offshore Installations (Offshore Safety Directive) (Safety Case etc.) Regulations 2015 — **SI 2015/398** ("SCR 2015"), implementing the EU Offshore Safety Directive 2013/30/EU.
- **Legacy:** the Offshore Installations (Safety Case) Regulations 2005 ("SCR 2005") — named only as the superseded reference; never cited as the live duty.

## Elements (KB-REG-OFFSHORE-SCR — SI 2015/398 Schedule 6/7)
1. **MAH identification** — major-accident hazards & major-accident scenarios (from the duty-holder's PHA / HAZID / HAZOP / bowtie inputs — not a generic substance-class list).
2. **SEMS** — the Safety & Environmental Management System description.
3. **CMAPP** — the corporate major-accident-prevention policy.
4. **ALARP demonstration** — risks reduced ALARP (consequence/likelihood; QRA external — the skill **records** the demonstration with provenance, it does **not** compute the numbers).
5. **SCE register + performance standards** — the safety-and-environmental-critical elements and the performance standards they must meet (the *test* the duty-holder evidences).
6. **Independent verification scheme** — the verifier and the verifier findings against the SCE performance standards.
7. **Emergency response (EER)** — **cross-referenced** to the sibling `marine-emergency-response` (MAR-03) plan; recorded here, never rebuilt.

## Output shape — the goal-structured argument
Assemble a **claim → sub-claim → argument strategy → evidence reference → status** map:
- **Top claim:** major-accident hazards on the named installation are controlled so that risks to personnel and the environment are reduced ALARP.
- Each sub-claim (hydrocarbon release controlled · fire & explosion controlled · structural integrity assured · EER adequate · environmental MAH controlled) carries an argument strategy and a **named evidence reference** (bowtie BT-n, HAZOP node, FEA report, SCE performance standard + verifier finding, the MAR-03 EER plan).
- A sub-claim with no supplied evidence is **`Open / [GAP]`**, never "Supported".

## Discipline (load-bearing — the assistive boundary)
- **Never invent** a scenario, ALARP number, consequence distance, MAH frequency, or QRA result — record `[GAP]` for unsupplied elements/figures; external figures are recorded **with their provenance**.
- **Never assert a barrier / SCE effective** without a cited performance-standard evidence reference or a verifier finding — downgrade an un-evidenced "barrier is effective" to `[GAP]`.
- **Never compute** MAH frequencies or consequence numbers — the skill deliberately does NOT use `incident_rates` / `risk_matrix` to generate them.
- HoC-rank the risk-reduction measures (`controls`); track the gap-closure actions with named role-owners + ISO dates (`smart_actions`).
- **Never emit "accepted / approved / authorised" language** — the output is the structured argument that PRECEDES competent-authority acceptance.
- Carry the assistive disclaimer: the AI structured the argument; the analysis and the QRA were performed externally and the safety case must be reviewed by a competent person and accepted by the competent authority.
