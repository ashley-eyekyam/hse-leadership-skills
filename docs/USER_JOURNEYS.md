# User Journeys — chaining skills for real work

The [User Manual](USER_MANUAL.md) shows you how to **set up and run one skill**. This
guide shows you how to **chain several skills** to get a real HSE task done end to end —
because most safety work is a sequence, not a single document.

Each card below is **situation-first**: a named situation, the ordered chain of skills,
*why* that order, the **handoff** at each step (what one skill produces that the next
skill consumes), a sample opening prompt per step, and links to each skill. These are
recipes — not full transcripts. Adapt the prompts to your real (de-identified) facts.

> **Decision-support only.** Every artifact in every chain is a draft for competent-person
> review and sign-off. See [`DISCLAIMER.md`](../DISCLAIMER.md).

**Read by role:** frontline & supervisors → Journeys 2, 5. HSE officers/managers →
Journeys 1, 3, 4, 5. Executives/board → Journey 4. Process-safety engineers → Journey 6.
India compliance leads → Journey 7.

---

## Journey 1 — The incident-learning loop

**Situation:** something happened (an injury, a near miss, a process upset) and you need to
turn it into durable, systemic improvement — not just a closed file.

**Chain:** [`incident-investigation`](../skills/incident-investigation/) →
[`capa-manager`](../skills/capa-manager/) → [`sop-writer`](../skills/sop-writer/) →
[`toolbox-talk`](../skills/toolbox-talk/) → [`board-safety-report`](../skills/board-safety-report/)

**Why this order:** investigate first (de-identified, evidence-based, RCA reaching systemic
causes) so the corrective actions are aimed at the real cause; manage those actions to
closure; bake the surviving control into a procedure; brief the crew on the change; then
roll the lesson up to leadership.

**Handoffs:**
- *investigation → capa-manager:* the investigation's **CAPA register** (cause-linked
  actions with owners and dates) is the input `capa-manager` ingests and tracks to closure.
- *capa-manager → sop-writer:* a procedural corrective action becomes the **SOP/SWP** that
  embeds the new control into routine work.
- *sop-writer → toolbox-talk:* the new procedure's key steps become the **briefing** the
  crew receives before the next job.
- *capa-manager → board-safety-report:* overdue/closed CAPA status + the systemic theme
  feed the **board narrative**.

**Opening prompts:**
1. `Investigate a lost-time hand injury on the Line 4 press: a worker removed the fixed guard to clear a jam and the press cycled. Use ICAM and check reportability.`
2. `Take the CAPA register from this investigation and manage it: owners, due dates, status, and verification of effectiveness.`
3. `Turn the new guard-interlock control into an SOP for clearing jams on the Line 4 press, frontline audience, review annually.`
4. `Write a 4-minute toolbox talk on the new jam-clearing procedure for the Line 4 crew.`
5. `Summarise this incident and its CAPA status for the board: systemic theme, HiPo/SIF relevance, action visibility.`

---

## Journey 2 — High-risk task planning

**Situation:** a non-routine, higher-risk job is coming up (confined space, work at height,
heavy lift) and you need it planned and controlled before anyone starts.

**Chain:** [`risk-assessment`](../skills/risk-assessment/) →
[`job-safety-analysis`](../skills/job-safety-analysis/) →
[`permit-to-work`](../skills/permit-to-work/) → [`toolbox-talk`](../skills/toolbox-talk/)

**Why this order:** assess the activity's risk and controls first; break the job into steps
with per-step hazards; gate the high-risk steps behind a permit; brief the crew last, on the
day, with the agreed controls fresh.

**Handoffs:**
- *risk-assessment → job-safety-analysis:* the assessment's **hazards and ranked controls**
  seed the per-step JSA so the steps inherit the agreed controls.
- *job-safety-analysis → permit-to-work:* the JSA's high-risk steps + controls become the
  **permit conditions** (isolation, gas test, sign-off).
- *permit-to-work / JSA → toolbox-talk:* the permit conditions and step controls become the
  **pre-task briefing**.

**Opening prompts:**
1. `Risk assessment for confined-space entry to clean tank T-402, Plant 3. Own workers and contractors. 5x5 matrix, baseline.`
2. `Build a JSA for that confined-space entry, step by step, carrying the controls from the risk assessment.`
3. `Draft the permit-to-work conditions for this entry: isolation, gas testing, standby, sign-off, close-out.`
4. `Write a toolbox talk for the entry crew covering the permit conditions and the top three controls.`

---

## Journey 3 — Audit & assurance

**Situation:** you need to audit a process or system against criteria and convert the
findings into tracked, risk-rated action — not a report that sits on a shelf.

**Chain:** [`safety-audit`](../skills/safety-audit/) →
[`capa-manager`](../skills/capa-manager/) →
[`board-safety-report`](../skills/board-safety-report/)

**Why this order:** audit against the criteria with objective evidence; turn each
nonconformity into a managed corrective action; report assurance status upward.

**Handoffs:**
- *safety-audit → capa-manager:* the audit's **nonconformities** (each a smart_actions-validated
  finding) are the register `capa-manager` ingests and drives to closure — the one cross-skill
  data contract these two share.
- *capa-manager → board-safety-report:* CAPA closure rate + open major NCs feed the
  **assurance narrative** to the board.

**Opening prompts:**
1. `Audit the Plant 3 permit-to-work process against ISO 45001 and our PTW checklist. Scope: issue, isolation, sign-off, close-out; hot work excluded.`
2. `Manage the nonconformities from this audit: classify, assign owners, set due dates, risk-rate, and track to closure.`
3. `Brief the board on audit assurance: conformity rate, open major NCs, CAPA progress, systemic theme.`

