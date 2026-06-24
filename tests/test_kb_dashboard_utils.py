from pathlib import Path

from agent.kb_dashboard_utils import (
    build_dashboard_metrics,
    extract_project_status_cards,
    get_active_knowledge_source,
    get_category_counts,
    get_files_by_category,
    get_inventory_report_status,
    get_knowledge_source_label,
    highlight_keyword,
    is_demo_mode,
    safe_read_markdown,
)


def test_safe_read_markdown_reads_allowed_markdown(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    kb_root.mkdir()
    note = kb_root / "Sample.md"
    note.write_text("# Sample\n\nAllowed note.", encoding="utf-8")

    assert "Allowed note" in safe_read_markdown(note, kb_root)


def test_safe_read_markdown_rejects_file_outside_allowed_root(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    outside_root = tmp_path / "outside"
    kb_root.mkdir()
    outside_root.mkdir()
    outside_file = outside_root / "Private.md"
    outside_file.write_text("# Private", encoding="utf-8")

    result = safe_read_markdown(outside_file, kb_root)

    assert "Security notice" in result
    assert "Private" not in result


def test_safe_read_markdown_only_allows_markdown_and_text(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    kb_root.mkdir()
    blocked_file = kb_root / "data.csv"
    blocked_file.write_text("secret,value", encoding="utf-8")

    result = safe_read_markdown(blocked_file, kb_root)

    assert "only .md and .txt" in result
    assert "secret,value" not in result


def test_get_category_counts_returns_counts():
    scan_results = [
        {"category_dir": "01_AI_Projects", "relative_path": "01_AI_Projects/A.md"},
        {"category_dir": "01_AI_Projects", "relative_path": "01_AI_Projects/B.md"},
        {
            "category_dir": "04_Business_Ideas",
            "relative_path": "04_Business_Ideas/C.md",
        },
    ]

    counts = get_category_counts(scan_results)

    assert counts["01_AI_Projects"] == 2
    assert counts["04_Business_Ideas"] == 1


def test_get_files_by_category_groups_results():
    scan_results = [
        {
            "category_dir": "04_Business_Ideas",
            "relative_path": "04_Business_Ideas/C.md",
        },
        {"category_dir": "01_AI_Projects", "relative_path": "01_AI_Projects/A.md"},
    ]

    grouped = get_files_by_category(scan_results)

    assert list(grouped) == ["01_AI_Projects", "04_Business_Ideas"]
    assert grouped["01_AI_Projects"][0]["relative_path"] == "01_AI_Projects/A.md"


def test_highlight_keyword_is_case_insensitive():
    result = highlight_keyword("QuantLabAgent uses quant workflows.", "quant")

    assert "<mark>Quant</mark>LabAgent" in result
    assert "<mark>quant</mark> workflows" in result


def test_highlight_keyword_returns_original_when_keyword_empty():
    text = "No search term."

    assert highlight_keyword(text, "") == text


def test_get_inventory_report_status_detects_report(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    outputs = project_root / "outputs"
    outputs.mkdir(parents=True)
    (outputs / "kb_inventory_report.md").write_text("# Report", encoding="utf-8")

    status = get_inventory_report_status(project_root)

    assert status["exists"] is True
    assert status["path"] == "outputs/kb_inventory_report.md"
    assert status["size_chars"] == len("# Report")


def test_build_dashboard_metrics_returns_total_files(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    scan_results = [
        {"category_dir": "01_AI_Projects", "relative_path": "01_AI_Projects/A.md"},
        {
            "category_dir": "04_Business_Ideas",
            "relative_path": "04_Business_Ideas/B.md",
        },
    ]

    metrics = build_dashboard_metrics(scan_results, project_root)

    assert metrics["total_files"] == 2
    assert metrics["total_categories"] == 2
    assert metrics["ai_project_notes"] == 1
    assert metrics["business_idea_notes"] == 1
    assert metrics["inventory_report_exists"] is False


def test_get_active_knowledge_source_returns_demo_path(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    project_root.mkdir()

    result = get_active_knowledge_source(project_root, "demo")

    assert result == (project_root / "demo_knowledge_base").resolve()


def test_get_active_knowledge_source_returns_private_path(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    project_root.mkdir()

    result = get_active_knowledge_source(project_root, "private")

    assert result == (project_root / "knowledge_base").resolve()


def test_get_active_knowledge_source_defaults_unknown_mode_to_demo(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    project_root.mkdir()

    result = get_active_knowledge_source(project_root, "unexpected")

    assert result == (project_root / "demo_knowledge_base").resolve()


def test_get_knowledge_source_label_and_demo_mode():
    assert get_knowledge_source_label("demo") == "Demo Mode: Safe public demo content"
    assert (
        get_knowledge_source_label("private")
        == "Local Private Mode: Local personal notes, not for public screenshots"
    )
    assert is_demo_mode("demo") is True
    assert is_demo_mode("private") is False
    assert is_demo_mode("unknown") is True


def test_extract_project_status_cards_reads_project_fields(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    project_dir = kb_root / "01_AI_Projects"
    project_dir.mkdir(parents=True)
    project_file = project_dir / "SampleAgent.md"
    project_file.write_text(
        "\n".join(
            [
                "# SampleAgent",
                "",
                "## Status",
                "- Current checkpoint: SAMPLE-001",
                "- Current stage: Active",
                "- Pause rule: Pause after showcase",
                "",
                "## Portfolio Value",
                "- Shows local workflow design.",
            ]
        ),
        encoding="utf-8",
    )
    project_files = [
        {
            "file_path": str(project_file),
            "relative_path": "01_AI_Projects/SampleAgent.md",
            "file_name": "SampleAgent.md",
            "category_dir": "01_AI_Projects",
        }
    ]

    cards = extract_project_status_cards(project_files, kb_root)

    assert cards == [
        {
            "project_name": "SampleAgent",
            "checkpoint": "SAMPLE-001",
            "stage": "Active",
            "portfolio_value": "Shows local workflow design.",
            "pause_rule": "Pause after showcase",
            "relative_path": "01_AI_Projects/SampleAgent.md",
        }
    ]
