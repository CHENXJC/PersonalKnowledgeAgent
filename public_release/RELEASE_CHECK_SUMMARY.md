# Release Check Summary

## Most Recent Recorded Check

- Status: WARNING
- Warnings: 26
- Failures: 0

This was the PKB-005 baseline recorded before Demo Mode and screenshot
preparation files were added.

## Current PKB-006 Check

- Status: WARNING
- Warnings: 29
- Failures: 0

## Current PKB-007 Check

- Status: WARNING
- Warnings: 32
- Failures: 0

Commands run:

```powershell
python tools/check_demo_mode.py
python tools/public_release_check.py
```

`python tools/check_demo_mode.py` returned:

- Status: PASS
- Warnings: 0
- Failures: 0

Policy:

- `WARNING` is allowed only if non-blocking and caused by safety documentation,
  tests, checker pattern examples, or synthetic path detection examples.
- `FAIL` means no release.

## Warning Types

The warnings were expected review items, not blocking failures:

- Safety keyword examples in documentation.
- Test fixtures that contain safety keyword strings.
- Code patterns used by scanner and release checker guardrails.
- Windows path regex examples in tests and checker code.
- Generated local inventory reports under `outputs/` created during validation.

## Current Blocking Status

There is no blocking failure in the current recorded check.

## Current PKB-008 Check

- Status: WARNING
- Scanned text files: 64
- Warnings: 32
- Failures: 0

PKB-008 added screenshot assets, screenshot index updates, and
`public_release/SCREENSHOT_REVIEW.md`. The warning count remains non-blocking
and there are still 0 failures.

## Current PKB-009 Check

- Status: WARNING
- Scanned text files: 66
- Warnings: 32
- Failures: 0

PKB-009 added GitHub public showcase prep documentation and `.gitignore`
protection for real `knowledge_base/` notes. The warning count remains
non-blocking and there are still 0 failures.

## Required Before Publishing

Run the checker again immediately before any public release:

```powershell
python tools/public_release_check.py
```

If the result contains any `FAIL`, do not publish. Remove or sanitize the risky
file/content, then rerun the check.
