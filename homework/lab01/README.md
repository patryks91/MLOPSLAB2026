# Sentiment Analysis API

## Run locally

Run from `homework/lab01`:

```bash
uv sync
uv run uvicorn app:app --port 8000
```

Open http://localhost:8000/docs to try the API.

## Tests

Tests cover input validation, model loading, inference and API responses.

```bash
uv run pytest -v
```

## Docker

```bash
docker compose up --build
```

The API is available at http://localhost:8000/docs.

Stop with Ctrl+C, then run:

```bash
docker compose down
```