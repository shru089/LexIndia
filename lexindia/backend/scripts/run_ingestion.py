import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.ingestion.sc_crawler import sci_crawler
from services.ocr_worker import ocr_worker
from services.embedder import embedder

async def main():
    print("🚀 Starting LexIndia Ingestion Pipeline...")
    
    # 1. Crawl for new judgments
    judgments = await sci_crawler.get_latest_judgments()
    
    for judgment in judgments:
        print(f"📄 Processing: {judgment['title']}")
        
        # 2. Extract Text (Simulated for now)
        raw_text = "This is the content of the Supreme Court judgment regarding..."
        
        # 3. Embed and Store
        await embedder.store_judgment(
            judgment_id=judgment['case_id'],
            text=raw_text,
            metadata=judgment
        )
        print(f"✅ Successfully ingested {judgment['case_id']}")

if __name__ == "__main__":
    asyncio.run(main())
