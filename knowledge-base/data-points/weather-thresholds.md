<!-- KB-DATA-WEATHER-THRESHOLDS -->
# Weather thresholds for outdoor/at-height work — method + anchors (values user-confirmed)

**Fragment ID:** `KB-DATA-WEATHER-THRESHOLDS`
**What this is:** the **dynamic / point-of-work weather risk-assessment method** for
outdoor and at-height renewables work — grounding `weather-dynamic-risk-assessment`
(REN-03). It carries the method (ISO 45001 cl 6.1.2 dynamic RA) plus the **verified
public anchor** (BS 7121-1 man-riding ceiling) and clearly-flagged
`[ASSUMED]`/user-confirmed thresholds.
**What this is NOT:** a single citable "wind cut-off standard." The hub-height
tower-top wind cut-off is an industry baseline (**`[ASSUMED A4]`**), not a citation —
it is **proposed and user-confirmed, never invented**. All numeric thresholds are
**user-confirmed for the site**.

> Source: dynamic/point-of-work RA method on ISO 45001:2018 cl 6.1.2; BS 7121-1 (2016 edition) man-riding ceiling; NFPA 780 lightning practice; manufacturer/CPA in-service crane wind limits · Year: 2026 · Reviewed: 2026-06-23 · Volatile: true (resolve site/manufacturer values at use time).

---

## The method (ISO 45001 cl 6.1.2 — dynamic, point-of-work)

Weather risk is managed by a **dynamic / point-of-work risk assessment**: define the
threshold → the action (hold / stop / evacuate) → the **mandatory re-assessment
trigger** → measured at **hub height (not base of tower)** for turbine work
(see `KB-SNIP-DYNAMIC-RA`).

## Anchors and thresholds

| Parameter | Value | Status |
|---|---|---|
| **BS 7121-1 man-riding wind ceiling** | **16 mph / 7 m/s** for personnel-carrier (man-riding) lifts | `[VERIFIED]` public anchor — **BS 7121-1:2016** (current edition; **not** the 2006 edition) |
| Hub-height tower-top wind cut-off for tower-top work | ≈ **15 m/s** industry baseline (stricter for less-experienced teams) | **`[ASSUMED A4]`** — industry baseline, **not** a single citable standard; **propose-and-user-confirms**, never embedded as a citation |
| Lightning stand-down / evacuate trigger | per **NFPA 780** practice / a lightning-warning service | method/practice — detection radius + time = user/service-confirmed → `[GAP]` |
| Manufacturer / CPA in-service crane wind limit | manufacturer's stated in-service limit | `[GAP]` — site/manufacturer-confirmed |
| Ice accretion / visibility / temperature triggers | site-defined trigger points | `[GAP]` — user-confirmed |

## Discipline (D-03 — user-confirmed, never invented)
- Embed the **method + the verified BS 7121-1 7 m/s man-riding figure** only.
- The ≈15 m/s tower-top cut-off is **proposed and user-confirmed** — never presented
  as a hard standard or a citation; SME confirms (A4) before golden-output LOCK.
- All manufacturer/site/lightning thresholds are `[GAP]` until the user confirms.

## How the skill uses this fragment
REN-03 builds a dynamic weather RA: each threshold carries an action + a mandatory
re-assessment trigger, the BS 7121-1 7 m/s man-riding figure is cited verbatim, and
every other numeric threshold (incl. the ≈15 m/s baseline) is proposed-and-confirmed
or `[GAP]` — never invented.
