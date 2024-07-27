from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TITLE: str = "Eather"
    PROJECT_NAME: str
    DATABASE_URI: str
    ACCESS_TOKEN_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str
    REFRESH_TOKEN_SECRET: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
