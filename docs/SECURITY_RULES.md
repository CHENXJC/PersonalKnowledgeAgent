# Security Rules

PersonalKnowledgeAgent is local-first and safety-first. The project must stay lightweight and must not read or upload private data unless the user explicitly approves a later controlled workflow.

## Do Not Read

- Do not read `.env` files.
- Do not read API keys.
- Do not read passwords.
- Do not read tokens.
- Do not read private credential files.
- Do not read certificate files such as `.key`, `.pem`, `.p12`, or `.pfx`.

## Do Not Upload Or Sync

- Do not upload private files.
- Do not automatically sync to cloud services.
- Do not create GitHub remotes automatically.
- Do not push to GitHub automatically.
- Do not send private files to any API.

## Highly Sensitive Data

Do not process or store the following highly sensitive material in this project:

- Passport files.
- Identity cards.
- Bank cards.
- Visa documents.
- Medical records.
- Tax documents.
- Account recovery codes.
- Password exports.

## Public Showcase Rule

The GitHub public version must contain demo/sample content only.

Public showcase content must not include:

- Real private study material.
- Real job application records.
- Private contact information.
- Customer data.
- Real financial account information.
- API keys, tokens, or passwords.
- Generated output reports from private workflows.

## PKB-001 Boundary

PKB-001 only created:

- Project skeleton.
- Markdown templates.
- Local scanner.
- Local keyword search.
- Tests and documentation.

PKB-001 does not include RAG, embeddings, OpenAI API, cloud sync, Streamlit UI, or private data import.

## PKB-003 Dashboard Boundary

PKB-003 adds a local Streamlit dashboard only.

The dashboard:

- Reads Markdown/TXT notes from `knowledge_base/`.
- Reads `PROJECT_STATUS.md` and `docs/SECURITY_RULES.md` for status and safety pages.
- Generates `outputs/kb_inventory_report.md`.
- Does not read `.env`, keys, tokens, passwords, credentials, PDFs, Excel files, images, videos, or private identity documents.
- Does not call OpenAI or any other external API.
- Does not upload files.
- Does not sync cloud storage.
- Does not create GitHub remotes.
- Does not push code.

## PKB-004 Dashboard Polish Boundary

PKB-004 improves dashboard UX, project cards, search highlighting, screenshot planning, and public showcase documentation.

PKB-004 still does not:

- Read files outside the current project knowledge base for knowledge browsing.
- Read `.env`, tokens, passwords, API keys, secrets, credentials, PDFs, Excel files, images, videos, or private identity files.
- Connect to OpenAI, RAG, local models, cloud services, or external APIs.
- Initialize Git, create a remote, or push code.
- Publish private personal knowledge files.

## PKB-005 Public Showcase Prep Boundary

PKB-005 adds public release preparation files, a sanitized demo knowledge base,
and a local release safety checker.

PKB-005 still does not:

- Read `.env`, tokens, passwords, API keys, secrets, credentials, PDFs, Excel files, images, videos, or private identity files.
- Copy real private knowledge base files into `public_release/`.
- Publish real personal knowledge files.
- Initialize Git, create a remote, or push code.
- Connect to OpenAI, RAG, embeddings, local models, cloud services, or external APIs.

Public showcase screenshots and demo material must use `demo_knowledge_base/`
or manually reviewed sanitized notes only.

## PKB-006 Demo Mode Boundary

PKB-006 adds a dashboard Knowledge Source Mode selector.

Allowed modes:

- Demo Mode: reads `demo_knowledge_base/`.
- Local Private Mode: reads `knowledge_base/`.

Demo Mode is the default and is the only recommended source for GitHub
screenshots and public demo publishing.

Local Private Mode must not be used for public screenshots. It exists only for
local personal review.

PKB-006 still does not:

- Allow arbitrary custom source paths.
- Read files outside the fixed project knowledge source folders.
- Read `.env`, keys, tokens, passwords, credentials, PDFs, Excel files, images,
  videos, or private identity files.
- Initialize Git, add a remote, or push code.
- Connect to OpenAI, RAG, embeddings, local models, cloud services, or external APIs.
