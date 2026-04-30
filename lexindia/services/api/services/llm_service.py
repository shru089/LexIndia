import httpx
from config import settings
from typing import List, Dict, Optional

class LLMService:
    """
    Handles connections to Llama 3 via Ollama (Local) or Groq (Cloud Free Tier).
    """
    
    def __init__(self):
        self.provider = settings.LLM_PROVIDER
        self.ollama_url = f"{settings.OLLAMA_BASE_URL}/api/generate"
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

    async def generate_text(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        if self.provider == "ollama":
            return await self._call_ollama(prompt, system_prompt)
        elif self.provider == "groq":
            return await self._call_groq(prompt, system_prompt)
        elif self.provider == "gemini":
            return await self._call_gemini(prompt, system_prompt)
        else:
            return "Error: Invalid LLM Provider"

    async def call_llama(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Legacy method name, now aliases to generate_text"""
        return await self.generate_text(prompt, system_prompt)

    async def _call_gemini(self, prompt: str, system_prompt: str) -> str:
        if not settings.GEMINI_API_KEY:
            return "Error: Gemini API Key not configured"
            
        url = f"{self.gemini_url}?key={settings.GEMINI_API_KEY}"
        payload = {
            "contents": [{
                "parts": [{"text": f"{system_prompt}\n\nUser: {prompt}" if system_prompt else prompt}]
            }]
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload)
                data = response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                return f"Error connecting to Gemini: {str(e)}"

    async def _call_ollama(self, prompt: str, system_prompt: str) -> str:
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "system": system_prompt,
            "stream": False
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.ollama_url, json=payload, timeout=30.0)
                return response.json().get("response", "Error: No response from Ollama")
            except Exception as e:
                return f"Error connecting to local Ollama: {str(e)}"

    async def _call_groq(self, prompt: str, system_prompt: str) -> str:
        if not settings.GROQ_API_KEY:
            return "Error: Groq API Key not configured"
            
        headers = {"Authorization": f"Bearer {settings.GROQ_API_KEY}"}
        payload = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.groq_url, headers=headers, json=payload)
                return response.json()["choices"][0]["message"]["content"]
            except Exception as e:
                return f"Error connecting to Groq: {str(e)}"

llm_service = LLMService()
