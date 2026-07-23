"""Request/response schemas shared across the app."""

from pydantic import BaseModel


class TaskRequest(BaseModel):
    prompt: str


class RouteDecision(BaseModel):
    model: str          # e.g. "claude", "gpt", "gemini", "groq"
    reason: str          # human-readable explanation of why this model was picked
    method: str           # "rules" or "classifier"


class TaskResponse(BaseModel):
    decision: RouteDecision
    response: str
