# De-identification Checklist (A5) — level-crossing-track-worker-safety (moderate tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> cannot be waived. This is the **moderate** de-id tier: a level-crossing / track-worker
> safe-system-of-work circulates to the gang, co-operating dutyholders and possibly ORR,
> so named **safety-critical role-holders** — the **COSS** (Controller of Site Safety),
> the **lookout**, the **PICOP / engineering supervisor**, the **crossing keeper** — and
> any **Sentinel competence-card number** must become role labels in any distributed copy.

The canonical A5 steps, with the level-crossing / track-worker reinforcement (CONV-7) that this skill needs:

1. **DETECT & FLAG** every personal/health identifier in the inputs and list them up
   front — names, the accountable manager and safety-critical role-holders, **COSS /
   lookout / PICOP / signaller / crossing-keeper / gang-member names**, **Sentinel
   numbers**, employee / Aadhaar / NI numbers, contacts, exact dates, precise crossing or
   chainage locations tied to a named person, and any fitness-for-duty / medical detail.
   If unsure whether something is identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** to stable **role labels** ("COSS (role)", "Lookout (role)",
   "PICOP (role)", "Engineering Supervisor", "Gang Member A"). Keep the re-identification
   key in a SEPARATE access-controlled artifact; **never** embed the key, any name↔label
   mapping, or a Sentinel number in the safe-system-of-work.
3. **AGGREGATE SMALL NUMBERS** — never publish an incident / near-miss / competence-exception
   cell of fewer than 5 individuals on a named crossing or corridor; aggregate up and apply
   secondary suppression so suppressed cells cannot be back-calculated from totals. A `<5`
   incident cell on a named crossing de-anonymizes the involved track worker — it is a
   `de_identification` HARD-FAIL.
4. **WARN BEFORE WIDE DISTRIBUTION** — the safe-system-of-work circulates to the gang and
   co-operating dutyholders; warn the user before any name, Sentinel number, or
   fitness-for-duty detail enters the distributed document.
5. **MINIMIZE & LIMIT PURPOSE** — use only the personal data the safe system needs; keep
   fitness-for-duty / occupational-health detail out of the circulated document (it lives
   in the separate confidential competence/medical record).
6. **GOLDEN OUTPUTS** — show accountability by ROLE LABEL (e.g. "COSS (role)", "PICOP
   (role)", "Lookout (role)"), never a realistic personal name; a personal name in a
   de-identified deliverable reads as a leak even though it is a deliberate safety-critical
   appointment.

> **Note on [ASSUMED] anchors for SME confirmation pre-LOCK.** The **NR/L2/OHS/019 issue
> number and date** (`[ASSUMED A3]`) and any embeddable **ALCRM band labels** (`[ASSUMED A2]`)
> are A2/A3 assumptions: the competent-person / rail-SME confirms the current issue/date and
> the citable band-label set before golden-output LOCK. Until then they stay `[GAP]`/cited
> by reference — never invented.

> **Note on legitimate framing data.** Standard references (NR/L2/OHS/019, ROGS SI 2006/599,
> CSM-RA Reg (EU) 402/2013, ISO clause numbers) and the named crossing/work-site are *framing
> facts*, not personal identifiers — they stay. Only **personal** data (names, Sentinel
> numbers, contacts, fitness-for-duty detail) is scrubbed. The user's **ALCRM band** is
> recorded as supplied — never invented.
