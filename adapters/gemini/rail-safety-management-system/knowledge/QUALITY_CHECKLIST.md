# Pre-output Quality Checklist — rail-safety-management-system

Before producing any output, validate the draft against this gate:

**Universal gates**
- [ ] De-identification pass complete BEFORE drafting; no identifier leak (no role-holder name, COSS, or Sentinel number, no embedded re-identification key).
- [ ] Every element traced to evidence (a supplied input or a cited KB fragment with `source`+`year`); no unsupported assertion; un-supplied facts flagged `[GAP]`, never invented.
- [ ] Risk-control arrangements: no vague controls; no PPE/admin-only treatment without a "higher-order not reasonably practicable" (SFAIRP) justification; the full hierarchy of controls walked; residual risk re-scored.
- [ ] Named **role** owner + target/review date on every action and every `[GAP]` closure.

**Rail-SMS domain gates**
- [ ] The **dutyholder route is correct and resolved once**: mainline transport operator → safety certificate; infrastructure manager → safety authorisation; non-mainline → ROGS Part 3 verification.
- [ ] The SMS is framed **for-acceptance** — it does **NOT** state it is "accepted / approved / granted by ORR". (ORR is the Safety Authority; acceptance is its act.)
- [ ] All nine ROGS/ORR elements are present and populated (policy, accountabilities, risk-control arrangements, CSM-RA change interface, competence/Sentinel, asset/ECM maintenance, emergency, monitoring/audit, continuous improvement) — no element left as an empty heading.
- [ ] The accountable duty-holder + safety-critical roles are named (role labels) with stated accountabilities.
- [ ] CSM-RA change element (where there is a significant change): significance test + risk-acceptance principle + independent AsBo present, not a vague "we manage change".
- [ ] Operator/operation specificity — names *this* dutyholder + operation; a generic "a railway" SMS is rejected.
- [ ] India: Railways Act 1989 / CRS framing cited, state detection done, state-specific content deferred to `hse-india`, no national form invented.

## Golden eval-output convention (`evals/output/*.md`)

When you author this skill's golden output (the LOCKed exemplar the grader scores
against), hold it to three rules so it reads like a real deliverable, not a
rubric-compliance demo:

1. **Owners by role label, never a realistic personal name** ("Site Manager
   (role)", "Appointed Person"). A personal name reads as a de-id leak; the role
   fully satisfies the "named owner" defensibility requirement.
2. **No process meta-narration in the deliverable prose** — cut
   "de-identification ran first" / "never narrated" / "(by design)" lines. KEEP
   the honest `[ASSUMPTION]` / `[GAP]` flags.
3. **Representative deliverable depth** — real document density, no padding.

Full convention + do/don't examples: `docs/AUTHORING_GUIDE.md` section 7
(Golden eval-output authoring).
