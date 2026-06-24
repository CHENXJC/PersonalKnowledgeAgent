from agent.kb_scanner import scan_knowledge_base


def test_scan_knowledge_base_finds_markdown_file(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    category = kb_root / "01_AI_Projects"
    category.mkdir(parents=True)
    sample_file = category / "SampleProject.md"
    sample_file.write_text("# SampleProject\n\nTest note.", encoding="utf-8")

    results = scan_knowledge_base(str(kb_root))

    assert len(results) == 1
    assert results[0]["file_name"] == "SampleProject.md"
    assert results[0]["category_dir"] == "01_AI_Projects"
    assert results[0]["char_count"] > 0
    assert results[0]["line_count"] == 3


def test_scan_knowledge_base_ignores_env_file(tmp_path):
    kb_root = tmp_path / "knowledge_base"
    kb_root.mkdir()
    (kb_root / ".env").write_text("SECRET" + "=do-not-read", encoding="utf-8")
    (kb_root / "Visible.md").write_text("# Visible", encoding="utf-8")

    results = scan_knowledge_base(str(kb_root))

    assert [item["file_name"] for item in results] == ["Visible.md"]
