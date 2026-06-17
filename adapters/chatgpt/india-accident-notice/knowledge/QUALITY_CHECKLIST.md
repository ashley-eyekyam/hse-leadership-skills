# Pre-output Quality Checklist — india-accident-notice

Before producing any output, validate the draft against this gate:

- [ ] **State resolved FIRST and confirmed** (mandatory state detection, CT-8); for a **mine**,
      the **DGMS region/zone** resolved first — no notice cited on an unconfirmed state/region.
- [ ] An **unseeded/unknown state** yields `[GAP]` and refuses a national form (KB-02).
- [ ] The form id traces to the resolved `KB-REG-IN-STATEFORMS` row (or the Mines/DGMS layer);
      every un-verified form id (incl. the numbered DGMS notice) is `[GAP]`, never invented.
- [ ] The **deadline is explicit** (e.g. within 24h) and each follow-up action carries a named
      owner + a deadline (`smart_actions` — the 24h timing is load-bearing).
- [ ] **OSH-Code transition note** appended (accident-notice duty retained; legacy-first) + the
      state authority / DGMS portal pointer (`KB-REG-IN-PORTALS`).
- [ ] The RCA is **deferred to `incident-investigation`** — this skill produces the notice, not
      the investigation.
- [ ] De-identification pass complete BEFORE drafting; no Aadhaar/name/employee-ID/address/
      diagnosis leak; small injury cells (<5) aggregated before entering the notice.
- [ ] Output states it is legacy-first decision-support requiring a competent person's review
      before filing.
