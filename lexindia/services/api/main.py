from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import auth, research, documents, navigate, workflow, court, citizen

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="LexIndia — AI-powered legal intelligence API for Indian law.",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ---------------------------------------------------------------------------
# CORS
# NOTE: In production, replace ["*"] with your exact frontend origin(s).
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(auth.router,       prefix=f"{settings.API_V1_STR}/auth",      tags=["auth"])
app.include_router(research.router,   prefix=f"{settings.API_V1_STR}/research",  tags=["research"])
app.include_router(documents.router,  prefix=f"{settings.API_V1_STR}/documents", tags=["documents"])
app.include_router(navigate.router,   prefix=f"{settings.API_V1_STR}/navigate",  tags=["navigate"])
app.include_router(workflow.router,   prefix=f"{settings.API_V1_STR}/workflow",  tags=["workflow"])
app.include_router(court.router,      prefix=f"{settings.API_V1_STR}/court",     tags=["court"])

if settings.CITIZEN_PORTAL_ENABLED:
    app.include_router(citizen.router, prefix=f"{settings.API_V1_STR}/citizen", tags=["citizen"])


# ---------------------------------------------------------------------------
# Root & Health
# ---------------------------------------------------------------------------
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
    """Liveness probe — returns 200 if the API process is up."""
    return {"status": "ok"}
