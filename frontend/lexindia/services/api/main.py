from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from db.search import search_client
from db.vector import vector_db
from models import judgment, query, section, user, workflow  # noqa: F401
from routers import auth, citizen, court, documents, navigate, research, workflow
from services.bootstrap import initialize_persistence


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_persistence(seed_demo_data=settings.BOOTSTRAP_MODE and settings.BOOTSTRAP_DEMO_DATA)
    yield
    await search_client.close()
    await vector_db.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="LexIndia - AI-powered legal intelligence API for Indian law.",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(research.router, prefix=f"{settings.API_V1_STR}/research", tags=["research"])
app.include_router(documents.router, prefix=f"{settings.API_V1_STR}/documents", tags=["documents"])
app.include_router(navigate.router, prefix=f"{settings.API_V1_STR}/navigate", tags=["navigate"])
app.include_router(workflow.router, prefix=f"{settings.API_V1_STR}/workflow", tags=["workflow"])
app.include_router(court.router, prefix=f"{settings.API_V1_STR}/court", tags=["court"])

if settings.CITIZEN_PORTAL_ENABLED:
    app.include_router(citizen.router, prefix=f"{settings.API_V1_STR}/citizen", tags=["citizen"])


@app.get("/", tags=["meta"])
async def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "operational",
        "docs": "/docs",
    }


@app.get("/health", tags=["meta"])
async def health_check():
    return {"status": "ok"}
