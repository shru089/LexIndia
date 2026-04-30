from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import auth, research, documents, navigate, workflow, court, citizen

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific origins
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

@app.get("/")
async def root():
    return {"message": "Welcome to Nyaya.AI API", "status": "operational"}
