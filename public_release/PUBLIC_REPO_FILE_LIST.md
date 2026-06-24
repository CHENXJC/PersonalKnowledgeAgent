# Public Repository File List

This file defines the recommended file scope for a future GitHub public
showcase release.

## Safe To Include

Review once before publishing, then include:

- `app.py`
- `agent/`
- `config/kb_config.json` after review
- `demo_knowledge_base/`
- `docs/`
- `public_release/`
- `portfolio/showcase_screenshots/`
- `portfolio/showcase_screenshots/*.png` after full-size manual review
- `tests/`
- `tools/`
- `README.md`
- `PROJECT_STATUS.md`
- `requirements.txt`
- `.gitignore`
- `knowledge_base/README.md`
- `knowledge_base/.gitkeep`

## Excluded / Private By Default

- Real notes under `knowledge_base/`
- Generated reports under `outputs/`, except `outputs/.gitkeep`
- `.env`
- `*.env`
- `*.key`
- `*.pem`
- Tokens
- Credentials
- Logs
- Raw private files
- PDFs, Excel files, videos, audio files, private images, and unreviewed media

## Review Carefully Before Including

- `PROJECT_STATUS.md` if it contains local machine paths.
- Any generated report.
- Any screenshot.
- Any note copied from a real private workflow.

## Do Not Include

- `.env`
- `*.key`
- `*.pem`
- Real private notes
- Real identity documents
- Tokens
- Credentials
- Logs
- Raw personal files
- PDFs, Excel files, images, or videos unless they are demo-only and manually reviewed

## Important

For a public GitHub showcase, `demo_knowledge_base/` is the safe demo content.

Real `knowledge_base/` content is excluded by `.gitignore` by default. Only
`knowledge_base/README.md` and `knowledge_base/.gitkeep` are intended for the
public showcase.

If unsure, exclude private `knowledge_base/` from public release or replace it
with sanitized demo notes only.
