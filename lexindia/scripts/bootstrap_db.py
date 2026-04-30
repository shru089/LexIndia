import sys
import os

# Add services/api to path so we can import models and db
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'services', 'api')))

from db.postgres import engine, Base
from models.user import User
from models.judgment import Judgment
from models.section import LegalSection
from models.query import AuditLog

def bootstrap():
    print("🚀 Initializing Nyaya.AI Database...")
    try:
        # Create all tables defined in models
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully.")
    except Exception as e:
        print(f"❌ Error during bootstrap: {str(e)}")

if __name__ == "__main__":
    bootstrap()
