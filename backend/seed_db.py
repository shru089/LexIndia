from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

mock_cases = [
    models.Case(title='Kesavananda Bharati Sripadagalvaru and Ors. v. State of Kerala and Anr.', year=1973, court='Supreme Court of India', citation='(1973) 4 SCC 225'),
    models.Case(title='M.C. Mehta vs. Union of India', year=1986, court='Supreme Court of India', citation='1987 AIR 1086'),
    models.Case(title='State of Maharashtra vs. Digital Entities', year=2024, court='Supreme Court of India', citation='Case ID: 442/2023'),
    models.Case(title='In Re: Intellectual Property in AI-Generated Content', year=2024, court='Delhi High Court', citation='Case ID: 891/2024')
]

for c in mock_cases:
    existing = db.query(models.Case).filter_by(title=c.title).first()
    if not existing:
        db.add(c)

db.commit()
db.close()
print("Database seeded successfully!")
