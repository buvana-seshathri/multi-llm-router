"""Central place for model registry and environment config."""

import os

# Which model key maps to which client + human description.
MODEL_REGISTRY = {
    "claude": {
        "label": "Claude (Anthropic)",
        "good_for": "code, resumes/writing, reasoning-heavy tasks",
    },
    "gpt": {
        "label": "GPT (OpenAI)",
        "good_for": "quick general questions, brainstorming",
    },
    "gemini": {
        "label": "Gemini (Google)",
        "good_for": "multimodal or research-style questions",
    },
    "groq": {
        "label": "Groq (fast open models)",
        "good_for": "simple/short tasks needing a fast answer",
    },
}

DEFAULT_MODEL = "groq" # default made grop - bcz high token limit

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

USE_REAL_APIS = os.getenv("USE_REAL_APIS", "false").lower() == "true"
