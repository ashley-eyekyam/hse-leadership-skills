# Pre-output Quality Checklist — india-osh-code-pack (status: beta)

Before producing any output, validate the draft against this gate:

- [ ] **State resolved FIRST and confirmed** (mandatory state detection, CT-8) — no
      state-specific consolidated form asserted before the state is known.
- [ ] The **legacy state form is the primary answer** (legacy-first); the consolidated mapping
      is opt-in transition mode.
- [ ] The consolidated direction + thresholds trace to `KB-REG-IN-OSH-CODE` by fragment ID;
      the OSH-Code commencement status is read from the KB, never hard-coded in the body.
- [ ] Any **unnotified consolidated form** is rendered `[GAP]` — never invented; the briefing
      **never instructs filing an OSH form the user's state has not notified** (Decision 7).
- [ ] The commencement caveat is explicit — only **GJ + AR** have notified OSH Rules; the
      savings clause keeps legacy filings valid.
- [ ] De-identification pass complete BEFORE drafting; no Aadhaar/name/employee-ID/address
      leak; small cells (<5) aggregated.
- [ ] Output states it is legacy-first decision-support requiring a competent person's review.
