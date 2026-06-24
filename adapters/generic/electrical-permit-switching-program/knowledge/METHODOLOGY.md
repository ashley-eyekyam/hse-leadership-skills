# Methodology — electrical-permit-switching-program (de-energize-first, switching-sequence-driven)

The domain method `electrical-permit-switching-program` applies. Its spine is **de-energization
first** (`KB-SNIP-DEENERGIZE-FIRST` + `KB-SNIP-HOC`) realised through the **ordered switching
sequence** (`KB-SNIP-SWITCHING-SEQUENCE`): isolate → **prove dead** → **earth** → sanction the work
via the correct **safety document** → restore. Establish an **electrically safe work condition**
(NFPA 70E **Article 120**) before any work; only if dead working is genuinely not reasonable is live
work **justified explicitly** (OSHA 1910.333 / EAWR — never on convenience). **Work authorised on
apparatus isolated but not proven dead, or with protective earthing omitted where the procedure
requires it, is never the program — it is a FLAG pushed up the hierarchy.** The sequence is
structured method (no new engine); the controls hierarchy and the SMART register are deterministic.

## 0. De-identify first (a prior switching / electrocution incident)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. A switching program may
cite a prior **switching, electrocution, or arc-flash incident** as context; a named injured
operator from that incident is **special-category health data** (GDPR Art. 9 / India DPDP). Reduce
the operator to a role label, record the incident at role level, apply `<5` small-cell suppression
to any injury breakdown, and **never circulate a named incident**. The De-identifier subagent runs
FIRST; everything downstream consumes only its scrubbed output.

## 1. Scope the named apparatus (Q1 → Q2)

- **Named apparatus (Q1)** — the exact feeder / busbar section / transformer / RMU / switchboard +
  operating voltage + function. **Refuse "the substation" / "the switchroom"** (the specificity
  anchor). A missing apparatus id is a `[GAP]`, never invented.
- **Operating voltage & system (Q2)** — LV / HV 11 kV / HV 33 kV / HV other / mixed. The voltage
  drives the approach distances, the **protective-earthing requirement**, and the **authorisation
  level** (authorised vs senior authorised person).

## 2. Record the de-energization / isolation decision — the de-energize-first gate (the spine)

This decision is recorded **first among the controls** because de-energization + isolation is the
**primary control**, not an afterthought:

- **Work dead** → the program scopes safe isolation + verification to establish an **ESWC** (NFPA
  70E Article 120). Enumerate **every point of isolation (Q3)** for the apparatus; identify where
  **protective earthing** will be applied. PPE is **not** the headline; it is at most a residual
  precaution during the switching steps.
- **Live work proposed (Q5 branch)** → capture the **live-work justification (Q5a)** against OSHA
  **1910.333(a)(2)** ("additional/increased hazard or infeasible") **or** EAWR. **A bare "production
  can't stop / it's quicker" is REFUSED** — economic convenience alone does not justify live work.

## 3. Build the ordered switching sequence (KB-SNIP-SWITCHING-SEQUENCE) — the backbone

Build the sequence with **per-step authorisation** (authorised vs senior authorised person by
voltage):

1. **Plan & authorise.** Identify the apparatus, all points of supply, and the competent authorised
   person; issue the switching schedule under control.
2. **Isolate.** Open the isolating device(s) at every point of supply; render the isolation secure
   (lock-off / caps-and-locks) so it cannot be inadvertently re-energized.
3. **Prove dead.** Test for absence of voltage at the point of work with a proving unit verified
   before and after (the **prove-test-prove** discipline). **Work is never authorised un-proven.**
4. **Earth / ground.** Apply protective earthing/grounding where the system or procedure requires
   it (per OSHA 1910.269(n) / utility practice). **Omitting earthing where required is rejected.**
5. **Issue the safety document.** Issue a **permit-to-work** (work on dead equipment) **or** a
   **sanction-to-test** (controlled re-energization for testing) — **kept DISTINCT** — defining the
   safe zone, the precautions, and the limits.
6. **Carry out, then restore.** Work within the document's limits; on completion **cancel the
   document, remove earths, remove locks/tags**, and restore supply under the switching schedule.

## 4. Rank the controls (the hierarchy gate) + the residual

Run the `controls` engine. The narrative **always leads with de-energization + isolation** → prove
dead → earth → the **safety-document control** (permit-to-work / sanction-to-test) → **PPE LAST**. A
program that **authorises work un-proven or un-earthed where earthing is required**
(`controls.validate_treatment` returning `ppe_admin_only=True` / a lower-order-only headline) is a
**FLAG pushed up the hierarchy, never the program**. Frame the qualitative residual via
`risk_matrix`.

## 5. SMART actions + report

Every isolation / prove-dead / earthing / document-issue / restoration action becomes a SMART action
(named role owner + ISO due date + measure), validated by `smart_actions.validate_register`.
Validate the draft against `references/QUALITY_CHECKLIST.md`, then assemble
`assets/electrical-permit-switching-program.report.json` and run the canonical `report-output` call.

## Jurisdiction

US NFPA 70E (2024) **Article 120** read with **OSHA 29 CFR 1910.269** (T&D — 269(d) LOTO / 269(n)
protective grounding / 269(m) de-energizing) + **1910.333** (work practices) + **1910.147** (LOTO)
is the default duty; UK/EU is **EAWR 1989 regs 12–13** (means of cutting off supply + isolation /
working dead) + **HSG85**. For India, resolve the state via `hse-india` (**mandatory state
detection**) per the CEA / state electricity rules + line-clearance permit practice, and emit a
literal `[GAP]` where a state return is owed — **never a minted national form number**.
