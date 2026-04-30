import httpx
from config import settings
from typing import Optional

class LLMService:
    def __init__(self):
        self.provider = settings.LLM_PROVIDER
        self.ollama_url = f"{settings.OLLAMA_BASE_URL}/api/generate"
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"

    async def call_llama(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        if self.provider == "ollama":
            payload = {"model": "llama3", "prompt": prompt, "system": system_prompt, "stream": False}
            async with httpx.AsyncClient() as client:
                response = await client.post(self.ollama_url, json=payload, timeout=30.0)
                return response.json().get("response", "Error")
        # Groq implementation logic here...
        return "Service Ready"

llm_service = LLMService()
