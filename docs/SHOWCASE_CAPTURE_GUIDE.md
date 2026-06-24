# Showcase Capture Guide

Use this guide to prepare and review PersonalKnowledgeAgent screenshots for a
future GitHub public showcase.

## PKB-009 Capture Status

- Current checkpoint: `PKB-009-GITHUB-PUBLIC-SHOWCASE-PREP`
- Status: screenshots refreshed using Demo Mode
- Captured PNG count: 9
- Screenshot directory: `portfolio/showcase_screenshots/`
- Manual full-size review before GitHub publication: required

## Start The Dashboard

From the project root:

```powershell
streamlit run app.py --server.port 8521
```

Open:

```text
http://127.0.0.1:8521
```

## Switch To Demo Mode

In the sidebar, set:

```text
Knowledge Source Mode -> Demo Mode: demo_knowledge_base
```

Demo Mode is the default. It reads `demo_knowledge_base/` and is the only
recommended mode for public screenshots.

Do not use Local Private Mode for GitHub screenshots or public demo publishing.

## PKB-007 Pre-Screenshot Checks

Before capturing screenshots, run:

```powershell
python tools/check_demo_mode.py
python tools/public_release_check.py
```

Required result:

- `check_demo_mode`: PASS
- `public_release_check`: 0 failures

Warnings are allowed only when they are non-blocking safety documentation,
tests, or checker pattern examples.

Latest PKB-007 result:

- `check_demo_mode`: PASS, 0 warnings, 0 failures.
- `public_release_check`: WARNING, 32 warnings, 0 failures.
- Streamlit smoke check: HTTP 200 on `127.0.0.1:8521`.

## Screenshot List

Save screenshots to:

```text
portfolio/showcase_screenshots/
```

Captured files:

1. `01_overview_command_center.png`
   - Status: captured
   - Page: Overview
   - Capture: hero, source banner, Command Center Summary
2. `02_demo_mode_source_selector.png`
   - Status: captured
   - Page: any page with sidebar visible
   - Capture: Knowledge Source Mode selector set to Demo Mode
3. `03_knowledge_health_cards.png`
   - Status: captured
   - Page: Overview
   - Capture: Knowledge Health Cards
4. `04_project_portfolio_map.png`
   - Status: captured
   - Page: Overview
   - Capture: demo project card section
5. `05_browse_demo_knowledge_base.png`
   - Status: captured
   - Page: Browse Knowledge Base
   - Capture: demo note selector and Markdown preview
6. `06_search_results_highlight.png`
   - Status: captured
   - Page: Search
   - Capture: demo search result highlighting
7. `07_inventory_report_demo.png`
   - Status: captured
   - Page: Inventory Report
   - Capture: demo report status and preview
8. `08_safety_rules.png`
   - Status: captured
   - Page: Safety Rules
   - Capture: dashboard safety warning and public boundaries
9. `09_public_release_check.png`
   - Status: captured
   - Source: terminal
   - Capture: `python tools/public_release_check.py` output with 0 failures

## Before Each Screenshot

Confirm:

- Demo Mode is selected.
- No real personal note is visible.
- No token, password, API key, credential, or recovery code is visible.
- No local absolute path is visible.
- No identity, passport, visa, bank, tax, medical, legal, or account file is visible.
- No private browser tab, notification, username, or desktop detail is visible.

## Forbidden

- Do not upload real `knowledge_base/` content.
- Do not capture Local Private Mode for public materials.
- Do not publish screenshots before full-size manual review.

## Manual Recapture Flow

If any screenshot needs to be replaced:

1. Run `python tools/check_demo_mode.py`.
2. Start the dashboard with `streamlit run app.py --server.port 8521`.
3. Confirm the sidebar source is Demo Mode.
4. Capture only demo/sanitized pages.
5. Save PNG files using the exact names in this guide.
6. Run `python tools/public_release_check.py`.
7. Update `public_release/SCREENSHOT_REVIEW.md`.
