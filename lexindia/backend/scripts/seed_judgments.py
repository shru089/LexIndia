import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.postgres import SessionLocal
from models.judgment import Judgment
from services.embedder import embedder

SAMPLE_JUDGMENTS = [
    {
        "title": "Arnav Goswami v. State of Maharashtra (2020)",
        "case_id": "W.P. (Crl) No. 1306/2020",
        "text": "Liberty of the individual is the hallmark of a democratic constitution. In this case, the Supreme Court emphasized the need for courts to protect personal liberty against arbitrary arrest...",
        "court": "Supreme Court of India",
        "date": "2020-11-27"
    },
    {
        "title": "Kesavananda Bharati v. State of Kerala (1973)",
        "case_id": "W.P. (C) No. 135/1970",
        "text": "The basic structure of the Constitution cannot be amended by the Parliament. This landmark judgment established the Basic Structure Doctrine in Indian Constitutional Law...",
        "court": "Supreme Court of India",
        "date": "1973-04-24"
    }
]

async def seed_judgments():
    print("🚀 Seeding Sample Judgments into LexIndia Search Engine...")
    db = SessionLocal()
    
    try:
        for data in SAMPLE_JUDGMENTS:
            # 1. Store in Postgres
            judgment = Judgment(
                title=data['title'],
                case_id=data['case_id'],
                full_text=data['text'],
                court=data['court'],
                date_published=data['date']
            )
            db.add(judgment)
            db.flush()
            
            # 2. Store in Qdrant (Vector DB)
            await embedder.store_judgment(
                judgment_id=str(judgment.id),
                text=data['text'],
                metadata={
                    "title": data['title'],
                    "court": data['court'],
                    "date": data['date']
                }
            )
            
        db.commit()
        print("✅ Judgments seeded successfully.")
    except Exception as e:
        print(f"❌ Error during seeding: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(seed_judgments())
