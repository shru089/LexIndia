from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from database import engine, Base
from routers import cases, chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lex India API")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cases.router, prefix="/api/v1/cases", tags=["cases"])
app.include_router(chat.router, prefix="/api/v1/ai/chat", tags=["chat"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Lex India API"}
