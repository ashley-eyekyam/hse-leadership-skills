# De-id phone filter — SEEDED fixture (one real phone leak)

This fixture deliberately contains a single residual phone number so the
regression test can prove the non-waivable de-id gate still trips.

## Contact line (seeded leak — by design)

Phone 555-867-5309

The line above is a 10-digit number with a phone cue word, so
`_has_phone_leak()` returns True and the de-id grader MUST hard-fail.
