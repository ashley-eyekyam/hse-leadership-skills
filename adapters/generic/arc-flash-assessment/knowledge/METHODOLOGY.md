# Methodology — arc-flash-assessment (de-energize-first, engine-computed)

The domain method `arc-flash-assessment` applies. Its spine is **de-energization first**
(`KB-SNIP-DEENERGIZE-FIRST` + `KB-SNIP-HOC`): establish an **electrically safe work condition**
(NFPA 70E **Article 120**) before any reliance on arc-rated PPE; only if dead working is genuinely
not reasonable is energized work **justified explicitly** (OSHA 1910.333(a)(2) / EAWR reg 14 — never
on convenience). The incident energy, the arc-flash boundary, and the PPE category are **COMPUTED by
the deterministic IEEE 1584-2018 engine** (`arcflash.py`), never narrated. **Arc-rated PPE is the
documented last line, never the headline control.**

## 0. De-identify first (a prior arc-flash burn / electrocution incident)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. An arc-flash assessment
may cite a prior **arc-flash burn / electrocution incident** as context; a named injured worker
from that incident is **special-category health data** (GDPR Art. 9 / India DPDP). Reduce the
worker to a role label, record the incident at role level, apply `<5` small-cell suppression to any
injury breakdown, and **never circulate a named incident**. The De-identifier subagent runs FIRST;
everything downstream consumes only its scrubbed output.

## 1. Scope the named equipment (Q1)

- **Named equipment (Q1)** — the exact panel / switchgear / MCC / transformer secondary /
  distribution board + manufacturer + function. **Refuse "a panel" / "the switchroom"** (the
  specificity anchor). A missing equipment id is a `[GAP]`, never invented.

## 2. Record the de-energization decision — the de-energize-first gate (the spine)

This question is asked **first among the controls** because de-energization is the **primary
control**, not an afterthought:

- **Q2 = yes** → the assessment scopes safe isolation + verification to establish an **ESWC**
  (NFPA 70E Article 120 — identify all sources → disconnect → lock/tag → test for absence of
  voltage → ground if required). Energized PPE is **not** the headline; arc-rated PPE is at most a
  residual precaution during the isolation/verification step.
- **Q2 = no** → the task is proposed energized: capture the **energized-work justification (Q3)**
  against OSHA **1910.333(a)(2)** ("additional/increased hazard or infeasible") **or** EAWR
  **reg 14** ("unreasonable to be dead"). **A bare "production can't stop / it's quicker" is
  REFUSED** — economic convenience alone does not justify energized work. Record the justification
  verbatim and route to an **energized-work permit** (NFPA 70E Annex J).

## 3. Capture the IEEE 1584 parameters (Q4) — no invented inputs

For the incident-energy computation, capture the IEEE 1584-2018 required inputs: nominal system
voltage, available bolted fault / short-circuit current, upstream protective-device clearing time,
electrode configuration (VCB / VCBB / HCB / VOA / HOA), enclosure & gap dimensions, working
distance. **A missing required parameter is a `[GAP]` and a request for a power-system /
short-circuit study — never an invented fault current or clearing time.**

## 4. Compute incident energy → boundary → PPE category (the engine — never narrated)

Run the **`arcflash.py` engine** via the portability shim — the cal/cm² value is **computed, never
narrated**:

```python
from _shim import ensure_hse_components
ensure_hse_components(__file__)
import arcflash

result = arcflash.incident_energy(
    v_oc=400, i_bf_kA=25.0, gap_mm=32, electrode="VCB",
    working_distance_mm=455, arc_time_s=0.2, enclosure_mm=(508, 508, 508),
)
blocks = arcflash.to_report_blocks(result)   # metrics + table (+ critical callout if >40)
```

- `result["incident_energy_cal_cm2"]`, `["arc_flash_boundary_mm"]`, and `["ppe_category"]` are the
  computed headline values; `to_report_blocks()` emits the `metrics` + `table` (and a `critical`
  callout when the category is the `>40 — extreme` flag).
- The **arc-flash boundary** is the distance at which incident energy = **1.2 cal/cm²** (the onset
  of a second-degree burn). The PPE category maps the cal/cm² to an NFPA 70E band by the
  **1.2 / 4 / 8 / 25 / 40 cal/cm²** breakpoints (structure only — `KB-STD-NFPA70E`).
- **`>40 cal/cm²` flags energized work as PROHIBITED** (a blast hazard, not just thermal) — no
  table PPE applies; the control is elimination via de-energization / remote operation.

## 5. Rank the controls (the hierarchy gate) + the residual

Run the `controls` engine. The control narrative **always leads with de-energization** →
engineer the source (insulation, barriers, remote racking/operation) → administrative approach
control (limited/restricted approach boundaries per 130.4, energized-work permit, qualified
persons) → **arc-rated PPE LAST**. An arc-flash treatment that **leads with arc-rated PPE when the
task could be de-energized** (`controls.validate_treatment` returning `ppe_admin_only=True`) is a
**FLAG pushed up the hierarchy, never the headline control**. Frame the qualitative residual via
`risk_matrix` (not the arc-flash scoring path — the incident energy is the quantified consequence,
computed by `arcflash.py`).

## 6. Label content + SMART actions + report

Author the **NFPA 70E 130.5(H)** label content (nominal system voltage; arc-flash boundary;
available incident energy + working distance *or* the required PPE category; study date). Every
label-install / study-refresh / remediation action becomes a SMART action (named role owner + ISO
due date + measure), validated by `smart_actions.validate_register`. Validate the draft against
`references/QUALITY_CHECKLIST.md`, then assemble `assets/arc-flash-assessment.report.json` and run
the canonical `report-output` call.

## Jurisdiction

US NFPA 70E (2024) read with **OSHA 29 CFR 1910.333** (de-energize-first / energized-work
justification) + **1910.269** (utility T&D approach distances) is the default duty; UK/EU is
**EAWR 1989 reg 14** (the dead-working default + the live-working test) + **HSG85**. For India,
resolve the state via `hse-india` (**mandatory state detection**) per the CEA / state electricity
rules, and emit a literal `[GAP]` where a state return is owed — **never a minted national form
number**.
