# Release Safety Check

PersonalKnowledgeAgent is a personal knowledge base project. A real local
knowledge base can contain private study notes, career material, personal goals,
project drafts, file names, or generated reports that are not suitable for a
public repository.

The public showcase version must use demo or sanitized notes only.

## Why Real Personal Knowledge Should Not Be Published

Public repositories are indexed, cloned, archived, and difficult to fully erase.
Private notes can expose identity, education, career plans, accounts, local
paths, confidential project details, or sensitive documents. Even harmless file
names can reveal private context.

## Allowed In A Public Showcase

- Source code for the local-first dashboard.
- Public-safe README and documentation.
- Sanitized demo notes in `demo_knowledge_base/`.
- Tests.
- Screenshot instructions.
- Release checklist files.
- Reviewed non-sensitive generated reports only.

## Forbidden In A Public Showcase

- `.env` files.
- API keys, tokens, passwords, recovery codes, or credentials.
- Real private personal knowledge files.
- Identity documents, passports, visas, bank cards, tax documents, medical files,
  or legal files.
- Real job applications, resumes, customer records, private emails, phone
  numbers, addresses, or account information.
- Private logs.
- Real generated output reports that have not been manually reviewed.

## How To Run The Check

```powershell
python tools/public_release_check.py
```

The checker scans text files inside the current project and reports:

- `PASS`: no warnings or failures found.
- `WARNING`: review before public release.
- `FAIL`: blocking risk that must be removed before release.

## Handling WARNING

Warnings require manual review. Common warnings include:

- Security words used in documentation.
- Local Windows path examples.
- Mentions of sensitive categories in safety rules.

If the warning is only a safety explanation, it can be accepted. If it points to
private content, remove or sanitize the file before release.

## Handling FAIL

Failures block public release. Remove the risky file or content and rerun the
check.

Examples of blocking issues:

- `.env`
- `.key`, `.pem`, `.p12`, or `.pfx` files.
- Secret-like assignments where a key name is directly assigned a value.
- Files whose names suggest private credentials or identity records.

## Manual Review Still Required

The checker is a guardrail, not a guarantee. Before publishing, manually inspect
the release file list and confirm that no private knowledge base content is
included.
