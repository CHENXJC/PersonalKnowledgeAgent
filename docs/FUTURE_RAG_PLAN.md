# Future RAG Plan

PKB-001 does not implement RAG. This document records the future direction so the project can stay lightweight now and grow later.

## Possible Future Pipeline

1. Document loading
2. Chunking
3. Embeddings
4. Vector store
5. Retrieval
6. Answer with citations/source files
7. Optional OpenAI integration
8. Optional local model integration

## Design Rules

- RAG must be optional.
- RAG must not read secrets or private identity documents.
- RAG must only use explicitly approved knowledge base folders.
- Answers should include source file references.
- Public showcase mode must use demo/sample documents only.

## Not For PKB-001

The first stage does not include:

- OpenAI API calls.
- Embedding generation.
- Vector database setup.
- File upload.
- Cloud sync.
- Autonomous agent actions.

