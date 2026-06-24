from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


REQUIRED_APP_STRINGS = [
    "Demo Mode",
    "Local Private Mode",
    "demo_knowledge_base",
    "knowledge_base",
]


@dataclass
class DemoModeCheckResult:
    """Result for static demo-mode release readiness checks."""

    warnings: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        """Return PASS, WARNING, or FAIL."""
        if self.failures:
            return "FAIL"
        if self.warnings:
            return "WARNING"
        return "PASS"


def read_config(config_path: Path) -> dict:
    """Read the knowledge base config JSON."""
    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def check_demo_mode(project_root: Path | str) -> DemoModeCheckResult:
    """Statically check that Demo Mode is configured as the public default."""
    root = Path(project_root).resolve()
    result = DemoModeCheckResult()

    config_path = root / "config" / "kb_config.json"
    app_path = root / "app.py"

    config = read_config(config_path)
    if config.get("default_knowledge_source_mode") != "demo":
        result.failures.append("default_knowledge_source_mode must be demo")

    if not config.get("demo_knowledge_base_path"):
        result.failures.append("demo_knowledge_base_path is missing")

    if config.get("enable_llm") is not False:
        result.warnings.append("enable_llm should remain false for public showcase prep")

    try:
        app_text = app_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        result.failures.append("app.py is missing")
        return result

    for required in REQUIRED_APP_STRINGS:
        if required not in app_text:
            result.failures.append(f"app.py missing required text: {required}")

    return result


def print_result(result: DemoModeCheckResult) -> None:
    """Print PASS/WARNING/FAIL summary."""
    print(f"Status: {result.status}")
    print(f"Warnings: {len(result.warnings)}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    print(f"Failures: {len(result.failures)}")
    for failure in result.failures:
        print(f"FAIL: {failure}")


def main() -> int:
    """Run the check for the current project."""
    project_root = Path(__file__).resolve().parents[1]
    result = check_demo_mode(project_root)
    print_result(result)
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
