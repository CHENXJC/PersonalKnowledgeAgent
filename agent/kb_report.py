from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from agent.kb_scanner import get_default_knowledge_base_root, scan_knowledge_base

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT_PATH = PROJECT_ROOT / "outputs" / "kb_inventory_report.md"


def _resolve_paths(root_path: str, output_path: str | None = None) -> tuple[Path, Path, Path]:
    root = Path(root_path).resolve()

    if (root / "knowledge_base").is_dir():
        project_root = root
        kb_root = root / "knowledge_base"
    else:
        kb_root = root
        project_root = root.parent

    if output_path is None:
        report_path = project_root / "outputs" / "kb_inventory_report.md"
    else:
        configured_output = Path(output_path)
        if configured_output.is_absolute():
            report_path = configured_output
        else:
            report_path = project_root / configured_output
    return project_root, kb_root, report_path


def _format_file_list(items: list[dict[str, Any]], category: str) -> list[str]:
    filtered = [item for item in items if item["category_dir"] == category]
    if not filtered:
        return ["- None"]
    return [f"- {item['relative_path']}" for item in filtered]


def generate_inventory_report(root_path: str, output_path: str | None = None) -> str:
    """Generate a Markdown inventory report for the local knowledge base."""
    project_root, kb_root, report_path = _resolve_paths(root_path, output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    index_path = kb_root / "00_Index.md"
    index_status = "Found" if index_path.exists() else "Missing"
    scanned_files = scan_knowledge_base(str(kb_root))
    category_counts = Counter(item["category_dir"] for item in scanned_files)
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")

    lines = [
        "# Knowledge Base Inventory Report",
        "",
        f"- Generated at: {generated_at}",
        f"- Project root: `{project_root.name}`",
        f"- Source root: `{kb_root.name}`",
        f"- Index file: {index_status}",
        f"- Total files: {len(scanned_files)}",
        "",
        "## Category Stats",
        "",
    ]

    if category_counts:
        for category, count in sorted(category_counts.items()):
            lines.append(f"- {category}: {count}")
    else:
        lines.append("- None: 0")

    lines.extend(
        [
            "",
            "## AI Project Files",
            "",
            *_format_file_list(scanned_files, "01_AI_Projects"),
            "",
            "## Business Idea Files",
            "",
            *_format_file_list(scanned_files, "04_Business_Ideas"),
            "",
            "## Safety Note",
            "",
            "This report is generated from Markdown and text files only. It should not include `.env`, keys, tokens, passwords, private credentials, or private binary files.",
            "",
        ]
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return str(report_path)


def main() -> int:
    report_path = generate_inventory_report(str(get_default_knowledge_base_root()))
    print(f"Inventory report generated: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
