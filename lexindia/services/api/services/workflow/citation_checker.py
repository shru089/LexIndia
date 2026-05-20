"""
Citation Checker: Validates legal citations against the database.
"""

KNOWN_CITATIONS = {
    "lalita kumari": "FIR registration guidance",
    "puttaswamy": "Constitution Bench privacy doctrine",
    "maneka gandhi": "Administrative fairness doctrine",
    "dpdp": "Digital Personal Data Protection Act, 2023",
    "bns 101": "Bharatiya Nyaya Sanhita Section 101",
}


async def validate_citation(citation: str):
    normalized = citation.strip().lower()
    for key, label in KNOWN_CITATIONS.items():
        if key in normalized:
            return {
                "valid": True,
                "citation": citation,
                "matched_authority": label,
                "notes": "Matched against the LexIndia demo authority register.",
            }

    return {
        "valid": False,
        "citation": citation,
        "matched_authority": None,
        "notes": "No exact demo authority match found. Review citation formatting and source register.",
    }
