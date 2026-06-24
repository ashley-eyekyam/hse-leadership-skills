<!-- KB-REG-FMCSA-HOS -->
# United States / European Union — FMCSA Hours-of-Service + EU drivers' hours map

**Fragment ID:** `KB-REG-FMCSA-HOS`
**What this is:** a copyright-safe **duty → limit-topic → artifact map** for
commercial-driver fatigue/hours regulation: the US FMCSA Hours-of-Service rules
(49 CFR 395) and the EU drivers' hours regime (Regulation (EC) 561/2006), naming
the limit *categories* (driving / duty / break / rest) and the records each
regime requires — not the numeric limits themselves, which the fatigue engine
embeds and verifies.
**What this is NOT:** a reproduction of 49 CFR 395, Regulation (EC) 561/2006, or
their guidance, and NOT the source of the numeric hour limits (those live in the
deterministic fatigue engine as cited LOCKED constants). Cite the
part/article/topic only — never paste the regulation wording.

> Source: FMCSA Hours-of-Service, 49 CFR Part 395 + Regulation (EC) No 561/2006 (EU drivers' hours) — citation map · Year: 2026 · Reviewed: 2026-06-21 · Volatile: true (rule amendments + exemptions drift; refresh on review).

This fragment maps the *structure* of commercial-driver fatigue regulation so a
logistics/transport skill knows which limit categories and records apply by
jurisdiction. The fatigue engine (`scripts/hse_components/`) holds the numeric
windows and computes compliance; this fragment supplies the duty framing and the
artifact each regime expects.

## Jurisdiction / topic → limit category → artifact it grounds

| Jurisdiction / topic | Limit category (paraphrased) | Artifact it grounds |
|---|---|---|
| US property-carrying (49 CFR 395) | Maximum driving window + on-duty window | HOS log / ELD record |
| US — required break | Break after accumulated driving | break entry in the HOS record |
| US — restart | Off-duty reset of the weekly cycle | restart evidence in the HOS record |
| EU (Reg 561/2006) — daily driving | Daily driving limit (with extensions) | tachograph record |
| EU — break | Break within the driving period | tachograph break record |
| EU — daily / weekly rest | Daily + weekly rest minima | tachograph rest record |
| Both — recordkeeping | Retain driver-hours records | the duty-holder's hours-of-service record set |

## How the skill uses this fragment
- A transport/logistics skill resolves the jurisdiction first, grounds the
  applicable limit categories here, then defers the numeric compliance check to
  the fatigue engine (which carries the cited limits as LOCKED constants).
- The numeric hour values are NOT in this fragment — a skill never quotes a limit
  from here; it asks the engine. A missing input is `[GAP]`, never invented.
