# Public Showcase Manifest

## Project Name

PersonalKnowledgeAgent

## Public Release Readiness

- Public release readiness status: GitHub public showcase published
- Current checkpoint: `PKB-010-GITHUB-PUBLISH`
- Public release mode: Demo/sanitized notes only
- Demo knowledge base path: `demo_knowledge_base/`
- Demo Mode status: Added to Streamlit dashboard and enabled by default
- Final release check status: Completed with 0 blocking failures
- Screenshot status: 9 screenshots captured using Demo Mode
- Real private knowledge base content is excluded from the public showcase by default.
- GitHub publication status: published.
- GitHub repository: `https://github.com/CHENXJC/PersonalKnowledgeAgent`
- Published branch: `main`

## Public Positioning

PersonalKnowledgeAgent is a local-first Markdown knowledge dashboard for
organizing AI project notes, university learning material, career assets,
business ideas, market observations, and long-term goals.

## Public Showcase Principle

The GitHub public version must contain demo or sanitized notes only. The real
private `knowledge_base/` is excluded by `.gitignore` by default. Only
`knowledge_base/README.md` and `knowledge_base/.gitkeep` are intended for the
public showcase.

## Knowledge Base Inclusion Policy

- Include: `demo_knowledge_base/`
- Include: `knowledge_base/README.md`
- Include: `knowledge_base/.gitkeep`
- Exclude by default: real notes under `knowledge_base/`
- Exclude by default: generated reports under `outputs/`, except
  `outputs/.gitkeep`

## Required Checks Before GitHub

- [x] `python -m pytest` - 27 passed.
- [x] `python -m compileall agent` - passed.
- [x] `python -m py_compile app.py` - passed.
- [x] `python -m agent.kb_scanner` - passed.
- [x] `python -m agent.kb_search QuantLabAgent` - passed.
- [x] `python -m agent.kb_report` - passed.
- [x] `python tools/check_demo_mode.py` - PASS, 0 warnings, 0 failures.
- [x] `python tools/public_release_check.py` - WARNING, 32 warnings, 0 failures.
- [x] Streamlit smoke check returns HTTP 200.

## Screenshot Readiness Checklist

- [x] Use demo/sanitized content only.
- [x] Prefer `demo_knowledge_base/` for screenshots.
- [x] Confirm no private note preview is visible.
- [x] Confirm no secret, token, password, credential, or account detail is visible.
- [x] Confirm no passport, visa, bank, tax, medical, or identity document is visible.
- [x] Confirm inventory reports do not show private local paths.
- [x] Confirm screenshots do not reveal unrelated browser or desktop information.
- [ ] Complete final manual full-size screenshot review before GitHub publication.

## Public Repository Content Checklist

Safe for public demo after review:

- `README.md`
- `PROJECT_STATUS.md`
- `app.py`
- `agent/`
- `config/kb_config.json`
- `docs/`
- `tests/`
- `public_release/`
- `demo_knowledge_base/`
- `knowledge_base/README.md`
- `knowledge_base/.gitkeep`
- `outputs/.gitkeep`
- `requirements.txt`
- `.gitignore`

Requires review before publishing:

- Any real `knowledge_base/` note if the user later decides to sanitize and include it.
- `outputs/kb_inventory_report.md`
- Any generated report.
- Any screenshot.
- Any note copied from a real private workflow.

Must not be published:

- `.env`
- API keys, tokens, passwords, credentials, or certificate files.
- Real identity, passport, visa, bank, tax, medical, or legal documents.
- Private logs.
- Private raw generated outputs.
- Unreviewed real personal knowledge files.

## Demo/Sanitized Data Only Principle

Use `demo_knowledge_base/` for public screenshots and public demos. It is the
only recommended source for public screenshots. Do not copy real private
knowledge base files into public release folders.

## Public Showcase Screenshot Readiness

- `portfolio/showcase_screenshots/` is prepared.
- Screenshot README and capture guide are prepared.
- Real screenshots are captured.
- Screenshot capture must use Demo Mode only.
- Screenshot review file: `public_release/SCREENSHOT_REVIEW.md`
- Screenshot PNGs should be included after final manual full-size review.

## Next Release Gate

Before any GitHub public release:

- [ ] All tests pass.
- [ ] Streamlit Demo Mode smoke check passes.
- [ ] `python tools/check_demo_mode.py` passes.
- [ ] `python tools/public_release_check.py` has 0 failures.
- [x] Screenshot folder is prepared.
- [x] Screenshots are captured from Demo Mode only.
- [ ] Screenshots receive final manual full-size review.
- [ ] User explicitly approves GitHub publication.

Current PKB-007 release check result: 32 non-blocking warnings and 0 failures.

## Final Release References

- `docs/FINAL_RELEASE_REVIEW.md`
- `public_release/PUBLIC_REPO_FILE_LIST.md`
- `public_release/WARNING_REVIEW.md`
- `public_release/RELEASE_CHECK_SUMMARY.md`
- `public_release/SCREENSHOT_REVIEW.md`

## GitHub Publish Decision

GitHub publish is complete. PKB-010 published the public showcase repository to
`https://github.com/CHENXJC/PersonalKnowledgeAgent`.

## Publication Boundary

PKB-010 does not connect OpenAI, add RAG, scan other local directories, force
push, or publish private personal knowledge files.
