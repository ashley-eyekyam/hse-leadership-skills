# De-identification Checklist (A5) — safety-authorisation (moderate tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> cannot be waived. This is the **moderate** de-id tier: a ROGS application pack is a
> document submitted to ORR and circulated to co-operating dutyholders, so named
> **safety-critical role-holders**, **COSS** (controller of site safety), and **Sentinel
> competence-card numbers** must become role labels in any distributed copy.

The canonical A5 steps, with the rail-application reinforcement (CONV-7) that this skill needs:

1. **DETECT & FLAG** every personal/health identifier in the inputs and list them up
   front — names, the accountable duty-holder and safety-critical role-holders, **COSS /
   lookout / driver / signaller names**, **Sentinel numbers**, employee / Aadhaar / NI
   numbers, contacts, exact dates, precise locations, and any fitness-for-duty / medical
   detail. If unsure whether something is identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** to stable **role labels** ("Accountable Duty-Holder",
   "Safety-Critical Role A", "COSS (role)", "Appointed AsBo"). Keep the re-identification
   key in a SEPARATE access-controlled artifact; **never** embed the key or any name↔label
   mapping (and never embed a Sentinel number) in the application pack.
3. **AGGREGATE SMALL NUMBERS** — never publish an injury/illness/competence-exception cell
   of fewer than 5 individuals; aggregate up and apply secondary suppression so suppressed
   cells cannot be back-calculated from totals.
4. **WARN BEFORE WIDE DISTRIBUTION** — the application pack circulates to ORR and
   co-operating dutyholders; warn the user before any name, Sentinel number, or
   fitness-for-duty detail enters the distributed document.
5. **MINIMIZE & LIMIT PURPOSE** — use only the personal data the application needs; keep
   fitness-for-duty / occupational-health detail out of the circulated pack (it lives in
   the separate confidential competence/medical record the SMS references).
6. **GOLDEN OUTPUTS** — show accountability by ROLE LABEL (e.g. "Accountable Duty-Holder",
   "COSS (role)", "Appointed AsBo"), never a realistic personal name; a personal name in a
   de-identified deliverable reads as a leak even though it is a deliberate contractual
   appointment.

> **Note on legitimate framing data.** ROGS regulation numbers, the SI 2006/599 citation,
> CSM-RA Reg (EU) 402/2013, ISO clause numbers, and the route name are *framing facts*, not
> personal identifiers — they stay. Only **personal** data (names, Sentinel numbers,
> contacts, fitness-for-duty detail) is scrubbed.
