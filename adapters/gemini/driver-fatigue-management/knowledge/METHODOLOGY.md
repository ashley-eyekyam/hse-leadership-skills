# Methodology — driver-fatigue-management (schedule-redesign-first, engine-computed)

The domain method `driver-fatigue-management` applies. Its spine is **schedule/roster redesign
first** (`KB-SNIP-FATIGUE-FRMS` + `KB-SNIP-HOC`): fatigue is a **scheduling and roster-design
problem before it is a "stay alert" problem**, so the controls lead with journey planning, roster
redesign, and built-in rest (a Fatigue Risk Management System — FRMS); a "stay alert" briefing or an
in-cab fatigue-detection gadget treated as the headline control is a **FLAG pushed up the
hierarchy**. The **hours-of-service compliance flags are COMPUTED by the deterministic `fatigue.py`
engine** (FMCSA 49 CFR 395.3 + EU 561/2006), never narrated; the **fatigue index is rendered as a
clearly-flagged ADVISORY metric**, never a regulatory threshold.

## 0. De-identify first (HIGHEST tier — driver medical / OSA / sleep-disorder)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. This is the **highest
de-id tier** in the logistics pack: the driver's name, **CDL / licence number, DOT-medical /
fitness certificate, obstructive-sleep-apnoea (OSA) / sleep-disorder note, and any fatigue-event /
sickness-absence count** are special-category occupational-health data (GDPR Art. 9 / India DPDP /
OSHA 29 CFR 1904.29 privacy cases). Reduce every driver to a stable **role label** ("Driver A"),
apply **`<5` small-cell suppression** (with the secondary back-calc guard) to any fatigue-event /
sickness breakdown, and **never circulate a named driver's medical detail or the re-identification
key**. The De-identifier subagent runs FIRST; everything downstream consumes only its scrubbed
output. **The re-identification key is held SEPARATELY (an instruction to the competent person) — the
skill emits NO key file.**

## 1. Scope the named fleet / operation (Q1)

- **Named fleet / operation (Q1)** — the exact fleet / route / depot / operation + its function
  (e.g. "night-trunk fleet, route R-204, Midlands depot"). **Refuse "our drivers" / "the fleet"**
  (the specificity anchor). A missing operation id is a `[GAP]`, never invented.

## 2. Resolve the jurisdiction & rule-set (Q2)

The jurisdiction selects the HOS rule-set the engine applies:

- **USA** → FMCSA Hours-of-Service, **49 CFR Part 395** (`fmcsa_compliance`).
- **EU / UK** → **EU Regulation (EC) 561/2006** drivers' hours (`eu561_compliance`); GB domestic
  drivers' hours read alongside EU 561.
- **India** → resolve the **state** via `hse-india` (**mandatory state detection**) per the Motor
  Transport Workers Act 1961 / Factories-Act-as-warehouse framing, and emit a literal `[GAP]` where
  a state return is owed — **never a minted national form number** (CONV-8 deferral).
- `KB-REG-FMCSA-HOS` is the **combined US+EU** citation map (a single fragment, never split); the
  numeric limits are LOCKED constants in `fatigue.py`, not pasted from the fragment.

## 3. Capture the driver duty log (Q3) — no invented hours

For the HOS computation, capture the shift as an ordered list of `{status, hours}` segments
(`status` ∈ `driving | on_duty | off_duty | sleeper`; `hours` a float). **A missing or vague log is
a `[GAP]` and a request for the ELD / tachograph download — never an invented driving hour, rest
segment, or duty figure.** The engine fails loud (`FatigueInputError`) on a negative duration, a
single-day total > 24 h, or a malformed segment — never a silent clamp.

## 4. The multi-day cycle & cross-shift rest `[GAP]` discipline (Q4)

This is the method's load-bearing honesty rule. The engine's multi-day rules
(`cycle_60_70h`, `restart_34h` for FMCSA; `daily_rest_11h`, `weekly_driving_56h`,
`fortnight_driving_90h` for EU 561) **default to compliant for a single-shift log only because no
multi-day breach is *detectable* — NOT because compliance is *proven***:

