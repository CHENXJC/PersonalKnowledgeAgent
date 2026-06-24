from agent.kb_search import search_knowledge_base


def test_search_knowledge_base_returns_matching_line(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    category = kb_root / "01_AI_Projects"
    category.mkdir(parents=True)
    (category / "MarketSenseAgent.md").write_text(
        "# MarketSenseAgent\n\nMarket signal dashboard note.",
        encoding="utf-8",
    )

    results = search_knowledge_base(str(kb_root), "signal")

    assert len(results) == 1
    assert results[0]["file_name"] == "MarketSenseAgent.md"
    assert results[0]["line_number"] == 3
    assert "signal" in results[0]["snippet"].lower()


def test_search_knowledge_base_is_case_insensitive(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    category = kb_root / "04_Business_Ideas"
    category.mkdir(parents=True)
    (category / "SME_AI_Automation_Service.md").write_text(
        "# SME AI Automation Service\n\nWorkflow automation for SMEs.",
        encoding="utf-8",
    )

    results = search_knowledge_base(str(kb_root), "workflow")

    assert len(results) == 1
    assert results[0]["category_dir"] == "04_Business_Ideas"