---

## Journey 4 — Leadership reporting

**Situation:** the board or executive team needs a defensible safety picture — leading and
lagging signals turned into insight and questions, not a data dump.

**Chain:** [`incident-rate-calculator`](../skills/incident-rate-calculator/) →
[`board-safety-report`](../skills/board-safety-report/)

**Why this order:** compute the lagging rates deterministically first (so the numbers are
auditable), then narrate them with HiPo/SIF context and the leadership questions they raise.

**Handoffs:**
- *incident-rate-calculator → board-safety-report:* the computed **TRIR / DART / LTIFR**
  (with the hours and counts behind them) become the lagging-indicator panel in the
  **board narrative**, framed as insight, not raw figures.

**Opening prompts:**
1. `Compute our annual TRIR, DART, and LTIFR: 3 recordable injuries, 1 with lost days, 290,000 hours worked, base 200,000.`
2. `Write a board safety report around these rates: trend, HiPo/SIF lens, weak signals, and the three questions the board should ask.`

---

## Journey 5 — Safe-procedure authoring

**Situation:** a recurring task needs a clear, controlled procedure your crew can actually
follow — built from the risk work, not from a blank page.

**Chain:** [`risk-assessment`](../skills/risk-assessment/) /
[`job-safety-analysis`](../skills/job-safety-analysis/) →
[`sop-writer`](../skills/sop-writer/) → [`toolbox-talk`](../skills/toolbox-talk/)

**Why this order:** establish the hazards and controls (risk assessment or JSA), embed those
controls into procedure steps, then brief the people who will run it.

**Handoffs:**
- *risk-assessment / job-safety-analysis → sop-writer:* the **controls** (ranked, with the
  residual risk) become the steps the SOP embeds — the procedure carries the control logic,
  not just task mechanics.
- *sop-writer → toolbox-talk:* the SOP's critical steps become the **briefing**.

**Opening prompts:**
1. `Build a JSA for manual print-head changeover on Press 4, frontline operators.`
2. `Turn that JSA into an SOP: purpose, roles, competencies, step-by-step controls, emergency provisions, review annually and on change.`
3. `Write a toolbox talk on the three highest-risk steps of the new changeover SOP.`

---

## Journey 6 — Process-safety study chain

**Situation:** a process unit or a significant change needs a structured process-safety study
that builds from hazard identification to layered, verifiable safeguards.

**Chain:** [`hazid-facilitator`](../skills/hazid-facilitator/) →
[`hazop-facilitator`](../skills/hazop-facilitator/) →
[`lopa-worksheet`](../skills/lopa-worksheet/) →
[`bowtie-builder`](../skills/bowtie-builder/) →
[`management-of-change`](../skills/management-of-change/)

**Why this order:** identify hazards broadly (HAZID), examine deviations node by node
(HAZOP), quantify the protection layers for the high-consequence scenarios (LOPA), visualise
the barriers around a top event (bowtie), then govern any change through MoC.

**Handoffs:**
- *hazid → hazop:* the HAZID's **hazard list** scopes the HAZOP nodes.
- *hazop → lopa:* the HAZOP's high-consequence **deviations** become the LOPA scenarios.
- *lopa → bowtie:* the LOPA's **independent protection layers** populate the bowtie's
  preventive and mitigative barriers.
- *bowtie → management-of-change:* a barrier change is governed through the **MoC** workflow.

**Opening prompts (assistive — a competent facilitator drives the real session):**
1. `Facilitate a HAZID for the new solvent-recovery skid on Unit 4: list the hazards and broad scenarios.`
2. `Run a HAZOP on the solvent-recovery feed node: deviations, causes, consequences, safeguards.`
3. `Build a LOPA worksheet for the overfill scenario from that HAZOP: initiating event, IPLs, residual risk.`
4. `Draw a bowtie for the overfill top event using the IPLs from the LOPA.`
5. `Run a management-of-change assessment for adding a high-level trip to that skid.`

---

## Journey 7 — India compliance flow

**Situation:** an Indian site needs to meet its statutory obligations — the right state form,
filed correctly, and the right accident notice when something is reportable.

**Chain:** [`india-state-form-finder`](../skills/india-state-form-finder/) →
[`factories-act-returns`](../skills/factories-act-returns/) /
[`india-accident-notice`](../skills/india-accident-notice/)

**Why this order:** detect the state and the legacy-first form you file *today* before
drafting anything — the form, rule, due date, and portal are state-specific; only then draft
the return or the accident notice on the correct form. State detection is mandatory.

**Handoffs:**
- *india-state-form-finder → factories-act-returns:* the finder's **(law, state) → {form,
  rule, due date, portal}** result tells the returns skill which form and deadline apply.
- *india-state-form-finder → india-accident-notice:* the same state lookup selects the
  correct **accident-notice form** and its reporting deadline.

**Opening prompts:**
1. `Which Factories Act return and accident form do we file for a factory in Maharashtra, and by when?`
2. `Draft the annual Factories Act return for this Maharashtra factory on the correct state form.`
3. `Draft the accident notice for a reportable injury at this Maharashtra factory on the correct state form, de-identified.`

---

## Where to go next

- One skill at a time → [User Manual](USER_MANUAL.md).
- The full catalog of 48 skills → [README catalog](../README.md#whats-in-the-box-the-catalog).
- Brand your outputs → [Branding](BRANDING.md).
