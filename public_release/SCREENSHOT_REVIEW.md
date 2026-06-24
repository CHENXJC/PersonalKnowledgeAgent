# Screenshot Review

## Current Checkpoint

`PKB-009-GITHUB-PUBLIC-SHOWCASE-PREP`

## Capture Summary

- Screenshot source: Streamlit Dashboard running locally.
- Required dashboard mode: Demo Mode.
- Required data source: `demo_knowledge_base/`.
- Local Private Mode used for screenshots: No.
- Screenshots faked or mocked: No.
- GitHub publication performed: No.
- Real `knowledge_base/` notes included in public showcase by default: No.

## Screenshot Review Table

| File | Status | Source | Demo Mode | Manual review needed |
| --- | --- | --- | --- | --- |
| `01_overview_command_center.png` | captured | Overview page | Yes | Yes |
| `02_demo_mode_source_selector.png` | captured | Sidebar source selector | Yes | Yes |
| `03_knowledge_health_cards.png` | captured | Overview health cards | Yes | Yes |
| `04_project_portfolio_map.png` | captured | Overview portfolio map | Yes | Yes |
| `05_browse_demo_knowledge_base.png` | captured | Browse Knowledge Base page | Yes | Yes |
| `06_search_results_highlight.png` | captured | Search page with `workflow` query | Yes | Yes |
| `07_inventory_report_demo.png` | captured | Inventory Report page | Yes | Yes |
| `08_safety_rules.png` | captured | Safety Rules page | Yes | Yes |
| `09_public_release_check.png` | captured | Actual release-check output rendered as terminal-style PNG | Not applicable | Yes |

## Safety Review

- Contains private personal notes: No.
- Contains real customer data: No.
- Contains credential values: No.
- Contains account recovery material: No.
- Contains local absolute paths: No.
- Contains private identity, legal, tax, medical, bank, or visa material: No.
- Requires full-size manual review before GitHub publication: Yes.

## GitHub Publishing Checklist

Before any public GitHub release:

- [ ] Open every PNG at full size.
- [ ] Confirm all dashboard screenshots show Demo Mode.
- [ ] Confirm no Local Private Mode screenshot is included.
- [ ] Confirm no real `knowledge_base/` preview appears.
- [ ] Confirm no private absolute path appears.
- [ ] Confirm `python tools/check_demo_mode.py` returns PASS.
- [ ] Confirm `python tools/public_release_check.py` returns 0 failures.
- [ ] Confirm real `knowledge_base/` notes remain excluded by default.
- [ ] Get explicit user approval before `git init`, adding a remote, or pushing.

## Recommendation

Use `demo_knowledge_base/` only for the public showcase repository unless the
real `knowledge_base/` is separately reviewed and sanitized.
