"""
Disclaimer Injector: Ensures every response ends with the mandatory legal safety block.
"""

MANDATORY_DISCLAIMER = "This is legal information, not legal advice. Please consult a licensed advocate before taking action."

async def inject_disclaimer(response_text: str) -> str:
    if MANDATORY_DISCLAIMER not in response_text:
        return f"{response_text}\n\n---\n⚠️ **Disclaimer**\n{MANDATORY_DISCLAIMER}"
    return response_text
