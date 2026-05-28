from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import cases, chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lex India API")

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
