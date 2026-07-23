"""FastAPI app: routes a task to the right LLM and returns its response."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from backend.history import load_history, log_entry
from backend.llm_clients import CLIENTS
from backend.models import TaskRequest, TaskResponse
from backend.router.rules import route_by_rules

app = FastAPI(title="Multi-LLM Task Router")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")


@app.post("/api/route", response_model=TaskResponse)
def route_task(task: TaskRequest) -> TaskResponse:
    decision = route_by_rules(task.prompt)

    client = CLIENTS[decision.model]
    response_text = client.generate(task.prompt)

    log_entry(task.prompt, decision.model, decision.reason, decision.method)

    return TaskResponse(decision=decision, response=response_text)


@app.get("/api/history")
def get_history():
    return load_history()


# Serve the simple frontend
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
