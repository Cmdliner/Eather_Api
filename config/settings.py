from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Eather"
    DATABASE_URI: str
    CORS_ORIGIN: str
    ACCESS_TOKEN_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str
    REFRESH_TOKEN_SECRET: str
    REFRESH_TOKEN_EXPIRE_DAYS: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()