- The FMCSA **60/70 h cycle** and **34 h restart** require the **7-/8-day cumulative on-duty
  figure**. If the user supplies only a single shift, **record a literal `[GAP]`** (request the
  cumulative figure) — **never assert the cycle / restart compliant from one shift**.
- The EU **daily rest** is assessed from the **longest rest segment within the supplied log**; a
  **cross-shift daily-rest** claim likewise needs the cross-shift rest figure or a `[GAP]`.
- These are **intake / method** concerns, never engine work (D-01: zero new engines — there is no
  `fatigue_hos`; the reused `fatigue.py` is the only HOS engine).

## 5. Compute the HOS flags + the advisory index (the engine — never narrated)

Run the **`fatigue.py` engine** via the portability shim — the HOS flags are **computed, never
narrated**, and the two output classes are kept strictly distinct:

```python
from _shim import ensure_hse_components
ensure_hse_components(__file__)
import hse_components.fatigue as fatigue

duty_log = [
    {"status": "driving", "hours": 4.5},
    {"status": "off_duty", "hours": 0.75},   # 45-min break
    {"status": "driving", "hours": 4.0},
    {"status": "on_duty", "hours": 1.0},
    {"status": "off_duty", "hours": 11.0},
]
fmcsa = fatigue.fmcsa_compliance(duty_log)                 # US — per-rule PASS/FAIL flags
eu = fatigue.eu561_compliance(duty_log, extensions_used=0) # EU — per-rule PASS/FAIL flags
idx = fatigue.fatigue_index(duty_log, time_of_day=3.0)     # ADVISORY index (advisory: True)
blocks = fatigue.to_report_blocks({"fmcsa": fmcsa, "eu561": eu, "fatigue_index": idx})
```

- The **compliance flags are the AUTHORITATIVE, primary finding** (compliance-flags-primary): each
  is a per-rule boolean where `True` == compliant. `to_report_blocks` renders the per-rule
  PASS/FAIL `table` and a `warning` callout on any breach.
- The **fatigue index is the ADVISORY, secondary metric** (advisory-index-secondary): the result
  dict carries `advisory: True` and a note that it is a transparent weighted-stressor heuristic,
  NOT a regulatory threshold and NOT a validated biomathematical model. Render it under an explicit
  "advisory" label; **never present the index as a compliance verdict**.
- A `[GAP]` from §4 is carried into the report's assumptions/gaps — **never** back-filled by the
  engine's single-shift default.

## 6. Rank the controls (the hierarchy gate) + the residual

Run the `controls` engine. The control narrative **always leads with schedule/roster redesign** →
journey-plan / route redesign and built-in rest (FRMS) → engineered backstops (e.g. in-cab
fatigue-detection as a backstop, not the headline) → administrative ("stay alert" briefings, break
reminders) **LAST**. A fatigue treatment that **leads with a driver-alertness briefing or an in-cab
gadget** (`controls.validate_treatment` returning `ppe_admin_only=True` — the alertness-led FLAG) is
a **FLAG pushed up the hierarchy, never the headline control** (`KB-SNIP-FATIGUE-FRMS`). Frame the
qualitative residual via `risk_matrix` (the HOS compliance flags are the quantified finding,
computed by `fatigue.py`).

## 7. SMART actions + report

Every roster-redesign / [GAP]-closure / FRMS-implementation action becomes a SMART action (named
role owner + ISO due date + measure), validated by `smart_actions.validate_register`. Validate the
draft against `references/QUALITY_CHECKLIST.md`, then assemble
`assets/driver-fatigue-management.report.json` and run the canonical `report-output` call. The
report keeps the **compliance-flags-primary / advisory-index-secondary** split visible to the
reader.

## Jurisdiction

US **FMCSA 49 CFR Part 395** (`fmcsa_compliance`) is the US duty; EU/UK is **EU Reg (EC) 561/2006**
(`eu561_compliance`) with GB domestic drivers' hours read alongside. For India, resolve the state
via `hse-india` (**mandatory state detection**) per the Motor Transport Workers Act 1961 / Factories
Act, and emit a literal `[GAP]` where a state return is owed — **never a minted national form
number**.
