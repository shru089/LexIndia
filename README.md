# LexIndia

LexIndia is a public-sector legal intelligence workspace for Indian law. It combines research search, statute translation, document intelligence, workflow tracking, and a JWT-backed identity layer in one demo-ready platform.

## Product Status

The active application now lives in:

- `lexindia/apps/web` for the Next.js command-center UI
- `lexindia/services/api` for the FastAPI backend

Archived legacy scaffolds now live in:

- `lexindia/archive/legacy-frontend`
- `lexindia/archive/legacy-backend`

## What Works

- JWT-backed account registration, login, and current-user lookup
- Persistent workflow records stored through the active database layer
- Research search backed by live legal records when available, with deterministic fallback data
- Structured legal scenario analysis for pitch and pilot walkthroughs
- Document brief generation, clause comparison, and OCR intake placeholders
- Court-watch, statute translation, and workflow endpoints with presentation-ready payloads
- A polished dashboard experience designed for government and institutional demos

## Architecture

```text
LexIndia/
|-- README.md
`-- lexindia/
    |-- apps/web/                    # Active Next.js frontend
    |-- services/api/                # Active FastAPI backend
    |-- services/ingestion/          # Ingestion workers
    |-- archive/                     # Retired scaffolds kept for reference
    |-- data/                        # Legal data and mappings
    |-- db/                          # Templates and static assets
    |-- infrastructure/              # Docker and infra files
    `-- scripts/                     # Utility scripts
```

## Identity And Persistence

LexIndia uses a local JWT identity provider inside the API:

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `POST /api/v1/auth/verify-bar-council`

On startup, the API now only creates the active schema. Demo data and admin seeding do not run automatically unless bootstrap is explicitly enabled.

### Bootstrap rules

- `BOOTSTRAP_MODE=true` is required before any admin user seeding can happen
- `BOOTSTRAP_DEMO_DATA=true` is required before demo judgments, sections, and workflow templates are seeded at startup
- `BOOTSTRAP_ADMIN_EMAIL` and `BOOTSTRAP_ADMIN_PASSWORD` must be provided explicitly if you want an admin account created

If `DATABASE_URL` is unavailable, the API will only fall back to `DATABASE_FALLBACK_URL` in development or test mode.

## Main API Surfaces

- `GET /health`
- `GET /api/v1/research/search`
- `POST /api/v1/research/analyze`
- `GET /api/v1/research/briefing`
- `GET /api/v1/documents/`
- `POST /api/v1/documents/brief`
- `POST /api/v1/documents/compare`
- `GET /api/v1/workflow/`
- `POST /api/v1/workflow/`
- `PATCH /api/v1/workflow/{workflow_id}`
- `POST /api/v1/workflow/citation-check`
- `GET /api/v1/court/`
- `GET /api/v1/navigate/`

## Local Development

### 1. Enter the active project

```powershell
cd lexindia
```

### 2. Prepare environment variables

Create:

- `services/api/.env`

You can start from:

- `.env.example`

### 3. Start infrastructure if you want the full local stack

```powershell
docker compose up
```

This can start:

- PostgreSQL
- Redis
- Qdrant
- Elasticsearch

In development mode, the API can still fall back to local SQLite if the primary database is unavailable.

### 4. Run the API

```powershell
cd services/api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API URL:

```text
http://localhost:8000
```

### 5. Optional explicit bootstrap

If you want seeded demo data and an admin account locally:

```powershell
$env:BOOTSTRAP_MODE='true'
$env:BOOTSTRAP_DEMO_DATA='true'
$env:BOOTSTRAP_ADMIN_EMAIL='admin@lexindia.in'
$env:BOOTSTRAP_ADMIN_PASSWORD='replace-this-password'
python scripts/bootstrap_db.py
```

### 6. Run the frontend

```powershell
cd apps/web
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

## Verification Commands

### API tests

```powershell
cd lexindia/services/api
C:\Users\admini\Desktop\LexIndia\venv\Scripts\python.exe -m unittest discover -s tests
```

The API tests use a dedicated disposable SQLite runtime database and do not rely on shared seeded state.

### Frontend checks

```powershell
cd lexindia/apps/web
cmd /c npm.cmd run lint
cmd /c npm.cmd run build
```

## Environment Notes

Important values include:

```env
APP_ENV=development
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/lex_db
DATABASE_FALLBACK_URL=./lexindia_local.db
ENABLE_DB_FALLBACK=true
REDIS_URL=redis://localhost:6379/0
QDRANT_URL=http://localhost:6333
ELASTICSEARCH_URL=http://localhost:9200
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
AUTH_JWT_SECRET=replace_with_a_long_random_secret
AUTH_JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=480
CORS_ALLOWED_ORIGINS=http://127.0.0.1:3000,http://localhost:3000
BOOTSTRAP_MODE=false
BOOTSTRAP_DEMO_DATA=false
BOOTSTRAP_ADMIN_EMAIL=
BOOTSTRAP_ADMIN_PASSWORD=
VOCAB_FILTER_ENABLED=true
AUDIT_LOG_ENABLED=true
DISCLAIMER_VERSION=v2
```

## Roadmap Priorities

- Replace local JWT auth with managed production identity and secret rotation controls
- Connect retrieval to a broader indexed corpus of judgments, statutes, and government circulars
- Expand workflow permissions, audit reporting, and multi-user collaboration
- Add frontend integration for authenticated sessions and workflow editing
- Remove the archived scaffold directories entirely once historical retention is no longer needed
