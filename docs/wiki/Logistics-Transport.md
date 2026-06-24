# Logistics & Transport

`hse-logistics-transport` is the transport and warehousing pack — the road, sea, and warehouse-floor artifacts of a logistics operation. It covers the ADR / DOT 49 CFR / IMDG chemical-transport classification cross-walk, driver-fatigue management (schedule/roster-led FRMS), and warehouse racking + MHE / pedestrian-segregation safety.

```
/plugin install hse-logistics-transport@hse-leadership-skills
```

Audience tags (`M` / `E` / `F` / `C`) and the five universal rules are explained once on [Home](Home).

---

**Audience legend:** **M** = manager · **E** = executive · **F** = frontline · **C** = consultant.

### chemical-transport-safety
- **Produces:** Produce loading/unloading and transport safety guidance and a classification cross-walk for road and sea — ADR (EU road), United States DOT 49 CFR HMR (American road), and IMDG (sea) — including UN number / class / packing group, placarding, marking and segregation.
- **For:** M, C · **Packs:** hse-chemicals, hse-logistics-transport · **Version:** 1.0 · **Jurisdiction:** All
- **Trigger:** "Produce loading/unloading and transport safety guidance and a classification cross-walk for road and sea — ADR (EU road)"; "United States DOT 49 CFR HMR (American road)"; "and IMDG (sea) — including UN number / class / packing group"
- **Summary:** Produce loading/unloading and transport safety guidance and a classification cross-walk for road and sea — ADR (EU road), United States DOT 49 CFR HMR (American road), and IMDG (sea) — including UN number / class / packing group, placarding, marking and segregation. Use it to classify dangerous goods for transport, cross-walk a GHS class to a transport class, work out placarding/segregation, or write loading/unloading safety guidance. Rail (RID) and air (IATA/ICAO-TI) are out of scope for v1.0 and flagged, not guessed; unknown UN entries are [GAP]-flagged; controls are hierarchy-of-controls ranked. Decision-support only; a competent person must review the output.

### driver-fatigue-management
- **Produces:** Produces a consultant-grade driver-fatigue-management artifact for a named fleet/operation and a real driver duty log, led by schedule/roster (FRMS) redesign rather than 'stay alert'.
- **For:** M, C · **Packs:** hse-logistics-transport · **Version:** 1.0 · **Jurisdiction:** US, EU, UK, IN
- **Trigger:** "manage driver fatigue"; "check hours-of-service (HOS) compliance"; "assess a duty/driving log against FMCSA 49 CFR 395"
- **Summary:** Produces a consultant-grade driver-fatigue-management artifact for a named fleet/operation and a real driver duty log, led by schedule/roster (FRMS) redesign rather than 'stay alert'. Use this skill when a user asks to manage driver fatigue, check hours-of-service (HOS) compliance, assess a duty/driving log against FMCSA 49 CFR 395 or EU Regulation (EC) 561/2006, build a fatigue risk management system (FRMS), or review rosters. The HOS compliance flags (driving limit, on-duty window, break, cycle, rest) are COMPUTED by the deterministic fatigue.py engine, never narrated, and are authoritative; a separate fatigue index is a clearly-flagged advisory metric, not a regulatory threshold. Multi-day cycle and cross-shift rest claims absent from a single-shift log are a [GAP], never invented. It leads controls with roster redesign, rejects an alertness-training / in-cab-gadget treatment, and de-identifies driver name / CDL / medical / OSA data to role labels first. Decision-support only; review by a competent person.

### warehouse-racking-mhe-safety
- **Produces:** Produces a consultant-grade warehouse racking + MHE/pedestrian-segregation safety artifact for a named warehouse, racking installation, and traffic layout — never a generic 'inspect carefully' or 'wear hi-vis'.
- **For:** M, C · **Packs:** hse-logistics-transport · **Version:** 1.0 · **Jurisdiction:** UK, US, IN
- **Trigger:** "Produces a consultant-grade warehouse racking + MHE/pedestrian-segregation safety artifact for a named warehouse"; "racking installation"; "and traffic layout — never a generic 'inspect carefully'"
- **Summary:** Produces a consultant-grade warehouse racking + MHE/pedestrian-segregation safety artifact for a named warehouse, racking installation, and traffic layout — never a generic 'inspect carefully' or 'wear hi-vis'. Use this skill to assess pallet racking, build a racking inspection regime, classify rack damage on the SEMA Red/Amber/Green bands, plan MHE/forklift and pedestrian segregation, or check a warehouse against BS EN 15635 / SEMA / OSHA 1910.178 / PUWER / HSE L117. It is design- and engineering-control-led: racking is controlled by SWL-rated configuration, column protection and the EN 15635 inspection regime (PRRS, weekly visual, >=12-monthly expert), and MHE/pedestrian conflict by ENGINEERED segregation (barriers, one-way systems, marked walkways) before hi-vis. It gets the SEMA RAG priority right (Green=monitor; Amber=repair in 4 weeks + escalate; Red=immediate off-load + isolate), refuses a vague 'a warehouse', never assumes an SWL ([GAP]). Decision-support only; a competent person must review.
