# LexIndia — Legal Intelligence Platform for India

> **"Your AI Research Associate, Trained on Indian Law"**  
> Semantic legal research · Case intelligence · Document analysis · For legal professionals.

---

## What is Nyaya.AI?

Nyaya.AI is a B2B AI legal research platform built exclusively for Indian legal professionals. It combines a large structured database of Indian court judgments with a retrieval-augmented generation (RAG) pipeline to help advocates, law firms, and corporate legal teams research faster, cite accurately, and never miss a precedent.

It is **not** a legal advice platform. Every output is framed as research information for a licensed professional's independent use.

---

## Architecture at a Glance

```
User Query (natural language / Hinglish)
        │
        ▼
┌─────────────────────┐
│  Intent Classifier  │  ← separates info queries from advice queries
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐     ┌──────────────────────────┐
│  Hybrid Search      │────▶│  Vector Store (Qdrant)   │
│  (keyword + vector) │     │  50M+ judgment embeddings│
└────────┬────────────┘     └──────────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Re-ranking Layer   │  ← authority, recency, jurisdiction filters
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  LLM Generation     │  ← Llama 3 / GPT-4o, legal fine-tuned
│  (RAG-grounded)     │  ← citation-first, no hallucination
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Safety Layer       │  ← vocabulary blocklist, disclaimer injector
│  + Audit Logger     │  ← every query logged with sources served
└────────┬────────────┘
         │
         ▼
    Response to user
    (sources cited before synthesis)
```

---

## The Six Modules

| Module | What it does |
|---|---|
| **1. Document Intelligence** | Upload judgments / case bundles → auto-brief, cross-doc Q&A, contradiction detection |
| **2. Legal Research Assistant** | Natural language search → statutes + precedents + BNS/IPC mapper |
| **3. Knowledge Navigation** | Browse by practice area, statutory cross-reference, daily legal radar |
| **4. Workflow Integration** | Draft enhancement, citation validator, research memo generator |
| **5. Court & Practice Management** | Court procedure navigator, cause list, judge citation patterns |
| **6. Citizen Portal (Safe Mode)** | Info-only with mandatory lawyer handoff — no advice language |

---

## Tech Stack

### Backend
| Layer | Technology |
|---|---|
| API framework | Python — FastAPI (async) |
| Auth | Supabase Auth (OTP + Bar Council verification) |
| Primary DB | PostgreSQL (RDS, ap-south-1) |
| Vector DB | Qdrant (self-hosted, Mumbai) |
| Full-text search | Elasticsearch |
| Queue / async jobs | Celery + Redis |
| File storage | AWS S3 (ap-south-1) |
| AI inference | Llama 3 (self-hosted) + GPT-4o fallback |
| Embedding model | multilingual-e5-large |
| Document generation | Jinja2 + python-docx + WeasyPrint |

### Frontend
| Layer | Technology |
|---|---|
| Web app | Next.js 14 (App Router, SSR) |
| Mobile | Flutter (iOS + Android) |
| UI library | Stitch (primary) + Radix UI primitives |
| Styling | Tailwind CSS |
| State management | Zustand |
| API client | TanStack Query |

### Infrastructure
| Layer | Technology |
|---|---|
| Hosting | AWS ap-south-1 (data residency — DPDP compliance) |
| CDN | Cloudflare |
| Monitoring | Datadog + Sentry |
| CI/CD | GitHub Actions |
| Containers | Docker + ECS Fargate |

---

## Design System

**Palette — Option C: Monochrome + Teal signal**

```
Background:   #0F0F0F (near-black) / #F7F7F7 (off-white)
Surface:      #1A1A1A / #EFEFEF
Border:       #2A2A2A / #E5E5E5
Text primary: #F7F7F7 / #0F0F0F
Text muted:   #777777 / #777777
AI signal:    #00897B (teal — interactive + AI elements only)
AI tint:      #E0F2F0
Error:        #E24B4A
Warning:      #BA7517
Success:      #1D9E75
```

**Design principles:**
- Minimal + glassmorphism hybrid — frosted glass cards on dark backgrounds
- Teal used exclusively for AI-generated content and interactive elements
- No color noise — maximum 2 accent colors on any screen
- Every AI response visually distinct from human UI chrome

