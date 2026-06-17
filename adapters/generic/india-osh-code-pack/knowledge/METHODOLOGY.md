# Methodology — OSH Code 2020 transition mapping (legacy-first, opt-in, state-detection-first)

A transition-briefing method over `KB-REG-IN-OSH-CODE` (status beta; 90d staleness, D-05c),
gated by **mandatory state detection** (CT-8). The legacy state form is ALWAYS the primary
answer; the consolidated mapping is opt-in and never instructs filing an unnotified form.

## The mapping method

1. **Resolve the state (BLOCKING gate).** Ask, or infer-from-address then confirm. An
   unseeded/unknown state → give the general direction of travel only; refuse to assert a
   state-specific consolidated form.
2. **Give the legacy-first answer.** Resolve the legacy form from `KB-REG-IN-STATEFORMS` as
   the primary, defensible answer.
3. **Map legacy → consolidated (opt-in transition mode).** Read `KB-REG-IN-OSH-CODE` and map
   the legacy obligation to its consolidated OSH-Code equivalent:
   - single registration (replacing per-law registrations);
   - single consolidated annual return;
   - raised factory threshold (10/20 → 20/40 workers);
   - shifted Safety-Officer trigger (1000 → 500/250).
4. **Flag commencement + freshness.** Warn that the consolidated form/portal **may not be
   live** in the user's state — only **GJ + AR** have notified OSH Rules as of the fragment's
   `last_reviewed`; the savings clause keeps legacy filings valid. Any unnotified consolidated
   form is rendered `[GAP]`, never invented (the citation grader is row-blind). **Never
   instruct the user to file an OSH form their state has not notified** (Decision 7).

## Evidence discipline
- The transition direction + thresholds trace to `KB-REG-IN-OSH-CODE`; the legacy form traces
  to `KB-REG-IN-STATEFORMS` — both by fragment ID, never model recall. Unnotified consolidated
  forms are `[GAP]`.
- The OSH-Code commencement status is read from the KB (90d staleness window), never hard-coded
  in this skill body.
- De-identify occupier/officer/worker PII (Aadhaar, employee ID, address, health) BEFORE
  drafting; aggregate small cells (<5).
