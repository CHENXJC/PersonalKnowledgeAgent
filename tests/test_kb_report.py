from pathlib import Path

from agent.kb_report import generate_inventory_report


def test_generate_inventory_report_creates_report_file(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    kb_root = project_root / "knowledge_base"
    ai_projects = kb_root / "01_AI_Projects"
    business_ideas = kb_root / "04_Business_Ideas"
    ai_projects.mkdir(parents=True)
    business_ideas.mkdir(parents=True)

    (kb_root / "00_Index.md").write_text("# Index", encoding="utf-8")
    (ai_projects / "SampleAgent.md").write_text("# SampleAgent", encoding="utf-8")
    (business_ideas / "SampleIdea.md").write_text("# SampleIdea", encoding="utf-8")

    report_path = generate_inventory_report(str(project_root))
    report_file = Path(report_path)

    assert report_file.exists()
    report_text = report_file.read_text(encoding="utf-8")
    assert "Total files: 3" in report_text
    assert "01_AI_Projects" in report_text
    assert "04_Business_Ideas" in report_text


def test_generate_inventory_report_supports_demo_root_and_output_path(tmp_path):
    project_root = tmp_path / "PersonalKnowledgeAgent"
    demo_root = project_root / "demo_knowledge_base"
    ai_projects = demo_root / "01_AI_Projects"
    ai_projects.mkdir(parents=True)

    (demo_root / "00_Index.md").write_text("# Demo Index", encoding="utf-8")
    (ai_projects / "DemoAgent.md").write_text("# DemoAgent", encoding="utf-8")

    output_path = project_root / "outputs" / "demo_kb_inventory_report.md"
    report_path = generate_inventory_report(str(demo_root), str(output_path))
    report_file = Path(report_path)

    assert report_file == output_path
    assert report_file.exists()
    report_text = report_file.read_text(encoding="utf-8")
    assert "Source root: `demo_knowledge_base`" in report_text
    assert "Total files: 2" in report_text
    assert "01_AI_Projects/DemoAgent.md" in report_text
    assert str(tmp_path) not in report_text
