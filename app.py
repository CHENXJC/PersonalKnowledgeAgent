from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import streamlit as st

from agent.kb_dashboard_utils import (
    build_dashboard_metrics,
    extract_project_status_cards,
    get_active_knowledge_source,
    get_category_counts,
    get_files_by_category,
    get_inventory_report_status,
    get_knowledge_source_label,
    get_project_root,
    highlight_keyword,
    is_demo_mode,
    load_project_status,
    load_security_rules,
    safe_read_markdown,
)
from agent.kb_report import generate_inventory_report
from agent.kb_scanner import scan_knowledge_base
from agent.kb_search import search_knowledge_base

CHECKPOINT = "PKB-009-GITHUB-PUBLIC-SHOWCASE-PREP"
NEXT_CHECKPOINT = "PKB-010-GITHUB-PUBLISH"

CATEGORY_DESCRIPTIONS = {
    "01_AI_Projects": "AI Agent, AI Skill, Streamlit, Vibecoding, and GitHub portfolio project notes.",
    "02_University": "University learning, Marketing notes, case studies, and revision outlines.",
    "03_Career": "Career planning, job-search material, portfolio positioning, and interview notes.",
    "04_Business_Ideas": "Business ideas, information gaps, cognition gaps, MVPs, and service concepts.",
    "05_Market_Investment": "Market observations and education-only investment research notes.",
    "06_Personal_Archive": "Low-risk personal learning reviews, reflections, and long-term ideas.",
}

ACTIVE_PROJECTS = ["PersonalKnowledgeAgent", "AgentHubControlCenter"]

PAUSED_PROJECTS = [
    "MarketSenseAgent",
    "VideoExtractSkill",
    "QuantLabAgent",
    "SocialPainFinderAgent",
    "CareerPilotAgent",
    "NewsSignalAgent",
    "BusinessOpsAgent",
]

EXAMPLE_QUERIES = [
    "QuantLabAgent",
    "MarketSenseAgent",
    "workflow",
    "checkpoint",
    "business value",
]


def load_config(project_root: Path) -> dict[str, Any]:
    config_path = project_root / "config" / "kb_config.json"
    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "local_first": True,
            "enable_llm": False,
            "allowed_extensions": [".md", ".txt"],
        }


