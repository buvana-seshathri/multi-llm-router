# Gemini (Google) client

from backend.config import GEMINI_API_KEY
from backend.llm_clients.base import BaseLLMClient


class GeminiClient(BaseLLMClient):
    name = "gemini"

    def _call_api(self, prompt: str) -> str:
        import google.generativeai as genai

        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content(prompt)
        return result.text
