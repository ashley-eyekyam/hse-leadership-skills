<!-- KB-REG-IN-BMW2016 -->
# India — Bio-Medical Waste Management Rules 2016 (legacy-first, state-PCB)

**Fragment ID:** `KB-REG-IN-BMW2016`
**What this is:** the duty → artifact **citation map** for India's Bio-Medical
Waste Management Rules 2016 (under the Environment (Protection) Act 1986) —
segregation, colour-coding, treatment, transport, and the authorisation/return
regime operated through the **State Pollution Control Boards (SPCBs)**. **This is
data, not the rules text** — a skill (or its Regulatory-Checker subagent) reads it
*after* resolving the user's state.
**What this is NOT:** a reproduction of the BMW Rules, and NOT a single nationwide
form catalogue — authorisation and the annual return operate through the **state
PCB**.

> Source: Bio-Medical Waste Management Rules 2016 (as amended) under the Environment (Protection) Act 1986 + state PCB notifications — per-row cite below · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true (amendments + state PCB notifications in flux).

**Legacy-first + mandatory state detection.** BMW authorisation, the common
bio-medical-waste-treatment-facility (CBWTF) linkage, and the annual return are
administered by the **State Pollution Control Board**; the authorisation and
return target is state-specific. An India healthcare-waste skill **resolves the
state first** (`KB-REG-IN-STATEFORMS`, mandatory) before citing any form or
portal, returns the legacy state-PCB requirement as the primary answer, and
appends any OSH-Code/EPA transition note. The detailed state form content is held
in the **`hse-india`** engine, which the skill defers to (subagent → inline →
`[GAP]` pointer); **no BMW return is ever cited as a single nationwide form
number**.

## Trigger → duty → artifact

| Trigger | Statutory duty | Artifact / instrument | Cite |
|---|---|---|---|
| Generate bio-medical waste (HCF) | Obtain authorisation from the State PCB | BMW authorisation (state-PCB form) | BMW Rules 2016; SPCB — resolve per state |
| Segregate at the point of generation | Colour-code by category (yellow / red / white-translucent / blue) | the segregation + colour-coding plan | BMW Rules 2016 Schedule I |
| Treat & dispose | Use prescribed treatment or a CBWTF; barcode/track | the treatment / CBWTF disposal record | BMW Rules 2016 Schedule I/II |
| Annual reporting | File the annual report to the State PCB | BMW annual report (state-prescribed form/timing) | BMW Rules 2016; SPCB — `[GAP]` per state |
| Accident involving BMW | Report the accident to the prescribed authority | accident report | BMW Rules 2016 — resolve per state |

## Verified anchors vs `[GAP]`
- **Verified anchor:** the **four-colour segregation scheme** (yellow / red /
  white-translucent / blue) and the **State-PCB authorisation** requirement are
  concrete — cite them.
- **`[GAP]` (resolve per state, never invent):** the authorisation **form id**,
  the annual-report format and due date, and the CBWTF particulars vary by **state
  PCB** notification — emit a literal `[GAP]` and route to the State PCB via the
  **`hse-india`** engine. The citation grader is row-blind; a fabricated state form
  value passes the automated gate, so honesty is enforced by the `[GAP]` marker +
  the per-skill no-fabrication eval + the SME FLAG.

## How the skills use this fragment
- India healthcare / infection-control skills ground here for the segregation /
  colour-coding / authorisation / annual-return duty set; they **resolve the state
  first** (`KB-REG-IN-STATEFORMS`) and defer state-specific form content to the
  **`hse-india`** engine, marking any unverified value `[GAP]`.

## Transition note
Amendments to the BMW Rules and any consolidation under broader environmental
codes are state-implemented; legacy state-PCB authorisations and returns remain
valid. Offer any consolidated mapping only as an explicit transition mode (warn the
form/portal may not be live).
