# De-identification Checklist — regulatory-returns (REINFORCED · D-06)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **`de_identification`
> hard-fail** (A8) and cannot be waived.
>
> **`regulatory-returns` is one of the three highest-de-identification-sensitivity
> skills** (with `psychosocial-risk-assessment` and `health-risk-assessment`). A
> statutory return holds **injured-person identity and special-category health data by
> law** — so the standard checklist below is reinforced with the special-category
> rules in the next section.

## Reinforcement — legally-required submission vs internal/shared copy (the load-bearing distinction)

A statutory return is **required by law to name the injured person** on the official
submission (e.g. the OSHA 301 incident report, the RIDDOR report). That is **NOT** a
licence to circulate identity. Produce and keep these **separate**:

1. **The legally-required submission (named, controlled).** The official form carries
   the names the regulator requires. It is **access-controlled** — filed to the
   regulator / portal, held by the named competent person, **never** pasted into a
   board pack, a toolbox talk, an email thread, or any widely-shared artifact.
2. **Every internal / shared / working copy (role-labelled).** Any copy that circulates
   internally — the working draft, the management summary, the 300A annual summary
   posted for employees — is **de-identified to stable role labels** ("Injured Worker
   A", "Supervisor 1"). The injured person's name, government ID (SSN / NI / Aadhaar),
   home address, contact, exact DOB, and **all diagnosis / health detail** are scrubbed.
3. **`<5` small-cell suppression on any aggregated summary.** Never publish an
   injury/illness category — e.g. a **300A broken down by department**, an injury-type
   tally, or a body-part breakdown — with **fewer than 5** individuals in a cell.
   Aggregate up and apply **secondary suppression** so a suppressed cell cannot be
   back-calculated from the row/column totals. (The OSHA 300A summary itself is posted
   in aggregate; a per-department or per-shift breakdown that creates a `<5` cell
   re-identifies a worker and is a leak.)
4. **Never embed the re-identification key.** The name↔role-label mapping is held in a
   **separate, access-controlled artifact** — **never** inside the return, the working
   copy, or any circulated document. Tell the user to store it apart.

> **Rule of thumb:** the regulator's official form may be named; everything you hand
> back for internal circulation is role-labelled, aggregated, and key-free. If you
> cannot tell which copy you are drafting, treat it as the circulated copy.

## Standard checklist (always applies)

1. **DETECT & FLAG** every personal/health identifier in the inputs and **list them up
   front** — names, employee / Aadhaar / SSN / NI numbers, contacts, exact dates,
   precise locations, job title / crew / shift, photos, and any medical / diagnosis
   detail. If unsure whether something is identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** for any output that will circulate — stable role labels;
   keep the re-identification key **SEPARATE** (per the reinforcement above).
3. **AGGREGATE SMALL NUMBERS** — never publish an injury/illness cell of **fewer than 5**
   (per the reinforcement above; the `<5` rule is eval-enforced as a hard-fail).
4. **WARN BEFORE WIDE DISTRIBUTION** — the 300A posting, board reports, and any shared
   summary default to de-identified / aggregated; warn before any name or health detail
   enters a widely-shared artifact.
5. **MINIMIZE & LIMIT PURPOSE** — use only the personal data the determination needs;
   keep sensitive raw data out of external services where you can.
