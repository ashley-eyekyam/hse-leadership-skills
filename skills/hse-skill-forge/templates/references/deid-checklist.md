# De-identification Checklist (A5)

> The deep reference the mandatory `hse:block:deid` block points to. Apply it BEFORE
> drafting any output. A de-identification leak is an eval **hard-fail** (A8) and
> cannot be waived.

The canonical, full checklist is authored by A5 and inherited by every skill. This
scaffold copy exists so the deid block's `references/deid-checklist.md` pointer
resolves on disk (linter rule 8). Replace this with the skill's de-id reference
content or symlink to the canonical A5 checklist.

1. DETECT & FLAG every personal/health identifier in the inputs and list them up front.
2. PSEUDONYMIZE BY DEFAULT to stable role labels; keep the re-identification key SEPARATE.
3. AGGREGATE SMALL NUMBERS — never publish an injury/illness cell of fewer than 5.
4. WARN BEFORE WIDE DISTRIBUTION.
5. MINIMIZE & LIMIT PURPOSE.
6. GOLDEN OUTPUTS — show accountability by ROLE LABEL (e.g. "Site Manager (role)", "Appointed Person"), never a realistic personal name; a personal name in a de-identified deliverable reads as a leak even though it is a deliberate contractual appointment.
