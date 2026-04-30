import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'services', 'api')))

from db.postgres import SessionLocal
from models.section import LegalSection

def seed_statutes():
    print("📚 Seeding Statutes (BNS/IPC)...")
    db = SessionLocal()
    
    # Load mapping from data directory
    mapping_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'legal', 'section_maps', 'ipc_to_bns.json'))
    
    with open(mapping_path, 'r') as f:
        mapping = json.load(f)
    
    try:
        for ipc_key, data in mapping.items():
            # Seed IPC section
            ipc_section = LegalSection(
                act_name="IPC",
                section_number=ipc_key.split("_")[1],
                title=data['title'],
                content=data['description'],
                notes="Classic Indian Penal Code section"
            )
            db.add(ipc_section)
            db.flush() # Get ID
            
            # Seed BNS section
            bns_section = LegalSection(
                act_name="BNS",
                section_number=data['bns_section'],
                title=data['title'],
                content=data['description'],
                mapped_section_id=ipc_section.id,
                notes="New Bharatiya Nyaya Sanhita section"
            )
            db.add(bns_section)
            
        db.commit()
        print("✅ Statutes seeded successfully.")
    except Exception as e:
        print(f"❌ Error during seeding: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_statutes()
