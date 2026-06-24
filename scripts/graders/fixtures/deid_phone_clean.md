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

All identifiers above are dates or standard clause numbers, not telephone
numbers, so `_has_phone_leak()` returns False and the de-id gate stays green.
