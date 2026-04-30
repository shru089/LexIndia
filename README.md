# LexIndia

LexIndia is an AI-assisted legal research platform focused on Indian law. It combines hybrid search, structured legal workflows, and a modern web interface to help legal professionals explore statutes, judgments, and document intelligence features more efficiently.

## Current Status

This repository is an active project scaffold and early product build.

- The main application code lives inside `lexindia/`
- The backend API is built with FastAPI
- The web app is built with Next.js
- Docker Compose is available for local infrastructure services
- Some modules are still placeholder implementations and need further production hardening

## Repository Layout

```text
LexIndia/
|-- README.md
`-- lexindia/
    |-- apps/web/              # Active Next.js frontend
    |-- services/api/          # Active FastAPI backend
    |-- services/ingestion/    # Ingestion workers
    |-- backend/               # Older backend scaffold kept in repo
    |-- frontend/              # Older frontend scaffold kept in repo
    |-- data/                  # Legal data and mappings
    |-- db/                    # Templates and static DB assets
    |-- infrastructure/        # Docker and infra files
    `-- scripts/               # Setup and utility scripts
```

## Core Features

- Hybrid legal search using keyword search plus vector search
- Legal research assistant workflows
- Document brief generation and comparison
- Safety-oriented response framing for legal information use
- Modular architecture for future workflow, court, and citizen-facing features

## Tech Stack

### Backend

- Python
- FastAPI
- PostgreSQL
- Redis
- Qdrant
- Elasticsearch

### Frontend

- Next.js
- React
- TypeScript

### Infrastructure

- Docker Compose

## Local Development

### 1. Go to the project directory

```powershell
cd lexindia
```

### 2. Prepare environment variables

Create:

- `services/api/.env`

You can start from:

- `lexindia/.env.example`

### 3. Start infrastructure with Docker

```powershell
docker compose up
```

This starts:

- PostgreSQL
- Redis
- Qdrant
- Elasticsearch

### 4. Run the API locally

```powershell
cd services/api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API default URL:

```text
http://localhost:8000
```

### 5. Run the web app locally

```powershell
cd apps/web
npm install
npm run dev
```

Web app default URL:

```text
http://localhost:3000
```

## Important Environment Values

The API currently expects values such as:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/lex_db
REDIS_URL=redis://localhost:6379/0
QDRANT_URL=http://localhost:6333
ELASTICSEARCH_URL=http://localhost:9200
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
SUPABASE_URL=
SUPABASE_ANON_KEY=
ALLOW_DEMO_AUTH=false
VOCAB_FILTER_ENABLED=true
AUDIT_LOG_ENABLED=true
DISCLAIMER_VERSION=v2
```

## Notes

- Do not commit local `.env` files
- Do not commit `node_modules`, `.next`, `venv`, or `__pycache__`
- Some directories reflect older scaffolding and may be consolidated later
- This project is intended as a legal information tool, not a substitute for professional legal advice

## Roadmap Direction

- Improve retrieval quality and result normalization
- Replace placeholder auth and verification flows
- Add tests for API routes and search behavior
- Consolidate duplicate legacy folders
- Harden deployment and compliance workflows

## License

This repository is currently proprietary unless you decide otherwise.
