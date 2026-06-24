from pathlib import Path

from tools.public_release_check import check_public_release


def test_public_release_check_passes_safe_sample(tmp_path: Path):
    (tmp_path / "README.md").write_text(
        "# Demo\n\nThis is a sanitized public sample note.",
        encoding="utf-8",
    )

    result = check_public_release(tmp_path)

    assert result.status == "PASS"
    assert result.scanned_file_count == 1
    assert result.failures == []


def test_public_release_check_fails_env_file(tmp_path: Path):
    (tmp_path / ".env").write_text("DO_NOT_USE=demo", encoding="utf-8")

    result = check_public_release(tmp_path)

    assert result.status == "FAIL"
    assert any(".env" in failure for failure in result.failures)


def test_public_release_check_fails_secret_assignment(tmp_path: Path):
    (tmp_path / "unsafe.md").write_text(
        "OPENAI_API_KEY" + "=sk-test",
        encoding="utf-8",
    )

    result = check_public_release(tmp_path)

    assert result.status == "FAIL"
    assert any("assignment" in failure.lower() for failure in result.failures)


def test_public_release_check_warns_on_windows_absolute_path(tmp_path: Path):
    (tmp_path / "note.md").write_text(
        r"Example leaked path: C:\Users\Demo\PrivateNote.md",
        encoding="utf-8",
    )

    result = check_public_release(tmp_path)

    assert result.status == "WARNING"
    assert any("windows" in warning.lower() for warning in result.warnings)
