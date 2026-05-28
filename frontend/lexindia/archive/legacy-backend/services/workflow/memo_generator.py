from services.workflow.draft_engine import drafting_engine
from datetime import datetime

class MemoGenerator:
    """
    Stage 3: Converts AI Research results into professional Legal Memos.
    """
    
    async def create_research_memo(self, research_data: dict) -> str:
        """
        Takes raw AI research and formats it into a memorandum.
        """
        memo_data = {
            "date": datetime.now().strftime("%d %B, %Y"),
            "subject": f"Research Memorandum regarding {research_data.get('situation_summary', 'Legal Inquiry')[:50]}...",
            "situation_summary": research_data.get("situation_summary"),
            "laws": research_data.get("applicable_laws", []),
            "cases": research_data.get("similar_case_insights", {}).get("trends", ""),
            "next_steps": research_data.get("next_steps", []),
            "disclaimer": research_data.get("disclaimer")
        }
        
        # Use the drafting engine to render the memo
        return await drafting_engine.generate_document("research_memo", memo_data)

memo_generator = MemoGenerator()
