# GPT (OpenAI) client

from backend.config import OPENAI_API_KEY
from backend.llm_clients.base import BaseLLMClient
 
 
class OpenAIClient(BaseLLMClient):
    name = "gpt"
 
    def _call_api(self, prompt: str) -> str:
        from openai import OpenAI
 
        client = OpenAI(api_key=OPENAI_API_KEY)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content
