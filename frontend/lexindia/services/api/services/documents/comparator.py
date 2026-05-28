import difflib
import re
from typing import List, Dict

class DocumentComparator:
    """
    Analyzes multiple documents to find inconsistencies, 
    variances in liability caps, and clause conflicts.
    """
    
    async def find_contradictions(self, doc_a_text: str, doc_b_text: str) -> List[Dict]:
        contradictions = []

        lower_a = doc_a_text.lower()
        lower_b = doc_b_text.lower()

        if "liability cap" in lower_a and "liability cap" in lower_b and doc_a_text != doc_b_text:
            contradictions.append({
                "conflict_type": "Clause Inconsistency",
                "severity": "HIGH",
                "description": "Variance detected in liability exposure between documents.",
                "action_recommended": "Align with global risk policy."
            })

        amounts_a = set(re.findall(r"(?:rs\.?|inr)?\s?\d[\d,]*(?:\.\d+)?", lower_a))
        amounts_b = set(re.findall(r"(?:rs\.?|inr)?\s?\d[\d,]*(?:\.\d+)?", lower_b))
        if amounts_a != amounts_b and (amounts_a or amounts_b):
            contradictions.append(
                {
                    "conflict_type": "Monetary Delta",
                    "severity": "MEDIUM",
                    "description": f"Document A amounts: {sorted(amounts_a) or ['none']} | Document B amounts: {sorted(amounts_b) or ['none']}",
                    "action_recommended": "Check commercial schedules, caps, and indemnity references before circulation.",
                }
            )

        similarity = difflib.SequenceMatcher(None, doc_a_text, doc_b_text).ratio()
        if similarity < 0.55:
            contradictions.append(
                {
                    "conflict_type": "Material Divergence",
                    "severity": "MEDIUM",
                    "description": "The documents diverge significantly in structure or wording, suggesting more than a redline-level change.",
                    "action_recommended": "Generate a side-by-side issue matrix for legal and business review.",
                }
            )

        return contradictions

comparator = DocumentComparator()
