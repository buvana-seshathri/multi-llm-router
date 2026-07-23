# Claude (Anthropic) client

from backend.config import ANTHROPIC_API_KEY
from backend.llm_clients.base import BaseLLMClient
 
 
class ClaudeClient(BaseLLMClient):
    name = "claude"
 
    def _call_api(self, prompt: str) -> str:
        import anthropic
 
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
