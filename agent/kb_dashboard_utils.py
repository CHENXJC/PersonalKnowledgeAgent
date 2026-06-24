from __future__ import annotations

import html
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ALLOWED_DASHBOARD_EXTENSIONS = {".md", ".txt"}


def get_project_root() -> Path:
    """Return the PersonalKnowledgeAgent project root."""
    return Path(__file__).resolve().parents[1]


def get_knowledge_base_path(project_root: Path) -> Path:
    """Return the knowledge base path for a project root."""
    return project_root / "knowledge_base"


def get_active_knowledge_source(project_root: Path, mode: str) -> Path:
    """Return the active knowledge source path for demo or private mode."""
    resolved_root = project_root.resolve()
    normalized_mode = (mode or "demo").strip().lower()
    source_name = "knowledge_base" if normalized_mode == "private" else "demo_knowledge_base"
    source_path = (resolved_root / source_name).resolve()

    if not _is_relative_to(source_path, resolved_root):
        return resolved_root / "demo_knowledge_base"
    return source_path


def get_knowledge_source_label(mode: str) -> str:
    """Return a UI-safe label for the selected knowledge source mode."""
    if (mode or "").strip().lower() == "private":
        return "Local Private Mode: Local personal notes, not for public screenshots"
    return "Demo Mode: Safe public demo content"


def is_demo_mode(mode: str) -> bool:
    """Return True when the selected source mode is demo mode."""
    return (mode or "demo").strip().lower() != "private"


def _is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
    except ValueError:
        return False
    return True


def safe_read_markdown(file_path: Path, allowed_root: Path) -> str:
    """Safely read a Markdown or text file inside an allowed root."""
    resolved_root = allowed_root.resolve()
    resolved_file = file_path.resolve(strict=False)

    if not _is_relative_to(resolved_file, resolved_root):
        return "Security notice: this dashboard can only read allowed local Markdown/TXT files."

    if resolved_file.suffix.lower() not in ALLOWED_DASHBOARD_EXTENSIONS:
        return "Security notice: only .md and .txt files can be opened in this dashboard."

    if not resolved_file.exists():
        return "File not found. The note may have been moved or removed."

    if not resolved_file.is_file():
        return "This path is not a readable Markdown/TXT file."

    try:
        return resolved_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return resolved_file.read_text(encoding="utf-8", errors="replace")


def get_category_counts(scan_results: list[dict[str, Any]]) -> dict[str, int]:
    """Return file counts grouped by knowledge base category."""
    counts = Counter(item.get("category_dir", ".") for item in scan_results)
    return dict(sorted(counts.items()))


def get_files_by_category(
    scan_results: list[dict[str, Any]]
) -> dict[str, list[dict[str, Any]]]:
    """Return scan results grouped by category."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in scan_results:
        grouped[item.get("category_dir", ".")].append(item)

    return {
        category: sorted(items, key=lambda item: item["relative_path"].lower())
        for category, items in sorted(grouped.items())
    }


def _extract_heading(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip() or fallback
    return fallback


def _extract_bullet_value(markdown_text: str, label: str) -> str:
    prefix = f"- {label}:"
    for line in markdown_text.splitlines():
        if line.strip().lower().startswith(prefix.lower()):
            value = line.split(":", 1)[1].strip()
            return value or "Not specified"
    return "Not specified"


def _extract_section_first_bullet(markdown_text: str, section_heading: str) -> str:
    lines = markdown_text.splitlines()
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            in_section = stripped.lower() == f"## {section_heading.lower()}"
            continue
        if in_section and stripped.startswith("- "):
            return stripped.removeprefix("- ").strip() or "Not specified"
    return "Not specified"


def extract_project_status_cards(
    project_files: list[dict[str, Any]], allowed_root: Path
) -> list[dict[str, str]]:
    """Extract compact project status cards from AI project Markdown files."""
    cards: list[dict[str, str]] = []

    for item in sorted(project_files, key=lambda entry: entry["file_name"].lower()):
        file_path = Path(item["file_path"])
        content = safe_read_markdown(file_path, allowed_root)
        fallback_name = file_path.stem

        if content.startswith("Security notice:") or content.startswith("File not found."):
            cards.append(
                {
                    "project_name": fallback_name,
                    "checkpoint": "Not specified",
                    "stage": "Not specified",
                    "portfolio_value": "Not specified",
                    "pause_rule": "Not specified",
                    "relative_path": item.get("relative_path", file_path.name),
                }
            )
            continue

        cards.append(
            {
                "project_name": _extract_heading(content, fallback_name),
                "checkpoint": _extract_bullet_value(content, "Current checkpoint"),
                "stage": _extract_bullet_value(content, "Current stage"),
                "portfolio_value": _extract_section_first_bullet(
                    content, "Portfolio Value"
                ),
                "pause_rule": _extract_bullet_value(content, "Pause rule"),
                "relative_path": item.get("relative_path", file_path.name),
            }
        )

    return cards


def highlight_keyword(text: str, keyword: str) -> str:
    """Return text with case-insensitive keyword matches wrapped in mark tags."""
    if not keyword:
        return text

    escaped_text = html.escape(text)
    escaped_keyword = html.escape(keyword.strip())
    if not escaped_keyword:
        return text

    pattern = re.compile(re.escape(escaped_keyword), re.IGNORECASE)
    return pattern.sub(lambda match: f"<mark>{match.group(0)}</mark>", escaped_text)


def get_inventory_report_status(
    project_root: Path, report_filename: str = "kb_inventory_report.md"
) -> dict[str, Any]:
    """Return safe status metadata for the generated inventory report."""
    safe_filename = Path(report_filename).name
    report_path = project_root / "outputs" / safe_filename
    exists = report_path.exists() and report_path.is_file()
    size_chars = 0
    if exists:
        try:
            size_chars = len(report_path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            size_chars = len(report_path.read_text(encoding="utf-8", errors="replace"))

    return {
        "exists": exists,
        "path": f"outputs/{safe_filename}",
        "size_chars": size_chars,
    }


def build_dashboard_metrics(
    scan_results: list[dict[str, Any]],
    project_root: Path,
    report_filename: str = "kb_inventory_report.md",
) -> dict[str, Any]:
    """Build the dashboard summary metrics used by the Overview page."""
    category_counts = get_category_counts(scan_results)
    report_status = get_inventory_report_status(project_root, report_filename)

    return {
        "total_files": len(scan_results),
        "total_categories": len(
            {item.get("category_dir", ".") for item in scan_results}
        ),
        "ai_project_notes": category_counts.get("01_AI_Projects", 0),
        "business_idea_notes": category_counts.get("04_Business_Ideas", 0),
        "local_first": True,
        "llm_enabled": False,
        "inventory_report_exists": report_status["exists"],
    }


def load_project_status(project_root: Path) -> str:
    """Load the project status document."""
    return safe_read_markdown(project_root / "PROJECT_STATUS.md", project_root)


def load_security_rules(project_root: Path) -> str:
    """Load the security rules document."""
    return safe_read_markdown(project_root / "docs" / "SECURITY_RULES.md", project_root)
