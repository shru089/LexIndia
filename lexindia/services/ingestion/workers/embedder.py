from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid

class Embedder:
    """
    Chunks judgment text, generates embeddings, and stores them in Qdrant.
    """
    
    def __init__(self, qdrant_url: str):
        self.client = QdrantClient(url=qdrant_url)
        self.collection_name = "judgments"

    async def chunk_and_store(self, judgment_id: str, text: str, metadata: dict):
        # 1. Simple chunking logic (e.g., 1000 characters with 200 overlap)
        chunks = [text[i:i+1000] for i in range(0, len(text), 800)]
        
        points = []
        for i, chunk in enumerate(chunks):
            # 2. In production: vector = embedding_model.embed(chunk)
            vector = [0.1] * 1536 # Placeholder
            
            points.append(PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "judgment_id": judgment_id,
                    "chunk_index": i,
                    "text": chunk,
                    **metadata
                }
            ))
            
        # 3. Upsert to Qdrant
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

# Initialize with default URL from config
embedder = Embedder(qdrant_url="http://localhost:6333")
