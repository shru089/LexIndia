from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Core
    PROJECT_NAME: str = "LexIndia"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/lex_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    QDRANT_URL: str = "http://localhost:6333"
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    
    # AI
    LLM_PROVIDER: str = "ollama"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    GROQ_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    EMBEDDING_MODEL: str = "multilingual-e5-large"
    
    # Storage
    AWS_REGION: str = "ap-south-1"
    S3_BUCKET_NAME: str = "lex-documents"
    
    # Auth
    SUPABASE_URL: Optional[str] = None
    SUPABASE_ANON_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
