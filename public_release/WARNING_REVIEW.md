# Warning Review

## Current Public Release Check Warning Count

- Current expected status: WARNING
- Current warning count: 32
- Current failure count: 0
- Current PKB-009 scanned text files: 66

## Warning Source Categories

## Security Keywords In Docs

Examples include documentation that explains why tokens, passwords, keys, and
identity files must not be published.

Blocking: No, if the warning is clearly part of safety guidance.

## Test Fixtures

Tests intentionally contain safety keyword strings to verify scanner behavior.

Blocking: No, if the test does not contain a real secret assignment or real
credential value.

## Checker Pattern Examples

The release checker itself contains keyword patterns used to detect risky files
and content.

Blocking: No, if the pattern is static code and not a real credential.

## Windows Path Detection Examples

Some tests and checker patterns contain Windows-path examples to verify path
leak detection.

Blocking: No, if the path is synthetic and not a private user path.

## Generated Local Output Reports

The PKB-007 validation run generated local Markdown reports under `outputs/`.
These files may contain project inventory text and should be treated as local
generated artifacts, not public repository files.

Blocking: No, if `outputs/` is ignored and only `outputs/.gitkeep` is included
in a future public repository.

## Current Failure Status

There is currently no known blocking failure.

PKB-009 note: real `knowledge_base/` notes are still visible to local safety
scans, but they are excluded from the future public GitHub showcase by
`.gitignore` by default.

## How To Recheck Before Publishing

Run:

```powershell
python tools/public_release_check.py
```

Then inspect all warnings and confirm there are 0 failures.

## Stop Conditions

If any warning contains a real secret, real token, real password, real identity
data, real private path, or real private personal note, stop the release and
remove or sanitize the content.

If any `FAIL` appears, do not publish.