---

## Project Structure

```
nyaya-ai/
│
├── apps/
│   ├── web/                          # Next.js 14 web app
│   │   ├── app/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   └── verify/
│   │   │   ├── (dashboard)/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── research/         # Module 2 — Legal Research
│   │   │   │   ├── documents/        # Module 1 — Document Intelligence
│   │   │   │   ├── navigate/         # Module 3 — Knowledge Navigation
│   │   │   │   ├── workflow/         # Module 4 — Workflow Integration
│   │   │   │   ├── court/            # Module 5 — Court Management
│   │   │   │   └── citizen/          # Module 6 — Citizen Portal
│   │   │   ├── api/                  # Next.js API routes (BFF layer)
│   │   │   └── globals.css
│   │   ├── components/
│   │   │   ├── ui/                   # Stitch + Radix primitives
│   │   │   ├── research/             # Research-specific components
│   │   │   ├── documents/            # Document upload / viewer
│   │   │   ├── chat/                 # AI chat interface
│   │   │   └── shared/               # Layout, Nav, Disclaimer blocks
│   │   ├── lib/
│   │   │   ├── api.ts                # API client
│   │   │   ├── auth.ts
│   │   │   └── constants.ts
│   │   └── public/
│   │
│   └── mobile/                       # Flutter app
│       ├── lib/
│       │   ├── main.dart
│       │   ├── screens/
│       │   ├── widgets/
│       │   └── services/
│       └── pubspec.yaml
│
├── services/
│   │
│   ├── api/                          # Core FastAPI backend
│   │   ├── main.py
│   │   ├── routers/
│   │   │   ├── research.py           # /research endpoints
│   │   │   ├── documents.py          # /documents endpoints
│   │   │   ├── navigate.py           # /navigate endpoints
│   │   │   ├── workflow.py           # /workflow endpoints
│   │   │   ├── court.py              # /court endpoints
│   │   │   ├── citizen.py            # /citizen endpoints
│   │   │   └── auth.py               # /auth endpoints
│   │   ├── models/
│   │   │   ├── judgment.py
│   │   │   ├── section.py
│   │   │   ├── user.py
│   │   │   └── query.py
│   │   ├── services/
│   │   │   ├── rag/
│   │   │   │   ├── retriever.py      # Hybrid search (vector + keyword)
│   │   │   │   ├── reranker.py       # Cross-encoder reranking
│   │   │   │   ├── generator.py      # LLM generation + citation grounding
│   │   │   │   └── validator.py      # Post-generation citation check
│   │   │   ├── safety/
│   │   │   │   ├── intent_classifier.py   # Info vs advice detection
│   │   │   │   ├── vocab_filter.py        # Directive language blocklist
│   │   │   │   ├── disclaimer_injector.py
│   │   │   │   └── audit_logger.py
│   │   │   ├── documents/
│   │   │   │   ├── ocr.py            # Tesseract + layout detection
│   │   │   │   ├── parser.py         # Judgment structure extraction
│   │   │   │   ├── comparator.py     # Multi-doc contradiction detection
│   │   │   │   └── brief_generator.py
│   │   │   └── workflow/
│   │   │       ├── citation_checker.py
│   │   │       ├── memo_generator.py
│   │   │       └── draft_enhancer.py
│   │   ├── db/
│   │   │   ├── postgres.py           # PostgreSQL client
│   │   │   ├── vector.py             # Qdrant client
│   │   │   ├── search.py             # Elasticsearch client
│   │   │   └── migrations/
│   │   └── config.py
│   │
│   ├── ingestion/                    # Data pipeline (Celery workers)
│   │   ├── workers/
│   │   │   ├── crawler.py            # eCourts / SCI / HC portal crawlers
│   │   │   ├── ocr_worker.py
│   │   │   ├── extractor.py          # Metadata + section extraction
│   │   │   ├── embedder.py           # Chunk + embed + store
│   │   │   └── legislation_monitor.py # Gazette + PRS feeds
│   │   ├── parsers/
│   │   │   ├── ecourts.py
│   │   │   ├── sci.py                # Supreme Court portal
│   │   │   ├── high_courts/
│   │   │   │   ├── bombay.py
│   │   │   │   ├── delhi.py
│   │   │   │   ├── madras.py
│   │   │   │   └── ...               # All 25 HCs
│   │   │   └── gazette.py
│   │   └── schema/
│   │       ├── section_map.json      # BNS ↔ IPC / BNSS ↔ CrPC mapping
│   │       └── act_taxonomy.json     # Legal act hierarchy
│   │
│   └── ml/                           # Model training + evaluation
│       ├── fine_tuning/
│       │   ├── dataset_builder.py
│       │   ├── train.py              # Llama 3 legal fine-tuning
│       │   └── eval.py               # Accuracy benchmarks
│       ├── embeddings/
│       │   ├── embed_pipeline.py
│       │   └── batch_embed.py
│       └── evals/
│           ├── citation_accuracy.py  # Target: >99%
│           ├── section_id_accuracy.py
│           └── hallucination_rate.py
│
├── data/
│   ├── legal/
│   │   ├── section_maps/
│   │   │   ├── ipc_to_bns.json       # CRITICAL — build before anything else
│   │   │   ├── crpc_to_bnss.json
│   │   │   └── evidence_act_to_bsa.json
│   │   ├── act_taxonomy/
│   │   └── court_hierarchy/
│   └── templates/
│       ├── affidavit.jinja2
│       ├── legal_notice.jinja2
│       ├── consumer_complaint.jinja2
│       └── research_memo.jinja2
│
├── infrastructure/
│   ├── terraform/                    # AWS infrastructure as code
│   │   ├── main.tf
│   │   ├── rds.tf
│   │   ├── ecs.tf
│   │   ├── s3.tf
│   │   └── cloudfront.tf
│   ├── docker/
│   │   ├── Dockerfile.api
│   │   ├── Dockerfile.ingestion
│   │   └── docker-compose.yml
│   └── k8s/                          # Kubernetes manifests (scale phase)
│
├── docs/
│   ├── PRD_v2.docx                   # Full product requirements
│   ├── legal/
│   │   ├── senior_advocate_opinion.pdf    # BLOCKING — get before launch
│   │   ├── dpdp_compliance_audit.pdf
│   │   └── ip_counsel_data_pipeline.pdf
│   ├── api/                          # OpenAPI specs
│   └── architecture/
│
├── scripts/
│   ├── bootstrap_db.py               # Initial DB setup + seed
│   ├── seed_section_maps.py          # Load BNS/BNSS maps
│   └── run_evals.py
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy_staging.yml
│       └── deploy_prod.yml
│
├── .env.example
├── docker-compose.yml
└── README.md                         # This file
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+
- Docker + Docker Compose
- AWS CLI configured (ap-south-1)
- PostgreSQL 15
- Redis 7

### Local Development

```bash
# Clone
git clone https://github.com/your-org/nyaya-ai
cd nyaya-ai

