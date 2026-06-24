# Showcase Screenshots

PKB-009 refreshed the public showcase screenshot set using Demo Mode and
`demo_knowledge_base/`.

## Required Safety Rule

Every public screenshot must use Demo Mode. Do not use Local Private Mode for
GitHub screenshots or public demo publishing.

Before publishing, inspect every PNG at full size and confirm:

- Demo Mode is selected.
- Only demo/sanitized notes are visible.
- No private notes are visible.
- No secrets, credentials, account details, or recovery codes are visible.
- No absolute local path or private username is visible.
- No identity, bank, tax, medical, legal, or customer material is visible.

## Screenshot List

| File | Status | Page / Source | Safety status |
| --- | --- | --- | --- |
| `01_overview_command_center.png` | captured | Streamlit Overview | Demo Mode only |
| `02_demo_mode_source_selector.png` | captured | Streamlit sidebar source selector | Demo Mode only |
| `03_knowledge_health_cards.png` | captured | Streamlit Overview, health cards | Demo Mode only |
| `04_project_portfolio_map.png` | captured | Streamlit Overview, portfolio map | Demo Mode only |
| `05_browse_demo_knowledge_base.png` | captured | Streamlit Browse Knowledge Base | Demo Mode only |
| `06_search_results_highlight.png` | captured | Streamlit Search, query `workflow` | Demo Mode only |
| `07_inventory_report_demo.png` | captured | Streamlit Inventory Report | Demo Mode only |
| `08_safety_rules.png` | captured | Streamlit Safety Rules | Demo Mode only |
| `09_public_release_check.png` | captured | Actual `public_release_check.py` output rendered for review | 0 failures required |

## Recommended GitHub README Order

1. Overview Command Center
2. Demo Mode Source Selector
3. Knowledge Health Cards
4. Project Portfolio Map
5. Browse Demo Knowledge Base
6. Search Results Highlight
7. Inventory Report Demo
8. Safety Rules
9. Public Release Check

## Replacement Rule

If any screenshot is replaced later, rerun:

```powershell
python tools/check_demo_mode.py
python tools/public_release_check.py
```

Then update `public_release/SCREENSHOT_REVIEW.md` before any GitHub release.
