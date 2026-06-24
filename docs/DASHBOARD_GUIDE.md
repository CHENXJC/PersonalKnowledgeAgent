# Dashboard Guide

## How To Start

Run the dashboard from the project root:

```powershell
cd PersonalKnowledgeAgent
streamlit run app.py
```

Optional fixed port:

```powershell
streamlit run app.py --server.port 8521
```

## Pages

## Knowledge Source Mode

The sidebar includes a fixed Knowledge Source Mode selector:

- Demo Mode: `demo_knowledge_base`
- Local Private Mode: `knowledge_base`

Demo Mode is selected by default and should be used for public screenshots.
Local Private Mode is for local personal review only and must not be used for
GitHub screenshots or public demo publishing.

## Overview

Shows the current checkpoint, core safety labels, file counts, AI project note count, business idea note count, local-first state, LLM state, category descriptions, active projects, and completed/paused projects.

## Browse Knowledge Base

Scans the selected source folder and displays Markdown/TXT files by category.
Opening a note uses safe path checks and only reads files inside the active
knowledge source root.

## Search

Runs local keyword search across Markdown/TXT files in the selected source.
Search is case-insensitive and can be filtered by category.

Search result snippets highlight the matched keyword with a small inline mark. Use the example buttons for common portfolio queries:

- QuantLabAgent
- MarketSenseAgent
- workflow
- checkpoint
- business value

## Inventory Report

Generates and displays the inventory report for the selected source. Demo Mode
uses `outputs/demo_kb_inventory_report.md`; Local Private Mode uses
`outputs/kb_inventory_report.md`. The report contains file counts, category
stats, AI project file list, business idea file list, and generation time.

To regenerate the report, open the Inventory Report page and click `Regenerate inventory report`, or run:

```powershell
python -m agent.kb_report
```

## Project Status

Displays `PROJECT_STATUS.md` and shows the current and next checkpoint.

## Safety Rules

Displays `docs/SECURITY_RULES.md` with an additional warning that the dashboard should only use sanitized local notes.

## Project Cards

The Overview page includes a Project Portfolio Map. Each project card shows:

- Project name
- Current checkpoint
- Current stage/status
- Portfolio value
- Pause rule

The project cards are extracted from sanitized Markdown summaries under `knowledge_base/01_AI_Projects/`.

## Safe Screenshots

Use `docs/SCREENSHOTS_GUIDE.md` before preparing screenshots for GitHub.

Before taking screenshots:

- Use sanitized demo/sample notes only.
- Use Demo Mode before public screenshots.
- Do not use Local Private Mode for public screenshots.
- Do not show secrets, tokens, credentials, identity documents, or private logs.
- Confirm search results do not expose private notes.
- Confirm the Inventory Report does not show private file names or sensitive paths.

## Safety Boundary

- The dashboard only reads `.md` and `.txt`.
- The Browse page only opens files inside `knowledge_base/`.
- The dashboard will not open Markdown/TXT files outside the allowed root.
- The dashboard does not read `.env`, API keys, tokens, passwords, or secret files.
- The dashboard does not read PDF, Excel, images, videos, or binary files.
- The dashboard does not upload files.
- The dashboard does not sync cloud storage.
- The dashboard does not call OpenAI or any other API.
- The dashboard does not create a GitHub remote or push code.

## Common Issues

## Streamlit Command Not Found

Install dependencies in your project environment:

```powershell
pip install -r requirements.txt
```

## Search Has No Results

Try one of the default keywords:

- QuantLabAgent
- MarketSenseAgent
- business
- workflow

## Report Is Missing

Open the Inventory Report page and click `Regenerate inventory report`, or run:

```powershell
python -m agent.kb_report
```

## Next Route

The current checkpoint is `PKB-006-DEMO-MODE-AND-SCREENSHOTS`, focused on demo
mode and screenshot readiness. The next recommended checkpoint is
`PKB-007-FINAL-PUBLIC-RELEASE-CHECK`. Optional RAG should wait until after
public showcase safety and final release checks are complete.
