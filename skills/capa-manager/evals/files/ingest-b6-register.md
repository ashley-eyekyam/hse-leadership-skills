Ingested CAPA register — emitted by safety-audit (the B6 producer side of the B6→B7 seam)

This is the producer register a safety-audit run emits: a `table` block whose HEADERS are
the B5 CAPA field names (action, owner, due, measure, links_to_cause, hoc_tier) — because
the strict report schema (additionalProperties:false) disallows extra keys on a
recommendations block, the producer carries the CAPA rows as a typed table. capa-manager
(B7) INGESTS this exact shape and runs the lifecycle over it, proving the SAME
smart_actions.validate_register accepts the ingested register with zero A7 change.

It is de-identified: every owner is a role label; no name, address, ID, or health detail.
(Due dates are written in prose here to keep the fixture de-id-clean; the real ingested
register carries ISO-8601 dates that smart_actions.validate_register checks.)

## Audit context

- Finding NC-1 (clause 8.1 / PTW-2): the permit-to-work procedure does not mandate an
  independent isolation-verification step before sign-off; 4 of 12 sampled permits were
  signed off with no recorded isolation check. Cause RC-1 (organisational/procedural gap).
- Finding NC-2 (clause 8.1 / PTW-3): close-out sign-back missing on 2 of 12 permits.
  Cause RC-2.

## CAPA register (producer shape — six B5 fields, no lifecycle fields yet)

| action | owner | due | measure | links_to_cause | hoc_tier |
|---|---|---|---|---|---|
| Fit an isolation-verification interlock so a permit cannot be signed off until isolation is independently confirmed in the register. | Maintenance Lead | by mid-July | 0 sampled permits signed off without a recorded isolation check at the next quarterly audit | RC-1 | Engineering |
| Amend the PTW procedure to mandate an independent isolation-verification step before sign-off; brief all issuers. | HSE Manager | by early July | Revised procedure issued and 100% of issuers briefed | RC-1 | Administrative |
| Add a mandatory close-out sign-back field that blocks permit closure if blank. | Maintenance Lead | by late July | 0 permits closed without sign-back in the following month's sample | NC-2 | Engineering |

Note: the producer supplied a corrective/structural action set but did NOT carry the B7
lifecycle fields (capa_type, verification, status) — those are exactly what B7 adds when it
ingests and manages this register. The owner is a role label; the cause ids round-trip.
