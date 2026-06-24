# Project Workflow

## PKB-001: Local Knowledge Base Skeleton

Create the local-first project skeleton, Markdown categories, templates, scanner, keyword search, safety docs, and tests.

## PKB-002: Import Real Project Notes

Import sanitized notes for existing AI projects. Do not import secrets, `.env`, generated reports, credentials, or private output files.

## PKB-003: Streamlit Local Dashboard

Build a local dashboard to browse categories, view scanned file counts, and inspect project notes.

## PKB-004: Basic Search UI

Add a Streamlit search panel for keyword search across Markdown and text files.

## PKB-005: Optional OpenAI/File Search/RAG

Evaluate optional RAG support after the local knowledge base is stable. Keep this optional and behind explicit configuration.

## PKB-006: GitHub Public Showcase Version

Prepare a public-safe showcase version with demo/sample content only. Run safety checks before any public release.

## PKB-007: Connect To AgentHubControlCenter

Expose sanitized project summaries to AgentHubControlCenter as the underlying knowledge base layer.

