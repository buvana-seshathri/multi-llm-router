"""Common interface for all LLM clients.

Every client (Claude, GPT, Gemini, Groq) implements generate(prompt) -> str and _call_api.
"""

from backend.config import USE_REAL_APIS


class BaseLLMClient:
    name = "base"

    def generate(self, prompt: str) -> str:
        # set to false in Phase 1 - check if mock_response works
        if USE_REAL_APIS: 
            return self._call_api(prompt)
        return self._mock_response(prompt)

    def _call_api(self, prompt: str) -> str:
        raise NotImplementedError

    def _mock_response(self, prompt: str) -> str:
        return f"[mocked {self.name} response] You asked: \"{prompt[:80]}\""
