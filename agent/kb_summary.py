"""Future module for LLM/RAG summarization."""

from __future__ import annotations


def summarize_text_basic(text: str, max_chars: int = 800) -> str:
    """Return the first max_chars characters as a simple local placeholder."""
    if max_chars < 0:
        max_chars = 0
    return text[:max_chars]

