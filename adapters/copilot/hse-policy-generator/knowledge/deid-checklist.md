# De-identification Checklist (A5) — hse-policy-generator (standard tier)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and cannot
> be waived.

## PII surface for this skill: **low (standard tier)**

A clause-5.2 OH&S policy names the **organisation** and the **top-management signatory by
role/title** — not personal data. The policy body therefore carries **no individual's
personal or health data** by design. The de-id discipline still runs FIRST on any **supplied
context** (e.g. a draft policy, an audit note, or a risk list the user pastes in), because
that context can contain identifiers that must not survive into the circulated policy.

## The standard-tier checklist (apply before drafting)

1. **DETECT & FLAG** every personal/health identifier in the supplied inputs — names,
   employee / Aadhaar / SSN / NI numbers, contacts, exact dates, precise locations, and any
   medical detail. **List what you found before drafting.** If unsure whether something is
   identifying, treat it as identifying.
2. **PSEUDONYMIZE BY DEFAULT** — the signatory and any named individual become a **role/title
   label** ("Managing Director", "HSE Director"), never a personal name. Keep any
   re-identification key in a SEPARATE access-controlled artifact; **never embed it in the
   policy**.
3. **AGGREGATE SMALL NUMBERS** — if the supplied context includes injury/illness counts, never
   carry a category of fewer than 5 individuals into the policy; aggregate up with secondary
   suppression. (A policy rarely publishes counts — but the rule still applies to any context
   that does.)
4. **WARN BEFORE WIDE DISTRIBUTION** — the policy is a widely circulated, often public document;
   confirm **no** name, contact, or health detail from the supplied context leaks into it.
5. **MINIMIZE & LIMIT PURPOSE** — use only the organisational facts the policy needs (name,
   scale, risks, signatory role); keep any sensitive supplied raw data out of the output.

## Hard-fail test (de_identification dimension)

Any **real name, government ID, contact, address, DOB, or health detail** — or any embedded
re-identification key / name-to-label mapping — surviving into the circulated policy is a
**de_identification AUTO-FAIL** (non-waivable, overrides the weighted mean). The signatory is
a **role/title**, never a person.
