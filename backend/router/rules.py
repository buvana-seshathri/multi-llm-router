"""
Phase 1: Simple keyword-based routing
look for keywords in the prompt and map them to 
the model best suited for that kind of task.
"""

from backend.config import DEFAULT_MODEL
from backend.models import RouteDecision

# Ordered list of (keywords, model, reason). First match wins.
RULES = [
    (["code", "function", "bug", "debug", "python", "javascript", "refactor"],
     "claude", "Prompt mentions coding — Claude handles code well."),

    (["resume", "cv", "cover letter", "job application"],
     "claude", "Prompt is about resume/career writing — Claude is strong here."),

    (["summarize", "summary", "explain simply", "tl;dr"],
     "groq", "Short summarization task — routed to fast model."),

    (["research", "compare", "pros and cons", "analyze"],
     "gemini", "Prompt needs broader research/analysis — routed to Gemini."),

    (["quick", "simple question", "what is", "define"],
     "gpt", "Quick/simple question — routed to GPT."),
]


def route_by_rules(prompt: str) -> RouteDecision:
    lowered = prompt.lower()

    # check for keyword match
    for keywords, model, reason in RULES:
        if any(keyword in lowered for keyword in keywords):
            return RouteDecision(model=model, reason=reason, method="rules")

    # fallback to default model if not match
    return RouteDecision(
        model=DEFAULT_MODEL,
        reason="No keyword matched — falling back to default model.",
        method="rules",
    )
