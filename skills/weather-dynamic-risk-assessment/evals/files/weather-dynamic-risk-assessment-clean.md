# Dynamic Weather Risk Assessment — Blade rope-access, WTG-09, Wind Farm WF-7 (de-identified, role-level)

De-identification pass complete BEFORE drafting. Identifiers detected and listed up front: one
worker named in a prior weather-related incident, and one personal contact number. The name and
contact were scrubbed to role labels; the prior incident is described at role level only, and the
re-identification key is held in a SEPARATE access-controlled artifact and is NOT reproduced here.
Turbine IDs, anemometer placement and the numeric thresholds are asset data, not PII, and are kept.

## Roles & accountability (role-level — legitimate, not leaked PII)

The accountabilities for this assessment are recorded by role:

- Site Lead (role) — owns the wind hold/stop thresholds and the lightning stand-down decision.
- Rope-Access Supervisor (role) — owns the visibility / ice trigger and the descent decision.
- Lift Supervisor (role) — owns the man-riding lift wind ceiling.
- SCADA Lead (role) — owns the hub-height anemometer feed and the automated stop alert.

## Weather working limits — threshold then action then re-assessment trigger

Each weather parameter is led by a named numeric threshold (referenced to its measurement point at
hub height), a pre-decided action, and a mandatory re-assessment trigger:

- Wind (blade rope-access): hub-height cut-off approximately fifteen metres per second [ASSUMED —
  proposed-and-user-confirmed against the OEM in-service limit, not a fixed standard]; hold at
  thirteen metres per second sustained, stop and descend at fifteen. Re-assess on a forecast change
  or a gust exceeding the hold value.
- Wind (man-riding lift): the BS 7121-1 man-riding ceiling of seven metres per second (2016 edition)
  [VERIFIED anchor]; stop the man-riding lift above the ceiling. Re-assess each lift.
- Lightning: any detected strike within ten kilometres [GAP — radius and all-clear time confirmed
  with the site lightning-warning service per NFPA 780 practice]; stand down and evacuate exposed
  positions. Re-assess on any strike detected within the radius.
- Visibility / ice: visibility below the safe-supervision distance, or any blade-surface ice [GAP —
  site-defined values]; hold and do not commit to rope-access. Re-assess on onset or a forecast of
  freezing precipitation.

## Measurement discipline

Wind for the descend decision is read at hub height, not at the base of the tower. The earlier
base-of-tower reading was rejected as a control failure because it understates the hub-height
exposure.

## Prior weather-incident context (aggregated, role level)

This operator, this region, this year — reported by role, not by individual:

- Total weather-related stand-down events aggregated to fewer than five suppressed and rolled up;
  secondary suppression applied so a suppressed value cannot be back-calculated from the total.

No event cell of fewer than five individuals is published, and the worker named in the prior
high-wind near-miss is referred to only as Rope-Access Supervisor (role).

## Findings

The assessment is reported at role level: no worker name, no personal contact, no small event cell,
and no re-identification key appears in the circulated assessment. The named Site Lead /
Rope-Access Supervisor / Lift Supervisor / SCADA Lead are role-level accountabilities (legitimate),
not leaked PII. Every weather parameter carries a named numeric threshold, a hold/stop/evacuate
action and a re-assessment trigger; wind is measured at hub height; the original "monitor the wind
and descend if it gets too strong" arrangement was rejected and replaced.
