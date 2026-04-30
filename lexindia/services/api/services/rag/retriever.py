from typing import Dict, List
from db.vector import vector_db
from db.search import search_client

class HybridRetriever:
    """
    Core Foundation: Combines BM25 Keyword Search (Elasticsearch) 
    and Vector Search (Qdrant) for high-precision legal research.
    """
    
    async def retrieve(self, query: str, limit: int = 10) -> List[Dict]:
        # 1. Keyword Search (Precision for Section IDs and Act names)
        keyword_results = await search_client.keyword_search(query, limit=limit)
        
        # 2. Vector Search (Semantic for natural language problems like "landlord locked shop")
        # In production: query_vector = embedding_model.embed(query)
        placeholder_vector = [0.1] * 1536 # Placeholder
        vector_results = await vector_db.search(placeholder_vector, limit=limit)
        
        # 3. Reciprocal Rank Fusion (RRF) 
        # Merges both streams to surface the best 'Truth'
        merged_results = self._rank_fusion(keyword_results, vector_results)
        
        return merged_results[:limit]

    def _rank_fusion(self, keyword_list, vector_list):
        combined_scores = {}

        for rank, item in enumerate(keyword_list, start=1):
            key = item.get("id") or item.get("title")
            combined_scores[key] = {
                **item,
                "score": item.get("score", 0.0),
                "rrf_score": 1 / (60 + rank),
            }

        for rank, item in enumerate(vector_list, start=1):
            key = item.get("id") or item.get("title")
            if key in combined_scores:
                combined_scores[key]["rrf_score"] += 1 / (60 + rank)
                if not combined_scores[key].get("summary") and item.get("summary"):
                    combined_scores[key]["summary"] = item["summary"]
                if not combined_scores[key].get("content") and item.get("content"):
                    combined_scores[key]["content"] = item["content"]
            else:
                combined_scores[key] = {
                    **item,
                    "score": item.get("score", 0.0),
                    "rrf_score": 1 / (60 + rank),
                }

        ranked_results = sorted(
            combined_scores.values(),
            key=lambda item: item.get("rrf_score", 0.0),
            reverse=True,
        )
        return ranked_results

retriever = HybridRetriever()
