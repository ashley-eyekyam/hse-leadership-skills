# Methodology — sharps-needlestick-management (engineering-first, PHI-protected)

The domain method `sharps-needlestick-management` applies. Its spine is **elimination and
safety-engineered devices first** (`KB-SNIP-SHARPS-HIERARCHY` + `KB-SNIP-HOC`): eliminate
unnecessary sharps, then engineer (safety-engineered devices, point-of-use disposal), then safe
work practices (no-recapping), with **PPE and post-exposure prophylaxis (PEP) as the documented
last lines**. A sharps treatment that **leads with "be careful / wear gloves"** where the sharp
could be eliminated or a safety-engineered device fitted is a **FLAG pushed up the hierarchy, never
the headline control**. There is **no calculation** — sharps control is a structured
engineering-control-first method over the named device inventory + the cited OSHA/EU hierarchy.

## 0. De-identify first (the highest-PHI step — source patient + injured worker)

Run the `deid` block + `references/deid-checklist.md` BEFORE any drafting. Bloodborne-pathogen
exposure data is **special-category health data (PHI)**. Scrub the **source / index patient's
identity and serostatus** (HIV/HBV/HCV — never circulated; the source-testing pathway references
"the source patient" by role only, with consent + a separate confidential record), the **injured
worker's identity, job, shift, and exposure/PEP medical record** (role-label "Worker A"; the medical
record held confidentially + separately per OSHA 1910.1030(f)), and any **patient identifier**.
Apply `<5` small-cell suppression (with secondary suppression) to every sharps-injury category.
**The skill emits NO re-identification / exposure key file** — the key is an instruction to the
competent person (held separately, access-controlled). The De-identifier subagent runs FIRST;
everything downstream consumes only its scrubbed output.

## 1. Scope the named service & sharps inventory (Q1)

- **Named service & sharps inventory (Q1)** — the exact unit/service (ward, phlebotomy round,
  dental surgery, ambulance, lab) **and the sharps actually used** (hollow-bore needles, lancets,
  scalpels, IV cannulae, suture needles). **Refuse "a clinic" / "the ward"** (the specificity
  anchor). A missing service or device list is a `[GAP]`, never invented.

## 2. Record the elimination/substitution decision — the engineering-first gate (the spine)

This question is asked **first among the controls** because eliminating the sharp is the **primary
control**, not the safety device:

- **Q2 = yes** → the plan **leads with elimination / substitution**: remove unnecessary sharps,
  substitute needle-free connectors / alternative routes, ban recapping by hand. The safety device
  is a residual measure for the sharps that genuinely remain.
- **Q2 = no** → branch to **safety-engineered devices (Q3)**: specify the devices with an integrated
  sharps-protection mechanism for the residual sharps, and record the **documented annual
  safer-device evaluation with non-managerial frontline-worker input** (OSHA (c)(1)(iv) /
  Needlestick Act). **A non-engineered device still in use without a recorded justification is
  FLAGGED.**

## 3. Work practices & disposal (Q4) — no recapping

Define the safe work practices and disposal: the **no-recapping rule** (recapping by hand fails),
**point-of-use sharps containers** (fill line, location — the sharp is disposed at the moment of
use), the safe-disposal route, and single-handed / scoop technique where a sharp must be re-sheathed
by design.

## 4. Confidential post-exposure (PEP) pathway (Q5) — role-only, consented

Author the **confidential** post-exposure pathway: immediate first aid → **confidential** incident
report → **source-patient testing with consent and confidentiality** (the source patient is "the
source patient" by role only) → **PEP timing for HBV/HCV/HIV** → follow-up → the Sharps Injury Log
entry. Record the **HBV-vaccination status** (offer + follow-up per OSHA (f)). **No source patient
or worker is named in the circulated plan**; the exposure / PEP medical record is held confidentially
and separately.

## 5. De-identified / aggregated Sharps Injury Log structure (h)(5)

Build the **Sharps Injury Log structure** per OSHA **1910.1030(h)(5)** — the fields (device type,
brand, the work area where the injury occurred, how it occurred) — but in the **circulated**
artifact the log is **structural / aggregated**, never line-level identified. Apply the `<5`
small-cell suppression with the secondary back-calculation guard to every category (by device,
unit, job, or period).

## 6. Rank the controls (the hierarchy gate) + the residual + SMART actions + report

Run the `controls` engine. The control narrative **always leads with eliminating the sharp** →
engineer (safety-engineered devices, point-of-use containers) → administrative (no-recapping,
training, the safer-device evaluation, the Sharps Injury Log) → **PPE + PEP LAST**. A sharps
treatment that **leads with "be careful / wear gloves" where the sharp could be eliminated or
engineered out** (`controls.validate_treatment` returning `ppe_admin_only=True`) is a **FLAG pushed
up the hierarchy, never the headline control**. Frame the qualitative residual sharps-exposure risk
via `risk_matrix`. Every device-changeover / training / log-implementation / vaccination action
becomes a SMART action (named role owner + ISO due date + measure), validated by
`smart_actions.validate_register`. Validate the draft against `references/QUALITY_CHECKLIST.md`,
then assemble `assets/sharps-needlestick-management.report.json` and run the canonical
`report-output` call.

## Jurisdiction

US **OSHA 29 CFR 1910.1030** ((c) ECP + annual review / (c)(1)(iv) safer-device evaluation /
(d)(2) engineering & work-practice controls / (f) confidential post-exposure follow-up / (h)(5)
Sharps Injury Log) + the **Needlestick Safety and Prevention Act (PL 106-430)** is the default duty;
EU/UK is **EU Directive 2010/32/EU** + the **UK Sharps Regulations 2013** with COSHH (cite the
member-state transposition for the binding obligation; RIDDOR for reportable UK exposures). For
India, resolve the state via `hse-india` (**mandatory state detection**) per the **Bio-Medical Waste
Management Rules 2016** sharps segregation (yellow/blue/white-translucent stream), and emit a literal
`[GAP]` where a state return is owed — **never a minted national form number**.
