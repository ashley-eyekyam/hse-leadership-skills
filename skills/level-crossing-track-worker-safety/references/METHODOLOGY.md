# Methodology — level-crossing-track-worker-safety

The domain method this skill applies. It produces a defensible safe-system-of-work for a
named level crossing and/or on-or-near-the-line track work, whose primary controls sit at
the higher orders of two engineered hierarchies — not at signage or a lookout — and which
**records** the user's ALCRM band rather than inventing it. Ground every step in
`KB-REG-LX-TRACKWORKER`, `KB-SNIP-LX-HIERARCHY` and `KB-DATA-ALCRM-BANDS`; rank every
control through `controls.py` + `KB-SNIP-HOC`; score residual risk on `risk_matrix.py`
(5×5); close every `[GAP]` with `smart_actions` (named **role** owner + due date).

## Step 0 — De-identify first (CONV-7)
Run the de-id scrub before any analysis (`references/deid-checklist.md`). Scrub COSS /
lookout / PICOP / engineering-supervisor / crossing-keeper names and any Sentinel number to
role labels; suppress any `<5` incident cell on a named crossing/corridor. The
re-identification key stays in a separate access-controlled artifact.

## Step 1 — Record the scope (refuse on vague)
From the intake (`references/intake.md`): the task type (crossing / track work / both), the
**named** crossing or work site (refuse a generic "a level crossing"), the crossing type
and/or activity, the line status (open vs line-blockage/possession), and the jurisdiction.

## Step 2 — Record the ALCRM band (never invent or recompute)
If the user supplies an ALCRM individual/collective band from their licensed model output,
**record it** and use it to prioritise the crossing for remediation. If they do not, the
band is **`[GAP]`** — **never invent, recompute, or hard-code a band** (the band threshold
values are the licensed RSSB/NR model output, `KB-DATA-ALCRM-BANDS`). The remedial hierarchy
in Step 3 applies regardless of whether a band was supplied.

## Step 3 — Rank crossing controls: the remedial hierarchy
For a crossing task, rank every control through the level-crossing remedial hierarchy and
**lead with the highest order that is reasonably practicable**:

1. **Closure** — eliminate the crossing.
2. **Grade separation** — bridge / underpass so road and rail do not cross at level.
3. **Engineering** — barriers / obstacle detection / MSL (Miniature Stop Light) /
   full-barrier protection.
4. **Sighting / signage / administrative** — **last**, only where a higher order is not
   reasonably practicable.

**Reject** a treatment whose lead control is new signage / admin while closure, grade
separation, or engineering is reasonably practicable — record the higher-order option and
justify (with a SMART action) if it is genuinely not reasonably practicable. "Controlled it
with a sign" is the indefensible output this method exists to prevent.

## Step 4 — Rank track-work controls: the protection hierarchy
For a track-work task, rank every control through the track-worker protection hierarchy and
**lead with the highest order that is reasonably practicable**:

1. **Separation** — green-zone working / line blockage / possession (work with no trains
   running).
2. **Safe systems of work (SSOW)** — a planned, authorised system for the task.
3. **Warning** — TOWS (Train Operated Warning System) / other warning systems.
4. **Lookout-only** — **last resort**, only where no higher protection is reasonably
   practicable; red-zone working is minimised.

**Reject** a system whose lead control is a lookout alone while separation (green-zone /
line blockage / possession) is reasonably practicable. A lookout is not a substitute for
keeping people and trains apart.

## Step 5 — Competence (COSS / Sentinel)
Confirm the safety-critical roles — **COSS** (Controller of Site Safety), lookout, PICOP,
engineering supervisor, crossing keeper — are appointed and competent (Sentinel framing),
named **by role** only. An unfilled safety-critical accountability is the indefensible
copy-paste output.

## Step 6 — Significant change (CSM-RA)
Where altering a crossing/asset is a significant change, apply the CSM-RA significance test
+ the three risk-acceptance principles + the independent AsBo (`KB-REG-CSM-RA`); change
specifics are `[GAP]` until supplied.

## Step 7 — Residual risk + SMART actions
Score residual risk on the 5×5 matrix after the lead controls are applied (`risk_matrix.py`).
Close every `[GAP]` (the ALCRM band, the NR/L2/OHS/019 issue/date, site specifics, any
not-reasonably-practicable justification) with a SMART action (`smart_actions`) carrying a
named **role** owner and a due date — never an invented value.

## Step 8 — India deferral (CONV-8)
For India: cite the Railways Act 1989 / Commissioner of Railway Safety framing; **state
detection is mandatory**; defer state-specific content to the `hse-india` engine; **no
national form number is invented** → `[GAP]` (`KB-REG-IN-RAIL`).

## Step 9 — Validate + render
Validate against `references/QUALITY_CHECKLIST.md`, run the SME Review & Sign-off, then
render via the Output format section (clone the `hse-rail.report.json` template; compose the
12 block types — CONV-11).

## Citation discipline (D-03 — `regulatory_citation_accuracy` is a HARD-fail dimension)
- Cite NR/L2/OHS/019 + ORR level-crossing strategic-risk guidance + LXRMTK **by reference**;
  never reproduce the text. The NR/L2/OHS/019 issue/date is `[ASSUMED A3]` → `[GAP]`/SME-confirmed.
- Embed ALCRM band **labels and the concept only** — never the proprietary threshold values.
- ROGS SI 2006/599 and CSM-RA Reg (EU) 402/2013 are framing references (where a significant
  change applies) — cite the instrument, not its full text.
