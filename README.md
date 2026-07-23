# Multi-LLM Task Router

Routes a task to the best-fit LLM (Claude, GPT, Gemini, Groq) based on
simple rules today, with a lightweight classifier planned for Phase 3.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Run (Phase 1 — mocked responses, no API keys needed)

```bash
uvicorn backend.main:app --reload
```

Open http://localhost:8000 in your browser, type a task, and click
"Route Task". You'll see which model it picked, why, and a mocked
response.

## Phases

- **Phase 1 (current):** Rule-based routing + mocked LLM responses.
- **Phase 2:** Real API calls. Fill in `.env` with your keys and set
  `USE_REAL_APIS=true`.
- **Phase 3:** Add a lightweight classifier (`backend/router/classifier.py`)
  trained on example prompts, as an alternative/fallback to the rules.
- **Phase 4:** Show routing history in the UI (backend already logs it
  to `backend/history_log.json` via `/api/history`).

## Project layout

```
backend/
  main.py              FastAPI app + routes
  config.py             model registry, env config
  models.py             request/response schemas
  history.py             JSON-file log of past routes
  router/
    rules.py             keyword-based routing (Phase 1)
    classifier.py         ML-based routing (Phase 3)
  llm_clients/
    base.py               shared client interface
    claude_client.py
    openai_client.py
    gemini_client.py
    groq_client.py
frontend/
  index.html
  style.css
  app.js
```

## How routing works (Phase 1)

`backend/router/rules.py` checks the prompt for keywords and picks a
model:

| Keywords | Model | Why |
|---|---|---|
| code, function, bug, debug, python, javascript, refactor | Claude | strong at code |
| resume, cv, cover letter, job application | Claude | strong at writing |
| summarize, summary, tl;dr | Groq | fast, short-task model |
| research, compare, pros and cons, analyze | Gemini | broader analysis |
| quick, simple question, what is, define | GPT | fast general Q&A |
| (no match) | GPT | default fallback |

Edit the `RULES` list in that file to change behavior.
