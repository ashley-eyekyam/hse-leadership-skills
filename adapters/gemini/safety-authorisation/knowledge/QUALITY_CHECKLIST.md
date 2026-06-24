# Pre-output Quality Checklist — safety-authorisation

Before producing any output, validate the draft against this gate:

**Universal gates**
- [ ] De-identification pass complete BEFORE drafting; no identifier leak (no role-holder name, COSS, or Sentinel number, no embedded re-identification key).
- [ ] Every element traced to evidence (a supplied input, the referenced SMS, or a cited KB fragment with `source`+`year`); no unsupported assertion; un-supplied facts flagged `[GAP]`, never invented.
- [ ] Risk-control summary: no vague controls; no PPE/admin-only treatment without a "higher-order not reasonably practicable" (SFAIRP) justification; the full hierarchy of controls walked.
- [ ] Named **role** owner + target/review date on every action and every `[GAP]` closure.

**Safety-authorisation domain gates**
- [ ] The **dutyholder route is correct and resolved once**: infrastructure manager → safety authorisation; mainline transport operator → safety certificate; non-mainline → ROGS Part 3 verification.
- [ ] The application **REFERENCES the SMS — it does NOT rebuild it.** The pack cites the SMS (RAIL-01's artifact) as an input and does not reconstruct the ROGS/ORR SMS element set. If the SMS is absent, the pack routes to RAIL-01 and records the SMS as a `[GAP]` input (CONV-12).
- [ ] The application is framed **for-submission** — it does **NOT** state it is "authorised / accepted / approved / granted by ORR". (ORR is the Safety Authority; granting the authorisation is its act.)
- [ ] All application elements are present and populated (applicant identity & route declaration, SMS reference & scope, risk-control summary, CSM-RA change evidence where applicable, competence/Sentinel & ECM assurance, declaration & submission) — no element left as an empty heading.
- [ ] The accountable duty-holder + safety-critical roles are named (role labels) with stated accountabilities.
- [ ] CSM-RA change evidence (where there is a significant change): significance test + risk-acceptance principle + independent AsBo present, not a vague "we manage change".
- [ ] Dutyholder/operation specificity — names *this* dutyholder + operation; a generic "a railway" application is rejected.
- [ ] India: Railways Act 1989 / CRS framing cited, state detection done, state-specific content deferred to `hse-india`, no national form invented.

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores
against), hold it to three rules so it reads like a real deliverable, not a
rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("Accountable
   Duty-Holder", "Appointed AsBo"). A personal name reads as a de-id leak; the role
   fully satisfies the "named owner" defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut
   "de-identification ran first" / "never narrated" / "(by design)" lines. KEEP
   the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real document density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7
(Golden eval-output authoring).
