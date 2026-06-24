# Methodology — site-specific health-and-safety induction design

The domain method `induction-pack` applies: lay the **mandatory induction baseline**, **layer the
named site's** real hazards, emergency arrangements and rules onto it, build a
**competence-verification record** proving each inductee understood the content, and schedule
**refreshers by role-risk**. The induction is **content assembly, not a calculation** — there is
no scoring engine; `smart_actions` is the only A7 script call (the refresher schedule).

The core lever (the single thing that makes this defensible, not boilerplate): **every induction
topic is tied to a named site arrangement, and every site-specific hazard carries its control
ranked up the hierarchy of controls — a generic induction with no named site/hazards is refused.**

**Grounded in:**
- `KB-SNIP-INDUCTION-BASELINE` — the **mandatory induction-topic baseline** (emergency · welfare
  & first aid · site rules · site-specific hazards & controls · incident/concern reporting) the
  named site's specifics are layered onto. The baseline is the floor, never the whole pack.
- `KB-DATA-COMPETENCE-LEVELS` — the shared **4-level competence scale** (aware → trained →
  competent → expert), each level with an **evidence test**; sets the **verification level** each
  inductee/role must reach. Quote its `source`+`year`. (The required level is set by the role's
  task risk, never downgraded to "pass" an inductee.)
- `KB-STD-ISO45001` — clauses **7.2 (competence) & 7.3 (awareness)** — the binding requirement
  that workers are competent and aware of the hazards and the arrangements that affect them.
- `KB-SNIP-HOC` — the hierarchy of controls, applied to **every site-specific hazard's control**
  in the induction (never a PPE-only line) and the refresher remediation.
- `KB-SNIP-OPS-CLAUSE-MAP` — the bundle clause cross-walk (induction = 7.3 awareness); route a
  user who asks for the wrong artifact for a clause to the owning sibling.
- The jurisdiction legal-induction baseline (Q5): UK MHSWR 1999 reg. 10/13 · US OSHA orientation
  duties (General Duty Clause + standard-specific) · India Factories Act 1948 s.111A (defers to
  `hse-india`; no national form number minted).

## The steps

### 1. De-identify the inputs (FIRST)
Before any drafting. Inductee names, contacts, and any health/medical detail are scrubbed to
stable role labels per the `deid` block + `references/deid-checklist.md`. **Inductee names belong
only on the legitimate signed competence-verification record**; any **widely distributed** copy of
the pack uses **role labels**, and **no inductee health/medical detail** enters the pack at all.
The de-id block warns before any name enters a shared artifact; the re-identification key is held
separately. Everything downstream consumes only the scrubbed text.

### 2. Resolve the audience + the named site
From intake Q1 (audience) and Q2 (named site). **Refuse a generic site** — there is no induction
without a named site. The **contractor cohort** (Q1 = contractors) branches to pull **site-rules +
permit-to-work awareness** and follows prequalification (`contractor-prequalification` #16 —
induction follows prequalification). Visitors get a shortened baseline; agency/temporary get the
permanent-starter baseline scaled to their tasks.

### 3. Lay the mandatory baseline
Apply `KB-SNIP-INDUCTION-BASELINE`: **every** induction covers the five baseline topics —

| # | Baseline topic | Must cover |
|---|---|---|
| 1 | **Emergency arrangements** | alarm, evacuation routes, **named muster point(s)**, what to do on discovering an incident (ties to `emergency-response-plan` #15) |
| 2 | **Welfare & first aid** | first-aiders, first-aid location, welfare facilities, reporting feeling unwell |
| 3 | **Site rules** | access/egress, PPE rules, traffic management, permit/PTW awareness (contractor cohorts get the PTW-awareness branch) |
| 4 | **Site-specific hazards & controls** | the real hazards of *this* site, each with its control ranked via `KB-SNIP-HOC` — never generic |
| 5 | **Incident & concern reporting** | how to report a hazard, near-miss, or concern, and the no-blame expectation |

The baseline is the floor — the pack is **not** done at the baseline.

### 4. Layer the named site's specifics (the core lever)
For every baseline topic, tie it to **this site's** real arrangement: the actual named muster
point, the real traffic-management plan, the specific permit systems, the named hazards of *this*
location. Each **site-specific hazard carries its control ranked via `KB-SNIP-HOC`** (Elimination
→ Substitution → Engineering → Administrative → PPE) — never a generic line, never a PPE-only
treatment without a higher-order option and a justification. A topic with no named site
arrangement is a `[GAP]`, never filled with boilerplate. **A warehouse induction and an
oil-terminal induction must differ on their named hazards and arrangements** — this is the
specificity test.

### 5. Build the competence-verification record
Every induction produces a **competence-verification record** — per inductee, **role-labelled in
any shared copy**, proving the content was understood. Set the **verification level** required for
the role on `KB-DATA-COMPETENCE-LEVELS` (aware / trained / competent / expert — by the role's task
risk, never downgraded) and the **verification method** from Q6 (questions/quiz · supervised
sign-off · competence demonstration). **An induction with no competence-verification record fails
the quality gate** (the repudiation defence: proof of understanding, not just attendance).

### 6. Schedule refreshers by role-risk
Turn the refresher cadence into **SMART actions** via `smart_actions.validate_register` — each
**specific, measurable, assignable (named owner), relevant, time-bound (ISO due date)**.
Higher-risk roles refresh more often (e.g. annual for high-hazard tasks; on change of site rules,
process, or after an incident). Any refresher missing an owner or a valid date is invalid and must
be fixed — no anonymous actions, no "ASAP".

### 7. Validate, then assemble the branded report
Run the `references/QUALITY_CHECKLIST.md` gate, then build `report.json` from
`assets/induction-pack-report.template.json` and render via the shared engine (the `report-output`
block in `SKILL.md`).

## Contractor-vs-permanent topic map
- **Permanent new starters** — full baseline + the role's site-specific hazards + the verification
  level for the role; refreshers on the role-risk cadence.
- **Contractors** — the baseline **+ site rules + permit-to-work awareness** (the PTW branch),
  scoped to the work package; induction **follows** `contractor-prequalification` (#16). Verify
  before site access.
- **Visitors** — a shortened baseline (emergency + escort rule + the hazards they could encounter)
  + a signed acknowledgement; no task competence required.
- **Agency / temporary** — the permanent-starter baseline scaled to the tasks they will do, with
  the verification level for those tasks.
