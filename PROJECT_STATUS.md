# Project Status

## Current Checkpoint

- Current checkpoint: `PKB-009-GITHUB-PUBLIC-SHOWCASE-PREP`
- Current status: GitHub public showcase prep completed locally
- Default knowledge source mode: Demo Mode
- Public demo source: `demo_knowledge_base/`
- Real private knowledge base policy: excluded from public showcase by default
- Screenshot status: 9 PNG screenshots captured from Demo Mode
- Local-first: Yes
- LLM/RAG enabled: No
- Cloud sync: No
- Git initialized: No
- GitHub remote: No
- Push performed: No

## Completed Items

- Updated `.gitignore` to exclude real `knowledge_base/` notes by default.
- Added `knowledge_base/README.md` as the public placeholder explanation.
- Added `knowledge_base/.gitkeep`.
- Confirmed `demo_knowledge_base/` remains the public demo source.
- Confirmed `portfolio/showcase_screenshots/*.png` remains eligible for public release.
- Updated README with PKB-009 public showcase prep policy.
- Updated public repository file list.
- Updated public showcase manifest.
- Updated final release review.
- Updated screenshot review.
- Updated release check summary and warning review.
- Added `docs/GITHUB_PUBLISH_GUIDE.md` for future manual publish approval.
- Confirmed no GitHub publication was performed.

## Public Release File Policy

Safe to include after review:

- `app.py`
- `agent/`
- `config/kb_config.json`
- `demo_knowledge_base/`
- `docs/`
- `public_release/`
- `portfolio/showcase_screenshots/`
- `tests/`
- `tools/`
- `README.md`
- `PROJECT_STATUS.md`
- `requirements.txt`
- `.gitignore`
- `knowledge_base/README.md`
- `knowledge_base/.gitkeep`
- `outputs/.gitkeep`

Excluded by default:

- Real notes under `knowledge_base/`
- Generated reports under `outputs/`, except `outputs/.gitkeep`
- `.env`, key files, credential files, logs, raw private files, and unreviewed
  media or documents

## Validation Results

- `python -m pytest`: passed, 27 tests passed.
- `python -m compileall agent`: passed.
- `python -m py_compile app.py`: passed.
- `python tools/check_demo_mode.py`: passed, Status PASS, 0 warnings, 0 failures.
- `python tools/public_release_check.py`: Status WARNING, 66 scanned text files, 32 warnings, 0 failures.
- `python -m agent.kb_report`: passed.
- Streamlit smoke check: passed, HTTP 200 on `127.0.0.1:8521`.

## Safety Notes

- Demo Mode default: confirmed.
- Local Private Mode screenshots: not used.
- Real private `knowledge_base/` content copied to `public_release/`: No.
- Real private `knowledge_base/` content copied to `demo_knowledge_base/`: No.
- Fake or blank screenshots generated: No.
- No `.env`, API key, token, password, secret, credential, passport, bank card,
  visa file, or private identity file was intentionally read or imported.
- No PDF, Excel, video, audio, or private binary file was read.
- No other local project directory was scanned.
- No OpenAI API, RAG, local model, embedding, vector store, cloud sync, GitHub
  remote, or push was used.

## Not Included

- No OpenAI API integration.
- No local model integration.
- No embeddings or vector database.
- No cloud sync.
- No GitHub public showcase release.
- No Git initialization.
- No GitHub remote.
- No push.

## Next Checkpoint

- Recommended next checkpoint: `PKB-010-GITHUB-PUBLISH`
- Alternative next checkpoint: `PKB-010-PROFILE-PIN-DECISION`

Recommendation: do not add RAG/OpenAI next. The next step is GitHub publishing
only after explicit user approval, followed by online README/screenshot review
and a GitHub profile pin decision.
