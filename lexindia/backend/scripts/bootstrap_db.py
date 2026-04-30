import sys
import os

# Add backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.postgres import engine, Base
# Ensure all models are imported so Base knows about them
from models.user import User
from models.judgment import Judgment
from models.section import LegalSection
from models.query import AuditLog

def bootstrap():
    print("🚀 Initializing LexIndia Database Schema...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ PostgreSQL tables created successfully.")
    except Exception as e:
        print(f"❌ Error during bootstrap: {str(e)}")

if __name__ == "__main__":
    bootstrap()
