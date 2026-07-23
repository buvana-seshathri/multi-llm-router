# Groq client

from backend.config import GROQ_API_KEY
from backend.llm_clients.base import BaseLLMClient


class GroqClient(BaseLLMClient):
    name = "groq"

    def _call_api(self, prompt: str) -> str:
        from groq import Groq

        client = Groq(api_key=GROQ_API_KEY)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content
