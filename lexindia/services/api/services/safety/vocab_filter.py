"""
Vocabulary Filter: Enforces 'Suggestive Language' and blocks 'Advice Language'.
"""

ADVICE_PHRASES = {
    "you should": "you may consider",
    "you must": "it is common to",
    "i advise": "legal information suggests",
    "this guarantees": "this is a frequent outcome in",
    "you will win": "past cases show a trend towards"
}

async def enforce_suggestive_language(text: str) -> str:
    """
    Scans response text and replaces definitive advice with suggestive information.
    """
    processed_text = text
    for advice, suggestion in ADVICE_PHRASES.items():
        processed_text = processed_text.replace(advice, f"**{suggestion}**")
        processed_text = processed_text.replace(advice.capitalize(), f"**{suggestion.capitalize()}**")
    
    return processed_text
