# GitHub Publish Guide

This guide is for a future GitHub Public Showcase release. It is documentation
only. Do not execute these commands unless the user explicitly approves the
publish step.

## Pre-Publish Manual Confirmation

Before publishing, confirm:

- `.gitignore` excludes real `knowledge_base/` notes by default.
- `knowledge_base/README.md` and `knowledge_base/.gitkeep` are the only intended
  public files under `knowledge_base/`.
- `demo_knowledge_base/` is included as the public demo source.
- `portfolio/showcase_screenshots/` contains reviewed public PNG screenshots.
- `outputs/` generated reports are excluded except `outputs/.gitkeep`.
- No private notes, account records, identity files, or raw personal files are
  included.
- No OpenAI/RAG integration is included yet.

## Required Local Checks

Run these before any publish decision:

```powershell
python -m pytest
python -m compileall agent
python -m py_compile app.py
python tools/check_demo_mode.py
python tools/public_release_check.py
```

Expected gate:

- Tests pass.
- Compile checks pass.
- Demo Mode check returns PASS.
- Public release check has 0 failures.

## Publish Commands For Future Approval Only

Do not run these commands until the user explicitly approves GitHub publishing:

```powershell
git init
git branch -M main
git add .
git status
git commit -m "Add PersonalKnowledgeAgent public showcase version"
gh repo create CHENXJC/PersonalKnowledgeAgent --public --source=. --remote=origin --push
```

If GitHub CLI is unavailable, stop after the local commit and ask the user to
create an empty public repository manually before adding a remote.

## Current Boundary

PKB-009 is local publish preparation only. It does not initialize Git, add a
remote, push code, connect cloud services, or add RAG/OpenAI functionality.
