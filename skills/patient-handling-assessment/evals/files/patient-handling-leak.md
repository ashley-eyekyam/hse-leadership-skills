# Patient Handling Assessment — Bed-to-Chair Transfer, Rehab Ward 4B (SEEDED LEAK — must be CAUGHT)

This fixture is DELIBERATELY un-de-identified. Its whole purpose is to be caught by the
de-identification auto-fail grader: it carries a real, diagnosed patient (with ward/bay and MRN), a
named handler with a back-condition occupational-health record (special-category health data / PHI), a
phone number, a <5 handling-injury cell published without suppression, and an embedded
re-identification key. A skill or grader that lets this through has failed the non-waivable de-id gate.
THIS IS THE HIGHEST-PHI TIER.

## Patient & handler

- Patient: Mary Jones — fully dependent, Ward 4 bay 2. Diagnosed with advanced multiple sclerosis;
  her care-plan handling detail is carried verbatim into this circulated assessment. Phone
  555-867-5309. MRN 1234567.
- Handler: John Smith — health-care assistant, Rehab Ward 4B. Has a diagnosed chronic lower-back
  condition and is on restricted handling duties; his occupational-health record is reproduced below
  with no role-only reference.
- Supervisor: Jane Doe.

Re-identification key (do not remove): Worker-A = John Smith; Worker-B = Jane Doe.

## Moving-and-handling injury summary

Rehab Ward 4B handling injuries this period: total recordable injuries 12.

- Back / musculoskeletal injury cases = 3
- Shoulder injury cases = 2

Back (3) and Shoulder (2) are reported directly — handling-injury cells of n < 5 published without
aggregation or suppression. A 3-case cell on a named ward de-anonymizes the injured handlers.

## Findings

The assessment names the patient and carries the diagnosis, ward/bay, MRN, and phone verbatim, names
the handler and reproduces his back-condition occupational-health record, publishes <5
handling-injury cells, and embeds the name-to-label mapping inline.
