# De-id phone filter — CLEAN fixture (no real phone)

This fixture carries ISO-8601 dates and dotted regulatory citations only. The
de-id grader must NOT hard-fail on any of these — none is a phone number.

## Due dates (ISO-8601)

- Action review due 2026-06-24.
- Re-inspection scheduled 2026-09-01.
- Annual recertification 2027-01-15.

## Regulatory citations (dotted)

- OSHA fall-protection trigger height: 29.1926.501.
- Arc-flash incident-energy method: 1584.2018.
- Approach-boundary table reference: 70E.130.

## Multi-token citations with edition years / spans (D-03 hardening)

These join across spaces, parentheses, and line breaks so the loose candidate
regex sees >=10 digits — but each is a regulatory/standard citation, not a phone:

- Live-work boundaries per US OSHA 29 CFR 1910.269
  (269(d) / 269(m)) with 1910.333 + 1910.147 cross-references.
- Hearing-conservation trigger per US OSHA 29 CFR 1910.95 (2008).
- High-wind man-riding cut-off per BS 7121-1 (2016) 7 m/s.

All identifiers above are dates or standard clause numbers, not telephone
numbers, so `_has_phone_leak()` returns False and the de-id gate stays green.
