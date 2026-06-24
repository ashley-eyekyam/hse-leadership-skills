# Methodology — machine-guarding-assessment (guard-by-hazard-zone, engineering-control-led)

The domain method `machine-guarding-assessment` applies. Its spine is the **engineering-control-led
guard/device selection** per danger zone (`KB-SNIP-GUARD-SELECTION` + `KB-SNIP-HOC`), inside the
**ISO 12100 three-step method** (`KB-STD-ISO12100-14120`): inherent safe design → safeguarding →
information for use. A mechanical-zone control left **PPE-only or admin-only** ("operators to keep
hands clear / wear gloves") is **never** the headline control — it is a **FLAG pushed up the
hierarchy**. The guard-selection order is a **cited decision rule run against the access-frequency
rule**, verified by the deterministic `controls` engine.

## 0. De-identify first (a prior amputation / crush incident)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. A guarding assessment
routinely cites a prior **amputation / crush incident** as evidence for a danger zone; the named
injured operator is **special-category health data** (GDPR Art. 9 / India DPDP). Reduce the
operator to a role label, record the incident at role level, apply `<5` small-cell suppression to
any injury breakdown, and **never circulate a named incident**. The De-identifier subagent runs
FIRST; everything downstream consumes only its scrubbed output.

## 1. Capture the named machine and the danger zones (Q1 → Q3)

- **Named machine (Q1)** — the exact machine / line / cell + manufacturer/model + function.
  **Refuse "a machine" / "the factory" / "looks guarded"** (the specificity anchor). A missing
  machine is a `[GAP]`, never invented.
- **Machine type & motion (Q2)** and **danger zones (Q3)** — per OSHA 29 CFR 1910.212(a) /
  ISO 12100: point of operation · in-running nip point · rotating parts · power-transmission
  (shaft/belt/gear — 1910.219) · flying chips/sparks · crush/trap point. Each zone is assessed
  individually; "guard all moving parts" is refused.

## 2. Record existing safeguarding & condition (Q4)

For each zone, record the guard/device fitted today and its condition. **A defeated, missing, or
overridden guard is an immediate high-priority finding** (a bridged interlock, a removed fixed
guard, a propped gate). Never assume a zone is guarded because it "looks guarded".

## 3. Select the guard/device per zone — the engineering-led gate (the spine)

For **each** danger zone, after Step 1 (design out the hazard — ISO 12100), select the
**highest-order** safeguarding measure the task allows from `KB-SNIP-GUARD-SELECTION`, governed by
the **access-frequency rule**:

1. **Fixed guard** — access not needed in normal operation (preferred).
2. **Interlocked movable guard** — regular access needed; opening stops/isolates the machine.
3. **Presence-sensing device** (light curtain, mat) — frequent access; sensing stops the motion.
4. **Two-hand / hold-to-run control** — hands kept out of the zone during the hazardous motion.
5. **Trip device** — complementary measure for the residual.

Then run the engine:

```python
from controls import rank_controls, validate_treatment   # via scripts/hse_components symlink
verdict = validate_treatment(controls_for_this_zone)      # {passed, ppe_admin_only, highest_order, flag, ranked}
```

- If an engineering-led guard/device is selected and a **residual** survives → re-score (step 4).
- If the treatment is **PPE/administrative only** (`ppe_admin_only=True`) — e.g. "operators to keep
  hands clear / wear gloves" with no fixed/interlocked guard — this is a **controls FLAG**. **Emit
  the flag, push the control up the hierarchy, NOT a PPE-led row.** This is the failure mode the
  skill exists to prevent: a mechanical hazard zone "controlled" by operator care.

## 4. Re-score the residual (risk_matrix)

Re-score each zone's **residual risk** after the selected guard via `risk_matrix` (the deterministic
5×5 bands), so the register carries the pre- and post-guard risk and a hierarchy-ranked residual.

## 5. Interaction modes + maintenance LOTO (Q5)

For each interaction mode (normal / setting / cleaning / **maintenance**), author the per-mode
controls. **When the maintenance mode is in scope, cross-reference `KB-REG-LOTO`** for energy
isolation: identify every energy source (electrical / stored mechanical / hydraulic / pneumatic /
thermal / gravity) → isolate → **verify zero energy** before access. A guarding assessment that
omits the maintenance-interaction isolation control is incomplete.

## 6. SMART actions + report

Every guard-install / guard-repair / LOTO-procedure action becomes a SMART action (named role owner
+ ISO due date + measure), validated by `smart_actions.validate_register`. Validate the draft
against `references/QUALITY_CHECKLIST.md`, then assemble `assets/machine-guarding-assessment.report.json`
and run the canonical `report-output` call.

## Jurisdiction

US OSHA 29 CFR 1910 Subpart O (1910.212 / 1910.219) is the default duty; UK/EU is **PUWER 1998
Regs 11–12** + ISO 12100/14120. For India, ground on **Factories Act 1948 §21 (fencing of
machinery)**, resolve the state via `hse-india` (**mandatory state detection**), and emit a literal
`[GAP]` where a state form/return is owed — **never a minted national form number**.
