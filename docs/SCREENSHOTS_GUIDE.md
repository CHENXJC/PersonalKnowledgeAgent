# Screenshots Guide

This guide defines the captured screenshots for the PersonalKnowledgeAgent
GitHub public showcase preparation.

## Current Capture Status

- Current checkpoint: `PKB-009-GITHUB-PUBLIC-SHOWCASE-PREP`
- Capture status: 9 screenshots captured
- Capture source: live Streamlit Dashboard and actual release-check output
- Required dashboard mode: Demo Mode
- Required data source: `demo_knowledge_base/`
- Manual full-size review before GitHub publication: required

## Required Mode

Always switch to Demo Mode before capturing public screenshots.

```text
Knowledge Source Mode -> Demo Mode: demo_knowledge_base
```

Do not use Local Private Mode for GitHub screenshots or public demo publishing.

## Screenshot Safety Checklist

Before every screenshot, confirm:

- Demo Mode is selected.
- The dashboard only shows demo/sanitized notes.
- No real private knowledge base content is visible.
- No `.env`, API key, token, password, secret, credential, or recovery code is visible.
- No passport, identity document, bank card, visa, medical, tax, legal, or account file is visible.
- No private customer data, job application data, private university record, or full private generated report is visible.
- No local absolute path, private username, unrelated browser tab, or desktop notification is visible.
- Search results and inventory report previews do not expose private file names.

## Recommended Screenshot Names

## 01_overview_command_center.png

- Status: captured
- Page: Overview
- Required mode: Demo Mode
- Focus: Hero header, source mode banner, and Command Center Summary
- Check before capture: checkpoint, source mode label, local-first labels, and safety mode do not expose private data

## 02_demo_mode_source_selector.png

- Status: captured
- Page: any page with sidebar visible
- Required mode: Demo Mode
- Focus: Knowledge Source Mode selector showing `Demo Mode: demo_knowledge_base`
- Check before capture: Local Private Mode is not selected

## 03_knowledge_health_cards.png

- Status: captured
- Page: Overview
- Required mode: Demo Mode
- Focus: Total files, total categories, AI project notes, business idea notes, inventory report status, and safety mode
- Check before capture: counts are safe to show and do not reveal private file names

## 04_project_portfolio_map.png

- Status: captured
- Page: Overview
- Required mode: Demo Mode
- Focus: Demo project notes and project portfolio map area
- Check before capture: all visible notes are demo/sanitized summaries only

## 05_browse_demo_knowledge_base.png

- Status: captured
- Page: Browse Knowledge Base
- Required mode: Demo Mode
- Focus: Category counts, file details, relative path, and Markdown preview from `demo_knowledge_base/`
- Check before capture: selected note contains only demo/sample content

## 06_search_results_highlight.png

- Status: captured
- Page: Search
- Required mode: Demo Mode
- Focus: Search examples, result count, result cards, line numbers, and keyword highlighting
- Check before capture: search results do not show secrets, credentials, private application data, or real identity material

## 07_inventory_report_demo.png

- Status: captured
- Page: Inventory Report
- Required mode: Demo Mode
- Focus: `outputs/demo_kb_inventory_report.md` status, category stats, and generated demo inventory content
- Check before capture: report uses safe source labels and does not expose private paths or sensitive files

## 08_safety_rules.png

- Status: captured
- Page: Safety Rules
- Required mode: Demo Mode
- Focus: dashboard safety warning and public showcase boundaries
- Check before capture: page clearly states demo/sanitized Markdown/TXT only

## 09_public_release_check.png

- Status: captured
- Source: terminal output from `python tools/public_release_check.py`
- Required condition: 0 failures
- Focus: PASS/WARNING/FAIL summary and scanned file count
- Check before capture: terminal output does not reveal private paths, usernames, tokens, or credentials

## Screenshot Publication Rule

Save reviewed images to:

```text
portfolio/showcase_screenshots/
```

Do not publish screenshots until each image has been manually inspected at full
size.

If screenshots are replaced later, rerun:

```powershell
python tools/check_demo_mode.py
python tools/public_release_check.py
```
