from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Quiz App Backend"
    ENVIRONMENT: str = "dev"

    class Config:
        env_file: str = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
