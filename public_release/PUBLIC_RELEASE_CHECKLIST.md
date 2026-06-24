# Public Release Checklist

## Safety

- [ ] No `.env` file exists in the release.
- [ ] No API keys, tokens, passwords, or credentials are present.
- [ ] No private identity, passport, visa, bank, tax, medical, or legal files are present.
- [ ] No real private study, career, or personal knowledge files are included.
- [ ] No real emails, phone numbers, addresses, or customer data are present.
- [ ] No private local absolute paths are present in public showcase docs.
- [ ] `outputs/` contains only `.gitkeep` or a reviewed non-sensitive report.

## Demo Data

- [ ] `demo_knowledge_base/` contains only demo/sanitized notes.
- [ ] Demo notes do not contain real accounts, credentials, private paths, or personal identifiers.
- [ ] Screenshots use demo/sanitized content only.

## Validation

- [ ] `python -m pytest`
- [ ] `python -m compileall agent`
- [ ] `python -m py_compile app.py`
- [ ] `python -m agent.kb_scanner`
- [ ] `python -m agent.kb_search QuantLabAgent`
- [ ] `python -m agent.kb_report`
- [ ] `python tools/public_release_check.py`
- [ ] Streamlit smoke check returns HTTP 200.

## Publication

- [ ] No Git repository is initialized until explicitly approved.
- [ ] No GitHub remote is created until explicitly approved.
- [ ] No push is performed until explicitly approved.
- [ ] README explains that public release uses demo/sanitized notes only.
- [ ] GitHub public version is reviewed file-by-file before publication.
