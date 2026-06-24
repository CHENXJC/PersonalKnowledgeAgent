from __future__ import annotations

import fnmatch
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".py",
    ".json",
    ".toml",
    ".yml",
    ".yaml",
}

SPECIAL_TEXT_FILENAMES = {".gitignore"}

SKIPPED_DIRS = {
    ".git",
    ".pytest_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv",
}

HIGH_RISK_FILENAME_PATTERNS = {
    ".env",
    "*.key",
    "*.pem",
    "*.p12",
    "*.pfx",
    "*secret*",
    "*token*",
    "*password*",
    "*credential*",
    "*passport*",
    "*visa*",
    "*bank*",
    "*id_card*",
}

BLOCKING_FILENAME_PATTERNS = {
    ".env",
    "*.key",
    "*.pem",
    "*.p12",
    "*.pfx",
}

CONTENT_KEYWORDS = {
    "API_KEY",
    "SECRET",
    "TOKEN",
    "PASSWORD",
    "PRIVATE KEY",
    "BEGIN RSA PRIVATE KEY",
    "OPENAI_API_KEY",
    "TELEGRAM_BOT_TOKEN",
    "passport",
    "bank card",
    "visa grant",
    "driver licence",
    "TFN",
    "Medicare",
}

ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(?:OPENAI_API_KEY|TELEGRAM_BOT_TOKEN|API_KEY|SECRET|TOKEN|PASSWORD)\b"
    r"\s*[:=]\s*['\"]?[^'\"\s]+"
)

WINDOWS_PATH_PATTERN = re.compile(r"(?i)(?:\b[A-Z]:\\|Users\\)")


@dataclass
class ReleaseCheckResult:
    """Public release safety check result."""

    scanned_file_count: int = 0
    warnings: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        """Return FAIL, WARNING, or PASS."""
        if self.failures:
            return "FAIL"
        if self.warnings:
            return "WARNING"
        return "PASS"


def should_skip_dir(dirname: str) -> bool:
    """Return True when a directory should be excluded from release scanning."""
    return dirname.lower() in SKIPPED_DIRS


def is_text_file(path: Path) -> bool:
    """Return True when the file should be scanned as text."""
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in SPECIAL_TEXT_FILENAMES


def matches_any(name: str, patterns: set[str]) -> bool:
    """Return True when a file name matches any shell-style pattern."""
    lowered = name.lower()
    return any(fnmatch.fnmatch(lowered, pattern.lower()) for pattern in patterns)


def iter_project_files(project_root: Path) -> list[Path]:
    """Return project files while skipping local caches and dependency folders."""
    files: list[Path] = []
    for current_dir, dirnames, filenames in os.walk(project_root):
        dirnames[:] = sorted(
            dirname for dirname in dirnames if not should_skip_dir(dirname)
        )
        current_path = Path(current_dir)
        for filename in sorted(filenames):
            files.append(current_path / filename)
    return files


def read_text_safely(path: Path) -> str:
    """Read a text file without failing on imperfect encoding."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def check_public_release(project_root: Path | str) -> ReleaseCheckResult:
    """Check a project directory for public release blocking risks."""
    root = Path(project_root).resolve()
    result = ReleaseCheckResult()

    for file_path in iter_project_files(root):
        relative_path = file_path.relative_to(root).as_posix()

        if matches_any(file_path.name, BLOCKING_FILENAME_PATTERNS):
            result.failures.append(
                f"Blocking high-risk file name found: {relative_path}"
            )
        elif matches_any(file_path.name, HIGH_RISK_FILENAME_PATTERNS):
            result.failures.append(
                f"High-risk private filename requires removal or review: {relative_path}"
            )

        if not is_text_file(file_path):
            continue

        result.scanned_file_count += 1
        text = read_text_safely(file_path)

        if ASSIGNMENT_PATTERN.search(text):
            result.failures.append(
                f"Secret-like assignment pattern found in: {relative_path}"
            )
            continue

        upper_text = text.upper()
        for keyword in sorted(CONTENT_KEYWORDS):
            if keyword.upper() in upper_text:
                result.warnings.append(
                    f"Sensitive keyword `{keyword}` found in: {relative_path}"
                )
                break

        if WINDOWS_PATH_PATTERN.search(text):
            result.warnings.append(
                f"Windows absolute path or user path pattern found in: {relative_path}"
            )

    return result


def print_result(result: ReleaseCheckResult) -> None:
    """Print a PASS/WARNING/FAIL summary."""
    print(f"Status: {result.status}")
    print(f"Scanned text files: {result.scanned_file_count}")
    print(f"Warnings: {len(result.warnings)}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    print(f"Failures: {len(result.failures)}")
    for failure in result.failures:
        print(f"FAIL: {failure}")


def main() -> int:
    """Run the public release safety check for the current project."""
    project_root = Path(__file__).resolve().parents[1]
    result = check_public_release(project_root)
    print_result(result)
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
