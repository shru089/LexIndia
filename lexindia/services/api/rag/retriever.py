# This file is intentionally a shim.
# The canonical retriever implementation lives at:
#   services/api/services/rag/retriever.py
#
# Import and re-export it here so both import paths resolve correctly.
from services.rag.retriever import HybridRetriever, retriever  # noqa: F401
