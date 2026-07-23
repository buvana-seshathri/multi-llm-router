from backend.llm_clients.claude_client import ClaudeClient
from backend.llm_clients.gemini_client import GeminiClient
from backend.llm_clients.groq_client import GroqClient
from backend.llm_clients.openai_client import OpenAIClient

# Maps the model key used everywhere else in the app to a client instance.
CLIENTS = {
    "claude": ClaudeClient(),
    "gpt": OpenAIClient(),
    "gemini": GeminiClient(),
    "groq": GroqClient(),
}
