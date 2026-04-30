from typing import Any, Dict, List

from qdrant_client import QdrantClient
from config import settings

class VectorDBClient:
    def __init__(self):
        self.client = QdrantClient(url=settings.QDRANT_URL)
        self.collection_name = "judgments"

    async def search(self, vector, limit=10, filter=None) -> List[Dict[str, Any]]:
        try:
            points = self.client.search(
                collection_name=self.collection_name,
                query_vector=vector,
                limit=limit,
                query_filter=filter
            )
        except Exception:
            return []

        normalized_results = []
        for point in points:
            payload = point.payload or {}
            normalized_results.append(
                {
                    "id": str(point.id),
                    "title": payload.get("title") or payload.get("case_title") or "Untitled Judgment",
                    "summary": payload.get("summary") or payload.get("snippet") or "",
                    "content": payload.get("content") or "",
                    "citation": payload.get("citation"),
                    "source": "vector",
                    "score": point.score or 0.0,
                }
            )
        return normalized_results

vector_db = VectorDBClient()
