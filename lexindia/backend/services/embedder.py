from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid
from config import settings

class Embedder:
    """
    Handles chunking and Vector DB storage.
    """
    def __init__(self):
        self.client = QdrantClient(url=settings.QDRANT_URL)
        self.collection = "judgments"

    async def store_judgment(self, judgment_id: str, text: str, metadata: dict):
        # 1000 char chunks with overlap
        chunks = [text[i:i+1000] for i in range(0, len(text), 800)]
        points = []
        
        for i, chunk in enumerate(chunks):
            # Placeholder for embedding model call
            vector = [0.1] * 1536 
            points.append(PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"judgment_id": judgment_id, "text": chunk, **metadata}
            ))
            
        self.client.upsert(collection_name=self.collection, points=points)

embedder = Embedder()