# Backend
cd services/api
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # fill in your keys
python scripts/bootstrap_db.py
uvicorn main:app --reload

# Frontend
cd apps/web
npm install
npm run dev

# Ingestion workers (separate terminal)
cd services/ingestion
celery -A workers worker --loglevel=info

# Full stack via Docker
docker-compose up
```

### Environment Variables

```bash
# Core
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
QDRANT_URL=http://localhost:6333
ELASTICSEARCH_URL=http://localhost:9200

# AI
OPENAI_API_KEY=...              # GPT-4o fallback
LLAMA_MODEL_PATH=./models/      # Self-hosted Llama 3

# Storage
AWS_REGION=ap-south-1
S3_BUCKET_NAME=nyaya-documents

# Auth
SUPABASE_URL=...
SUPABASE_ANON_KEY=...

# Safety
VOCAB_FILTER_ENABLED=true
AUDIT_LOG_ENABLED=true
DISCLAIMER_VERSION=v2

# Feature flags
CITIZEN_PORTAL_ENABLED=false    # Off until B2B is stable
MARKETPLACE_ENABLED=false       # Phase 2
```

---

## Legal Safety — Non-Negotiable Checklist

Before any public deployment, the following must be complete:

- [ ] Senior Advocate opinion letter — confirms platform does not constitute legal practice under Advocates Act 1961
- [ ] IPC → BNS / CrPC → BNSS section mapping table — complete and validated
- [ ] IP counsel sign-off on data ingestion pipeline
- [ ] DPO appointed — DPDP Act 2023 compliance
- [ ] Bar Council advisor onboarded (minimum 1 before beta)
- [ ] Vocabulary blocklist tested against 500+ directive phrase variants
- [ ] Disclaimer version locked and displayed in all 12 supported languages
- [ ] All AI outputs audit-logged (immutable, 2-year retention)
- [ ] ToS reviewed by tech law firm — "research tool, not legal advisor" framing

---

## Key Design Decisions

### Why RAG over fine-tuning only?
Fine-tuned models hallucinate citations. RAG with a closed knowledge base means the AI can only cite cases that exist in the database. Every claim is verifiable. This is the core accuracy guarantee.

### Why Qdrant self-hosted over Pinecone?
Data residency. All PII and legal queries must stay in AWS ap-south-1 under DPDP Act. Managed vector DBs with US-based infrastructure fail this requirement.

### Why Llama 3 self-hosted over GPT-4o as primary?
Same reason — data residency. Sensitive legal queries (criminal charges, domestic matters) should not traverse OpenAI's infrastructure. GPT-4o is available as a fallback for non-sensitive research queries where the user consents.

### Why B2B first?
The Bombay HC December 2025 ruling makes standalone citizen AI legally risky. B2B positions the platform as a tool for licensed professionals, which is explicitly safe under the Advocates Act. Citizen portal opens in Phase 2 with mandatory lawyer handoff architecture.

### Why "suggestion language" not "advice language"?
The legal distinction between information and advice is the core compliance mechanism. The AI presents what courts have done, what sections apply, and what patterns exist — never what the user should do. This mirrors how legal information services, law review articles, and NALSA pamphlets operate — all of which are explicitly lawful.

---

## Roadmap

| Stage | Theme | Key Deliverables |
|---|---|---|
| Stage 1 (M1–4) | Foundation | Core RAG pipeline, 100K judgments, Modules 1–2, web app, 10 beta firms |
| Stage 2 (M5–9) | Research depth | Modules 3–4, 500K judgments, Hindi + Tamil, 100 firms, paid subscriptions |
| Stage 3 (M10–15) | Practice management | Module 5, 1M judgments, all 25 HCs, 500 firms, marketplace |
| Stage 4 (M16–24) | Scale | Citizen portal (Safe Mode), 2M+ judgments, B2G pilots, multilingual |

---

## Spec Gaps & Open Questions

| # | Issue | Status |
|---|---|---|
| OQ-01 | SCC Online / Manupatra listed as sources — need licensing agreements or remove | Blocking |
| OQ-02 | Rs. 15,000/month solo tier may be too high for district court advocates | Validate pre-launch |
| OQ-03 | Judge tendency profiling (Feature 5.2) needs legal review — potential sub judice concerns | Legal review needed |
| OQ-04 | E-filing (Feature 5.3) requires eCourts integration agreements | Government BD needed |
| OQ-05 | Offline / low-bandwidth mode not specified — district court lawyers in Tier 2/3 need this | Add to backlog |
| OQ-06 | Infrastructure cost per query estimated Rs. 5–10 — likely underestimated at RAG + LLM scale | Re-estimate before pricing |

---

## Contributing

This is a private repository. Internal team only during Stage 1.

Code review requirements:
- All safety layer changes require sign-off from Legal + CTO
- Vocabulary filter updates require regression test against 500-phrase test suite
- Any change to disclaimer injection requires legal team approval
- Data pipeline changes require IP counsel review if new sources are added

---

## License

Proprietary. All rights reserved. © 2025 Nyaya.AI Technologies Pvt. Ltd.

---

*Built for India's 1.5 million advocates. By people who believe access to legal knowledge is a right, not a privilege.*
#   L e x I n d i a  
 