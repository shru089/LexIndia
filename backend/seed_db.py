from database import SessionLocal, engine
import models
import auth_utils

# Recreate tables with the new schema columns
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    mock_cases = [
        models.Case(
            title="Kesavananda Bharati Sripadagalvaru and Ors. v. State of Kerala and Anr.",
            year=1973,
            court="Supreme Court of India",
            citation="(1973) 4 SCC 225",
            case_number="Writ Petition (Civil) 135 of 1970",
            bench="S.M. Sikri (CJI), J.M. Shelat, K.S. Hegde, A.N. Grover, B. Jaganmohan Reddy, D.G. Palekar, H.R. Khanna, A.K. Mukherjea, Y.V. Chandrachud, J.R. Mudholkar",
            date="1973-04-24",
            acts_cited="Constitution of India",
            sections_cited="Article 368, Article 13, Article 19, Article 31",
            outcome="Allowed with limitations (Basic Structure Doctrine established)",
            key_parties="Kesavananda Bharati (Petitioner) v. State of Kerala (Respondent)",
            summary_facts="The petitioner challenged the validity of the Kerala Land Reforms Act, 1963, and questioned the constitutional validity of the 24th, 25th, and 29th Amendments, which permitted Parliament to curtail fundamental rights.",
            summary_held="The Supreme Court held by a 7-6 majority that while Parliament has wide powers to amend the Constitution under Article 368, it cannot alter or damage its 'Basic Structure'.",
            summary_ratio="The power to amend under Article 368 does not include the power to destroy or abrogate the basic structure or essential framework of the Constitution.",
            amended_recently=False,
            full_text="Detailed transcript of the landmark basic structure judgment concerning Article 368."
        ),
        models.Case(
            title="M.C. Mehta vs. Union of India",
            year=1986,
            court="Supreme Court of India",
            citation="1987 AIR 1086",
            case_number="Writ Petition (Civil) 12739 of 1985",
            bench="P.N. Bhagwati (CJI), D.P. Madon, G.L. Oza",
            date="1986-12-20",
            acts_cited="Constitution of India, Environment (Protection) Act 1986",
            sections_cited="Article 21, Article 32",
            outcome="Allowed (Absolute Liability Principle established)",
            key_parties="M.C. Mehta (Petitioner) v. Union of India & Shriram Food and Fertilizers (Respondents)",
            summary_facts="A public interest litigation was filed following the leakage of toxic oleum gas from a plant owned by Shriram Food and Fertilizers in Delhi, causing deaths and serious injuries to nearby citizens.",
            summary_held="The Supreme Court introduced the doctrine of Absolute Liability, holding that enterprises engaged in hazardous activities have a non-delegable duty to ensure safety and must compensate victims regardless of negligence.",
            summary_ratio="Strict liability exceptions (like Act of God) do not apply to hazardous activities. Compensation must be proportional to the size and capacity of the enterprise to act as a deterrent.",
            amended_recently=False,
            full_text="Detailed text on environmental public interest litigation, Article 21 (Right to Life), and absolute liability."
        ),
        models.Case(
            title="State of Maharashtra vs. Digital Entities",
            year=2024,
            court="Supreme Court of India",
            citation="Case ID: 442/2023",
            case_number="Criminal Appeal 2201 of 2023",
            bench="D.Y. Chandrachud (CJI), Hrishikesh Roy",
            date="2024-02-18",
            acts_cited="Information Technology Act 2000, Indian Penal Code",
            sections_cited="Section 66D, Section 66E, Section 420",
            outcome="Appeal Allowed (Charges Reinstated)",
            key_parties="State of Maharashtra (Appellant) v. Digital Entities Pvt. Ltd. (Respondent)",
            summary_facts="Respondents were accused of conducting coordinated phishing and online transaction fraud. The Bombay High Court quashed the charge sheet arguing lack of physical presence, which the State appealed.",
            summary_held="The Supreme Court reversed the High Court's decision, clarifying that cybercrimes using digital impersonation are cognizable and do not require physical presence in the territory to establish jurisdiction.",
            summary_ratio="Section 66D of the IT Act encompasses virtual identity theft and online fraud, and local jurisdictional boundaries must be interpreted broadly to prevent digital crime evasion.",
            amended_recently=True,
            full_text="Details of digital evidence, jurisdiction under IT Act 2000, and replacement of IPC by Bharatiya Nyaya Sanhita."
        ),
        models.Case(
            title="In Re: Intellectual Property in AI-Generated Content",
            year=2024,
            court="Delhi High Court",
            citation="Case ID: 891/2024",
            case_number="CS(COMM) 105 of 2024",
            bench="Prathiba M. Singh",
            date="2024-04-12",
            acts_cited="Copyright Act 1957, Patents Act 1970",
            sections_cited="Section 2(d), Section 13",
            outcome="Clarified (Human authorship declared mandatory)",
            key_parties="In Re: Intellectual Property in AI-Generated Content (Suo Motu)",
            summary_facts="A suo motu proceeding was initiated by the High Court to resolve a dispute regarding copyright registration of an artwork created by an generative AI algorithm without human creative input.",
            summary_held="The High Court held that copyright protection requires human expression and intellect. An AI cannot be recognized as an author under Section 2(d) of the Copyright Act.",
            summary_ratio="Legal protection of intellectual property in India is contingent upon human origin. Synthetic creations are excluded from proprietary copyright unless significant human contribution is proved.",
            amended_recently=False,
            full_text="Text of judgment regarding artificial intelligence, copyright authorship, and ownership under Indian law."
        )
    ]

    for c in mock_cases:
        existing = db.query(models.Case).filter_by(title=c.title).first()
        if not existing:
            db.add(c)
        else:
            # Update existing records with the new fields
            existing.case_number = c.case_number
            existing.bench = c.bench
            existing.date = c.date
            existing.acts_cited = c.acts_cited
            existing.sections_cited = c.sections_cited
            existing.outcome = c.outcome
            existing.key_parties = c.key_parties
            existing.summary_facts = c.summary_facts
            existing.summary_held = c.summary_held
            existing.summary_ratio = c.summary_ratio
            existing.amended_recently = c.amended_recently
            existing.full_text = c.full_text

    # Seed mock users with hashed passwords
    mock_users = [
        models.User(username="free_user", hashed_password=auth_utils.hash_password("password123"), tier="free"),
        models.User(username="pro_user", hashed_password=auth_utils.hash_password("password123"), tier="citizen_pro"),
        models.User(username="advocate_user", hashed_password=auth_utils.hash_password("password123"), tier="advocate")
    ]

    for u in mock_users:
        existing_user = db.query(models.User).filter_by(username=u.username).first()
        if not existing_user:
            db.add(u)
        else:
            existing_user.hashed_password = u.hashed_password
            existing_user.tier = u.tier

    db.commit()
    print("Database seeded successfully!")
except Exception as e:
    db.rollback()
    print(f"Error seeding database: {e}")
finally:
    db.close()