def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root {
            --pkb-border: #e5e7eb;
            --pkb-muted: #667085;
            --pkb-panel: #ffffff;
            --pkb-soft: #f7f8fa;
            --pkb-text: #111827;
            --pkb-accent: #2563eb;
            --pkb-success: #047857;
            --pkb-warning: #b45309;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        h1, h2, h3 {
            letter-spacing: 0;
        }

        .pkb-hero {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
            border: 1px solid var(--pkb-border);
            border-radius: 20px;
            padding: 30px 32px;
            margin-bottom: 22px;
            box-shadow: 0 18px 44px rgba(15, 23, 42, 0.06);
        }

        .pkb-hero-kicker {
            color: var(--pkb-accent);
            font-size: 0.82rem;
            font-weight: 760;
            margin-bottom: 8px;
            text-transform: uppercase;
        }

        .pkb-hero h1 {
            margin: 0 0 8px 0;
            color: var(--pkb-text);
            font-size: 2.35rem;
            line-height: 1.08;
        }

        .pkb-hero p {
            color: var(--pkb-muted);
            font-size: 1rem;
            margin: 0 0 18px 0;
            max-width: 930px;
        }

        .pkb-badges {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .pkb-badge {
            border: 1px solid var(--pkb-border);
            border-radius: 999px;
            padding: 6px 10px;
            background: #ffffff;
            color: #344054;
            font-size: 0.82rem;
            font-weight: 650;
        }

        .pkb-badge-strong {
            background: #eff6ff;
            border-color: #bfdbfe;
            color: #1d4ed8;
        }

        .pkb-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin: 12px 0 18px 0;
        }

        .pkb-grid-two {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin: 12px 0 18px 0;
        }

        .pkb-card {
            border: 1px solid var(--pkb-border);
            border-radius: 14px;
            padding: 16px 18px;
            background: var(--pkb-panel);
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.04);
            min-height: 112px;
        }

        .pkb-card-title {
            color: var(--pkb-muted);
            font-size: 0.80rem;
            font-weight: 760;
            margin-bottom: 8px;
            text-transform: uppercase;
        }

        .pkb-card-value {
            color: var(--pkb-text);
            font-size: 1.5rem;
            font-weight: 760;
            margin-bottom: 5px;
        }

        .pkb-card-caption {
            color: var(--pkb-muted);
            font-size: 0.86rem;
            line-height: 1.45;
        }

        .pkb-note-card {
            border: 1px solid var(--pkb-border);
            border-radius: 12px;
            padding: 14px 16px;
            background: #ffffff;
            margin-bottom: 10px;
        }

        .pkb-note-title {
            font-weight: 720;
            color: var(--pkb-text);
            margin-bottom: 5px;
        }

        .pkb-note-body {
            color: var(--pkb-muted);
            font-size: 0.92rem;
            line-height: 1.52;
        }

        .pkb-status-line {
            color: #475467;
            font-size: 0.88rem;
            margin-top: 7px;
        }

        .pkb-safety {
            border: 1px solid #fecaca;
            background: #fff1f2;
            color: #991b1b;
            border-radius: 12px;
            padding: 14px 16px;
            font-weight: 650;
            margin-bottom: 16px;
        }

        .pkb-safe-strip {
            border: 1px solid #bbf7d0;
            background: #f0fdf4;
            color: #166534;
            border-radius: 12px;
            padding: 12px 14px;
            font-weight: 650;
            margin: 8px 0 18px 0;
        }

        mark {
            background: #fef3c7;
            color: #92400e;
            border-radius: 4px;
            padding: 1px 3px;
        }

        div[data-testid="stSidebar"] {
            background: #fbfbfd;
        }

        div[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {
            color: #475467;
        }

        @media (max-width: 900px) {
            .pkb-grid, .pkb-grid-two {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        f"""
        <div class="pkb-hero">
            <div class="pkb-hero-kicker">Personal AI Knowledge Command Center</div>
            <h1>PersonalKnowledgeAgent</h1>
            <p>Local-first personal knowledge base for AI projects, university notes, career materials, business ideas, and market observations.</p>
            <div class="pkb-badges">
                <span class="pkb-badge pkb-badge-strong">{CHECKPOINT}</span>
                <span class="pkb-badge">Local-first</span>
                <span class="pkb-badge">No cloud sync</span>
                <span class="pkb-badge">No secrets</span>
                <span class="pkb-badge">Markdown only</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card_html(title: str, value: str, caption: str = "") -> str:
    return (
        '<div class="pkb-card">'
        f'<div class="pkb-card-title">{title}</div>'
        f'<div class="pkb-card-value">{value}</div>'
        f'<div class="pkb-card-caption">{caption}</div>'
        "</div>"
    )


def metric_card(title: str, value: str, caption: str = "") -> None:
    st.markdown(card_html(title, value, caption), unsafe_allow_html=True)


def note_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="pkb-note-card">
            <div class="pkb-note-title">{title}</div>
            <div class="pkb-note-body">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def project_card(card: dict[str, str]) -> None:
    st.markdown(
        f"""
        <div class="pkb-note-card">
            <div class="pkb-note-title">{card['project_name']}</div>
            <div class="pkb-note-body">{card['portfolio_value']}</div>
            <div class="pkb-status-line"><strong>Stage:</strong> {card['stage']}</div>
            <div class="pkb-status-line"><strong>Checkpoint:</strong> {card['checkpoint']}</div>
            <div class="pkb-status-line"><strong>Pause rule:</strong> {card['pause_rule']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(
    project_root: Path,
    config: dict[str, Any],
    categories: list[str],
) -> tuple[str, str, str, bool, str]:
    st.sidebar.markdown("## Dashboard Navigation")
    page = st.sidebar.radio(
        "Select page",
        [
            "Overview",
            "Browse Knowledge Base",
            "Search",
            "Inventory Report",
            "Project Status",
            "Safety Rules",
        ],
        label_visibility="collapsed",
    )

    st.sidebar.markdown("## Knowledge Source Mode")
    default_mode = str(config.get("default_knowledge_source_mode", "demo")).lower()
    mode_options = ["demo", "private"]
    default_index = 1 if default_mode == "private" else 0
    source_mode = st.sidebar.selectbox(
        "Knowledge source",
        mode_options,
        index=default_index,
        format_func=lambda mode: (
            "Demo Mode: demo_knowledge_base"
            if mode == "demo"
            else "Local Private Mode: knowledge_base"
        ),
    )
    st.sidebar.caption(get_knowledge_source_label(source_mode))

    st.sidebar.markdown("## Search")
    search_query = st.sidebar.text_input(
        "Search input",
        value="",
        placeholder="Search projects, checkpoints, workflows, business ideas...",
    )

    category_options = ["All", *categories]
    category_filter = st.sidebar.selectbox("Category filter", category_options)
    refresh_report = st.sidebar.button("Refresh inventory report", use_container_width=True)

    st.sidebar.markdown("## Project Metadata")
    st.sidebar.caption(f"Project: `{project_root.name}`")
    st.sidebar.caption(f"Current checkpoint: `{CHECKPOINT}`")
    st.sidebar.caption(f"LLM enabled: `{bool(config.get('enable_llm', False))}`")

    return page, search_query, category_filter, refresh_report, source_mode


def get_report_filename(source_mode: str) -> str:
    """Return the inventory report filename for the active source mode."""
    return "demo_kb_inventory_report.md" if is_demo_mode(source_mode) else "kb_inventory_report.md"


def render_source_mode_banner(source_mode: str, active_source: Path) -> None:
    """Render the current source mode and public screenshot warning."""
    source_label = get_knowledge_source_label(source_mode)
    if is_demo_mode(source_mode):
        st.success(f"{source_label}. Active source: `{active_source.name}`")
    else:
        st.warning(
            "Local Private Mode: Local personal notes, not for public screenshots. "
            "Do not use Local Private Mode for GitHub screenshots or public demo publishing."
        )


def render_command_center_summary(
    metrics: dict[str, Any], source_mode: str, active_source: Path
) -> None:
    st.markdown("## Command Center Summary")
    st.markdown(
        f"""
        <div class="pkb-safe-strip">
        Current source: {get_knowledge_source_label(source_mode)}. Active folder: {active_source.name}.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="pkb-grid-two">'
        + card_html("Current checkpoint", CHECKPOINT, "Local GitHub public showcase prep")
        + card_html("Knowledge source", active_source.name, get_knowledge_source_label(source_mode))
        + card_html("Local-first", str(metrics["local_first"]), "Designed for local portfolio workflow")
        + card_html("LLM enabled", str(metrics["llm_enabled"]), "No OpenAI/RAG in this checkpoint")
        + card_html("Cloud sync", "False", "No uploads or remote sync")
        + card_html("Safety mode", "On", "Secrets and binary files stay out of scope")
        + "</div>",
        unsafe_allow_html=True,
    )


def render_health_cards(metrics: dict[str, Any], report_filename: str) -> None:
    report_label = "Ready" if metrics["inventory_report_exists"] else "Missing"
    st.markdown("## Knowledge Health Cards")
    st.markdown(
        '<div class="pkb-grid">'
        + card_html("Total files", str(metrics["total_files"]), "Markdown/TXT files scanned")
        + card_html("Total categories", str(metrics["total_categories"]), "Categories currently containing notes")
        + card_html("AI project notes", str(metrics["ai_project_notes"]), "Portfolio project summaries")
        + card_html("Business idea notes", str(metrics["business_idea_notes"]), "Idea and service concept notes")
        + card_html("Inventory report", report_label, f"outputs/{report_filename}")
        + card_html("Safety mode", "Local safe", "No cloud sync / no secrets")
        + "</div>",
        unsafe_allow_html=True,
    )


def render_project_portfolio_map(project_cards: list[dict[str, str]]) -> None:
    st.markdown("## Project Portfolio Map")
    card_by_name = {card["project_name"]: card for card in project_cards}
    rendered_names: set[str] = set()
    personal_card = {
        "project_name": "PersonalKnowledgeAgent",
        "checkpoint": CHECKPOINT,
        "stage": "Active local dashboard project",
        "portfolio_value": "Shows local-first knowledge management, dashboard UX, and AI portfolio organization.",
        "pause_rule": "Pause after GitHub Public Showcase + Profile Pin unless explicitly resumed.",
    }

    col_active, col_paused = st.columns(2)
    with col_active:
        st.markdown("### Active Projects")
        for name in ACTIVE_PROJECTS:
            if name == "PersonalKnowledgeAgent":
                project_card(personal_card)
                rendered_names.add(name)
            elif name in card_by_name:
                project_card(card_by_name[name])
                rendered_names.add(name)
    with col_paused:
        st.markdown("### Completed / Paused Projects")
        for name in PAUSED_PROJECTS:
            if name in card_by_name:
                project_card(card_by_name[name])
                rendered_names.add(name)

    demo_cards = [
        card for card in project_cards if card["project_name"] not in rendered_names
    ]
    if demo_cards:
        st.markdown("### Demo Project Notes")
        for card in demo_cards:
            project_card(card)


def render_overview(
    scan_results: list[dict[str, Any]],
    metrics: dict[str, Any],
    project_cards: list[dict[str, str]],
    source_mode: str,
    active_source: Path,
    report_filename: str,
) -> None:
    st.markdown("## Overview")
    render_command_center_summary(metrics, source_mode, active_source)
    render_health_cards(metrics, report_filename)

    st.markdown("## Knowledge Categories")
    cat_cols = st.columns(2)
    category_counts = get_category_counts(scan_results)
    for index, (category, description) in enumerate(CATEGORY_DESCRIPTIONS.items()):
        count = category_counts.get(category, 0)
        with cat_cols[index % 2]:
            note_card(category, f"{description}<br><strong>{count}</strong> file(s) currently indexed.")

    render_project_portfolio_map(project_cards)


def render_browse(
    scan_results: list[dict[str, Any]],
    files_by_category: dict[str, list[dict[str, Any]]],
    kb_root: Path,
    category_filter: str,
    source_mode: str,
) -> None:
    st.markdown("## Browse Knowledge Base")
    st.caption(
        f"Browse only reads Markdown/TXT files discovered inside `{kb_root.name}`. "
        f"{get_knowledge_source_label(source_mode)}."
    )

    st.markdown("### Category File Counts")
    count_cols = st.columns(3)
    for index, category in enumerate(CATEGORY_DESCRIPTIONS):
        count = len(files_by_category.get(category, []))
        with count_cols[index % 3]:
            metric_card(category, str(count), "indexed note(s)")

    visible_results = [
        item
        for item in scan_results
        if category_filter == "All" or item["category_dir"] == category_filter
    ]

    if not visible_results:
        st.info("No Markdown/TXT notes found for the selected category yet.")
        return

    st.markdown("### Select A Knowledge Note")
    for category in CATEGORY_DESCRIPTIONS:
        items = files_by_category.get(category, [])
        if category_filter != "All" and category != category_filter:
            continue
        if not items:
            with st.expander(f"{category} (0)", expanded=False):
                st.info("This category is ready, but no Markdown/TXT notes have been added yet.")
            continue
        with st.expander(f"{category} ({len(items)})", expanded=category_filter != "All"):
            for item in items:
                st.markdown(f"- `{item['relative_path']}`")

    option_map = {item["relative_path"]: item for item in visible_results}
    selected_relative_path = st.selectbox(
        "Open a note",
        list(option_map.keys()),
        index=0,
    )
    selected_item = option_map[selected_relative_path]

    st.markdown("### File Details")
    detail_cols = st.columns(4)
    detail_cols[0].metric("File name", selected_item["file_name"])
    detail_cols[1].metric("Category", selected_item["category_dir"])
    detail_cols[2].metric("Characters", selected_item["char_count"])
    detail_cols[3].metric("Lines", selected_item["line_count"])
    st.caption(f"Relative path: `{selected_item['relative_path']}`")

    st.markdown("### Markdown Preview")
    content = safe_read_markdown(Path(selected_item["file_path"]), kb_root)
    st.markdown(content)


def render_search(
    kb_root: Path, sidebar_query: str, category_filter: str, source_mode: str
) -> None:
    st.markdown("## Search")
    st.caption(
        f"Keyword search is local, case-insensitive, and limited to Markdown/TXT notes in `{kb_root.name}`. "
        f"{get_knowledge_source_label(source_mode)}."
    )

    if "search_query" not in st.session_state:
        st.session_state.search_query = sidebar_query or "QuantLabAgent"
    elif sidebar_query:
        st.session_state.search_query = sidebar_query

    example_cols = st.columns(len(EXAMPLE_QUERIES))
    for col, example in zip(example_cols, EXAMPLE_QUERIES):
        with col:
            if st.button(example, use_container_width=True):
                st.session_state.search_query = example

    query = st.text_input(
        "Keyword",
        value=st.session_state.search_query,
        placeholder="Search projects, checkpoints, workflows, business ideas...",
    )
    st.session_state.search_query = query

    if not query.strip():
        st.info("Enter a keyword to search the local knowledge base.")
        return

    results = search_knowledge_base(str(kb_root), query)
    if category_filter != "All":
        results = [item for item in results if item["category_dir"] == category_filter]

    st.markdown(f"### Search Results ({len(results)})")
    if not results:
        st.info(
            "No results found. Try another keyword, check spelling, or import more sanitized notes in PKB-002/future stages."
        )
        return

    for item in results:
        highlighted = highlight_keyword(item["snippet"], query)
        st.markdown(
            f"""
            <div class="pkb-note-card">
                <div class="pkb-note-title">{item['file_name']} · {item['category_dir']} · line {item['line_number']}</div>
                <div class="pkb-note-body">{highlighted}</div>
                <div class="pkb-status-line">Source: {item['relative_path']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_inventory(project_root: Path, kb_root: Path, source_mode: str) -> None:
    st.markdown("## Inventory Report")
    report_filename = get_report_filename(source_mode)
    report_path = project_root / "outputs" / report_filename
    st.caption(
        f"Generate and inspect the Markdown/TXT inventory report for `{kb_root.name}`."
    )

    status = get_inventory_report_status(project_root, report_filename)
    status_label = "Ready" if status["exists"] else "Missing"
    cols = st.columns(3)
    cols[0].metric("Report status", status_label)
    cols[1].metric("Size", str(status["size_chars"]))
    cols[2].metric("Path", status["path"])

    if st.button("Regenerate inventory report", use_container_width=False):
        generated_path = generate_inventory_report(str(kb_root), str(report_path))
        st.success(f"Inventory report generated: {Path(generated_path).name}")

    if not report_path.exists():
        report_path = Path(generate_inventory_report(str(kb_root), str(report_path)))
        st.success("Inventory report generated.")

    st.markdown(safe_read_markdown(report_path, project_root))


def render_project_status(project_root: Path) -> None:
    st.markdown("## Project Status")
    st.info(f"Current checkpoint: {CHECKPOINT}. Next checkpoint: {NEXT_CHECKPOINT}.")
    st.markdown(load_project_status(project_root))


def render_safety_rules(project_root: Path) -> None:
    st.markdown("## Safety Rules")
    st.markdown(
        """
        <div class="pkb-safety">
        This dashboard supports Demo Mode for public screenshots. Do not use
        Local Private Mode for GitHub screenshots or public demo publishing.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(load_security_rules(project_root))


def main() -> None:
    st.set_page_config(
        page_title="PersonalKnowledgeAgent",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    project_root = get_project_root()
    config = load_config(project_root)
    categories = list(CATEGORY_DESCRIPTIONS.keys())

    page, sidebar_query, category_filter, refresh_report, source_mode = render_sidebar(
        project_root=project_root,
        config=config,
        categories=categories,
    )

    kb_root = get_active_knowledge_source(project_root, source_mode)
    report_filename = get_report_filename(source_mode)
    scan_results = scan_knowledge_base(str(kb_root))
    files_by_category = get_files_by_category(scan_results)
    metrics = build_dashboard_metrics(scan_results, project_root, report_filename)
    project_files = [
        item for item in scan_results if item["category_dir"] == "01_AI_Projects"
    ]
    project_cards = extract_project_status_cards(project_files, kb_root)

    if refresh_report:
        report_path = generate_inventory_report(
            str(kb_root), str(project_root / "outputs" / report_filename)
        )
        st.sidebar.success(f"Generated {Path(report_path).name}")

    render_hero()
    render_source_mode_banner(source_mode, kb_root)

    if page == "Overview":
        render_overview(
            scan_results,
            metrics,
            project_cards,
            source_mode,
            kb_root,
            report_filename,
        )
    elif page == "Browse Knowledge Base":
        render_browse(scan_results, files_by_category, kb_root, category_filter, source_mode)
    elif page == "Search":
        render_search(kb_root, sidebar_query, category_filter, source_mode)
    elif page == "Inventory Report":
        render_inventory(project_root, kb_root, source_mode)
    elif page == "Project Status":
        render_project_status(project_root)
    elif page == "Safety Rules":
        render_safety_rules(project_root)


if __name__ == "__main__":
    main()
