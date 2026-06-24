from __future__ import annotations

import fnmatch
import os
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_KB_ROOT = PROJECT_ROOT / "knowledge_base"

ALLOWED_EXTENSIONS = {".md", ".txt"}

IGNORED_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "outputs",
    "venv",
}

IGNORED_FILE_PATTERNS = {
    ".env",
    "*.env",
    "*.key",
    "*.pem",
    "*.p12",
    "*.pfx",
    "*.sqlite",
    "*.db",
    "*.log",
    "*.csv",
    "*.xlsx",
    "*.pdf",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.gif",
    "*.webp",
    "*.mp4",
    "*.mov",
    "*.avi",
    "*.mkv",
}

SENSITIVE_NAME_TOKENS = {
    "api_key",
    "apikey",
    "credential",
    "credentials",
    "password",
    "secret",
    "token",
}


def get_default_knowledge_base_root() -> Path:
    """Return the default local knowledge base path."""
    return DEFAULT_KB_ROOT


def should_ignore_dir(dirname: str) -> bool:
    """Return True when a directory should not be scanned."""
    return dirname.lower() in IGNORED_DIRS


def should_ignore_file(file_path: Path) -> bool:
    """Return True when a file is unsafe or outside the text-only scope."""
    name = file_path.name.lower()

    if file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
        return True

    if any(fnmatch.fnmatch(name, pattern.lower()) for pattern in IGNORED_FILE_PATTERNS):
        return True

    if any(token in name for token in SENSITIVE_NAME_TOKENS):
        return True

    return False


def _read_text_file(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return file_path.read_text(encoding="utf-8", errors="replace")


def _category_for(root_path: Path, file_path: Path) -> str:
    relative_path = file_path.relative_to(root_path)
    if len(relative_path.parts) <= 1:
        return "."
    return relative_path.parts[0]


def scan_knowledge_base(root_path: str) -> list[dict[str, Any]]:
    """Scan Markdown and text files under a local knowledge base folder."""
    root = Path(root_path).resolve()
    if not root.exists():
        return []

    results: list[dict[str, Any]] = []

    for current_dir, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            dirname for dirname in dirnames if not should_ignore_dir(dirname)
        )
        current_path = Path(current_dir)

        for filename in sorted(filenames):
            file_path = current_path / filename
            if should_ignore_file(file_path):
                continue

            text = _read_text_file(file_path)
            relative_path = file_path.relative_to(root)
            results.append(
                {
                    "file_path": str(file_path),
                    "relative_path": relative_path.as_posix(),
                    "file_name": file_path.name,
                    "category_dir": _category_for(root, file_path),
                    "char_count": len(text),
                    "line_count": len(text.splitlines()),
                }
            )

    return sorted(results, key=lambda item: item["relative_path"].lower())


def main() -> int:
    root = get_default_knowledge_base_root()
    results = scan_knowledge_base(str(root))

    print(f"Knowledge base root: {root}")
    print(f"Scanned text files: {len(results)}")

    for item in results:
        print(
            "- "
            f"[{item['category_dir']}] {item['relative_path']} "
            f"| {item['char_count']} chars | {item['line_count']} lines"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

