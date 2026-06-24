from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from agent.kb_scanner import get_default_knowledge_base_root, scan_knowledge_base


def _read_text_file(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return file_path.read_text(encoding="utf-8", errors="replace")


def _make_snippet(line: str, query: str, max_chars: int = 220) -> str:
    clean_line = " ".join(line.strip().split())
    if len(clean_line) <= max_chars:
        return clean_line

    index = clean_line.lower().find(query.lower())
    if index < 0:
        return clean_line[: max_chars - 3] + "..."

    start = max(index - 70, 0)
    end = min(start + max_chars - 3, len(clean_line))
    snippet = clean_line[start:end]
    if start > 0:
        snippet = "..." + snippet
    if end < len(clean_line):
        snippet = snippet + "..."
    return snippet


def search_knowledge_base(root_path: str, query: str) -> list[dict[str, Any]]:
    """Search Markdown and text files in the local knowledge base."""
    normalized_query = query.strip()
    if not normalized_query:
        return []

    query_lower = normalized_query.lower()
    results: list[dict[str, Any]] = []

    for item in scan_knowledge_base(root_path):
        file_path = Path(item["file_path"])
        text = _read_text_file(file_path)

        for line_number, line in enumerate(text.splitlines(), start=1):
            if query_lower in line.lower():
                results.append(
                    {
                        "file_path": item["file_path"],
                        "relative_path": item["relative_path"],
                        "file_name": item["file_name"],
                        "category_dir": item["category_dir"],
                        "line_number": line_number,
                        "snippet": _make_snippet(line, normalized_query),
                    }
                )

    return results


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print('Usage: python -m agent.kb_search "keyword"')
        return 1

    query = " ".join(args)
    root = get_default_knowledge_base_root()
    results = search_knowledge_base(str(root), query)

    print(f"Knowledge base root: {root}")
    print(f"Query: {query}")
    print(f"Matches: {len(results)}")

    for item in results:
        print(
            "- "
            f"{item['relative_path']}:{item['line_number']} "
            f"| {item['snippet']}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

