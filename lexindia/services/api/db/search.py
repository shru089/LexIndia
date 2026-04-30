from typing import Any, Dict, List

from elasticsearch import AsyncElasticsearch
from config import settings

class SearchClient:
    def __init__(self):
        self.client = AsyncElasticsearch(hosts=[settings.ELASTICSEARCH_URL])
        self.index_name = "judgments"

    async def keyword_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "content", "summary"]
                }
            },
            "size": limit
        }
        try:
            response = await self.client.search(index=self.index_name, body=body)
        except Exception:
            return []

        hits = response.get("hits", {}).get("hits", [])
        normalized_results = []
        for hit in hits:
            source = hit.get("_source", {})
            normalized_results.append(
                {
                    "id": hit.get("_id"),
                    "title": source.get("title") or source.get("case_title") or "Untitled Judgment",
                    "summary": source.get("summary") or source.get("snippet") or "",
                    "content": source.get("content") or "",
                    "citation": source.get("citation"),
                    "source": "keyword",
                    "score": hit.get("_score", 0.0),
                }
            )
        return normalized_results

search_client = SearchClient()
