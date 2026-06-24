import json
from pathlib import Path

from tools.check_demo_mode import check_demo_mode


APP_SAMPLE = """
Demo Mode
Local Private Mode
demo_knowledge_base
knowledge_base
"""


def write_sample_project(
    tmp_path: Path,
    default_mode: str = "demo",
    include_demo_path: bool = True,
) -> Path:
    project_root = tmp_path / "PersonalKnowledgeAgent"
    config_dir = project_root / "config"
    config_dir.mkdir(parents=True)
    config = {
        "default_knowledge_source_mode": default_mode,
        "enable_llm": False,
    }
    if include_demo_path:
        config["demo_knowledge_base_path"] = "demo_knowledge_base"
    (config_dir / "kb_config.json").write_text(
        json.dumps(config),
        encoding="utf-8",
    )
    (project_root / "app.py").write_text(APP_SAMPLE, encoding="utf-8")
    return project_root


def test_check_demo_mode_passes_when_default_is_demo(tmp_path):
    project_root = write_sample_project(tmp_path)

    result = check_demo_mode(project_root)

    assert result.status == "PASS"
    assert result.failures == []


def test_check_demo_mode_fails_when_default_is_not_demo(tmp_path):
    project_root = write_sample_project(tmp_path, default_mode="private")

    result = check_demo_mode(project_root)

    assert result.status == "FAIL"
    assert any("default_knowledge_source_mode" in item for item in result.failures)


def test_check_demo_mode_fails_when_demo_path_missing(tmp_path):
    project_root = write_sample_project(tmp_path, include_demo_path=False)

    result = check_demo_mode(project_root)

    assert result.status == "FAIL"
    assert any("demo_knowledge_base_path" in item for item in result.failures)
