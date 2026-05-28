from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Core
    PROJECT_NAME: str = "LexIndia"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    APP_ENV: str = "development"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/lex_db"
    DATABASE_FALLBACK_URL: str = "./lexindia_local.db"
    ENABLE_DB_FALLBACK: bool = True
    REDIS_URL: str = "redis://localhost:6379/0"
    QDRANT_URL: str = "http://localhost:6333"
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    TEST_DATABASE_URL: str = "./lexindia_test.db"

    # AI
    LLM_PROVIDER: str = "ollama"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    GROQ_API_KEY: Optional[str] = None
    GEMINI_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    LLAMA_MODEL_PATH: str = "./models/"
    EMBEDDING_MODEL: str = "multilingual-e5-large"

    # Storage
    AWS_REGION: str = "ap-south-1"
    S3_BUCKET_NAME: str = "nyaya-documents"

    # Auth
    SUPABASE_URL: Optional[str] = None
    SUPABASE_ANON_KEY: Optional[str] = None
    AUTH_JWT_SECRET: str = "change-this-lexindia-secret"
    AUTH_JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480
    ALLOW_DEMO_AUTH: bool = False
    CORS_ALLOWED_ORIGINS: str = "http://127.0.0.1:3000,http://localhost:3000"

    # Bootstrap
    BOOTSTRAP_MODE: bool = False
    BOOTSTRAP_DEMO_DATA: bool = False
    BOOTSTRAP_ADMIN_EMAIL: Optional[str] = None
    BOOTSTRAP_ADMIN_PASSWORD: Optional[str] = None
    BOOTSTRAP_ADMIN_NAME: str = "LexIndia Administrator"

    # Safety
    VOCAB_FILTER_ENABLED: bool = True
    AUDIT_LOG_ENABLED: bool = True
    DISCLAIMER_VERSION: str = "v2"

    # Feature flags
    CITIZEN_PORTAL_ENABLED: bool = False
    MARKETPLACE_ENABLED: bool = False

    @property
    def is_dev(self) -> bool:
        return self.APP_ENV.lower() in {"development", "dev", "local"}

    @property
    def is_test(self) -> bool:
        return self.APP_ENV.lower() == "test"

    @property
    def cors_allowed_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ALLOWED_ORIGINS.split(",") if origin.strip()]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
